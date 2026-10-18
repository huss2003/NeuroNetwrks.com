# 7. Production QA checklist

Nothing goes live until this checklist has been run and the numbers written down. **Measure, don't claim.** "It feels fast" is not a result. A result is a number, a screenshot or a test report, with the date and the device or profile used.

## Targets

| Metric | Google "good" threshold | Our internal target (website CLAUDE.md) | How to measure |
|---|---|---|---|
| Largest Contentful Paint (LCP) | ≤ 2.5 s | ≤ 1.8 s on throttled mid-range Android | Lighthouse mobile; field data later |
| Interaction to Next Paint (INP) | ≤ 200 ms | ≤ 150 ms | Field data (Vercel Speed Insights or Chrome UX report); lab proxy: Total Blocking Time |
| Cumulative Layout Shift (CLS) | ≤ 0.1 | ≤ 0.05 | Lighthouse; Playwright layout-shift observer |
| Lighthouse scores | — | ≥ 95 Performance, Accessibility, Best Practices, SEO (mobile) | Lighthouse |
| Home page JS before interaction | — | ≤ 100 KB gzip | Build output; network panel |

Google's thresholds are measured at the 75th percentile of page loads, separately for mobile and desktop ([web.dev: Web Vitals](https://web.dev/articles/vitals)). Lighthouse is a lab test on one simulated device. Treat it as a warning light; real visitors decide the final numbers.

The lab's own targets are not in its CLAUDE.md. Suggested workflow: use the same internal targets for lab pages that students open often (dashboard, lecture page), and measure the exercise page separately because Monaco is heavy.

## 1. Performance

- [ ] Lighthouse mobile and desktop on home, one program page, and (lab) dashboard, lecture and exercise pages
- [ ] LCP element identified in the report is text or an image, never a canvas
- [ ] JS transferred before interaction recorded per page
- [ ] 3D bundles (`aiml3d.js`, NN-Bot) not requested before intersection
- [ ] Three.js downloaded once even when two 3D objects are on the page
- [ ] Fonts self-hosted and preloaded only where used
- [ ] Images have width and height (prevents CLS)
- [ ] Results saved in the PR with date and profile

## 2. Slow network

- [ ] Chrome DevTools "Slow 4G" (or Lighthouse mobile throttling): page usable before 3D arrives
- [ ] Poster visible while the GLB downloads
- [ ] Save-Data header on: no 3D requested
- [ ] Lab: Monaco slow or failing → plain-text fallback appears
- [ ] Lab: Pyodide CDN slow → clear "loading Python" message; grading still possible through the server

## 3. Low-end laptops

- [ ] CPU 4× slowdown: scrolling smooth; no long tasks over 200 ms caused by 3D
- [ ] A real 4-core, 4 GB laptop if you have one (gates should show the poster)
- [ ] Fan and battery: render loops pause off-screen and when the tab is hidden
- [ ] Device pixel ratio capped (1.75 website)

## 4. Keyboard navigation

- [ ] Tab through every page: visible focus on every link and button
- [ ] NN-Bot: its bubble links are reachable and readable; the bot itself does not trap focus; it can be dismissed
- [ ] Lab: skip link works; focus moves sensibly after route changes and after a result appears
- [ ] Monaco: Tab behaviour documented for students (Monaco captures Tab; check that a keyboard user can leave the editor)
- [ ] 3D explorer (future): rotation also possible with buttons or keys, and all facts available in text

## 5. Reduced motion

- [ ] Run Playwright with `reducedMotion: 'reduce'`
- [ ] Website: no WebGL requested; posters shown; scroll line static or simple
- [ ] Lab: Motion animations reduced (`MotionConfig reducedMotion="user"`); Rive replaced by a still image
- [ ] No information is only available through motion

## 6. Loading and error states

- [ ] Every 3D or Rive component has a loading state (poster) and an error state (poster stays; no broken box)
- [ ] Block the GLB request in DevTools: page still complete
- [ ] Block the `.riv` request: result text still shows
- [ ] WebGL disabled (`--disable-webgl` or blocklisted GPU): poster
- [ ] Lab grader down: `npm run e2e:grader-down` passes

## 7. 3D asset loading

- [ ] Each GLB within its size budget (manifest)
- [ ] `gltf-transform inspect` output saved for new assets
- [ ] Correct decoder (meshopt) configured
- [ ] Model scale and colours match the poster
- [ ] Animations play; NN-Bot crossfades without popping
- [ ] Cache: versioned file names (`-v02`) so visitors get the new file

## 8. Animation smoothness

- [ ] Performance panel recording during animation: frames mostly under 16 ms on desktop
- [ ] Only `transform` and `opacity` animated in CSS and Motion
- [ ] No element animated by two systems at once
- [ ] No animation longer than 1 s in the lab interface

## 9. Stability

- [ ] Leave a page with 3D open for 10 minutes: memory steady (DevTools Memory)
- [ ] Navigate away and back in the lab: R3F and Rive instances cleaned up (no growing canvas count)
- [ ] No console errors on any tested page
- [ ] WebGL context loss handled (poster returns)

## 10. Lab regression

Run the lab's existing CI steps locally or confirm they are green on the PR:

```bash
# frontend
cd frontend
npm run lint && npm run typecheck && npm test && npm run build
npm run test:ui          # Playwright UI tests with axe
# backend and grader run in CI: gitleaks, ruff + pytest, grader docker + pytest
```

- [ ] All existing tests pass before and after the change (record both)
- [ ] New tests added for new behaviour (lab rule)
- [ ] Lecture timeline tests (`timeline.test.ts`) unchanged and passing
- [ ] `ResultPanel.test.tsx` passing; result text unchanged
- [ ] Hints still revealed one at a time from the server
- [ ] No student output rendered as HTML
- [ ] Auth, MFA and RLS untouched by visual PRs

## 11. Accessibility

- [ ] axe-core: zero serious or critical issues
- [ ] Contrast ≥ 4.5:1 for text, ≥ 3:1 for large text and interface parts
- [ ] Canvas elements `aria-hidden="true"` with the same information in text
- [ ] Touch targets ≥ 44 px (website rule)

## 12. Website-specific

- [ ] No prices anywhere
- [ ] Banned visuals absent (purple or blue gradients, glassmorphism blobs, particle or neural backgrounds, brain imagery)
- [ ] Each page: unique title, meta description, canonical, JSON-LD validates
- [ ] Sitemap, robots and `llms.txt` regenerated by `build.py`
- [ ] IndexNow ping after deploy

## The QA report

Save one short report per release:

```text
Release: website 2026-10-xx, branch feat/nn-bot
Tested on: Lighthouse 12 (mobile, simulated), Playwright Chromium + SwiftShader, Windows laptop 4-core
Home: LCP 1.6 s, CLS 0.01, TBT 90 ms, JS before interaction 78 KB gzip
NN-Bot GLB: 362 KB; loads after intersection; skipped with reduced motion (screenshot attached)
Not tested: real Android device; Safari
```

The numbers above are an example layout, not real results.
