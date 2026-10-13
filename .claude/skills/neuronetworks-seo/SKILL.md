---
name: neuronetworks-seo
description: SEO, AEO and GEO checklist for neuronetwrks.com pages. Use when creating or auditing any page, schema, robots.txt, sitemap or meta tags.
---

# NeuroNetworks SEO

Every page needs: unique title (≤60 chars) and description (≤155), self-referencing canonical, `<html lang="en-IN">`, one H1 with the descriptive keyword (not the brand slogan), Open Graph and Twitter tags, breadcrumbs, and JSON-LD.

JSON-LD by page: Home/About `EducationalOrganization` + `WebSite` with one reused `@id` and `sameAs`; program pages `Course` + `CourseInstance` (`courseMode`, `courseWorkload`, INR `offers`, `provider`) and `EducationalOccupationalProgram`; blog `Article` with `Person` author; all pages `BreadcrumbList`. `FAQPage` only for visible FAQs (Google no longer shows FAQ rich results since 7 May 2026; it still helps answer engines). Validate with the Rich Results Test.

robots.txt: allow OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot, Claude-User; training bots (GPTBot, ClaudeBot, Google-Extended) are an owner decision; disallow `/api/`; list `sitemap-index.xml`. Check Cloudflare AI Crawl Control matches. llms.txt is optional and Google ignores it.

Content: answer-first definitional H2s ("What is AI for school students?"), grade and city modifiers, INR prices in visible text, honest outcome language. Budgets: LCP ≤ 1.8 s, INP ≤ 150 ms, CLS ≤ 0.1.
