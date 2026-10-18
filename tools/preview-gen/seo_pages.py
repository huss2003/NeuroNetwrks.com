# Programmatic SEO engine: one renderer for ANY keyword pattern. exec'd from build.py after career_pages.py (shares its namespace).
# Pages live in seo/<pattern>/<slug>.json. Each file is a list of question sections made of typed blocks (see
# .claude/skills/programmatic-seo-page/references/blocks.md). Program facts come from D / SALARY via "program_*" blocks,
# never from the JSON, so pages stay in step with the curriculum. The career roadmaps (careers/) use their own older renderer.

SEO_DIR = os.path.join(HERE, "seo")
SEO_PATTERNS = {}  # pattern slug -> {"name", "intro", "pages": [...]}
for _f in sorted(glob.glob(os.path.join(SEO_DIR, "*", "*.json"))):
    _p = json.load(open(_f))
    _pat = os.path.basename(os.path.dirname(_f))
    _meta_f = os.path.join(SEO_DIR, _pat, "pattern.json")
    if os.path.basename(_f) == "pattern.json": continue
    _meta = json.load(open(_meta_f)) if os.path.exists(_meta_f) else {"name": _pat.replace("-", " ").capitalize(), "intro": ""}
    SEO_PATTERNS.setdefault(_pat, dict(_meta, pages=[]))["pages"].append(_p)
SEO_BY = {p["slug"]: p for pat in SEO_PATTERNS.values() for p in pat["pages"]}
for _p in SEO_BY.values():
    GUIDE_BY[_p["slug"]] = {"slug": _p["slug"], "title": _p["title"], "desc": _p["desc"]}

def s_inline(x):  # only <strong>, <em> and site links are allowed inside JSON text
    return x

def s_block(b, page):
    t, s = b["type"], page.get("program")
    if t == "p":
        return f'<p>{s_inline(b["html"])}</p>'
    if t == "note":
        return f'<p class="cr-note">{s_inline(b["html"])}</p>'
    if t == "callout":
        return f'<p class="cr-fit">{"<b>" + E(b["label"]) + "</b> " if b.get("label") else ""}{s_inline(b["html"])}</p>'
    if t == "table":
        return c_table(b["head"], [[s_inline(c) for c in r] for r in b["rows"]], b.get("caption", "Table"))
    if t == "list":
        tag = "ol" if b.get("ordered") else "ul"
        items = "".join(f'<li>{"<strong>" + E(i[0]) + "</strong> " if i[0] else ""}{s_inline(i[1])}</li>' for i in b["items"])
        return f"<{tag}>{items}</{tag}>"
    if t == "cards":  # e.g. project ideas: name, meta chips, body, steps
        out = ""
        for i, c in enumerate(b["items"]):
            meta = "".join(f"<li>{E(m)}</li>" for m in c.get("meta", []))
            steps = "".join(f"<li>{s_inline(x)}</li>" for x in c.get("steps", []))
            out += (f'<section class="sp-card" aria-labelledby="sp{i}"><h3 id="sp{i}">{E(c["name"])}</h3>'
                    f'{"<ul class=\"cr-chips\">" + meta + "</ul>" if meta else ""}<p>{s_inline(c["body"])}</p>'
                    f'{"<ol class=\"sp-steps\">" + steps + "</ol>" if steps else ""}'
                    f'{"<p class=\"cr-builds\"><b>In the program:</b> " + s_inline(c["link"]) + "</p>" if c.get("link") else ""}</section>')
        return f'<div class="sp-cards">{out}</div>'
    if t == "program_roadmap":
        c = {"program": s, "year_focus": b.get("year_focus", []), "projects": [[p, ""] for p in b.get("highlight", [])]}
        return c_beats(c) + c_years(c)
    if t == "program_note":
        return f'<p class="cr-prog">{c_program_note({"program": s})}</p>'
    if t == "talk":
        return c_talk(b.get("h", "Not sure which path fits?"), b.get("p", "Ask us about the modules, batch timings and fees. A person replies. Students under 18 enquire through a parent or guardian."))
    if t == "program_certs":
        notes = b.get("notes", {})
        cl = "".join(f'<li><strong>{E(c_clean(x))}.</strong>{" " + E(notes[x]) if x in notes else ""}</li>' for x in D[s]["certifications"])
        return f'<p>The {E(c_prog_name(s))} program prepares students for these {len(D[s]["certifications"])}. Each is awarded by its own certifying body after its own exam, and passing is not guaranteed.</p><ul>{cl}</ul>'
    if t == "program_laptop":
        hw = "".join(f"<li>{E(c_clean(x))}</li>" for x in D[s]["hardware"])
        return f'<ul>{hw}</ul><p class="cr-note">These are recommendations, not entry requirements. A phone alone is not enough for the labs.</p>'
    if t == "program_salary":
        sp = c_salary_prog({"program": s, "alt_programs": page.get("alt_programs", [])})
        if not sp: return ""
        bnd = SALARY[sp][0]
        return c_table(["Experience", "Indicative range (per year)"], [["Fresher", bnd[0]], ["3–5 years", bnd[2]], ["Senior", bnd[-1]]], "Indicative salary in India") + f'<p class="cr-note">{SAL_SHORT}</p>'
    if t == "parents":
        pq = [("Can I see the whole curriculum, month by month?", "A good course shows every module and its hours before you pay."),
              ("What will my child build, and where will I see it?", "Ask for project names and whether work goes on GitHub."),
              ("How is learning checked, and how often?", "Regular exams and practicals show progress early, not only at the end."),
              ("Who answers questions, and how quickly?", "Ask how doubts are handled between classes."),
              ("What is promised, and what is not?", "Get the certificate, timings and fees in writing. Be careful of anyone who guarantees a job or salary.")]
        return "<ol>" + "".join(f"<li><strong>{q}</strong> {x}</li>" for q, x in pq) + "</ol>"
    if t == "jee":
        return f"<p>{E(JEE_LINE)}</p>"
    raise ValueError(f"{page['slug']}: unknown block type {t}")

