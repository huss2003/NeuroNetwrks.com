# MASTER BUILD PROMPT: neuronetwrks.com (NeuroNetworks AI Ed)

How to use this file: put it in the repo at `docs/BUILD_PROMPT.md` next to `CLAUDE.md`. Start Claude Code, run `/model opusplan`, then paste:

> Read CLAUDE.md and docs/BUILD_PROMPT.md fully. Then start **Phase 0**. Use plan mode, show me the plan, and wait for my approval before writing code. After each phase, stop, summarise in 5 lines, and wait for me to say "next phase".

Each phase below is self-contained. Do not skip ahead. Do not merge phases.

---

## 0. Role and mission

You are a senior design engineer and technical SEO lead at a boutique studio known for hand-crafted, editorial websites that never look templated or AI-made. You are building the public website for **NeuroNetworks AI Ed**, an Indian AI education company.

**Mission:** a premium, bright, Apple-grade-but-editorial marketing site that (1) converts parents, students, professionals and schools into enquiries and applications, (2) impresses investors on first load, and (3) ranks and gets cited for AI, course and learning searches in India across Google, Bing, ChatGPT, Perplexity, Gemini and Claude.

**The owner is not technical.** Explain in plain language. Never ask the owner to write code. When you need something only the owner can provide, list it clearly (see section 2) and keep going with clearly marked placeholders.

