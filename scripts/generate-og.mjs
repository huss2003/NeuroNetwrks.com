// Renders one 1200x630 social card per indexable page into public/og/ (committed). Run after a build:
//   npm run build && npm run og
// It reads titles and descriptions from the built HTML, so cards always match the pages.
// Fonts are the self-hosted ones; Chromium comes from Playwright (PW_CHROMIUM overrides the path).
import { readdirSync, readFileSync, writeFileSync, mkdirSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { chromium } from '@playwright/test';

const dist = 'dist/client';
const out = 'public/og';
mkdirSync(out, { recursive: true });

const b64 = (p) => readFileSync(p).toString('base64');
const display = b64(
  'node_modules/@fontsource-variable/bricolage-grotesque/files/bricolage-grotesque-latin-wght-normal.woff2',
);
const body = b64(
  'node_modules/@fontsource-variable/ibm-plex-sans/files/ibm-plex-sans-latin-wght-normal.woff2',
);
const mark = readFileSync('src/assets/brand/logo-mark.svg', 'utf8');
const css = readFileSync('src/styles/global.css', 'utf8');
const token = (n) => css.match(new RegExp(`--color-${n}:\\s*(#[0-9a-fA-F]{6})`))[1];
const C = {
  blue: token('blue-600'),
  green: token('green-600'),
  ink: token('ink'),
  slate: token('slate'),
  soft: token('bg-soft'),
};

function pages(dir, base = '') {
  const found = [];
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) {
      if (name === '_astro' || name === 'dev' || name === 'og') continue;
      found.push(...pages(p, `${base}/${name}`));
    } else if (name === 'index.html') found.push(base || '/');
  }
  return found;
}

const meta = (html, re) =>
  (html.match(re) ?? [])[1]
    ?.replace(/&amp;/g, '&')
    .replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"');
const cards = [];
for (const path of pages(dist)) {
  const html = readFileSync(join(dist, path === '/' ? '' : path, 'index.html'), 'utf8');
  if (
    /name="robots" content="noindex/.test(html) &&
    !/staging/.test(process.env.OG_ALLOW_NOINDEX ?? '')
  ) {
    // staging builds add noindex to every page; only skip pages that are noindex by design
    if (/\/apply\/thanks|\/dev\//.test(path)) continue;
  }
  const title = meta(html, /<title>([^<]*)<\/title>/) ?? 'NeuroNetworks AI Ed';
  const description = meta(html, /<meta name="description" content="([^"]*)"/) ?? '';
  const slug = path === '/' ? 'home' : path.replace(/^\//, '').replace(/\//g, '-');
  cards.push({ slug, title: title.replace(/\s*\|\s*NeuroNetworks.*$/, ''), description });
}
cards.push({
  slug: 'default',
  title: 'AI, data and software careers, taught from zero',
  description: 'Programs for students after Class 10, built on monthly projects.',
});

const clip = (d) => {
  if (d.length <= 125) return d.replace(/</g, '&lt;');
  return (
    d
      .slice(0, 125)
      .replace(/\s+\S*$/, '')
      .replace(/[,;:.]$/, '')
      .replace(/</g, '&lt;') + '…'
  );
};

const template = ({
  title,
  description,
}) => `<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{font-family:D;src:url(data:font/woff2;base64,${display}) format('woff2');font-weight:200 800}
@font-face{font-family:B;src:url(data:font/woff2;base64,${body}) format('woff2');font-weight:100 700}
*{box-sizing:border-box;margin:0}
body{width:1200px;height:630px;background:#fff;color:${C.ink};font-family:B,sans-serif;position:relative;overflow:hidden}
.bar{position:absolute;left:0;top:0;bottom:0;width:18px;background:${C.blue}}
.dot{position:absolute;left:0;bottom:0;width:18px;height:90px;background:${C.green}}
.wrap{position:absolute;left:86px;right:80px;top:70px;bottom:64px;display:flex;flex-direction:column}
.tag{font:700 26px D;color:${C.blue};letter-spacing:-0.01em}
h1{font:800 ${title.length > 48 ? 66 : 80}px/1 D;letter-spacing:-0.035em;margin-top:26px;max-width:980px;text-wrap:balance}
p{font-size:28px;line-height:1.4;color:${C.slate};margin-top:28px;max-width:900px}
.foot{margin-top:auto;display:flex;align-items:center;gap:18px}
.foot svg{height:64px;width:auto}
.foot span{font:800 30px D;letter-spacing:-0.02em}
.foot em{font-style:normal;color:${C.slate};font-size:24px;margin-left:auto}
</style></head><body><div class="bar"></div><div class="dot"></div><div class="wrap">
<div class="tag">Learn · Develop · Create</div><h1>${title.replace(/</g, '&lt;')}</h1>
<p>${clip(description)}</p>
<div class="foot">${mark.replace('<svg ', '<svg height="64" ')}<span>NeuroNetworks AI Ed</span><em>neuronetwrks.com</em></div>
</div></body></html>`;

const browser = await chromium.launch(
  process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {},
);
const page = await browser.newPage({ viewport: { width: 1200, height: 630 } });
for (const c of cards) {
  await page.setContent(template(c), { waitUntil: 'load' });
  await page.evaluate(() => globalThis.document.fonts.ready);
  writeFileSync(join(out, `${c.slug}.png`), await page.screenshot({ type: 'png' }));
}
await browser.close();
console.log(`Wrote ${cards.length} social cards to ${out}/`);
