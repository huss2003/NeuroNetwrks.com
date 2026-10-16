/**
 * Service worker: owns the queue state machine, talks to the content script
 * and the side panel, and does downloads. All queue logic is in queue.js.
 */
import {
  QueueEngine,
  initialState,
  STATUS,
  RUN,
  slugify,
  parsePromptText,
  promptsFromCsv,
  finalPrompt,
} from './queue.js';

const STORAGE_KEY = 'fpq_state';
const ALARM_NEXT = 'fpq-next';
const ALARM_WATCHDOG = 'fpq-watchdog';
const FLOW_URL_PATTERN = 'https://labs.google/fx/*';

let engine = null;
let ready = null; // Promise resolved once state is loaded
const panelPorts = new Set();
let persistTimer = null;
let pendingAlarmFn = null;

// ---------- persistence ----------
function persist(state) {
  clearTimeout(persistTimer);
  persistTimer = setTimeout(() => chrome.storage.local.set({ [STORAGE_KEY]: state }), 150);
}

async function loadState() {
  const got = await chrome.storage.local.get(STORAGE_KEY);
  const saved = got[STORAGE_KEY];
  const base = initialState();
  if (!saved) return base;
  return {
    settings: { ...base.settings, ...(saved.settings || {}) },
    queue: Array.isArray(saved.queue) ? saved.queue : [],
    run: { ...base.run, ...(saved.run || {}) },
    log: Array.isArray(saved.log) ? saved.log : [],
  };
}

// ---------- UI push ----------
function notify(state) {
  const snapshot = { state };
  for (const port of panelPorts) {
    try {
      port.postMessage({ type: 'STATE', ...snapshot });
    } catch {
      panelPorts.delete(port);
    }
  }
  updateBadge(state);
  manageWatchdog(state);
}

function updateBadge(state) {
  const { status, stopReason } = state.run;
  let text = '';
  let color = '#006DEE';
  if (status === RUN.RUNNING) {
    const left = state.queue.filter(
      (i) => i.status === STATUS.PENDING || i.status === STATUS.RUNNING,
    ).length;
    text = String(left);
  } else if (status === RUN.PAUSED) text = '||';
  else if (status === RUN.STOPPED && stopReason && stopReason !== 'user') {
    text = '!';
    color = '#C62828';
  }
  chrome.action.setBadgeText({ text });
  chrome.action.setBadgeBackgroundColor({ color });
}

function manageWatchdog(state) {
  if (state.run.status === RUN.RUNNING)
    chrome.alarms.create(ALARM_WATCHDOG, { periodInMinutes: 0.5 });
  else chrome.alarms.clear(ALARM_WATCHDOG);
}

// ---------- Flow tab + content script ----------
async function findFlowTab(preferredId) {
  const tabs = await chrome.tabs.query({ url: FLOW_URL_PATTERN });
  if (!tabs.length)
    throw new Error('No Google Flow tab is open (https://labs.google/fx/tools/flow).');
  return tabs.find((t) => t.id === preferredId) || tabs.find((t) => t.active) || tabs[0];
}

async function sendToTab(tabId, message) {
  try {
    return await chrome.tabs.sendMessage(tabId, message);
  } catch {
    // Content script not there (extension reloaded, page loaded before install): inject and retry once.
    await chrome.scripting.executeScript({
      target: { tabId },
      files: ['selectors.js', 'content.js'],
    });
    return await chrome.tabs.sendMessage(tabId, message);
  }
}

async function runPrompt(item, settings, index) {
  const tab = await findFlowTab(engine.state.run.tabId);
  engine.state.run.tabId = tab.id;
  const ack = await sendToTab(tab.id, {
    type: 'RUN_PROMPT',
    id: item.id,
    index,
    text: item.text,
    timeoutMs: (Number(settings.timeoutSec) || 180) * 1000,
    autoDownload: !!settings.autoDownload,
  });
  if (!ack?.ok) throw new Error(ack?.error || 'Content script refused the prompt');
}

async function abort() {
  try {
    const tab = await findFlowTab(engine.state.run.tabId);
    await chrome.tabs.sendMessage(tab.id, { type: 'ABORT' });
  } catch {
    /* tab gone; nothing to abort */
  }
}

/** Delays under 25 s use setTimeout (the worker stays alive that long after an event); longer ones use an alarm. */
function schedule(ms, fn) {
  if (ms < 25_000) {
    const t = setTimeout(fn, ms);
    return () => clearTimeout(t);
  }
  pendingAlarmFn = fn;
  chrome.alarms.create(ALARM_NEXT, { when: Date.now() + ms });
  return () => {
    pendingAlarmFn = null;
    chrome.alarms.clear(ALARM_NEXT);
  };
}

// ---------- downloads ----------
async function download(url, index, promptText, ext = 'png') {
  const filename = `flow/${String(index + 1).padStart(3, '0')}_${slugify(promptText)}.${ext}`;
  const id = await chrome.downloads.download({
    url,
    filename,
    conflictAction: 'uniquify',
    saveAs: false,
  });
  return { id, filename };
}

// ---------- boot ----------
async function init() {
  const state = await loadState();
  engine = new QueueEngine({ runPrompt, abort, schedule, persist, notify }, state);
  engine.restore();
  return engine;
}
ready = init();

