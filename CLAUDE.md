# CLAUDE.md: NeuroNetworks AI Ed website (neuronetwrks.com)

Read this file at the start of every session. Rules here beat your defaults. If a rule blocks the task, say so and ask; do not silently work around it.

## What this project is

Marketing website for **NeuroNetworks AI Ed**, an Indian AI education brand (tagline: **Learn · Develop · Create**, never reworded). Goal: enquiries and applications, investor impression, brand awareness, and top organic/AI-search visibility. Pre-launch. India first. English only (`lang="en-IN"`).
The site only collects enquiries (Google Sheet + email). No login, no payments, no chatbot, **no prices anywhere**. The Neuromind Practical Lab IDE is a separate product: link or teaser only.
The owner is not a developer. Explain decisions in plain language, keep changes small, and never ask the owner to edit code.

## Stack (verify versions with `npm view <pkg> version` and Context7 before installing)

Astro 7 (static output) · Tailwind CSS v4 (`@tailwindcss/vite`, tokens in `@theme`) · MDX · TypeScript strict · GSAP (+ ScrollTrigger, SplitText) · Lenis · Three.js (one lazy island only) · `@astrojs/cloudflare` adapter used only for `src/pages/api/*` · Cloudflare Workers static assets · GitHub Actions for CI and deploy.

## Commands

- `npm run dev` start dev server
- `npm run check` = `astro check && tsc --noEmit`
- `npm run lint` = ESLint + Prettier check
- `npm run build` production build to `dist/`
- `npm run preview` serve the build
- `npm run test:e2e` Playwright flows (mobile + desktop)
- `npm run audit` Lighthouse CI + pa11y-ci + link check
- Deploy happens from GitHub Actions on merge to `main`. Do not run `wrangler deploy` yourself unless the owner asks.

## Folder map

- `docs/source/` owner-supplied originals (six curriculum .docx, logo). Read-only. Never edit.
- `docs/open-questions.md` every fact you could not confirm goes here, not into the site.
- `docs/launch-checklist.md` pending launch items and owner steps (GA4 ID, Search Console, Bing, Business Profile, placeholders). When the owner asks what is pending, answer from it and keep it updated.
- `src/content/{programs,posts,faqs,audiences}/` content collections (Zod schemas in `src/content.config.ts`).
- `src/components/` UI; `src/layouts/Base.astro` is the only layout that renders `<html>`.
- `src/lib/` `schema.ts` (JSON-LD builders), `seo.ts`, `sheets.ts`, `turnstile.ts`.
- `src/scripts/motion/` all GSAP/Lenis/WebGL code. Nothing else may import `gsap` or `three`.
- `src/styles/global.css` design tokens. No raw hex colours anywhere else.
- `src/pages/api/enquiry.ts` the only server route (`export const prerender = false`).

## Hard rules

1. **Static by default.** Every page is prerendered. Only `/api/*` may run on demand.
2. **No invented facts.** No made-up stats, testimonials, faculty, ratings, partner logos, outcomes, fees, or accreditation. Use text from `docs/source/` or write `{{CONFIRM: ...}}` and log it in `docs/open-questions.md`. A build step fails if `{{CONFIRM` appears in `dist/`.
3. **No prices.** CTAs are "Apply" and "Talk to us" only.
4. **Images** only through `astro:assets` (`<Image>`/`<Picture>`), always with `width`, `height`, meaningful `alt`. The LCP image uses `loading="eager"` and `fetchpriority="high"`. Never use AI-generated faces or stock "glowing brain / robot hand" art.
5. **JS budget.** Home page ≤ 100 KB JS (gzip) before interaction. Decorative islands use `client:visible` or `client:idle`, never `client:load`. WebGL loads by dynamic `import()` after intersection, with a static poster fallback for reduced motion, `saveData`, ≤4 cores, or ≤4 GB memory.
6. **LCP element is real HTML text or an optimised image.** Never a canvas, never hidden by an animation waiting to start.
7. **Motion must respect `prefers-reduced-motion`** (use `gsap.matchMedia`). Content is fully readable and visible with JS disabled.
8. **One `<h1>` per page.** Heading levels never skip. Semantic landmarks. WCAG 2.2 AA, visible focus states, 44 px touch targets.
9. **Every page** has unique `<title>` (≤ 60 chars), meta description (≤ 155), canonical, OG/Twitter tags, `BreadcrumbList`, and the JSON-LD for its type (see `src/lib/schema.ts`). Run `/seo-check` before finishing a page.
10. **Forms** follow the DPDP rules in `docs/PLAN.md` section 9: parent-first flow for under-18s, unticked consent boxes, versioned notice, Turnstile, honeypot, rate limit. Sheet writes use `valueInputOption=RAW` and neutralise cells starting with `= + - @`.
11. **Secrets** live in Cloudflare/GitHub secrets and `.dev.vars` (git-ignored). Never print, commit, or log a secret. Never put an email or phone number in the repo that the owner has not approved.
12. **No third-party scripts** except GA4 (after consent, via Partytown) and Cloudflare Turnstile. No chat widgets, no ad pixels, no remarketing, no tracking aimed at under-18s.
13. **Do not add dependencies** casually. Justify each in the PR description with its size cost.

