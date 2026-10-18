# 1. Tool master guide

This part explains what each of the six tools is for, what it must never be used for, and how its output reaches the next tool. Read the plain-language summary first. The responsibility matrix after it is the reference you and Claude Code check before starting any task.

## The six tools in one sentence each

| Tool | In plain language |
|---|---|
| Claude Max + Claude Code | Your engineer. It reads the code, writes new code, runs tests, takes screenshots and explains what it did. It does not draw. |
| Spline | A 3D design app in the browser or desktop where you can build and animate a scene by hand, then put it on a web page. Optional for us. |
| Blender | A free, professional 3D studio. It makes detailed models, materials, rigs and animations, and exports them as web-ready files. Our main 3D source. |
| Motion for React | A free code library that animates parts of a React page: panels sliding, lists reordering, pages changing. Lab only. |
| Rive | A design app plus a free player for small interactive animations driven by a "state machine", for example a badge that reacts to pass or fail. Lab only, later. |
| Three.js + React Three Fiber | Free code libraries that draw 3D in the browser. Three.js is used directly on the website. React Three Fiber is the React version for the lab. |

## Four kinds of job, and which tool owns each

It helps to sort the tools by the kind of work they do. Most mistakes come from asking a tool to do a job from a different column.

| Kind of job | What it means | Tools |
|---|---|---|
| Create visual assets | Make the thing people look at: a 3D model, its materials, its shape | Blender (main), Spline (optional, visual design) |
| Animate assets | Make an asset or interface element move or react | Rive (state-driven 2D graphics), Motion for React (React interface elements), Blender (baked 3D animation such as NN-Bot's walk), CSS (website) |
| Implement application behaviour | Decide when things load, what happens on click, how 3D connects to grading, routing or data | Three.js, React Three Fiber, React code, all written and tested by Claude Code |
| Build the production interface | The real pages and lab screens students and parents use, with accessibility, speed and tests | Python static generator + vanilla JS (website); React + Vite + TypeScript (lab). Claude Code does the work; Playwright, axe and Lighthouse check it. |

> A design tool never ships to production on its own. Something always has to export a file and write code to load it. That step is manual and must be tested.

## What is already true in our projects

- **Website** (neuronetwrks.com, repo `huss2003/NeuroNetwrks.com`): a Python generator (`tools/preview-gen/build.py`) writes static HTML into `site-preview/`, deployed on Vercel. No React. Three.js is already used for one card (AI/ML) through a lazy-loaded module (`assets/aiml3d.js`). NN-Bot and 11 Blender models are in progress.
- **Lab** (repo `huss2003/Neuromind-lab`): React 19 + Vite + TypeScript. No animation library and no 3D yet. Monaco code editor, Pyodide practice runs, server-side grader.

This is why the matrix below says "website" or "lab" for each tool. Using a React-only tool on the website would mean adding React to a site that does not need it.

## Tool responsibility matrix

Each table below is one row of the matrix, turned sideways so it can be read on A4. Costs are monthly, checked on 15 October 2026, converted at ₹95.16 per US dollar before GST. See Part 8 for the full cost breakdown and sources.

### Claude Max + Claude Code

| Field | Detail |
|---|---|
| Tool | Claude Max subscription with Claude Code (terminal, desktop app or web) |
| Primary purpose | Plan, write, test and debug all code; write briefs and asset manifests; run checks; report honestly what was run |
| Exact tasks | Read each repo's CLAUDE.md and AGENTS.md; propose a plan in plan mode; write Blender Python scripts; run `gltf-transform`; write the Three.js loader, React components, Rive and Motion wiring; write Playwright and Vitest tests; take screenshots; run Lighthouse and axe; open small pull requests |
| Must not be used for | Inventing facts, prices or features; pushing to `main` or deploying without your approval; rebuilding working features; changing grading, auth or database rules as a side effect of visual work; claiming something works without running it |
| Inputs | Your brief in plain language, the repo, asset source files, the asset manifest, screenshots |
| Outputs | Code changes on a branch, scripts, compressed exports, test results, screenshots, a written summary |
| File formats | `.py`, `.js`, `.ts`, `.tsx`, `.css`, `.json`, `.md`, `.png` screenshots |
| How output reaches next tool | Git branch and pull request; Vercel preview deployment; files in `docs/3d/` or the lab's asset folder |
| When to use | Every code task, every integration, every check |
| When not to use | To "design by eye" a scene that you want to shape yourself (use Spline or Blender by hand), or to make visual decisions that belong to you |
| Estimated cost | Already owned. Max is listed "from $100" per month ([claude.com/pricing](https://claude.com/pricing)). Excluded from new costs. |
| Common mistakes | Big, vague prompts; skipping plan mode; letting it add dependencies freely; not asking for screenshots; accepting "it should work" |
| Quality checks before proceeding | Plan approved by you; tests passed before and after; screenshots at 390×844 and 1440×900 reviewed; Lighthouse and axe run; summary lists what was not run |

### Spline (optional)

| Field | Detail |
|---|---|
| Tool | Spline, browser and desktop 3D design app ([spline.design](https://spline.design)) |
| Primary purpose | Designing and animating a 3D scene visually, by hand, when you (not code) want to control the look |
| Exact tasks | Import a Blender GLB or FBX; arrange camera, lights and materials; add states and events (hover, click); export as Viewer embed, public URL or code |
| Must not be used for | The only copy of a model (keep the Blender source); the LCP element of any page; anything in the lab's editor, terminal or grading path; heavy scenes on mobile |
| Inputs | GLB/GLTF, FBX, OBJ, STL, PNG, JPG, SVG (partial), MP4, MP3, WAV (verified: [Spline import docs](https://docs.spline.design/importing-content/how-to-import-content.md)) |
| Outputs | Hosted scene URL, `<spline-viewer>` embed, code export (Vanilla JS, Three.js, React, Next.js, react-three-fiber), GLB/GLTF, USDZ, images, video (verified: [export as code](https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md)) |
| File formats | `.spline` (editable source), `.splinecode` (runtime scene file), `.glb` |
| How output reaches next tool | Manual: you click Export in Spline, then Claude Code adds the embed or package to the page. Nothing syncs automatically. |
| When to use | Only if you want to design a 3D scene yourself, visually, and accept a paid plan to remove the watermark |
| When not to use | When Blender + Three.js already does the job (true today on the website); for detailed engineering models; on low-end devices |
| Estimated cost | Free (watermark on web exports). Hobby $12 per seat per month yearly ≈ ₹1,142; Pro $25 yearly ≈ ₹2,379; code-export download from Pro ([spline.design/pricing](https://spline.design/pricing)) |
| Common mistakes | Assuming an exported GLB keeps Spline interactions (it does not: [glTF export docs](https://docs.spline.design/exporting-your-scene/files/exporting-as-gtlf-glb.md)); loading the scene from Spline's servers on a page that must be fast; more than 3 embeds per page |
| Quality checks before proceeding | Fewer than 3 lights; compression set to "Performance"; Performance Panel size checked; poster image ready; works with reduced motion |

### Blender

| Field | Detail |
|---|---|
| Tool | Blender 5.1, free and open source ([blender.org](https://www.blender.org)); we also run it headless as a Python module (`pip install bpy==5.1.2`) |
| Primary purpose | Making detailed 3D models, materials, rigs and baked animations; the master source for all 3D |
| Exact tasks | Model the 11 program objects and NN-Bot; set Principled BSDF materials; rig and animate (Idle, Walk, Wave, Jump, LookAround); render transparent preview PNGs (Cycles); export GLB |
| Must not be used for | Interactive logic (that belongs in code); final web compression (use `gltf-transform`); 2D interface animation |
| Inputs | Your brief and references, Claude-written Python scripts in `tools/blender/` |
| Outputs | `.blend` source, `.glb` export, `preview.png` poster |
| File formats | `.blend`, `.glb` (glTF Binary), `.gltf`, `.png`, `.webp` |
| How output reaches next tool | Script writes to `docs/3d/<asset>/`; `npx @gltf-transform/cli meshopt` compresses into `tools/preview-gen/assets/`; Three.js loads it |
| When to use | Every custom 3D model, especially software-architecture objects and NN-Bot |
| When not to use | For a quick visual experiment you want to click together yourself (Spline is faster to learn), or for 2D feedback animation (Rive) |
| Estimated cost | ₹0. GPL, free for commercial use; "What you create with Blender is your sole property" ([blender.org licence](https://www.blender.org/about/license/)) |
| Common mistakes | Exporting with unapplied scale; forgetting to stash actions so only one animation exports; huge textures; materials built from nodes glTF cannot read; unnamed objects code cannot find |
| Quality checks before proceeding | Every object has a stable name; applied transforms; triangle count noted; `gltf-transform inspect` run; preview PNG looks right; `.blend` saved next to the GLB |

### Motion for React

| Field | Detail |
|---|---|
| Tool | Motion for React, npm package `motion`, imported from `"motion/react"` ([motion.dev install](https://motion.dev/docs/react-installation)) |
| Primary purpose | Animating React interface elements in the lab: entry, exit, layout changes, hover, scroll |
| Exact tasks | Page and panel transitions with `AnimatePresence`; result panel entrance; outline progress; hover and tap feedback; reduced-motion handling with `MotionConfig` |
| Must not be used for | The website (no React there; use CSS); 3D (use React Three Fiber); illustrated character animation (use Rive); delaying any result text |
| Inputs | React components, design tokens in `frontend/src/styles.css` |
| Outputs | Animated React components |
| File formats | `.tsx` |
| How output reaches next tool | Normal code in the lab repo, tested by Vitest and Playwright |
| When to use | When a lab element appears, disappears or moves and a plain CSS transition is not enough (exit animations, layout reflow) |
| When not to use | When one CSS transition does the job; on the marketing site |
| Estimated cost | ₹0. MIT licence ([GitHub](https://github.com/motiondivision/motion)). Motion+ is a separate paid tier; we do not need it. |
| Common mistakes | Importing the full `motion` component everywhere (about 34 KB) instead of `m` with `LazyMotion` (about 4.6 KB plus features) ([bundle size docs](https://motion.dev/docs/react-reduce-bundle-size)); forgetting `key` inside `AnimatePresence`; animating layout on every render |
| Quality checks before proceeding | Bundle size compared before and after; reduced-motion test passes; no layout shift (CLS); focus stays where it should |

### Rive

| Field | Detail |
|---|---|
| Tool | Rive editor ([rive.app](https://rive.app)) and its React runtime (`@rive-app/react-webgl2`, `react-canvas` or `react-canvas-lite`) |
| Primary purpose | Small interactive vector animations whose state is driven by app data: pass, fail, progress, onboarding |
| Exact tasks | Design a badge or mascot; build a state machine; expose view-model properties (data binding); export `.riv`; Claude Code wires it to real lab events |
| Must not be used for | 3D models; long video-like sequences; anything the student must see to understand a result (text stays the source of truth); the website |
| Inputs | Your sketch, the brand palette, a list of states the code will send |
| Outputs | `.riv` runtime file |
| File formats | `.rev` (editor backup, unverified file name; keep the Rive project in your Rive account plus a downloaded backup), `.riv` (runtime) |
| How output reaches next tool | Manual: export `.riv` from the Rive editor; save into the lab repo; Claude Code loads it with `useRive` |
| When to use | When a lab element must react to several states and a CSS animation would be messy |
| When not to use | For a single fade or slide (Motion or CSS); before the grading flow is stable |
| Estimated cost | Runtime free (MIT, [rive-react](https://github.com/rive-app/rive-react)). Editor Free exports `.riv` with a Rive splash screen; Cadet $9 per seat per month ≈ ₹856 removes it ([rive.app/pricing](https://rive.app/pricing)) |
| Common mistakes | Using the deprecated "inputs" API in new work ([Rive docs: "DEPRECATED: Use Data Binding instead of Inputs"](https://rive.app/docs/runtimes/react/inputs.md)); a container with no height; letting the animation decide pass or fail |
| Quality checks before proceeding | Property names match the contract; reduced-motion shows a still frame; text result still shown; file size noted |

### Three.js + React Three Fiber

| Field | Detail |
|---|---|
| Tool | Three.js (MIT, [GitHub](https://github.com/mrdoob/three.js)); React Three Fiber v9 for React 19 ([R3F install](https://r3f.docs.pmnd.rs/getting-started/installation)); drei helpers |
| Primary purpose | Drawing and controlling 3D in the browser |
| Exact tasks | Website: load GLB with `GLTFLoader` + `MeshoptDecoder`, light with `RoomEnvironment`, animate parts, play NN-Bot actions with `AnimationMixer`, pause off-screen. Lab: an optional rotatable architecture explorer with `useGLTF` and orbit controls |
| Must not be used for | Text, buttons or forms (use HTML); the LCP element; the code editor or terminal; anything that blocks grading |
| Inputs | Compressed `.glb` from Blender; app state (lab) |
| Outputs | A `<canvas>` with interactive 3D, plus a poster fallback |
| File formats | `.js`, `.tsx`, `.glb` |
| How output reaches next tool | Bundled by esbuild (website: `assets/aiml3d.js`) or Vite (lab); deployed on Vercel |
| When to use | Every time 3D must appear in the browser and we own the model |
| When not to use | Low-end devices, reduced motion, Save-Data, no WebGL: show the poster instead |
| Estimated cost | ₹0 |
| Common mistakes | Forgetting `setMeshoptDecoder` for meshopt files ([GLTFLoader docs](https://threejs.org/docs/pages/GLTFLoader.html)); animating quantised nodes without respecting their stored scale (a real bug we hit); no pause off-screen; DPR uncapped |
| Quality checks before proceeding | Loads only after intersection; poster shows first; DPR capped at 1.75; JS budget respected; frame rate checked on a 4-core laptop |
