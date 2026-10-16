/**
 * Queue state machine. Pure logic, no Chrome APIs, so it can be unit-tested.
 *
 * The engine is driven by events:
 *   start() pause() resume() stop()        from the side panel
 *   promptResult(id, result)               from the content script
 *   tick()                                 watchdog (alarm)
 *   restore(state)                         after the service worker restarts
 *
 * Side effects go through `deps`:
 *   runPrompt(item, settings, index)  -> Promise  ask the content script to run one prompt
 *   abort()                           -> void     tell the content script to stop waiting
 *   schedule(ms, fn)                  -> cancel() delayed callback (setTimeout / chrome.alarms)
 *   persist(state)                    -> void     save to storage
 *   notify(state)                     -> void     push the new state to the UI
 *   now()                             -> number   Date.now()
 *   random()                          -> number   Math.random()
 */

export const STATUS = { PENDING: 'pending', RUNNING: 'running', DONE: 'done', FAILED: 'failed' };
export const RUN = { IDLE: 'idle', RUNNING: 'running', PAUSED: 'paused', STOPPED: 'stopped' };

export const DEFAULT_SETTINGS = {
  minDelaySec: 5,
  maxDelaySec: 12,
  timeoutSec: 180,
  retries: 2,
  autoDownload: false,
  prefix: '',
  suffix: '',
};

const MAX_LOG = 500;
const RETRY_DELAY_MS = 3000;
const WATCHDOG_GRACE_MS = 60_000;

export function makeItem(text, id) {
  return {
    id: id || `p_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 8)}`,
    text,
    status: STATUS.PENDING,
    attempts: 0,
    error: '',
    images: [],
  };
}

export function initialState() {
  return {
    settings: { ...DEFAULT_SETTINGS },
    queue: [],
    run: {
      status: RUN.IDLE,
      phase: 'idle',
      currentId: null,
      startedAt: 0,
      stopReason: '',
      tabId: null,
      nextAt: 0,
    },
    log: [],
  };
}

/** Applies prefix / suffix. Exported so the UI can preview the final prompt. */
export function finalPrompt(text, settings) {
  const pre = settings.prefix ? settings.prefix.trim() + ' ' : '';
  const sufRaw = (settings.suffix || '').trim();
  // A suffix that starts with punctuation (", soft light") is glued on without a space.
  const suf = sufRaw ? (/^[,.;:!?)]/.test(sufRaw) ? '' : ' ') + sufRaw : '';
  return (pre + text.trim() + suf).trim();
}

export class QueueEngine {
  constructor(deps, state) {
    this.deps = { now: () => Date.now(), random: Math.random, ...deps };
    this.state = state || initialState();
    this.cancelTimer = null;
  }

  // ---------- helpers ----------
  log(level, message, index) {
    const entry = { t: this.deps.now(), level, index: index ?? null, message };
    this.state.log.push(entry);
    if (this.state.log.length > MAX_LOG) this.state.log.splice(0, this.state.log.length - MAX_LOG);
  }

  commit() {
    this.deps.persist?.(this.state);
    this.deps.notify?.(this.state);
  }

  item(id) {
    return this.state.queue.find((i) => i.id === id);
  }

  indexOf(id) {
    return this.state.queue.findIndex((i) => i.id === id);
  }

  firstPending() {
    return this.state.queue.find((i) => i.status === STATUS.PENDING);
  }

  clearTimer() {
    if (this.cancelTimer) {
      this.cancelTimer();
      this.cancelTimer = null;
    }
    this.state.run.nextAt = 0;
  }

  randomDelayMs() {
    const s = this.state.settings;
    const min = Math.max(0, Number(s.minDelaySec) || 0);
    const max = Math.max(min, Number(s.maxDelaySec) || 0);
    return Math.round((min + this.deps.random() * (max - min)) * 1000);
  }

  // ---------- queue editing ----------
  setQueue(items) {
    this.state.queue = items;
    this.commit();
  }

  addPrompts(texts) {
    const added = texts
      .map((t) => t.trim())
      .filter(Boolean)
      .map((t) => makeItem(t));
    this.state.queue.push(...added);
    this.log('info', `Added ${added.length} prompt(s). Queue size ${this.state.queue.length}.`);
    this.commit();
    return added.length;
  }

  updateItem(id, patch) {
    const it = this.item(id);
    if (!it) return;
    Object.assign(it, patch);
    this.commit();
  }

  removeItem(id) {
    const i = this.indexOf(id);
    if (i < 0) return;
    if (this.state.queue[i].status === STATUS.RUNNING) return; // cannot delete the running one
    this.state.queue.splice(i, 1);
    this.commit();
  }

