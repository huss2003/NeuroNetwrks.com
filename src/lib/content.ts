import { getCollection } from 'astro:content';

const order = [
  'ai-foundation',
  'ai-ml-engineering',
  'software-development',
  'data-science-ai',
  'product-ux-ai-design',
  'cybersecurity',
];

export async function getPrograms() {
  const all = await getCollection('programs');
  return all.sort((a, b) => order.indexOf(a.data.slug) - order.indexOf(b.data.slug));
}

export async function getAudiences() {
  const order = ['students', 'parents', 'schools', 'professionals'];
  const all = await getCollection('audiences');
  return all.sort((a, b) => order.indexOf(a.data.slug) - order.indexOf(b.data.slug));
}

/** FAQs by file id, in the order requested. Unknown ids are skipped. */
export async function getFaqs(ids: string[]) {
  const all = await getCollection('faqs');
  return ids
    .map((id) => all.find((f) => f.id === id))
    .filter((f) => !!f)
    .map((f) => ({ q: f.data.q, a: f.data.a }));
}

export async function getFaqGroup(group: string) {
  const all = await getCollection('faqs');
  return all.filter((f) => f.data.group === group).map((f) => ({ q: f.data.q, a: f.data.a }));
}

/** Published posts only: drafts and future-dated posts are excluded until their date. */
export async function getPublishedPosts() {
  const now = new Date();
  const all = await getCollection('posts', (p) => !p.data.draft && p.data.pubDate <= now);
  return all.sort((a, b) => b.data.pubDate.valueOf() - a.data.pubDate.valueOf());
}

export const programMeta = (d: { durationYears: number; totalHours: number }) =>
  `${d.durationYears} ${d.durationYears === 1 ? 'year' : 'years'} · ${d.totalHours} hours`;
