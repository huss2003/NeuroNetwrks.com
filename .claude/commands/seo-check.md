---
description: Verify title, description, canonical, H1 and JSON-LD for a page
argument-hint: <route, for example /programs>
---

For `$ARGUMENTS` (default `/`), read the built HTML in `dist/client` and check: one `<h1>`; `<title>` ≤ 60 chars; meta description ≤ 155; absolute canonical without trailing slash; Open Graph and Twitter tags; `BreadcrumbList`; the JSON-LD required for the page type; answer-first first sentence under each H2. Use the `neuronetworks-seo` skill. Report pass or fail per item.
