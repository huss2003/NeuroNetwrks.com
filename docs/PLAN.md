# PLAN: neuronetwrks.com (NeuroNetworks AI Ed)

Status: draft for owner approval. Owner: non-technical founder. Builder: Claude Code (Claude Max plan) working in a GitHub repo from Claude Code on the web. Companion files: `CLAUDE.md` (rules), `BUILD_PROMPT.md` (step-by-step build instructions), `TOOLS.md` (repos, skills, MCP servers).

## 1. Summary and goals
Build a premium, bright, editorial marketing website for NeuroNetworks AI Ed that:
1. Turns parents, students, professionals and schools into enquiries and applications.
2. Impresses investors on first load (craft, speed, clarity, credibility).
3. Ranks and gets cited for AI, course and learning searches in India (SEO) and appears in AI answers (AEO and GEO).
4. Collects leads into a Google Sheet and email, safely, in line with India's DPDP rules for children's data.

Why a new approach: the three HTML previews were rejected as generic and AI-looking and for the 3D brain/particle cliché. This plan changes the idea, not just the polish: type-led editorial design, real content from the owner's curricula, one meaningful signature motion (a scroll-drawn line linking Learn, Develop, Create), and one abstract 3D object that is not a brain.

Success measures: Lighthouse mobile ≥ 95 everywhere; LCP ≤ 1.8 s, INP ≤ 150 ms, CLS ≤ 0.05 on throttled mid-range Android; WCAG 2.2 AA; valid structured data; form to Sheet in under 3 s; 24 posts scheduled; indexed in Google and Bing within two weeks of launch.

## 2. Decisions and scope
| Topic | Decision |
|---|---|
| Domain | neuronetwrks.com (exact spelling), `www` redirects to apex |
| Market and language | India only, English only, `lang="en-IN"` |
| Framework | Astro 7, static output; Tailwind v4; MDX; TypeScript strict |
| Hosting | Cloudflare Workers static assets; one on-demand route `/api/enquiry` |
| Deploy | GitHub Actions on merge to `main`; preview deploys are noindex |
| Motion | GSAP (ScrollTrigger, SplitText) + Lenis; native CSS view transitions |
| 3D | One lazy Three.js ribbon in the closing CTA; static poster fallback |
| Forms | Turnstile + Worker route + Google Sheets API (service account) + email API |
| Analytics | GA4 after consent via Partytown; GSC; Bing Webmaster; IndexNow |
| Content | Six programs from the owner's .docx files; blog written and scheduled by Claude |
| Not in scope | Prices, login, payments, chatbot, multi-language, LMS, the Practical Lab IDE |
| Brand | Logo blue #006DEE, green #49B716, tagline "Learn · Develop · Create" |

## 3. Architecture
```
GitHub repo (private)
  ├─ PR ──► GitHub Actions: check, lint, build, Playwright, Lighthouse CI, pa11y
  └─ merge to main ──► wrangler deploy ──► Cloudflare Workers
                                             ├─ static assets (dist/): all pages, images, fonts, OG images
                                             └─ /api/enquiry (on demand)
                                                  ├─ Turnstile siteverify
                                                  ├─ Google Sheets API (service account JWT, Web Crypto)
                                                  └─ Email API (team notification + confirmation)
Cloudflare DNS (moved from Squarespace) ── keeps Google Workspace MX / SPF / DKIM
Daily cron (GitHub Actions) ──► rebuild ──► scheduled posts go live ──► IndexNow
```
Why this shape: static HTML is the best base for SEO and Core Web Vitals; the only dynamic part is the form; Cloudflare is now Astro's first-class host; GitHub Actions gives CI and the daily rebuild in one place.

## 4. Sitemap and page inventory
Home · Programs · AI Foundation · AI & ML Engineering · Software Development · Product & UX AI Design · Data Science & AI · Cybersecurity · For students · For parents · For schools · For professionals · About · Admissions · Apply · Apply/thanks (noindex) · Resources (hub, post pages, categories) · Contact · Privacy · Terms · 404. Generated: sitemap, robots, llms.txt, llms-full.txt, RSS.
Full per-page keyword, title, H1 and schema table is in `BUILD_PROMPT.md` section 3.1.

