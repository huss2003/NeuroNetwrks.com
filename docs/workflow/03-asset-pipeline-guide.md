# 3. Asset pipeline guide

This part says where every file lives, how it is named, and which copy is the master. The single most important rule: **never make the only copy an export.** A `.glb`, `.riv` or `.splinecode` file is a delivery format. If you lose the `.blend`, the Rive project or the `.spline` file, you can no longer change the asset.

## Five kinds of file

| Kind | Meaning | Examples | Where it lives | Can be deleted? |
|---|---|---|---|---|
| Editable source | The master you open to make changes | `.blend`, Blender Python script, Rive project, `.spline` | Repo (`docs/3d/`, `tools/blender/`) or shared drive, recorded in the manifest | Never |
| Production export | The compressed file the site or lab loads | `.glb` (meshopt), `.riv`, `.webp` poster | Website: `tools/preview-gen/assets/`; lab: `frontend/public/` | Only when replaced by a newer version |
| Third-party embedded scene | A scene hosted by someone else and loaded by URL | Spline public URL, Spline Viewer embed | Spline account; URL in the manifest | Only after removing it from every page |
| Runtime configuration | Code-side settings for an asset | Loader module, device checks, Rive property names, component contract | `tools/preview-gen/*.src.js`; lab `src/features/...` | Only with the asset |
| Temporary prototype | Experiments, test renders, AI-generated drafts | `scratch/`, renders named `*-test` | Outside the repo or in a git-ignored folder | Yes, freely |

## Folder structure: website repo (`huss2003/NeuroNetwrks.com`)

The folders below exist today except where marked *(new)*.

```text
NeuroNetwrks.com/
├── tools/
│   ├── blender/                     # Editable source: Blender Python scripts (one per asset)
│   │   ├── ai_ml_pipeline.py
│   │   ├── data_science_pipeline.py
│   │   ├── software_dev_architecture.py
│   │   ├── product_ux_flow.py
│   │   └── nn_style.py              # shared materials and palette
│   └── preview-gen/
│       ├── build.py                 # static site generator -> site-preview/
│       ├── site.css, site.js        # global styles and vanilla JS
│       ├── aiml3d.src.js            # Runtime config: Three.js loader source
│       └── assets/                  # Production exports served to visitors
│           ├── ai-ml-training-pipeline.glb   # meshopt-compressed
│           ├── aiml3d.js                     # esbuild bundle
│           └── i-aiml-pipeline.webp          # poster
├── docs/
│   ├── 3d/
│   │   └── ai-ml-training-pipeline/ # Editable source + uncompressed export + preview
│   │       ├── README.md
│   │       ├── ai-ml-training-pipeline.blend
│   │       ├── ai-ml-training-pipeline.glb
│   │       └── preview.png
│   ├── 3d/asset-manifest.json       # (new) one entry per asset
│   └── workflow/                    # this manual
└── site-preview/                    # generated output; never edit by hand
```

## Folder structure: lab repo (`huss2003/Neuromind-lab`)

Nothing below `assets/` or `rive/` exists yet. Add folders only when the first approved asset arrives.

```text
Neuromind-lab/
├── frontend/
│   ├── public/
│   │   ├── pyodide-worker.js        # exists
│   │   ├── models/                  # (new) production .glb for R3F
│   │   └── rive/                    # (new) production .riv files
│   └── src/
│       ├── styles.css               # Cortex design tokens (source of truth until owner decides)
│       ├── features/lab/            # ExerciseLab, ResultPanel (do not restyle without approval)
│       ├── features/lecture/        # timeline.ts state machine
│       └── features/visual/         # (new) GradeBadge, ArchitectureExplorer, motion presets
├── content/
└── docs/
    └── 04-ui-ux/
        ├── DESIGN_SYSTEM.md         # v0.1.0, conflicts with styles.css (owner decision)
        └── assets/                  # (new) briefs, manifest, source exports (.rev backups)
```

> Lab rule from its CLAUDE.md: "Never expand scope without approval." Creating these folders is part of an approved task, not something Claude Code does on its own.

## Naming conventions

- **kebab-case**, lowercase, no spaces: `nn-bot`, `db-architecture-explorer`.
- **Version suffix** `-v01`, `-v02` on production exports and Rive or Spline files when the content changes: `grade-badge-v02.riv`. Raise the version when anything visible changes, so browsers do not show an old cached copy.
- **Same base name** across source, export and poster: `nn-bot-v03.blend`, `nn-bot-v03.glb`, `nn-bot-v03-poster.webp`.
- **Object names inside 3D files** are stable and meaningful (`Server_DB`, `Arm_L`, `Bar_03`) because code finds them by name. Renaming one breaks the code.
- **Animation names** match exactly what code calls: `Idle`, `Walk`, `Wave`, `Jump`, `LookAround`.
- **Rive names**: artboard `GradeBadge`, state machine `Result`, view model `GradeVM`, properties in camelCase.