def seo_page(slug):
    pg = SEO_BY[slug]; s = pg.get("program")
    secs = [(x["h2"], f'<p class="cr-answer">{E(x["answer"])}</p>' + "".join(s_block(b, pg) for b in x.get("blocks", []))) for x in pg["sections"]]
    faq = f'<section class="gd-sec" id="faq"><h2>Frequently asked questions</h2><div class="faq gd-faq">{faq_items([(E(q), "<p>" + E(a) + "</p>") for q, a in pg["faqs"]], first_open=False)}</div></section>'
    src = [tuple(x) for x in pg["sources"]] + (SHARED_SOURCES if pg.get("shared_sources", True) else []) + (
        [(f"{c_prog_name(s)} program roadmap", f"{SITE}/programs/{s}", "NeuroNetworks AI Ed. Modules, projects, hours, certifications and laptop recommendations.")] if s else [])
    srcs = "".join(f'<li><a href="{E(u)}" rel="noopener">{E(t)}</a>, {E(n)}</li>' for t, u, n in src)
    sources = f'<section class="gd-sec" id="sources"><h2>Sources</h2><p>Checked on {E(pg["date_txt"])}.</p><ul class="cr-sources">{srcs}</ul></section>'
    body_secs = "".join(f'<section class="gd-sec" id="s{i+1}"><h2>{E(h)}</h2>{b}</section>' for i, (h, b) in enumerate(secs))
    toc = "".join(f'<li><a href="#s{i+1}">{E(h)}</a></li>' for i, (h, _) in enumerate(secs))
    tldr = "".join(f"<li>{x}</li>" for x in pg["in_short"])
    progs = ([s] if s else []) + pg.get("alt_programs", [])[:2]
    rel_p = "".join(f'<a class="gd-card" href="/programs/{x}"><small>{prog(x)[4]} · {prog(x)[3]} hours</small><strong>{E(prog(x)[2])}</strong><span>{E(D[x]["summary"])}</span></a>' for x in progs)
    rel_g = "".join(f'<li><a href="/guides/{g}">{E(GUIDE_BY[g]["title"])}</a></li>' for g in pg.get("related_guides", []) if g in GUIDE_BY and g != slug)
    mins = guide_minutes(body_secs + faq)
    hero = f'''<section class="page-hero gd-hero"><div class="wrap"><div><p class="crumbs"><a href="/">Home</a> / <a href="/guides">Guides</a> / {E(pg["h1"][0])}</p>
<h1>{headline(E(pg["h1"][0]), E(pg["h1"][1]))}</h1><p class="lead">{E(pg["lead"])}</p>
<p class="gd-meta">By the NeuroNetworks AI Ed team · Updated <time datetime="{pg["date"]}">{E(pg["date_txt"])}</time> · {mins} min read</p></div></div></section>'''
    body = f'''{hero}<div class="wrap gd-wrap"><aside class="gd-toc" aria-label="On this page"><p>On this page</p><ol>{toc}<li><a href="#faq">FAQs</a></li><li><a href="#sources">Sources</a></li></ol></aside>
<article class="gd-art"><div class="gd-tldr"><h2>In short</h2><ul>{tldr}</ul></div>{"<p class=\"cr-intro\">" + E(pg["intro"]) + "</p>" if pg.get("intro") else ""}{body_secs}{faq}{sources}
{"<section class=\"gd-sec\"><h2>Programs in this guide</h2><div class=\"gd-cards\">" + rel_p + "</div></section>" if rel_p else ""}
{"<section class=\"gd-sec gd-more\"><h2>Related guides</h2><ul>" + rel_g + "</ul></section>" if rel_g else ""}</article></div>{cta_panel(pg.get("cta_h", "Questions about the right path?"), pg.get("cta_p", "Tell us what the student enjoys. We will explain the program, timings and fees."))}'''
    ld = {"@type": "Article", "@id": f"{SITE}/guides/{slug}#article", "headline": pg["title"], "description": pg["desc"], "image": SITE + "/assets/og.png",
          "datePublished": pg["date"], "dateModified": pg.get("modified", pg["date"]), "inLanguage": "en-IN",
          "author": {"@type": "Organization", "name": "NeuroNetworks AI Ed team", "url": SITE + "/about"}, "publisher": {"@id": ORG_ID},
          "mainEntityOfPage": f"{SITE}/guides/{slug}", "mentions": [{"@id": f"{SITE}/programs/{x}#course"} for x in progs],
          "citation": [u for _, u, _ in src if u.startswith("http")]}
    if pg.get("about"): ld["about"] = pg["about"]
    return layout(f"/guides/{slug}", pg["title"], body, "resources", desc=pg["desc"], jsonld=ld)

_guides_index_careers = guides_index
def guides_index():
    html = _guides_index_careers()
    extra = ""
    for pat in SEO_PATTERNS.values():
        cards = "".join(f'<a class="gd-card" href="/guides/{p["slug"]}"><small>{E(c_prog_name(p["program"])) if p.get("program") else "Guide"}</small><strong>{E(p["h1"][0])}</strong><span>{E(p["desc"])}</span></a>' for p in pat["pages"])
        extra += f'<section class="sec"><div class="wrap">{sec_head(E(pat["name"]), E(pat.get("headline", pat["name"])), E(pat.get("intro", "")))}<div class="gd-cards gd-cards--3">{cards}</div></div></section>'
    return html.replace('<section class="sec sec--tint">', extra + '<section class="sec sec--tint">', 1) if extra else html

for _p in SEO_BY.values():
    if _p.get("program"):
        PROG_GUIDES[_p["program"]] = list(dict.fromkeys(PROG_GUIDES.get(_p["program"], []) + [_p["slug"]]))
GUIDE_PAGES["/guides"] = guides_index
GUIDE_PAGES.update({f"/guides/{slug}": (lambda s=slug: seo_page(s)) for slug in SEO_BY})
