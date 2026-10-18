# 05 Design and 3D history

## Visual direction timeline
- 14 Oct: Claude Design canvas "Neuronetwrks website design" (claude.ai/artifact/SzQZetCgX2eUbfWVdxwS6t).
  Owner chose **Direction A: Cinematic sculpture**, light theme, brand colours, staircase 3D model on home hero.
- Pages redesigned one by one from owner reference images: home program tiles (each course with its own motion/3D,
  e.g. shield for cyber), Learning Experience (laptop-opening animation), Projects carousel (3 projects, AgentFlow AI
  renamed from "tool-using AI agent"), About (Our Story section, no "built by educators"), Admissions (teen photo),
  FAQs, Contact, Faculty (later hidden).
- 15 Oct: owner-supplied 3D model images per program card: AI Foundation ("AI ENG", plain AI text, no molecule balls),
  AI/ML, Software Dev, Data Science, Product UX, Cybersecurity; "Ready to ask" CTA model. Wide program cards
  (text left, model right). AI/ML card = live WebGL Blender model (docs/3d/ai-ml-training-pipeline) on capable desktops.

## Blender / 3D (tools/blender, docs/3d)
- Shared house-style module + scripts: ai_ml_pipeline.py, build_path_staircase.py, ai_foundation_first_app.py,
  cyber_network_defence.py and others. Models (GLB + renders) in docs/3d/: admissions-steps, ai-foundation-first-app,
  ai-ml-training-pipeline, build-path-staircase, cta-night-build, cyber-network-defence, data-science-pipeline,
  laptop-lab, nn-bot, product-ux-flow, project-image-classifier, project-rag-assistant, software-dev-architecture.
- Review gallery artifact: "NeuroNetworks 3D Model Review" (claude.ai/artifact/VNYiBcQyTfj55KyMM1uKJ1) — awaiting approval.
- **NN-Bot**: small rigged, animated robot (GLB) at bottom of every page, waves + quick links, footer "Show the robot"
  toggle, localStorage key `nnbot` = off. Built, NOT deployed (awaiting approval).

## Figma (16 Oct)
- File https://www.figma.com/design/K78t9xZp319MrlBTmSIxQR, pages "Assets & cover", "Desktop · 1440", "Mobile · 390"
  (Starter plan: max 3 pages; MCP call limit hit). Editable layers rebuilt from DOM capture (scratchpad figma/capture.mjs, gen.py).
- Done: 9 desktop + 7 mobile; partial: Home mobile, AI Foundation/Product UX/About desktop. Remaining 24 parts via
  dev plugin NeuroNetworks-Figma-Import.zip (sent to owner, owner must run it). Figma needs PNG/JPEG, not WebP.

## Redesign research (paused 15 Oct)
- Plan: /root/.claude/plans/root-claude-uploads-0779ba5b-5159-575f-cuddly-pizza.md. 155 candidates → 100+ passing
  (>100k visits via Tranco/Similarweb, UI score ≥7/10), report artifact, 6 concepts (Exhibition Dark, Cinematic Scroll 10K,
  Developer Console, Editorial Syllabus, Playground with NN-Bot, Parent-first Trust) in "NeuroNetworks Home Concepts"
  (claude.ai/artifact/UUryDBPvKxz8zheGWHXgTn, assets uploaded, no artboards). Firecrawl/OpenRush credits ran out.
