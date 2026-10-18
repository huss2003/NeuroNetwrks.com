# 6. Decision matrix

Use this part when you have a specific idea and want to know which tool to use. Each situation gives the recommended tool, the exact order of actions, what you should end up with, and why.

## Quick table

| # | Situation | Recommended tool(s) | Not this |
|---|---|---|---|
| 1 | An impressive 3D hero section | HTML text hero + Blender model + Three.js below or beside it | A canvas as the main hero content |
| 2 | A custom, detailed software-architecture model | Blender (script-built) | Spline AI generation |
| 3 | Scroll-triggered animation | Website: CSS + IntersectionObserver. Lab: Motion `whileInView` | Adding React or GSAP to the website just for this |
| 4 | A button that changes with student progress | Lab: CSS or Motion; Rive if it has several illustrated states | 3D |
| 5 | Student rotates and explores a 3D database architecture | Blender + React Three Fiber (lab, Guided Simulation) | Spline embed in the lab |
| 6 | Code editor and terminal interface | The existing Monaco editor + Pyodide + server grader | Any 3D or animation tool |
| 7 | Animation when the practical exam is passed | Rive (or Motion) wired to the real exam result | Building it before the exam exists |
| 8 | A slow 3D scene on student laptops | gltf-transform + device gates + `frameloop="demand"` | Buying a bigger plan |
| 9 | Change a visual component across the whole app | Design tokens in CSS + Claude Code in one PR | Editing each page by hand |
| 10 | Animation responding to live grading results | Rive data binding or Motion, driven by submission status | Polling extra APIs for animation |

## 1. An impressive 3D hero section

**Recommended.** HTML headline and buttons as the hero (this is the LCP element), with a Blender model loaded by Three.js after the page is visible.

**Action sequence.**

1. Write the hero text and buttons first. They must load instantly.
2. Brief and build the model in Blender (software-engineering subject, not a brain or sphere).
3. Compress with `gltf-transform meshopt`; make a WebP poster.
4. Show the poster in the hero; load Three.js by `import()` after the hero is visible and only on capable desktops.
5. Measure LCP: it must still be the text or poster.

**Expected output.** A fast hero that looks premium on every device and comes alive on desktops.

**Reason.** The website rule says the LCP element is "real HTML text or an optimised image. Never a canvas". A 3D-first hero would make the page slower and fail that rule.

## 2. A custom, detailed software-architecture model

**Recommended.** Blender, built by a Claude-written Python script, the same way as `ai_ml_pipeline.py`.

**Action sequence.**

1. Write a brief: components (API gateway, services, queue, database, cache), connections, camera angle, palette from `nn_style.py`.
2. Claude Code writes `tools/blender/<asset>.py` with one named object per component.
3. Run headless; review `preview.png`.
4. Iterate on the script until approved.
5. Export, compress, poster, manifest.

**Expected output.** A precise, rebuildable model whose parts code can animate individually.

