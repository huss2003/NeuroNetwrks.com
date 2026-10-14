// @ts-check
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://neuronetwrks.com',
  output: 'static', // every page prerendered; only src/pages/api/* opts out
  adapter: cloudflare(),
  trailingSlash: 'never',
  build: { inlineStylesheets: 'always' },
  integrations: [
    mdx(),
    sitemap({ filter: (p) => !p.includes('/apply/thanks') && !p.includes('/dev/') }),
  ],
  vite: { plugins: [tailwindcss()] },
  prefetch: { defaultStrategy: 'viewport', prefetchAll: false },
});
