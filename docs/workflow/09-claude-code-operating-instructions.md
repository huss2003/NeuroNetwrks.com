# 9. Claude Code operating instructions

This part explains how to use Claude Code to run the whole workflow without damaging features that already work. You do not need to read code. You need to ask for a plan, read it, approve it, look at screenshots and the preview link, and say yes or no.

## The ten rules

1. **Plan mode first.** Start with `claude --permission-mode plan`, or press Shift+Tab until the status bar shows plan mode. Claude reads and proposes; it edits nothing until you approve ([Claude Code docs](https://code.claude.com/docs/en/common-workflows)).
2. **Read the rules every time.** Each repo has a `CLAUDE.md` and an `AGENTS.md`. Ask Claude Code to read both before planning. Where they conflict with this manual, the repo rule wins until you change it.
3. **One small branch per change.** One asset, one component or one fix per pull request. Never "redo the homepage".
4. **Tests before and after.** Claude Code runs the existing tests before touching anything. If they already fail, it stops and tells you.
5. **Screenshots for you.** Every visual change comes with Playwright screenshots at 390×844 (phone) and 1440×900 (laptop), before and after.
6. **Manifest in the same PR.** Any asset change updates `asset-manifest.json`.
7. **Never rebuild working features.** Improve in place. If Claude Code proposes replacing something that works (the AI/ML card loader, the lecture timeline, the grader flow), ask why and say no unless the reason is strong.
8. **No new dependencies without a reason.** The PR description must say what was added, why, and how much it adds to the download size.
9. **No deploys or pushes to `main` without you.** Claude Code opens a PR; you merge.
10. **Honest reports.** Every summary lists what was run, the results, and what was not run.

## Repo-specific rules Claude Code must respect

### Website (`huss2003/NeuroNetwrks.com`)

- No prices anywhere. CTAs "Apply" and "Talk to us".
- WCAG 2.2 AA; respect `prefers-reduced-motion`.
- LCP element is HTML text or an optimised image, never a canvas.
- WebGL loads by dynamic `import()` after intersection, with a poster fallback.
- Home page JavaScript ≤ 100 KB gzip before interaction.
- Banned visuals: purple or blue gradients, glassmorphism blobs, particle or neural-network backgrounds, brain imagery.
- Approved WebGL objects: the AI/ML card and NN-Bot only.
- Known gap: the website `CLAUDE.md` describes an Astro + Cloudflare stack and "one WebGL object maximum", but the live site is the Python generator on Vercel with two approved WebGL objects. Ask Claude Code to propose a CLAUDE.md update for your approval before Phase 4 continues.

### Lab (`huss2003/Neuromind-lab`)

- "Never expand scope without approval."
- "If docs conflict, stop and report the conflict; do not silently choose." (The DESIGN_SYSTEM.md versus styles.css conflict is one.)
- "Never render student output as HTML."
- Add or update tests with each behaviour change; never weaken tests to get a green build.
- "Never add paid hosting, Redis, paid AI APIs or GPU infrastructure without approval." Treat paid design-tool plans the same way.
- Scores and completion stay server-authoritative.

## The standard session, step by step

1. Open the repo folder in a terminal. Run `git status` (or ask Claude Code to) and make sure there are no surprise changes. In the website repo today, some new Blender scripts are untracked; decide whether they belong in the next commit.
2. Start `claude --permission-mode plan`.
3. Paste the task prompt (examples below).
4. Read the plan. Check: files touched, files not touched, tests, screenshots, risks.
5. Approve. Claude Code creates a branch, works, tests and opens a PR.
6. Open the Vercel preview. Check on your phone and laptop.
7. Ask follow-up questions in plain language.
8. Merge, or ask for changes.
9. After merging, ask Claude Code to confirm the live site and run the smoke test.

## Example prompts

### Start of any session

```text
Read CLAUDE.md and AGENTS.md in this repo and docs/workflow/README.md.
Summarise in five bullet points the rules that apply to visual and 3D work.
Then wait for my task. Do not edit anything.
```

### New Blender asset (website)

```text
Plan only. Build the "data-science-pipeline" program model using the same approach
as tools/blender/ai_ml_pipeline.py and the palette in tools/blender/nn_style.py.
Subject: data flowing from sources to a warehouse to a notebook and a chart.
No brains, glowing spheres, particles or gradients. Every part a separately named object.
Output to docs/3d/data-science-pipeline/ (.blend, .glb, transparent preview.png).
Budget: compressed GLB ≤ 300 KB. Add a manifest entry with ownerApproved false.
Do not change any page yet. Show me preview.png when done.
```

### Add NN-Bot to the website

```text
Plan only. Add NN-Bot (docs/3d/nn-bot/nn-bot-v03.glb) to the site as described in
docs/workflow/04-implementation-roadmap.md phase 4. Reuse the Three.js chunk and device
gates from aiml3d.src.js and site.js. Desktop only. Clicking plays Wave and shows an HTML
bubble with "Explore programs" and "Talk to us" links. Respect quantised node scale.
List: files to change, size impact on home page JS, tests and screenshots you will produce.
```

### Lab: lazy-load Monaco first

```text
Plan only. In the lab frontend, Monaco is bundled eagerly in the lab route. Propose the
smallest change to lazy-load it with React.lazy and Suspense, keeping the plain-text
fallback. Run lint, typecheck, vitest, build and test:ui before and after. Report the
bundle size of the lab route before and after. Do not change grading or the timeline.
```

### Lab: add Motion for React

```text
Plan only. Add the "motion" package to frontend. Use LazyMotion with domAnimation and
MotionConfig reducedMotion="user" around the routed content in AppShell, keeping the skip
link and #main focus target. Animate only: route change (200 ms fade) and ResultPanel
entrance. Do not change ResultPanel text, structure or role="status". Add tests.
Report bundle size change.
```

### Lab: Rive grade badge

```text
Plan only. I have exported frontend/public/rive/grade-badge-v01.riv with state machine
"Result" and view model properties status (string) and celebrate (trigger).
Build GradeBadge per the contract in docs/workflow/02-integration-guide.md section G,
using Rive data binding (not the deprecated inputs API). Verify the current hook names
against rive.app/docs before coding. Decorative only, aria-hidden, still image for reduced
motion. Platform-fault statuses (error, expired, cancelled) must not show a failure animation.
```

### Debugging a slow 3D scene

```text
The NN-Bot page feels slow on my laptop. Do not change anything yet. Measure with a
Performance trace at 4x CPU slowdown, run gltf-transform inspect on the GLB, and tell
me in plain language the top three causes with numbers. Then propose fixes in order of
impact, smallest change first.
```

### Visual refinement with screenshots

```text
Take Playwright screenshots of the home page at 390x844 and 1440x900, with and without
reduced motion. Compare against the previous screenshots in the PR. Point out anything
that looks broken, crowded or off-brand, and anything that uses a banned visual.
Do not edit; report only.
```

## The verification checklist Claude Code must complete

Copy this into every PR description:

```text
- [ ] Read CLAUDE.md and AGENTS.md
- [ ] Tests run before change: <command> -> <result>
- [ ] Tests run after change: <command> -> <result>
- [ ] New tests added: <files>
- [ ] Screenshots 390x844 and 1440x900 attached (and reduced-motion variant)
- [ ] Lighthouse mobile: Perf/A11y/BP/SEO = __/__/__/__, LCP __ s, CLS __
- [ ] JS size change: __ KB gzip
- [ ] axe: __ serious/critical issues
- [ ] Manifest updated
- [ ] Files changed outside the task: none (or listed with reason)
- [ ] Not tested: <list>
```

## Warning signs: stop and ask

- The plan touches authentication, database migrations, RLS, grading or the grader worker for a visual task.
- The plan deletes or renames existing assets or object names.
- A new dependency over 50 KB gzip.
- "I'll refactor X while I'm here."
- Tests were skipped, weakened or marked as expected failures.
- Claude Code says a feature works but shows no command output.

## Tools Claude Code can use, and what still needs you

| Task | Claude Code alone | Needs you |
|---|---|---|
| Write Blender scripts and run Blender headless | Yes | Approve the preview image |
| Compress GLBs, bundle JS | Yes | — |
| Export from Spline or Rive editors | No (Spline's MCP server is an experimental exception; untested by us) | Click Export, save the file |
| Buy or upgrade any plan | No | Always you |
| Vercel deploy | Can run the CLI when you ask | Approve the merge and deploy |
| AWS, Supabase dashboards | Only with credentials you deliberately give; avoid | You, in the dashboard |
