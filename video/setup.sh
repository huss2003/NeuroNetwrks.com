#!/usr/bin/env bash
# Re-creates the video-generation environment (HyperFrames + Remotion + FFmpeg)
# on a fresh machine. Safe to run more than once.
#
#   cd video && ./setup.sh
#
# Needs: Node.js 22+, npm, git, ffmpeg. Bun is optional (only for the
# HyperFrames source checkout).

set -euo pipefail
cd "$(dirname "$0")"

HYPERFRAMES_VERSION="0.8.167"

echo "==> 1/5 FFmpeg"
if ! command -v ffmpeg >/dev/null || ! command -v ffprobe >/dev/null; then
  echo "ffmpeg/ffprobe not found. Install it first, e.g. on Ubuntu/Debian:"
  echo "    sudo apt-get install -y ffmpeg"
  echo "or on macOS:  brew install ffmpeg"
  exit 1
fi
ffmpeg -version | head -1

echo "==> 2/5 HyperFrames CLI (global command: hyperframes)"
npm install -g "hyperframes@${HYPERFRAMES_VERSION}"
hyperframes --version

echo "==> 3/5 HyperFrames source checkout (reference, docs, skills, catalog)"
if [ ! -d hyperframes-src/.git ]; then
  git clone --depth 1 https://github.com/heygen-com/hyperframes.git hyperframes-src
else
  git -C hyperframes-src pull --ff-only
fi
if command -v bun >/dev/null; then
  (cd hyperframes-src && bun install)
else
  echo "bun not installed; skipping monorepo dependency install (not needed for rendering)."
fi

echo "==> 4/5 Demo projects"
(cd hyperframes-demo && npm install && HYPERFRAMES_SKIP_SKILLS=1 hyperframes doctor || true)
(cd remotion-demo && npm install && npx remotion browser ensure)

echo "==> 5/5 Agent skills for HyperFrames (installed to ~/.claude/skills and ~/.agents/skills)"
(cd hyperframes-demo && hyperframes skills update) || echo "Skill install skipped (needs network)."

echo
echo "Done. Smoke tests:"
echo "  cd video/hyperframes-demo && hyperframes render --output renders/demo.mp4"
echo "  cd video/remotion-demo   && npx remotion render HelloWorld out/hello.mp4"
echo "  ffmpeg -f lavfi -i testsrc2=size=1280x720:rate=30:duration=3 -c:v libx264 -pix_fmt yuv420p video/renders/ffmpeg-smoke.mp4"
