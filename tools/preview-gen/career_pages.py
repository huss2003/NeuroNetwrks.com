# Career roadmap pages: "how to become [role] after 10th". exec'd from build.py after guides_pages.py (shares its namespace).
# One JSON file per role in careers/ (spec: careers/SPEC.md). Program facts (modules, projects, certifications, laptop, salary)
# always come from the program data D / SALARY, never from the JSON, so every page stays in step with the curriculum.

CAREER_DATE, CAREER_DATE_TXT = "2026-10-18", "18 October 2026"
CAREERS = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(HERE, "careers", "*.json")))]
CAREER_BY = {c["slug"]: c for c in CAREERS}

# The two older guides on these slugs are replaced by their career-roadmap versions.
GUIDES[:] = [g for g in GUIDES if g["slug"] not in CAREER_BY]
for c in CAREERS:
    GUIDE_BY[c["slug"]] = {"slug": c["slug"], "title": c["title"], "desc": c["desc"]}

SHARED_SOURCES = [
    ("JEE (Main) 2026 Information Bulletin", "https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2025/11/202511021649722475.pdf",
     "National Testing Agency, November 2025. Class 12 subjects for B.E. and B.Tech admission through JEE Main (section 5.8.1)."),
    ("Technology Sector in India: Strategic Review 2026", "https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026",
     "Nasscom, February 2026. Industry revenue, employment and technology trends."),
]
JEE_LINE = ("For the NITs and other institutes that fill B.E. and B.Tech seats through JEE Main, the 2026 rules ask for Physics, Mathematics, a language, "
            "one of Chemistry, Biotechnology, Biology or a technical vocational subject, and one more subject in Class 12. State colleges can set their own rules.")
SAL_SHORT = ("Indicative market ranges, not a promise. Pay depends on employer, city, role and skills, and for some employers, a degree. "
             "Neuronetworks AI Ed does not guarantee a job, internship or salary.")

def c_clean(s):  # program data keeps em dashes from the source documents; the guides never show them
    return s.replace(" — ", ": ").replace("—", ", ")

def c_art(role):
    return "an" if role[:1].lower() in "aeio" else "a"

def c_prog_name(slug):
    return prog(slug)[2]

def c_program_note(c):
    s, d = c["program"], D[c["program"]]
    link = f'<a href="/programs/{s}">{E(c_prog_name(s))} program</a>'
    if s == "ai-foundation":
        return (f"If you want to follow this roadmap with a mentor and a project most months, the six-month {link} covers it: 104 hours, online, "
                f"4 hours a week for 26 weeks. It is open from Class 9, and no coding experience is needed. Students receive a Neuronetworks AI Ed certificate on completion.")
    return (f"If you want to follow this roadmap with a mentor and a project every month, the 3-year {link} covers these three years: 624 hours, online, "
            f"4 hours a week, with a 1-hour exam after each of the 36 monthly modules. It is open to anyone from Class 11 onwards"
            f"{' (' + E(c_clean(d['entry'].split(';', 1)[1].strip())) + ')' if ';' in d['entry'] else ''}. Students receive a Neuronetworks AI Ed certificate on completion.")

def c_years(c):
    d = D[c["program"]]
    picks = {p for p, _ in c["projects"]}
    out = ""
    for i, y in enumerate(d["years"]):
        focus = c["year_focus"][i] if i < len(c["year_focus"]) else y["title"]
        projs = d["projects"][i * 12:(i + 1) * 12] if len(d["years"]) > 1 else d["projects"]
        mine = [p for p in projs if p in picks] or projs[:3]
        chips = "".join(f"<li>{E(c_clean(m))}</li>" for m in y["modules"])
        out += (f'<section class="cr-year" aria-labelledby="cy{i+1}"><p class="cr-yhead"><strong>{"Year " + str(i+1) if len(d["years"]) > 1 else "6 months"}</strong>'
                f'{y["hours"]} hours · {len(y["modules"])} modules</p><div><h3 id="cy{i+1}">{E(focus)}</h3><ul class="cr-chips">{chips}</ul>'
                f'<p class="cr-builds"><b>You build:</b> {g_join([c_clean(p) for p in mine])}.</p></div></section>')
    return f'<div class="cr-road">{out}</div>'

