/** Side panel UI. Talks to background.js over a long-lived port; renders whatever state it is sent. */
const port = chrome.runtime.connect({ name: 'panel' });
const $ = (id) => document.getElementById(id);
let state = null;
let logRenderedLen = -1;

const cmd = (type, extra = {}) => port.postMessage({ type, ...extra });

port.onMessage.addListener((msg) => {
  if (msg.type === 'STATE') {
    state = msg.state;
    render();
  } else if (msg.type === 'DEBUG_REPORT') {
    renderDebug(msg.report, msg.url);
  }
});
port.onDisconnect.addListener(() => {
  $('runStatus').textContent = 'disconnected';
  $('runStatus').className = 'pill stopped';
});

// ---------- rendering ----------
function render() {
  if (editingId && state.queue.some((i) => i.id === editingId)) return renderLogOnly();
  const { queue, run, settings, log } = state;
  const total = queue.length;
  const done = queue.filter((i) => i.status === 'done').length;
  const failed = queue.filter((i) => i.status === 'failed').length;
  const pending = queue.filter((i) => i.status === 'pending').length;

  const pill = $('runStatus');
  pill.textContent =
    run.status === 'stopped' && run.stopReason && run.stopReason !== 'user'
      ? `stopped: ${run.stopReason}`
      : run.status;
  pill.className = 'pill ' + run.status;

  $('progressBar').style.width = total ? `${Math.round(((done + failed) / total) * 100)}%` : '0';
  $('progressText').textContent =
    `${done + failed} / ${total} finished · ${done} done · ${failed} failed · ${pending} pending` +
    (run.phase === 'delay' && run.nextAt
      ? ` · next in ${Math.max(0, Math.round((run.nextAt - Date.now()) / 1000))}s`
      : '');

  const running = run.status === 'running';
  const paused = run.status === 'paused';
  $('btnStart').disabled = running || paused || pending === 0;
  $('btnPause').disabled = !running;
  $('btnResume').disabled = !paused;
  $('btnStop').disabled = !running && !paused;

  const notice = $('stopNotice');
  if (run.status === 'stopped' && run.stopReason === 'quota') {
    notice.hidden = false;
    notice.textContent =
      'Stopped: Flow reported a quota, rate limit or credit message. Progress is saved. Check your Flow account, then press Start to continue from the first unfinished prompt.';
  } else notice.hidden = true;

  // queue
  $('queueCount').textContent = total;
  const list = $('queue');
  const tpl = $('queueItem');
  list.replaceChildren(
    ...queue.map((it, i) => {
      const li = tpl.content.firstElementChild.cloneNode(true);
      li.dataset.id = it.id;
      li.dataset.status = it.status;
      li.querySelector('.status').textContent = it.status;
      li.querySelector('.idx').textContent = `${i + 1}.`;
      li.querySelector('.text').textContent = it.text;
      li.querySelector('.err').textContent = it.error
        ? `${it.error}${it.attempts > 1 ? ` (${it.attempts} attempts)` : ''}`
        : '';
      const busy = it.status === 'running';
      for (const b of li.querySelectorAll('button')) b.disabled = busy;
      return li;
    }),
  );

  // settings (do not overwrite a field the user is typing in)
  for (const key of ['minDelaySec', 'maxDelaySec', 'timeoutSec', 'retries', 'prefix', 'suffix']) {
    const el = $(key);
    if (document.activeElement !== el) el.value = settings[key] ?? '';
  }
  $('autoDownload').checked = !!settings.autoDownload;

  // log (append only when it changed)
  if (log.length !== logRenderedLen) {
    logRenderedLen = log.length;
    const ol = $('log');
    ol.replaceChildren(...log.slice(-200).map(logLine));
    ol.scrollTop = ol.scrollHeight;
  }
}

function renderLogOnly() {
  const ol = $('log');
  const log = state.log;
  if (log.length === logRenderedLen) return;
  logRenderedLen = log.length;
  ol.replaceChildren(...log.slice(-200).map(logLine));
  ol.scrollTop = ol.scrollHeight;
}

function logLine(e) {
  const li = document.createElement('li');
  li.className = e.level;
  const t = new Date(e.t).toLocaleTimeString();
  li.textContent = `${t} ${e.index != null && e.index >= 0 ? `#${e.index + 1} ` : ''}${e.message}`;
  return li;
}

