# Knowledge graph (~600 tokens)

```mermaid
graph LR
  Owner[Hussain / owner] -->|owns| Brand[NeuroNetworks AI Ed]
  Brand -->|tagline| Tag[Learn · Develop · Create]
  Brand -->|offers| AIF[AI Foundation 1y 104h Class 8+]
  Brand -->|offers| SPEC[5 x 3y 624h after Class 10]
  SPEC --> AIML[AI/ML Engineering] & SW[Software Development] & DS[Data Science & AI] & UX[Product & UX / AI Design] & CY[Cybersecurity]
  Brand -->|website| Site[neuronetwrks.com]
  Site -->|built by| Gen[tools/preview-gen/build.py]
  Gen -->|outputs| Out[site-preview/]
  Out -->|npx vercel deploy --prod| Vercel[Vercel project neuronetwrks-preview]
  Vercel -->|domain via Squarespace DNS| Site
  Site -->|analytics after consent| GA4[G-1D2KJQ9RCF]
  Site -->|enquiries| Sheet[Google Sheet + Hussain@neuronetwrks.com]
  Site -->|indexed by| GSC[Search Console verified] & Bing[Bing / IndexNow]
  Repo[github huss2003/NeuroNetwrks.com branch preview-site] --> Gen
  Blender[tools/blender scripts] -->|GLB + renders| D3[docs/3d models] --> Out
  NNBot[NN-Bot robot, not deployed] --> Out
  Figma[Figma file K78t9xZp319MrlBTmSIxQR] -.export of.-> Out
  CD[Claude Design canvases] -.design source.-> Gen
  Docs[docs/*.docx deliverables] -.describe.-> Site
  Rules[CLAUDE.md hard rules] -->|constrain| Gen
```

## Edge list (grep-friendly)
- program → entry: AI Foundation→Class 8+; all 3-yr→Class 10 pass
- program → hours: AIF 104 (2 h/wk, 52 wk); 3-yr 624 (4 h/wk, 208/yr, 36 monthly modules + 1 h exam each)
- site → host: Vercel `neuronetwrks-preview`; preview URL neuronetwrks-preview.vercel.app
- site → source: `tools/preview-gen` (build.py, site.css, site.js, art.py, guides_pages.py, projects_pages.py)
- site → legacy: Astro scaffold in repo (CLAUDE.md describes Astro/Cloudflare; ACTUAL live site = preview-gen on Vercel)
- domain → DNS: Squarespace (apex A/ALIAS to Vercel, www redirect, Google MX/SPF kept)
- rules → file: `/home/user/NeuroNetwrks.com/CLAUDE.md`, open facts → `docs/open-questions.md`, pending → `docs/launch-checklist.md`