  moveItem(id, delta) {
    const i = this.indexOf(id);
    const j = i + delta;
    if (i < 0 || j < 0 || j >= this.state.queue.length) return;
    const [it] = this.state.queue.splice(i, 1);
    this.state.queue.splice(j, 0, it);
    this.commit();
  }

  resetItems(filter) {
    for (const it of this.state.queue) {
      if (it.status === STATUS.RUNNING) continue;
      if (!filter || filter(it)) {
        it.status = STATUS.PENDING;
        it.attempts = 0;
        it.error = '';
        it.images = [];
      }
    }
    this.commit();
  }

  clearDone() {
    this.state.queue = this.state.queue.filter((i) => i.status !== STATUS.DONE);
    this.commit();
  }

  updateSettings(patch) {
    Object.assign(this.state.settings, patch);
    this.commit();
  }

  // ---------- run control ----------
  start(tabId) {
    const run = this.state.run;
    if (run.status === RUN.RUNNING) return;
    if (!this.firstPending()) {
      this.log('warn', 'Nothing to run: no pending prompts.');
      this.commit();
      return;
    }
    run.status = RUN.RUNNING;
    run.stopReason = '';
    if (tabId != null) run.tabId = tabId;
    this.log('info', 'Queue started.');
    this.commit();
    this.next();
  }

  pause() {
    const run = this.state.run;
    if (run.status !== RUN.RUNNING) return;
    run.status = RUN.PAUSED;
    this.clearTimer();
    this.log(
      'info',
      run.phase === 'generating' ? 'Pausing after the current generation finishes.' : 'Paused.',
    );
    this.commit();
  }

  resume() {
    const run = this.state.run;
    if (run.status !== RUN.PAUSED) return;
    run.status = RUN.RUNNING;
    this.log('info', 'Resumed.');
    this.commit();
    if (run.phase !== 'generating') this.next();
  }

  stop(reason = 'user') {
    const run = this.state.run;
    this.clearTimer();
    const current = run.currentId && this.item(run.currentId);
    if (current && current.status === STATUS.RUNNING) {
      current.status = STATUS.PENDING; // will be the first unfinished prompt on restart
      current.attempts = Math.max(0, current.attempts - 1);
    }
    if (run.phase === 'generating') this.deps.abort?.();
    run.status = RUN.STOPPED;
    run.phase = 'idle';
    run.currentId = null;
    run.stopReason = reason;
    this.log(
      reason === 'user' ? 'info' : 'error',
      reason === 'user'
        ? 'Stopped by user. Progress saved.'
        : `Stopped: ${reason}. Progress saved.`,
    );
    this.commit();
  }

  /** Called after the service worker was restarted with the persisted state. */
  restore() {
    const run = this.state.run;
    const current = run.currentId && this.item(run.currentId);
    if (current && current.status === STATUS.RUNNING) {
      current.status = STATUS.PENDING;
      current.attempts = Math.max(0, current.attempts - 1);
      this.log(
        'warn',
        'Extension restarted mid-generation; that prompt will run again.',
        this.indexOf(current.id),
      );
    }
    run.currentId = null;
    run.phase = 'idle';
    run.nextAt = 0;
    if (run.status === RUN.RUNNING) {
      this.log('info', 'Resuming queue after restart.');
      this.commit();
      this.next();
    } else {
      this.commit();
    }
  }

  // ---------- the loop ----------
  async next() {
    const run = this.state.run;
    this.clearTimer();
    if (run.status !== RUN.RUNNING) return;
    const it = this.firstPending();
    if (!it) {
      run.status = RUN.IDLE;
      run.phase = 'idle';
      run.currentId = null;
      const done = this.state.queue.filter((i) => i.status === STATUS.DONE).length;
      const failed = this.state.queue.filter((i) => i.status === STATUS.FAILED).length;
      this.log('info', `Queue finished: ${done} done, ${failed} failed.`);
      this.commit();
      return;
    }
    const index = this.indexOf(it.id);
    it.status = STATUS.RUNNING;
    it.attempts += 1;
    it.error = '';
    run.phase = 'generating';
    run.currentId = it.id;
    run.startedAt = this.deps.now();
    this.log(
      'info',
      `Submitting prompt ${index + 1}/${this.state.queue.length}` +
        (it.attempts > 1 ? ` (attempt ${it.attempts})` : ''),
      index,
    );
    this.commit();
    try {
      await this.deps.runPrompt(
        { ...it, text: finalPrompt(it.text, this.state.settings) },
        this.state.settings,
        index,
      );
    } catch (e) {
      this.promptResult(it.id, {
        ok: false,
        kind: 'error',
        error: `Could not reach the Flow tab: ${e?.message || e}`,
      });
    }
  }

