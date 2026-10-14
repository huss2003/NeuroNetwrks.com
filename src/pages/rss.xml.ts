import type { APIRoute } from 'astro';
import { getPublishedPosts } from '../lib/content';
import { site } from '../data/site';
import { abs } from '../lib/seo';

const esc = (s: string) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

export const GET: APIRoute = async () => {
  const posts = await getPublishedPosts();
  const items = posts
    .map(
      (p) =>
        `<item><title>${esc(p.data.title)}</title><link>${abs(`/resources/${p.id}`)}</link><guid>${abs(`/resources/${p.id}`)}</guid><pubDate>${p.data.pubDate.toUTCString()}</pubDate><description>${esc(p.data.description)}</description></item>`,
    )
    .join('');
  const xml = `<?xml version="1.0" encoding="UTF-8"?><rss version="2.0"><channel><title>${esc(site.name)} resources</title><link>${abs('/resources')}</link><description>Guides on learning AI and technology after Class 10.</description><language>en-in</language>${items}</channel></rss>`;
  return new Response(xml, { headers: { 'Content-Type': 'application/rss+xml; charset=utf-8' } });
};
