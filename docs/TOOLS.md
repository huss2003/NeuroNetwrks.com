# TOOLS: repos, skills, plugins, MCP servers and setup (Claude Max, Claude Code on the web)

Legend: **V** = verified in the October 2026 research against official docs or the repo; **U** = exists to the best of the research but install command or stars not re-verified (check the README first); **C** = community, not screened by Anthropic (read the code before granting access).

## 1. Setup for Claude Code on the web
1. Create the private GitHub repo `neuronetwrks`, commit `CLAUDE.md`, `docs/PLAN.md`, `docs/BUILD_PROMPT.md`, `docs/TOOLS.md`, and the owner files in `docs/source/`.
2. Open claude.ai/code, connect GitHub, select the repo, start a session.
3. First commands: `/model opusplan`, then `/mcp` (see which servers connected), then `/plugin` (install the plugins in section 3).
4. Paste the start prompt from the top of `docs/BUILD_PROMPT.md`.
5. Keep production secrets out of the session. Claude works with test keys and a test Sheet; real secrets live in Cloudflare and GitHub secrets, set by the owner.
6. The web sandbox restricts network access to an allowlist (npm and GitHub normally work; arbitrary sites may not). Self-host fonts and avoid build-time fetches from other domains. Some stdio MCP servers may be unavailable on the web; Claude falls back to the Playwright and Lighthouse command-line tools.
7. Deploys run from GitHub Actions after you merge a pull request. Claude opens PRs; you (or Claude, if you ask) merge when CI is green.

## 2. Claude Max plan: how to make it last
- **Plan (V, Anthropic support pages):** Max 5x is $100/month and Max 20x is $200/month. Usage limits are shared across Claude and Claude Code; the session limit resets every five hours; there is also a weekly limit across models; Max also has a separate weekly limit for Fable. Monthly API credits included with Max cannot be used in Claude Code. Anthropic has doubled Claude Code's five-hour limits for Max and other plans.
- **Models (V):** Claude Opus 5.5 (released 22 Sep 2026) and Sonnet 5.5 (28 Sep 2026), both with 1M context; Haiku 5.5 reported 7 Oct 2026 (secondary sources). **Conflict:** Anthropic's model-config page says Max defaults to Opus 5 while a third-party guide says Opus 5.5 is the default from v2.1.280; run `/model` to see yours.
- **Recommended use:** `/model opusplan` (Opus plans in plan mode, Sonnet builds). Switch to Opus for design direction, animation choreography and hard debugging (`/model claude-opus-5-5`). Use Haiku for repetitive passes (meta descriptions, alt text, FAQ drafts).
- **Habits that save limits:** plan mode first; one phase per session; `/compact` between phases and `/clear` between topics; keep `CLAUDE.md` short; let scripts do heavy lifting (Lighthouse, pa11y, link check) and have Claude read only summaries; use subagents for broad research or audits so the main context stays small; never paste whole documents (point to files); stop and review at the end of each phase.
- **Check usage** in Claude settings and with `/status` or `/usage` (commands may differ by version).

## 3. Anthropic and Claude Code ecosystem
| Item | What it does here | Install / link | Status |
|---|---|---|---|
| anthropics/skills | Official skills: `frontend-design` (avoids templated looks), `skill-creator` (build our own SEO and voice skills) | `/plugin marketplace add anthropics/skills` or `npx skills add anthropics/skills --skill frontend-design`; https://github.com/anthropics/skills | V (frontend-design, skill-creator); other skills U |
| anthropics/claude-plugins-official | Official marketplace: `frontend-design`, `code-review`, `security-guidance`, `commit-commands`, `feature-dev`, `plugin-dev`, partner plugins | Added by default; `/plugin install frontend-design@claude-plugins-official`; https://github.com/anthropics/claude-plugins-official | V |
| anthropics/claude-plugins-community | Screened community marketplace | `/plugin marketplace add anthropics/claude-plugins-community` | V |
| anthropics/claude-code | Demo marketplace and CLI repo | `/plugin marketplace add anthropics/claude-code`; https://github.com/anthropics/claude-code | V |
| obra/superpowers | Workflow skills (brainstorm, plan, TDD, review); ~298k stars at research time | `superpowers@claude-plugins-official`; https://github.com/obra/superpowers | V |
| hesreallyhim/awesome-claude-code | Curated index of skills, hooks, commands, CLAUDE.md examples; ~55.5k stars | https://github.com/hesreallyhim/awesome-claude-code | V |
| wshobson/agents | Large set of subagents and skills; review before installing | https://github.com/wshobson/agents | U, C |
| awesome-claude-skills (travisvn or ComposioHQ) | Skill directories | search GitHub | U |
| Astro Docs MCP and Astro agent rules | Official Astro docs for agents (announced April 2026); copy its rules into CLAUDE.md | see https://astro.build/blog/whats-new-april-2026/ | U for Claude Code |
| SEO-specific Claude skills | No authoritative public one found; build `neuronetworks-seo` with `skill-creator` | n/a | gap |

