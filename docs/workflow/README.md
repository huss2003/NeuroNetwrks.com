# NeuroNetworks 3D and motion lab: operating manual

**Owner:** NeuroNetworks AI Ed (Learn · Develop · Create)
**Covers:** the marketing website (neuronetwrks.com) and the student learning lab (NeuroMind Lab)
**Version:** v01, 15 October 2026. Prices and product facts were checked on this date. Re-check them before you spend money.

This folder is the Markdown copy of the Word manual `NeuroNetworks-3D-Motion-Lab-Operating-Manual.docx`. Both say the same thing. Use whichever is easier to read.

## How to use this manual

Read "Start here" first. It is one page. Then read the part you need today. You do not have to read the whole manual in order.

Each part starts in plain language. Technical detail comes after, for Claude Code or a developer. When a sentence says **verified**, it was checked against the official page linked next to it on 15 October 2026. When it says **unverified**, we could not confirm it and you should check before relying on it. When it says **suggested workflow**, it is our advice, not a feature of the tool.

## Files in this folder

| File | What it covers |
|---|---|
| [01-tool-master-guide.md](01-tool-master-guide.md) | What each of the six tools is for, and what it must not be used for |
| [02-integration-guide.md](02-integration-guide.md) | How work moves from one tool to the next (seven connections) |
| [03-asset-pipeline-guide.md](03-asset-pipeline-guide.md) | Folders, file names, the asset manifest, and where the master copy lives |
| [04-implementation-roadmap.md](04-implementation-roadmap.md) | Phases 0 to 8, from audit to production release |
| [05-practical-tutorials.md](05-practical-tutorials.md) | Beginner tutorials for each tool |
| [06-decision-matrix.md](06-decision-matrix.md) | Ten common situations and which tool to use |
| [07-production-qa-checklist.md](07-production-qa-checklist.md) | What to test before anything goes live |
| [08-cost-breakdown-inr.md](08-cost-breakdown-inr.md) | Costs in Indian rupees, free versus paid |
| [09-claude-code-operating-instructions.md](09-claude-code-operating-instructions.md) | How to drive Claude Code without breaking working features |
| [10-final-checklist.md](10-final-checklist.md) | One checklist from idea to deployed website and lab |

<!-- docx:start-here -->
## Start here: the short version

**What you already have.** The website already shows real 3D. Blender builds the model from a script, a free tool shrinks the file, and Three.js draws it in the browser only on capable desktop computers. Everyone else sees a still image. This works today. Keep it.

**The smallest stack that does the job.** Blender (free) plus Three.js (free) covers the website. Motion for React (free) and, later, Rive (free to start) cover the student lab. Claude Code (already paid for in your Claude Max plan) writes and tests the code. Spline is optional. Pay for Spline or Rive only when a specific need appears, such as wanting to design 3D scenes yourself without code.

**Who does what.**

| Job | Tool |
|---|---|
| Make a detailed 3D model (architecture, robot, pipeline) | Blender |
| Design a 3D scene by hand, visually, without code | Spline (optional) |
| Animate a small interactive graphic that reacts to a student (pass, fail, progress) | Rive |
| Animate page elements in the React lab (panels, lists, page changes) | Motion for React |
| Show and control 3D in the browser | Three.js on the website; React Three Fiber in the lab |
| Write the code, connect everything, test, take screenshots | Claude Code |

**Five rules that protect the business.**

1. Never let 3D or animation block the code editor, the terminal, or grading in the lab. They are extras. They must be optional.
2. Never make an export the only copy. Keep the `.blend`, `.spline` or `.riv` source file in the repo or in shared storage.
3. Measure speed; do not guess. Use Lighthouse and Playwright before every release.
4. Respect "reduce motion" settings and keyboard users on every animated element.
5. Work in small branches with Claude Code in plan mode first. Never rebuild a feature that already works.

**Decisions only you can make (before the visual upgrade starts).**