def c_beats(c):
    if c["program"] == "ai-foundation":
        steps = [("Lecture", "1 hour"), ("Homework", "10 to 15 minutes"), ("Project", "Most modules"), ("Unit exam", "30 questions"), ("Capstone", "Final module")]
    else:
        steps = [("Step 1", "Theory"), ("Step 2", "Demonstration"), ("Step 3", "Hands-on lab"), ("Step 4", "A project"), ("Step 5", "A 1-hour exam")]
    return '<ol class="cr-beats" aria-label="How each month works">' + "".join(f"<li><span>{a}</span>{b}</li>" for a, b in steps) + "</ol>"

def c_talk(h, p):
    return (f'<aside class="cr-talk" aria-label="{E(h)}"><div><h3>{E(h)}</h3><p>{E(p)}</p></div>'
            f'<div class="cr-talk-btns"><a class="le-btn le-btn--w" href="/contact">Talk to us {ARW}</a><a class="le-btn le-btn--g" href="/admissions">Apply</a></div></aside>')

def c_table(head, rows, cap):
    th = "".join(f'<th scope="col">{E(h)}</th>' for h in head)
    tr = "".join("<tr>" + "".join((f'<th scope="row">{x}</th>' if j == 0 else f"<td>{x}</td>") for j, x in enumerate(r)) + "</tr>" for r in rows)
    return f'<div class="gd-table"><table><caption class="vh">{E(cap)}</caption><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

def c_salary_prog(c):
    for s in [c["program"]] + c.get("alt_programs", []):
        if s in SALARY: return s
    return None

