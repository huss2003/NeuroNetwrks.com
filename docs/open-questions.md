# Open questions

Every unconfirmed fact lives here. On the site it appears as `{{CONFIRM: ...}}` and blocks a production build.

## Owner inputs needed

| # | Question | Needed by | Status |
|---|---|---|---|
| 1 | Vector logo (SVG/AI/PDF). Only a JPG exists (`docs/source/logo.jpg`); a traced SVG will be provisional | Phase 1 | open |
| 2 | Official public names of all six programs. Is "Neuromind" a public product name? Which certifications does the foundation program align to (docs mention Microsoft AI-901 and AWS AIF-C01)? | Phase 2 | open |
| 3 | Real photography of students, professionals, mentors, labs | Phase 3 | open |
| 4 | Team and faculty names, photos, credentials (or omit section) | Phase 3 | open |
| 5 | Contact email, phone, address, grievance officer, social profile URLs | Phase 3 | open |
| 6 | Admissions steps, eligibility, intake dates, batch sizes, certification details | Phase 3 | open |
| 7 | AI training-bot policy: allow or block GPTBot, ClaudeBot, Google-Extended | Phase 5 | open |
| 8 | aikolearn.com: confirm the correct URL | Phase 5 | open |
| 9 | Correct GitHub repo URL (`huss2003/NeuroNetwrks.com` returned 404; private or misspelled) | Phase 0 | open |
| 10 | Accounts: GitHub, Cloudflare + API token, Turnstile, Google Cloud service account, GA4, Search Console, Bing, Resend (see PLAN.md section 15) | Phase 6-10 | open |

## Content gaps found while building
_None yet._

## Added in Phase 2 (content model)

12. **AI-900 is retired.** The 1-year course document says AI-900 retired on 30 June 2026 and must not be advertised as current, but the 3-year AI/ML document still lists "AI-900 / AI-901". Site copy uses AI-901 only for the foundation course; the AI/ML program page lists the roadmap as written. Confirm the intended certification for the AI/ML track.
13. **Certification costs are in the curriculum documents** (for example approximate rupee figures and a total for the six). The site shows no prices, so these were left out. Confirm whether any may ever be shown.
14. **Earning potential and employment sections** in the 3-year documents (salary ranges, freelancing, remote work) were not used. The site makes no salary or placement claims. Confirm if any should appear, with sources.
15. **Hardware requirements are high for some programs** (for example Data Science & AI lists 32 GB RAM, 1 TB SSD and a dedicated 8 GB GPU). Confirm these are minimums for parents to see.
16. **Product & UX document names no design tools.** The tools list is empty apart from GitHub. Which tools (for example design and prototyping software) are used?
17. **Program names** are taken from the document titles. Confirm the public names, and whether "Neuromind" (file name only) is a public brand.
18. **Delivery mode** (online, in person, hybrid), batch timings and who responds to enquiries: not in the documents.
19. **Professionals and schools offers:** the documents are for Class 10 entrants and a teacher-ready foundation course. Is there an offer for working professionals, and may schools adopt the foundation course? Both pages hold `{{CONFIRM}}` placeholders until answered.
20. **Faculty:** who teaches? The FAQ holds a placeholder.

## Added in Phase 5 (SEO)

21. **Social profile URLs** (LinkedIn, YouTube, Instagram, X) for `sameAs` and entity clarity. None are emitted until confirmed.
22. **AI training bots:** the site currently allows GPTBot, ClaudeBot and Google-Extended (default in the plan). Confirm or tell me to block them (open question 9 still stands).
23. **Named authors and short bios** for guides and the About page (E-E-A-T). Nothing is invented.
24. **Google Business Profile:** only if there is a physical centre. Is there?

## Owner answers (15 Oct 2026)

- **Certificate:** every program awards a NeuroNetworks AI Ed certificate on completion. Shown on program pages and in the Course schema (`educationalCredentialAwarded`). Answers the diploma question: these are certificate programs.
- **Q12 AI-900:** use AI-901 only. The AI/ML program data now says AI-901.
- **Q17 Program names:** the six names on the site are the official names. "Neuromind" is no longer used; the brand is NeuroNetworks. The only remaining mention is the source file name in `docs/source/`, which stays unchanged.
- **Q19 Professionals and schools:** there is no offer for working professionals. The professionals audience page is not built.
- **Q15 Hardware:** the laptop specifications are recommendations, not entry requirements. The site wording now says so.
- **Q13 Certification costs:** never shown.
- **Q14 Earning potential:** show it as indicative ranges, never guaranteed. The salary bands come from each 3-year curriculum document. They appear on the five 3-year program pages and the related guides, with a disclaimer. The AI Foundation document has no salary table, so none is shown. Freelance rates appear only for AI/ML, Software and UX, because the Cyber and Data Science documents copy the AI/ML freelance text.
- **Q20 Faculty:** the Faculty and Team page is hidden for now. `/faculty-and-team` redirects to `/about` with a 308, and the "Who teaches?" FAQ is removed. To restore it, add `write("/faculty-and-team", team_page())` back to `main()` in build.py.

## Updated curricula (15 Oct 2026)

The owner supplied four updated ("FIXED") curriculum documents, now in `docs/source/` and `docs/extracted/`. They are the source for these programs:

- **AI Foundation** (`AI_Creator_Program_104Hours_FIXED`):
  - The document title is "AI Foundations, AI Application & AI Creator Program". The public name stays **AI Foundation** (owner decision).
  - Entry is now **Class 8+**, for this course only. The 3-year programs stay Class 10.
  - New module titles for Months 8–12, new hours per month (4, 4, 10, 8, 10, 6, 8, 7, 8, 9, 12, 18) and new monthly projects.
  - Certification prep moved into Month 12.
  - The old "80% pass mark" is gone; the new model has unit exams, practicals, mock exams and a capstone.
- **AI/ML Engineering:**
  - Modules unchanged.
  - DeepLearning.AI ML Specialization removed, because it no longer appears in the document.
  - AWS certification shown as AIF-C01.
  - Month 36 project is now "Final Professional AI/ML Capstone Project".
- **Data Science & AI:**
  - DP-100 (retired 1 June 2026) replaced by Microsoft AI-300 (MLOps Engineer Associate).
  - The Month 20 module is shown as "Azure ML & AI-300 Preparation". The document's table still says DP-100, but its text says AI-300 is taught in its place.
  - HackerRank shown as Python & SQL Certificates.
- **Product & UX / AI Design:** no data change; the site already matched. The NN/g cost is not shown.
- The new documents have no tools, careers, salary or hardware sections, so the existing values remain.
- Software Development and Cybersecurity were not updated, because no new documents were supplied for them.
