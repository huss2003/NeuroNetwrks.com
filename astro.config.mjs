import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import cloudflare from '@astrojs/cloudflare';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://neuronetwrks.com',
  output: 'static', // every page prerendered
  adapter: cloudflare(), // used only by src/pages/api/*
  trailingSlash: 'never',
  integrations: [mdx(), sitemap({ filter: (p) => !p.includes('/apply/thanks') })],
  vite: { plugins: [tailwindcss()] },
  prefetch: { defaultStrategy: 'viewport', prefetchAll: false },
});