The existing AI/ML asset (`ai-ml-training-pipeline.glb`) has no version suffix. Do not rename it now; it works and renaming means changing code. Add `-v02` the next time it changes.

## The asset manifest

The manifest is a single JSON file listing every visual asset, where its master copy is, and where it is used. Claude Code reads it before touching any asset and updates it in the same pull request.

### Example (`docs/3d/asset-manifest.json`)

```json
{
  "schemaVersion": 1,
  "assets": [
    {
      "id": "nn-bot",
      "type": "3d-model-animated",
      "tool": "blender",
      "version": "v03",
      "sourcePath": "tools/blender/nn_bot.py",
      "sourceFile": "docs/3d/nn-bot/nn-bot-v03.blend",
      "exportPath": "tools/preview-gen/assets/nn-bot-v03.glb",
      "posterPath": "tools/preview-gen/assets/nn-bot-v03-poster.webp",
      "animations": ["Idle", "Walk", "Wave", "Jump", "LookAround"],
      "compression": "meshopt",
      "sizeBudgetKB": 400,
      "actualSizeKB": null,
      "ownerApproved": false,
      "usedOnPages": ["/", "all pages (desktop only)"],
      "fallback": "poster hidden on mobile; robot not shown",
      "notes": "Desktop only. Skipped for reduced motion, Save-Data, <=4 cores, <=4 GB."
    }
  ]
}
```

### Field meanings

| Field | Meaning |
|---|---|
| `id` | Stable kebab-case name, never changes |
| `type` | `3d-model`, `3d-model-animated`, `rive`, `spline-scene`, `poster`, `motion-preset` |
| `tool` | Which tool owns the source |
| `version` | Current version suffix |
| `sourcePath` / `sourceFile` | Script and editable master |
| `exportPath` | Production file |
| `sizeBudgetKB` / `actualSizeKB` | Limit and measured size (fill after compression) |
| `ownerApproved` | `true` only after you have seen it and said yes |
| `usedOnPages` | Every page or screen that loads it |
| `fallback` | What people see without WebGL or with reduced motion |

## Size budgets (starting points, adjust after measuring)

| Asset | Budget | Why |
|---|---|---|
| Card model (one of the 11) | ≤ 300 KB compressed GLB | AI/ML card is 293 KB today and loads well |
| NN-Bot with 5 animations | ≤ 400 KB compressed GLB | Animation data adds size; measure |
| Poster image | ≤ 60 KB WebP at display size | Shown to most visitors |
| Rive badge | ≤ 50 KB `.riv` | Small vector file; **unverified** typical size, measure ours |
| Website home page JS before interaction | ≤ 100 KB gzip | Website CLAUDE.md rule; 3D bundles load later, after interaction or intersection |

## The flow for one 3D asset (website)

1. Brief written and approved (Part 2, section G).
2. Claude Code writes or updates the Blender script in `tools/blender/`.
3. Script runs headless and writes `.blend`, `.glb`, `preview.png` into `docs/3d/<id>/`.
4. You look at `preview.png`. Approve or ask for changes.
5. `npx @gltf-transform/cli meshopt` writes the compressed GLB into `tools/preview-gen/assets/`.
6. A WebP poster is made from `preview.png`.
7. Loader code is updated; esbuild bundles it.
8. Manifest entry updated with real sizes.
9. Tests, screenshots, Lighthouse (Part 7).
10. Pull request; you approve; deploy.

## Backups

- `.blend` files are binary and can be large. Keep them in the repo while they stay under a few MB; if one grows past about 50 MB, move it to shared storage and record the location in the manifest (GitHub warns on large files; **unverified** exact limits, check GitHub docs before relying on them).
- Rive and Spline projects live in those companies' accounts. Download a backup after every approved change and record the date in the manifest.
- Never keep the only copy on one laptop.

## Licence note on Blender scripts

Blender's licence page says that publicly shared Python scripts using the Blender API fall under the GPL ([blender.org licence](https://www.blender.org/about/license/)). The models you create are your property. If the website repository is public, the scripts in `tools/blender/` are effectively GPL. This is normal and usually fine, but it is your decision; ask a lawyer if it matters to you.