## 5. Design system (summary; details in BUILD_PROMPT Phase 1)
- **Colour:** blue leads, green is rare, blue-tinted ink, white and soft blue-white backgrounds. Green text uses a darker green for contrast. No purple, no cream, no gradients except the signature line (and optionally the ribbon).
- **Type:** self-hosted variable fonts, pairing chosen after a three-way specimen test (starting candidates: Fraunces + Instrument Sans; a confident grotesque + humanist body; a high-contrast serif + neutral sans). Type is the hero.
- **Layout:** asymmetric, left-aligned, generous whitespace, hairline rules; cards only where an object is a card; two radii only.
- **Imagery:** real photography of Indian students and professionals; if unavailable, clearly marked slots (never AI faces).
- **Voice:** plain, specific, active, no hype.

## 6. Page specs (summary)
- **Home:** header → editorial hero with real facts line → Learn · Develop · Create story → programs index → who it is for → how learning works (and Practical Lab teaser) → FAQ → latest guides → closing CTA with ribbon → footer.
- **Program pages (six):** facts list → answer-first definition → who it is for → year-by-year curriculum → tools → projects → roles it prepares for (only if documented) → assessment/certification (only as documented) → FAQ → related programs → sticky mobile CTA. No prices.
- **Audience pages:** each answers one real question for that audience; parents page explains privacy and consent in plain language; schools page leans on the teacher-ready curriculum if the document supports it.
- **Admissions, About, Contact, Apply, Resources, legal pages:** as in BUILD_PROMPT 3.4.
Content rule: every fact comes from the owner's documents or is marked `{{CONFIRM}}`.

## 7. Motion and 3D
- **Signature:** one SVG line in the brand gradient, drawn on scroll, passing through the Learn, Develop and Create anchors and ending at the closing CTA. Simplified on mobile. Fully visible without motion.
- **Details:** one-time headline line reveal in the hero; section pin for the three chapters on desktop only; CSS-only row hover; magnetic hover on the two main buttons; clip-path image reveal on the hero image.
- **3D:** a single glossy twisting ribbon (blue to green) behind the closing CTA. Lazy-loaded, paused off-screen, pixel ratio capped, disposed on teardown; static WebP poster for reduced motion, data saver, low-end devices, or WebGL failure.
- **Not used:** particles, neural-network visuals, brain imagery, fade-up on every section, smooth-scroll hijacking beyond Lenis, a client-side router.

## 8. SEO, AEO and GEO
- **Technical:** static HTML, canonical URLs, sitemap, robots, security headers, fast fonts and images, no layout shift, INP discipline.
- **Structured data (JSON-LD):** Organization + EducationalOrganization (one `@id` graph), WebSite, Course + CourseInstance, EducationalOccupationalProgram, BreadcrumbList, BlogPosting, FAQPage, CollectionPage, ContactPage. Google withdrew Course Info rich results (June 2025) and FAQ rich results (7 May 2026), so this markup is for understanding and AI answers, not for rich-result snippets.
- **AEO/GEO content:** H2s phrased as questions; 40–60 word answer-first paragraphs; tables and definition lists; named authors and dates; sources cited; consistent entity name and `sameAs` profiles; internal links between programs, audience pages and posts.
- **AI crawler policy (owner decision):**
  - Search/answer bots (OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Claude-User): **allow** (recommended).
  - Training bots (GPTBot, ClaudeBot, Google-Extended): default **allow** to build brand presence in models; block them if the owner prefers not to contribute training data. Google-Extended only affects Gemini training use, not Google Search or AI Overviews.
  - Check Cloudflare's AI Crawl Control and Bot Fight settings after the DNS move so they match this policy.
- **llms.txt:** shipped from a build script. Google says it ignores it and a 2026 study found most files get no traffic, so effort stays minimal.
- **Keyword strategy:** 25 themes grouped by intent (informational, commercial, transactional, local/brand), each mapped to one URL. Full map in BUILD_PROMPT 5.4. Do not promise unconfirmed offers (demo classes, workshops, placements).
- **Indexing:** Domain property in GSC, Bing import, IndexNow on deploy, Cloudflare Crawler Hints.
- **Competitor notes:** BrightCHAMPS uses `/courses/<subject>-classes-for-kids` URLs, INR prices on cards and a founder trust block; Codingal's AI/ML page pairs a keyword H1 with definitional H2s, grade-banded courses and an FAQ. aikolearn.com could not be analysed (URL needs confirming). Learn from structure; do not copy wording or design.