**Success criteria (all measurable):**
- Lighthouse mobile ≥ 95 in Performance, Accessibility, Best Practices, SEO on every page.
- LCP ≤ 1.8 s, INP ≤ 150 ms, CLS ≤ 0.05 on throttled mid-range Android over 4G (Google's thresholds are LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; ours are stricter on purpose).
- Home page JavaScript ≤ 100 KB gzip before interaction; total page weight ≤ 1 MB excluding the lazy WebGL chunk.
- WCAG 2.2 AA. Works with JavaScript disabled (content visible, forms degrade to a clear message).
- Valid JSON-LD on every page. Sitemap, robots, llms.txt, RSS all live.
- Zero invented facts on the site.

---

## 1. Fixed facts (do not change; do not ask again)

| Item | Value |
|---|---|
| Brand | NeuroNetworks AI Ed (alternate spellings in schema: "NeuroNetworks", "Neuronetworks AI Ed", "neuronetwrks") |
| Tagline | **Learn · Develop · Create** (exact characters, middle dots, never reworded) |
| Domain | `https://neuronetwrks.com` (note the spelling: "neuronetwrks", no "o" after "netw") |
| Language / market | English only, India only, `<html lang="en-IN">`, no hreflang needed (single locale) |
| Brand colours | Blue `#006DEE`, Green `#49B716` (sampled from the logo) |
| Goals | Enquiries/applications, investor impression, brand awareness, lead capture |
| Audiences | School students, college students, working professionals, parents, schools/institutions |
| CTAs | "Apply" (primary) and "Talk to us" (secondary). **No prices anywhere.** |
| Site type | Marketing front end only. No login, payments, or chatbot. Neuromind Practical Lab IDE is a separate product: link/teaser only |
| Form destination | Google Sheet ID `1S0jhByc2AuBwy9iRt0ZJjHmXWJ3lCzM6UREL-xtiPdQ` plus email notification |
| Hosting | Cloudflare (Workers static assets). DNS is currently at Squarespace with Google Workspace email, which must keep working |
| Programs | Six: one 1-year AI foundation (104 hours) and five 3-year specialisations (624 hours each): AI & ML Engineering, Software Development, Product & UX AI Design, Data Science & AI, Cybersecurity |
| Competitors to learn from (not copy) | brightchamps.com/en-in, codingal.com/courses/ai-and-machine-learning, aikolearn.com (URL unverified; ask the owner) |
| Visual rejection list | The owner rejected three earlier previews as "generic / AI-made" and as a "3D brain / particles cliché". **Do not use a brain, neural network, or particle field anywhere** |

---

## 2. Inputs only the owner can supply (ask once, at the start of Phase 0, then continue with placeholders)

Create `docs/open-questions.md` and keep it current. For every unknown, put `{{CONFIRM: <what is needed>}}` in content and log it there. The build must fail if `{{CONFIRM` is in `dist/`.

1. **Vector logo** (SVG/AI/PDF). Only a PNG exists. If no vector arrives, vectorise the PNG yourself (potrace or Illustrator-style trace) into `src/assets/logo.svg`, and flag it as provisional.
2. **Six curriculum documents** in `docs/source/`: foundation (104 hrs), plus AI/ML, Software Development, Product & UX AI Design, Data Science & AI, Cybersecurity (624 hrs each). Read them in full. They are the source of truth for program pages. Confirm the **official public names** of each program (the foundation file is titled "Neuromind 1-Year AI Curriculum ... Teacher Ready, Certification Aligned"; confirm whether "Neuromind" is a public product name and which certification it aligns to).
3. **Real photography**: Indian students (ages roughly 12–22), working professionals, mentors, classrooms, hands-on lab sessions. If none exists yet, build with typographic and illustrated layouts and clearly marked image slots. **Never use AI-generated faces or generic stock art.**
4. **Team and faculty** names, photos, credentials (or leave the section out).
5. **Contact details**: email, phone (optional), postal address, grievance officer name/email (needed for the DPDP notice), social profile URLs.
6. **Admissions process** steps, eligibility, intake dates, batch sizes, certification details, outcomes. Do not invent any. Use placeholders.
7. **Accounts and access** (the owner does these; give them exact click-paths in `docs/PLAN.md` section 15): GitHub repo, Cloudflare account and API token, Cloudflare Turnstile site, Google Cloud service account with Sheets API enabled and the Sheet shared with its email, GA4 property, Google Search Console, Bing Webmaster Tools, Resend (or other email API) account.

---

## 3. Phase map

| Phase | Name | Output |
|---|---|---|
| 0 | Setup and tooling | Repo, Astro 7 skeleton, CI, MCP, Claude config |
| 1 | Brand and design system | Tokens, fonts, logo, components, style guide page |
| 2 | Content model | Collections, schemas, curriculum extracted from the .docx files |
| 3 | Pages | All routes built in static HTML with real copy |
| 4 | Motion and 3D | Signature scroll path, reveals, one WebGL ribbon, fallbacks |
| 5 | SEO, AEO, GEO | Head, schema, sitemap, robots, llms.txt, RSS, OG images |
| 6 | Forms | Apply and Talk-to-us, Turnstile, Worker route, Sheets, email, DPDP flow |
| 7 | Blog engine | Posts, calendar, scheduled publishing |
| 8 | Deploy and DNS | Cloudflare, domain, redirects, headers, email safe |
| 9 | QA and performance | Automated and manual test pass |
| 10 | Launch and measurement | GSC, GA4, Bing, IndexNow, weekly review |

---

## PHASE 0: Setup and tooling

**Goal:** a clean, verified, version-pinned skeleton with guardrails before any design work.

1. **Verify before installing.** Use Context7 and `npm view` to confirm current stable versions of: `astro`, `@astrojs/cloudflare`, `@astrojs/mdx`, `@astrojs/sitemap`, `tailwindcss`, `@tailwindcss/vite`, `gsap`, `lenis`, `three`, `astro-seo`, `astro-og-canvas`, `astro-icon`, `@astrojs/partytown`, `@fontsource-variable/*`. (Research in Oct 2026 reported Astro 7.0 shipped 22 June 2026 and 7.3.x is current; this came from a third-party tracker. Confirm.) Record exact versions in `docs/PLAN.md`.
2. **Create the project:**
   ```bash
   npm create astro@latest . -- --template minimal --typescript strict --install --git
   npx astro add mdx sitemap cloudflare tailwind   # tailwind: accept the Tailwind v4 Vite plugin setup
   ```
   If `astro add tailwind` installs the legacy `@astrojs/tailwind`, remove it and use `@tailwindcss/vite` in `astro.config.mjs` instead.
3. **`astro.config.mjs`** (verify each option against the current docs; keep it this simple):
   ```js
   import { defineConfig } from 'astro/config';
   import mdx from '@astrojs/mdx';
   import sitemap from '@astrojs/sitemap';
   import cloudflare from '@astrojs/cloudflare';
   import tailwindcss from '@tailwindcss/vite';

   export default defineConfig({
     site: 'https://neuronetwrks.com',
     output: 'static',            // every page prerendered
     adapter: cloudflare(),       // used only by src/pages/api/*
     trailingSlash: 'never',
     integrations: [mdx(), sitemap({ filter: (p) => !p.includes('/apply/thanks') })],
     vite: { plugins: [tailwindcss()] },
     prefetch: { defaultStrategy: 'viewport', prefetchAll: false },
     image: { layout: 'constrained' }, // confirm option name in current docs
   });
   ```
   Pick `trailingSlash` and `build.format` once and keep them consistent with Cloudflare's behaviour (test `/about` and `/about/` both resolve to one canonical URL with a 301).
4. **TypeScript strict**, ESLint (`eslint-plugin-astro`, `typescript-eslint`), Prettier (`prettier-plugin-astro`). Scripts: `dev`, `check`, `lint`, `build`, `preview`, `test:e2e`, `audit` (see `CLAUDE.md`).
5. **Claude config committed to the repo:**
   - `CLAUDE.md` (already provided).
   - `.claude/settings.json`: allow `npm run *`, `npx astro *`, `git *` (no force push); deny reading `.env*`, `.dev.vars`, `*.pem`. Add a `PostToolUse` hook running Prettier on edited files and a `Stop` hook running `npm run check`.
   - `.claude/commands/audit.md` (`/audit`: build, run Lighthouse CI + pa11y + link check, summarise failures), `.claude/commands/seo-check.md` (`/seo-check`: verify title/description/canonical/H1/schema on the current page), `.claude/commands/new-post.md` (`/new-post <topic>`: scaffold a post from the template).
   - `.claude/agents/seo-reviewer.md` (read-only subagent that audits a built page against the SEO rules) and `a11y-reviewer.md`.
   - `.mcp.json` (project scope) for: Context7, Playwright, Chrome DevTools, GitHub, Cloudflare docs (see `docs/TOOLS.md` for exact commands). Run `/mcp` and report which connected. Some stdio servers may not work in Claude Code on the web; report honestly and fall back to the Playwright and Lighthouse CLIs.
6. **Install skills/plugins** (see `docs/TOOLS.md`): `frontend-design` (official), `skill-creator`, `code-review`, `security-guidance`. Create two project skills with `skill-creator`: `neuronetworks-seo` (the per-page checklist and JSON-LD builders) and `neuronetworks-voice` (copy voice and banned phrases).
7. **CI** `.github/workflows/ci.yml` on every PR: `npm ci`, `npm run check`, `npm run lint`, `npm run build`, Playwright e2e, Lighthouse CI (`@lhci/cli`, budgets in `lighthouserc.json`), `pa11y-ci`, link check. Fail on regressions.
8. **Security baseline:** `.gitignore` includes `.dev.vars`, `.env*`, `dist`, `.wrangler`. Enable GitHub secret scanning and Dependabot.
9. **Staging safety:** until launch, every deployment except the production domain sends `X-Robots-Tag: noindex, nofollow` and `robots.txt` disallows all. Control with `PUBLIC_ENV=staging|production`.

**Exit criteria:** `npm run dev`, `check`, `build` pass on an empty home page; CI green; `/mcp` report written to `docs/PLAN.md`; open questions file exists.

---

## PHASE 1: Brand and design system

**Goal:** a distinctive, bright, editorial system that cannot be mistaken for a template.

### 1.1 Colour tokens (`src/styles/global.css`, Tailwind v4 `@theme`)
Derive, do not guess. Build tints/shades from the two brand colours in OKLCH, then check contrast with a script and record results in `docs/PLAN.md`.

```css
@theme {
  --color-blue-600: #006DEE;   /* brand blue, primary */
  --color-blue-700: #0A55C8;   /* hover / pressed (verify contrast) */
  --color-blue-50:  #EEF5FF;
  --color-green-600:#49B716;   /* brand green: fills, rules, marks; NOT text on white */
  --color-green-700:#2F8F0B;   /* green for text on white (verify >= 4.5:1) */
  --color-green-50: #F0FAE8;
  --color-ink:      #0B1B33;   /* blue-tinted near-black */
  --color-slate:    #4A5B75;   /* secondary text */
  --color-line:     #E3EAF4;
  --color-bg:       #FFFFFF;
  --color-bg-soft:  #F6F9FD;
}
```
Rules: blue leads; green is rare (≤ 10% of coloured surface); text on green fills is `--color-ink`; white text only on blue-600 or darker. No gradients except the signature path line and (optionally) the closing WebGL ribbon. No purple. No cream.

### 1.2 Typography (decide with evidence)
- Self-host variable fonts via `@fontsource-variable/*` (no runtime request to Google). Preload only the display and body WOFF2 actually used above the fold. Use `font-display: swap` with a metric-matched fallback (`size-adjust`, `ascent-override`) to avoid layout shift.
- **Do the specimen test:** build a temporary `/dev/type` page showing three pairings on real headlines and body copy, at mobile and desktop. Candidates: (A) Fraunces (display, optical-size axis, restrained weight) + Instrument Sans (body); (B) a confident grotesque display with a humanist body (try Bricolage Grotesque or Familjen Grotesk, but not Inter/Space Grotesk/Poppins); (C) a high-contrast serif such as Newsreader or Gloock with a neutral sans. Screenshot all three, pick one with reasons, record in `docs/PLAN.md`, **delete `/dev/type` before launch**. Check that the chosen font ships the Latin and punctuation glyphs including "·" and "₹".
- Scale: fluid `clamp()` scale, ratio about 1.25, display sizes up to about 7–9 rem on desktop, body 17–18 px, line length 60–68 characters, serif body gets slightly more line-height. Headings use `text-wrap: balance`, paragraphs `text-wrap: pretty`.
- **Type is the hero.** Treat headline typography as the main visual: tight tracking on display sizes, deliberate line breaks, optical alignment, real italics where the font has them. Do not accent one word in colour on every heading. At most one headline on the whole site may use the brand gradient.

### 1.3 Layout, spacing, shape
- 12-column grid, 1280 px max content, 16 px mobile gutters (24 px tablet, 32+ desktop). Spacing scale 4/8 px base. Section rhythm varies (do not repeat the same padding on every section).
- **Layouts are asymmetric and editorial**: left-aligned text, large offsets, overlapping image and type, occasional full-bleed band. Centre-align only short closing statements. Avoid the "equal rounded cards in a 3-column grid" look. Use cards only where an object is genuinely a card; elsewhere use rules, whitespace, and type.
- Radius: two values only (e.g., 6 px controls, 20 px media), not one radius everywhere. Shadows are rare, hard to notice, and tinted blue-ink.

### 1.4 Logo
Use the real logo. The mark has a green left and blue right half like a brain (that is fine in the **logo**, but the site must not repeat brain imagery elsewhere). Provide: horizontal lockup, mark-only, one-colour, favicon (`favicon.svg`, 32 px PNG, `apple-touch-icon` 180 px, `icon-192`, `icon-512`), safe-area and minimum-size rules. Wordmark can be set in live text only if it matches the logo's geometric sans; otherwise use the SVG.

### 1.5 Components (build as Astro components with props and slots; document on a temporary `/dev/styleguide`)
`Header` (sticky, transparent to white on scroll, mega-menu for "For students / parents / schools / professionals"), `Footer`, `Button` (primary blue, secondary outline, text link; magnetic hover only on the two main CTAs), `Link`, `Eyebrow` (rare), `Heading`, `AnswerBlock` (the 40–60 word answer-first paragraph), `FactList` (definition list: duration, hours, level, mode), `ProgramRow`, `AudienceLink`, `FAQ` (native `<details>`, with schema), `CurriculumYear`, `PostCard`, `Breadcrumbs`, `ApplyForm`, `ConsentBox`, `Seo` (head), `JsonLd`, `Picture`, `Section` (applies rhythm), `PathAnchor` (marks where the signature line passes).

**Exit criteria:** tokens in place and contrast report saved; font pairing chosen with screenshots; logo set exported; component styleguide reviewed on mobile and desktop screenshots; no hard-coded hex outside `global.css`.

---

## PHASE 2: Content model

**Goal:** all content typed, validated, and sourced from the owner's documents.

1. **Convert the six .docx files** to Markdown/JSON: `pandoc -f docx -t gfm --wrap=none --extract-media=docs/extracted/<name> docs/source/<file>.docx -o docs/extracted/<name>.md` (or `mammoth`). Read every file completely. Produce `docs/extracted/curriculum-summary.md`: for each program, official name, hours, years, structure per year/term, modules, tools, projects/capstone, assessments, certifications mentioned, prerequisites, intended learners. Mark anything missing as `{{CONFIRM}}`.
2. **Content collections** in `src/content.config.ts` using the `glob()` loader and Zod:
   ```ts
   import { defineCollection, z } from 'astro:content';
   import { glob } from 'astro/loaders';

   const programs = defineCollection({
     loader: glob({ pattern: '**/*.mdx', base: './src/content/programs' }),
     schema: z.object({
       name: z.string(),
       slug: z.string(),
       shortName: z.string(),
       level: z.enum(['foundation', 'specialisation']),
       durationYears: z.number(),
       totalHours: z.number(),
       summary: z.string().max(200),
       answer: z.string().min(150).max(420),     // answer-first paragraph for AEO
       audience: z.array(z.enum(['school','college','professional','parent','institution'])),
       years: z.array(z.object({ title: z.string(), hours: z.number().optional(), modules: z.array(z.string()) })),
       tools: z.array(z.string()).default([]),
       projects: z.array(z.string()).default([]),
       careerRoles: z.array(z.string()).default([]), // only if the curriculum doc states them
       faqs: z.array(z.object({ q: z.string(), a: z.string() })).min(4),
       related: z.array(z.string()).default([]),
       keywords: z.object({ primary: z.string(), secondary: z.array(z.string()) }),
       seo: z.object({ title: z.string().max(60), description: z.string().max(155) }),
     }),
   });

   const posts = defineCollection({
     loader: glob({ pattern: '**/*.mdx', base: './src/content/posts' }),
     schema: ({ image }) => z.object({
       title: z.string(), description: z.string().max(155),
       pubDate: z.coerce.date(), updatedDate: z.coerce.date().optional(),
       author: z.string(), category: z.enum(['guides','careers','schools','parents','professionals']),
       cover: image().optional(), coverAlt: z.string().optional(),
       tldr: z.string().max(320), primaryKeyword: z.string(),
       faqs: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
       related: z.array(z.string()).default([]),
       draft: z.boolean().default(false),
     }),
   });
   const faqs = defineCollection({ loader: glob({ pattern: '**/*.yaml', base: './src/content/faqs' }), schema: z.object({ q: z.string(), a: z.string(), group: z.string() }) });
   const audiences = defineCollection({ loader: glob({ pattern: '**/*.mdx', base: './src/content/audiences' }), schema: z.object({ name: z.string(), slug: z.string(), answer: z.string(), seo: z.object({ title: z.string().max(60), description: z.string().max(155) }), programs: z.array(z.string()) }) });
   export const collections = { programs, posts, faqs, audiences };
   ```
3. **Site data** `src/data/site.ts`: name, alternate names, URL, tagline, contact, social URLs, grievance contact, notice version (`2026-10-v1`), all with `{{CONFIRM}}` where unknown.
4. **Program MDX**: one file per program, content derived from the curriculum summary (not invented). Include real module lists, hours per year, tools, projects.
5. **Audience MDX** for students, parents, schools, professionals: each answers "Which program fits me?" and links to programs.
6. **FAQ YAML**: at least 8 global FAQs (admissions process, eligibility, learning mode, certification, data privacy for minors, who teaches, how to apply, how to talk to a counsellor). Mark unknown answers `{{CONFIRM}}`.

**Exit criteria:** `astro check` passes with all collections; curriculum summary reviewed; every program MDX has real data; unknowns are logged.

---

## PHASE 3: Pages (static HTML first, then motion)

Build every route with final copy, accessible markup, and zero animation. Animation arrives in Phase 4. All pages use `Base.astro`, `Seo`, `JsonLd`, `Breadcrumbs`.

### 3.1 Route inventory and SEO targets

| Route | Primary keyword | Title (≤60) | H1 | Schema |
|---|---|---|---|---|
| `/` | AI courses in India | AI Courses in India \| NeuroNetworks AI Ed | draft: "Learn AI. Develop real skills. Create what's next." | Organization+EducationalOrganization, WebSite, BreadcrumbList(n/a), FAQPage |
| `/programs` | AI programs for students and professionals | AI, Data Science & Cybersecurity Programs | "Six programs, one way of learning" | CollectionPage, ItemList, BreadcrumbList |
| `/programs/ai-foundation` | AI course for beginners | AI Foundation Course for Beginners (1 Year) | per program | Course+CourseInstance, FAQPage, BreadcrumbList |
| `/programs/ai-ml-engineering` | machine learning course online India | AI & Machine Learning Engineering Program | per program | Course, EducationalOccupationalProgram, FAQPage, BreadcrumbList |
| `/programs/software-development` | full stack developer course India | Software Development Program (Full-Stack) | per program | same |
| `/programs/product-ux-ai-design` | UX design course India | Product & UX Design with AI Program | per program | same |
| `/programs/data-science-ai` | data science course India | Data Science & AI Program in India | per program | same |
| `/programs/cybersecurity` | cybersecurity course India | Cybersecurity Program for Beginners | per program | same |
| `/for/students` | AI course for school students | AI Courses for School & College Students | "AI learning for students" | WebPage, FAQPage, BreadcrumbList |
| `/for/parents` | AI classes for kids India | AI Learning for Your Child: A Parent's Guide | "..." | same |
| `/for/schools` | AI curriculum for schools | AI Curriculum for Schools & Institutions | "..." | same |
| `/for/professionals` | AI course for working professionals | AI Courses for Working Professionals | "..." | same |
| `/about` | about NeuroNetworks AI Ed | About NeuroNetworks AI Ed | "..." | AboutPage, Organization |
| `/admissions` | how to apply AI course | Admissions: How to Apply | "..." | WebPage, FAQPage, HowTo only if steps are real |
| `/apply` | apply AI course India | Apply to NeuroNetworks AI Ed | "Apply" | WebPage |
| `/apply/thanks` | n/a | Thank you | "Thank you" | noindex |
| `/resources` | AI learning guides | AI Learning Guides & Resources | "Resources" | CollectionPage |
| `/resources/[slug]` | per post | per post | per post | BlogPosting, BreadcrumbList, FAQPage if FAQs |
| `/resources/category/[cat]` | category | per category | "..." | CollectionPage |
| `/contact` | contact | Talk to Us | "Talk to us" | ContactPage |
| `/privacy`, `/terms` | n/a | Privacy Notice, Terms | "..." | WebPage |
| `/404` | n/a | Page not found | "..." | noindex |

Also generate: `/sitemap-index.xml`, `/robots.txt`, `/llms.txt`, `/llms-full.txt`, `/rss.xml`, `/humans.txt` (optional).

### 3.2 Home page: section by section
Every section has exactly one job. Write real copy from the curriculum; mark gaps `{{CONFIRM}}`.
1. **Header**: logo left; links: Programs, For (students, parents, schools, professionals), About, Admissions, Resources, Contact; primary "Apply" button right. Skip link first in DOM.
2. **Hero** (the first screen is the brand). Big editorial H1 (type is the star), a one-sentence subhead containing "AI courses", "India", "students and professionals", two CTAs ("Apply", "Talk to us"), the tagline `Learn · Develop · Create` set as typographic detail, and a **fact line using only real numbers**: "6 programs · 104-hour foundation · 3-year specialisations of 624 hours". Image slot for real photography (art-direction notes below) overlapping the type. The signature line begins here.
3. **Learn · Develop · Create** (the story section). Three chapters mapped to the real structure of the programs (foundation, specialisation, capstone/projects). Each chapter: answer-first paragraph, 2–3 concrete facts from the curriculum, a link to the relevant program. The signature line passes through each chapter's anchor.
4. **Programs index**: editorial list (not a card grid): program name large, years and hours aligned right, one-line outcome, arrow. Hover reveals a short description.
5. **Who it is for**: four paths (students, parents, schools, professionals) as large text links to `/for/*`, each with one honest sentence.
6. **How learning works**: practical, project-based learning drawn from the documents; teaser for the Neuromind Practical Lab as "a separate product" with a link only if the owner confirms its public URL.
7. **FAQ**: 6–8 questions, visible, with `FAQPage` JSON-LD.
8. **From the resources**: latest three posts.
9. **Closing CTA**: statement + "Apply" + "Talk to us", with the single WebGL ribbon behind (Phase 4).
10. **Footer**: nav columns, legal links, contact, grievance contact, tagline, `© NeuroNetworks AI Ed`, social links (only real ones).

### 3.3 Program page template (all six)
1. Breadcrumbs. 2. H1 (official program name) + one-line promise. 3. `FactList`: duration, total hours, level, who it is for, mode/schedule (`{{CONFIRM}}` if unknown). 4. `AnswerBlock`: "What is the <program>?" 40–60 words. 5. Who it is for / prerequisites. 6. What you will learn: year-by-year (`CurriculumYear`) from the MDX. 7. Tools and technologies. 8. Projects and capstone. 9. Roles it prepares you for (only if the document states it; no salary claims). 10. How assessment/certification works (only as documented). 11. FAQ (4–8, program-specific). 12. Related programs. 13. Sticky mobile CTA bar ("Apply" / "Talk to us"). Include `Course` + `CourseInstance` (`courseMode`, `courseWorkload` as ISO-8601 duration where real) + `EducationalOccupationalProgram` (`timeToComplete`, `educationalCredentialAwarded` only if real). Omit `offers` (no pricing).

### 3.4 Other pages
- **Programs index**: comparison table (name, years, hours, best for) plus the editorial list.
- **For students / parents / schools / professionals**: each answers a different question ("Where do I start?", "Is it safe and worth it?", "How do we introduce AI in our school?", "How do I learn AI next to my job?"). The parents page covers data privacy and consent in plain language and links to the privacy notice. The schools page leans on the "teacher ready" nature of the foundation curriculum **if the document supports it**.
- **About**: mission, why NeuroNetworks, the team (real or omitted), approach, the Neuromind Lab mention.
- **Admissions**: the real process as steps (placeholders until confirmed), eligibility, timelines, FAQ, "Apply" and "Talk to us".
- **Apply** and **Contact**: forms (Phase 6).
- **Resources**: hub with category filters (links, not JS), featured post, latest posts, RSS link.
- **Legal**: privacy notice (DPDP-aligned, versioned), terms, cookie/analytics note. Mark as "draft for legal review".
- **404**: helpful links to programs and Apply.

### 3.5 Image art direction
Natural light, candid, Indian students and professionals actually working (laptops, whiteboards, pair programming, lab sessions), diverse in age and gender, real faces with consent, shallow depth of field, **no** stock handshakes, **no** floating holograms, **no** glowing brains/robots, **no** blue-tinted "AI look". Provide 16:10 hero crop, 4:5 portrait, 1:1 detail. All images AVIF/WebP via `astro:assets`, `sizes` set, explicit width/height. Until real photos exist, use clearly labelled neutral placeholder blocks, never AI faces.

### 3.6 Copy rules
Plain, specific, active, sentence case. Use real numbers. Short sentences. No hype words (see banned list in `CLAUDE.md`). No em-dash asides. No "not X but Y" device. No colon-reveal sentences. CTA labels state what happens ("Apply", "Talk to us", "Read the guide"). Errors say what went wrong and how to fix it.

**Exit criteria:** all routes render with real copy; no animation yet; Lighthouse ≥ 95 on every page before motion; screenshots of home, one program page, and apply at mobile and desktop reviewed.

---

## PHASE 4: Motion and 3D (restraint is the premium signal)

**Principle:** one signature moment, a few quiet details, one 3D object. Everything else is still. Motion explains or rewards; it never decorates. If a motion hurts INP, LCP, or readability, cut it.

### 4.1 Architecture
- All motion code in `src/scripts/motion/` and loaded by one small module from `Base.astro` (`<script>` bundled by Astro, deferred). Nothing else imports `gsap`, `lenis`, or `three`.
- `gsap.registerPlugin(ScrollTrigger, SplitText)` (all GSAP plugins are free since 3.13; verify current licence note).
- **Lenis + GSAP sync (exact pattern):**
  ```ts
  import Lenis from 'lenis';
  import gsap from 'gsap';
  import { ScrollTrigger } from 'gsap/ScrollTrigger';
  gsap.registerPlugin(ScrollTrigger);
  const lenis = new Lenis({ lerp: 0.1, smoothWheel: true });   // native scroll underneath
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add((t) => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
  ```
  Disable Lenis for `prefers-reduced-motion`, for `(pointer: coarse)` if it feels laggy in testing, and on pages with long forms.
- Use `gsap.matchMedia()` for every animation: separate branches for `(prefers-reduced-motion: no-preference)` and reduce; separate mobile/desktop timelines.
- Page transitions: native CSS `@view-transition { navigation: auto; }` with a short cross-fade and a shared logo element (`view-transition-name`). **Do not use `<ClientRouter />`** unless the owner approves; it forces re-initialising ScrollTrigger on `astro:page-load` and killing it on `astro:before-swap`.
- Content must be visible before JS runs. Add classes like `js-motion` to `<html>` via an inline snippet **only after** confirming motion will run, so the no-JS and reduced-motion states show the final layout.

### 4.2 Signature moment: the scroll-drawn line (`signature-path.ts`)
A single continuous line in the brand gradient (blue at the top to green at the bottom) that starts in the hero, passes down the left (desktop) gutter and through anchor points (`data-path-anchor` on each of Learn, Develop, Create and the programs index), and ends at the closing CTA. It draws as the user scrolls and leaves small solid nodes at each anchor. It is the only gradient on the site besides the optional ribbon.
Implementation:
1. Place one absolutely positioned `<svg>` (`pointer-events:none`, `aria-hidden="true"`) inside `<main>`, full height.
2. On load and on `ResizeObserver` (debounced), read each anchor's position, build a smooth path through the points with cubic Béziers (gentle S-curves, slight hand-drawn irregularity from seeded noise so it is not geometric).
3. `path.getTotalLength()` then set `stroke-dasharray`/`stroke-dashoffset`; animate `strokeDashoffset` with a `ScrollTrigger` (`scrub: 0.6`, `start: 'top 80%'`, `end: 'bottom 20%'` on `main`). `linearGradient` with `gradientUnits="userSpaceOnUse"` from the start y to the end y.
4. Node dots scale in (`scale 0 → 1`) when the line reaches their anchor (`onUpdate` progress check or one small ScrollTrigger per anchor).
5. Mobile: simplify to a straight vertical line in the left gutter with the same nodes (cheaper, no overlap with text).
6. Reduced motion or no JS: show the full line statically (or hide it); never leave it half-drawn.
7. Performance: one path, no filters, `will-change` only during animation, kill triggers when the page is hidden.

### 4.3 Supporting details (keep it small)
- **Headline reveal** (once, on load, hero only): `SplitText` by lines with `mask: 'lines'`, `yPercent: 100 → 0`, 0.9 s, `expo.out`, stagger 0.08. The H1 text exists in the HTML and is visible for LCP; the animation must not delay the paint (animate from `visibility` already visible, or run after first paint with `requestAnimationFrame`). Use `autoSplit: true` with `onSplit()` so lines re-split on resize.
- **Chapter transitions** in the Learn/Develop/Create section: on desktop, the section pins for a short distance; each chapter's text swaps with a clean mask reveal. Do not pin on mobile.
- **Programs list hover**: a rule draws under the row, the arrow shifts, the row text offsets 8 px. CSS only.
- **Magnetic CTA** on the two primary buttons only (desktop pointer: fine only). Max 8 px pull.
- **Image reveal**: hero image uses a clip-path reveal on load (CSS, once). Other images do not animate.
- **No** fade-up on every section. Where something enters, use position-based reveals that clarify structure (a line extending, a number counting once from real values), at most once per page.

### 4.4 The one 3D object: closing CTA ribbon (`cta-ribbon.ts`)
Not a brain, not a network, not particles. A single glossy ribbon (a twisting open loop that echoes the logo's two halves) with a vertex-colour gradient blue → green, soft studio lighting, slow rotation tied to scroll progress, tiny pointer parallax.
- Build with `three` (import only what you use; tree-shake) in a separate chunk loaded by `import()` when the CTA section is within one viewport of entering. Cap pixel ratio at 1.5, pause the render loop when offscreen (`IntersectionObserver`), dispose geometry/materials on teardown.
- Geometry: `TubeGeometry` along a parametric curve (e.g., a stretched trefoil) with a flattened cross-section via vertex scaling to read as a ribbon. Material: `MeshPhysicalMaterial` (clearcoat) or a baked matcap for lower cost. Lights: one hemisphere + one directional.
- **Fallback**: if `prefers-reduced-motion`, `navigator.connection.saveData`, `hardwareConcurrency <= 4`, `deviceMemory <= 4`, WebGL unavailable, or the chunk fails, show a pre-rendered WebP poster of the same ribbon (render it once headlessly with the same scene and commit the image). The page must look finished with the poster alone.
- Budget: the 3D chunk may exceed the home JS budget because it is lazy and below the fold, but record its size and keep it under 200 KB gzip. Verify it does not move LCP, INP, or CLS.
- Optional second 3D touch: CSS 3D tilt (`perspective`, `rotateX/Y` ≤ 4°) on the program rows' image thumbnails on hover. No JS needed beyond pointer variables.

### 4.5 Motion QA
Test with: reduced-motion on, JS disabled, 4× CPU throttle, Slow 4G, and a real mid-range Android if available. Record INP in Chrome DevTools MCP. Remove any effect that causes a long task above 50 ms.

**Exit criteria:** signature line works at 390 px and 1440 px and on resize; 3D loads lazily with working poster fallback; CWV budgets met with motion on; screen-recorded or screenshot-sequenced review sent to the owner.

---

## PHASE 5: SEO, AEO, GEO

### 5.1 Head and metadata (`Seo.astro`)
Per page: `<title>` (≤ 60), meta description (≤ 155), canonical (absolute, no trailing slash), `robots` (index, follow; `noindex` for thanks/404/staging), Open Graph (`og:title`, `og:description`, `og:type`, `og:url`, `og:image` 1200×630, `og:locale=en_IN`, `og:site_name`), Twitter card `summary_large_image`, theme-color, manifest, favicon set, `rel="alternate" type="application/rss+xml"`. Use `astro-seo` or a hand-written component.
**OG images:** generate at build per page with `astro-og-canvas` (or `satori` + `@resvg/resvg-js` for full design control): brand type, logo, page title. Self-hosted fonts only.

### 5.2 JSON-LD (`src/lib/schema.ts`)
Create typed builders and one `@id` graph so entities connect. Use `schema-dts` types. Reuse stable IDs: `https://neuronetwrks.com/#organization`, `#website`.
```ts
export const organization = () => ({
  '@type': ['Organization', 'EducationalOrganization'],
  '@id': 'https://neuronetwrks.com/#organization',
  name: 'NeuroNetworks AI Ed',
  alternateName: ['NeuroNetworks', 'Neuronetworks AI Ed', 'neuronetwrks'],
  url: 'https://neuronetwrks.com',
  logo: 'https://neuronetwrks.com/logo.png',
  slogan: 'Learn · Develop · Create',
  areaServed: { '@type': 'Country', name: 'India' },
  sameAs: [/* real profile URLs only */],
  contactPoint: [{ '@type': 'ContactPoint', contactType: 'admissions', email: '{{CONFIRM}}', availableLanguage: 'en' }],
});
```
Builders: `website()`, `course(program)` (with `provider` = organization `@id`, `hasCourseInstance` with `courseMode` and `courseWorkload`), `occupationalProgram(program)`, `breadcrumbs(items)`, `faqPage(items)` (only for FAQs visible on the page), `blogPosting(post)` (`author` as a `Person`, `datePublished`, `dateModified`, `image`, `mainEntityOfPage`), `collectionPage()`, `contactPage()`. Output via `<script type="application/ld+json">` using `JSON.stringify`. Validate with the Rich Results Test and validator.schema.org; **expect** Google to show no Course or FAQ rich results (both were withdrawn: Course Info June 2025, FAQ 7 May 2026). The markup is kept for machine understanding and AI answers.

### 5.3 Crawling and indexing files
- **`robots.txt`** generated by `src/pages/robots.txt.ts`, environment aware. Production:
  ```
  User-agent: *
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

  # Training crawlers: the owner decides (default below allows, to maximise brand presence in AI models)
  User-agent: GPTBot
  Allow: /
  User-agent: ClaudeBot
  Allow: /
  User-agent: Google-Extended
  Allow: /

  Sitemap: https://neuronetwrks.com/sitemap-index.xml
  ```
  Staging: `User-agent: *` / `Disallow: /`. Also check Cloudflare dashboard "AI Crawl Control" and bot-fight settings so they do not override this file after the DNS move.
- **Sitemap**: `@astrojs/sitemap` with `lastmod` from content dates, excluding noindex pages. Submit in GSC and Bing.
- **`llms.txt` and `llms-full.txt`**: generated from collections (site summary, program list with one-line descriptions and URLs, key pages, contact). Cheap to ship; low expected impact (Google says it ignores llms.txt; a large 2026 study found almost no traffic from it). Do not spend more time on it than a build script.
- **RSS** `/rss.xml` for posts.
- **IndexNow**: on production deploy, POST changed URLs to `https://api.indexnow.org/indexnow` with a key file at `/<key>.txt`. (Bing and Yandex only; Google does not use it.)
- **Redirects** (`public/_redirects` or Workers assets config; verify support): `www` → apex 301; trailing slash normalisation; any old URLs.

### 5.4 On-page SEO and AEO/GEO content rules
- One H1 containing the primary keyword naturally. H2s phrased as the questions people ask ("What is the AI Foundation course?", "Who is it for?", "How long does it take?").
- **Answer-first:** the first sentence under each H2 answers it directly in 40–60 words, then elaborates. Use tables for comparisons and definition lists for facts. These formats are what answer engines extract.
- **E-E-A-T:** named authors with short bios (real), dates, `Last updated`, sources cited with links, an About page with real people, contact details, and a clear privacy notice.
- **Entity clarity:** the same brand name, description, logo, and `sameAs` links everywhere. Create or claim the LinkedIn, YouTube, Instagram, X profiles and link them. Consider a Google Business Profile only if there is a physical centre.
- **Internal linking:** every program links to its audience pages, related programs, and relevant posts; every post links to at least two programs; breadcrumbs everywhere; footer links to all programs.
- **Keyword map** (assign each theme to exactly one URL to avoid cannibalisation):
  - Informational/AEO → blog posts: "what is AI for kids/school students", "how to learn AI from scratch", "machine learning vs AI vs data science", "AI career after 12th", "is coding necessary for AI / Python for AI", "prompt engineering for students", "generative AI explained for teens", "data science roadmap India".
  - Commercial → program and audience pages: "best AI course online India", "AI course for beginners", "machine learning course online India", "data science course India", "cybersecurity course India / ethical hacking for beginners", "full stack developer course India", "UX design course India", "AI certification India", "generative AI course India", "AI classes for kids India", "AI course for working professionals", "AI curriculum for schools".
  - Transactional → `/apply`, `/contact`, `/admissions`: "enrol AI course online India", "free demo/trial class" (only if offered), "AI workshop for schools" (only if offered).
  - Brand → home/about: "NeuroNetworks AI Ed", "neuronetwrks", "neuronetworks".
  Do not promise services that are not confirmed (demo classes, workshops, placements, fees).
- **Competitor patterns to match or beat:** BrightCHAMPS uses `/courses/<subject>-classes-for-kids` URLs and INR prices on cards; Codingal's AI/ML page pairs a keyword H1, definitional H2s ("What is AI for kids?"), grade-banded courses and an FAQ. Beat them with clearer answer-first content, honest specifics from the curriculum, and faster pages. Do not copy their wording.
- **Local/India signals:** `en-IN`, INR formatting, Indian examples and context, `areaServed: India`, city/state fields in the form, no hreflang until a second locale exists.

### 5.5 Technical SEO and performance
Preload the two critical fonts; inline critical CSS (Astro does this when small); `fetchpriority="high"` on the LCP image only; lazy-load everything below the fold; no layout shift (reserve space for images, embeds, the signature SVG); `<link rel="preconnect">` only for hosts actually used (Turnstile on the form pages only). Security headers via `public/_headers` (verify Workers assets support): `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` (deny camera/mic/geolocation), `Content-Security-Policy` (self + Turnstile + GA4 hosts, nonce/hash for inline JSON-LD), cache headers (`immutable` for hashed assets).

**Exit criteria:** every page passes `/seo-check`; Rich Results Test shows valid structured data; robots, sitemap, llms.txt, RSS resolve; OG images render; Lighthouse SEO 100.

---

## PHASE 6: Forms (Apply and Talk to us)

### 6.1 Flow and fields (DPDP-aware; not legal advice, owner to get legal review)
Under India's DPDP framework anyone under 18 is a child; verifiable parental consent is required before processing a child's data, and tracking or targeted advertising directed at children is prohibited. The substantive duties are reported to start about **13 May 2027** (sources differ by a day). Build the compliant flow now.

**Step 1:** "Who is filling this in?" radio: *Student under 18*, *Student 18 or over*, *Parent/guardian of a student*, *Working professional*, *School or institution*.
- If *Student under 18*: show a message "Please ask a parent or guardian to complete this form" and switch to the parent/guardian path (collect the **parent's** contact details only; the child's first name and age band are optional).
- **Fields (Apply):** role, full name, email, mobile (Indian format, with country code), city, state, program(s) of interest (checkboxes from the collection), student age band (Under 13 / 13–17 / 18–24 / 25+), parent/guardian name (if applicable), preferred contact time, message (optional, max 500 chars).
- **Talk to us:** role, name, email, mobile, topic (admissions / schools / partnerships / press / other), message.
- **Consent:** (1) required, unticked: "I have read the privacy notice and agree that NeuroNetworks AI Ed may contact me about my enquiry" linking to `/privacy`; (2) required for the parent path, unticked: "I am the parent or legal guardian and I consent on behalf of my child" ; (3) optional, unticked: "Send me updates and learning guides". Store which boxes were ticked, timestamp (IST), and the notice version.
- **Anti-abuse:** Cloudflare Turnstile (managed), honeypot field (hidden, `autocomplete="off"`, `tabindex="-1"`), Cloudflare rate limiting rule on `/api/enquiry`, server-side validation of every field, max body size.
- **Accessibility:** real `<label>`s, error summary with focus management, `aria-live` status, no placeholder-only labels, large touch targets, works without JS via a standard POST fallback to the same endpoint returning a redirect to `/apply/thanks`.

### 6.2 API route `src/pages/api/enquiry.ts`
```ts
export const prerender = false;
import type { APIRoute } from 'astro';
import { env } from 'cloudflare:workers';   // Astro 6+/adapter v13+: env comes from here (verify in docs)

export const POST: APIRoute = async ({ request }) => {
  // 1. Parse (JSON or form), enforce content-length, same-origin check (Origin header)
  // 2. Validate with Zod; reject honeypot hits silently with 200
  // 3. Verify Turnstile token: POST https://challenges.cloudflare.com/turnstile/v0/siteverify
  //    body { secret: env.TURNSTILE_SECRET, response: token, remoteip? } (tokens are single use)
  // 4. Append a row to Google Sheets (see 6.3)
  // 5. Send notification email (see 6.4)
  // 6. Return 200 JSON { ok: true } or 303 redirect to /apply/thanks for non-JS POST
};
```
Errors return a generic message to the client and log details server-side without personal data. Never echo input back unescaped.

### 6.3 Google Sheets without the Node SDK (Workers cannot run `googleapis`)
1. Owner creates a Google Cloud project, enables the Sheets API, creates a **service account**, downloads the JSON key, and **shares the Sheet with the service account's email as Editor**. Secrets set with `wrangler secret put GOOGLE_SERVICE_ACCOUNT_JSON` (and `TURNSTILE_SECRET`, `RESEND_API_KEY`). Non-secret vars in `wrangler.jsonc`: `GOOGLE_SHEET_ID`, `NOTIFY_TO`, `NOTIFY_FROM`.
2. Sign a JWT with Web Crypto and exchange it for an access token:
   ```ts
   async function accessToken(sa: {client_email: string; private_key: string}) {
     const enc = (o: object) => btoa(JSON.stringify(o)).replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
     const now = Math.floor(Date.now()/1000);
     const unsigned = enc({alg:'RS256',typ:'JWT'}) + '.' + enc({
       iss: sa.client_email, scope: 'https://www.googleapis.com/auth/spreadsheets',
       aud: 'https://oauth2.googleapis.com/token', iat: now, exp: now + 3600 });
     const pem = sa.private_key.replace(/-----[^-]+-----|\s/g,'');
     const key = await crypto.subtle.importKey('pkcs8', Uint8Array.from(atob(pem), c => c.charCodeAt(0)),
       { name: 'RSASSA-PKCS1-v1_5', hash: 'SHA-256' }, false, ['sign']);
     const sig = await crypto.subtle.sign('RSASSA-PKCS1-v1_5', key, new TextEncoder().encode(unsigned));
     const jwt = unsigned + '.' + btoa(String.fromCharCode(...new Uint8Array(sig))).replace(/=/g,'').replace(/\+/g,'-').replace(/\//g,'_');
     const r = await fetch('https://oauth2.googleapis.com/token', { method:'POST',
       headers:{'content-type':'application/x-www-form-urlencoded'},
       body: new URLSearchParams({ grant_type:'urn:ietf:params:oauth:grant-type:jwt-bearer', assertion: jwt }) });
     return (await r.json()).access_token as string;
   }
   ```
3. Append a row: `POST https://sheets.googleapis.com/v4/spreadsheets/{ID}/values/Enquiries!A:Z:append?valueInputOption=RAW&insertDataOption=INSERT_ROWS`, `Authorization: Bearer <token>`, body `{ values: [[...]] }`.
4. **Neutralise formula injection:** with `RAW` strings stay text, but also prefix any cell beginning with `=`, `+`, `-`, `@` with a single quote.
5. **Sheet layout** (tab `Enquiries`, frozen header, protected header row): `submitted_at_ist, form, role, full_name, email, mobile, city, state, programs, age_band, parent_name, preferred_time, message, consent_privacy, consent_parent, consent_updates, notice_version, source_path, utm_source, utm_medium, utm_campaign, status, assigned_to, notes`. Last three are for the team. Do **not** store IP addresses or user-agents. Restrict Sheet sharing to named team members.
6. Retention: add a `delete_by` date column (default 12 months after last contact, owner to confirm) and a documented process to honour deletion requests.

### 6.4 Email
- **Notification to the team + confirmation to the enquirer** via a transactional email API from the Worker (Resend recommended; any equivalent works). Send from `no-reply@neuronetwrks.com`; replies go to a monitored address.
- **DNS caution:** there must be exactly **one SPF record**. Merge providers into it, for example `v=spf1 include:_spf.google.com include:<provider> ~all`. Add the provider's DKIM CNAME/TXT records. Do **not** touch Google's MX/DKIM. Do **not** enable Cloudflare Email Routing (it conflicts with Google Workspace MX).
- Alternative with no extra vendor: an Apps Script attached to the Sheet with an installable `onChange` trigger that emails the team on new rows. Test that rows added by the API trigger it before relying on it.
- Email copy: plain text plus a simple HTML version, no tracking pixels.

### 6.5 Tests
Playwright: happy path (each role), under-18 path forces parent flow, missing consent blocks submit, honeypot is ignored, invalid mobile rejected, Turnstile failure shows an error, JS-disabled POST works, double-submit is safe. Verify a test row lands in a **separate test Sheet** first, then switch to the real one.

**Exit criteria:** end-to-end submission appears in the Sheet and in the inbox; consent fields recorded; no secrets in git; tests green.

---

## PHASE 7: Blog engine and content calendar

### 7.1 Engine
- Posts in `src/content/posts/*.mdx`. Template: H1, byline (real author, avatar, role), dates (`Published`, `Last updated`), reading time, **TL;DR box** (answer in 2–3 sentences), table of contents (auto from H2/H3), body with answer-first H2s, comparison tables where useful, a "Key facts" definition list, FAQ (3–5, marked up), "Related programs" block with 2 program links, "Related guides", sources list.
- Listing at `/resources`, categories at `/resources/category/<cat>` (static routes), pagination at 12 per page (`rel` links via normal anchors), RSS.
- **Scheduled publishing:** `getCollection('posts', p => !p.data.draft && p.data.pubDate <= new Date())` in every route and in sitemap/RSS/llms.txt. Future-dated posts are excluded until the day they are due.
- **Daily rebuild:** GitHub Actions workflow `schedule.yml` (cron `30 18 * * *` UTC ≈ 00:00 IST) that builds and deploys with `cloudflare/wrangler-action`. This publishes posts on their `pubDate` and runs IndexNow for new URLs.
- Writing rules: no invented statistics; cite primary sources (government, standards bodies, vendor docs) with links; name the author; update dates when content changes; include India-specific context (boards such as CBSE/ICSE/state, class levels 6–12, entrance and career paths) only when accurate and sourced; never make income, job, or admission guarantees.

### 7.2 Twelve-week calendar (two posts per week, 24 posts; weeks start at launch)
| Wk | Post A (primary keyword, intent) | Post B |
|---|---|---|
| 1 | What is AI? A plain-language guide for students and parents (what is AI for kids; informational) | How to learn AI from scratch in India: a 12-month roadmap (how to learn AI from scratch) |
| 2 | AI vs machine learning vs data science: what is the difference? | Do you need to know coding to learn AI? |
| 3 | How to choose an AI course for school students in India: a checklist (best AI courses for kids India; commercial) | AI career after 12th: paths, subjects and skills |
| 4 | Python for AI beginners: what to learn first | Prompt engineering for students: a practical guide |
| 5 | Generative AI explained for teens: how ChatGPT and Gemini work | Data science roadmap for India: skills, tools and projects |
| 6 | Cybersecurity careers in India: roles and how to start | Ethical hacking for beginners: what is legal, what is not, and where to learn |
| 7 | Full-stack developer roadmap for India | Software development vs AI engineering: which to choose? |
| 8 | UX design course in India: what to look for | How AI is changing product and UX design |
| 9 | How working professionals can learn AI next to a job | How to move from software development to AI engineering |
| 10 | How schools can introduce AI in the curriculum | AI literacy for classes 6–12: age-appropriate topics |
| 11 | AI certifications in India: what they are and how to compare them | How to build an AI project portfolio as a student |
| 12 | A parent's guide to judging an AI course: safety, data privacy, outcomes | Machine learning course online: a syllabus checklist |
Each post maps to one primary keyword, links to 2 program pages and 1 audience page, and includes a 3–5 question FAQ. After week 12, run a keyword review from Search Console data and plan the next batch (use the `searchfit-seo:content-strategy` and `keyword-clustering` skills if available).
Write posts in the owner's brand voice (plain, specific, no hype). Draft all week-1 posts before launch; stage the rest as future-dated.

**Exit criteria:** template reviewed on one real post; scheduling proven with a future-dated test post; 4 launch posts ready; calendar saved in `docs/content-calendar.md`.

---

## PHASE 8: Deploy, domain, DNS, email safety

### 8.1 Cloudflare deployment (Workers static assets)
- `wrangler.jsonc` (verify keys against current docs): `name`, `compatibility_date` (today), `assets.directory: "./dist"` (static) and the Astro adapter's worker entry for `/api/*`. Follow the current Astro "Deploy to Cloudflare" guide exactly; Cloudflare now recommends Workers (not Pages) for new projects and the current Astro Cloudflare adapter no longer supports Pages.
- GitHub Actions `deploy.yml` on push to `main`: `npm ci`, `npm run check`, `npm run build`, `npx wrangler deploy` via `cloudflare/wrangler-action` with repo secrets `CLOUDFLARE_API_TOKEN` (scoped: Workers Scripts edit, plus Zone DNS edit only if automating DNS) and `CLOUDFLARE_ACCOUNT_ID`. Preview deploys for PRs get `noindex`.
- Custom domains: add `neuronetwrks.com` and `www.neuronetwrks.com` as Worker Custom Domains. Redirect `www` to apex with a Redirect Rule (301).
- Cloudflare settings: SSL/TLS "Full (strict)", Always Use HTTPS, HTTP/3, Brotli, Early Hints, Crawler Hints on (sends IndexNow), Bot Fight Mode on but not blocking legitimate search/AI crawlers, Turnstile widget with hostname `neuronetwrks.com`, rate limiting rule on `/api/enquiry` (for example 5 requests per minute per IP).

### 8.2 Move DNS from Squarespace to Cloudflare without breaking email
Based on the screenshots the owner provided, the current DNS contains: Squarespace default A records (`@` → 198.185.159.144, .145, 198.49.23.144, .145), `www` CNAME → `ext-sq.squarespace.com`, an HTTPS record, a `_domainconnect` CNAME, and custom records: **MX `@` priority 1 → `smtp.google.com`**, **TXT SPF `v=spf1 include:_spf.google.com ~all`**, and **TXT DKIM `google._domainkey`** (long `v=DKIM1; k=rsa; p=…` value).
1. **Back up first:** screenshot or export every record. Copy the full DKIM value from Squarespace (it is truncated on screen).
2. Add the domain to Cloudflare (Free plan). Let it scan, then manually compare. **Keep exactly:** the Google MX (`smtp.google.com` priority 1, or whatever Google Workspace currently specifies; if the owner's Workspace admin console shows the older five-record `aspmx.l.google.com` set, use what the admin console says), the SPF TXT, the DKIM TXT, and any Google site-verification TXT. **Do not copy:** Squarespace A records, the `www` CNAME to Squarespace, the Squarespace HTTPS record, `_domainconnect`.
3. All MX/TXT records are **DNS-only** (grey cloud). Add a DMARC record to start monitoring: TXT `_dmarc` = `v=DMARC1; p=none; rua=mailto:<owner mailbox>`; tighten later.
4. At Squarespace: switch off DNSSEC if enabled, then replace nameservers with the two Cloudflare nameservers shown in the dashboard. Wait until Cloudflare shows the zone Active, then re-enable DNSSEC in Cloudflare if wanted.
5. Attach the Worker custom domain (this creates the apex and `www` records automatically). **Do not enable Cloudflare Email Routing.**
6. **Test email immediately:** send to and from the Workspace mailbox; in Gmail "Show original" confirm SPF, DKIM and DMARC pass. Test the website over HTTPS on apex and `www`.
7. The domain registration can stay at Squarespace; transferring it to Cloudflare Registrar is optional later (no DNS edits during a transfer).
8. Flip `PUBLIC_ENV=production` only when everything above passes and content is final.

**Exit criteria:** site live on `https://neuronetwrks.com`, `www` redirects, email in/out verified, headers verified with a header-check tool, staging remains noindex.

---

## PHASE 9: QA and performance

Automate everything possible; the owner reviews screenshots, not code.
1. **Playwright e2e** at 390×844 and 1440×900 and a tablet size: navigation, menu, all CTAs, forms (Phase 6 cases), keyboard-only navigation, focus visibility, reduced-motion, JS-disabled.
2. **Lighthouse CI** budgets: Perf ≥ 0.95, A11y ≥ 0.95, Best Practices ≥ 0.95, SEO ≥ 0.98; LCP ≤ 1.8 s; CLS ≤ 0.05; TBT ≤ 150 ms; total JS and image budgets per page type.
3. **Chrome DevTools MCP**: record performance traces with 4× CPU and Slow 4G; capture INP; list long tasks; fix the top offender.
4. **pa11y-ci / axe** on every route; manual screen-reader pass on home, a program page, and the form (VoiceOver/NVDA notes).
5. **Link check** (internal and external), image `alt` audit, heading-order audit, duplicate title/description audit, canonical audit, orphan page audit.
6. **Structured data**: validate every template in Rich Results Test and validator.schema.org; save results.
7. **Security**: headers, CSP violations, dependency audit (`npm audit`), secret scan, form abuse tests, CORS.
8. **Visual QA**: compare against the design system, check at 320, 390, 768, 1024, 1440, 1920 widths, dark/light OS settings (site is light only; `color-scheme: light`), print stylesheet for program pages (clean, with URL).
9. **Content QA**: no `{{CONFIRM`, no lorem, no invented claims, tagline exact, spelling is Indian/British English where the owner prefers (confirm), numbers match the curriculum documents.
10. Run the `searchfit-seo` skills (technical-seo, on-page-seo, schema-markup, ai-visibility) and `design:accessibility-review` if installed, and report findings.

---

## PHASE 10: Launch and measurement

1. **Google Search Console:** add a **Domain property** (DNS TXT verification in Cloudflare), submit `sitemap-index.xml`, request indexing for home and each program page, then check Coverage weekly.
2. **Bing Webmaster Tools:** import from GSC (Bing feeds ChatGPT/Copilot search), submit sitemap, enable IndexNow.
3. **GA4:** create a property and a web data stream for `neuronetwrks.com`. Load `gtag` through Partytown **after** consent (consent mode default denied). Events: `apply_start`, `apply_submit`, `talk_click`, `program_view` (with `program_name`), `scroll_75`, `outbound_click`, `resource_read`. Mark `apply_submit` and `talk_submit` as key events. **No** remarketing, Google Signals, or ad personalisation. No analytics profiling of under-18s.
4. **Consent banner:** minimal, accessible, two equal buttons (Accept analytics / Reject), remembered in `localStorage` with try/catch, links to the privacy notice.
5. **Uptime and errors:** Cloudflare analytics and an uptime monitor on `/` and `/api/enquiry` (health check route that does not write).
6. **Weekly SEO routine** (a scheduled task or a Claude command): top queries and pages from GSC, pages with impressions but low CTR (rewrite title/description), new keyword opportunities, indexing issues, Core Web Vitals report, AI-referral traffic in GA4, and a 3-line summary for the owner.
7. **GEO monitoring:** monthly, ask ChatGPT, Perplexity, Gemini, and Claude the target questions ("best AI courses for school students in India", etc.) and record whether and how NeuroNetworks is cited; update content accordingly.
8. **Post-launch week 1 checklist:** form test from a phone, email test, broken-link scan, GSC coverage, Lighthouse on production, social profile links, 404 monitoring.

---

## Appendix A: Anti-AI-look rules (enforced in review)

Reject any section that shows: purple/blue gradient hero; Inter/Space Grotesk/Poppins as the primary face; centred everything; three identical rounded cards with soft shadows; gradient text on multiple headings; glass blobs; particles/neural-net/brain visuals; emoji icons; tracked all-caps eyebrow over every heading; numbered 01/02/03 when not a real sequence; fade-up on every section; stat tiles with invented numbers; fake logos/testimonials; hype copy ("unlock", "revolutionise", "cutting-edge", "seamless", "journey", "empower"); lorem ipsum.
Do instead: confident asymmetric layouts; large, well-set type; real photography; honest specifics from the curriculum; rare, meaningful motion; generous whitespace; hairline rules; one accent colour doing most of the work.

## Appendix B: Definition of done (whole site)
All routes live · Lighthouse ≥ 95 on mobile for every page · CWV budgets met on throttled Android · WCAG 2.2 AA · valid JSON-LD · sitemap, robots, llms.txt, RSS · form end-to-end to Sheet and email with DPDP-aware consent · DNS migrated with email verified · GSC, Bing, GA4 live · 4+ launch posts and 24 scheduled · no `{{CONFIRM` · `docs/PLAN.md` status table fully green · owner has reviewed screenshots and approved launch.

## Appendix C: What to report at the end of each phase (5 lines)
1. What was built. 2. What was tested and the results. 3. What could not be tested and why. 4. Open questions added to `docs/open-questions.md`. 5. What the owner must do next.
