/**
 * ALL Flow DOM selectors live here. Edit this file when Google changes the UI.
 *
 * Every entry is an ordered list of fallbacks; the first one that matches a
 * visible element wins. Never rely on auto-generated class names (sc-xxxx,
 * css-xxxx): they change on every deploy.
 *
 * Provenance (October 2026): Flow's project page uses a Slate.js editor for
 * the prompt box (div[role="textbox"][data-slate-editor]) and a "Create"
 * button whose icon is the Material symbol "arrow_forward". Those two facts
 * were taken from the source of public extensions that automate Flow, not
 * from a live session in this build. Use the panel's "Selector Debug" button
 * on a real project page and fix anything that reports "no match".
 *
 * Loaded as a plain content script before content.js, so it attaches to
 * globalThis; also imported by the unit tests as a module-free global.
 */
globalThis.FLOW_SELECTORS = {
  /** The box you type the prompt into. */
  promptInput: [
    'div[role="textbox"][data-slate-editor="true"][contenteditable="true"]',
    'div[contenteditable="true"][data-slate-editor="true"]',
    'div[contenteditable="true"][role="textbox"][aria-multiline="true"]',
    'div[contenteditable="true"][role="textbox"]',
    'textarea[aria-label*="prompt" i]',
    'textarea[placeholder*="prompt" i]',
    'textarea[placeholder*="describe" i]',
    'textarea[placeholder*="create" i]',
    '[data-testid*="prompt" i] textarea',
    '[data-testid*="prompt" i] [contenteditable="true"]',
    'textarea',
  ],

  /**
   * Words found in the empty-state placeholder of the prompt box. When more
   * than one editable box is on screen, the one whose placeholder contains
   * one of these wins; otherwise the lowest one on screen (the prompt bar).
   */
  promptPlaceholderWords: ['what do you want', 'create', 'generate', 'describe', 'prompt'],

  /** The Generate / Create button. */
  generateButton: [
    'button[aria-label="Create"]',
    'button[aria-label*="create" i]',
    'button[aria-label*="generate" i]',
    'button[data-testid*="generate" i]',
    'button[data-testid*="submit" i]',
    'button[type="submit"]',
  ],

  /**
   * Fallback: a visible <button> containing a Material Symbols icon with one
   * of these ligature names (Flow's Create button shows "arrow_forward").
   */
  generateButtonIconNames: ['arrow_forward', 'send', 'auto_awesome'],

  /** Fallback: visible button whose text equals one of these (case-insensitive). */
  generateButtonTexts: ['create', 'generate', 'run'],

  /**
   * Containers that hold generated results. Used to scope the image scan;
   * if none match, every <img> in the document is scanned instead.
   */
  resultContainers: [
    '[data-testid*="result" i]',
    '[data-testid*="gallery" i]',
    '[data-testid*="scene" i]',
    '[role="list"]',
    'main',
  ],

  /**
   * A single result tile. Used to find the tile around a new image so its
   * own download button can be clicked. `closest()` is run with each entry.
   */
  resultTile: [
    '[data-testid*="tile" i]',
    '[data-testid*="card" i]',
    '[data-testid*="media" i]',
    '[role="listitem"]',
    'article',
    'figure',
  ],

  /** Images that count as a finished result (must also be loaded and >= minResultImageSize). */
  resultImage: [
    'img[src^="blob:"]',
    'img[src*="googleusercontent" i]',
    'img[src^="https://"]',
    'img[src^="data:image"]',
  ],
  minResultImageSize: 160,

  /** Things that mean "still generating": a visible one blocks completion. */
  progressIndicators: [
    '[role="progressbar"]',
    'progress',
    '[aria-busy="true"]',
    '[data-testid*="loading" i]',
    '[data-testid*="progress" i]',
  ],

  /** Flow's own download control, searched inside the result tile first, then the document. */
  downloadButton: [
    'button[aria-label="Download"]',
    'button[aria-label*="download" i]',
    '[role="menuitem"][aria-label*="download" i]',
    'a[download]',
    'button[data-testid*="download" i]',
  ],
  /** Text of a menu item that triggers a download (used when the tile shows a "more" menu). */
  downloadMenuTexts: ['download'],
  /** A tile's "more options" button, clicked before searching for a download menu item. */
  tileMenuButton: [
    'button[aria-label*="more" i]',
    'button[aria-label*="options" i]',
    'button[aria-haspopup="menu"]',
  ],

  /** Overlays that may cover the page; closed before every prompt. */
  dismissOverlays: [
    'button[aria-label="Close"]',
    'button[aria-label="Dismiss"]',
    'button[aria-label="Got it"]',
  ],

  /** Where error / status messages appear. Only these are scanned for quota and failure text. */
  messageContainers: [
    '[role="alert"]',
    '[role="status"]',
    '[role="dialog"]',
    '[aria-live]',
    '[data-testid*="toast" i]',
    '[data-testid*="snackbar" i]',
    '[data-testid*="error" i]',
  ],

  /** If one of these phrases shows up in a message container, the queue STOPS (no workarounds). */
  quotaPatterns: [
    'quota',
    'rate limit',
    'rate-limit',
    'too many requests',
    'out of credits',
    'no credits',
    'insufficient credits',
    'not enough credits',
    'credits have run out',
    'run out of credits',
    'daily limit',
    'usage limit',
    'limit reached',
    'reached your limit',
    'try again tomorrow',
    'try again later',
    'unusual traffic',
    'verify you are human',
    'captcha',
  ],

  /** Phrases that mean this generation failed and may be retried. */
  failurePatterns: [
    'something went wrong',
    'failed to generate',
    'generation failed',
    'could not generate',
    'try again',
    'error',
    'blocked',
    'policy',
    'violat',
  ],
};
