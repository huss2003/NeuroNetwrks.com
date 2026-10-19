# Career page data spec ("how to become [role] after 10th")

Each role is ONE JSON file in this folder, named `<slug>.json`. The site generator turns it into a full page
(layout, roadmap from program data, laptop, salary table, parents' questions, shared sources, schema).
The reference example is `become-software-engineer-after-10th.json`. Match its fields, depth and tone exactly.

## Reader and goal
- Reader: a Class 10 student in India and their parent, reading together. English (India).
- Goal: the reader clicks "Talk to us" or "Apply" for the mapped program. The pitch is gentle and inside the content.
- Unique angle: a year-by-year roadmap built from the real 624-hour (or 104-hour) curriculum, real projects, an honest "not for you if".

## Facts: use ONLY these sources (never invent)
- Program facts: `/home/user/NeuroNetwrks.com/site-preview/llms-full.txt` (modules, projects, certifications, tools, roles, salary, laptop).
  Project names in "projects" MUST be copied exactly from that program's "Projects:" list.
  Certification names in "cert_notes" keys MUST match that program's certification list exactly.
- All 3-year programs: 624 hours, 4 hours a week, 208 hours a year, 36 monthly modules, 1-hour exam after each module (inside the 624 h),
  entry Class 10 pass. AI Foundation: 1 year, 104 hours, 2 hours a week, open from Class 8, no coding needed.
- Classes are online. Batch timings: "shared on enquiry". Under-18s enquire/apply through a parent or guardian.
- Every month: theory, demonstration, hands-on lab, a project, then the exam (3-year programs).
- Students receive a Neuronetworks AI Ed certificate on completion (a certificate, NOT a degree).
- External certifications: preparation only, awarded by the certifying bodies, passing not guaranteed, NEVER mention their costs.
- Salary: only the program's indicative India ranges (fresher, 3–5 years, senior) from llms-full.txt, always "indicative, not a promise".
- No job, internship, salary or exam-pass guarantee. No student numbers, success rates, testimonials, ratings, placements, partners, faculty names.
- B.Tech via JEE Main (NTA JEE Main 2026 Information Bulletin, sec 5.8.1): Class 12 needs Physics, Mathematics, a language, one of
  Chemistry/Biotechnology/Biology/Technical vocational, and one more subject. State colleges can set their own rules.
- Nasscom Strategic Review 2026 (Feb 2026): India tech industry $315 bn revenue, employment near 6 million, AI moved from optional to core
  infrastructure, cloud-native architecture widespread, cybersecurity rising with AI-powered threats. Use at most one such line per page ("context_fact").
- If the program does NOT teach something the role needs (e.g. game engines, native mobile apps), say so plainly in "fit_note" and in the
  roadmap framing. Never imply the program covers it.

## Fresh data (required per page)
- Use WebSearch/WebFetch to find 1 to 3 CURRENT official sources specific to this role (official certification pages from Microsoft, AWS,
  Google/Coursera, CompTIA, ISC2, EC-Council, IxDF, NN/g, Oracle, IBM, NVIDIA; or Indian government/industry pages).
  Open each page you cite. Put them in "sources" as [title, url, "Publisher, checked 18 October 2026" or the page's own updated date].
  Only state facts you read on those pages. If a page cannot be opened, do not cite it.
  The template already adds shared sources (JEE bulletin, Nasscom, the program page). Do not repeat them.

## Writing rules
- Plain words, short sentences (under 25 words), active voice, sentence case. Indian English (programme spelling NOT used: write "program").
- NO em dashes (—) anywhere. Use commas, colons or full stops. En dash only inside number ranges (₹4–8) and official names.
- Never use: unlock, revolutionise/revolutionize, cutting-edge, seamless, journey, dive, delve, game-changer, unleash, empower.
- No fees or prices of any program. CTAs are only "Apply" and "Talk to us" (the template adds them).
- Each page must be genuinely different from its siblings (e.g. AI engineer vs ML engineer vs AI developer): different role definition,
  different stream advice, different skill table, different project picks and reasons, different not-for-you, different FAQs.
- "start_answer", "roadmap_answer", "skills_answer", "build_answer", "certs_answer", "notfor_answer", "salary_answer": ONE sentence that
  directly answers the section question (the H2 is a question). 20 to 45 words.
- FAQ: exactly 5. Must include "How many years does it take to become a/an [role] after 10th?" and "Can I become a/an [role] without maths?".
- "title" ≤ 60 characters, "desc" ≤ 155 characters. Title pattern: "How to Become a/an [Role] After 10th (2026)" (shorten if needed).
- HTML allowed only: <strong> in in_short; <a href="/programs/..."> or <a href="/guides/..."> links in start_extra / fit_note / notfor text.

## Fields (all required unless marked optional)
slug, role, keyword, searches (string or ""), program, alt_programs (1-3 program slugs), title, desc, h1 [line1, line2], lead, role_intro,
in_short [3], start_answer, start_bridge, streams [[path, keeps open, watch out] x3], start_extra, roadmap_answer, year_focus [3 strings
"Year N: ..."] (for ai-foundation: 1 string), fit_note (optional, "" if none), skills_answer, skills [[skill, why it matters, when you learn it]] 7-11,
build_answer, projects [[exact project name, why it matters for THIS role]] 6-8, certs_answer, cert_notes {exact cert name: short note
from the source page} (optional entries), cert_extra (optional), notfor_answer, notfor [[bold lead, sentence]] 5-6, salary_answer,
faqs [[q, a]] x5, context_fact, sources [[title, url, date note]] 1-3, related_guides [existing /guides slugs, 2-3].

Existing guide slugs: ai-courses-after-10th, courses-after-10th, computer-coding-courses-after-10th, cyber-security-course-after-10th,
data-science-after-10th, ai-vs-software-vs-data-science, ai-projects-for-students, career-options-after-10th, plus every career slug.
Program slugs: ai-foundation, ai-ml-engineering, software-development, data-science-ai, product-ux-ai-design, cybersecurity.

## Validate before finishing
python3 /home/user/NeuroNetwrks.com/tools/preview-gen/careers/check.py <slug>.json   (must print OK)

## Originality pass (Oct 2026): extra role-specific fields
- "day_to_day": {"answer": one sentence 20-45 words, "html": 2-3 short <p> paragraphs}. Rendered as H2 "What does a/an [role] do day to day?" (first section).
  Cover: what the work is day to day (tasks, who they work with), the main tools named for this role, and one paragraph
  "How it differs from <closest sibling role>". No invented statistics, salaries, companies or India-specific numbers unless from a source you opened.
- "first_project": {"answer": one sentence, "html": 1-2 <p> with a concrete, realistic first project a student can do at home in 1-3 weeks,
  its steps, and which real program project it leads to (exact name from llms-full.txt)}. Rendered as H2 "What is a realistic first project for a future [role]?".
- Rewrite "in_short" (3 bullets) and "start_answer" so they are specific to THIS role and not interchangeable with sibling pages.
- Allowed HTML in html fields: <p>, <strong>, <ul><li>, links to /programs/... or /guides/... (only slugs that exist in careers/*.json, guides_pages.py or seo/).
