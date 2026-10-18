---
name: programmatic-seo-page
description: Build many small, high-quality SEO pages from one keyword pattern for neuronetwrks.com (for example "how to become [role] after 10th" or "[topic] project ideas for students"). Use when the owner asks for new SEO pages, a new keyword pattern, more pages "like the reference page", programmatic SEO, or Claude Traffic plan steps 3 to 5.
---

# Programmatic SEO pages (NeuroNetworks AI Ed)

One keyword pattern → many pages, each answering one small real question, all built from one template and one data
file per page. The page engine is `tools/preview-gen/seo_pages.py`; pages live in `tools/preview-gen/seo/<pattern>/<slug>.json`.
Reference examples: `seo/project-ideas/python-project-ideas-for-students.json` (engine) and the 20 live career roadmaps in
`tools/preview-gen/careers/` (older dedicated renderer `career_pages.py`, same rules).

Always apply the project rules too: skills `neuronetworks-voice` and `neuronetworks-seo`, and `/home/user/NeuroNetwrks.com/CLAUDE.md`.

## The 4 things every page must nail
1. **Unique angle.** Built from our own data (real modules, hours, projects, monthly rhythm) plus an honest section
   (what the program does not cover, or who should not choose this). Generic advice alone fails this test.
2. **Fresh data.** 1 to 3 current sources per page that you actually opened (official certification pages, Indian
   government or industry pages). Each source gets a date. If a fact cannot be checked, leave it out.
3. **SEO + AI search.** Title ≤ 60, description ≤ 155, "In short" box (3 bullets), every H2 a question whose first
   sentence answers it, 5 FAQs, schema (Article, FAQPage, BreadcrumbList are added automatically), sitemap and llms.txt (automatic).
4. **Goal blended.** The program link sits inside the content where the reader is thinking "how do I do this?", with a
   `talk` block (Talk to us / Apply) right after it, not only at the end.

## Workflow (follow in order; tell the owner at each step)
1. **Pick the pattern and keywords.** Read `docs/seo/keyword-map.md` and the owner's Traffic plan. List 10 to 20 keywords
   in the pattern with search numbers if known ("" if not). Ask the owner to check volumes in a free tool when unknown.
   Drop near-zero keywords. Check no existing guide already answers the same question (`ls tools/preview-gen/careers seo/*/`
   and `GUIDES` in `guides_pages.py`); if one does, upgrade it instead of duplicating.
2. **Create the pattern folder** with `python3 .claude/skills/programmatic-seo-page/scripts/new_pattern.py <pattern-slug> "<Name>" "<keyword pattern>"`.
   Edit `pattern.json`: `headline`, `intro`, and `required_faq` (words every page's FAQ must contain, e.g. "how many years").
3. **Design the section outline once** for the pattern (see `references/patterns.md` for proven outlines). Write it into
   `seo/<pattern>/OUTLINE.md`. Every section is a question. Decide where the program block and talk box go.
4. **Build ONE reference page** by hand: research sources, write the JSON (`references/blocks.md` lists every block),
   run `python3 tools/preview-gen/seo/check.py`, build (`cd tools/preview-gen && python3 build.py`), screenshot desktop 1440
   and phone 390, and show the owner. Do not scale until the owner approves the reference page.
5. **Scale.** Split the remaining keywords across 3 to 4 background agents (general-purpose). Give each: the OUTLINE.md,
   the reference JSON, `references/blocks.md`, the facts file `site-preview/llms-full.txt`, and the rules below. Each agent must
   run `seo/check.py` on its files until OK. Each page must differ from its siblings (definition, examples, FAQs).
6. **Show progress.** Keep the owner's live board updated (an Artifact page republished after each step: queued, writing,
   checked, built, live). The generator from 18 Oct 2026 is in the session scratchpad `board/`; recreate it if missing.
7. **Verify.** Run the checker on all files, build, check internal links (no 404s), titles/descriptions, H2 questions, schema,
   screenshots of a sample of pages on desktop and phone, no sideways scroll.
8. **Deploy only after the owner says so.** Steps are in `memory/neuronetworks-website-memory/chunks/04-deploy-domain-seo.md`
   (build, copy `site-preview` to a scratch dir, `npx vercel@latest deploy --prod --yes`, then `python3 tools/preview-gen/indexnow.py`).
   Keep `NNBOT_ON = False` in `build.py` unless the owner has approved the robot.
9. **Record it.** Commit and push to `preview-site`, update `docs/seo/keyword-map.md` and the memory chunk 07-pending.

## Hard content rules (the checker enforces most of them)
- Facts only from `site-preview/llms-full.txt`, the owner, or sources you opened. No invented numbers, students, success
  rates, testimonials, ratings, placements, partners or faculty names. Project names in `highlight` must match the program list exactly.
- No fees or prices anywhere. CTAs only "Apply" and "Talk to us". Classes are online; batch timings "shared on enquiry".
- External certifications: preparation only, awarded by the certifying body, passing not guaranteed, never their costs.
- Salary: only through the `program_salary` block (indicative, with the not-guaranteed note).
- Certificate on completion is a NeuroNetworks AI Ed certificate, not a degree. AI Foundation is open from Class 8; 3-year programs need Class 10 pass.
- Plain words, sentences under 25 words, active voice, sentence case. No em dashes. Never: unlock, revolutionise, cutting-edge,
  seamless, journey, delve, game-changer, unleash, empower. Byline is "NeuroNetworks AI Ed team" (automatic).
- Honest gaps: if the program does not teach something the keyword needs, say so in a `callout` block.
