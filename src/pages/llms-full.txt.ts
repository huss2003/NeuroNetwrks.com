import type { APIRoute } from 'astro';
import { getPrograms } from '../lib/content';
import { site } from '../data/site';
import { abs } from '../lib/seo';

export const GET: APIRoute = async () => {
  const programs = await getPrograms();
  const out = [`# ${site.name}`, '', site.tagline, ''];
  for (const { data: d } of programs) {
    out.push(`## ${d.name}`, `URL: ${abs(`/programs/${d.slug}`)}`, '', d.answer, '');
    out.push(
      `- Duration: ${d.durationYears} year(s), ${d.totalHours} hours, ${d.hoursPerWeek} hours a week`,
      `- Entry: ${d.entry}`,
      `- Assessment: ${d.assessment}`,
      '',
    );
    for (const y of d.years)
      out.push(
        `### ${y.title}${y.hours ? ` (${y.hours} hours)` : ''}`,
        ...y.modules.map((m, i) => `${i + 1}. ${m}`),
        '',
      );
    if (d.certifications.length)
      out.push('Certifications named in the roadmap: ' + d.certifications.join('; '), '');
    out.push('No job, internship, salary or exam result is guaranteed.', '');
  }
  return new Response(out.join('\n'), { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
