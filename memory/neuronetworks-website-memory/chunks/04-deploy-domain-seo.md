# 04 Deploy, domain, SEO

## Deploy (production)
1. `python3 tools/preview-gen/build.py`
2. Copy `site-preview/` into a scratch dir D (as D/site-preview), then in D:
   `npx --yes vercel@latest link --yes --project neuronetwrks-preview` (first time) and `npx vercel@latest deploy --prod --yes`.
   Needs Vercel auth in the session (connector/CLI login); never print tokens.
3. `python3 tools/preview-gen/indexnow.py` (notify Bing). Verify https://neuronetwrks.com with curl.
- Preview URL: https://neuronetwrks-preview.vercel.app. Owner said: commit to git but deploy only when asked.
- Lesson: a big redesign once broke the site; owner asked to revert. Screenshot-check desktop 1440 + mobile 390 before deploy.

## Domain
- Registrar/DNS: Squarespace. Apex neuronetwrks.com → Vercel, www → redirect to apex, HTTPS issued.
  Google Workspace MX + SPF records kept. Search Console TXT added.

## Analytics / search
- GA4 G-1D2KJQ9RCF, loads only after cookie consent ("Allow analytics"). Events: program_view, talk_click, scroll_75, outbound_click.
- Google Search Console: Domain property verified; sitemap submitted as FULL URL https://neuronetwrks.com/sitemap.xml.
- Bing Webmaster: import from GSC (pending owner). IndexNow key served from site.
- SEO/AEO/GEO done: titles ≤60, meta ≤155, canonicals, OG/Twitter, JSON-LD (Org, WebSite, Breadcrumb, FAQPage, Course,
  projects), answer-first H2s, llms.txt, AI bots allowed. Keyword map: docs/seo/keyword-map.md ("after 10th" intent).
- Promotion kit: docs/marketing/ (launch campaign, social setup, first posts, listings, PR & partnerships).
