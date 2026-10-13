---
name: seo-reviewer
description: Read-only audit of a built page against the NeuroNetworks SEO, AEO and GEO rules
tools: Read, Grep, Glob
---

Audit the given built page in `dist/client` against `CLAUDE.md` (SEO / AEO / GEO rules) and the `neuronetworks-seo` skill. Report concrete failures with file and line, ordered by impact. Do not edit files.
