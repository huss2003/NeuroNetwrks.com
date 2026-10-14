import type { APIRoute } from 'astro';
import { getPrograms, getAudiences } from '../lib/content';
import { site } from '../data/site';
import { abs } from '../lib/seo';

export const GET: APIRoute = async () => {
  const programs = await getPrograms();
  const audiences = await getAudiences();
  const lines = [
    `# ${site.name}`,
    '',
    `> ${site.name} teaches AI, software development, data science, product and UX design and cybersecurity to students in India who have passed Class 10. Tagline: ${site.tagline}.`,
    '',
    '## Programs',
    ...programs.map(
      (p) => `- [${p.data.name}](${abs(`/programs/${p.data.slug}`)}): ${p.data.summary}`,
    ),
    '',
    '## Audiences',
    ...audiences
      .filter((a) => !a.data.answer.includes('{{CONFIRM'))
      .map((a) => `- [${a.data.name}](${abs(`/for/${a.data.slug}`)})`),
    '',
    '## Site',
    `- [Admissions](${abs('/admissions')})`,
    `- [About](${abs('/about')})`,
    `- [Resources](${abs('/resources')})`,
    '',
  ];
  return new Response(lines.join('\n'), {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
};