## 9. Forms, data and DPDP
- **Flow:** step 1 asks who is filling in the form. Under-18 students are routed to a parent/guardian path that collects the parent's details; the child's data is minimal and optional.
- **Consent:** separate, unticked, itemised checkboxes: privacy notice and contact (required); parent/guardian consent (required on the parent path); updates (optional). Store ticks, IST timestamp, notice version.
- **Prohibited:** tracking, behavioural monitoring or targeted advertising directed at children; remarketing audiences; storing IP addresses or user agents.
- **Protection:** Turnstile, honeypot, rate limit, strict server validation, `RAW` Sheet writes with formula-injection neutralising, restricted Sheet sharing, secrets only in Cloudflare/GitHub.
- **Retention and rights:** `delete_by` column (default 12 months after last contact, owner to confirm); a named grievance contact; a documented process for access, correction and deletion requests.
- **Timeline:** the DPDP Rules were notified 13 November 2025; the substantive duties (notice, security, breach reporting, retention, verifiable parental consent) are reported to begin about 13 May 2027 (sources differ by a day). Build compliant now. **This is not legal advice; have a lawyer review the privacy notice and consent flow before launch.**

## 10. Analytics and measurement
GA4 via Partytown after consent (default denied), no ad features. Events: apply_start, apply_submit, talk_click, program_view, scroll_75, outbound_click, resource_read. GSC and Bing for search data. Weekly SEO review and monthly AI-citation check (see BUILD_PROMPT Phase 10).

## 11. Blog engine and calendar
Posts are MDX in a content collection. A post publishes when its `pubDate` arrives, because the daily rebuild includes only posts whose date has passed. Twelve weeks, two posts per week (24 posts), each mapped to one primary keyword and linked to two programs and one audience page. Calendar table is in BUILD_PROMPT 7.2. Claude drafts all posts (real author name and review by the owner or faculty), cites primary sources, and avoids guarantees about jobs, income or admissions. After week 12, plan the next batch from Search Console data.

## 12. Deploy, DNS and email
- Cloudflare Workers static assets; GitHub Actions deploy; custom domain on apex and `www` (301 to apex); SSL Full (strict); security headers; rate limiting on the API route.
- **DNS move (from Squarespace):** the screenshots show Squarespace A records for the apex, a `www` CNAME to `ext-sq.squarespace.com`, an HTTPS record and `_domainconnect`, plus the records that must survive: MX `@` priority 1 `smtp.google.com`, SPF TXT `v=spf1 include:_spf.google.com ~all`, and the DKIM TXT at `google._domainkey`. Copy the full DKIM value before moving. In Cloudflare keep MX/TXT as DNS-only, add a `_dmarc` TXT starting at `p=none`, do not add Squarespace's web records, and do not enable Cloudflare Email Routing. Change nameservers at Squarespace (disable DNSSEC first), wait for Active, attach the Worker custom domain, then test mail both ways and check SPF/DKIM/DMARC in Gmail "Show original".
- **Sending site email:** use one SPF record that merges Google and the email API provider; add the provider's DKIM records; never touch Google's.

## 13. QA and performance
Automated: Playwright (mobile, tablet, desktop; keyboard; reduced motion; no-JS), Lighthouse CI budgets, pa11y/axe, link check, schema validation, header checks, `npm audit`, secret scan. Manual: throttled Android, screen reader pass, visual pass at six widths, content QA for invented claims. Full list in BUILD_PROMPT Phase 9.

## 14. Phases, exit criteria and status
Effort: S = under a day of Claude sessions, M = 1–3 days, L = 3+ days (depends on owner reply speed and asset availability).
| Phase | Scope | Effort | Exit criteria | Status |
|---|---|---|---|---|
| 0 | Setup, CI, MCP, Claude config | S | check/build pass, CI green, MCP report | ✔ local (CI and MCP report pending repo) |
| 1 | Brand, fonts, components | M | contrast report, font choice with screenshots, styleguide reviewed | ◐ done except owner review: tokens, contrast report, font choice, traced logo set (provisional), icons, 15 components + `/dev/styleguide`; ApplyForm, PostCard, Picture deferred to Phases 6, 7, 3 |
| 2 | Content model, curriculum extraction | M | all collections valid; curriculum summary approved | ☐ |
| 3 | All pages, static | L | all routes render; Lighthouse ≥ 95 before motion | ☐ |
| 4 | Motion and 3D | M | signature line and ribbon work; budgets met with motion | ☐ |
| 5 | SEO, AEO, GEO | M | `/seo-check` clean; schema valid; files live | ☐ |
| 6 | Forms | M | end-to-end Sheet and email; consent stored; tests green | ☐ |
| 7 | Blog engine, 4 launch posts | M | template approved; scheduling proven | ☐ |
| 8 | Deploy and DNS | S–M | live on domain; email verified; staging noindex | ☐ |
| 9 | QA | M | all gates green; owner approves screenshots | ☐ |
| 10 | Launch and measurement | S | GSC, Bing, GA4 live; weekly routine set | ☐ |

