import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  QueueEngine,
  initialState,
  STATUS,
  RUN,
  parsePromptText,
  parseCsv,
  promptsFromCsv,
  slugify,
  finalPrompt,
} from '../queue.js';

/** Builds an engine with fake timers and a recording driver. */
function harness(opts = {}) {
  let now = 1_000_000;
  const timers = [];
  const calls = { run: [], abort: 0, persist: 0 };
  const deps = {
    now: () => now,
    random: () => 0.5,
    runPrompt: async (item, settings, index) => {
      calls.run.push({ id: item.id, text: item.text, index });
      if (opts.runThrows) throw new Error('tab gone');
    },
    abort: () => calls.abort++,
    persist: () => calls.persist++,
    notify: () => {},
    schedule: (ms, fn) => {
      const t = { at: now + ms, fn, cancelled: false };
      timers.push(t);
      return () => (t.cancelled = true);
    },
  };
  const engine = new QueueEngine(deps, initialState());
  Object.assign(engine.state.settings, opts.settings || {});
  const fire = () => {
    const due = timers.filter((t) => !t.cancelled && t.at <= now);
    for (const t of due) {
      t.cancelled = true;
      t.fn();
    }
    return due.length;
  };
  const advance = (ms) => {
    now += ms;
    return fire();
  };
  const tick = () => new Promise((r) => setTimeout(r, 0));
  return {
    engine,
    calls,
    timers,
    advance,
    tick,
    get now() {
      return now;
    },
  };
}

test('runs prompts in order with a random delay between them', async () => {
  const h = harness({ settings: { minDelaySec: 5, maxDelaySec: 12 } });
  h.engine.addPrompts(['one', 'two']);
  h.engine.start(7);
  await h.tick();
  assert.equal(h.calls.run.length, 1);
  assert.equal(h.engine.state.queue[0].status, STATUS.RUNNING);
  assert.equal(h.engine.state.run.tabId, 7);

  h.engine.promptResult(h.engine.state.queue[0].id, { ok: true, images: ['a'] });
  assert.equal(h.engine.state.queue[0].status, STATUS.DONE);
  assert.equal(h.engine.state.run.phase, 'delay');
  assert.equal(h.timers.at(-1).at - h.now, 8500); // 5 + 0.5 * 7 seconds

  assert.equal(h.advance(8000), 0, 'not yet');
  assert.equal(h.advance(600), 1);
  await h.tick();
  assert.equal(h.calls.run.length, 2);
  assert.equal(h.calls.run[1].text, 'two');

  h.engine.promptResult(h.engine.state.queue[1].id, { ok: true, images: [] });
  assert.equal(h.engine.state.run.status, RUN.IDLE);
  assert.match(h.engine.state.log.at(-1).message, /Queue finished: 2 done, 0 failed/);
});

test('applies prefix and suffix to the submitted text only', async () => {
  const h = harness({ settings: { prefix: 'Photo of', suffix: ', 35mm' } });
  h.engine.addPrompts(['a cat']);
  h.engine.start();
  await h.tick();
  assert.equal(h.calls.run[0].text, 'Photo of a cat, 35mm');
  assert.equal(h.engine.state.queue[0].text, 'a cat');
  assert.equal(finalPrompt('  x  ', { prefix: '', suffix: '' }), 'x');
});

test('retries a failed prompt up to N times, then marks it failed and continues', async () => {
  const h = harness({ settings: { retries: 2 } });
  h.engine.addPrompts(['bad', 'good']);
  h.engine.start();
  await h.tick();
  const bad = h.engine.state.queue[0];
  for (let attempt = 1; attempt <= 3; attempt++) {
    assert.equal(h.calls.run.length, attempt);
    assert.equal(h.calls.run.at(-1).text, 'bad');
    h.engine.promptResult(bad.id, { ok: false, kind: 'timeout', error: 'no image' });
    if (attempt < 3) {
      assert.equal(bad.status, STATUS.PENDING, `attempt ${attempt} goes back to pending`);
      h.advance(3000);
      await h.tick();
    }
  }
  assert.equal(bad.status, STATUS.FAILED);
  assert.equal(bad.attempts, 3);
  assert.equal(bad.error, 'no image');
  h.advance(60_000);
  await h.tick();
  assert.equal(h.calls.run.at(-1).text, 'good');
  assert.equal(h.engine.state.run.status, RUN.RUNNING);
});