def career_page(slug):
    c = CAREER_BY[slug]; s = c["program"]; d = D[s]; role = c["role"]; a = c_art(role)
    secs = []
    # 0 role-specific: what the work is day to day (Oct 2026 originality pass)
    if c.get("day_to_day"):
        secs.append((f"What does {a} {role} do day to day?", f'<p class="cr-answer">{E(c["day_to_day"]["answer"])}</p>' + c["day_to_day"]["html"]))
    # 1 can you start
    rows = [[E(x), E(y), E(z)] for x, y, z in c["streams"]]
    secs.append((f"Can you start on the path to {a} {role} right after Class 10?",
        f'<p class="cr-answer">{E(c["start_answer"])}</p><p>{E(c["start_bridge"])}</p>'
        + c_table(["Path after 10th", "What it keeps open", "Watch out for"], rows, "Stream choices after Class 10")
        + f"<p>{E(JEE_LINE)}</p><p>{c['start_extra']}</p>"))
    # 2 roadmap + program + talk box
    fit = f'<p class="cr-fit"><b>What this program does not cover:</b> {c["fit_note"]}</p>' if c.get("fit_note") else ""
    yrs = "three years" if len(d["years"]) > 1 else "six months"
    secs.append((f"What is the {'year-by-year' if len(d['years']) > 1 else 'step-by-step'} roadmap to become {a} {role}?",
        f'<p class="cr-answer">{E(c["roadmap_answer"])}</p><p>Each {"year is 208 hours, split into 12 monthly modules. Every month follows the same five steps, so a student always knows what comes next." if len(d["years"]) > 1 else "month has weekly lectures with short homework, and every major unit ends with an exam."}</p>'
        + c_beats(c) + c_years(c) + f'<p class="cr-prog">{c_program_note(c)}</p>' + fit
        + c_talk(f"Not sure if this roadmap fits?", f"Ask us about the modules, batch timings and fees. A person replies. Students under 18 enquire through a parent or guardian.")))
    # 3 skills
    secs.append((f"Which skills does {a} {role} need?",
        f'<p class="cr-answer">{E(c["skills_answer"])}</p><p>{E(c["context_fact"])}</p>'
        + c_table(["Skill", "Why it matters", "When you learn it"], [[E(x), E(y), E(z)] for x, y, z in c["skills"]], "Skills and when they are learned")))
    # 4 build
    items = "".join(f"<li><strong>{E(c_clean(p))}.</strong> {E(w)}</li>" for p, w in c["projects"])
    secs.append(("What will you build on the way?",
        f'<p class="cr-answer">{E(c["build_answer"])}</p><p>These are real projects from the {E(c_prog_name(s))} roadmap, in the order a student meets them:</p><ol>{items}</ol>'
        f'<p>A parent can open the GitHub page at any time and see the work. That is often more convincing than a marksheet.</p>'))
    if c.get("first_project"):
        secs.append((f"What is a realistic first project for a future {role}?", f'<p class="cr-answer">{E(c["first_project"]["answer"])}</p>' + c["first_project"]["html"]))
    # merged sections from retired low-demand role pages (Oct 2026), kept where they are genuinely unique
    for x in c.get("merged_sections", []):
        secs.append((x["h2"], f'<p class="cr-answer">{E(x["answer"])}</p>' + x["html"]))
    # 5 certificates
    notes = c.get("cert_notes", {})
    cl = "".join(f'<li><strong>{E(c_clean(x))}.</strong>{" " + E(notes[x]) if x in notes else ""}</li>' for x in d["certifications"])
    secs.append((f"Which certificates help {a} future {role}?",
        f'<p class="cr-answer">{E(c["certs_answer"])}</p><p>The {E(c_prog_name(s))} program prepares students for these {len(d["certifications"])}. Each is awarded by its own certifying body after its own exam, and passing is not guaranteed.</p><ul>{cl}</ul>'
        + (f'<p class="cr-note">{E(c["cert_extra"])}</p>' if c.get("cert_extra") else "")))
    # 6 laptop
    hw = "".join(f"<li>{E(c_clean(x))}</li>" for x in d["hardware"])
    secs.append((f"What laptop do you need to become {a} {role}?",
        f'<p class="cr-answer">You need a laptop or desktop with internet, because a phone alone is not enough for the labs. This is the setup recommended for the {E(c_prog_name(s))} program.</p>'
        f'<ul>{hw}</ul><p class="cr-note">These are recommendations, not entry requirements. Ask us if your current computer is enough to start.</p>'))
    # 7 not for you
    nf = "".join(f"<li><strong>{E(x)}</strong> {y}</li>" for x, y in c["notfor"])
    alts = [x for x in ["ai-foundation", "ai-ml-engineering", "software-development", "data-science-ai", "product-ux-ai-design", "cybersecurity"] if x != s]
    secs.append(("Who should not choose this path?",
        f'<p class="cr-answer">{E(c["notfor_answer"])}</p><ul class="cr-notfor">{nf}</ul>'
        f'<p>Other paths to compare: {", ".join(g_prog_link(x) for x in alts)}.</p>'))
    # 8 parents
    pq = [("Can I see the whole curriculum, month by month?", "A good course shows every module and its hours before you pay."),
          ("What will my child build, and where will I see it?", "Ask for project names and whether work goes on GitHub."),
          ("How is learning checked, and how often?", "Regular exams and practicals show progress early, not only at the end."),
          ("Who answers questions, and how quickly?", "Ask how doubts are handled between classes."),
          ("What is promised, and what is not?", "Get the certificate, timings and fees in writing. Be careful of anyone who guarantees a job or salary.")]
    secs.append(("What should parents ask before choosing a course?",
        '<p class="cr-answer">Parents should ask five things of any course: can I see the full curriculum, what will my child build, how is learning checked, who answers questions, and what exactly is promised.</p><ol>'
        + "".join(f"<li><strong>{q}</strong> {x}</li>" for q, x in pq) + "</ol>"))
    # 9 salary
    sp = c_salary_prog(c)
    if sp:
        b = SALARY[sp][0]
        tbl = c_table(["Experience", "Indicative range (per year)"], [["Fresher", b[0]], ["3–5 years", b[2]], ["Senior", b[-1]]], "Indicative salary in India")
        lbl = "" if sp == s else f'<p>No salary range is published for {E(c_prog_name(s))}. These are the ranges for {g_prog_link(sp)} roles, the usual next step.</p>'
        secs.append((f"What can {a} {role} earn in India?", f'<p class="cr-answer">{E(c["salary_answer"])}</p>{lbl}{tbl}<p class="cr-note">{SAL_SHORT}</p>'))
    # faq
    faq = f'<section class="gd-sec" id="faq"><h2>Frequently asked questions</h2><div class="faq gd-faq">{faq_items([(E(q), "<p>" + E(x) + "</p>") for q, x in c["faqs"]], first_open=False)}</div></section>'
    # sources
    src = [(t, u, n) for t, u, n in c["sources"]] + SHARED_SOURCES + [(f"{c_prog_name(s)} program roadmap", f"{SITE}/programs/{s}", "Neuronetworks AI Ed. Modules, projects, hours, certifications and laptop recommendations.")]
    srcs = "".join(f'<li><a href="{E(u)}" rel="noopener">{E(t)}</a>, {E(n)}</li>' for t, u, n in src)
    sources = f'<section class="gd-sec" id="sources"><h2>Sources</h2><p>Checked on {CAREER_DATE_TXT}.</p><ul class="cr-sources">{srcs}</ul></section>'
    # assemble
    body_secs = "".join(f'<section class="gd-sec" id="s{i+1}"><h2>{E(h)}</h2>{b}</section>' for i, (h, b) in enumerate(secs))
    toc = "".join(f'<li><a href="#s{i+1}">{E(h)}</a></li>' for i, (h, _) in enumerate(secs))
    tldr = "".join(f"<li>{x}</li>" for x in c["in_short"])
    rel_p = "".join(f'<a class="gd-card" href="/programs/{x}"><small>{prog(x)[4]} · {prog(x)[3]} hours</small><strong>{E(prog(x)[2])}</strong><span>{E(D[x]["summary"])}</span></a>' for x in [s] + c.get("alt_programs", [])[:2])
    rel_g = "".join(f'<li><a href="/guides/{g}">{E(GUIDE_BY[g]["title"])}</a></li>' for g in c.get("related_guides", []) if g in GUIDE_BY and g != slug)
    sib = [x for x in CAREERS if x["slug"] != slug and (x["program"] == s or s in x.get("alt_programs", []))][:4]
    rel_g += "".join(f'<li><a href="/guides/{x["slug"]}">{E(x["title"])}</a></li>' for x in sib if x["slug"] not in c.get("related_guides", []))
    mins = guide_minutes(body_secs + faq)
    hero = f'''<section class="page-hero gd-hero"><div class="wrap"><div><p class="crumbs"><a href="/">Home</a> / <a href="/guides">Guides</a> / {E(c["h1"][0])}</p>
<h1>{headline(E(c["h1"][0]), E(c["h1"][1]))}</h1><p class="lead">{E(c["lead"])}</p>
<p class="gd-meta">By the Neuronetworks AI Ed team · Updated <time datetime="{CAREER_DATE}">{CAREER_DATE_TXT}</time> · {mins} min read</p></div></div></section>'''
    body = f'''{hero}<div class="wrap gd-wrap"><aside class="gd-toc" aria-label="On this page"><p>On this page</p><ol>{toc}<li><a href="#faq">FAQs</a></li><li><a href="#sources">Sources</a></li></ol></aside>
<article class="gd-art"><div class="gd-tldr"><h2>In short</h2><ul>{tldr}</ul></div><p class="cr-intro">{E(c["role_intro"])}</p>{body_secs}{faq}{sources}
<section class="gd-sec"><h2>Programs in this guide</h2><div class="gd-cards">{rel_p}</div></section>
<section class="gd-sec gd-more"><h2>Related guides</h2><ul>{rel_g}</ul></section></article></div>{cta_panel(f"Ready to plan the next {yrs}?" if len(d["years"]) > 1 else "Ready to start the first year?", "Tell us what the student enjoys. We will explain the program, timings and fees.")}'''
    ld = {"@type": "Article", "@id": f"{SITE}/guides/{slug}#article", "headline": c["title"], "description": c["desc"], "image": SITE + "/assets/og.png",
          "datePublished": CAREER_DATE, "dateModified": CAREER_DATE, "inLanguage": "en-IN",
          "author": {"@type": "Organization", "name": "Neuronetworks AI Ed team", "url": SITE + "/about"}, "publisher": PUBLISHER,
          "mainEntityOfPage": f"{SITE}/guides/{slug}", "about": [{"@type": "Occupation", "name": role[:1].upper() + role[1:]}],
          "mentions": [{"@id": f"{SITE}/programs/{x}#course"} for x in [s] + c.get("alt_programs", [])],
          "citation": [u for _, u, _ in src if u.startswith("http")]}
    return layout(f"/guides/{slug}", c["title"], body, "resources", desc=c["desc"], jsonld=ld)