  promptResult(id, result) {
    const run = this.state.run;
    const it = this.item(id);
    if (!it || it.status !== STATUS.RUNNING || run.currentId !== id) return; // stale or duplicate
    const index = this.indexOf(id);
    run.phase = 'idle';
    run.currentId = null;

    if (result.ok) {
      it.status = STATUS.DONE;
      it.images = result.images || [];
      it.error = '';
      this.log(
        'ok',
        `Done: ${it.images.length} result(s)` +
          (result.downloaded ? `, ${result.downloaded} downloaded` : ''),
        index,
      );
      this.afterItem(this.randomDelayMs());
      return;
    }

    if (result.kind === 'quota') {
      it.status = STATUS.PENDING;
      it.attempts = Math.max(0, it.attempts - 1);
      this.log('error', `Flow reported a limit: "${result.error}"`, index);
      this.stop('quota');
      return;
    }

    const msg = result.error || result.kind || 'unknown error';
    if (it.attempts <= this.state.settings.retries) {
      it.status = STATUS.PENDING;
      it.error = msg;
      this.log(
        'warn',
        `Failed (${result.kind || 'error'}): ${msg}. Retrying (${it.attempts}/${this.state.settings.retries}).`,
        index,
      );
      this.afterItem(RETRY_DELAY_MS);
    } else {
      it.status = STATUS.FAILED;
      it.error = msg;
      this.log('error', `Failed after ${it.attempts} attempt(s): ${msg}. Skipping.`, index);
      this.afterItem(this.randomDelayMs());
    }
  }

  afterItem(delayMs) {
    const run = this.state.run;
    if (run.status === RUN.PAUSED) {
      this.log('info', 'Paused. Press Resume to continue.');
      this.commit();
      return;
    }
    if (run.status !== RUN.RUNNING) {
      this.commit();
      return;
    }
    if (!this.firstPending()) {
      this.next();
      return;
    }
    run.phase = 'delay';
    run.nextAt = this.deps.now() + delayMs;
    this.log('info', `Waiting ${(delayMs / 1000).toFixed(1)}s before the next prompt.`);
    this.commit();
    this.cancelTimer = this.deps.schedule(delayMs, () => {
      this.cancelTimer = null;
      this.next();
    });
  }

  /** Watchdog: handles a content script that never answered (tab closed, crashed). */
  tick() {
    const run = this.state.run;
    if (run.phase === 'generating' && run.currentId) {
      const limit = (Number(this.state.settings.timeoutSec) || 180) * 1000 + WATCHDOG_GRACE_MS;
      if (this.deps.now() - run.startedAt > limit) {
        this.deps.abort?.();
        this.promptResult(run.currentId, {
          ok: false,
          kind: 'timeout',
          error: 'No answer from the Flow tab (watchdog timeout)',
        });
      }
    } else if (
      run.phase === 'delay' &&
      run.nextAt &&
      this.deps.now() > run.nextAt + 5000 &&
      !this.cancelTimer
    ) {
      // The timer was lost (service worker restarted during the delay).
      this.next();
    }
  }
}

/** Splits pasted text into prompts: one per line, or blocks separated by @@@NEXT@@@ for multi-line prompts. */
export function parsePromptText(text) {
  const t = String(text || '').replace(/\r\n?/g, '\n');
  if (t.includes('@@@NEXT@@@')) {
    return t
      .split('@@@NEXT@@@')
      .map((s) => s.trim())
      .filter(Boolean);
  }
  return t
    .split('\n')
    .map((s) => s.trim())
    .filter(Boolean);
}

/** Minimal CSV parser (handles quoted fields with commas, quotes and newlines). Returns rows of cells. */
export function parseCsv(text) {
  const rows = [];
  let row = [];
  let cell = '';
  let inQuotes = false;
  const s = String(text || '').replace(/\r\n?/g, '\n');
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (inQuotes) {
      if (c === '"') {
        if (s[i + 1] === '"') {
          cell += '"';
          i++;
        } else inQuotes = false;
      } else cell += c;
    } else if (c === '"') inQuotes = true;
    else if (c === ',') {
      row.push(cell);
      cell = '';
    } else if (c === '\n') {
      row.push(cell);
      rows.push(row);
      row = [];
      cell = '';
    } else cell += c;
  }
  if (cell.length || row.length) {
    row.push(cell);
    rows.push(row);
  }
  return rows.filter((r) => r.some((c) => c.trim()));
}

/** First column of each CSV row, skipping a header cell named "prompt". */
export function promptsFromCsv(text) {
  const rows = parseCsv(text);
  const out = rows.map((r) => (r[0] || '').trim()).filter(Boolean);
  if (out.length && /^prompts?$/i.test(out[0])) out.shift();
  return out;
}

export function slugify(text, max = 60) {
  return (
    String(text)
      .toLowerCase()
      .normalize('NFKD')
      .replace(/[̀-ͯ]/g, '')
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '')
      .slice(0, max)
      .replace(/-+$/g, '') || 'prompt'
  );
}
