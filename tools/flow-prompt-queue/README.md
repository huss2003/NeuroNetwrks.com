# Flow Prompt Queue

A small Chrome extension (Manifest V3) that submits a list of prompts to
[Google Flow](https://flow.google.com) one at a time. You paste the
prompts, press Start, and it fills Flow's prompt box, clicks Create, waits for
the result, optionally downloads it, pauses for a random few seconds, and
moves on. It stops on its own if Flow shows a quota, rate-limit or credits
message. It never tries to get around limits or captchas.

Plain JavaScript, no build step, no dependencies.

## Install

1. Open `chrome://extensions` in Chrome.
2. Turn on **Developer mode** (top right).
3. Click **Load unpacked** and choose this folder (`tools/flow-prompt-queue`).
4. Pin the extension if you like. Clicking its icon opens the side panel.

After editing any file in this folder, press the reload icon on the
extension's card in `chrome://extensions` and reload the Flow tab.

## Use

1. Open a Flow **project** page (the URL looks like `flow.google.com/project/...`;
   the older `labs.google/fx/tools/flow` address also works) and sign in
   as usual. Choose the image mode and any settings in Flow yourself; the
   extension only types the prompt and presses Create.
2. Click the extension icon to open the side panel.
3. Paste prompts, one per line, or put `@@@NEXT@@@` on its own line between
   multi-line prompts. You can also paste a whole image-prompt script document
   (blocks with `Image 001 Prompt`, `[Script Segment Text]`, `Image Prompt:`,
   `Camera Angle:` and so on): only the `Image Prompt:` lines are queued. Or
   use **Import CSV** (first column = prompt, a header cell called `prompt` is
   skipped). Click **Add to queue**. A sample is in `examples/`.
4. Check **Settings**: delay range, timeout, retries, auto-download, and an
   optional prefix/suffix applied to every prompt (for example a style suffix).
5. Press **Start**. Watch the progress bar and the log.

### Flow only accepts a real click

Google Flow checks that the click on its "Start generation" arrow comes from
a real person (the browser's `isTrusted` flag). Scripted clicks and a
scripted Enter key are ignored. This extension does not work around that.
Instead, when the scripted click is ignored, the panel shows an amber "Your
turn" notice, the extension icon shows a `YOU` badge, and the log says
"YOUR TURN". Press the arrow in Flow yourself. The extension notices the
submission, waits for the image, downloads it if enabled, pauses, fills in
the next prompt and asks again. The "Wait for my click (s)" setting is how
long it waits for you (default 15 minutes); set it to 0 to mark the prompt
failed instead.

Buttons:

| Button | What it does |
| --- | --- |
| Start | Runs from the first pending prompt. |
| Pause | Lets the current generation finish, then waits. |
| Resume | Continues after a pause. |
| Stop | Aborts the wait, puts the current prompt back to pending, saves progress. |
| Retry failed | Marks failed prompts pending again. |
| Reset all to pending | Re-run everything. |
| Remove done | Drops finished prompts from the list. |
| Test first prompt only | Runs the first pending prompt once without changing the queue. Use this to check the page before a long run. |
| Selector Debug | Reports which selectors matched on the open Flow tab (see below). |

The queue, settings and log are saved in `chrome.storage.local`, so closing
the panel, reloading the extension or restarting Chrome does not lose them.
Press Start again to continue from the first unfinished prompt.

### Statuses

`pending` → `running` → `done` or `failed`. A failed or timed-out generation is
retried up to the number in Settings, then marked failed and skipped. A
quota/rate-limit/credits message stops the whole queue; the prompt stays
pending, the status pill turns red, and the extension icon shows a red `!`.

### Downloads

With **Auto-download** on, the extension first tries Flow's own download
control on each new result tile. If it cannot find one, it saves the image
itself through Chrome's downloads to `Downloads/flow/001_slug-of-prompt.png`.
Blob images are converted in the page; https images are fetched by Chrome
with your normal cookies.

## How it works

```
sidepanel.js  ──port──▶  background.js (queue state machine, queue.js)
                              │  chrome.tabs.sendMessage
                              ▼
                         content.js on the Flow tab (uses selectors.js)
```

- `queue.js` is the state machine (start, pause, resume, stop, retry, quota
  stop, watchdog, restore after restart). It has no Chrome calls so it can be
  unit-tested.
- `background.js` wires it to Chrome: storage, alarms (keeps the service
  worker alive and schedules delays over 25 s), downloads, messaging.
- `content.js` runs one prompt end to end: focus and fill the prompt box
  (native value setter for textareas, simulated paste for Slate/contenteditable
  boxes), click Create, then watch the DOM with a MutationObserver for new
  result images, progress indicators and error/limit messages.
- `selectors.js` holds every DOM selector, with fallbacks.

## Updating selectors when Flow's UI changes

All selectors are in `selectors.js`. Each entry is a list; the first entry
that matches a visible element wins. Never use auto-generated class names.

1. Open a Flow project page, open the panel, click **Selector Debug**.
2. Lines marked `MISS` had no visible match. For that group, right-click the
   element in Flow → Inspect, and look for a stable attribute: `aria-label`,
   `role`, `placeholder`, `data-testid`, `type`, or the button's text or icon
   name (Material Symbols show the icon name as text, e.g. `arrow_forward`).
3. Add a selector to the top of that list in `selectors.js`.
4. Reload the extension and the Flow tab, run Selector Debug again.

The "Chosen elements" section prints the element the extension would use, so
you can confirm it picked the right box and button.

Groups you are most likely to touch:

- `promptInput` — the prompt box.
- `generateButton` / `generateButtonIconNames` / `generateButtonTexts` — the Create button.
- `resultImage` / `minResultImageSize` — what counts as a finished result.
- `downloadButton` / `tileMenuButton` — Flow's download control inside a result tile.
- `quotaPatterns` — phrases that stop the queue.

## Tests

From the repository root:

```
npm run test:ext
```

This runs the queue state machine tests (`test/queue.test.mjs`) with Node's
built-in test runner: ordering and delays, prefix/suffix, retries, quota stop,
pause/resume, stop, watchdog timeout, restore after a service-worker restart,
queue editing, prompt parsing, CSV import and file-name slugs.

## Limits and notes

- Only the Flow domains (`flow.google.com`, `labs.google`) are in `host_permissions`; nothing else is contacted.
- The content script needs a Flow **project** page. The Flow home page has no prompt box.
- Keep the Flow tab open. It can be in the background, but if Chrome discards it the run fails and is retried.
- If the panel says the prompt text could not be set, type one prompt by hand once so Flow's editor is initialised, then press Start again.
- Google's terms apply to your use of Flow. This tool only automates what you would type yourself, at a human-like pace, and stops when Flow says to stop.