**Reason.** Engineering diagrams need exact structure and labels. AI 3D generators produce one fused mesh from a prompt and cannot guarantee correct structure (Spline's AI generation works from text or a single image: [docs](https://docs.spline.design/generate/ai-3d-generation.md)).

## 3. Scroll-triggered animation

**Recommended.** Website: CSS transitions triggered by an `IntersectionObserver` class toggle (the site already uses vanilla JS). Lab: Motion `whileInView` with `viewport={{ once: true }}`.

**Action sequence.**

1. Decide which single element animates (website rule: one signature scroll-drawn line; everything else quiet; no fade-and-slide-up on every section).
2. Website: add a class when the element enters the viewport; CSS animates it inside `@media (prefers-reduced-motion: no-preference)`.
3. Lab: wrap in `m.div` with `whileInView`.
4. Test with reduced motion.

**Expected output.** One meaningful scroll moment, not a page full of effects.

**Reason.** Adding React or a large animation library to a static site costs JavaScript budget (≤ 100 KB home page) for an effect CSS can do.

## 4. A button that changes with student progress

**Recommended.** Lab only. CSS or Motion for colour, fill and width changes. Rive only if the button has illustrated states (for example a mascot that grows).

**Action sequence.**

1. Define states from real data (for example, lessons completed out of total from the progress API).
2. Style each state in CSS using Cortex tokens.
3. If movement is needed, Motion animates width or a progress bar with `transform: scaleX`.
4. Text always says the progress ("3 of 8 sections done").

**Expected output.** A button whose look and label match progress, readable without animation.

**Reason.** Simple state changes do not need a design tool. Rive adds a file, a runtime and a paid plan to remove the splash screen.

## 5. Student rotates and explores a 3D database architecture

**Recommended.** Blender model + React Three Fiber in the lab, as part of a future Guided Simulation.

**Action sequence.**

1. Owner approves a Guided Simulation spec (it is missing today; the lab rule says never expand scope without approval).
2. Build the model in Blender with named parts (tables, indexes, replicas).
3. Compress; place in `frontend/public/models/`.
4. Claude Code builds `ArchitectureExplorer` with `useGLTF`, `OrbitControls`, `frameloop="demand"`, loaded with `React.lazy`.
5. Every 3D fact also appears as text next to the canvas (keyboard and screen-reader users).
6. Wire the highlighted part to the lesson step from `timeline.ts`.

**Expected output.** An optional, rotatable model that helps understanding and never blocks the lesson.

**Reason.** This is genuinely educational 3D tied to app state, which is what React Three Fiber is for. A Spline embed cannot easily follow lesson state from our code.

## 6. Code editor and terminal interface

**Recommended.** The existing stack: `@monaco-editor/react` 4.7 (with its plain-text fallback), Pyodide in a web worker for practice runs, and the server-side grader. **No 3D tool and no animation tool.**

**Action sequence.**

1. Lazy-load Monaco (currently bundled eagerly in the lab route).
2. Verify Monaco and Pyodide CDN loading in the live app, including the fallback.
3. Keep the terminal output as text; never render student output as HTML (lab rule).
4. Test keyboard use inside and out of the editor.

**Expected output.** A fast, reliable editor and output panel.

**Reason.** The editor is the product. Decoration here only adds risk.

## 7. Animation when the practical exam is passed

**Recommended.** Rive grade badge (or Motion if a simple effect is enough), triggered by the real, server-confirmed exam result.

**Action sequence.**

1. Wait: the real Practical Exam does not exist yet (only an `exit_check` multiple-choice section). It needs owner approval and its own spec.
2. When it exists, add an exam result status to the component contract.
3. Add a `status = "exam_passed"` state to the Rive file.
4. Trigger it only after the server confirms the pass.
5. Show the text result first; the animation is a bonus.

**Expected output.** A short, dignified celebration that cannot fire on a client-side guess.

**Reason.** Scores and completion are server-authoritative (lab rule). Animation must follow the server, never lead it.

## 8. A slow 3D scene on student laptops

**Recommended.** Optimise the asset and the runtime before anything else.

**Action sequence.**

1. Measure: Chrome Performance panel with 4× CPU slowdown; note frame rate and long tasks.
2. `gltf-transform inspect`; reduce triangles (`simplify` or Blender Decimate); resize textures to 1024; `meshopt`.
3. Cap DPR at 1.75 (or `dpr={[1, 1.5]}` in R3F); use `frameloop="demand"`.
4. Pause when off-screen or tab hidden.
5. Fewer lights; no real-time shadows; use the environment map.
6. Gate by device (cores, memory, Save-Data, reduced motion), with a poster fallback.
7. Re-measure.

**Expected output.** Smooth interaction on a 4-core laptop, or a poster where that is not possible.

**Reason.** Most 3D slowness comes from too many pixels, too much geometry or an always-running loop. Paid plans do not fix any of these.

## 9. Change a visual component across the whole app

**Recommended.** Change the design token, then let Claude Code update every use in one reviewed pull request.

**Action sequence.**

1. Website: tokens in `tools/preview-gen/site.css`. Lab: tokens in `frontend/src/styles.css` (after the DESIGN_SYSTEM.md conflict is resolved).
2. Ask Claude Code, in plan mode, to list every place the component or token is used.
3. Change the token or the single shared component.
4. Screenshots of every affected page before and after.
5. Contrast re-checked.

**Expected output.** One consistent change everywhere, visible in one PR.

**Reason.** Tokens exist so a change happens once. Editing pages one by one creates drift.

## 10. Animation responding to live grading results

**Recommended.** Rive data binding (illustrated feedback) or Motion (panel and badge motion), driven by the submission status the lab already receives.

**Action sequence.**

1. Map statuses: `queued`/`running` → waiting; `passed` → success; `failed` → try again; `runtime_error`/`timeout` → check your code; `error`/`expired`/`cancelled` → platform problem (show help text, no "you failed" animation).
2. Map timeline phases: `awaiting_grading` → waiting; `showing_remediation` → try again; `completed` → lesson done.
3. Feed the status into `GradeBadge` (Part 2, section E).
4. No extra network requests for animation.
5. Text in `ResultPanel` stays the source of truth.

**Expected output.** Feedback that feels alive and is always accurate.

**Reason.** The data already exists in the app. Platform faults must not look like the student's mistake.
