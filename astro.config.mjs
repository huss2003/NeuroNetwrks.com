// @ts-check
import { execFileSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import tailwindcss from '@tailwindcss/vite';

/**
 * Source file that holds a page's content, so sitemap lastmod reflects real edits (from git history).
 * @param {string} pathname
 */
function sourceFor(pathname) {
  const p = pathname.replace(/\/$/, '') || '/';
  const candidates = [];
  let m;
  if ((m = p.match(/^\/programs\/([^/]+)$/))) candidates.push(`src/content/programs/${m[1]}.mdx`);
  else if ((m = p.match(/^\/for\/([^/]+)$/))) candidates.push(`src/content/audiences/${m[1]}.mdx`);
  else if (p === '/') candidates.push('src/pages/index.astro');
  else candidates.push(`src/pages${p}.astro`, `src/pages${p}/index.astro`);
  return candidates.find((c) => existsSync(c));
}

/** @param {string} pathname */
function lastModified(pathname) {
  const file = sourceFor(pathname);
  if (!file) return undefined;
  try {
    const iso = execFileSync('git', ['log', '-1', '--format=%cI', '--', file], {
      encoding: 'utf8',
    }).trim();
    return iso ? new Date(iso) : undefined;
  } catch {
    return undefined; // no git history (for example a shallow export): omit lastmod rather than guess
  }
}

export default defineConfig({
  site: 'https://neuronetwrks.com',
  output: 'static', // every page prerendered; only src/pages/api/* opts out
  adapter: cloudflare(), // used only by src/pages/api/*
  trailingSlash: 'never',
  build: { inlineStylesheets: 'always' },
  integrations: [
    mdx(),
    sitemap({
      filter: (p) => !p.includes('/apply/thanks') && !p.includes('/dev/'),
      serialize(item) {
        const lastmod = lastModified(new URL(item.url).pathname);
        return lastmod ? { ...item, lastmod: lastmod.toISOString() } : item;
      },
    }),
  ],
  vite: { plugins: [tailwindcss()] },
  prefetch: { defaultStrategy: 'viewport', prefetchAll: false },
});
