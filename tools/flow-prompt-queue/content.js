/**
 * Content script: runs ONE prompt end-to-end on the Flow page when asked by
 * background.js, then reports the result. All selectors come from selectors.js.
 */
(() => {
  if (globalThis.__FPQ_LOADED) return;
  globalThis.__FPQ_LOADED = true;

  const S = globalThis.FLOW_SELECTORS;
  const TAG = '[Flow Prompt Queue]';
  const SETTLE_MS = 3000; // no new image for this long = generation finished
  const SETTLE_FALLBACK_MS = 12000; // ...unless a progress indicator never clears; then use this
  let aborted = false;
  let running = false;

  // ---------- small utils ----------
  const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

  function send(message) {
    try {
      return chrome.runtime.sendMessage(message).catch(() => null);
    } catch {
      return Promise.resolve(null);
    }
  }

  function log(level, message, index) {
    console.log(TAG, level, message);
    return send({ type: 'LOG', level, message, index });
  }

  function isVisible(el) {
    if (!el || !el.isConnected) return false;
    const r = el.getBoundingClientRect();
    if (r.width <= 0 || r.height <= 0) return false;
    const st = getComputedStyle(el);
    return st.visibility !== 'hidden' && st.display !== 'none' && st.opacity !== '0';
  }

  function queryAll(selector, root = document) {
    try {
      return Array.from(root.querySelectorAll(selector));
    } catch {
      return [];
    }
  }

  function firstVisible(selectors, root = document) {
    for (const sel of selectors) {
      const el = queryAll(sel, root).find(isVisible);
      if (el) return { el, selector: sel };
    }
    return { el: null, selector: null };
  }

  function bottomOf(el) {
    return el.getBoundingClientRect().bottom;
  }

  function textOf(el) {
    return (el?.innerText || el?.textContent || '')
      .replace(/[\u200b\ufeff]/g, '')
      .replace(/\s+/g, ' ')
      .trim();
  }

  function describe(el) {
    if (!el) return null;
    const attrs = {};
    for (const a of [
      'id',
      'role',
      'aria-label',
      'data-testid',
      'placeholder',
      'aria-placeholder',
      'type',
      'contenteditable',
      'disabled',
      'aria-disabled',
    ]) {
      const v = el.getAttribute?.(a);
      if (v != null) attrs[a] = v;
    }
    return {
      tag: el.tagName?.toLowerCase(),
      attrs,
      text: textOf(el).slice(0, 80),
      html: el.outerHTML.slice(0, 300),
    };
  }

  // ---------- locate elements ----------
  function findPromptEditor() {
    const candidates = [];
    for (const sel of S.promptInput)
      for (const el of queryAll(sel))
        if (isVisible(el) && !candidates.includes(el)) candidates.push(el);
    if (!candidates.length) return null;
    const words = S.promptPlaceholderWords.map((w) => w.toLowerCase());
    const placeholderOf = (el) =>
      (
        el.getAttribute('placeholder') ||
        el.getAttribute('aria-placeholder') ||
        textOf(el.querySelector('[data-slate-placeholder]')) ||
        ''
      ).toLowerCase();
    const preferred = candidates.filter((el) => words.some((w) => placeholderOf(el).includes(w)));
    const pool = preferred.length ? preferred : candidates;
    return pool.sort((a, b) => bottomOf(b) - bottomOf(a))[0];
  }

  function findGenerateButton(editor) {
    const { el } = firstVisible(S.generateButton);
    if (el) return el;
    const buttons = queryAll('button, [role="button"]').filter(isVisible);
    const iconNames = S.generateButtonIconNames;
    const byIcon = buttons.filter((b) =>
      queryAll('i, span', b).some((i) => iconNames.includes(textOf(i))),
    );
    const texts = S.generateButtonTexts;
    const byText = buttons.filter((b) => texts.includes(textOf(b).toLowerCase()));
    const pool = byIcon.length ? byIcon : byText;
    if (!pool.length) return null;
    if (editor) {
      const er = editor.getBoundingClientRect();
      const dist = (b) => {
        const r = b.getBoundingClientRect();
        return Math.hypot(r.left - er.right, r.top - er.top);
      };
      return pool.sort((a, b) => dist(a) - dist(b))[0];
    }
    return pool.sort((a, b) => bottomOf(b) - bottomOf(a))[0];
  }

  function isDisabled(btn) {
    return !btn || btn.disabled || btn.getAttribute('aria-disabled') === 'true';
  }

  function resultRoot() {
    const { el } = firstVisible(S.resultContainers);
    return el || document.body;
  }

  function resultImages(root = resultRoot()) {
    const seen = new Set();
    const out = [];
    for (const sel of S.resultImage) {
      for (const img of queryAll(sel, root)) {
        if (seen.has(img)) continue;
        seen.add(img);
        if (!isVisible(img)) continue;
        if (
          !img.complete ||
          img.naturalWidth < S.minResultImageSize ||
          img.naturalHeight < S.minResultImageSize
        )
          continue;
        out.push(img);
      }
    }
    return out;
  }

  function imageKey(img) {
    return img.currentSrc || img.src;
  }

  function messagesText() {
    return queryAll(S.messageContainers.join(','))
      .filter(isVisible)
      .map(textOf)
      .filter(Boolean)
      .join(' | ');
  }

  function matchPattern(text, patterns) {
    const t = text.toLowerCase();
    return patterns.find((p) => t.includes(p.toLowerCase())) || null;
  }

  // ---------- user-like interaction ----------
  function pointerEvents(el, types) {
    const r = el.getBoundingClientRect();
    const common = {
      bubbles: true,
      cancelable: true,
      composed: true,
      view: window,
      clientX: r.left + r.width / 2,
      clientY: r.top + r.height / 2,
      button: 0,
    };
    for (const t of types) {
      if (t.startsWith('pointer'))
        el.dispatchEvent(
          new PointerEvent(t, { ...common, pointerId: 1, pointerType: 'mouse', isPrimary: true }),
        );
      else el.dispatchEvent(new MouseEvent(t, common));
    }
  }

  async function focusLikeUser(el) {
    el.scrollIntoView({ block: 'center', inline: 'nearest' });
    await sleep(50);
    pointerEvents(el, [
      'pointerover',
      'mouseover',
      'pointerdown',
      'mousedown',
      'pointerup',
      'mouseup',
      'click',
    ]);
    el.focus();
    await sleep(60);
  }

  async function clickLikeUser(el) {
    el.scrollIntoView({ block: 'center', inline: 'nearest' });
    await sleep(50);
    pointerEvents(el, [
      'pointerover',
      'mouseover',
      'mouseenter',
      'pointerdown',
      'mousedown',
      'pointerup',
      'mouseup',
    ]);
    el.click();
    await sleep(100);
  }

  function hover(el) {
    pointerEvents(el, ['pointerover', 'mouseover', 'mouseenter', 'pointermove', 'mousemove']);
  }

  function setNativeValue(el, value) {
    const proto = Object.getPrototypeOf(el);
    const setter = Object.getOwnPropertyDescriptor(proto, 'value')?.set;
    if (setter) setter.call(el, value);
    else el.value = value;
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
  }

  function editorContains(el, text) {
    const have = el.value != null && el.tagName !== 'DIV' ? el.value : textOf(el);
    const want = text.replace(/\s+/g, ' ').trim();
    return have.replace(/\s+/g, ' ').includes(want.slice(0, Math.min(48, want.length)));
  }

  async function clearEditable(el) {
    const sel = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(el);
    sel.removeAllRanges();
    sel.addRange(range);
    await sleep(30);
    try {
      document.execCommand('delete', false, null);
    } catch {
      /* ignore */
    }
    el.dispatchEvent(
      new InputEvent('beforeinput', {
        bubbles: true,
        cancelable: true,
        inputType: 'deleteContentBackward',
      }),
    );
    await sleep(40);
  }

  function syntheticPaste(el, text) {
    const dt = new DataTransfer();
    dt.setData('text/plain', text);
    const ev = new ClipboardEvent('paste', {
      bubbles: true,
      cancelable: true,
      composed: true,
      clipboardData: dt,
    });
    if (!ev.clipboardData) Object.defineProperty(ev, 'clipboardData', { value: dt });
    return el.dispatchEvent(ev);
  }

  async function fillPrompt(el, text) {
    await focusLikeUser(el);
    if (el.tagName === 'TEXTAREA' || el.tagName === 'INPUT') {
      setNativeValue(el, '');
      setNativeValue(el, text);
      await sleep(100);
      if (editorContains(el, text)) return 'native setter';
      throw new Error('Text did not stick in the textarea');
    }
    await clearEditable(el);
    await focusLikeUser(el);

    syntheticPaste(el, text);
    await sleep(200);
    if (editorContains(el, text)) return 'synthetic paste';

    el.dispatchEvent(
      new InputEvent('beforeinput', {
        bubbles: true,
        cancelable: true,
        composed: true,
        inputType: 'insertText',
        data: text,
      }),
    );
    el.dispatchEvent(
      new InputEvent('input', {
        bubbles: true,
        composed: true,
        inputType: 'insertText',
        data: text,
      }),
    );
    await sleep(200);
    if (editorContains(el, text)) return 'insertText event';

    try {
      document.execCommand('insertText', false, text);
    } catch {
      /* ignore */
    }
    await sleep(200);
    if (editorContains(el, text)) return 'execCommand';

    throw new Error(
      'Could not set the prompt text in a way Flow accepts. Type one prompt by hand once, then retry.',
    );
  }

  async function dismissOverlays() {
    for (let i = 0; i < 3; i++) {
      const { el } = firstVisible(S.dismissOverlays);
      if (!el) return;
      el.click();
      await sleep(300);
    }
  }

  // ---------- completion detection ----------
  function waitForCompletion({ timeoutMs, before, promptText }) {
    return new Promise((resolve, reject) => {
      const start = Date.now();
      const known = new Set(before);
      const found = new Map(); // key -> { img, at }
      let lastNewAt = 0;
      let addedText = '';
      const promptHead = promptText.slice(0, 40).toLowerCase();

      const observer = new MutationObserver((records) => {
        for (const rec of records) {
          for (const node of rec.addedNodes) {
            if (node.nodeType !== 1 && node.nodeType !== 3) continue;
            const t = textOf(node.nodeType === 3 ? node.parentElement : node);
            if (t && t.length < 600 && !t.toLowerCase().includes(promptHead)) addedText += ' ' + t;
          }
        }
        addedText = addedText.slice(-4000);
      });
      observer.observe(document.body, { childList: true, subtree: true, characterData: true });

      const finish = (fn, arg) => {
        observer.disconnect();
        clearInterval(timer);
        fn(arg);
      };

      const timer = setInterval(() => {
        if (aborted) return finish(reject, { kind: 'aborted', error: 'Aborted' });
        const now = Date.now();

        // 1. Limits: stop, never work around.
        const msgs = messagesText() + ' ' + addedText;
        const quota = matchPattern(msgs, S.quotaPatterns);
        if (quota)
          return finish(reject, {
            kind: 'quota',
            error: `${quota} (${msgs.trim().slice(0, 160)})`,
          });

        // 2. New results.
        for (const img of resultImages()) {
          const key = imageKey(img);
          if (!key || known.has(key) || found.has(key)) continue;
          found.set(key, { img, at: now });
          lastNewAt = now;
        }

        // 3. Explicit failure after submit (only once nothing new is arriving).
        if (!found.size && now - start > 5000) {
          const fail = matchPattern(messagesText(), S.failurePatterns);
          if (fail)
            return finish(reject, {
              kind: 'failed',
              error: `Flow showed: ${messagesText().slice(0, 160)}`,
            });
        }

        // 4. Finished = new image(s) and nothing arrived for SETTLE_MS, and no spinner (or spinner stuck past fallback).
        if (found.size) {
          const quiet = now - lastNewAt;
          const busy = queryAll(S.progressIndicators.join(','), resultRoot()).some(isVisible);
          if ((quiet >= SETTLE_MS && !busy) || quiet >= SETTLE_FALLBACK_MS) {
            return finish(resolve, { images: Array.from(found.values()).map((f) => f.img) });
          }
        }

        if (now - start > timeoutMs)
          return finish(reject, {
            kind: 'timeout',
            error: `No new result within ${Math.round(timeoutMs / 1000)}s`,
          });
      }, 1000);
    });
  }

  // ---------- downloads ----------
  async function blobToDataUrl(url) {
    const res = await fetch(url);
    const blob = await res.blob();
    const dataUrl = await new Promise((resolve, reject) => {
      const fr = new FileReader();
      fr.onload = () => resolve(fr.result);
      fr.onerror = reject;
      fr.readAsDataURL(blob);
    });
    const ext = (blob.type.split('/')[1] || 'png').replace('jpeg', 'jpg');
    return { dataUrl, ext };
  }

  function tileOf(img) {
    for (const sel of S.resultTile) {
      try {
        const t = img.closest(sel);
        if (t) return t;
      } catch {
        /* bad selector */
      }
    }
    return img.parentElement?.parentElement || img.parentElement;
  }

  async function clickFlowDownload(img) {
    const tile = tileOf(img);
    if (!tile) return false;
    tile.scrollIntoView({ block: 'center' });
    hover(tile);
    hover(img);
    await sleep(400);
    let { el: btn } = firstVisible(S.downloadButton, tile);
    if (!btn) {
      const { el: menu } = firstVisible(S.tileMenuButton, tile);
      if (menu) {
        await clickLikeUser(menu);
        await sleep(500);
        btn =
          firstVisible(S.downloadButton).el ||
          queryAll('[role="menu"] [role="menuitem"]').find(
            (b) =>
              isVisible(b) && S.downloadMenuTexts.some((t) => textOf(b).toLowerCase().includes(t)),
          );
      }
    }
    if (!btn) {
      document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
      return false;
    }
    await clickLikeUser(btn);
    await sleep(600);
    // A size sub-menu (1K / 2K / 4K / Original) may appear: pick the first option.
    // Only menu items: never a page button (a resolution toggle in the prompt bar must not be touched).
    const option = queryAll(
      '[role="menu"] [role="menuitem"], [role="listbox"] [role="option"]',
    ).find((b) => isVisible(b) && /\b(1k|2k|4k|original|full size|png|jpe?g)\b/i.test(textOf(b)));
    if (option) {
      await clickLikeUser(option);
      await sleep(400);
    }
    document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
    return true;
  }

  async function downloadImages(images, index, promptText) {
    let count = 0;
    for (const img of images) {
      try {
        if (await clickFlowDownload(img)) {
          count++;
          await log('info', "Downloaded via Flow's own download button.", index);
          continue;
        }
        const src = imageKey(img);
        let payload;
        if (src.startsWith('blob:') || src.startsWith('data:')) {
          const { dataUrl, ext } = await blobToDataUrl(src);
          payload = { url: dataUrl, ext };
        } else payload = { url: src, ext: /\.jpe?g(\?|$)/i.test(src) ? 'jpg' : 'png' };
        const r = await send({
          type: 'DOWNLOAD',
          index: index < 0 ? 0 : index,
          prompt: promptText,
          ...payload,
        });
        if (r?.ok) {
          count++;
          await log('info', `Saved ${r.filename}`, index);
        } else await log('warn', `Download failed: ${r?.error || 'no answer'}`, index);
      } catch (e) {
        await log('warn', `Download error: ${e?.message || e}`, index);
      }
    }
    return count;
  }

  // ---------- one prompt, end to end ----------
  async function runPrompt({ id, index, text, timeoutMs, autoDownload, test }) {
    running = true;
    aborted = false;
    const heartbeat = setInterval(() => send({ type: 'HEARTBEAT' }), 20_000);
    let result;
    try {
      await dismissOverlays();
      const editor = findPromptEditor();
      if (!editor)
        throw {
          kind: 'error',
          error:
            'Prompt box not found. Open a Flow project (…/flow/project/…) and run Selector Debug.',
        };
      const how = await fillPrompt(editor, text);
      await log('info', `Prompt text set (${how}).`, index);

      let btn = findGenerateButton(editor);
      for (let i = 0; i < 20 && (!btn || isDisabled(btn)); i++) {
        await sleep(250);
        btn = findGenerateButton(editor);
      }
      if (!btn) throw { kind: 'error', error: 'Generate button not found. Run Selector Debug.' };
      if (isDisabled(btn))
        throw { kind: 'error', error: 'Generate button stayed disabled after filling the prompt.' };

      const before = resultImages().map(imageKey);
      await clickLikeUser(btn);
      await log(
        'info',
        `Clicked Generate. Waiting up to ${Math.round(timeoutMs / 1000)}s (${before.length} existing image(s) ignored).`,
        index,
      );

      const { images } = await waitForCompletion({ timeoutMs, before, promptText: text });
      await log('info', `Generation finished with ${images.length} new image(s).`, index);
      let downloaded = 0;
      if (autoDownload) downloaded = await downloadImages(images, index, text);
      result = { ok: true, images: images.map(imageKey).map((u) => u.slice(0, 200)), downloaded };
    } catch (e) {
      const kind = e?.kind || 'error';
      const error = e?.error || e?.message || String(e);
      result = { ok: false, kind, error };
      await log(kind === 'quota' ? 'error' : 'warn', `${kind}: ${error}`, index);
    } finally {
      clearInterval(heartbeat);
      running = false;
      try {
        document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
      } catch {
        /* ignore */
      }
    }
    await send({ type: 'PROMPT_RESULT', id, result, test: !!test });
  }

  // ---------- selector debug ----------
  function debugSelectors() {
    const groups = [
      'promptInput',
      'generateButton',
      'resultContainers',
      'resultTile',
      'resultImage',
      'progressIndicators',
      'downloadButton',
      'tileMenuButton',
      'dismissOverlays',
      'messageContainers',
    ];
    const report = { url: location.href, groups: {}, chosen: {} };
    for (const g of groups) {
      report.groups[g] = S[g].map((sel) => {
        const all = queryAll(sel);
        return { selector: sel, count: all.length, visible: all.filter(isVisible).length };
      });
    }
    const editor = findPromptEditor();
    const btn = findGenerateButton(editor);
    report.chosen.promptInput = describe(editor);
    report.chosen.generateButton = btn ? { ...describe(btn), disabled: isDisabled(btn) } : null;
    const imgs = resultImages();
    report.chosen.resultImages = {
      count: imgs.length,
      sample: imgs.slice(0, 3).map((i) => ({
        src: imageKey(i).slice(0, 120),
        w: i.naturalWidth,
        h: i.naturalHeight,
        tile: describe(tileOf(i))?.html?.slice(0, 160),
      })),
    };
    report.chosen.messages = messagesText().slice(0, 300);
    report.chosen.isProjectPage = /\/flow\/project\//.test(location.pathname);
    return report;
  }

  // ---------- messages ----------
  chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
    if (sender.id !== chrome.runtime.id) return;
    switch (msg?.type) {
      case 'PING':
        sendResponse({ ok: true, running, url: location.href });
        break;
      case 'RUN_PROMPT':
        if (running) sendResponse({ ok: false, error: 'A prompt is already running in this tab' });
        else {
          sendResponse({ ok: true });
          runPrompt(msg);
        }
        break;
      case 'ABORT':
        aborted = true;
        sendResponse({ ok: true });
        break;
      case 'DEBUG_SELECTORS':
        sendResponse(debugSelectors());
        break;
      default:
        sendResponse({ ok: false, error: 'unknown message' });
    }
  });

  console.log(TAG, 'content script ready on', location.href);
})();
