# ai-ml-training-pipeline (AI/ML Engineering card model)

This is the 3D model on the AI/ML Engineering program card. It shows the training pipeline from left to right:

1. input data;
2. processor;
3. four feature layers, with lime activation nodes;
4. the trained model;
5. a training chart and a prediction chart.

It contains no text, logos or numbers. The card's title, facts and arrow button are ordinary HTML, not part of the model.

## Files

| File | What it is |
|---|---|
| `tools/blender/ai_ml_pipeline.py` | The Blender script that builds the whole scene, including materials, lights and camera. This is the source of truth. |
| `ai-ml-training-pipeline.blend` | Editable Blender file, saved by the script. |
| `ai-ml-training-pipeline.glb` | Full-precision GLB export. |
| `preview.png` | High-resolution transparent Cycles render, 2400 × 1350. |
| `tools/preview-gen/assets/ai-ml-training-pipeline.glb` | Web copy of the GLB, compressed with meshopt (`gltf-transform meshopt`), about 0.3 MB. |
| `tools/preview-gen/assets/i-aiml-pipeline.webp`, `-m.webp` | Static fallback images (1200 px and 640 px) made from `preview.png`. |
| `tools/preview-gen/aiml3d.src.js` | Three.js loader and animations. It is bundled to `tools/preview-gen/assets/aiml3d.js`. |

## Rebuild

```bash
pip install bpy==5.1.2          # Blender 5.1 as a Python module (Python 3.13)
python tools/blender/ai_ml_pipeline.py --out docs/3d/ai-ml-training-pipeline --samples 128 --res 2400
npx @gltf-transform/cli@4 meshopt docs/3d/ai-ml-training-pipeline/ai-ml-training-pipeline.glb tools/preview-gen/assets/ai-ml-training-pipeline.glb
node_modules/.bin/esbuild tools/preview-gen/aiml3d.src.js --bundle --format=esm --minify --target=es2020 --outfile=tools/preview-gen/assets/aiml3d.js
```

After rebuilding, regenerate the two webp posters from `preview.png`. Then run `python3 tools/preview-gen/build.py`. The asset version hash already includes the GLB and the JS bundle.

## Object names

The website code looks these names up, so keep them stable. Blender is Z-up; the GLB is Y-up.

| Object | What it is | Animation on the site |
|---|---|---|
| `ai-ml-training-pipeline` | Root of the model | Turns at most 2.5° toward the pointer while it hovers over the card |
| `Base` | Frosted platform | None |
| `InputData` | Group of input items: `InputCube01`–`06`, `InputTile01`–`03`, `InputPanel` | Children slide in from the left on first view |
| `ProcessorCore` | Accelerator block: fins, compute grid, glowing output face | Rises into place |
| `FeatureLayer01`–`04` | Glass tensor/feature panels with grid cells | Drop into place one after another |
| `ActivationNodes` | Lime nodes on the layers | Glow brighter on hover |
| `DataPaths` | Cyan data lines and arrow. Its `extras.paths` holds the sampled path points in GLB space; `mainPathCount` is how many of them are main paths | 3–5 slow light pulses travel along the paths |
| `TrainedModel`, `TrainedModelCore` | Output glass cube with the inner lattice | Slides in from the right |
| `TrainingChart`, `TrainingCurveA`, `TrainingCurveB` | Abstract loss-curve panel | Curves draw in on a 7-second loop |
| `PredictionChart`, `PredictionBar01`–`05` | Abstract prediction-bar panel | Bars rise and settle slowly |
| `CardCamera` | Three-quarter camera, 16:9 | The site uses it, so the live model lines up with the poster image |

## Loading rules (site.js)

The model loads only when the card is within 300 px of the viewport. It does not load when any of these is true:

- the viewport is under 760 px;
- reduced motion is on;
- Save-Data is on;
- the device reports 4 or fewer CPU cores, or 4 GB or less memory;
- WebGL is unavailable.

In each of those cases the WebP poster stays in place.

Rendering pauses when the card is off screen or the tab is hidden. There is no post-processing, and the pixel ratio is capped at 1.75.
