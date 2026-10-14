// Automated /seo-check over the built site (dist/client). Hard failures exit 1; warnings are listed.
//   npm run build && npm run seo
// With PUBLIC_ENV=production, leftover {{CONFIRM placeholders also fail. Staging builds are noindex by design.
import { readdirSync, readFileSync, statSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const dist = 'dist/client';
const origin = 'https://neuronetwrks.com';
const production = process.env.PUBLIC_ENV === 'production';
const errors = [];
const warnings = [];
const fail = (page, msg) => errors.push(`${page}: ${msg}`);
const warn = (page, msg) => warnings.push(`${page}: ${msg}`);

function pages(dir, base = '') {
  const out = [];
  for (const n of readdirSync(dir)) {
    const p = join(dir, n);
    if (statSync(p).isDirectory()) {
      if (n === '_astro' || n === 'og') continue;
      out.push(...pages(p, `${base}/${n}`));
    } else if (n === 'index.html') out.push(base || '/');
  }
  return out;
}

const text = (html) =>
  html
    .replace(/<script[\s\S]*?<\/script>/g, ' ')
    .replace(/<style[\s\S]*?<\/style>/g, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/\s+/g, ' ');
const decode = (s) =>
  s
    .replace(/&amp;/g, '&')
    .replace(/&#39;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>');
const attr = (html, re) => {
  const v = (html.match(re) ?? [])[1];
  return v === undefined ? v : decode(v);
};
const words = (s) => s.split(/\s+/).filter(Boolean).length;

const required = {
  Course: ['name', 'description', 'provider'],
  EducationalOccupationalProgram: ['name', 'description', 'provider', 'timeToComplete'],
  WebSite: ['url', 'name'],
  BreadcrumbList: ['itemListElement'],
  FAQPage: ['mainEntity'],
  BlogPosting: ['headline', 'author', 'datePublished'],
  ItemList: ['itemListElement'],
};

const list = pages(dist).filter((p) => !p.startsWith('/dev'));
let answerFirst = 0;
let h2Total = 0;

for (const path of list) {
  const html = readFileSync(join(dist, path === '/' ? '' : path, 'index.html'), 'utf8');
  const id = path;
  const noindexByDesign = path === '/apply/thanks';

  const h1 = (html.match(/<h1[\s>]/g) ?? []).length;
  if (h1 !== 1) fail(id, `${h1} h1 elements`);

  const title = attr(html, /<title>([^<]*)<\/title>/) ?? '';
  const desc = attr(html, /<meta name="description" content="([^"]*)"/) ?? '';
  if (!title || title.length > 60) fail(id, `title length ${title.length}: ${title}`);
  if (!desc || desc.length > 155) fail(id, `description length ${desc.length}`);
  if (desc && desc.length < 70) warn(id, `short description (${desc.length})`);

  const canonical = attr(html, /<link rel="canonical" href="([^"]*)"/);
  const expected = origin + (path === '/' ? '' : path);
  if (canonical !== expected) fail(id, `canonical ${canonical} should be ${expected}`);
  if (canonical?.endsWith('/') && path !== '/') fail(id, 'canonical has trailing slash');

  const robots = attr(html, /<meta name="robots" content="([^"]*)"/) ?? '';
  const noindex = /noindex/.test(robots);
  if (production && noindex && !noindexByDesign && path !== '/404')
    fail(id, 'noindex in production build');
  if (!noindex && !/index, follow/.test(robots)) fail(id, `robots meta missing or odd: ${robots}`);
  if (noindexByDesign && !noindex) fail(id, 'must be noindex');

  for (const prop of [
    'og:title',
    'og:description',
    'og:url',
    'og:image',
    'og:type',
    'og:locale',
    'og:site_name',
  ]) {
    if (!new RegExp(`property="${prop}"`).test(html)) fail(id, `missing ${prop}`);
  }
  if (!/name="twitter:card" content="summary_large_image"/.test(html)) fail(id, 'twitter:card');
  const og = attr(html, /property="og:image" content="([^"]*)"/);
  if (og && !existsSync(join(dist, og.replace(origin, ''))))
    fail(id, `og image missing in build: ${og}`);
  if (!/rel="manifest"/.test(html)) fail(id, 'manifest link');
  if (!/lang="en-IN"/.test(html)) fail(id, 'html lang');

  // JSON-LD
  const blocks = [
    ...html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g),
  ].map((m) => m[1]);
  const nodes = [];
  for (const b of blocks) {
    try {
      const d = JSON.parse(b);
      nodes.push(...(d['@graph'] ?? [d]));
    } catch {
      fail(id, 'JSON-LD does not parse');
    }
  }
  const types = nodes.flatMap((n) => [].concat(n['@type'] ?? []));
  if (!blocks.length && !noindexByDesign) fail(id, 'no JSON-LD');
  if (path !== '/' && !noindexByDesign && path !== '/404' && !types.includes('BreadcrumbList'))
    fail(id, 'BreadcrumbList missing');
  for (const n of nodes) {
    for (const t of [].concat(n['@type'] ?? [])) {
      for (const prop of required[t] ?? [])
        if (n[prop] === undefined) fail(id, `${t} lacks ${prop}`);
    }
    if (n.offers) fail(id, 'offers present (no prices on this site)');
  }
  if (path.startsWith('/programs/') && path !== '/programs') {
    for (const t of ['Course', 'EducationalOccupationalProgram', 'FAQPage'])
      if (!types.includes(t)) fail(id, `${t} missing`);
  }
  // FAQ markup must match visible text
  const visible = text(html.replace(/<script[\s\S]*?<\/script>/g, ''));
  for (const n of nodes.filter((x) => x['@type'] === 'FAQPage')) {
    for (const q of n.mainEntity ?? [])
      if (!visible.includes(q.name)) fail(id, `FAQ question not visible: ${q.name}`);
  }

  // Content structure
  const levels = [...html.matchAll(/<h([1-6])[\s>]/g)].map((m) => Number(m[1]));
  levels.forEach(
    (l, i) =>
      i > 0 && l - levels[i - 1] > 1 && fail(id, `heading level jumps ${levels[i - 1]} to ${l}`),
  );
  for (const m of html.matchAll(/<img\b[^>]*>/g))
    if (!/\salt(=|\s|>)/.test(m[0])) fail(id, 'img without alt');
  for (const m of html.matchAll(
    /<h2[^>]*>[\s\S]*?<\/h2>\s*(?:<[^>]+>\s*)*?<p[^>]*>([\s\S]*?)<\/p>/g,
  )) {
    h2Total++;
    if (words(text(m[1])) >= 15) answerFirst++;
    else if (process.env.VERBOSE)
      warn(
        id,
        `H2 "${text(m[0].match(/<h2[^>]*>([\s\S]*?)<\/h2>/)[1]).trim()}" has a short first paragraph`,
      );
  }

  // Internal links resolve to a built page or file
  for (const m of html.matchAll(/<a\b[^>]*\shref="(\/[^"#?]*)/g)) {
    const href = m[1];
    if (href.startsWith('//')) continue;
    const clean = href.replace(/\/$/, '');
    const ok = [
      join(dist, clean, 'index.html'),
      join(dist, clean),
      join(dist, `${clean}.html`),
    ].some((f) => existsSync(f) && statSync(f).isFile());
    if (clean && !ok) fail(id, `broken internal link ${href}`);
    if (href.length > 1 && href.endsWith('/')) warn(id, `link with trailing slash ${href}`);
  }

  // Entity consistency: exact brand casing in visible text
  for (const m of visible.matchAll(/neuro\s?networks(?:\s+AI\s+Ed)?/gi)) {
    const v = m[0];
    if (
      v !== 'NeuroNetworks AI Ed' &&
      v !== 'NeuroNetworks' &&
      !/^neuronetwrks/i.test(v) &&
      !visible.includes('neuronetwrks.com')
    )
      warn(id, `brand written as "${v}"`);
    if (/^Neuronetworks/.test(v)) fail(id, `brand written as "${v}"`);
  }

  if (/\{\{CONFIRM/.test(html)) (production ? fail : warn)(id, '{{CONFIRM placeholder present');
}

// Site-level files
for (const f of [
  'robots.txt',
  'sitemap-index.xml',
  'sitemap-0.xml',
  'llms.txt',
  'llms-full.txt',
  'rss.xml',
  'manifest.webmanifest',
  '404.html',
]) {
  if (!existsSync(join(dist, f))) errors.push(`missing ${f}`);
}
const robots = readFileSync(join(dist, 'robots.txt'), 'utf8');
if (production) {
  for (const bot of [
    'OAI-SearchBot',
    'ChatGPT-User',
    'PerplexityBot',
    'Claude-SearchBot',
    'Claude-User',
  ]) {
    if (!robots.includes(`User-agent: ${bot}`)) errors.push(`robots.txt lacks ${bot}`);
  }
  if (!robots.includes('Sitemap: https://neuronetwrks.com/sitemap-index.xml'))
    errors.push('robots.txt lacks sitemap line');
}
const sm = readFileSync(join(dist, 'sitemap-0.xml'), 'utf8');
for (const bad of ['/dev/', '/apply/thanks', '/404'])
  if (sm.includes(bad)) errors.push(`sitemap contains ${bad}`);
const locs = [...sm.matchAll(/<loc>([^<]+)<\/loc>/g)].map((m) => m[1]);
if (locs.length !== list.filter((p) => p !== '/apply/thanks').length)
  warnings.push(`sitemap has ${locs.length} URLs, site has ${list.length - 1} indexable pages`);

console.log(
  `Checked ${list.length} pages. Answer-first paragraph (15+ words) under ${answerFirst} of ${h2Total} H2s.`,
);
if (warnings.length)
  console.log(
    `\n${warnings.length} warning(s):\n  ` + [...new Set(warnings)].slice(0, 30).join('\n  '),
  );
if (errors.length) {
  console.error(`\n${errors.length} error(s):\n  ` + errors.slice(0, 60).join('\n  '));
  process.exit(1);
}
console.log('\nseo-check passed');
