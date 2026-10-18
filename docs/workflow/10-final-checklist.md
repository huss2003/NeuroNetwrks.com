# 10. Final end-to-end checklist

One list, from idea to a deployed website and lab. Tick each box in order. If a box cannot be ticked, stop and fix it, or write down why it is being skipped and who approved that.

## A. Before anything starts

- [ ] Owner decision: DESIGN_SYSTEM.md versus styles.css tokens for the lab
- [ ] Owner decision: keep "NeuroMind Lab" as the lab product name
- [ ] Website CLAUDE.md updated to match the real stack and the two approved WebGL objects
- [ ] Vercel team on Pro (commercial use)
- [ ] Baseline Lighthouse and test results saved for both projects
- [ ] `asset-manifest.json` created

## B. Concept

- [ ] One sentence: what the visual is for and who it helps
- [ ] Which page or lab screen; desktop only or all devices
- [ ] Subject is a software-engineering concept (modules, APIs, databases, pipelines, terminals), not a brain, sphere, particles or gradient
- [ ] Decision matrix (Part 6) consulted; tool chosen
- [ ] For the lab: feature is in approved scope

## C. Brief

- [ ] Asset brief written (purpose, states, size budget, poster, banned visuals)
- [ ] Component contract written (props, events, loading, error, reduced motion, text alternative)
- [ ] Manifest entry added with `ownerApproved: false`

## D. Create the asset

- [ ] Blender: script or `.blend` saved as master, objects named, transforms applied, actions stashed
- [ ] Spline (if used): scene saved in your account; backup downloaded
- [ ] Rive (if used): state machine and view model names match the contract; backup downloaded
- [ ] Preview image reviewed and approved by you

## E. Export and optimise

- [ ] GLB exported with the settings in Part 2, section C
- [ ] `gltf-transform inspect` output saved
- [ ] Compressed with `meshopt`; size within budget
- [ ] WebP poster made; under 60 KB
- [ ] `.riv` or `.splinecode` exported with a version suffix
- [ ] Manifest updated with real sizes

## F. Integrate

- [ ] Branch created; plan approved in plan mode
- [ ] Existing tests run and passing before changes
- [ ] Poster renders first; 3D or animation loads later
- [ ] Device and reduced-motion gates in place
- [ ] Decoders configured (meshopt)
- [ ] Animations driven by real app state (lab), never deciding results
- [ ] Text alternative present for every canvas
- [ ] No element animated by two systems

## G. Test

- [ ] Unit and UI tests pass after changes; new tests added
- [ ] Lighthouse mobile and desktop recorded
- [ ] LCP ≤ 1.8 s target (≤ 2.5 s absolute limit), CLS ≤ 0.05, INP proxy acceptable
- [ ] Home JS before interaction ≤ 100 KB gzip
- [ ] Slow network, low-end CPU, Save-Data checked
- [ ] Keyboard-only run
- [ ] Reduced-motion run
- [ ] axe clean
- [ ] Error states: asset blocked, WebGL off, grader down
- [ ] Lab regression: timeline, ResultPanel, hints, MFA untouched
- [ ] Screenshots at 390×844 and 1440×900 reviewed by you

## H. Review

- [ ] PR description has the verification checklist filled in
- [ ] Files outside the task: none, or explained
- [ ] New dependencies justified with size
- [ ] Vercel preview checked on your own phone and laptop
- [ ] You approve and set `ownerApproved: true` in the manifest

## I. Release

- [ ] Merge
- [ ] Website: deploy with the Vercel CLI as today; lab: deploy through its pipeline
- [ ] Live smoke test passes (same Playwright test against the live URL)
- [ ] Website: sitemap, robots and `llms.txt` regenerated; IndexNow pinged
- [ ] Release note saved: what changed, numbers, rollback steps

## J. After release

- [ ] Vercel logs and analytics checked after 24 and 48 hours
- [ ] Field Web Vitals reviewed once enough visits exist
- [ ] Source files backed up (Blender in repo; Rive and Spline downloads)
- [ ] Prices in Part 8 re-checked before renewing any subscription
- [ ] Lessons learned added to this manual (new version, `v02`)