test('quota message stops the queue, keeps the prompt pending and records the reason', async () => {
  const h = harness();
  h.engine.addPrompts(['p1', 'p2']);
  h.engine.start();
  await h.tick();
  const p1 = h.engine.state.queue[0];
  h.engine.promptResult(p1.id, { ok: false, kind: 'quota', error: 'out of credits' });
  assert.equal(h.engine.state.run.status, RUN.STOPPED);
  assert.equal(h.engine.state.run.stopReason, 'quota');
  assert.equal(p1.status, STATUS.PENDING);
  assert.equal(p1.attempts, 0, 'a quota stop does not count as an attempt');
  assert.equal(h.calls.run.length, 1, 'no further prompt was submitted');
  assert.ok(h.engine.state.log.some((e) => e.level === 'error' && /limit/.test(e.message)));

  // Start again later: resumes from the first unfinished prompt.
  h.engine.start();
  await h.tick();
  assert.equal(h.calls.run.at(-1).text, 'p1');
});

test('pause waits for the current generation, resume continues; pause during delay cancels the timer', async () => {
  const h = harness();
  h.engine.addPrompts(['a', 'b', 'c']);
  h.engine.start();
  await h.tick();
  h.engine.pause();
  assert.equal(h.engine.state.run.status, RUN.PAUSED);
  const a = h.engine.state.queue[0];
  h.engine.promptResult(a.id, { ok: true, images: ['x'] });
  assert.equal(a.status, STATUS.DONE);
  assert.equal(h.timers.length, 0, 'nothing scheduled while paused');
  assert.equal(h.calls.run.length, 1);

  h.engine.resume();
  await h.tick();
  assert.equal(h.calls.run.length, 2, 'resume starts the next prompt immediately');
  const b = h.engine.state.queue[1];
  h.engine.promptResult(b.id, { ok: true });
  assert.equal(h.engine.state.run.phase, 'delay');
  h.engine.pause();
  assert.ok(
    h.timers.every((t) => t.cancelled),
    'delay timer cancelled on pause',
  );
  h.advance(100_000);
  await h.tick();
  assert.equal(h.calls.run.length, 2, 'nothing ran while paused');
  h.engine.resume();
  await h.tick();
  assert.equal(h.calls.run.at(-1).text, 'c');
});

test('stop aborts the running prompt, puts it back to pending and saves progress', async () => {
  const h = harness();
  h.engine.addPrompts(['a', 'b']);
  h.engine.start();
  await h.tick();
  const a = h.engine.state.queue[0];
  h.engine.stop('user');
  assert.equal(h.calls.abort, 1);
  assert.equal(a.status, STATUS.PENDING);
  assert.equal(a.attempts, 0);
  assert.equal(h.engine.state.run.status, RUN.STOPPED);
  // A late result from the aborted run is ignored.
  h.engine.promptResult(a.id, { ok: true, images: ['late'] });
  assert.equal(a.status, STATUS.PENDING);
  assert.ok(h.calls.persist > 0);
});

test('unreachable Flow tab counts as a failed attempt', async () => {
  const h = harness({ runThrows: true, settings: { retries: 0 } });
  h.engine.addPrompts(['a']);
  h.engine.start();
  await h.tick();
  assert.equal(h.engine.state.queue[0].status, STATUS.FAILED);
  assert.match(h.engine.state.queue[0].error, /Could not reach the Flow tab/);
});

test('watchdog tick times out a generation that never answered', async () => {
  const h = harness({ settings: { timeoutSec: 10, retries: 0 } });
  h.engine.addPrompts(['a']);
  h.engine.start();
  await h.tick();
  h.engine.tick();
  assert.equal(h.engine.state.queue[0].status, STATUS.RUNNING);
  h.advance(10_000 + 60_000 + 1);
  h.engine.tick();
  assert.equal(h.calls.abort, 1);
  assert.equal(h.engine.state.queue[0].status, STATUS.FAILED);
});