def guides_index():
    cr = "".join(f'<a class="gd-card" href="/guides/{c["slug"]}"><small>{E(c_prog_name(c["program"]))}</small><strong>{E(c["h1"][0])}</strong><span>{E(c["desc"])}</span></a>' for c in CAREERS)
    cards = "".join(f'<a class="gd-card gd-card--lg" href="/guides/{g["slug"]}"><strong>{E(g["title"])}</strong><span>{E(g["desc"])}</span><em>Read the guide <i aria-hidden="true">→</i></em></a>' for g in GUIDES)
    hero = page_hero("Guides", "Guides for students", "and parents.", "Plain answers to the questions families ask after Class 10: which tech course, which career, how long it takes, what students build and how to choose.")
    body = (hero + f'<section class="sec"><div class="wrap">{sec_head("Career roadmaps", "How to become one, after 10th.", "Year-by-year plans for 20 technology careers, built from real program modules and projects.")}<div class="gd-cards gd-cards--3">{cr}</div></div></section>'
            + f'<section class="sec sec--tint"><div class="wrap">{sec_head("Course guides", "Choosing a course.", "Courses after Class 10, explained with real hours, tools and projects.")}<div class="gd-grid">{cards}</div></div></section>' + cta_panel())
    ld = {"@type": "CollectionPage", "@id": SITE + "/guides#collection", "name": "Guides", "hasPart": [{"@id": f"{SITE}/guides/{x['slug']}#article"} for x in CAREERS + GUIDES]}
    return layout("/guides", "Guides: AI and tech courses after Class 10", body, "resources", desc="Career roadmaps and course guides for students and parents: how to become a software engineer, AI engineer, data scientist and more after Class 10.", jsonld=ld)

for _c in CAREERS:
    PROG_GUIDES.setdefault(_c["program"], [])
for _s, _lst in PROG_GUIDES.items():
    mine = [c["slug"] for c in CAREERS if c["program"] == _s]
    PROG_GUIDES[_s] = list(dict.fromkeys(mine + [g for g in _lst if g in GUIDE_BY]))  # every guide about the field

GUIDE_PAGES = {"/guides": guides_index, **{f"/guides/{g['slug']}": (lambda s=g["slug"]: guide_page(s)) for g in GUIDES},
               **{f"/guides/{c['slug']}": (lambda s=c["slug"]: career_page(s)) for c in CAREERS}}
