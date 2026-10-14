import { site } from '../data/site';

export const abs = (path = '/') =>
  new URL(path, site.url).toString().replace(/\/$/, '') || site.url;

/** A value still holding a {{CONFIRM}} placeholder must never reach structured data. */
export const isPlaceholder = (v?: string) => !v || v.includes('{{CONFIRM');

/** Dev-time guard for the length rules in CLAUDE.md (title ≤ 60, description ≤ 155). */
export function checkSeo(path: string, title: string, description: string) {
  if (!import.meta.env.DEV) return;
  if (title.length > 60) console.warn(`[seo] ${path}: title is ${title.length} chars (max 60)`);
  if (description.length > 155)
    console.warn(`[seo] ${path}: description is ${description.length} chars (max 155)`);
}