test('restore after a worker restart re-runs the interrupted prompt', async () => {
  const h = harness();
  h.engine.addPrompts(['a', 'b']);
  h.engine.start();
  await h.tick();
  const saved = JSON.parse(JSON.stringify(h.engine.state));
  assert.equal(saved.queue[0].status, STATUS.RUNNING);

  const h2 = harness();
  h2.engine.state = saved;
  h2.engine.restore();
  await h2.tick();
  assert.equal(h2.calls.run.length, 1);
  assert.equal(h2.calls.run[0].text, 'a');
  assert.equal(h2.engine.state.queue[0].attempts, 1);
});

test('queue editing: move, remove, reset, clear done', () => {
  const h = harness();
  h.engine.addPrompts(['a', 'b', 'c']);
  const [a, b, c] = h.engine.state.queue;
  h.engine.moveItem(c.id, -1);
  assert.deepEqual(
    h.engine.state.queue.map((i) => i.text),
    ['a', 'c', 'b'],
  );
  h.engine.moveItem(a.id, -1); // no-op at the top
  assert.equal(h.engine.state.queue[0].text, 'a');
  h.engine.removeItem(b.id);
  assert.deepEqual(
    h.engine.state.queue.map((i) => i.text),
    ['a', 'c'],
  );
  a.status = STATUS.FAILED;
  a.error = 'x';
  c.status = STATUS.DONE;
  h.engine.resetItems((i) => i.status === STATUS.FAILED);
  assert.equal(a.status, STATUS.PENDING);
  assert.equal(c.status, STATUS.DONE);
  h.engine.clearDone();
  assert.deepEqual(
    h.engine.state.queue.map((i) => i.text),
    ['a'],
  );
});

test('parsePromptText: one per line, or @@@NEXT@@@ blocks', () => {
  assert.deepEqual(parsePromptText('a\n\n b \r\nc'), ['a', 'b', 'c']);
  assert.deepEqual(parsePromptText('line one\nline two\n@@@NEXT@@@\nsecond prompt'), [
    'line one\nline two',
    'second prompt',
  ]);
});

test('parsePromptText: a script document yields only the "Image Prompt:" lines', () => {
  const doc = `IMAGE PROMPTS - "Why $100,000"
358 images, one per 3-5 second script beat
--------------------------------------------------
Image 001 Prompt
[Script Segment Text]: "You skip the fancy coffee."
Image Prompt: Cartoon of a man refusing a coffee cup, flat 2D, 16:9
Camera Angle: eye-level medium shot
Lighting: flat even studio lighting
Mood: smug
Action: He waves off a coffee.
--------------------------------------------------
Image 002 Prompt
[Script Segment Text]: "You drive the same car."
Image Prompt:   Cartoon of a man leaning on an old sedan, 16:9
Camera Angle: eye-level medium-wide
`;
  assert.deepEqual(parsePromptText(doc), [
    'Cartoon of a man refusing a coffee cup, flat 2D, 16:9',
    'Cartoon of a man leaning on an old sedan, 16:9',
  ]);
});

test('CSV import takes the first column and skips a "prompt" header', () => {
  assert.deepEqual(parseCsv('a,b\n"x, y","q""q"\n'), [
    ['a', 'b'],
    ['x, y', 'q"q'],
  ]);
  assert.deepEqual(promptsFromCsv('prompt,notes\n"a red fox, running",n1\nblue sky,n2\n'), [
    'a red fox, running',
    'blue sky',
  ]);
  assert.deepEqual(promptsFromCsv('"multi\nline",x'), ['multi\nline']);
});

test('slugify makes safe file names', () => {
  assert.equal(slugify('  A Red Fox, running! Über 🦊 '), 'a-red-fox-running-uber');
  assert.equal(slugify('!!!'), 'prompt');
  assert.equal(slugify('x'.repeat(100)).length, 60);
});
