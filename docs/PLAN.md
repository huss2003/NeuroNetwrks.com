# Plan

Phases (one per session):
0. Scaffold: `npm create astro@latest`, Tailwind v4, Cloudflare config, fonts, brand tokens, CI (Lighthouse CI, pa11y, `astro check`).
1. Layout, SEO head (astro-seo, JSON-LD), sitemap, robots, llms.txt, OG images.
2. Home page from `docs/design/Main.dc.html`.
3. Program pages from `docs/source/*.docx` (content collection `programs`), starting with `docs/design/Program.dc.html`.
4. Enquiry Worker: Turnstile verify, Sheets append (service account), email, rate limit, honeypot, DPDP consent record.
5. Motion: GSAP, SplitText, Lenis; one lazy 3D ribbon at most.
6. Blog and guides (AEO: definitional H2s, FAQs).
7. DNS move Squarespace to Cloudflare keeping Google Workspace MX/SPF/DKIM/DMARC; GSC, Bing, GA4 via Partytown, IndexNow.
8. Audit and launch.

Source of truth for course content: `docs/source/`. Tooling: `docs/TOOLS.md`.