- The lab's design tokens in `docs/04-ui-ux/DESIGN_SYSTEM.md` (v0.1.0) do not match the real `frontend/src/styles.css`. Choose which one is correct.
- The lab is branded "NeuroMind Lab". The company is "NeuroNetworks AI Ed". Confirm whether "NeuroMind Lab" stays as the product name.
- The website's `CLAUDE.md` still describes an Astro and Cloudflare stack and says "one WebGL object maximum". The live site is a Python static generator on Vercel with two approved WebGL objects (the AI/ML card and NN-Bot). Update `CLAUDE.md` so it matches reality.
- Vercel's free Hobby plan is for non-commercial use only. A business website and a paid course lab need the Pro plan. Check which plan your Vercel team is on.

**What to do this week.** Finish NN-Bot and the 11 Blender models using the pipeline that already works (Part 4, phases 2 and 4). Do not add Spline, Rive or React to the website.
<!-- /docx -->

<!-- docx:sources -->
## Sources and verification log

Every price and tool-specific claim in this manual was checked against the pages below on **15 October 2026** unless stated. Prices change; re-check before buying.

### Pricing pages

| Source | What it verified |
|---|---|
| [spline.design/pricing](https://spline.design/pricing) | Free $0; Hobby $15 per seat per month (monthly) or $12 (yearly, $144 per year); Pro $30 monthly or $25 yearly ($300 per year); Max $70 monthly or $60 yearly; Enterprise custom. Free web exports carry a watermark. Code export download from Pro; self-hosted export on Enterprise. AI credits per month: Hobby 2,000, Pro 3,000, Max 10,000. |
| [rive.app/pricing](https://rive.app/pricing) | Free $0 (exports .riv with a Rive splash screen, 3 collaborative files); Cadet $9 per seat per month (export without splash screen, unlimited files, 3 seats maximum); Voyager $32 per seat per month; Enterprise $120 per seat per month for organisations with $10M+ annual revenue. The page has a yearly/monthly toggle but shows one price per plan, so whether $9 and $32 are yearly-billed rates is **unverified**. |
| [vercel.com/pricing](https://vercel.com/pricing), [Hobby plan docs](https://vercel.com/docs/plans/hobby), [Pro plan docs](https://vercel.com/docs/plans/pro-plan), [Fair use guidelines](https://vercel.com/docs/limits/fair-use-guidelines) | Hobby free, "restricted to non-commercial personal use only"; "advertising the sale of a product or service" counts as commercial. Pro $20 per month platform fee with one deploying seat and $20 monthly usage credit; extra deploying seats $20 each; viewer seats free. Prices exclude GST. |
| [supabase.com/pricing](https://supabase.com/pricing) | Free $0: 500 MB database per project, 50,000 monthly active users, 5 GB egress, paused after 1 week of inactivity, 2 active projects. Pro from $25 per month: 8 GB disk, 100,000 MAU, 250 GB egress, $10 compute credit, never paused. Basic MFA included on both; phone MFA is a Pro add-on at $75 per month for the first project. |
| [AWS EC2 price list, Asia Pacific (Mumbai)](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/ap-south-1/index.csv) (file dated 12 Oct 2026) | On-demand Linux: t4g.small $0.0112 per hour; t3.small $0.0224; t3.micro $0.0112; t3.medium $0.0448. gp3 storage $0.0912 per GB-month. |
| [aws.amazon.com/vpc/pricing](https://aws.amazon.com/vpc/pricing/) | Public IPv4 address $0.005 per hour (in use or idle). |
| [aws.amazon.com/free](https://aws.amazon.com/free/) | New accounts: up to $200 credits, account closes after 6 months or when credits run out on the free plan. EC2 free hours for a specific instance type: **not stated, unverified**. |
| [claude.com/pricing](https://claude.com/pricing) | Max "from $100" per month; "Claude Code is included in all paid plans." |
| [api.frankfurter.dev](https://api.frankfurter.dev/v1/latest?from=USD&to=INR) (European Central Bank reference data), cross-checked with [open.er-api.com](https://open.er-api.com/v6/latest/USD) | 1 USD = ₹95.16 on 14 October 2026 (ECB); ₹95.25 on 15 October 2026 (second source). This manual uses ₹95.16. Your card issuer's rate and forex mark-up will differ. |
| [Treelife: OIDAR registration](https://treelife.in/legal/oidar-registration-in-india/), [xflowpay: OIDAR services](https://www.xflowpay.com/blog/oidar-services) | Secondary sources only: foreign online services sold to unregistered Indian buyers carry 18% IGST; GST-registered businesses pay under reverse charge. **Confirm with your chartered accountant.** |

### Tool documentation

| Source | What it verified |
|---|---|
| [Spline: importing content](https://docs.spline.design/importing-content/how-to-import-content.md) | Imports OBJ, FBX, STL, GLTF, GLB, .spline, PNG, JPG, SVG (partial), MP4, MP3, WAV, Gaussian splats. |
| [Spline: importing animated objects](https://docs.spline.design/importing-content/import-animated-objects.md) | FBX and GLB/GLTF with animations, including skeletal. One animation per file; add more with the "+" icon. |
| [Spline: exporting as code](https://docs.spline.design/exporting-your-scene/web/exporting-as-code.md) | Targets: Vanilla JS, Three.js, React, Next.js, react-three-fiber. "Animations and events are only enabled when exporting to Vanilla js and React." Download to host yourself. |
| [Spline: self-hosted export](https://docs.spline.design/exporting-your-scene/web/exporting-as-self-hosted-project.md) | Bundled ZIP of project, assets and runtime; Enterprise plan. |
| [Spline: viewer](https://docs.spline.design/exporting-your-scene/web/exporting-as-spline-viewer.md) | `<spline-viewer>` web component; lazy-loads by default; optional loading spinner and hint; logo toggle. |
| [Spline: glTF/GLB export](https://docs.spline.design/exporting-your-scene/files/exporting-as-gtlf-glb.md) | Only colour layer of materials; basic textures; only position, rotation and scale animations; no states, events, interactivity, lighting or post-processing. "Color & Texture" option on Pro and Max. |
| [Spline: optimisation](https://docs.spline.design/exporting-your-scene/how-to-optimize-your-scene.md) | Fewer than 3 lights; 1 to 2 subdivision levels; geometry compression "Performance"; no more than 3 embeds per page. |
| [Spline: AI 3D generation](https://docs.spline.design/generate/ai-3d-generation.md), [AI agent](https://docs.spline.design/spline-ai/ai-agent.md) | Text or image to 3D model using monthly AI credits on paid plans; in-editor AI agent edits scenes with normal undo history. |
| [Spline: MCP server](https://docs.spline.design/generate/spline-mcp-server.md) | Runs inside the Spline desktop app (macOS or Windows) on 127.0.0.1; lets Claude Code and other MCP clients inspect, edit and screenshot scenes; registers itself in `~/.claude.json`; plan requirement not stated. |
| [splinetool/react-spline README](https://github.com/splinetool/react-spline) | `@splinetool/react-spline` + `@splinetool/runtime`; props `scene`, `onLoad`, `renderOnDemand`; event props such as `onSplineMouseDown`; `findObjectByName`, `emitEvent`; lazy loading with `React.lazy`; self-host the `.splinecode` file for CORS problems. |
| [Rive: React runtime](https://rive.app/docs/runtimes/react/react.md) | `npm i --save @rive-app/react-webgl2`; `useRive({ src, stateMachine, autoplay, autoBind })`; container must have a size. |
| [Rive: React data binding](https://rive.app/docs/runtimes/react/data-binding) | `useViewModel`, `useViewModelInstance`, `useViewModelInstanceBoolean/Number/String/Trigger`. |
| [Rive: React inputs (legacy)](https://rive.app/docs/runtimes/react/inputs.md) | "DEPRECATED: Use Data Binding instead of Inputs for controlling Rive animations." |
| [Rive: choosing a renderer](https://rive.app/docs/runtimes/choose-a-renderer/overview.md) | `@rive-app/react-webgl2` (Rive Renderer, highest fidelity), `react-canvas` (many instances, smaller), `react-canvas-lite` (smallest). |
| [rive-react on GitHub](https://github.com/rive-app/rive-react) | MIT licence. |
| [Motion: installation](https://motion.dev/docs/react-installation) | `npm install motion`; import from `"motion/react"`; React 18.2 or newer. |
| [Motion: bundle size](https://motion.dev/docs/react-reduce-bundle-size) | `motion` component about 34 KB; `m` + `LazyMotion` about 4.6 KB initial, plus 15 KB (`domAnimation`) or 25 KB (`domMax`). |
| [Motion: accessibility](https://motion.dev/docs/react-accessibility) | `<MotionConfig reducedMotion="user">` disables transform and layout animations for users who ask for reduced motion; `useReducedMotion()`. |
| [Motion: scroll animations](https://motion.dev/docs/react-scroll-animations), [AnimatePresence](https://motion.dev/docs/react-animate-presence) | `whileInView` + `viewport={{ once: true }}`; `useScroll({ target, offset })`; `useTransform`; `AnimatePresence` needs a unique `key` per child; `mode="wait"`. |
| [motiondivision/motion on GitHub](https://github.com/motiondivision/motion) | "Motion is MIT licensed." Motion+ is a separate paid tier. |
| [React Three Fiber: installation](https://r3f.docs.pmnd.rs/getting-started/installation) | `@react-three/fiber@9` pairs with React 19; Vite works without extra config. |
| [drei: useGLTF](https://drei.docs.pmnd.rs/loaders/gltf-use-gltf) | `useGLTF(path, useDraco = true, useMeshOpt = true)`; `useGLTF.preload(url)`. |
| [gltfjsx on GitHub](https://github.com/pmndrs/gltfjsx) | `npx gltfjsx model.glb`; `--transform`, `--types`, `--resolution` (default 1024), `--format` (default webp), `--keepnames`. |
| [glTF Transform CLI](https://gltf-transform.dev/cli) | `optimize`, `inspect`, `meshopt`, `draco`, `resize`, `webp`, `etc1s`, `uastc`, `dedup`, `prune`, `simplify`. |
| [Three.js GLTFLoader](https://threejs.org/docs/pages/GLTFLoader.html) | `setMeshoptDecoder` needed for `EXT_meshopt_compression`; `setDRACOLoader` for Draco; `setKTX2Loader` for KTX2. |
| [Three.js on GitHub](https://github.com/mrdoob/three.js) | MIT licence. |
| [Blender 5.1 manual: glTF 2.0](https://docs.blender.org/manual/en/5.1/addons/import_export/scene_gltf2.html) | Formats glTF Binary (.glb), Separate, Embedded; Include: Selected, Visible, Renderable Objects; "Y Up"; "Apply Modifiers"; Images: PNG, JPEG, WebP, None; Draco compression; Animation modes Actions, Active Actions merged, NLA Tracks, Scene; "Export Deformation Bones only"; "If you have multiple actions you want to export, make sure they are stashed!" |
| [blender.org: licence](https://www.blender.org/about/license/) | GPL; free for any purpose including commercial; "What you create with Blender is your sole property"; publicly shared Python scripts using the Blender API fall under GPL. |
| [Claude Code: common workflows](https://code.claude.com/docs/en/common-workflows) | Plan mode via `claude --permission-mode plan` or Shift+Tab; worktrees with `claude --worktree`; images and screenshots in the conversation; `@` file references. |
| [web.dev: Web Vitals](https://web.dev/articles/vitals) | Good: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1, at the 75th percentile, segmented by mobile and desktop. |

### Facts from the project itself

The audit facts (pipeline, file sizes, rules, lab architecture) come from the two repositories: `huss2003/NeuroNetwrks.com` (CLAUDE.md, `tools/blender/`, `tools/preview-gen/`, `docs/3d/`) and `huss2003/Neuromind-lab` (CLAUDE.md, `frontend/package.json`, `frontend/src/features/lecture/timeline.ts`, `frontend/src/features/lab/ExerciseLab.tsx`, `frontend/src/styles.css`).
<!-- /docx -->
