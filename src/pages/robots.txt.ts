import type { APIRoute } from 'astro';

const production = import.meta.env.PUBLIC_ENV === 'production';

const prodBody = `User-agent: *
Allow: /
Disallow: /api/
Disallow: /apply/thanks

User-agent: OAI-SearchBot
Allow: /
User-agent: ChatGPT-User
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Claude-SearchBot
Allow: /
User-agent: Claude-User
Allow: /

# Training crawlers: owner decision pending (see docs/PLAN.md section 8)
User-agent: GPTBot
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Google-Extended
Allow: /

Sitemap: https://neuronetwrks.com/sitemap-index.xml
`;

export const GET: APIRoute = () =>
  new Response(production ? prodBody : 'User-agent: *\nDisallow: /\n', {
    headers: { 'Content-Type': 'text/plain; charset=utf-8' },
  });