## Design rules (editorial, premium, bright)

- Colours: brand blue `#006DEE` and brand green `#49B716` plus derived tints from `global.css`. Blue leads; green is rare (≤ 10% of coloured surface). `#49B716` fails contrast as text on white; use the darker `--green-700` for text and ink text on green fills. Compute contrast; do not guess.
- Neutrals are tinted toward blue (`--ink #0B1B33`, `--bg #FFFFFF`, `--bg-soft #F6F9FD`). No cream backgrounds. No pure grey.
- Type: self-hosted variable fonts (no Google Fonts request at runtime). Pairing is locked after the specimen test in Phase 1. Type is the main design element.
- **Signature motion** = one scroll-drawn line (blue → green) that links Learn, Develop, Create down the home page. Everything else is quiet. One WebGL object maximum (closing CTA), and it is **not a brain, network, or particle field**.
- **Banned (reads as AI-made):** purple/blue gradients; gradient text on more than one heading; Inter, Space Grotesk, Poppins as primary faces; identical rounded-card grids with the same soft shadow; glassmorphism blobs; particle or neural-network backgrounds; brain imagery; emoji as icons; "01 / 02 / 03" numbering unless the content is truly a sequence; tracked all-caps eyebrow above every heading; everything centred; fade-and-slide-up on every section; hype copy ("unlock your potential", "revolutionise", "cutting-edge", "seamless", "journey"); fake logo walls or testimonials.
- Copy voice: plain, specific, active, sentence case, written for a parent and a student at the same table. Use real numbers from the curriculum documents.
- Navigation transitions use native CSS `@view-transition { navigation: auto; }`, not `<ClientRouter />`, unless the owner approves.

## SEO / AEO / GEO rules

- Under each H2, first sentence answers the heading directly in 40–60 words (answer-first). Use definition lists and tables for facts.
- FAQ blocks are visible on the page and marked up with `FAQPage` (helps AI answers; Google no longer shows FAQ rich results).
- Entity consistency: "NeuroNetworks AI Ed" everywhere; `alternateName` includes "NeuroNetworks", "Neuronetworks", "neuronetwrks".
- Allow AI search bots in `robots.txt`; training-bot policy is the owner's decision (see `docs/PLAN.md` section 8). `llms.txt` is generated at build; treat it as optional.
- Blog posts: real named author, date, `dateModified`, TL;DR, sources, FAQ, internal links to at least 2 program pages. Future `pubDate` posts are excluded from the build until their date (daily rebuild publishes them).

## Workflow

1. **Plan mode first** for every phase in `docs/BUILD_PROMPT.md`. Use `/model opusplan`.
2. Build one section/page at a time. Commit small, conventional messages. Work on a branch; open a PR; CI must be green.
3. After each page: run `npm run check`, take mobile (390×844) and desktop (1440×900) screenshots with Playwright MCP, run Lighthouse via Chrome DevTools MCP, and fix before moving on.
4. Use **Context7** for current Astro, GSAP, Tailwind v4, Lenis, Three.js docs. Do not rely on memory for APIs.
5. Never claim something works unless you ran it. Report what you ran and what you could not run.
6. Use subagents for independent research or audits to protect main context. `/compact` between phases; `/clear` when switching topics.
7. Update `docs/PLAN.md` status table at the end of each phase.

## Definition of done (every page)

Type-checks · builds · Lighthouse ≥ 95 (Perf, A11y, Best Practices, SEO) on mobile profile · LCP ≤ 1.8 s, INP ≤ 150 ms, CLS ≤ 0.05 on throttled mid-range Android · pa11y clean · JSON-LD validates · works with JS disabled · reduced-motion tested · no `{{CONFIRM` left · screenshots reviewed.