## 15. Owner checklist (things only you can do)
Menu names may change slightly; ask Claude if a screen looks different.
1. **GitHub:** create a private repository named `neuronetwrks`. Upload the six .docx files and the logo files into `docs/source/` (Claude can do this once the repo exists and is connected).
2. **Claude Code on the web:** open claude.ai/code, connect GitHub, choose the repo, then paste the start prompt from the top of `BUILD_PROMPT.md`. Run `/model opusplan` first.
3. **Cloudflare:** create or sign in to an account; Add a site → `neuronetwrks.com` → Free plan. Do not change nameservers yet (Claude gives the exact moment in Phase 8).
4. **Cloudflare API token:** My Profile → API Tokens → Create Token → use the "Edit Cloudflare Workers" template → copy the token into the GitHub repo secret `CLOUDFLARE_API_TOKEN`; copy the Account ID into `CLOUDFLARE_ACCOUNT_ID` (Settings → Secrets and variables → Actions).
5. **Turnstile:** Cloudflare dashboard → Turnstile → Add site → hostname `neuronetwrks.com` → Managed. Put the site key in the repo variables and the secret key in Cloudflare secrets. For local testing use Cloudflare's published always-pass test keys (verify in the Turnstile docs).
6. **Google Sheets access:** console.cloud.google.com → new project → APIs & Services → enable Google Sheets API → IAM & Admin → Service Accounts → create → Keys → Add key → JSON. Share your Google Sheet with the service account's email as Editor. Store the JSON as the Cloudflare secret `GOOGLE_SERVICE_ACCOUNT_JSON` (never paste it into chat or the repo). Use a separate test Sheet until launch.
7. **Email API:** create a Resend (or similar) account, add `neuronetwrks.com`, and give Claude the DNS records to add to Cloudflare.
8. **GA4:** analytics.google.com → Admin → Create property → web data stream for neuronetwrks.com → send Claude the Measurement ID.
9. **Search Console and Bing:** add a Domain property in Search Console (copy the TXT record to Cloudflare DNS); in Bing Webmaster Tools choose Import from Google Search Console.
10. **Content and legal:** confirm official program names, admissions steps, contact details and grievance officer; supply photos and team details; get a lawyer to review the privacy notice and consent flow.
11. **Social profiles:** create or claim LinkedIn, YouTube, Instagram, X under "NeuroNetworks AI Ed" so schema `sameAs` is real.
12. **Decisions:** AI training-bot policy (allow or block), indexing go-live date, and whether to keep the foundation program's "Neuromind" name public.

## 16. Risks and mitigations
| Risk | Impact | Mitigation |
|---|---|---|
| Looks generic again | Rejected design | Anti-AI rules in CLAUDE.md; real photography; type specimen test; one signature motion; owner reviews screenshots at Phase 1 and 3 |
| No real photos or team data | Weak credibility | Marked placeholders, no AI faces, `{{CONFIRM}}` gate blocks launch |
| Email breaks during DNS move | Lost mail | Back up records first, copy full DKIM, test both directions, no Email Routing |
| Motion hurts Core Web Vitals | Lower rank and conversions | Budgets in CI, lazy 3D, reduced-motion and low-end fallbacks |
| Children's data compliance | Legal and reputational | Parent-first flow now, minimal data, lawyer review, deadline tracked |
| Invented claims | Trust and legal risk | No-invention rule, `{{CONFIRM}}` build gate |
| Claude Max limits reached mid-phase | Delays | Short phases, `/compact`, subagents for research, Haiku for repetitive content, avoid pasting large files |
| Version drift (Astro 7, Tailwind 4, GSAP) | Broken APIs | Verify with Context7 and `npm view` before coding |
| Sheet or secrets leak | Data breach | Secrets only in Cloudflare/GitHub, restricted Sheet sharing, secret scanning on |
| Competitors outrank on head terms | Slow traffic | Target long-tail and answer-first content first; build topical authority with 24 posts; earn links via schools and partnerships |

