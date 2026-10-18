# 4. Step-by-step implementation roadmap

This part lists nine phases, from checking what exists to releasing to production. Each phase says what must be true before it starts, the tasks, what it delivers, and how you know it is finished. Some phases are already partly done on the website; they are marked so you do not redo them.

## Overview

| Phase | Name | Website status today | Lab status today |
|---|---|---|---|
| 0 | Audit and preparation | Done (this manual is based on it) | Done; open owner decisions listed |
| 1 | Visual identity | Mostly done (brand blue `#006DEE`, ink `#0B1B33`) | Cortex tokens exist; conflict with DESIGN_SYSTEM.md |
| 2 | Signature 3D asset | AI/ML card live; NN-Bot and 11 models in progress | Not started (not needed yet) |
| 3 | Motion system | CSS motion and scroll-drawn line rule | Not started |
| 4 | Website implementation | In progress | — |
| 5 | Student lab implementation | — | Visual layer not started; Guided Simulation and Practical Exam missing |
| 6 | Integration | Partial | Not started |
| 7 | Performance and QA | Tooling exists | Tooling exists (CI) |
| 8 | Production release | Live on Vercel | Live on Vercel |

## Phase 0: audit and preparation

**Entry criteria.** Both repos cloned; CLAUDE.md and AGENTS.md read.

**Tasks.**

- Confirm what is live: website is the Python generator output in `site-preview/` on Vercel; lab is React 19 + Vite on Vercel with FastAPI, Supabase and an EC2 grader.
- List conflicts and owner decisions (see "Start here").
- Record baseline numbers: Lighthouse mobile scores, JS size per page, lab CI status.
- Create `docs/3d/asset-manifest.json` with the AI/ML asset as its first entry.

**Deliverables.** Baseline report; owner-decision list; manifest v1.

**Completion criteria.** You have answered the four owner decisions, or consciously postponed them.

**Checklist.**

- [ ] Baseline Lighthouse (mobile and desktop) saved for home and one program page
- [ ] Lab CI green on `main`
- [ ] DESIGN_SYSTEM.md versus styles.css decision made
- [ ] "NeuroMind Lab" naming decision made
- [ ] Website CLAUDE.md updated to describe the real stack (Python generator, Vercel, two approved WebGL objects)
- [ ] Vercel plan checked (Pro needed for commercial use)

## Phase 1: visual identity

**Entry criteria.** Phase 0 decisions made.

**Tasks.**

- Lock the 3D visual language: software-engineering objects (code blocks, connected modules, servers, databases, pipelines, terminals, IDE windows). Banned: floating brains, purple or blue gradients, glowing spheres, particle or neural-network backgrounds, glassmorphism blobs.
- Lock one shared material palette for Blender (`tools/blender/nn_style.py` already exists for this).
- Lab: confirm Cortex tokens (ink `#0b1020`, axon blue `#2f54ff`, pulse amber `#ffb020`, mint `#0b8a68`, coral `#c7283a`) or the DESIGN_SYSTEM.md set.
- Decide how website and lab relate visually: same company, different product. Website uses brand blue `#006DEE`; lab uses Cortex. Do not merge them without a decision.

**Deliverables.** One-page style sheet for 3D (materials, lighting, camera angle, background); approved palette.

**Completion criteria.** Two test renders approved by you.

**Checklist.**

- [ ] Palette in `nn_style.py` matches the approved colours
- [ ] Contrast checked for any text over or near 3D posters
- [ ] Banned-visuals list copied into each asset brief

## Phase 2: signature 3D asset

**Entry criteria.** Phase 1 approved.

**Tasks.**

- Finish NN-Bot in Blender: rig, five actions (Idle, Walk, Wave, Jump, LookAround) each stashed so all export.
- Finish the 11 program models using the AI/ML script as the template.
- Compress with `gltf-transform meshopt`; make WebP posters.
- Record sizes in the manifest.

**Deliverables.** `.blend`, `.glb` (raw and compressed), poster and manifest entry for each.

**Completion criteria.** Every GLB within budget; every object named; you approved each preview.

**Checklist.**

- [ ] `gltf-transform inspect` shows expected animations for NN-Bot (5 clips)
- [ ] No texture larger than 2048 px
- [ ] Each model under its size budget
- [ ] Posters under 60 KB

## Phase 3: motion system

**Entry criteria.** Phase 1 approved.

**Tasks.**

- Website: keep CSS motion and the single scroll-drawn line; define durations and easings as CSS custom properties; every animation inside `@media (prefers-reduced-motion: no-preference)`.
- Lab: add Motion for React with `LazyMotion` + `MotionConfig reducedMotion="user"`; one `motion-presets.ts`; decide which three to five moments get motion (route change, result panel, outline progress, hint reveal).
- Rive: only design a grade badge if you want one after seeing Motion in place.

