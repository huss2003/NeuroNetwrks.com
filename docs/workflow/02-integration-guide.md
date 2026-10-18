# 2. Integration guide

This part explains how work moves between tools. No two of these tools connect automatically. Every connection below needs at least one manual export, a file saved in the right folder, and code that Claude Code writes and tests. Each connection is described with the same ten points so you can compare them.

## How to read each connection

| # | Point | What it answers |
|---|---|---|
| 1 | Tool used first | Where the work starts |
| 2 | What to create | The thing you make in that tool |
| 3 | Export or integration method | How it leaves the first tool |
| 4 | Exact format or mechanism | The file type or package |
| 5 | How it is imported next | How the next tool or the code picks it up |
| 6 | Configuration | Settings that matter |
| 7 | How to verify | How you know it worked |
| 8 | What can break | Common failures |
| 9 | Fixes | What to do when it breaks |
| 10 | Maintainability | How to keep it working next year |

## A. Claude Code → Spline

**In plain language.** There are two different things people mean by "Claude and Spline". First, Spline has its own AI features inside its editor. Second, Claude Code can write the website or lab code that shows a Spline scene you already made. There is now also a third, newer route: Spline's desktop app includes an MCP server that lets Claude Code operate the Spline editor directly (verified on [Spline's MCP server page](https://docs.spline.design/generate/spline-mcp-server.md), 15 October 2026). We have not tested that route ourselves. Treat it as optional and experimental for this project.

### What exists, verified

- **Spline AI inside the editor.** AI 3D Generation turns text or a 2D image into a 3D model, using monthly AI credits that come with paid plans ([AI 3D generation](https://docs.spline.design/generate/ai-3d-generation.md)). The AI Agent "builds and edits 3D scenes through the editor's own commands", and its edits appear in normal undo history ([AI agent](https://docs.spline.design/spline-ai/ai-agent.md)). Credits per month: Hobby 2,000, Pro 3,000, Max 10,000 ([pricing](https://spline.design/pricing)).
- **Spline MCP server.** Runs inside the Spline desktop app on macOS or Windows, on `127.0.0.1`, with no tokens. It "connects AI coding tools like Claude, Cursor, Codex, and Antigravity directly to your Spline editor." It can inspect objects, run scene edits, set the camera and capture screenshots. It registers itself for Claude Code in `~/.claude.json`. The desktop app must stay open; calls time out after about 60 seconds; only one editor connection is active at a time. The page does not state a plan requirement (**unverified** whether the free plan works).
- **Code that shows an existing scene.** Claude Code writes the `<spline-viewer>` embed or the `@splinetool/react-spline` component. This is ordinary code work and needs no Spline AI.

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Spline (you design) or Claude Code via the Spline MCP server (experimental) |
| 2. What to create | A Spline scene with named objects, states and events |
| 3. Export or integration method | You click Export in Spline: Viewer, Code (Vanilla JS or React), or download `.splinecode` |
| 4. Exact format or mechanism | `<spline-viewer>` web component; `@splinetool/runtime`; `@splinetool/react-spline`; `.splinecode` file |
| 5. How it is imported next | Claude Code adds the embed or component to a page and lazy-loads it |
| 6. Configuration | Lazy loading on; logo setting per plan; "Performance" geometry compression; scene URL or self-hosted file path |
| 7. How to verify | Playwright screenshot; network panel shows scene loads only when visible; Lighthouse score unchanged |
| 8. What can break | CORS errors from the hosted scene; runtime and React package version mismatch; Spline watermark on Free; scene too heavy on mobile |
| 9. Fixes | Self-host the `.splinecode` file ([react-spline README](https://github.com/splinetool/react-spline)); install both packages at matching versions; upgrade plan only if the watermark matters; show a poster on mobile |
| 10. Maintainability | Keep the `.spline` file name and version in the asset manifest; note which Spline account owns it; re-export after every edit and re-test |

> Rule for Claude Code: if you use the Spline MCP server, never let it overwrite a scene without a saved duplicate first. Its edits are real editor edits.

## B. Blender → Spline

**In plain language.** You can build a model in Blender and then open it in Spline to arrange it, light it and add hover or click reactions without code. Do this only when you want to design the interaction yourself. If the model only needs to sit on the website and turn, skip Spline and load it with Three.js, which we already do.

### When to import into Spline versus load directly on the web

| Situation | Choose |
|---|---|
| Model shown on the website with simple motion we code (AI/ML card, NN-Bot) | Blender → Three.js directly |
| You want to try layouts, lights and hover states yourself, visually | Blender → Spline |
| Model must react to lab data (grading, progress) | Blender → React Three Fiber in the lab |
| A quick concept to show someone before building it properly | Blender → Spline, then rebuild in Three.js if approved |

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Blender |
| 2. What to create | A clean model with applied transforms, named objects, Principled BSDF materials, and optionally skeletal animation |
| 3. Export or integration method | File > Export > glTF 2.0 in Blender, then drag the file into Spline or use Spline's Import (Ctrl+O / Cmd+O) |
| 4. Exact format or mechanism | GLB or GLTF (also FBX, OBJ, STL) — verified on [Spline import docs](https://docs.spline.design/importing-content/how-to-import-content.md) |
| 5. How it is imported next | In Spline the object appears in the scene; animations appear in the right sidebar ([animated objects](https://docs.spline.design/importing-content/import-animated-objects.md)) |
| 6. Configuration | Export one animation per file if you need several in Spline (the docs say export each as a separate file and add with "+"); keep textures small; triangulate dense meshes |
| 7. How to verify | Model looks the same as Blender's preview; animations play in Spline; Spline Performance Panel shows an acceptable export size |
| 8. What can break | Materials look different (Spline uses its own material layers); shape-key (morph) animation support is not documented on that page (**unverified**); huge files from un-decimated meshes |
| 9. Fixes | Rebuild the look in Spline's materials; bake complex shading to a texture in Blender; use Decimate or remodel before export |
| 10. Maintainability | The `.blend` stays the master. Spline is a downstream copy. Record both in the manifest with matching version suffixes (`-v03`). |

### Geometry and texture optimisation before Spline

- Remove hidden faces and unused objects. Apply modifiers.
- Keep textures at 1024 or 2048 pixels, not 4096, unless you can see the difference.
- Spline's own advice: fewer than 3 lights, 1 to 2 subdivision levels, geometry compression set to "Performance" ([Spline optimisation](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md)).

### Spline → back out to glTF: what is lost

Spline can export GLB, but only basic geometry, the colour layer of materials, and position, rotation and scale animation survive. States, events, interactivity, lighting and post-processing are not exported ([glTF export](https://docs.spline.design/exporting-your-scene/files/exporting-as-gtlf-glb.md)). So Spline is not a good middle step if the final destination is Three.js.

## C. Blender → Three.js / React Three Fiber

**In plain language.** This is the route we already use on the website. Blender makes the model, a free command shrinks it, and Three.js draws it. The lab can use the same files later through React Three Fiber.

### The pipeline we run today (website)

1. `python tools/blender/ai_ml_pipeline.py --out docs/3d/ai-ml-training-pipeline` builds the model with the Blender Python module (`bpy==5.1.2`) and writes `.blend`, `.glb` and a transparent Cycles `preview.png`.
2. `npx @gltf-transform/cli meshopt docs/3d/ai-ml-training-pipeline/ai-ml-training-pipeline.glb tools/preview-gen/assets/ai-ml-training-pipeline.glb` compresses the geometry (1.06 MB → 293 KB in our case).
3. `tools/preview-gen/aiml3d.src.js` loads it with `GLTFLoader` + `MeshoptDecoder`, lights it with `RoomEnvironment`, uses `NeutralToneMapping`, caps the device pixel ratio at 1.75 and pauses when off-screen. esbuild bundles it to `assets/aiml3d.js` (about 166 KB gzip).
4. `site.js` loads that bundle with `import()` only when the card nears the viewport on capable desktops. It is skipped for reduced motion, Save-Data, 4 or fewer CPU cores, 4 GB or less memory, screens narrower than 760 px, and no WebGL. Those visitors see a WebP poster.

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Blender (by hand or by Claude-written Python script) |
| 2. What to create | Model with stable object names, applied transforms, Principled BSDF materials, stashed actions for each animation |
| 3. Export or integration method | glTF 2.0 exporter, then `gltf-transform` compression |
| 4. Exact format or mechanism | `.glb` with `EXT_meshopt_compression` (or Draco) |
| 5. How it is imported next | `GLTFLoader` + `setMeshoptDecoder` (website); `useGLTF` from drei (lab) |
| 6. Configuration | Blender export: glTF Binary, Y Up, Apply Modifiers, Images WebP or JPEG, animation mode Actions or NLA Tracks. Runtime: DPR cap, environment light, tone mapping, pause off-screen |
| 7. How to verify | `npx @gltf-transform/cli inspect file.glb`; Playwright screenshot with SwiftShader; compare against `preview.png`; check frame rate and JS size |
| 8. What can break | Only one animation exported; meshopt file loads blank (decoder missing); parts jump in size when animated (quantisation scale); colours too dark or washed out |
| 9. Fixes | Stash every action in the NLA editor before export; call `setMeshoptDecoder(MeshoptDecoder)`; multiply by the stored original scale; use `RoomEnvironment` and the agreed tone mapping |
| 10. Maintainability | Script-built assets can be rebuilt from scratch. Keep scripts, `.blend` and manifest together. Pin the `bpy` version in the script header. |

### Blender export settings (verified option names, Blender 5.1)

Option names below are taken from the [Blender 5.1 glTF manual page](https://docs.blender.org/manual/en/5.1/addons/import_export/scene_gltf2.html).

| Section | Setting | Our choice | Why |
|---|---|---|---|
| Format | glTF Binary (.glb) | Yes | One file, easy to host |
| Include | Selected Objects / Visible Objects | Selected | Avoids exporting helper objects |
| Transform | Y Up | On | Three.js expects Y up |
| Data - Mesh | Apply Modifiers | On | Bakes bevels and arrays into geometry |
| Material | Images | WebP or JPEG | Smaller than PNG |
| Data - Compression | Draco | Off | We compress with meshopt later instead |
| Animation | Mode | Actions (NN-Bot) | Exports each stashed action as a clip |
| Animation | Export Deformation Bones only | On | Drops control bones, smaller file |
| Animation | Sampling | On | Converts constraints to plain keyframes |

> The Blender manual warns: "If you have multiple actions you want to export, make sure they are stashed!" This is the most common reason NN-Bot would arrive with only one animation.

### Compression choices

| Command | Use | Runtime needs |
|---|---|---|
| `gltf-transform meshopt in.glb out.glb` | Our default. Compresses geometry and animation. | `MeshoptDecoder` (Three.js) |
| `gltf-transform draco in.glb out.glb` | Alternative for geometry-heavy static models | `DRACOLoader` and decoder files |
| `gltf-transform webp in.glb out.glb` | Converts textures to WebP | Browser WebP support (all modern browsers) |
| `gltf-transform resize --width 1024 --height 1024` | Shrinks textures | none |
| `gltf-transform optimize in.glb out.glb` | All-in-one; the docs warn defaults "may not be ideal for all scenes" | depends on options |

Commands verified on the [glTF Transform CLI page](https://gltf-transform.dev/cli).

### Website example: the quantised-scale rule

When meshopt quantises a model, each node can carry a scale. If code sets `scale.y = 1.2` directly, the part jumps to the wrong size. Store the original and multiply:

```js
// Save the scale each node had when it loaded
const baseY = bars.map((bar) => bar.scale.y);

function animate(t) {
  bars.forEach((bar, i) => {
    // Pulse between 86% and 100% of the ORIGINAL scale, never an absolute value
    bar.scale.y = baseY[i] * (0.86 + 0.14 * (0.5 + 0.5 * Math.sin(t / 1400 + i)));
  });
}
```

### Website example: NN-Bot animations

```js
import { AnimationMixer, LoopOnce } from 'three';

const mixer = new AnimationMixer(gltf.scene);
const clip = (name) => gltf.animations.find((a) => a.name === name);
const walk = mixer.clipAction(clip('Walk'));
const wave = mixer.clipAction(clip('Wave'));
wave.setLoop(LoopOnce, 1);
wave.clampWhenFinished = true;

walk.play();
function onBotClick() {
  walk.crossFadeTo(wave.reset().play(), 0.25, false); // blend from walk to wave
  showBubble(); // HTML bubble with "Explore programs" and "Talk to us" links
}
```

Plain language: the mixer plays named animations from the GLB. Clicking blends from walking to waving and shows an ordinary HTML speech bubble, so the links are real, keyboard-reachable links.

### Lab example: a React Three Fiber model connected to app state

This is for a future Guided Simulation, not something to build now.

```tsx
import { Canvas } from '@react-three/fiber';
import { useGLTF, OrbitControls } from '@react-three/drei';

function DbArchitecture({ highlight }: { highlight: string | null }) {
  const { nodes } = useGLTF('/models/db-architecture-v01.glb'); // meshopt decoded by default
  return (
    <group>
      {Object.entries(nodes).map(([name, node]) =>
        'geometry' in node ? (
          <mesh key={name} geometry={node.geometry}>
            <meshStandardMaterial color={name === highlight ? '#ffb020' : '#2f54ff'} />
          </mesh>
        ) : null,
      )}
    </group>
  );
}

export function ArchitectureExplorer({ highlight }: { highlight: string | null }) {
  return (
    <Canvas dpr={[1, 1.75]} frameloop="demand" aria-hidden="true">
      <ambientLight intensity={0.6} />
      <DbArchitecture highlight={highlight} />
      <OrbitControls enablePan={false} />
    </Canvas>
  );
}
```

Plain language: the model loads from a file; the part the lesson is talking about turns amber (the lab's "you are here" colour, pulse amber `#ffb020`); students can rotate it. `frameloop="demand"` means it only redraws when something changes. The canvas is hidden from screen readers, so the lesson must also describe the same thing in text. `useGLTF` signature and meshopt default verified on [drei docs](https://drei.docs.pmnd.rs/loaders/gltf-use-gltf). Lab colours come from `frontend/src/styles.css`; read them from CSS variables in real code rather than hard-coding.

`gltfjsx` can turn a GLB into a typed React component: `npx gltfjsx public/models/db-architecture-v01.glb --types --keepnames` ([gltfjsx](https://github.com/pmndrs/gltfjsx)). Its `--transform` flag writes a separate compressed copy and does not alter the original.

## D. Spline → React

**In plain language.** If you design a scene in Spline, the lab (which is React) can show it with Spline's React component. The website is not React, so there you would use the `<spline-viewer>` tag instead.

### Current options, verified

| Option | Package or tag | Animations and events? | Notes |
|---|---|---|---|
| React component | `@splinetool/react-spline` + `@splinetool/runtime` | Yes | Props: `scene`, `onLoad`, `renderOnDemand` (default true), event props such as `onSplineMouseDown` ([README](https://github.com/splinetool/react-spline)) |
| Vanilla runtime | `@splinetool/runtime` | Yes | For non-React pages |
| Viewer web component | `<spline-viewer>` | Yes, in the scene | Lazy-loads by default; optional spinner and hint ([viewer docs](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer.md)) |
| Code export to Three.js or react-three-fiber | `@splinetool/loader`, `r3f-spline` | No: "Animations and events are only enabled when exporting to Vanilla js and React" ([export as code](https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md)) | |
| Self-hosted ZIP | Bundled project | Yes | Enterprise plan ([self-hosted](https://docs.spline.design/exporting-your-scene/web/exporting-as-self-hosted-project.md)) |
| Public URL or iframe | Hosted by Spline | Yes | No page documents iframe specifically; treat as **unverified** |

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Spline |
| 2. What to create | A scene with named objects and events you plan to trigger from code |
| 3. Export or integration method | Export > Code > React; copy scene URL or download `.splinecode` |
| 4. Exact format or mechanism | `.splinecode` file loaded by `@splinetool/react-spline` |
| 5. How it is imported next | `React.lazy(() => import('@splinetool/react-spline'))` inside `Suspense` |
| 6. Configuration | Container with fixed aspect ratio; `renderOnDemand`; self-hosted file path; poster fallback |
| 7. How to verify | Bundle analyser shows Spline in its own chunk; scene appears after poster; no layout shift |
| 8. What can break | CORS errors; heavy runtime added to the main bundle; scene steals scroll or touch on mobile; watermark on Free |
| 9. Fixes | Self-host `.splinecode`; lazy-load; set events to Local in Spline; plan upgrade only if justified |
| 10. Maintainability | Pin both package versions together; store scene version in manifest; re-test after each Spline re-export |

### Example (lab, lazy and optional)

```tsx
import { lazy, Suspense, useState } from 'react';
const Spline = lazy(() => import('@splinetool/react-spline'));

export function SplineFigure({ poster, alt }: { poster: string; alt: string }) {
  const [failed, setFailed] = useState(false);
  if (failed || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    return <img src={poster} alt={alt} width={800} height={600} />;
  }
  return (
    <div style={{ aspectRatio: '4 / 3' }}>
      <Suspense fallback={<img src={poster} alt={alt} width={800} height={600} />}>
        <Spline scene="/scenes/hero-v01.splinecode" onLoad={(app) => app.findObjectByName('Server')} />
      </Suspense>
    </div>
  );
}
```

Plain language: the poster shows first; the 3D only downloads when this component renders; reduced-motion users keep the poster. In real code, also wrap it in the lab's `ErrorBoundary` and call `setFailed(true)` from there.

## E. Rive → React

**In plain language.** Rive animations are small files that can change state when the app tells them to. For the lab, that means a badge that celebrates when the grader says "passed", or nudges gently when it says "failed". The grader decides the result. Rive only shows it.

### What is current, verified

- React packages: `@rive-app/react-webgl2`, `@rive-app/react-canvas`, `@rive-app/react-canvas-lite` ([renderer choice](https://rive.app/docs/runtimes/choose-a-renderer/overview.md)). For a few small badges, `react-canvas-lite` or `react-canvas` keeps size down; `react-webgl2` is needed for Rive Renderer-only features such as vector feathering.
- **Use data binding, not inputs.** Rive's React inputs page is marked "DEPRECATED: Use Data Binding instead of Inputs for controlling Rive animations" ([inputs](https://rive.app/docs/runtimes/react/inputs.md)). New work uses `useViewModel`, `useViewModelInstance` and `useViewModelInstanceBoolean / Number / String / Trigger` ([data binding](https://rive.app/docs/runtimes/react/data-binding)).
- Free editor exports carry a Rive splash screen; Cadet removes it ([pricing](https://rive.app/pricing)).

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Rive editor |
| 2. What to create | An artboard, a state machine named e.g. `Result`, and a view model with properties such as `status` (string), `score` (number), `celebrate` (trigger) |
| 3. Export or integration method | Export > `.riv` from the Rive editor (manual) |
| 4. Exact format or mechanism | `.riv` file + `@rive-app/react-*` runtime |
| 5. How it is imported next | `useRive({ src, stateMachine, autoBind: true })` and view-model hooks |
| 6. Configuration | Container width and height; `stateMachine` name exactly as in the editor; property names exactly as in the contract |
| 7. How to verify | Vitest unit test that the component sets the right property for each submission status; Playwright screenshot of pass and fail |
| 8. What can break | Name mismatch (silent: nothing animates); zero-height canvas; splash screen on Free exports; animation shown before the text result |
| 9. Fixes | Keep a written contract of names; give the container a size; buy Cadet only when shipping to students; render text first, animation second |
| 10. Maintainability | Version `.riv` files (`grade-badge-v02.riv`); keep the Rive project backed up; a contract file lists every property name |

### Example: wire grading results to a Rive badge

Real lab facts used here: submissions have a `status` of `queued`, `running`, `passed`, `failed`, `runtime_error`, `timeout`, `error`, `expired` or `cancelled` (`frontend/src/services/types.ts`), and `ResultPanel` shows them inside `role="status"`.

```tsx
import { useRive, useViewModel, useViewModelInstance,
  useViewModelInstanceString, useViewModelInstanceTrigger } from '@rive-app/react-canvas';
import { useEffect } from 'react';
import type { Submission } from '../../services/types';

export function GradeBadge({ status }: { status: Submission['status'] }) {
  const { rive, RiveComponent } = useRive({
    src: '/rive/grade-badge-v01.riv', stateMachine: 'Result', autoplay: true, autoBind: false,
  });
  const vm = useViewModel(rive);
  const vmi = useViewModelInstance(vm, { rive });
  const { setValue: setStatus } = useViewModelInstanceString('status', vmi);
  const { trigger: celebrate } = useViewModelInstanceTrigger('celebrate', vmi);

  useEffect(() => {
    setStatus(status);                 // 'passed', 'failed', 'running', ...
    if (status === 'passed') celebrate();
  }, [status, setStatus, celebrate]);

  return <div aria-hidden="true" style={{ width: 96, height: 96 }}><RiveComponent /></div>;
}
```

Plain language: the badge is decoration (`aria-hidden`). The words "Passed" or "Not passed" stay in `ResultPanel`, so screen-reader users and reduced-motion users get the same information. Check the exact hook signatures against the Rive data-binding page before coding; the API is newer than inputs and may change.

### The four lab moments

| Moment | Real trigger in the code | Rive property | Rule |
|---|---|---|---|
| Exercise completed | `EXERCISE_PASSED` event in `timeline.ts` | `celebrate` trigger | Short (under 1 second), no sound |
| Failed test | `GRADING_FINISHED` with `passed: false` → phase `showing_remediation` | `status = "failed"` | Calm, encouraging; never red flashing |
| Practical exam passed | Does not exist yet (Practical Exam is missing) | `status = "exam_passed"` | Build only after the exam feature exists and is approved |
| Onboarding | First lab visit (needs an owner-approved flag) | `step` number | Skippable; never blocks the editor |

## F. Motion for React

**In plain language.** Motion makes React elements move smoothly: a result panel sliding in, a list reordering, one page fading into the next. It is free. It is only for the lab, because the website does not use React.

### Verified basics

- Install `npm install motion`; import from `"motion/react"`; React 18.2 or newer ([installation](https://motion.dev/docs/react-installation)). The lab uses React 19.0.0, so it qualifies.
- `whileInView` with `viewport={{ once: true }}`, `useScroll({ target, offset })`, `useTransform` ([scroll animations](https://motion.dev/docs/react-scroll-animations)).
- `AnimatePresence` with a unique `key` per child; `mode="wait"` ([AnimatePresence](https://motion.dev/docs/react-animate-presence)).
- `<MotionConfig reducedMotion="user">` turns off transform and layout animations for users who ask for reduced motion; opacity still animates ([accessibility](https://motion.dev/docs/react-accessibility)).
- `LazyMotion` + `m` keeps the first load near 4.6 KB plus 15 KB for `domAnimation` ([bundle size](https://motion.dev/docs/react-reduce-bundle-size)).

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Claude Code (Motion is code, not a design app) |
| 2. What to create | A small set of shared motion presets (durations, easings) and wrapped components |
| 3. Export or integration method | npm dependency in `frontend/package.json` |
| 4. Exact format or mechanism | `motion` package, `motion/react` import |
| 5. How it is imported next | `LazyMotion` at the app root, `m.div` in components |
| 6. Configuration | `MotionConfig reducedMotion="user"`; durations 150–300 ms; no animation on result text itself |
| 7. How to verify | Vitest still passes; Playwright with `reducedMotion: 'reduce'`; bundle size diff in the PR |
| 8. What can break | Clashing with the global CSS rule that sets `animation: none !important; transition: none !important` under reduced motion (Motion animates with JS, so the CSS rule does not stop it); focus lost on exit; layout shift |
| 9. Fixes | Always wrap in `MotionConfig reducedMotion="user"`; move focus deliberately after route changes (the lab already has `RouteA11y`); animate `opacity` and `transform` only |
| 10. Maintainability | One `motion-presets.ts` file; no ad-hoc durations; Motion confined to presentation components |

### Example: route transition and result panel

```tsx
import { LazyMotion, domAnimation, m, AnimatePresence, MotionConfig } from 'motion/react';
import { useLocation, Outlet } from 'react-router-dom';

export function AnimatedRoutes() {
  const location = useLocation();
  return (
    <MotionConfig reducedMotion="user">
      <LazyMotion features={domAnimation}>
        <AnimatePresence mode="wait">
          <m.div key={location.pathname}
            initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}>
            <Outlet />
          </m.div>
        </AnimatePresence>
      </LazyMotion>
    </MotionConfig>
  );
}
```

Plain language: each page fades in and moves up 8 pixels in 0.2 seconds. People who turned on "reduce motion" get a plain fade. In the lab, `AppShell.tsx` already renders `<Outlet />` inside `<div id="main" tabIndex={-1}>` with a skip link; this wrapper would replace only that `<Outlet />`, keeping the skip link and focus target exactly as they are.

### Combining Motion, Rive and React Three Fiber without conflicts

| Rule | Why |
|---|---|
| Each element is animated by exactly one system | Two systems fighting over one `transform` causes jitter |
| Motion animates the box; Rive or R3F draws inside it | Motion can fade a card in; the Rive badge inside plays its own state machine |
| Never animate the size of a `<canvas>` with Motion layout animations | Canvas resizes trigger re-renders and blurry frames; fade or move it instead |
| R3F uses `frameloop="demand"`; Rive pauses when hidden | Keeps the editor and Monaco responsive (INP) |
| Grading, editor and terminal never wait for any animation | The student's work is the priority |

## G. Claude Code → all tools

**In plain language.** Claude Code is the glue. It writes the brief for each asset, keeps the list of assets up to date, writes and tests the code, and takes screenshots so you can see the result without reading code.

### The ten points

| Point | Answer |
|---|---|
| 1. Tool used first | Claude Code, in plan mode |
| 2. What to create | An asset brief, a manifest entry, a component contract, then code and tests |
| 3. Export or integration method | Git branch, pull request, Vercel preview |
| 4. Exact format or mechanism | Markdown brief, JSON manifest, TypeScript or JS code, Playwright screenshots |
| 5. How it is imported next | You review the preview and screenshots; merge only when happy |
| 6. Configuration | Each repo's CLAUDE.md and AGENTS.md; plan mode (`claude --permission-mode plan` or Shift+Tab, [docs](https://code.claude.com/docs/en/common-workflows)) |
| 7. How to verify | Tests before and after; Lighthouse; axe; screenshots at 390×844 and 1440×900 |
| 8. What can break | Scope creep; unrelated files changed; new dependencies without justification; visual work touching grading or auth |
| 9. Fixes | Small branches; ask for a diff summary; reject PRs that touch unrelated files; revert |
| 10. Maintainability | Every change leaves the manifest, tests and docs updated in the same PR |

### Five documents Claude Code produces for every visual feature

1. **Asset brief**: purpose, page, size budget, states, banned visuals, poster requirement.
2. **Manifest entry**: see Part 3.
3. **Component contract**: props in, events out, loading and error states, reduced-motion behaviour, what text replaces the visual for screen readers.
4. **Implementation task**: files to touch, files not to touch, tests to add.
5. **Verification report**: commands run, results, screenshots, what was not run.

### Example component contract (Rive grade badge)

```text
Component: GradeBadge
Lives in: frontend/src/features/lab/GradeBadge.tsx
Props: status: Submission['status']
Rive file: public/rive/grade-badge-v01.riv, state machine "Result"
View model properties: status (string), celebrate (trigger)
Decorative only: aria-hidden="true"; ResultPanel text unchanged
Reduced motion: render a static icon instead of the Rive canvas
Failure: if the .riv fails to load, render nothing (no error to the student)
Must not: delay ResultPanel, change grading, add network calls
Tests: one Vitest case per status; Playwright screenshot passed and failed
```