chrome.runtime.onInstalled.addListener(() => {
  chrome.sidePanel.setPanelBehavior({ openPanelOnActionClick: true }).catch(() => {});
});

chrome.alarms.onAlarm.addListener(async (alarm) => {
  await ready;
  if (alarm.name === ALARM_NEXT) {
    const fn = pendingAlarmFn;
    pendingAlarmFn = null;
    if (fn) fn();
    else if (engine.state.run.status === RUN.RUNNING && engine.state.run.phase === 'delay')
      engine.next();
  } else if (alarm.name === ALARM_WATCHDOG) {
    engine.tick();
  }
});

// Messages from the content script.
chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (sender.id !== chrome.runtime.id) return;
  ready.then(async () => {
    switch (msg?.type) {
      case 'PROMPT_RESULT':
        if (msg.test) {
          const r = msg.result;
          engine.log(
            r.ok ? 'ok' : 'error',
            r.ok
              ? `Test prompt done: ${r.images.length} image(s)` +
                  (r.downloaded ? `, ${r.downloaded} downloaded` : '')
              : `Test prompt ${r.kind}: ${r.error}`,
          );
          engine.commit();
        } else engine.promptResult(msg.id, msg.result);
        sendResponse({ ok: true });
        break;
      case 'HEARTBEAT':
        sendResponse({ ok: true }); // the event itself keeps the worker alive
        break;
      case 'LOG':
        engine.log(msg.level || 'info', msg.message, msg.index);
        engine.commit();
        sendResponse({ ok: true });
        break;
      case 'DOWNLOAD':
        try {
          const r = await download(msg.url, msg.index, msg.prompt, msg.ext);
          sendResponse({ ok: true, ...r });
        } catch (e) {
          sendResponse({ ok: false, error: String(e?.message || e) });
        }
        break;
      default:
        sendResponse({ ok: false, error: 'unknown message' });
    }
  });
  return true;
});

// Long-lived port from the side panel.
chrome.runtime.onConnect.addListener((port) => {
  if (port.name !== 'panel') return;
  panelPorts.add(port);
  port.onDisconnect.addListener(() => panelPorts.delete(port));
  port.onMessage.addListener(async (msg) => {
    await ready;
    try {
      await handlePanelCommand(msg, port);
    } catch (e) {
      engine.log('error', `Panel command ${msg?.type} failed: ${e?.message || e}`);
      engine.commit();
    }
  });
  ready.then(() => port.postMessage({ type: 'STATE', state: engine.state }));
});

async function handlePanelCommand(msg, port) {
  const s = engine.state;
  switch (msg.type) {
    case 'GET_STATE':
      port.postMessage({ type: 'STATE', state: s });
      break;
    case 'ADD_TEXT':
      engine.addPrompts(parsePromptText(msg.text));
      break;
    case 'ADD_CSV':
      engine.addPrompts(promptsFromCsv(msg.text));
      break;
    case 'UPDATE_ITEM':
      engine.updateItem(msg.id, msg.patch);
      break;
    case 'REMOVE_ITEM':
      engine.removeItem(msg.id);
      break;
    case 'MOVE_ITEM':
      engine.moveItem(msg.id, msg.delta);
      break;
    case 'RESET_FAILED':
      engine.resetItems((i) => i.status === STATUS.FAILED);
      break;
    case 'RESET_ALL':
      engine.resetItems();
      break;
    case 'CLEAR_DONE':
      engine.clearDone();
      break;
    case 'CLEAR_QUEUE':
      if (s.run.status === RUN.RUNNING || s.run.status === RUN.PAUSED) engine.stop('user');
      engine.setQueue([]);
      break;
    case 'CLEAR_LOG':
      s.log = [];
      engine.commit();
      break;
    case 'SETTINGS':
      engine.updateSettings(msg.patch);
      break;
    case 'START': {
      const tab = await findFlowTab(s.run.tabId);
      engine.start(tab.id);
      break;
    }
    case 'PAUSE':
      engine.pause();
      break;
    case 'RESUME':
      engine.resume();
      break;
    case 'STOP':
      engine.stop('user');
      break;
    case 'DEBUG_SELECTORS': {
      const tab = await findFlowTab(s.run.tabId);
      const report = await sendToTab(tab.id, { type: 'DEBUG_SELECTORS' });
      port.postMessage({ type: 'DEBUG_REPORT', report, url: tab.url });
      break;
    }
    case 'TEST_ONE': {
      // Runs a single prompt end-to-end without touching the queue (stage-1 test).
      const first = s.queue.find((i) => i.status === STATUS.PENDING);
      if (!first) throw new Error('Add a pending prompt first.');
      const tab = await findFlowTab(s.run.tabId);
      s.run.tabId = tab.id;
      const ack = await sendToTab(tab.id, {
        type: 'RUN_PROMPT',
        id: 'test',
        index: -1,
        text: finalPrompt(first.text, s.settings),
        timeoutMs: (Number(s.settings.timeoutSec) || 180) * 1000,
        autoDownload: !!s.settings.autoDownload,
        test: true,
      });
      engine.log(
        ack?.ok ? 'info' : 'error',
        ack?.ok ? 'Test prompt submitted; watch the log.' : `Test prompt refused: ${ack?.error}`,
      );
      engine.commit();
      break;
    }
    default:
      engine.log('warn', `Unknown panel command ${msg.type}`);
      engine.commit();
  }
}