**Deliverables.** Motion spec (one table: element, trigger, duration, reduced-motion behaviour).

**Completion criteria.** Spec approved; no element animated by two systems.

**Checklist.**

- [ ] Durations 150–300 ms for interface; no animation over 1 s except NN-Bot walk
- [ ] Reduced-motion behaviour written for every row
- [ ] Lab bundle size increase estimated (about 20 KB for Motion with `domAnimation`)

## Phase 4: website implementation

**Entry criteria.** Phase 2 assets approved.

**Tasks.**

- Replace generic images with the 11 models: poster everywhere, live 3D only where approved (today only the AI/ML card and NN-Bot are approved for WebGL).
- Add NN-Bot: desktop only, walks along the bottom, draggable to rotate, click to wave and show an HTML bubble with "Explore programs" and "Talk to us" links. Same device gates as the AI/ML card.
- Share one Three.js runtime chunk between the card and NN-Bot so the browser downloads Three.js once.
- Keep the LCP element as HTML text or an optimised image.

**Deliverables.** Updated generator, CSS, JS and assets; Vercel preview.

**Completion criteria.** Phase 7 checks pass on the preview.

**Checklist.**

- [ ] Home JS before interaction ≤ 100 KB gzip
- [ ] NN-Bot never covers a button, link or form field; can be dismissed
- [ ] Keyboard users can reach the bubble links; NN-Bot itself is not a keyboard trap
- [ ] Bot pauses when tab hidden and off-screen
- [ ] No prices anywhere

## Phase 5: student lab implementation

**Entry criteria.** Lab owner decisions made; Phase 3 motion spec approved; lab CI green.

**Tasks.**

- Lazy-load Monaco (it is currently bundled eagerly in the lab route). Do this before any visual work: it is the biggest speed win.
- Verify Monaco and Pyodide CDN loading in the live app (not yet exercised there).
- Add Motion for React for the agreed moments.
- Optionally add the Rive grade badge wired to submission status (Part 2, section E).
- Do not build 3D yet. React Three Fiber waits for the Guided Simulation feature, which does not exist and needs its own approved spec.

**Deliverables.** Small PRs, each with tests.

**Completion criteria.** All existing tests pass; new tests added; Playwright UI tests with axe pass.

**Checklist.**

- [ ] Monaco loads only when the editor is opened; plain-text fallback still works
- [ ] Grading flow unchanged (server-authoritative scores, hints one at a time)
- [ ] Student output never rendered as HTML
- [ ] Animations never delay `ResultPanel` text

## Phase 6: integration

**Entry criteria.** Phases 4 and 5 merged to preview branches.

**Tasks.**

- Link website to lab where approved (teaser only on the website).
- Wire lab animations to the real timeline phases (`awaiting_grading`, `showing_remediation`, `completed`) and submission statuses.
- Error and loading states for every asset: missing file, slow network, WebGL lost.

**Deliverables.** End-to-end Playwright flows covering the visual layer.

**Completion criteria.** A failed asset never breaks a page; every flow works with JavaScript animations disabled.

**Checklist.**

- [ ] Delete the GLB on a test branch: page still works with poster
- [ ] Block the `.riv` request: result still shows as text
- [ ] Simulate grader down (`npm run e2e:grader-down` exists in the lab)

## Phase 7: performance and QA

**Entry criteria.** Phase 6 complete on preview deployments.

**Tasks.** Run the full checklist in Part 7.

**Deliverables.** QA report with numbers, screenshots and anything not tested.

**Completion criteria.** Internal targets met (LCP ≤ 1.8 s, INP ≤ 150 ms, CLS ≤ 0.05) or a written, approved exception.

**Checklist.**

- [ ] Lighthouse mobile and desktop
- [ ] Low-end profile tested (4× CPU slowdown, slow 4G)
- [ ] Keyboard-only run
- [ ] Reduced-motion run
- [ ] axe clean

## Phase 8: production release

**Entry criteria.** Phase 7 report approved by you.

**Tasks.**

- Merge the PR; deploy (website through the Vercel CLI as today; lab through its CI).
- Check the live URL with the same Playwright smoke test.
- Website: ping IndexNow with the existing script for changed URLs.
- Watch Vercel analytics and error logs for 48 hours.

**Deliverables.** Release note: what changed, measured numbers, rollback steps.

**Completion criteria.** Live checks pass; no new errors for 48 hours.

**Checklist.**

- [ ] Rollback tested (Vercel "Instant Rollback" or redeploy previous build; **unverified** feature name, check the Vercel dashboard)
- [ ] Manifest marks shipped versions as `ownerApproved: true`
- [ ] Release note saved in the repo