**Skills already visible in your Claude workspace** (confirm with `/skills` in Claude Code; account skills may not sync to the web): `frontend-design`, `searchfit-seo:technical-seo`, `on-page-seo`, `schema-markup`, `ai-visibility`, `keyword-clustering`, `content-strategy`, `content-brief`, `internal-linking`, `broken-links`, `seo-audit`; `marketing:seo-audit`, `content-creation`, `draft-content`; `design:accessibility-review`, `design-critique`, `design-system`, `ux-copy`; `engineering:code-review`, `deploy-checklist`, `testing-strategy`, `documentation`; `anthropic-skills:skill-creator`, `web-artifacts-builder`, `docx`, `pdf`.

## 4. MCP servers (project scope in `.mcp.json`)
| Server | Purpose | Command | Status |
|---|---|---|---|
| Context7 (Upstash) | Current docs for Astro 7, GSAP, Tailwind v4, Lenis, Three.js | `claude mcp add --transport http context7 https://mcp.context7.com/mcp` (or `npx -y @upstash/context7-mcp`); https://github.com/upstash/context7 | U (listed in research; verify README) |
| Playwright MCP (Microsoft) | Click-through tests, screenshots at mobile and desktop | `claude mcp add playwright npx @playwright/mcp@latest`; https://github.com/microsoft/playwright-mcp | V |
| Chrome DevTools MCP (Google) | Performance traces, INP/LCP, console and network | `claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest`; https://github.com/ChromeDevTools/chrome-devtools-mcp | V |
| GitHub MCP | Issues and PRs | `claude mcp add --transport http github https://api.githubcopilot.com/mcp/` or `github@claude-plugins-official` | U |
| Cloudflare MCP servers | Docs, Workers, observability, DNS analytics | `claude mcp add --transport http cloudflare-docs https://docs.mcp.cloudflare.com/mcp`; https://github.com/cloudflare/mcp-server-cloudflare | U (check README for the current endpoint list) |
| Figma MCP | Pull tokens/frames if you later use Figma | `claude mcp add --transport http figma https://mcp.figma.com/mcp` | U |
| Google Analytics MCP | Query GA4 from Claude after launch | https://github.com/googleanalytics/google-analytics-mcp | U |
| Google Search Console MCP | Query clicks and queries (community only) | search GitHub for `mcp-gsc` | C |
| Firecrawl MCP | Competitor page structure audits (paid API key) | `claude mcp add firecrawl -e FIRECRAWL_API_KEY=… -- npx -y firecrawl-mcp` | U |
| Lighthouse MCP | Optional; Chrome DevTools MCP plus Lighthouse CI cover this | community | C |
Treat every "U" command as "read the repo README before running it". Never put API keys in `.mcp.json`; use environment variables.

