import type { APIRoute } from 'astro';

export const GET: APIRoute = () => {
  const production = import.meta.env.PUBLIC_ENV === 'production';
  const body = production
    ? [
        'User-agent: *',
        'Allow: /',
        'Disallow: /api/',
        'Disallow: /apply/thanks',
        '',
        ...[
          'OAI-SearchBot',
          'ChatGPT-User',
          'PerplexityBot',
          'Claude-SearchBot',
          'Claude-User',
        ].flatMap((b) => [`User-agent: ${b}`, 'Allow: /', '']),
        '# Training crawlers: owner decision (default allow)',
        ...['GPTBot', 'ClaudeBot', 'Google-Extended'].flatMap((b) => [
          `User-agent: ${b}`,
          'Allow: /',
          '',
        ]),
        'Sitemap: https://neuronetwrks.com/sitemap-index.xml',
        '',
      ].join('\n')
    : 'User-agent: *\nDisallow: /\n';
  return new Response(body, { headers: { 'Content-Type': 'text/plain; charset=utf-8' } });
};
