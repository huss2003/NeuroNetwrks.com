# 5. Practical tutorials

These tutorials take you through one small, real task in each tool. They are written for a beginner. Each step is marked:

- **Verified**: checked against the tool's official documentation on 15 October 2026 (link given).
- **Suggested workflow**: our recommended way of working. The tool does not require it.
- **Unverified**: a menu name or detail we could not confirm. Look for something similar if the screen differs.

Software screens change often. If a button is not where the tutorial says, search the tool's help for the action's name.

## Tutorial 1: Blender — export a model for the web

**Goal.** Export a simple model so Three.js can show it, and keep the master file safe.

### What to open

Blender 5.1 (free from blender.org). Or, for script-built assets, nothing: Claude Code runs Blender headless.

### Steps

1. **Open or build the model.** File > Open the `.blend` file, for example `docs/3d/ai-ml-training-pipeline/ai-ml-training-pipeline.blend`. *(Suggested workflow.)*
2. **Name every part.** In the Outliner (top right), double-click each object and give it a clear name such as `Server_DB`. Code finds parts by these names. *(Suggested workflow.)*
3. **Apply transforms.** Select all (A), then Object > Apply > All Transforms. This stops parts appearing at the wrong size on the web. *(Suggested workflow; menu path is standard Blender but unverified for 5.1.)*
4. **Use Principled BSDF materials.** The glTF exporter reads Base Color, Metallic and Roughness from the Principled BSDF node. *(Verified: [Blender 5.1 glTF manual](https://docs.blender.org/manual/en/5.1/addons/import_export/scene_gltf2.html).)*
5. **Stash animations.** For a rigged model like NN-Bot, open the Action Editor and stash every action (Idle, Walk, Wave, Jump, LookAround). The manual says: "If you have multiple actions you want to export, make sure they are stashed!" *(Verified.)*
6. **Save the master.** File > Save As `nn-bot-v03.blend`. Never skip this. *(Suggested workflow.)*
7. **Export.** File > Export > glTF 2.0. Choose:
   - Format: glTF Binary (.glb)
   - Include: Selected Objects (if you selected only the model)
   - Transform: Y Up on
   - Data - Mesh: Apply Modifiers on
   - Material: Images WebP or JPEG
   - Data - Compression: off (we compress afterwards)
   - Animation: mode Actions; Export Deformation Bones only on; Sampling on

   *(Option names verified on the Blender 5.1 manual.)*
8. **Save next to the master.** `docs/3d/nn-bot/nn-bot-v03.glb`. *(Suggested workflow.)*

### Headless version (what we actually run)

```bash
pip install bpy==5.1.2
python tools/blender/ai_ml_pipeline.py --out docs/3d/ai-ml-training-pipeline --samples 128 --res 2400
```

This builds the scene from code and writes `.blend`, `.glb` and a transparent `preview.png`. Re-running it rebuilds the asset exactly, which is why script-built assets are easy to maintain.

### Compress

```bash
npx @gltf-transform/cli inspect docs/3d/nn-bot/nn-bot-v03.glb
npx @gltf-transform/cli meshopt docs/3d/nn-bot/nn-bot-v03.glb tools/preview-gen/assets/nn-bot-v03.glb
```

`inspect` lists meshes, textures and animations, so you can confirm all five NN-Bot clips are present. `meshopt` compresses. *(Commands verified: [glTF Transform CLI](https://gltf-transform.dev/cli).)*

### How to test

- Drag the compressed GLB into an online glTF viewer, or ask Claude Code to run a Playwright screenshot of the page that loads it.
- Compare with `preview.png`.

### What success looks like

The model looks the same as in Blender, all animations are listed, the compressed file is within budget (≤ 300 KB for a card, ≤ 400 KB for NN-Bot).

### Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Only one animation in the GLB | Actions not stashed | Stash each action; re-export |
| Model is black or flat | Materials not Principled BSDF, or no environment light on the web | Rebuild material; check `RoomEnvironment` in the loader |
| Model is huge or tiny | Unapplied scale | Apply All Transforms; re-export |
| File is several MB | Big textures, dense mesh | Resize textures to 1024; Decimate modifier; compress |
| Blank on the web after meshopt | Decoder not set | `loader.setMeshoptDecoder(MeshoptDecoder)` |

## Tutorial 2: Spline — design a scene and embed it (optional tool)

**Goal.** Bring a Blender model into Spline, add a hover effect, and embed it on a test page. Use this only if you want to design scenes yourself.

### What to open

spline.design in a browser, or the Spline desktop app. Sign in.

### Steps

1. **Create a new file.** *(Suggested workflow.)*
2. **Import the Blender model.** Main Menu > Open / Import, Ctrl+O (Windows) or Cmd+O (Mac), or drag the `.glb` into the viewport. *(Verified: [Spline import docs](https://docs.spline.design/importing-content/how-to-import-content.md).)*
3. **Check animations.** If the GLB has animations, they appear in the right sidebar. To trigger one on hover or click, add an animation action. *(Verified: [animated objects](https://docs.spline.design/importing-content/import-animated-objects.md).)*
4. **Keep it light.** Fewer than 3 lights; 1 to 2 subdivision levels; turn on compression with Geometry Quality "Performance". *(Verified: [optimisation](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md).)*
5. **Add a hover state.** Select an object, add a state and a Mouse Hover event. *(Suggested workflow; exact panel names unverified.)*
6. **Check the Performance Panel.** It estimates export size and load time; the docs say "Actual values may vary". *(Verified.)*
7. **Export.** Click Export, choose Viewer, wait for the "URL is ready" message, copy the embed snippet. Or choose Code > React for the lab. *(Verified: [viewer](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer.md), [code](https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md).)*
8. **Save.** The `.spline` file stays in your Spline account. Download a backup copy and record its name in the manifest. *(Suggested workflow.)*

### How to integrate

Give the embed snippet to Claude Code with this instruction: "Add this Spline Viewer to a test page only. Lazy-load it, show the poster first, skip it for reduced motion and screens under 760 px."

### How to test

Playwright screenshot; Lighthouse before and after. A Spline scene adds its own runtime download, so expect the score to move. Measure it.

### What success looks like

The scene appears after the poster, reacts to hover, and Lighthouse performance on mobile does not drop below the target.

### Troubleshooting

| Problem | Fix |
|---|---|
| Spline logo on the page | Free plan web exports carry a watermark; paid plans remove it ([pricing](https://spline.design/pricing)) |
| CORS error loading the scene | Download the `.splinecode` file and host it yourself ([react-spline README](https://github.com/splinetool/react-spline)) |
| Page scrolls badly on phones | Set events to Local, not Global, in the viewer settings; or do not show the scene on phones |
| Scene looks different from Blender | Spline uses its own material layers; rebuild the look in Spline |

## Tutorial 3: Rive — a grade badge driven by data

**Goal.** Make a small badge with three looks (idle, passed, not passed) that the lab can switch from code.

### What to open

rive.app in a browser or the Rive desktop app. Sign in. The Free plan is enough to learn; Free exports show a Rive splash screen ([pricing](https://rive.app/pricing)).

### Steps

1. **New file; new artboard** named `GradeBadge`, 96 × 96. *(Suggested workflow.)*
2. **Draw the badge** with shapes in the brand palette. No glowing effects, no gradients. *(Suggested workflow.)*
3. **Create timelines**: `idle`, `passed` (a short check-mark draw and small bounce), `failed` (a gentle shake, no red flash). *(Suggested workflow.)*
4. **Create a state machine** named `Result` with states for each timeline. *(Rive concept verified: [state machines](https://rive.app/docs/runtimes/state-machines); editor menu names unverified.)*
5. **Create a view model** named `GradeVM` with a string property `status` and a trigger `celebrate`. Bind the state machine transitions to these properties. Rive recommends data binding over the older "inputs". *(Verified: [data binding](https://rive.app/docs/runtimes/react/data-binding); inputs deprecated per [inputs page](https://rive.app/docs/runtimes/react/inputs.md).)*
6. **Export the `.riv` file** (Rive's export or download option; exact menu name unverified). Save as `grade-badge-v01.riv`.
7. **Back up the project.** Keep the Rive project in your account and download a backup. *(Suggested workflow.)*

### How to integrate

Save the file to `frontend/public/rive/` in the lab repo. Give Claude Code the component contract from Part 2, section G, and the example code in Part 2, section E.

### How to test

- Vitest: render `GradeBadge` with each status and check the right property is set (mock the Rive hooks).
- Playwright: screenshot after a passing and a failing submission against the mock build (`npm run build:mock` exists in the lab).

### What success looks like

Submitting correct code shows "Passed" text in `ResultPanel` and the badge celebrates once. Submitting wrong code shows the remediation text and the badge changes calmly. With reduced motion on, the badge is a still image.

### Troubleshooting

| Problem | Fix |
|---|---|
| Nothing animates, no error | A name does not match exactly (`Result`, `status`, `celebrate`). Compare with the contract. |
| Canvas is empty | The container has no height. Give it width and height. |
| Splash screen appears | Free plan export. Upgrade to Cadet before showing students. |

## Tutorial 4: Motion for React — animate the result panel

**Goal.** Make the lab's result panel fade in smoothly, respecting reduced motion.

### What to open

The lab repo in Claude Code. This tool has no design app.

### Steps

1. **Ask Claude Code, in plan mode:** "Add Motion for React to the lab. Use LazyMotion with domAnimation and MotionConfig reducedMotion user at the app root. Animate only the ResultPanel container entrance: opacity 0 to 1, y 8 to 0, 200 ms. Do not change ResultPanel's text, structure or role. Add a test." *(Suggested workflow.)*
2. **Review the plan**, then approve.
3. Claude Code runs `npm install motion` in `frontend/`. *(Verified: [installation](https://motion.dev/docs/react-installation).)*

### What the code looks like

```tsx
import { m } from 'motion/react';

export function ResultReveal({ children }: { children: React.ReactNode }) {
  return (
    <m.div initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.2 }}>
      {children}
    </m.div>
  );
}
// In ExerciseLab.tsx: <ResultReveal><ResultPanel ... /></ResultReveal>
```

Plain language: the panel's contents are unchanged; only the box around it moves. The `role="status"` inside `ResultPanel` still announces the result to screen readers.

### How to test

```bash
cd frontend
npm run typecheck && npm run lint && npm test && npm run build
npm run test:ui    # Playwright UI tests with axe
```

### What success looks like

All existing tests still pass. The production bundle grows by roughly 20 KB (measure it). With reduced motion on, the panel appears without moving.

### Troubleshooting

| Problem | Fix |
|---|---|
| `m.div` does not animate | `LazyMotion` missing at the root |
| Bundle grew by 30 KB+ | Something imports `motion` instead of `m` |
| Animation still runs with reduced motion | `MotionConfig reducedMotion="user"` missing; the global CSS rule does not stop JavaScript animations |

## Tutorial 5: Three.js and React Three Fiber — load a model safely

**Goal (website).** Add a second 3D object using the same pattern as the AI/ML card.

### Steps for the website

1. Asset ready and compressed (Tutorial 1).
2. Ask Claude Code: "Following `tools/preview-gen/aiml3d.src.js` and the device gates in `site.js`, add a loader for `<asset>.glb`. Reuse the same Three.js chunk. Poster first. DPR cap 1.75. Pause off-screen. Respect the quantised scale."
3. Claude Code bundles with esbuild into `tools/preview-gen/assets/`.

### The core loading code (website)

```js
import { WebGLRenderer, Scene, PMREMGenerator, NeutralToneMapping, SRGBColorSpace } from 'three';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/examples/jsm/libs/meshopt_decoder.module.js';
import { RoomEnvironment } from 'three/examples/jsm/environments/RoomEnvironment.js';

const renderer = new WebGLRenderer({ antialias: true, alpha: true, powerPreference: 'low-power' });
renderer.setPixelRatio(Math.min(devicePixelRatio || 1, 1.75)); // cap sharpness for speed
renderer.outputColorSpace = SRGBColorSpace;
renderer.toneMapping = NeutralToneMapping;
renderer.domElement.setAttribute('aria-hidden', 'true'); // decorative; the page text says the same thing

const scene = new Scene();
scene.environment = new PMREMGenerator(renderer).fromScene(new RoomEnvironment()).texture;

const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder); // required for meshopt files
const gltf = await loader.loadAsync('/assets/asset-v01.glb');
scene.add(gltf.scene);
// The camera comes from the Blender file (gltf.cameras[0]) so the live model matches the poster.
```

`setMeshoptDecoder` is required for `EXT_meshopt_compression` files *(verified: [GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html))*. Import paths follow our working file `aiml3d.src.js`.

### Steps for the lab (later, only for Guided Simulation)

```bash
cd frontend && npm install three @react-three/fiber @react-three/drei
```

R3F v9 pairs with React 19 *(verified: [R3F install](https://r3f.docs.pmnd.rs/getting-started/installation))*. Load the component with `React.lazy` so the editor route does not download Three.js. See the example in Part 2, section C.

### How to test

- Playwright with headless Chromium; WebGL works through SwiftShader (as we already do).
- Check the network panel: the GLB and Three.js download only after the element nears the viewport.
- Run with `prefers-reduced-motion: reduce`: poster only, no WebGL request.

### What success looks like

Poster appears immediately; 3D replaces it smoothly on capable desktops; nothing loads on phones or low-end devices; Lighthouse unchanged.

### Troubleshooting

| Problem | Fix |
|---|---|
| Blank canvas, no error | Missing meshopt decoder, or camera not pointing at the model |
| Parts jump in size | Quantised scale: multiply stored original scale |
| Fan spins on laptops | Render loop never pauses; add IntersectionObserver and `visibilitychange` pausing |
| Very dark model | No environment map; tone mapping missing |

## Tutorial 6: Claude Code — run one safe change end to end

**Goal.** Make one small visual change without breaking anything.

### Steps

1. Open a terminal in the repo folder. Start `claude --permission-mode plan` (or press Shift+Tab until the status bar shows plan mode). *(Verified: [common workflows](https://code.claude.com/docs/en/common-workflows).)*
2. Say: "Read CLAUDE.md and AGENTS.md. Then plan, but do not edit: [your change]. List the files you will touch, the tests you will run, and anything that conflicts with the rules."
3. Read the plan. Ask questions in plain language. Approve only when you understand what will change.
4. Claude Code creates a branch, runs the existing tests first, makes the change, runs the tests again, takes screenshots at 390×844 and 1440×900, and opens a pull request.
5. Open the Vercel preview link. Look at it on your phone and laptop.
6. Merge only when happy.

### What success looks like

A pull request with a short description, green checks, screenshots and a list of what was and was not tested.

### Troubleshooting

| Problem | Fix |
|---|---|
| Claude Code touched files you did not expect | Ask it to explain each one; ask it to revert unrelated changes |
| Tests fail on `main` before the change | Stop. Fix or report that first; do not stack changes on a broken base |
| It says "should work" without running it | Ask: "Run it and show me the output." The website CLAUDE.md says never claim something works unless it was run. |