function renderDebug(report, url) {
  const out = $('debugOut');
  out.hidden = false;
  const lines = [
    `Page: ${url}`,
    `Project page: ${report.chosen.isProjectPage ? 'yes' : 'NO (open a project first)'}`,
    '',
  ];
  for (const [group, rows] of Object.entries(report.groups)) {
    const hit = rows.find((r) => r.visible > 0);
    lines.push(
      `${hit ? 'OK  ' : 'MISS'} ${group}` +
        (hit
          ? `  ← ${hit.selector} (${hit.visible} visible)`
          : '  (no selector matched a visible element)'),
    );
    for (const r of rows)
      lines.push(
        `      ${r.visible > 0 ? '✓' : r.count > 0 ? '~' : '✗'} ${r.selector}  [${r.count} match, ${r.visible} visible]`,
      );
  }
  lines.push('', 'Chosen elements:');
  lines.push(`promptInput: ${JSON.stringify(report.chosen.promptInput, null, 1)}`);
  lines.push(`generateButton: ${JSON.stringify(report.chosen.generateButton, null, 1)}`);
  lines.push(
    `generateCandidates (in order tried): ${JSON.stringify(report.chosen.generateCandidates)}`,
  );
  lines.push(`resultImages: ${JSON.stringify(report.chosen.resultImages, null, 1)}`);
  lines.push(`messages: ${report.chosen.messages || '(none)'}`);
  lines.push(
    '',
    'Legend: ✓ visible match · ~ matched but hidden · ✗ no match. Edit selectors.js, then reload the extension and the Flow tab.',
  );
  out.textContent = lines.join('\n');
}

// ---------- wiring ----------
$('btnStart').onclick = () => cmd('START');
$('btnPause').onclick = () => cmd('PAUSE');
$('btnResume').onclick = () => cmd('RESUME');
$('btnStop').onclick = () => cmd('STOP');

$('btnAdd').onclick = () => {
  const text = $('promptText').value;
  if (!text.trim()) return;
  cmd('ADD_TEXT', { text });
  $('promptText').value = '';
};
$('csvFile').onchange = async (e) => {
  const file = e.target.files?.[0];
  if (!file) return;
  cmd('ADD_CSV', { text: await file.text() });
  e.target.value = '';
};

$('queue').onclick = (e) => {
  const btn = e.target.closest('button[data-act]');
  if (!btn) return;
  const li = btn.closest('li');
  const id = li.dataset.id;
  const act = btn.dataset.act;
  if (act === 'up') cmd('MOVE_ITEM', { id, delta: -1 });
  else if (act === 'down') cmd('MOVE_ITEM', { id, delta: 1 });
  else if (act === 'del') cmd('REMOVE_ITEM', { id });
  else if (act === 'edit') startEdit(li, id);
  else if (act === 'save') {
    const text = li.querySelector('textarea').value.trim();
    editingId = null;
    if (text)
      cmd('UPDATE_ITEM', { id, patch: { text, status: 'pending', error: '', attempts: 0 } });
    else render();
  } else if (act === 'cancel') {
    editingId = null;
    render();
  }
};

let editingId = null;
function startEdit(li, id) {
  editingId = id;
  const current = state.queue.find((i) => i.id === id);
  const ta = document.createElement('textarea');
  ta.rows = 3;
  ta.value = current?.text ?? '';
  li.querySelector('.text').replaceChildren(ta);
  li.querySelector('.actions').replaceChildren(
    Object.assign(document.createElement('button'), { textContent: 'Save', dataset: {} }),
    Object.assign(document.createElement('button'), { textContent: 'Cancel' }),
  );
  const [save, cancel] = li.querySelectorAll('.actions button');
  save.dataset.act = 'save';
  cancel.dataset.act = 'cancel';
  ta.focus();
}

$('btnResetFailed').onclick = () => cmd('RESET_FAILED');
$('btnResetAll').onclick = () => cmd('RESET_ALL');
$('btnClearDone').onclick = () => cmd('CLEAR_DONE');
$('btnClearQueue').onclick = (e) => {
  const b = e.currentTarget;
  if (b.dataset.armed) {
    delete b.dataset.armed;
    b.textContent = 'Clear queue';
    cmd('CLEAR_QUEUE');
  } else {
    b.dataset.armed = '1';
    b.textContent = 'Click again to clear';
    setTimeout(() => {
      delete b.dataset.armed;
      b.textContent = 'Clear queue';
    }, 4000);
  }
};
$('btnClearLog').onclick = () => cmd('CLEAR_LOG');

for (const key of ['minDelaySec', 'maxDelaySec', 'timeoutSec', 'retries']) {
  $(key).onchange = (e) =>
    cmd('SETTINGS', { patch: { [key]: Math.max(0, Number(e.target.value) || 0) } });
}
for (const key of ['prefix', 'suffix'])
  $(key).onchange = (e) => cmd('SETTINGS', { patch: { [key]: e.target.value } });
$('autoDownload').onchange = (e) => cmd('SETTINGS', { patch: { autoDownload: e.target.checked } });

$('btnDebug').onclick = () => {
  $('debugOut').hidden = false;
  $('debugOut').textContent = 'Asking the Flow tab…';
  cmd('DEBUG_SELECTORS');
};
$('btnTestOne').onclick = () => {
  cmd('TEST_ONE'); // background logs "Add a pending prompt first." when the queue is empty
};

// Refresh the "next in Ns" countdown while waiting.
setInterval(() => {
  if (state?.run.phase === 'delay') render();
}, 1000);
