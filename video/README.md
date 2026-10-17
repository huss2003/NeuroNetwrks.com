# Video workspace (HyperFrames + Remotion + FFmpeg)

This folder is a separate toolbox for making MP4 videos. It is not part of the
website build. Nothing in here ships to neuronetwrks.com.

## What is installed

| Tool | What it does | Where |
| --- | --- | --- |
| FFmpeg 6.1 | Encodes frames and audio into MP4, WebM, MOV, GIF | system `ffmpeg` / `ffprobe` |
| HyperFrames 0.8.167 | Write a video as plain HTML + CSS + GSAP, render it with headless Chrome and FFmpeg | global `hyperframes` command, `hyperframes-demo/`, source clone in `hyperframes-src/` |
| Remotion 4.0.536 | Write a video as React components, render it with headless Chrome and FFmpeg | `remotion-demo/` |

Both HyperFrames and Remotion download their own Chrome headless build on first
use. They do not need Docker, whisper, or any paid service to render an MP4.

## Fresh machine

```bash
cd video
./setup.sh
```

The script installs the `hyperframes` command, clones the HyperFrames source,
installs both demo projects, downloads Chrome for rendering, and installs the
HyperFrames agent skills into `~/.claude/skills`.

## Make a video with HyperFrames

```bash
cd video/hyperframes-demo
hyperframes check                               # lint + runtime + layout + contrast gate
hyperframes render --output renders/demo.mp4    # 1920x1080, 30 fps, H.264
hyperframes preview                             # open Studio in the browser
```

Edit `index.html`. Every animated element has `class="clip"` and `data-start` /
`data-duration` attributes. All motion goes on one paused GSAP timeline stored
on `window.__timelines`, which is what lets the renderer seek frame by frame.

More: `hyperframes docs`, https://hyperframes.heygen.com, and the full
source with 50+ ready-made blocks in `hyperframes-src/registry/`.

## Make a video with Remotion

```bash
cd video/remotion-demo
npx remotion render HelloWorld out/hello.mp4    # render the sample composition
npm run dev                                     # open Remotion Studio
```

Compositions are registered in `src/Root.tsx`. Each one is a React component
that receives the current frame through `useCurrentFrame()`.

More: https://www.remotion.dev/docs. Note Remotion's licence: free for
individuals and teams of up to three people, otherwise a company licence is
needed (https://www.remotion.pro/license).

## FFmpeg on its own

```bash
# 3-second 720p test pattern with a tone
ffmpeg -f lavfi -i testsrc2=size=1280x720:rate=30:duration=3 \
       -f lavfi -i sine=frequency=440:duration=3 \
       -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest renders/ffmpeg-smoke.mp4

# inspect any file
ffprobe -v error -show_entries format=duration:stream=codec_name,width,height file.mp4
```

## What is git-ignored here

`hyperframes-src/` (the upstream clone), every `node_modules/`, and all render
output (`renders/`, `out/`, `*.mp4`). Run `./setup.sh` to get them back.
