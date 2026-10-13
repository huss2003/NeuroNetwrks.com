# neuronetwrks.com (NeuroNetworks AI Ed)

India-first marketing site for AI, data, software, cybersecurity and UX courses (Class 10 entry). Brand: logo in `docs/source/logo.jpg`; green `#49B716`, blue `#086BE9`, ink `#0B1F3F`.

## Stack
Astro 7 (static, prerendered) on Cloudflare Workers static assets (not Pages). Tailwind v4 via `@tailwindcss/vite`. GSAP + Lenis in small script islands. One Worker route `/api/enquiry` (Turnstile, Google Sheets, email). Full tool list: `docs/TOOLS.md`. Design reference: `docs/design/*.dc.html`.

## Commands
`npm run dev` · `npx astro check` · `npm run build` · `npx wrangler deploy` (deploys run from GitHub Actions after PR merge)

## Hard rules
- Static by default. No `client:load` for decorative work; lazy-load any WebGL (`client:visible`).
- Every page: title, description, canonical, `lang="en-IN"`, JSON-LD.
- Images only via `astro:assets`. Self-host fonts. No particle backgrounds, no Spline on home, no `<ClientRouter />` unless approved.
- LCP element is real HTML text or an image, never a canvas. Respect `prefers-reduced-motion`.
- Budgets: LCP ≤ 1.8 s, INP ≤ 150 ms, homepage JS ≤ 100 KB.
- Never promise placement, internships or exam passes. Fees and dates stay placeholders until the owner supplies them.
- Forms: parent/guardian first for under-18s, unticked consent, stored with timestamp and notice version (DPDP). No secrets in the repo or `.mcp.json`.
- Use Context7 for Astro, GSAP and Tailwind v4 docs before writing code.

## Workflow
Plan mode first, one phase per session, `/compact` between phases. Run `astro check` and the audits (Lighthouse CI, pa11y) and read summaries only. Open PRs; do not merge without the owner.