## 5. Build libraries (npm)
| Package | Why | Link | Status |
|---|---|---|---|
| astro (7.x) | Framework; static HTML; agent-aware dev server | https://docs.astro.build; release notes https://astro.build/blog/astro-7/ | V (7.0 on 22 Jun 2026; patch version via third-party tracker, check `npm view astro version`) |
| @astrojs/cloudflare | Adapter for the `/api` route; v13+ no longer supports Pages | https://docs.astro.build/en/guides/integrations-guide/cloudflare/ | V |
| @astrojs/sitemap, @astrojs/mdx | Sitemap; MDX content | https://docs.astro.build/en/guides/integrations-guide/ | V |
| tailwindcss + @tailwindcss/vite | Tailwind v4 | https://tailwindcss.com/docs/installation/framework-guides/astro | V |
| gsap (ScrollTrigger, SplitText) | Core animation; all plugins free since 3.13 (29 Apr 2025) | https://gsap.com/blog/3-13/ | V |
| lenis | Smooth scroll on native scroll; official GSAP sync pattern | https://github.com/darkroomengineering/lenis | V |
| three | The one lazy 3D ribbon | https://threejs.org | U |
| ogl (alternative) | Much smaller WebGL if the ribbon is simplified | https://github.com/oframe/ogl | U |
| motion (motion.dev) | Optional micro-interactions | https://motion.dev | U |
| astro-seo | Typed SEO head component | https://github.com/jonasmerlin/astro-seo | U |
| schema-dts or astro-seo-schema | Typed JSON-LD | https://github.com/codiume/orbit (verify package location) | U |
| astro-og-canvas | Build-time OG images | https://github.com/delucis/astro-og-canvas | U |
| satori + @resvg/resvg-js | Fully designed OG images | https://github.com/vercel/satori | U |
| astro-icon | Inline SVG icons, no runtime JS | https://github.com/natemoo-re/astro-icon | U |
| @astrojs/partytown | Run GA4 off the main thread | https://docs.astro.build/en/guides/integrations-guide/partytown/ | V |
| @fontsource-variable/* | Self-hosted variable fonts | https://fontsource.org | U |
| @casoon/astro-crawler-policy | robots.txt and llms.txt with per-bot AI rules | listed in https://astro.build/blog/whats-new-april-2026/ | U |
Rejected on purpose: tsParticles and similar particle backgrounds (reads as generic AI aesthetic, costs main-thread time), Spline runtime on the home page (heavy), `<ClientRouter />` (forces motion re-initialisation) unless approved.

## 6. Starter templates to study (structure only; do not copy the look)
AstroWind (https://github.com/onwidget/astrowind), Astroship (https://github.com/surjithctly/astroship), ScrewFast (https://github.com/mearashadowfax/ScrewFast), AstroPaper for blog structure (https://github.com/satnaing/astro-paper), official theme catalogue (https://astro.build/themes/). Stars and last-updated dates were not re-verified; check before relying on them.

## 7. Quality, audit and SEO tooling
| Tool | Use | Link | Status |
|---|---|---|---|
| Lighthouse CI | Budgets in CI | https://github.com/GoogleChrome/lighthouse-ci | U |
| Unlighthouse | Crawl all pages | https://github.com/unlighthouse/unlighthouse | U |
| pa11y / pa11y-ci | Accessibility regression | https://github.com/pa11y/pa11y | U |
| Rich Results Test, Schema Markup Validator | Validate JSON-LD | https://search.google.com/test/rich-results ; https://validator.schema.org | V |
| PageSpeed Insights / CrUX | Field data (INP) | https://pagespeed.web.dev | V |
| Web Vitals thresholds | LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 (we use stricter targets) | https://web.dev/articles/vitals | V |
| IndexNow | Bing/Yandex instant indexing | https://www.indexnow.org | V |
| Google Search Console, Bing Webmaster Tools, GA4 | Search and traffic data | Google and Microsoft consoles | V |

## 8. Forms and operations
- Turnstile server-side validation (required; tokens single use): https://developers.cloudflare.com/turnstile/get-started/server-side-validation/ (V)
- Reference Worker + Sheets API service-account implementation: https://github.com/awbauer/gsheet-form-handler (U; it gates by Cloudflare Access, remove that for a public form)
- Google auth on Workers without the Node SDK (JWT with Web Crypto): see the guide cited in the research (Medium, "How to authenticate Google APIs on Cloudflare Workers", U)
- Cloudflare Google Workspace DNS guide: https://developers.cloudflare.com/dns/manage-dns-records/how-to/set-up-google-workspace/ (V)
- Squarespace domain transfer / DNS notes: https://support.squarespace.com/hc/en-us/articles/205812338-Transferring-a-domain-away-from-Squarespace (V)
- DPDP background (not legal advice): see the research notes; have a lawyer review.

## 9. Install order (do this in the first session)
1. `/model opusplan`
2. `/plugin install frontend-design@claude-plugins-official`, `code-review`, `security-guidance`
3. `/plugin marketplace add anthropics/skills` then add `skill-creator`
4. Add MCP: Context7, Playwright, Chrome DevTools, GitHub, Cloudflare docs; run `/mcp`
5. Create project skills `neuronetworks-seo` and `neuronetworks-voice` with `skill-creator`
6. Start Phase 0