## 17. Launch checklist
- [ ] All pages final copy; no `{{CONFIRM` in `dist/`
- [ ] Lighthouse ≥ 95 on mobile for every route; CWV budgets met on throttled Android
- [ ] pa11y/axe clean; keyboard and screen-reader pass
- [ ] JSON-LD validates; canonical, titles, descriptions unique
- [ ] robots, sitemap, llms.txt, RSS live; production not noindex
- [ ] Form test from phone to the real Sheet; confirmation and notification emails arrive
- [ ] Privacy notice and consent flow lawyer-reviewed
- [ ] DNS moved; email in and out verified; SPF/DKIM/DMARC pass
- [ ] `www` to apex redirect; HTTPS everywhere; headers verified
- [ ] GSC Domain property verified, sitemap submitted; Bing imported; GA4 events firing after consent
- [ ] 4 launch posts live, 20 scheduled; social profiles linked
- [ ] Owner has approved screenshots and the go-live date

## 18. Open items
- aikolearn.com: confirm the URL (could not be analysed).
- Latest Astro patch (reported 7.3.8 by a third-party tracker), the Cloudflare adapter version and several repo star counts are unverified; Claude verifies before coding.
- DPDP start date differs by a day between sources (13 or 14 May 2027); lawyer to confirm.
- Claude Code's default model on Max is reported inconsistently; check `/model`.
- Official public names of the six programs and whether "Neuromind" is a public brand.
- Real assets: vector logo, photography, team, outcomes, admissions process, contact details.

## 19. Verified versions (Phase 0, 13 Oct 2026)
Node 24.20.0 · npm 11.19.0 · astro 7.3.8 · @astrojs/cloudflare 14.3.4 · @astrojs/mdx 8.0.3 · @astrojs/sitemap 3.7.4 · tailwindcss and @tailwindcss/vite 4.3.3 · gsap 3.15.0 · lenis 1.3.26 · three 0.186.1 · astro-seo 1.2.0 · astro-og-canvas 0.13.2 · @astrojs/partytown 2.1.8. Build output goes to `dist/client` with this adapter.

## 20. Phase 1 record

**Font pairing (chosen): Bricolage Grotesque (display) + IBM Plex Sans (body).** Specimen screenshots: `docs/design/phase1/type-desktop.png` and `type-mobile.png`. All three candidates rendered "·", "₹", curly quotes and en-dashes. B won because it is a sans like the logo wordmark, matches the owner's mockups in `docs/design/`, holds up at 8 rem display size with tight tracking, and avoids the Fraunces look that is now common on template sites. Rejected: A (Fraunces + Instrument Sans), C (Newsreader + Source Sans 3). The `/dev/type` page and unused font packages were removed.

**Contrast:** `node scripts/contrast.mjs` writes `docs/contrast-report.md`; every text pair passes AA. `--green-700` was darkened to `#2b7f0a` (5.07:1 on white). Brand green on white is 2.6:1, so it is decorative only.

**Logo:** traced from the JPG with `scripts/vectorize-logo.py` into `src/assets/brand/` (full, mark, ink mark, wordmark) plus favicon, 32 px, apple-touch 180, icon-192 and icon-512 in `public/`. Provisional until a vector original arrives (open question 1). `favicon.svg` is about 37 KB and should be simplified once the vector original exists.

**Components:** Header, Footer, Logo, Button, Section, Eyebrow, AnswerBlock, FactList, ProgramRow, AudienceLink, CurriculumYear, FAQ (with FAQPage JSON-LD), Breadcrumbs (with BreadcrumbList), JsonLd, ConsentBox, PathAnchor. Screenshots: `docs/design/phase1/styleguide-*.png`. `/dev/styleguide` is temporary; delete before launch.

**Known exceptions to "no raw hex outside global.css":** `<meta name="theme-color">` in `Base.astro` and the logo SVG artwork.
