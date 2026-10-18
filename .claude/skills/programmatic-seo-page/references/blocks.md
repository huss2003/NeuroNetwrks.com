# Page JSON and blocks (seo_pages.py)

Top-level fields:
| Field | Notes |
|---|---|
| slug | URL is /guides/<slug>. File must be named <slug>.json |
| keyword, searches | target keyword; monthly searches as text or "" |
| program, alt_programs | program slug that the page leads to (or omit for a non-program page); up to 3 alternatives |
| date, date_txt, modified | "2026-10-18", "18 October 2026"; `modified` optional |
| title (≤60), desc (≤155) | used for <title>, meta description, OG, Article schema |
| h1 | [line 1, line 2 shown in blue] |
| lead | 1 to 2 sentences under the H1 |
| intro | optional paragraph after the In short box |
| in_short | exactly 3 bullets; <strong> allowed |
| sections | list of {h2 (a question), answer (one sentence, 15 to 50 words), blocks: [...]} |
| faqs | exactly 5 [question, answer] pairs; must include pattern.json `required_faq` words |
| sources | 1 to 3 [title, https url, "Publisher, checked DD Month YYYY"] that you opened |
| shared_sources | true adds the JEE Main 2026 bulletin and Nasscom 2026 review (career-type pages); false for others |
| related_guides | 2 to 3 existing guide slugs |
| cta_h, cta_p | closing panel heading and line (optional) |
| about | optional schema.org `about` list, e.g. [{"@type":"Occupation","name":"Data analyst"}] |

Blocks (HTML allowed inside `html`, table cells, list text and card text: <strong>, <em>, <a href="/programs/..."> or <a href="/guides/...">):
| type | fields | renders |
|---|---|---|
| p | html | paragraph |
| note | html | small grey note |
| callout | html, label (optional, e.g. "What this program does not cover:") | bordered honest-gap box |
| table | head [..], rows [[..]], caption | site table |
| list | ordered (bool), items [[bold lead or "", text]] | ul/ol |
| cards | items [{name, meta [chips], body, steps [..], link (optional, "In the program: ...")}] | idea/project cards |
| program_roadmap | year_focus [one per year], highlight [exact project names] | monthly steps strip + year blocks with modules |
| program_note | | "If you want to follow this with a mentor..." paragraph with program link |
| talk | h, p (optional) | blue Talk to us / Apply box. Put it right after program_note |
| program_certs | notes {exact cert name: note from a source you opened} | certification list with not-guaranteed line |
| program_laptop | | recommended laptop list + note |
| program_salary | | indicative salary table + note (falls back to an alt program with a salary table) |
| parents | | 5 questions parents should ask |
| jee | | B.Tech subject rule from the JEE Main 2026 bulletin |
