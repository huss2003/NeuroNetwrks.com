#!/usr/bin/env python3
"""Builds the static Neuronetworks AI Ed preview site into ../../site-preview.
Data comes from src/content (programs and FAQs). Run: python3 tools/preview-gen/build.py
Placeholder strings are kept exactly as before: they are out of scope for this pass."""
import os, re, sys, json, html, shutil, glob
import yaml
sys.path.insert(0, os.path.dirname(__file__))
from art import ART, shot

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "site-preview")
E = html.escape

# ---------------------------------------------------------------- data
PROGRAMS = [  # slug, short key, display name, hours, length, summary override (from roadmap summary)
    ("ai-foundation", "found", "AI Foundation", "104", "6 months"),
    ("ai-ml-engineering", "aiml", "AI/ML Engineering", "624", "3 years"),
    ("software-development", "sw", "Software Development", "624", "3 years"),
    ("data-science-ai", "ds", "Data Science & AI", "624", "3 years"),
    ("product-ux-ai-design", "ux", "Product and UX/UI Design", "624", "3 years"),
    ("cybersecurity", "cy", "Cybersecurity", "624", "3 years"),
]
KEY = {p[0]: p[1] for p in PROGRAMS}
STILL = {"found": "p-found", "aiml": "p-aiml", "sw": "p-sw", "ds": "p-ds", "ux": "p-ux", "cy": "p-cy"}
D = {}
for slug, *_ in PROGRAMS:
    t = open(os.path.join(ROOT, "src/content/programs", slug + ".mdx")).read().split("---")[1]
    D[slug] = yaml.safe_load(t)
FAQ_FILES = sorted(f for f in glob.glob(os.path.join(ROOT, "src/content/faqs/*.yaml")) if not f.endswith("who-teaches.yaml"))  # faculty hidden by owner decision

def conf(s):
    return re.sub(r"\{\{CONFIRM:?\s*(.*?)\}\}", lambda m: "[To be confirmed: " + m.group(1).strip() + "]", s)
def name_of(p): return E(p[2])
def prog(slug): return [p for p in PROGRAMS if p[0] == slug][0]
def modules(slug): return [m for y in D[slug]["years"] for m in y["modules"]]
def aligned(slug): return len(D[slug]["projects"]) == len(modules(slug))
LV = {"foundation": "Beginner", "specialisation": "Specialisation"}

# placeholder strings (unchanged)
FEE = "Shared on enquiry"
FEE_LINE = ""
FEE_LINK = '<a class="tl" href="/contact?topic=fees">Enquire about fees <i aria-hidden="true">→</i></a>'

# ---------------------------------------------------------------- shared pieces
ROUTES = [("programs", "/programs", "Programs"), ("learning", "/learning-experience", "Learning Experience"), ("projects", "/projects", "Projects"),
          ("about", "/about", "About"), ("admissions", "/admissions", "Admissions"), ("resources", "/guides", "Guides")]

def icon(kind):
    paths = {
        "cube": '<path d="M12 2l9 5v10l-9 5-9-5V7l9-5z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
        "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
        "layers": '<path d="M12 3l9 5-9 5-9-5 9-5z"/><path d="M3 13l9 5 9-5" opacity=".6"/>',
        "bars": '<path d="M4 20V13M10 20V8M16 20V11M22 20V4"/>',
        "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
    }
    return f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[kind]}</svg>'

def header(active):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if a == active else ""}>{t}</a>' for a, h, t in ROUTES)
    return f'''<header class="hd"><div class="wrap">
<a class="brand" href="/" aria-label="Neuronetworks AI Ed home"><img src="/assets/mark.webp" alt="" aria-hidden="true" width="97" height="76"><span class="brand-t"><span>Neuronetworks</span><span>AI Ed</span></span></a>
<nav class="nav" id="nav" aria-label="Primary">{links}<a class="nav-cta" href="/contact">Start Learning</a></nav>
<div class="hd-actions"><a class="hd-search" href="/faqs" aria-label="Search the FAQs">{icon("search")}</a><a class="btn btn-primary btn-sm" href="/contact">Start Learning <i aria-hidden="true">→</i></a>
<button class="burger" type="button" aria-expanded="false" aria-controls="nav" aria-label="Open menu"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg></button></div>
</div></header>'''

def footer():
    pl = "".join(f'<li><a href="/programs/{p[0]}">{name_of(p)}</a></li>' for p in PROGRAMS)
    return f'''<footer class="ft"><div class="wrap">
<div class="ft-grid">
<div class="ft-brand"><a class="brand" href="/" aria-label="Neuronetworks AI Ed home"><img src="/assets/mark.webp" alt="" aria-hidden="true" width="153" height="120" loading="lazy"><span class="brand-t brand-t--ft"><span>Neuronetworks</span><span>AI Ed</span></span></a>
<p>AI / Super Intelligence and technology education for a better tomorrow.</p>{SOCIAL_HTML}
</div>
<nav aria-label="Programs"><h2>Programs</h2><ul>{pl}</ul></nav>
<nav aria-label="Company"><h2>Company</h2><ul><li><a href="/about">About</a></li><li><a href="/learning-experience">Learning Experience</a></li><li><a href="/projects">Projects</a></li></ul></nav>
<nav aria-label="Resources"><h2>Resources</h2><ul><li><a href="/guides">Guides</a></li><li><a href="/curriculum">Curriculum</a></li><li><a href="/faqs">FAQs</a></li><li><a href="/programs">Compare programs</a></li></ul></nav>
<div><h2>Admissions and contact</h2><ul><li><a href="/admissions">Admissions</a></li><li><a href="/contact">Contact</a></li></ul><p class="small" style="margin-top:16px"><a href="mailto:Hussain@neuronetwrks.com">Enquire@neuronetwrks.com</a></p><p class="small muted" style="margin-top:6px">Online classes · India</p></div>
</div>
<div class="ft-base"><span>© Neuronetworks AI Ed Private Limited. All rights reserved.</span><nav aria-label="Legal"><a href="/privacy">Privacy Policy</a><a href="/terms">Terms of Service</a>{'<button type="button" class="ft-cookie" data-consent-open>Cookie settings</button>' if GA_ID else ''}{'<button type="button" class="ft-cookie" data-nnbot-show hidden>Show the robot</button>' if NNBOT_ON else ''}</nav><span>Designed for curious minds. Built for what's next.</span></div>
</div></footer>'''

DESC = {
 "/": "Practical AI and technology programs: a 6-month AI course from Class 9 and five 3-year specialisations from Class 11. Project-based, with exams.",
 "/programs": "Six programs: a 6-month AI Foundation course from Class 9 and five three-year specialisations from Class 11, 104 to 624 hours.",
 "/curriculum": "Every module and project, month by month, for all six Neuronetworks AI Ed programs.",
 "/learning-experience": "How lessons, labs, projects and exams work at Neuronetworks AI Ed, from AI Foundation to the three-year programs.",
 "/projects": "Project names from every program roadmap, from first notebooks to capstones.",
 "/about": "About Neuronetworks AI Ed: practical AI and technology education for school students, from Class 9 onwards.",
 "/admissions": "Admissions at Neuronetworks AI Ed: eligibility for every program, how to apply and what parents should know.",
 "/faqs": "Answers about eligibility, hours, certifications, learning and applying at Neuronetworks AI Ed.",
 "/contact": "Talk to Neuronetworks AI Ed. Ask about a program, fees or how to apply.",
}

import hashlib as _h
SOCIAL = {}  # e.g. {"Instagram": "https://...", "X": "https://...", "LinkedIn": "https://..."}; empty until the owner sends real profile URLs
SOCIAL_HTML = ""
NNBOT_ON = False  # NN-Bot robot: switched off until the owner approves it (18 Oct 2026)
ASSET_V = _h.sha1((open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.css"), "rb").read() + open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "site.js"), "rb").read() + b"".join(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", f), "rb").read() for f in ("aiml3d.js", "nnbot.js", "ai-ml-training-pipeline.glb", "nn-bot.glb") if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", f))))).hexdigest()[:10]

SITE = "https://neuronetwrks.com"
# Google Analytics 4 Measurement ID (G-XXXXXXXXXX). Empty = analytics and the consent banner are off.
GA_ID = "G-1D2KJQ9RCF"
# IndexNow key (public by design; served at /<key>.txt so Bing and others accept URL pings).
INDEXNOW_KEY = "e7fd3f9464fa4857fe51aa4ef1a906fa"

def ga_head():
    if not GA_ID: return ""
    return ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
            "gtag('consent','default',{analytics_storage:'denied',ad_storage:'denied',ad_user_data:'denied',ad_personalization:'denied'});"
            "document.documentElement.dataset.ga='%s'</script>" % GA_ID)
ORG_ID = SITE + "/#organization"
PUBLISHER = {"@type": "Organization", "@id": ORG_ID, "name": "Neuronetworks AI Ed", "logo": {"@type": "ImageObject", "url": SITE + "/assets/logo-512.png", "width": 512, "height": 512}}
# Official profiles (LinkedIn, Instagram, YouTube, Google Business Profile). Add each URL once it exists.
SAME_AS = []
ORG = {"@type": "EducationalOrganization", "@id": ORG_ID, "name": "Neuronetworks AI Ed", "legalName": "Neuronetworks AI Ed Private Limited", "alternateName": ["NeuroNetworks AI Ed", "Neuronetworks", "NeuroNetworks", "neuronetwrks"], "url": SITE + "/", "logo": SITE + "/assets/logo-512.png", "email": "Hussain@neuronetwrks.com", "description": "Practical AI and technology programs: a six-month AI Foundation course from Class 9 and three-year specialisations from Class 11.", "areaServed": {"@type": "Country", "name": "India"}, "slogan": "Learn · Develop · Create", "knowsAbout": ["Artificial intelligence", "Machine learning", "Generative AI", "Software development", "Data science", "UI/UX design", "Cyber security", "Python programming"], "sameAs": SAME_AS}
if not SAME_AS: ORG.pop("sameAs")
ORG["hasOfferCatalog"] = {"@type": "OfferCatalog", "name": "AI and technology programs from Class 9", "itemListElement": [{"@type": "Offer", "itemOffered": {"@id": f"{SITE}/programs/{p[0]}#course"}} for p in PROGRAMS]}
CRUMB = {"programs": "Programs", "projects": "Projects", "about": "About", "admissions": "Admissions", "faqs": "FAQs", "contact": "Contact", "curriculum": "Curriculum", "learning-experience": "Learning Experience", "faculty-and-team": "Faculty and team"}
_tagre = re.compile(r"<[^>]+>")
def _txt(h): return html.unescape(re.sub(r"\s+", " ", _tagre.sub(" ", h))).strip()

def page_graph(route, title, d, body, extra):
    url = SITE + ("/" if route == "/" else route)
    g = [ORG]
    if route == "/":
        g.append({"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Neuronetworks AI Ed", "inLanguage": "en-IN", "publisher": {"@id": ORG_ID}})
    g.append({"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": d, "inLanguage": "en-IN", "isPartOf": {"@id": SITE + "/#website"}, "about": {"@id": ORG_ID}})
    if route != "/":
        parts = route.strip("/").split("/"); items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
        for i in range(len(parts)):
            p = "/" + "/".join(parts[:i + 1])
            nm = CRUMB.get(parts[i]) or (title if i == len(parts) - 1 else parts[i].replace("-", " ").title())
            items.append({"@type": "ListItem", "position": i + 2, "name": nm, "item": SITE + p})
        g.append({"@type": "BreadcrumbList", "itemListElement": items})
    qa = re.findall(r"<details[^>]*>\s*<summary>(.*?)</summary>\s*<div class=\"ans\">(.*?)</div>\s*</details>", body, re.S)
    if qa:
        seen, ents = set(), []
        for q, a in qa:
            q, a = _txt(q), _txt(re.sub(r'<a [^>]*class="le-link"[^>]*>.*?</a>', "", a, flags=re.S))
            q = re.sub(r"^(Admissions|Learning|Certification|Outcomes|Privacy|AI/ML program) ", "", q) if route == "/faqs" else q
            if q in seen or not a or "to be confirmed" in a.lower(): continue
            seen.add(q); ents.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}})
        if ents: g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": ents})
    if extra:
        for x in (extra if isinstance(extra, list) else [extra]):
            x = dict(x); x.pop("@context", None); g.append(x)
    return {"@context": "https://schema.org", "@graph": g}

def layout(route, title, body, active="none", desc=None, jsonld=None):
    t = title if route == "/" or len(title) + 22 > 60 else f"{title} | Neuronetworks AI Ed"
    d = desc or DESC.get(route) or DESC["/programs"]
    canon = SITE + ("/" if route == "/" else route)
    ld = '<script type="application/ld+json">' + json.dumps(page_graph(route, t, d, body, jsonld), ensure_ascii=False).replace("</", "<\\/") + "</script>"
    og = og_image(route, re.sub(r"\s*\|\s*Neuronetworks AI Ed$", "", title)) or SITE + "/assets/og.png"
    return f'''<!doctype html><html lang="en-IN" data-v="{ASSET_V}"{' data-nnbot="on"' if NNBOT_ON else ""}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t)}</title><meta name="description" content="{E(d)}"><meta name="robots" content="index, follow, max-image-preview:large"><meta name="theme-color" content="#006DEE">
<link rel="icon" href="/favicon.ico" sizes="48x48"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/assets/favicon-32.png" sizes="32x32" type="image/png"><link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"><link rel="canonical" href="{canon}">
<meta property="og:title" content="{E(t)}"><meta property="og:description" content="{E(d)}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:site_name" content="Neuronetworks AI Ed"><meta property="og:locale" content="en_IN">
<meta property="og:image" content="{og}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="{E(t) if "/assets/og/" in og else "Neuronetworks AI Ed: Learn. Develop. Create."}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(t)}"><meta name="twitter:description" content="{E(d)}"><meta name="twitter:image" content="{og}">
<link rel="preload" href="/assets/f-jakarta.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css?v={ASSET_V}"><link rel="alternate" type="application/rss+xml" title="Neuronetworks AI Ed guides" href="/guides/feed.xml">{ga_head()}{ld}</head>
<body><a class="skip" href="#main">Skip to content</a>
{header(active)}<main id="main">{body}</main>{footer()}<script src="/assets/site.js?v={ASSET_V}" defer></script></body></html>'''

def stair(blob, alt, opts, cid=None, tags=False):
    cid_attr = f' id="{cid}"' if cid else ""
    tg = ""
    if tags:
        for i, (l, x, y) in enumerate([("LEARN", 24, 76), ("PRACTISE", 20, 60), ("BUILD", 66, 52), ("TEST", 60, 30), ("IMPROVE", 30, 15)]):
            tg += f'<span class="lab-tag{" on" if i == 0 else ""}" aria-hidden="true" style="left:{x}%;top:{y}%;animation-delay:{-i*1.2}s">{l}</span>'
    return f'<div class="stair"><img src="/assets/{blob}.webp"{f' srcset="/assets/{blob}-600.webp 600w,{f" /assets/{blob}-800.webp 800w," if os.path.exists(os.path.join(HERE, "assets", blob + "-800.webp")) else ""} /assets/{blob}.webp 1200w" sizes="(max-width: 900px) 80vw, 560px"' if os.path.exists(os.path.join(HERE, "assets", blob + "-600.webp")) else ""} alt="{E(alt)}" width="1000" height="1000" fetchpriority="high"><canvas{cid_attr} data-stack=\'{json.dumps(opts)}\' aria-hidden="true"></canvas>{tg}</div>'

def headline(l1, l2):
    return f'<span class="ln"><span style="animation-delay:.2s">{l1}</span></span><span class="ln"><span style="animation-delay:.32s;color:var(--blue)">{l2}</span></span>'

def page_hero(crumb, l1, l2, lead, actions="", art=""):
    return f'''<section class="page-hero"><div class="wrap grid"><div><p class="crumbs"><a href="/">Home</a> / {crumb}</p><h1>{headline(l1, l2)}</h1><p class="lead fade">{lead}</p>{f'<div class="actions fade">{actions}</div>' if actions else ''}</div>{art}</div></section>'''

def btn(kind, href, label, arrow=True):
    return f'<a class="btn btn-{kind}" href="{href}">{label}{" <i aria-hidden=\"true\">→</i>" if arrow else ""}</a>'

def cta_panel(h="Ready to ask?", p="Tell us which program interests you. Ask us about fees and intake dates."):
    sparks = "".join(f'<i style="left:{x}%;top:{y}%;--d:{d}s;--s:{sz}px"></i>' for x, y, d, sz in [(58, 22, 0, 4), (66, 70, 1.2, 5), (93, 30, 2.1, 4), (88, 78, .6, 6), (73, 12, 1.7, 3), (97, 58, 2.6, 4), (61, 48, 3.1, 3)])
    return f'''<section class="sec"><div class="wrap"><div class="cta2"><div class="cta2-glow" aria-hidden="true"></div><div class="cta2-sparks" aria-hidden="true">{sparks}</div>
<div class="cta2-body"><p class="cta2-eb">Your next step</p><h2>{h}</h2><p class="cta2-lead">{p}</p>
<div class="cta2-actions"><a class="cta2-apply" href="/admissions">Apply <i aria-hidden="true">→</i></a><a class="cta2-talk" href="/contact">Talk to us</a></div></div></div></div></section>'''

def faq_items(items, first_open=True, cat=False):
    out = ""
    for i, it in enumerate(items):
        q, a = it[0], it[1]
        attr = f' data-cat="{it[2]}"' if cat else ""
        out += f'<details{attr}{" open" if first_open and i == 0 else ""}><summary>{q}</summary><div class="ans">{a}</div></details>'
    return out

def sec_head(eyebrow, h, lead=""):
    return f'<div class="sec-head"><div><p class="eyebrow">{eyebrow}</p><h2>{h}</h2></div>{f"<p class=\"lead\">{lead}</p>" if lead else ""}</div>'

def beats():
    b = [("Theory", "Short, clear explanations"), ("Demonstration", "Watch it worked through"), ("Hands-on lab", "Do it yourself"), ("Project", "Make something real"), ("Exam", "One hour, then move on")]
    return '<ol class="step-rail rv">' + "".join(f'<li><p class="mono">{i+1:02d} · {a}</p><h3>{c}</h3></li>' for i, (a, c) in enumerate(b)) + '</ol>'

def path_diagram():
    s = [("Learn", "A clear concept, then a worked example"), ("Guided practice", "Follow along with support"), ("Independent lab", "Solve real tasks yourself"),
         ("Practical exam", "A one-hour exam after each module"), ("Get feedback", "Review your results and hints"), ("Improve and retry", "Learn from mistakes and try again")]
    return '<ol class="path rv">' + "".join(f'<li><span class="n">{i+1:02d}</span><div><h3>{a}</h3><p>{b}</p></div></li>' for i, (a, b) in enumerate(s)) + '</ol>'

def lab_showcase():
    return '''<div class="lab rv"><div class="win"><div class="bar"><i></i><i></i><i></i><span>clean.py · sample task</span></div><pre><em># Task 3 of 5: clean the marks</em>
<b>import</b> pandas <b>as</b> pd
df = pd.read_csv(<em>"marks.csv"</em>)
mid = df.maths.median()
df.maths = df.maths.fillna(mid)
df = df.drop_duplicates(<em>"roll_no"</em>)
print(df.describe())</pre></div>
<div class="side"><div class="box"><span class="mono">Lab instructions</span><ul><li class="t">Load marks.csv</li><li class="t">Fill missing maths marks with the median</li><li class="t">Remove duplicate roll numbers</li></ul><span class="btn btn-primary btn-sm" style="width:100%;margin-top:8px" aria-hidden="true">Submit for evaluation</span></div>
<div class="box"><span class="mono">Evaluation result</span><p style="font:600 1.1rem var(--font-display);margin-bottom:12px">Score 86 / 100 <span class="muted small" style="font-family:var(--font-body);font-weight:500">5 of 5 checks passed · 1 hint used</span></p>
<div class="score"><div><span>Correctness</span><span class="bar-track"><i style="width:100%"></i></span></div><div><span>Code quality</span><span class="bar-track"><i style="width:80%"></i></span></div><div><span>Best practices</span><span class="bar-track"><i style="width:65%"></i></span></div></div></div></div></div>'''


IMG = {"found": "aif3", "aiml": "aiml3", "sw": "sw3", "ds": "ds2", "ux": "ux2", "cy": "cy2"}
NO_DOT = {"found", "aiml", "sw", "ds", "ux", "cy"}  # AI Foundation model has no floating spheres (owner request)  # AI Foundation uses the "AI on a platform" model
ICON_ALT = {"ai-foundation": "3D steps icon for the AI Foundation course, a first step into AI",
            "ai-ml-engineering": "3D connected spheres icon for the AI/ML Engineering program, like nodes in a model",
            "software-development": "3D stacked layers icon for the Software Development program, like the layers of an app",
            "data-science-ai": "3D bar chart icon for the Data Science & AI program",
            "product-ux-ai-design": "3D ring icon for the Product and UX/UI Design program",
            "cybersecurity": "3D shield icon for the Cybersecurity program"}
ICON = {"ai-foundation": "found", "ai-ml-engineering": "aiml", "software-development": "sw", "data-science-ai": "ds", "product-ux-ai-design": "ux", "cybersecurity": "cy"}

def pt_art(ic):
    if ic == "aiml":  # live Blender/WebGL model (assets/aiml3d.js); the poster is the same render, shown until WebGL is ready
        return (f'<div class="pt-ico pt-ico--3d pt-3d" data-glb="/assets/ai-ml-training-pipeline.glb?v={ASSET_V}" aria-hidden="true">'
                '<picture><source media="(max-width:760px)" srcset="/assets/i-aiml-pipeline-m.webp">'
                '<img class="pt-poster" src="/assets/i-aiml-pipeline.webp" alt="" width="1200" height="675" loading="lazy"></picture></div>')
    return (f'<div class="pt-ico ic-{ic}" aria-hidden="true"><img class="pt-obj" src="/assets/i-{IMG.get(ic, ic)}.webp" alt="" width="360" height="360" loading="lazy">'
            + ("" if ic in NO_DOT else f'<img class="pt-dot" src="/assets/i-{ic}-dot.webp" alt="" width="360" height="360" loading="lazy">') + '</div>')

def program_tile(p, i, cat=None, hl="h3"):
    d = D[p[0]]; lead = i == 0; ic = ICON[p[0]]
    tag = f"Start here · {p[4]}" if lead else f"Specialisation · {p[4]}"
    cat_attr = f' data-cat="{cat}"' if cat else ""
    return f"""<a class="pcard pt{' pt--lead' if lead else ''}"{cat_attr} href="/programs/{p[0]}" style="--ti:{i}">
<div class="pt-body"><span class="pt-tag">{tag}</span><{hl}>{name_of(p)}</{hl}><p>{E(d["summary"])}</p></div>
{pt_art(ic)}
<dl class="pt-stats"><div><dd class="n">{p[3]}</dd><dt>Hours</dt></div><div><dd>{LV[d["level"]]}</dd><dt>Level</dt></div><div><dd>{p[4]}</dd><dt>Duration</dt></div></dl>
<span class="pt-go" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></span></a>"""

PP_LEAD = '<div class="pp-lead"><p>6 Courses – 1 Foundation course &amp; 5 specialisation courses. No previous experience required.</p><ul class="pp-list"><li><a href="/programs/ai-foundation">AI Foundation</a>: 26 weeks (6 months @ 4 hours a week)</li><li><a href="/programs/ai-ml-engineering">AI/ML Engineering</a>: 3 years (4 hours a week)</li><li><a href="/programs/data-science-ai">Data Science &amp; AI</a>: 3 years (4 hours a week)</li><li><a href="/programs/product-ux-ai-design">Product and UX/UI Design</a>: 3 years (4 hours a week)</li><li><a href="/programs/cybersecurity">Cybersecurity</a>: 3 years (4 hours a week)</li><li><a href="/programs/software-development">Software Development</a>: 3 years (4 hours a week)</li></ul></div>'
def prog_head(level="h2"):
    return f"""<div class="pp-head"><div><p class="pp-eyebrow">Our programs</p><{level} class="pp-h"><span class="ln"><span>Choose a path.</span></span><span class="ln"><span>Build your future.</span></span></{level}></div>
{PP_LEAD if level == "h1" else ""}</div>"""

def prog_banner(hl="h3", lazy=True):
    d = D["ai-foundation"]
    return f"""<div class="pp-banner"><div class="pp-b-body"><span class="pt-tag">Start here · 6 months</span><{hl}>AI Foundation</{hl}><p>{E(d["summary"])}</p>
<div class="pp-b-row"><dl class="pp-b-stats"><div><dd data-count-to="104">104</dd><dt>Hours</dt></div><div><dd>Beginner</dd><dt>Level</dt></div><div><dd>6 months</dd><dt>Duration</dt></div></dl>
<a class="pp-b-btn" href="/programs/ai-foundation">View program <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a></div></div>
<div class="pp-b-art" aria-hidden="true"><svg class="pp-b-grid" viewBox="0 0 600 400" preserveAspectRatio="none"><path d="M0 330 L600 210 M0 250 L600 130 M120 0 L60 400 M300 0 L250 400 M480 0 L440 400" stroke="#fff" stroke-opacity=".14" fill="none"/></svg><img class="pp-b-obj" src="/assets/i-banner-aif4.webp" srcset="/assets/i-banner-aif4-640.webp 640w, /assets/i-banner-aif4.webp 1218w" sizes="(max-width: 760px) 70vw, 609px"{' loading="lazy"' if lazy else ''} alt="3D model for the AI Foundation course: the letters AI on a small laptop lab with a gear" width="609" height="419"></div></div>"""

def prog_swoosh():
    return '<svg class="pp-swoosh" viewBox="0 0 1440 900" preserveAspectRatio="none" aria-hidden="true"><path d="M1440 120 C1180 220 1100 420 1440 560" fill="none" stroke="#D9E8FF" stroke-width="90" stroke-opacity=".45"/><path d="M-40 760 C320 640 620 860 980 720" fill="none" stroke="#E6F0FF" stroke-width="70" stroke-opacity=".6"/></svg>'

def prog_filters():
    return """<div class="pp-filters"><div role="group" aria-label="Filter programs" data-filter-group class="pp-chips"><button class="pp-chip" type="button" data-filter="all" aria-pressed="true">All programs</button><button class="pp-chip" type="button" data-filter="start" aria-pressed="false">Start here</button><button class="pp-chip" type="button" data-filter="three" aria-pressed="false">Three-year specialisations</button></div><span class="pp-rule" aria-hidden="true"></span><p class="pp-count" data-count role="status">6 programs</p></div>"""

# ---------------------------------------------------------------- pages
def home_guides():
    picks = ["courses-after-10th", "ai-courses-after-10th", "career-options-after-10th"]
    cards = "".join(f'<a class="gd-card" href="/guides/{g}"><strong>{E(GUIDE_BY[g]["title"])}</strong><span>{E(GUIDE_BY[g]["desc"])}</span></a>' for g in picks)
    return (f'<section class="sec"><div class="wrap">{sec_head("Guides", "Choosing a tech course after 10th?", "AI, coding, data science, UI/UX and cyber security courses after Class 10, explained with real hours, tools and projects.")}'
            f'<div class="gd-cards gd-cards--3">{cards}</div><div class="actions" style="margin-top:28px">{btn("secondary", "/guides", "All guides")}</div></div></section>')

def home():
    hero = f'''<section class="hero"><div class="wrap hero-grid"><div>
<p class="eyebrow">AI/Super Intelligence and related technology education</p>
<h1 class="display"><span class="ln"><span style="animation-delay:.2s">Build your skills</span></span><span class="ln"><span style="animation-delay:.3s">to shape the</span></span><span class="ln"><span style="animation-delay:.4s;color:var(--blue)">Future</span></span></h1>
<div class="lead fade hero-lead"><p>Employment-oriented, practical, project-based programs, with a portfolio of every real-world industry project you solve.</p>
<p><strong>AI Foundation course:</strong> 104 hours, 4 hours a week for 26 weeks (6 months), from Class 9.</p>
<p><strong>Specialisation in any one of 5 streams</strong>, from Class 11 (Software Development, AI/ML Engineering, Data Science &amp; AI, Cybersecurity, Product and UX/UI Design), taught through 624 hours: 4 hours a week for 52 weeks a year, over three years.</p>
<p>In the three-year specialisation programs, every learner takes part in an individual or a collaborative project and an examination, to show proof of learning.</p></div>
<div class="actions fade">{btn("primary", "/programs", "Explore Programs")}{btn("secondary", "/learning-experience", "See the learning experience", False)}</div>
<p class="hero-note fade"><span class="ic" aria-hidden="true">{icon("layers")}</span><span>AI Foundation from Class 9. Specialisations from Class 11.<br>From 104 to 624 hours.</span></p></div>
{stair("r-hero", "Module Stack: a spiral staircase of 36 glass plates, one for each monthly module, with a green bead for each monthly project", {"n": 36, "lit": 0.2, "yaw": -0.7, "dist": 15.2, "dy": -0.1}, "heroStair", True)}
</div></section>
<div class="wrap"><ul class="pillars" aria-label="What to expect">
<li><span class="ic">{icon("cube")}</span><span><b>Project-based</b><span>A project every month</span></span></li>
<li><span class="ic">{icon("clock")}</span><span><b>1-hour exams</b><span>After each module</span></span></li>
<li><span class="ic">{icon("layers")}</span><span><b>Hands-on labs</b><span>In every month</span></span></li>
<li><span class="ic">{icon("bars")}</span><span><b>Step-by-step</b><span>Start from Class 9</span></span></li></ul></div>'''
    tiles = "".join(program_tile(p, i) for i, p in enumerate(PROGRAMS))
    programs = f'''<section class="pp" id="programs">{prog_swoosh()}<div class="wrap">{prog_head("h2")}{prog_banner()}<div class="pp-grid">{tiles}</div><div class="actions" style="margin-top:36px">{btn("secondary", "/programs", "Compare all six programs")}</div></div></section>'''
    method = f'''<section class="sec sec--tint"><div class="wrap">{sec_head("Our approach", "Learn. Build. Test.<br>Improve. Repeat.", "Gain real technical skills through structured learning, hands-on practice, projects and a one-hour exam at the end of each module.")}{path_diagram()}
<div class="actions" style="margin-top:40px">{btn("primary", "/learning-experience", "See the learning experience")}{btn("secondary", "/curriculum", "Explore the curriculum", False)}</div></div></section>'''
    lab = f'''<section class="sec"><div class="wrap">{sec_head("Real practice environment", "Hands-on labs<br>with real tools", "Practise in a lab environment with real tasks, checked work and clear feedback.")}{lab_showcase()}
<ul class="lab-points"><li>Real tools and environments</li><li>Checked tasks</li><li>Feedback and hints</li><li>Labs you can reset and retry</li></ul><p class="small muted" style="margin-top:20px">Every program uses the same lab. You write and run code in the browser, each task is checked when you submit, a hint appears when you are stuck, and you can reset a lab and try again as many times as you need.</p></div></section>'''
    feats = [("Image classification application", "Year 2 · AI/ML", True), ("Document RAG assistant", "Year 3 · AI/ML", False), ("Tool-using AI agent", "Year 3 · AI/ML", False)]
    fc = "".join(f'<a class="fcard rv{" big" if b else ""}" href="/projects#aiml"><div class="shot">{shot(1 if "mage" in n else 2 if "gent" in n else 0)}</div><div class="cap"><span class="tag">{y}</span><h3>{n}</h3></div></a>' for k, (n, y, b) in enumerate(feats))
    projects = featured_projects()
    fq = [("Who can apply?", "<p>AI Foundation is open from Class 9. The five three-year specialisations are for students from Class 11 onwards.</p>"),
          ("How many hours is the AI/ML program?", "<p>624 hours over three years (36 months): 4 hours a week for 52 weeks a year, or 208 hours a year. Exam time is counted inside the 624 hours.</p>"),
          ("How are learners assessed?", "<p>Every month ends with a project and a one-hour exam. In AI Foundation the pass mark is 80%, with review and a retry below it.</p>"),
          ("What does it cost?", "<p>We share fees when you enquire, so you get the details for the program you choose. Use the Enquire about fees button and a specialist will respond.</p><p><a class=\"tl\" href=\"/contact?topic=fees\">Enquire about fees <i aria-hidden=\"true\">→</i></a></p>")]
    faq = f'''<section class="sec"><div class="wrap split"><div><p class="eyebrow">Frequently asked questions</p><h2>Got questions?<br>We've got answers.</h2><p class="lead" style="margin-top:16px">Find answers about our programs, learning format and admissions.</p><div class="actions" style="margin-top:28px">{btn("secondary", "/faqs", "All questions", True)}</div></div><div>{faq_items(fq)}</div></div></section>'''
    ld = None
    return layout("/", "Neuronetworks AI Ed: AI & tech courses after 10th in India", hero + programs + method + lab + projects + home_guides() + faq + cta_panel(), "none", jsonld=ld)

def programs_page():
    cards = "".join(program_tile(p, i, "start" if i == 0 else "three", "h2") for i, p in enumerate(PROGRAMS))
    rows = "".join(f'<tr><td data-l="Program"><a href="/programs/{p[0]}">{name_of(p)}</a></td><td data-l="Length">{p[4]}</td><td data-l="Hours">{p[3]}</td><td data-l="Level">{LV[D[p[0]]["level"]]}</td><td data-l="Entry">{"Class 9 onwards" if p[0] == "ai-foundation" else "Class 11 onwards"}</td><td data-l="Fees"><a class="tl" href="/contact?topic=fees">Enquire</a></td></tr>' for p in PROGRAMS)
    body = f'''<section class="pp pp--page" id="all">{prog_swoosh()}<div class="wrap">{prog_head("h1")}{prog_banner("h2", lazy=False)}{prog_filters()}<div class="pp-grid">{cards}</div></div></section>
<section class="sec sec--tint" id="compare"><div class="wrap">{sec_head("Compare at a glance", "Different starting points.<br>Different depth.", "The same six programs, side by side. Every program is open to students from Class 11 onwards. Pick by length and subject, then open the program page for modules and projects.")}
<div class="tablewrap"><table class="cmp"><caption class="sr">Comparison of the six programs</caption><thead><tr><th scope="col">Program</th><th scope="col">Length</th><th scope="col">Hours</th><th scope="col">Level</th><th scope="col">Entry</th><th scope="col">Fee</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>
<section class="sec"><div class="wrap">{sec_head("How every month works", "The same five beats<br>in every three-year program.")}{beats()}</div></section>
<section class="sec sec--tint"><div class="wrap split"><div><p class="eyebrow">Before you choose</p><h2>Not sure which<br>course to choose?</h2><p class="lead" style="margin-top:16px">Ask us. A course specialist will reply with a suggestion based on your interests.</p><div class="actions" style="margin-top:24px">{btn("primary", "/contact", "Talk to us")}</div></div>
<div>{faq_items([("Who can apply?", "<p>AI Foundation is open from Class 9. The five three-year specialisations are for students from Class 11 onwards.</p>"), ("Where should a beginner start?", "<p>AI Foundation is a beginner course of 104 hours over six months, from AI literacy to Python, data, machine learning and small AI applications.</p>"), ("How long are the specialisations?", "<p>Each is three years and 624 hours: 4 hours a week for 52 weeks a year, or 208 hours a year. Exam time is counted inside those hours.</p>"), ("What does it cost?", "<p>We share fees when you enquire, so you get the details for the program you choose. Use the Enquire about fees button and a specialist will respond.</p><p><a class=\"tl\" href=\"/contact?topic=fees\">Enquire about fees <i aria-hidden=\"true\">→</i></a></p>")])}</div></div></section>''' + cta_panel()
    return layout("/programs", "Programs", body, "programs")

PROG_SEO = {
 "ai-foundation": ("AI Foundation course from Class 9: 6 months, 104 hours", "A 6-month, 104-hour AI course open from Class 9: Python, data, machine learning, generative AI, RAG and agents, with AI-901 and AIF-C01 preparation."),
 "ai-ml-engineering": ("AI and ML engineering course after 10th: 3 years", "A 3-year, 624-hour AI/ML engineering course from Class 11: Python, maths for ML, deep learning, generative AI, MLOps and 36 projects."),
 "software-development": ("Coding and software development course after 10th", "A 3-year, 624-hour coding course from Class 11: Java, JavaScript, React, databases, Spring Boot and cloud, with a project every month."),
 "data-science-ai": ("Data science and AI course after 10th: 3 years", "A 3-year, 624-hour data science course from Class 11: Python, SQL, statistics, dashboards, machine learning and generative AI."),
 "product-ux-ai-design": ("UI/UX and AI design course after 10th: 3 years", "A 3-year, 624-hour UI/UX design course from Class 11: user research, wireframes, prototyping, design systems and AI product design."),
 "cybersecurity": ("Cyber security course after 10th: 3-year program", "A 3-year, 624-hour cyber security course from Class 11: networking, Linux, SOC, ethical hacking in authorised labs and cloud security."),
}
PROG_GUIDES = {
 "ai-foundation": ["ai-courses-after-10th", "ai-projects-for-students", "career-options-after-10th"],
 "ai-ml-engineering": ["become-ai-engineer-after-10th", "ai-courses-after-10th", "ai-projects-for-students"],
 "software-development": ["computer-coding-courses-after-10th", "ai-vs-software-vs-data-science", "courses-after-10th"],
 "data-science-ai": ["data-science-after-10th", "ai-vs-software-vs-data-science", "courses-after-10th"],
 "product-ux-ai-design": ["ui-ux-designer-after-10th", "courses-after-10th", "career-options-after-10th"],
 "cybersecurity": ["cyber-security-course-after-10th", "career-options-after-10th", "courses-after-10th"],
}

# Indicative India salary ranges (LPA) from the curriculum documents (docs/extracted/3-Year_*.md, "Earning potential").
# Shown by owner decision (15 Oct 2026) as indicative, never guaranteed. AI Foundation has no source table.
SAL_BANDS = ["Fresher", "1–2 years", "3–5 years", "5–8 years", "Senior"]
SALARY = {
 "ai-ml-engineering": (["₹5–10 LPA", "₹7–15 LPA", "₹12–25 LPA", "₹20–40 LPA", "₹30–60+ LPA"], "₹800–2,000 an hour early on, rising to ₹4,000–8,000+ for specialised work"),
 "software-development": (["₹4–8 LPA", "₹5–12 LPA", "₹10–20 LPA", "₹18–35 LPA", "₹25–50+ LPA"], "₹500–1,200 an hour with 0–2 years' experience, rising to ₹2,500–5,000+ after 5 years"),
 "data-science-ai": (["₹4–8 LPA", "₹5–12 LPA", "₹10–22 LPA", "₹18–35 LPA", "₹25–50+ LPA"], None),
 "product-ux-ai-design": (["₹4–8 LPA", "₹6–12 LPA", "₹10–22 LPA", "₹18–35 LPA", "₹25–50+ LPA"], "₹500–1,500 an hour early on, rising to ₹3,000–6,000+ for advanced work"),
 "cybersecurity": (["₹4–8 LPA", "₹5–10 LPA", "₹8–20 LPA", "₹15–35 LPA", "₹25–60+ LPA"], None),
}
SAL_NOTE = ("Indicative 2026 India market ranges from our curriculum research. They are not a promise: pay depends on the employer, city, role, skills, "
            "portfolio and, for some employers, a degree. Neuronetworks AI Ed does not guarantee a job, internship or salary.")

def salary_section(slug):
    if slug not in SALARY: return ""
    bands, free = SALARY[slug]; nm = E(prog(slug)[2])
    rows = "".join(f'<tr><th scope="row">{b}</th><td>{v}</td></tr>' for b, v in zip(SAL_BANDS, bands))
    fl = f'<p style="margin-top:16px">Freelance work is another route: indicative rates are {E(free)}.</p>' if free else ""
    return (f'<section class="sec"><div class="wrap split"><div><p class="eyebrow">Earning potential</p><h2>What can you earn in India?</h2>'
            f'<p class="lead" style="margin-top:16px">Entry-level roles linked to {nm} typically pay {bands[0]} in India, rising with experience to {bands[-1]} at senior level. These are market estimates, not guarantees.</p>{fl}</div>'
            f'<div><div class="gd-table gd-table--sal" style="margin-top:0"><table><caption class="vh">Indicative salary by experience</caption><thead><tr><th scope="col">Experience</th><th scope="col">Indicative salary (per year)</th></tr></thead><tbody>{rows}</tbody></table></div>'
            f'<p class="small muted" style="margin-top:14px">{SAL_NOTE}</p></div></div></section>')

def program_detail(slug):
    p = prog(slug); d = D[slug]; k = p[1]; yrs = d["years"]; ny = len(yrs); total = sum(len(y["modules"]) for y in yrs)
    nm = name_of(p); plain = p[2]
    l1, l2 = {"ai-foundation": ("AI", "Foundation."), "ai-ml-engineering": ("AI/ML", "Engineering."), "software-development": ("Software", "Development."),
              "data-science-ai": ("Data Science", "&amp; AI."), "product-ux-ai-design": ("Product and", "UX/UI Design."), "cybersecurity": ("Cyber", "security.")}[slug]
    art = (f'<figure class="art-frame hero-art hero-art--3d"><img src="/assets/p-found-hero3.webp" alt="3D illustration: the letters AI on a layered platform with gears, a code panel and a padlock" width="900" height="900" fetchpriority="high"></figure>'
           if slug == "ai-foundation" else f'<figure class="art-frame hero-art">{ART[slug]()}<figcaption>Illustration</figcaption></figure>')
    body = page_hero(f'<a href="/programs">Programs</a> / {nm}', l1, l2, E(d["summary"]), btn("primary", "/contact", "Talk to us") + btn("secondary", "/curriculum#" + k + "-y1", "See the curriculum", False), art)
    facts = [("Duration", p[4], 0), ("Total hours", p[3], 0), ("Per week", f'{d["hoursPerWeek"]} hours', 0), ("Entry", "From Class 9" if slug == "ai-foundation" else "From Class 11", 0), ("Certificate", "On completion", 0), ("Fees", FEE_LINK, 0), ("Next intake", FEE, 1)]
    body += '<section class="sec sec--tight" style="padding-top:0"><div class="wrap"><dl class="facts panel">' + "".join(f'<div><dt>{a}</dt><dd{" class=\"ph-text\"" if c else ""}>{b}</dd></div>' for a, b, c in facts) + '</dl></div></section>'
    body += f'''<section class="sec"><div class="wrap split"><div><p class="eyebrow">Overview</p><h2>What this program is.</h2></div><div class="stack"><p class="lead">{E(d["answer"])}</p>
<div class="dual"><div><p class="mono" style="color:var(--blue-text)">Intended learner</p><p style="margin-top:8px">{E(d["entry"])}.</p></div><div><p class="mono" style="color:var(--blue-text)">How it is assessed</p><p style="margin-top:8px">{E(d["assessment"])}</p></div></div></div></div></section>'''
    yr_html = ""
    for yi, y in enumerate(yrs):
        lbl = f'Year {yi+1} · {y["hours"]} hours' if ny > 1 else f'{y["hours"]} hours · {len(y["modules"])} modules'
        yr_html += f'<div class="yr rv"><p class="mono" style="color:var(--blue-text)">{lbl}</p><ol>' + "".join(f'<li><span class="m">{yi*12+i+1:02d}</span><span>{E(m)}{f" <small class=\"mh\">· {d['moduleHours'][yi*12+i]} hours</small>" if d.get("moduleHours") else ""}</span></li>' for i, m in enumerate(y["modules"])) + '</ol></div>'
    body += f'''<section class="sec sec--tint"><div class="wrap">{sec_head("Curriculum overview", f"{total} modules," + (" twelve a year." if ny > 1 else " in six months."), "Each module is one month of the program. The curriculum page shows every module with its project." if ny > 1 else "About two modules a month, at 4 hours a week. The curriculum page shows every module with its project.")}<div class="yrs" style="--cols:{ny}">{yr_html}</div>
<div class="actions" style="margin-top:32px">{btn("primary", "/curriculum#" + k + "-y1", "Open the full curriculum")}</div></div></section>'''
    projs = d["projects"]
    items = "".join(f'<a class="pj rv" href="/curriculum#{k}-y{(i//12)+1 if aligned(slug) else 1}"><small>{(f"Year {i//12+1} · Month {i+1}" if ny > 1 else f"Module {i+1}") if aligned(slug) else f"Project {i+1}"}</small><h3>{E(x)}</h3></a>' for i, x in enumerate(projs[:6]))
    body += f'''<section class="sec"><div class="wrap">{sec_head("Practical projects", "Things you build.", f"A sample of the {len(projs)} projects in this program. The full list is on the Projects page.")}<div class="pj-list">{items}</div><div class="actions" style="margin-top:32px">{btn("secondary", "/projects#" + k, f"See all {len(projs)} projects")}</div></div></section>'''
    tools = "".join(f"<span>{E(x)}</span>" for x in d["tools"])
    certs = "".join(f"<li>{E(x)}</li>" for x in d["certifications"])
    roles = "".join(f"<li>{E(x)}</li>" for x in d["careerRoles"])
    cols = [f'<div><h3>Tools and technologies</h3><div class="pills" style="margin-top:20px">{tools}</div></div>',
            f'<div><h3>Certification pathways</h3><ul class="list-rule" style="margin-top:16px">{certs}</ul><p class="small muted" style="margin-top:14px">Awarded by the certifying organisations, not by Neuronetworks AI Ed. Passing is not guaranteed.</p></div>']
    if roles: cols.append(f'<div><h3>Career directions</h3><ul class="list-rule" style="margin-top:16px">{roles}</ul><p class="small muted" style="margin-top:14px">Directions, not promises. No job or internship is guaranteed.</p></div>')
    body += f'<section class="sec sec--tint"><div class="wrap cols3" style="--cols:{len(cols)}">{"".join(cols)}</div></section>'
    body += salary_section(slug)
    hw = "".join(f"<li>{E(x)}</li>" for x in d["hardware"])
    body += f'''<section class="sec"><div class="wrap split"><div><p class="eyebrow">Requirements</p><h2>Recommended laptop.</h2><p class="lead" style="margin-top:16px">Entry: {E(d["entry"])}. The setup below is recommended, not required to join; ask us if your current computer is enough to start.</p><div class="actions" style="margin-top:24px">{btn("secondary", "/admissions", "Admissions details")}</div></div><ul class="panel list-rule" style="padding:8px 28px">{hw}</ul></div></section>'''
    fq = [(E(f["q"]), "<p>" + E(conf(f["a"])) + "</p>") for f in d["faqs"]]
    body += f'<section class="sec sec--tint"><div class="wrap split"><div><p class="eyebrow">Questions</p><h2>About this program.</h2></div><div>{faq_items(fq)}</div></div></section>'
    gl = "".join(f'<a class="gd-card" href="/guides/{g}"><strong>{E(GUIDE_BY[g]["title"])}</strong><span>{E(GUIDE_BY[g]["desc"])}</span></a>' for g in PROG_GUIDES[slug])
    body += f'<section class="sec"><div class="wrap">{sec_head("Guides", "Read before you decide.", "Plain answers for students and parents.")}<div class="gd-cards gd-cards--3">{gl}</div></div></section>' + cta_panel()
    ld = {"@type": "Course", "@id": f"{SITE}/programs/{slug}#course", "name": plain, "description": d["summary"], "url": f"{SITE}/programs/{slug}", "provider": {"@id": ORG_ID}, "inLanguage": "en-IN", "educationalLevel": "Beginner" if d["level"] == "foundation" else "Beginner to advanced", "coursePrerequisites": "Class 9 and above" if slug == "ai-foundation" else "Class 11 and above", "timeRequired": f"PT{p[3]}H", "educationalCredentialAwarded": "Certificate of completion from Neuronetworks AI Ed", "hasCourseInstance": {"@type": "CourseInstance", "courseMode": "Online", "courseWorkload": f"PT{p[3]}H", "inLanguage": "en-IN"}, "teaches": [m for y in yrs for m in y["modules"]][:12]}
    return layout(f"/programs/{slug}", PROG_SEO[slug][0], body, "programs", desc=PROG_SEO[slug][1], jsonld=ld)

def curriculum_page():
    chips = ""; ylists = ""; panels = ""
    for i, p in enumerate(PROGRAMS):
        d = D[p[0]]; k = p[1]; ny = len(d["years"]); al = aligned(p[0])
        chips += f'<button class="chip" type="button" data-prog-btn="{k}" aria-pressed="{"true" if i == 1 else "false"}"><b>{name_of(p)}</b><small>{p[4]} · {p[3]} h</small></button>'
        tabs = "".join(f'<button class="chip" role="tab" type="button" id="t-{k}-{y+1}" data-year="{y+1}" aria-selected="false" aria-controls="p-{k}-{y+1}">{f"Year {y+1}" if ny > 1 else "Six months"}</button>' for y in range(ny))
        ylists += f'<div class="tabs" role="tablist" aria-label="{name_of(p)} years" data-year-list="{k}"{"" if i == 1 else " hidden"}>{tabs}</div>'
        n = 0
        for yi, y in enumerate(d["years"]):
            groups = ""
            for g in range(0, len(y["modules"]), 4):
                rows = ""
                for mi in range(g, min(g + 4, len(y["modules"]))):
                    rows += f'<div class="mod"><span class="m">{n+1:02d}</span><span>{E(y["modules"][mi])}</span><span class="p">{f"<small>Project</small>{E(d["projects"][n])}" if al else ""}</span></div>'
                    n += 1
                groups += f'<details{" open" if g == 0 else ""}><summary>{"Months" if ny > 1 else "Modules"} {yi*12+g+1} to {yi*12+min(g+4,len(y["modules"]))}</summary>{rows}</details>'
            extra = "" if al else '<p class="cur-note"><strong>Projects:</strong> ' + "; ".join(E(x) for x in d["projects"]) + ".</p>"
            panels += f'<div class="tabpanel mods" role="tabpanel" id="p-{k}-{yi+1}" aria-labelledby="t-{k}-{yi+1}" data-panel="{k}-{yi+1}" hidden><div class="yearbar"><h2 class="h3">{name_of(p)}{f", year {yi+1}" if ny > 1 else ""}</h2><span class="mono muted">{y["hours"]} hours · {len(y["modules"])} modules</span></div>{groups}{extra}<p class="cur-note">{E(d["assessment"])}</p><div class="actions" style="margin-top:24px"><a class="tl" href="/programs/{p[0]}">About this program <i aria-hidden="true">→</i></a><a class="tl" href="/projects#{k}">See its projects <i aria-hidden="true">→</i></a></div></div>'
    body = f'''<section class="page-hero"><div class="wrap"><p class="crumbs"><a href="/">Home</a> / Curriculum</p><h1>{headline("The full", "curriculum.")}</h1><p class="lead fade">Every module and project, month by month, taken from each program's roadmap. Choose a program, then open a year.</p></div></section>
<section class="sec sec--tight"><div class="wrap" id="cur"><div class="cur-top"><div><p class="eyebrow">1. Choose a program</p><div class="cur-prog" role="group" aria-label="Choose a program">{chips}</div></div><div><p class="eyebrow">2. Choose a year</p>{ylists}</div></div>
<p id="cur-live" class="sr" role="status"></p>{panels}</div></section>''' + cta_panel("Questions about a module?", "Ask us. A specialist responds.")
    return layout("/curriculum", "Curriculum", body, "programs")

LI = {
 "book": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3H20v15H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 20.5A2.5 2.5 0 0 1 6.5 18H20v3H6.5"/>',
 "play": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l5.5 3.5-5.5 3.5z" fill="currentColor"/>',
 "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 12h6M10 16h6"/>',
 "code": '<path d="M9 8l-4 4 4 4M15 8l4 4-4 4M13.5 5l-3 14"/>',
 "chart": '<path d="M5 20V12M10 20V6M15 20V10M20 20V4"/>',
 "check": '<rect x="4" y="4" width="16" height="16" rx="2"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "tools": '<path d="M14.5 6.5a3.5 3.5 0 0 0 4.6 4.6L20 12l-8 8-3-3 8-8z"/><path d="M4 4l6 6M4 10l6-6"/>',
 "image": '<rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="9" cy="10" r="1.6"/><path d="M21 16l-5-5-8 8"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
}
def li(k, s=22): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{LI[k]}</svg>'
ARW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

def le_eyebrow(t, both=False): return f'<p class="le-eb{" le-eb--both" if both else ""}">{t}</p>'

def learning_page():
    hero = f'''<section class="le-hero" data-le-hero><svg class="le-swoosh" viewBox="0 0 1440 700" preserveAspectRatio="none" aria-hidden="true"><path d="M-60 600 C380 420 760 720 1500 420" fill="none" stroke="#DCE9FF" stroke-width="120" stroke-opacity=".5"/></svg>
<div class="wrap le-hero-grid"><div class="le-hero-copy">{le_eyebrow("Learning experience", True)}<h1 class="le-h1"><span class="ln"><span>How you</span></span><span class="ln"><span>will learn.</span></span></h1>
<p class="le-lead">A structured, project-based learning experience. Learn by doing, get regular practice, sit real exams and build a portfolio that shows what you can do.</p>
<div class="le-actions"><a class="le-btn le-btn--p" href="/programs">Explore programs {ARW}</a><a class="le-btn le-btn--s" href="/contact">Talk to us</a></div></div>
<div class="le-hero-art" aria-hidden="true"><span class="le-glow g1"></span><span class="le-glow g2"></span><img class="le-stair" src="/assets/r-hero.webp" srcset="/assets/r-hero-600.webp 600w, /assets/r-hero-800.webp 800w, /assets/r-hero.webp 1200w" sizes="(max-width: 900px) 80vw, 560px" alt="" width="1000" height="1000" fetchpriority="high"><p class="le-note">From concepts<br>to real skills</p><svg class="le-note-arrow" viewBox="0 0 90 40"><path d="M2 8 C30 2 60 6 80 28" fill="none" stroke="#7D8DA6" stroke-width="1.6" pathLength="1"/><path d="M72 28 L81 30 L80 20" fill="none" stroke="#7D8DA6" stroke-width="1.6"/></svg></div></div></section>'''
    steps = [("book", "Concept", "One idea, explained simply."), ("play", "Worked example", "See it done before you do it."), ("doc", "Scenario question", "Choose the best answer in a real situation."), ("code", "Guided practice", "Try it with support close by."), ("chart", "Exit check", "Confirm you are ready to move on.")]
    st = "".join(f'<li class="le-step" style="--i:{i}"><span class="le-step-n">Step {i+1:02d}</span><span class="le-step-ic">{li(ic)}</span><h3>{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate(steps))
    lesson = f'''<section class="le-sec" data-le-steps><div class="wrap"><div class="le-head"><div>{le_eyebrow("From theory to real skills")}<h2>Five steps<br>in every lesson.</h2></div>
<p class="le-head-p">Every lesson follows the same flow, so you always know what comes next. You learn a concept, work through it, practise it, answer a question on your own and finish with a quick check.</p></div>
<div class="le-track"><div class="le-line" aria-hidden="true"><i></i><b></b></div><span class="le-track-end" aria-hidden="true">{ARW}</span><ol class="le-steps">{st}</ol></div>
<p class="le-foot">AI Foundation: 4 guided hours a week for 104 hours, plus 10 to 15 minutes of homework after each lecture.</p></div></section>'''
    beats = [("play", "Theory", "Short explanations of the month's topic."), ("check", "Demonstration", "An instructor works through an example on screen."), ("tools", "Hands-on lab", "You repeat and extend it yourself."), ("image", "Project", "A piece of work you finish and can show."), ("clock", "Exam", "A one-hour exam closes the month.")]
    bt = "".join(f'<li class="le-beat" style="--i:{i}"><div class="le-beat-top"><span class="le-beat-n">{i+1:02d}</span><span class="le-beat-ic">{li(ic, 24)}</span></div><h3>{t}</h3><p>{d}</p></li>' for i, (ic, t, d) in enumerate(beats))
    month = f'''<section class="le-sec le-sec--tint" data-le-beats><div class="wrap"><div class="le-head"><div>{le_eyebrow("A structured three-year program")}<h2>Five beats<br>in every month.</h2></div>
<p class="le-head-p">A project every month, followed by an online evaluation.</p></div>
<div class="le-beats-wrap"><ol class="le-beats">{bt}</ol><span class="le-track-end le-track-end--b" aria-hidden="true">{ARW}</span></div></div></section>'''
    code = [("c", "# Calculate accuracy"), ("k", "def calculate_accuracy(y_true, y_pred):"), ("", "    correct = sum(1 for a, b in zip(y_true, y_pred)"), ("", "                  if a == b)"), ("k", "    return correct / len(y_true)"), ("", ""), ("c", "# Example usage"), ("", "y_true = [0, 1, 1, 0, 1]"), ("", "y_pred = [0, 1, 1, 0, 0]"), ("", "print(calculate_accuracy(y_true, y_pred))")]
    cl = "".join(f'<span class="cl{" " + t if t else ""}" style="--l:{i}"><em>{i+1}</em>{E(s) or "&nbsp;"}</span>' for i, (t, s) in enumerate(code))
    tests = "".join(f'<li style="--t:{i}"><span class="tk" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>Test {i+1}<span class="ps">Passed</span></li>' for i in range(4))
    lab = f'''<section class="le-sec le-lab" data-le-lab><div class="wrap le-lab-grid"><div>{le_eyebrow("Practical, hands-on", True)}<h2>Labs with<br>checked work.</h2>
<p class="le-head-p" style="margin-top:16px">Solve real tasks in a lab environment. Run your code, see what passed, fix issues and try again.</p>
<a class="le-btn le-btn--p" style="margin-top:26px" href="/curriculum">See the curriculum {ARW}</a><p class="le-small">The same lab runs across all six programs: browser-based coding, automatic checks on every task, hints when you are stuck, and labs you can reset and retry.</p></div>
<div class="le-lab-vis" aria-label="Design sample of a lab: code editor and test results" role="img"><div class="le-ed"><div class="le-ed-bar"><i></i><i></i><i></i><span>scorer.py</span><b>Run</b></div><pre aria-hidden="true">{cl}</pre></div>
<div class="le-res" aria-hidden="true"><div class="le-res-tabs"><span class="on">Results</span><span>Tests</span><span>Feedback</span></div><div class="le-res-body"><ul class="le-tests">{tests}</ul><div class="le-pass"><span class="le-pass-ic">{li("check", 26)}</span><b>All tests passed!</b><small>Score 100 / 100 · first attempt</small></div></div></div></div></div></section>'''
    req = ["A laptop or desktop computer", "A stable internet connection", "A web browser", "Python installed, or a browser-based notebook", "A phone alone is not enough for the programming labs"]
    rq = "".join(f'<li style="--i:{i}"><span class="tk" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>{E(x)}</li>' for i, x in enumerate(req))
    need = f'''<section class="le-sec" data-le-need><div class="wrap le-need-grid"><div>{le_eyebrow("All you need to start")}<h2>A laptop<br>and internet.</h2><p class="le-head-p" style="margin-top:16px">You need a computer with a browser and a stable connection for lessons, labs and course material.</p></div>
<div><ul class="le-req">{rq}</ul><a class="le-link" href="/programs/ai-foundation">View detailed requirements {ARW}</a><p class="le-small" style="margin-top:8px">Setup for AI Foundation. Each three-year program lists its own on its program page.</p></div>
<div class="le-laptop" aria-hidden="true" data-frames="24"><span class="le-laptop-floor"></span><img src="/assets/lap-23.webp" alt="" width="640" height="494" loading="lazy"></div></div></section>'''
    cta = f'''<section class="le-sec" style="padding-top:0"><div class="wrap"><div class="le-cta" data-le-cta><div class="le-cta-body">{le_eyebrow("See it for yourself", True)}<h2>Want to see how a class works?</h2>
<p>Ask us about the learning experience. Classes are online. Batch timings are shared on enquiry.</p><div class="le-actions"><a class="le-btn le-btn--w" href="/contact">Book a call {ARW}</a><a class="le-btn le-btn--g" href="/contact">Talk to us</a></div></div>
<div class="le-cta-art" aria-hidden="true"><img src="/assets/r-full.webp" alt="" width="600" height="600" loading="lazy"></div></div></div></section>'''
    return layout("/learning-experience", "Learning Experience", hero + lesson + month + lab + need + cta, "learning")

def projects_page():
    pbs = "".join(f'<button class="chip" type="button" data-pj-prog="{p[1]}" data-years="{len(D[p[0]]["years"])}" aria-pressed="{"true" if p[1]=="aiml" else "false"}">{name_of(p)} · {len(D[p[0]]["projects"])}</button>' for p in PROGRAMS)
    items = ""
    for p in PROGRAMS:
        d = D[p[0]]; k = p[1]; n = len(d["projects"]); multi = len(d["years"]) > 1
        for i, x in enumerate(d["projects"]):
            y = i // 12 + 1 if multi else 1
            tag = f"Year {y} · Month {i+1}" if multi else f"Project {i+1}"
            items += f'<a class="pj" data-p="{k}" data-y="{y}" href="/curriculum#{k}-y{y}" hidden><small>{tag}</small><h3>{E(x)}</h3></a>'
    feats = [("Image classification application", "AI/ML Engineering · Year 2", True), ("Document RAG assistant", "AI/ML Engineering · Year 3", False), ("Tool-using AI agent", "AI/ML Engineering · Year 3", False)]
    fc = "".join(f'<a class="fcard rv{" big" if b else ""}" href="/curriculum#aiml-y{2 if b else 3}"><div class="shot">{shot(1 if "mage" in n else 2 if "gent" in n else 0)}</div><div class="cap"><span class="tag">{y}</span><h3>{n}</h3></div></a>' for k, (n, y, b) in enumerate(feats))
    body = page_hero("Projects", "Things you", "build.", "Every program is built around projects. These names come from the program roadmaps. Student work appears here once the institute supplies and approves it.", btn("primary", "#all", "Browse all projects") + btn("secondary", "/curriculum", "See the curriculum", False))
    body += featured_projects().replace('href="/projects">View all projects', 'href="#all">Browse all projects')
    body += f'''<section class="sec sec--tint" id="all"><div class="wrap" id="pj">{sec_head("All projects", "By program and year.", "Choose a program, then a year. Each project links to its month in the curriculum.")}
<div class="chips" role="group" aria-label="Program">{pbs}</div><div class="chips" id="pj-years" role="group" aria-label="Year" style="margin-top:12px"><button class="chip" type="button" data-pj-year="all" aria-pressed="true">All years</button><button class="chip" type="button" data-pj-year="1" aria-pressed="false">Year 1</button><button class="chip" type="button" data-pj-year="2" aria-pressed="false">Year 2</button><button class="chip" type="button" data-pj-year="3" aria-pressed="false">Year 3</button></div>
<p id="pj-count" class="mono muted" role="status" style="margin:28px 0 16px">&nbsp;</p><div class="pj-list">{items}</div><div class="more"><button id="pj-more" class="btn btn-secondary" type="button">Show more projects</button></div></div></section>''' + cta_panel("Build yours.", "Tell us which program interests you. Ask us about fees and intake dates.")
    return layout("/projects", "Projects", body, "projects")

AVATAR = '<svg class="tm-sil" viewBox="0 0 120 120" aria-hidden="true"><circle cx="60" cy="46" r="22" fill="#fff" fill-opacity=".85"/><path d="M18 118c4-26 22-40 42-40s38 14 42 40z" fill="#fff" fill-opacity=".85"/></svg>'
def team_page():
    people = "".join(f'<article class="tm-card" style="--k:{i}"><div class="tm-av">{AVATAR}<span class="tm-ph">[Photo to be supplied]</span></div><div class="tm-t"><h3>[Name]</h3><p class="tm-role">[Role and subject]</p><p class="tm-bg">[Two-line background, verified credentials only]</p><span class="tm-prog">[Programs taught]</span></div></article>' for i in range(8))
    areas = "".join(f'<a class="tm-area" href="/programs/{p[0]}" style="--k:{i}"><img src="/assets/i-{ICON[p[0]]}.webp" alt="{E(ICON_ALT[p[0]])}" width="56" height="56" loading="lazy"><span><b>{name_of(p)}</b><small>{p[4]} · {p[3]} hours</small></span><span class="go">{ARW}</span></a>' for i, p in enumerate(PROGRAMS))
    orbit = "".join(f'<span class="tm-orb o{i}">{AVATAR}</span>' for i in range(5))
    hero = f"""<section class="tm-hero" data-pd><div class="wrap tm-hero-grid"><div><p class="pd-crumbs"><a href="/">Home</a> / <span>Faculty and team</span></p>{eb("Faculty and team")}<h1 class="ad-h1"><span class="ln"><span>The people</span></span><span class="ln"><span>who teach.</span></span></h1>
<p class="ab-lead">Names, roles and credentials appear here once they are confirmed. We do not use stock photos or generated faces.</p><div class="pd-actions"><a class="le-btn le-btn--p" href="/contact">Talk to us {ARW}</a><a class="le-btn le-btn--s" href="/programs">Explore programs</a></div></div>
<div class="tm-hero-art" aria-hidden="true"><span class="tm-ring r1"></span><span class="tm-ring r2"></span><img class="tm-core" src="/assets/i-aiml.webp" alt="" width="340" height="360">{orbit}<div class="fq-bubble b2"><b>Profiles coming soon</b><small>Verified credentials only</small></div></div></div></section>"""
    rules = "".join(f'<li style="--k:{i}"><span class="ic">{pi(ic,22)}</span><b>{a}</b><small>{b}</small></li>' for i, (ic, a, b) in enumerate([("check", "Verified credentials only", "Nothing is listed until it is confirmed."), ("user", "Real people, real photos", "No stock photos or generated faces."), ("link", "Linked to programs", "Each profile shows the programs they teach.")]))
    lead = f"""<section class="pd-sec" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Leadership")}<h2>Who leads the programs.</h2></div><p class="pd-p">[Leadership names, roles and a short note to be supplied.]</p></div>
<div class="tm-lead"><div class="tm-av tm-av--lg">{AVATAR}<span class="tm-ph">[Photo to be supplied]</span></div><div class="tm-lead-t"><span class="pd-tag">Leadership</span><h3>[Name]</h3><p class="tm-role">[Role]</p><p>[Leadership names, roles and a short note to be supplied.]</p><ul class="tm-rules">{rules}</ul></div></div></div></section>"""
    fac = f"""<section class="pd-sec pd-sec--tint" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Faculty")}<h2>Instructors and mentors.</h2></div><p class="pd-p">[Faculty and mentor names and credentials to be confirmed, or this section is removed.]</p></div><div class="tm-grid">{people}</div></div></section>"""
    area = f"""<section class="pd-sec" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Teaching areas")}<h2>Find the program.</h2></div><p class="pd-p">Each faculty profile will link to the programs they teach. Until then, explore the programs directly.</p></div><div class="tm-areas">{areas}</div></div></section>"""
    cta = f"""<section class="pd-sec" style="padding-top:0" data-pd><div class="wrap"><div class="pd-cta">{eb("Your next step")}<h2>Want to meet the faculty?</h2><p>Ask us. Classes are online. Batch timings are shared on enquiry.</p><div class="pd-actions"><a class="le-btn le-btn--w" href="/contact">Talk to us {ARW}</a><a class="le-btn le-btn--g" href="/programs">Explore programs</a></div><img class="pd-cta-art" src="/assets/i-banner.webp" alt="" aria-hidden="true" width="609" height="419" loading="lazy"></div></div></section>"""
    return layout("/faculty-and-team", "Faculty and Team", hero + lead + fac + area + cta, "about")

def admissions_page():
    ents = {p[0]: D[p[0]]["entry"] for p in PROGRAMS}
    steps = [("chat", "Talk to us", "Ask any question about the programs. A specialist responds.", "We reply by email to the address you give."), ("doc", "Apply", "Use the Apply form. Students under 18 apply through a parent or guardian.", ""), ("flow", "What happens next", "We reply with the next steps, intake dates and batch details for your program.", "")]
    st = "".join(f'<li style="--k:{i}"><span class="ad-node"><b>{i+1:02d}</b></span><div class="ad-step"><span class="ic">{pi(ic,22)}</span><h3>{a}</h3><p>{b}</p>{f"<small>{c}</small>" if c else ""}</div></li>' for i, (ic, a, b, c) in enumerate(steps))
    rows = "".join(f'<tr style="--k:{i}"><td data-l="Program"><a class="ad-prog" href="/programs/{p[0]}"><img src="/assets/i-{ICON[p[0]]}.webp" alt="{E(ICON_ALT[p[0]])}" width="40" height="40" loading="lazy"><span><b>{name_of(p)}</b><small>{"Start here" if i == 0 else "Specialisation"}</small></span></a></td><td data-l="Length">{p[4]}</td><td data-l="Hours"><b class="ad-h">{p[3]}</b></td><td data-l="Entry">{E(ents[p[0]])}</td><td data-l="Fees"><a class="ad-enq" href="/contact?topic=fees">Enquire</a></td><td data-l="Next intake" class="muted">{FEE}</td></tr>' for i, p in enumerate(PROGRAMS))
    path = "".join(f'<li style="--k:{i}"><span class="d">{TICK if i < 2 else ""}</span><div><b>{a}</b><small>{b}</small></div></li>' for i, (a, b) in enumerate([("Talk to us", "Ask anything"), ("Apply", "Online form"), ("What happens next", "We reply by email")]))
    hero = f"""<section class="ad-hero" data-pd><div class="wrap ad-hero-grid"><div><p class="pd-crumbs"><a href="/">Home</a> / <span>Admissions</span></p>{eb("Admissions and fees")}<h1 class="ad-h1"><span class="ln"><span>Join</span></span><span class="ln"><span>the next step.</span></span></h1>
<p class="ab-lead">AI Foundation is open from Class 9; the three-year programs are open from Class 11. Ask us about fees and intake dates.</p><div class="pd-actions"><a class="le-btn le-btn--p" href="/contact">Apply {ARW}</a><a class="le-btn le-btn--s" href="/contact">Talk to us</a></div></div>
<div class="ad-hero-art" aria-hidden="true"><img class="ad-steps-img" src="/assets/i-banner.webp" alt="" width="609" height="419"><div class="ad-card"><p class="ad-card-h">Your path to joining</p><ol class="ad-path">{path}</ol><div class="ad-card-f"><span>Entry</span><b>Class 9 / Class 11</b></div></div></div></div></section>"""
    how = f"""<section class="pd-sec" data-pd data-ad-track><div class="wrap"><div class="pd-head"><div>{eb("How to apply")}<h2>Three steps.</h2></div><p class="pd-p">A short, simple path. Ask first if you are not sure which program fits.</p></div><div class="ad-steps-wrap"><span class="ad-line" aria-hidden="true"><i></i></span><ol class="ad-steps">{st}</ol></div></div></section>"""
    table = f"""<section class="pd-sec pd-sec--tint" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Eligibility, fees and intakes")}<h2>By program.</h2></div><p class="pd-p">Compare entry requirements and intakes, and enquire about fees. Open a program for its modules and projects.</p></div>
<div class="ad-table"><table class="cmp"><caption class="sr">Eligibility, fees and intake by program</caption><thead><tr><th scope="col">Program</th><th scope="col">Length</th><th scope="col">Hours</th><th scope="col">Entry</th><th scope="col">Fees</th><th scope="col">Next intake</th></tr></thead><tbody>{rows}</tbody></table></div></div></section>"""
    li_s = "".join(f"<li>{TICK}<span>{x}</span></li>" for x in ["You are in Class 9 or above for AI Foundation, or Class 11 or above for a three-year program.", "You have a laptop or desktop with internet. See each program page for its recommended setup.", "You know which program you are interested in, or you are happy to ask us."])
    li_p = "".join(f"<li>{TICK}<span>{x}</span></li>" for x in ["A parent or guardian applies and gives consent.", "We collect only what is needed to respond, use unticked consent boxes, and do not track or advertise to children. See our <a href='/privacy'>privacy policy</a>.", "At admission we ask for the student's latest marksheet, a photo ID for the student and for the parent or guardian, and a signed consent form. Nothing else.", "Enquiry details are deleted 12 months after our last contact if you do not join. A parent can ask us to delete them sooner by writing to <a href='mailto:Hussain@neuronetwrks.com'>Enquire@neuronetwrks.com</a>."])
    before = f"""<section class="pd-sec" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Before you apply")}<h2>Students first,<br>parents informed.</h2></div><p class="pd-p">What to check before you send the form, whether you are the student or a parent or guardian.</p></div>
<div class="ad-two"><div class="ad-box" style="--k:0"><div class="ad-box-h"><span class="ic">{pi("user",22)}</span><div><small>For students</small><h3>Before you apply.</h3></div></div><ul class="ad-list">{li_s}</ul><a class="le-link" href="/programs">Compare programs {ARW}</a></div>
<div class="ad-box ad-box--alt" style="--k:1"><div class="ad-box-h"><span class="ic">{pi("shield",22)}</span><div><small>For parents and guardians</small><h3>Applying for a student under 18.</h3></div></div><ul class="ad-list">{li_p}</ul><a class="le-link" href="/faqs#privacy">Privacy questions {ARW}</a></div></div></div></section>"""
    qs = [("Who is eligible to join?", "<p>All five three-year programs are designed for students from Class 11 onwards. The six-month AI Foundation course is open from Class 9, with no prior coding, AI or cloud experience needed.</p>"), ("How do I apply?", "<p>Use the Apply form on this site. We reply by email with the next steps.</p>"), ("Do the programs guarantee a job or internship?", "<p>No. The programs aim at job readiness through skills, hands-on practice, a GitHub record and a portfolio, but no internship, employment or salary is guaranteed.</p>")]
    faq = f"""<section class="pd-sec pd-sec--tint" data-pd><div class="wrap ad-faq"><div>{eb("Questions")}<h2>Admissions FAQ.</h2><p class="pd-p">Short answers to what most families ask first.</p><a class="le-link" href="/faqs#admissions">All admissions questions {ARW}</a></div><div class="ad-faq-list">{faq_items(qs)}</div></div></section>"""
    cta = f"""<section class="pd-sec" style="padding-top:clamp(40px,4vw,64px)" data-pd><div class="wrap"><div class="pd-cta">{eb("Your next step")}<h2>Ready to apply?</h2><p>Tell us which program interests you. Ask us about fees and intake dates.</p><div class="pd-actions"><a class="le-btn le-btn--w" href="/contact">Apply {ARW}</a><a class="le-btn le-btn--g" href="/contact">Talk to us</a></div><img class="pd-cta-art" src="/assets/i-banner.webp" alt="" aria-hidden="true" width="609" height="419" loading="lazy"></div></div></section>"""
    return layout("/admissions", "Admissions and Fees", hero + how + table + before + faq + cta, "admissions")

FAQ_CATS = [("all", "All"), ("admissions", "Admissions"), ("learning", "Learning"), ("certification", "Certification"), ("outcomes", "Outcomes"), ("privacy", "Privacy"), ("program", "AI/ML program")]
FAQ_LINKS = {"admissions": ('/admissions', "Admissions details"), "learning": ('/learning-experience', "How learning works"), "certification": ('/programs/ai-ml-engineering', "See certification pathways"),
             "outcomes": ('/projects', "See the projects"), "privacy": ('/contact', "Contact us about privacy"), "program": ('/curriculum#aiml-y1', "See the curriculum")}

FAQ_ICONS = {"all": "grid", "admissions": "doc", "learning": "box", "certification": "check", "outcomes": "target", "privacy": "shield", "program": "cpu"}
def faq_page():
    its = []
    for f in FAQ_FILES:
        d = yaml.safe_load(open(f)); its.append((d["group"], E(d["q"]), E(conf(d["a"]))))
    for q in D["ai-ml-engineering"]["faqs"][:3]: its.append(("program", E(q["q"]), E(conf(q["a"]))))
    counts = {c: sum(1 for i in its if i[0] == c) for c, _ in FAQ_CATS if c != "all"}; counts["all"] = len(its)
    chips = "".join(f'<button class="fq-cat" type="button" data-faq-cat="{c}" aria-pressed="{"true" if c=="all" else "false"}"><span class="ic">{pi(FAQ_ICONS[c],17)}</span><span class="t">{n}</span><span class="c">{counts[c]}</span></button>' for c, n in FAQ_CATS)
    names = dict(FAQ_CATS)
    det = ""
    for k, (c, q, a) in enumerate(its):
        href, lbl = FAQ_LINKS[c]
        det += f'<details class="fq-item" data-cat="{c}" style="--k:{k}"><summary><span class="fq-tag">{names[c]}</span><span class="fq-q">{q}</span><span class="fq-pm" aria-hidden="true"></span></summary><div class="ans"><p>{a}</p><a class="le-link" href="{href}">{lbl} {ARW}</a></div></details>'
    hero = f"""<section class="fq-hero" data-pd><div class="wrap fq-hero-grid"><div><p class="pd-crumbs"><a href="/">Home</a> / <span>FAQs</span></p>{eb("Frequently asked questions")}<h1 class="ad-h1"><span class="ln"><span>Got questions?</span></span><span class="ln"><span>We have answers.</span></span></h1>
<p class="ab-lead">Straight answers from the program roadmaps. Where something is not confirmed yet, it says so.</p>
<label class="fq-search"><span class="sr">Search the questions</span>{pi("search",20)}<input id="faq-q" type="search" placeholder="Search questions, e.g. eligibility, hours, exams" autocomplete="off"></label></div>
<div class="fq-hero-art" aria-hidden="true"><img src="/assets/i-aiml.webp" alt="" width="340" height="360"><div class="fq-bubble b1"><b>Who can apply?</b><small>AI Foundation from Class 9; specialisations from Class 11.</small></div><div class="fq-bubble b2"><b>How long is AI/ML?</b><small>624 hours over 3 years.</small></div></div></div></section>"""
    main = f"""<section class="pd-sec" data-pd><div class="wrap fq-grid" id="faq"><aside class="fq-side"><p class="fq-side-h">Categories</p><div class="fq-cats" role="group" aria-label="Question categories">{chips}</div>
<div class="fq-ask"><span class="ic">{pi("chat",22)}</span><b>Still have a question?</b><p>Ask us. A specialist responds.</p><a class="le-btn le-btn--p" href="/contact">Ask us something {ARW}</a></div></aside>
<div class="fq-main"><div class="fq-bar"><p id="faq-count" class="fq-count" role="status">{len(its)} questions</p></div><div class="fq-list">{det}</div><p class="fq-empty" hidden>No questions match. Try another word or <a href="/contact">ask us directly</a>.</p></div></div></section>"""
    return layout("/faqs", "FAQs: eligibility, hours, certificates and how to apply", hero + main + cta_panel("Still have a question?", "Ask us. A specialist responds."), "none")

CT_FORM = r'''<div id="err-sum" class="err-sum" role="alert" hidden></div>
<form id="enq" class="form" novalidate>
<fieldset class="ct-fs"><legend><span class="ct-n">1</span>About you</legend><div class="field"><span class="lbl" id="role-l">I am</span><div class="radios" role="radiogroup" aria-labelledby="role-l"><label class="radio"><input type="radio" name="role" value="parent" checked> a parent or guardian</label><label class="radio"><input type="radio" name="role" value="under"> a student under 18</label><label class="radio"><input type="radio" name="role" value="adult"> a student aged 18 or over</label></div></div>
<div id="under" class="notice" hidden><strong>Please ask a parent or guardian to send this form.</strong> Students under 18 apply through a parent or guardian, who gives consent.</div>
<div class="field"><label for="f-name">Your name</label><input id="f-name" class="inp" autocomplete="name" placeholder="Full name" aria-describedby="m-name"><p id="m-name" class="msg"></p></div>
<div class="field"><label for="f-email">Email</label><input id="f-email" class="inp" type="email" autocomplete="email" placeholder="name@example.com" aria-describedby="m-email"><p id="m-email" class="msg"></p></div>
<div class="field"><label for="f-phone">Phone <span class="opt">(optional)</span></label><input id="f-phone" class="inp" type="tel" autocomplete="tel" placeholder="Phone number"></div></fieldset>
<fieldset class="ct-fs"><legend><span class="ct-n">2</span>Your enquiry</legend><div class="field"><label for="f-prog">Program</label><select id="f-prog" class="inp" aria-describedby="m-prog"><option value="">Choose a program</option>{opts}<option value="unsure">Not sure yet</option></select><p id="m-prog" class="msg"></p></div>
<div class="field"><label for="f-msg">Your question <span class="opt">(optional)</span></label><textarea id="f-msg" class="inp" placeholder="What would you like to know?"></textarea></div></fieldset>
<fieldset class="ct-fs"><legend><span class="ct-n">3</span>Consent</legend><div class="field"><label class="agree"><input id="f-consent" type="checkbox" aria-describedby="m-consent"><span>I agree that Neuronetworks AI Ed may use these details to reply to my enquiry. <a href="/privacy" style="color:var(--blue-text)">Privacy policy</a></span></label><p id="m-consent" class="msg"></p></div></fieldset>
<div><button id="send" class="btn btn-primary" type="submit">Send enquiry <i aria-hidden="true">→</i></button></div></form>
<div id="ok" class="ok"><h2 class="h3">Your email app should now be open.</h2><p class="lead" style="margin-top:12px">Press send in your email app to complete your enquiry. If nothing opened, write to <a href="mailto:Hussain@neuronetwrks.com" style="color:var(--blue-text)">Enquire@neuronetwrks.com</a>.</p><div class="actions" style="margin-top:24px"><button id="again" class="btn btn-secondary" type="button">Try again</button><a class="btn btn-primary" href="/programs">Browse programs <i aria-hidden="true">→</i></a></div></div>'''

def contact_page():
    opts = "".join(f'<option value="{p[0]}">{name_of(p)}</option>' for p in PROGRAMS)
    FORM_HTML = CT_FORM.replace('{opts}', opts)
    topics = "".join(f'<a class="ct-topic" href="{h}">{pi(ic,16)}{t}</a>' for ic, t, h in [("cpu", "Programs", "/programs"), ("doc", "Fees", "/contact?topic=fees#enq"), ("check", "Admissions", "/admissions"), ("box", "Learning", "/learning-experience")])
    path = "".join(f'<li><span class="d">{i+1}</span><div><b>{a}</b><small>{b}</small></div></li>' for i, (a, b) in enumerate([("Send your enquiry", "From your email app"), ("A specialist reads it", "Not a chatbot"), ("We reply", "By email, with the next steps")]))
    hero = f"""<section class="ct-hero" data-pd><div class="wrap ct-hero-grid"><div><p class="pd-crumbs"><a href="/">Home</a> / <span>Contact</span></p>{eb("Contact")}<h1 class="ad-h1"><span class="ln"><span>Talk to us.</span></span><span class="ln"><span>A specialist responds.</span></span></h1>
<p class="ab-lead">Ask about a program, fees or how to apply. Students under 18 send this through a parent or guardian.</p><div class="ct-topics">{topics}</div></div>
<div class="ct-hero-art" aria-hidden="true"><img src="/assets/i-contact-envelope.webp" alt="" width="640" height="546"><div class="fq-bubble b1"><b>Hi! Which program fits me?</b><small>Ask us anything.</small></div><div class="fq-bubble b2"><b>A specialist responds.</b><small>No chatbot.</small></div></div></div></section>"""
    aside = f"""<aside class="ct-aside"><div class="ct-info"><p class="ct-info-h">Reach us directly</p><a class="ct-mail" href="mailto:Hussain@neuronetwrks.com"><span class="ic">{pi("chat",20)}</span><span><small>Email</small><b>Enquire@neuronetwrks.com</b></span></a>
<dl class="ct-dl"><div><dt>{pi("map",16)} Where</dt><dd>Online classes, India</dd></div><div><dt>{pi("history",16)} Reply</dt><dd>By email, from a specialist</dd></div></dl>
<p class="ct-info-h" style="margin-top:26px">What happens next</p><ol class="ct-path">{path}</ol></div>
<div class="ct-priv"><span class="ic">{pi("shield",18)}</span><p>We collect only what is needed to reply, and never advertise to children.</p></div></aside>"""
    body = hero + f"""<section class="pd-sec ct-sec" data-pd><div class="wrap ct-grid">{aside}<div class="ct-form">""" + FORM_HTML + """</div></div></section>
<section class="pd-sec pd-sec--tint pd-sec--tight" data-pd><div class="wrap"><ul class="ct-links">""" + "".join(f'<li><a href="{h}"><span class="ic">{pi(ic,22)}</span><b>{t}</b><small>{d}</small><span class="go">{ARW}</span></a></li>' for ic, t, d, h in [("info", "Read the FAQs", "Straight answers to common questions", "/faqs"), ("check", "Admissions", "Eligibility, steps and intakes", "/admissions"), ("grid", "Compare programs", "Six programs side by side", "/programs")]) + """</ul></div></section>"""
    return layout("/contact", "Contact Neuronetworks AI Ed: ask about a program", body.replace("{FORM}", ""), "none")

# ---------------------------------------------------------------- write
exec(open(os.path.join(HERE, 'projects_pages.py')).read())
exec(open(os.path.join(HERE, 'guides_pages.py')).read())
exec(open(os.path.join(HERE, 'career_pages.py')).read())
exec(open(os.path.join(HERE, 'seo_pages.py')).read())
exec(open(os.path.join(HERE, 'legal_pages.py')).read())
exec(open(os.path.join(HERE, 'og_images.py')).read())

def about_page():
    tags = [("Curious minds", 6, 78), ("Practical learning", 22, 44), ("Real projects", 74, 34), ("A stronger tomorrow", 60, 4)]
    tg = "".join(f'<span class="ab-tag" style="left:{x}%;top:{y}%;--k:{i}"><i></i>{t}</span>' for i, (t, x, y) in enumerate(tags))
    hero = f'''<section class="ab-hero" data-pd><div class="wrap ab-hero-grid"><div class="ab-hero-copy"><p class="pd-eb">About Neuronetworks AI Ed</p>
<h1 class="ab-h1"><span class="ln"><span>Learn.</span></span><span class="ln"><span>Develop.</span></span><span class="ln"><span>Create.</span></span></h1>
<p class="ab-lead">Neuronetworks AI Ed Private Limited provides advanced skill training through a structured curriculum and industry-relevant, collaborative problem-solving projects, in five streams of Super Intelligence, also known as Artificial Intelligence.</p>
<div class="pd-actions"><a class="le-btn le-btn--p" href="/learning-experience">Our approach {ARW}</a><a class="le-btn le-btn--s" href="/programs">Explore programs</a></div></div>
<div class="ab-hero-art" aria-hidden="true"><span class="ab-glow"></span><img class="ab-stair" src="/assets/r-hero.webp" srcset="/assets/r-hero-600.webp 600w, /assets/r-hero-800.webp 800w, /assets/r-hero.webp 1200w" sizes="(max-width: 900px) 80vw, 560px" alt="" width="1000" height="1000" fetchpriority="high">{tg}</div></div></section>'''
    stats = "".join(f'<div style="--k:{i}"><small>{a}</small><b>{b}</b></div>' for i, (a, b) in enumerate([("Programs", "6"), ("Hours", "104 to 624"), ("Entry", "Class 9 / Class 11")]))
    story = f'''<section class="ab-sec ab-story2" data-pd><svg class="ab-arc" viewBox="0 0 600 400" aria-hidden="true"><path d="M-40 380 C80 140 300 120 560 260" fill="none" stroke="#D6E3F5" stroke-width="1.5"/><path d="M-60 400 C60 200 260 170 520 300" fill="none" stroke="#E3EBF7" stroke-width="1.2"/><circle cx="150" cy="215" r="6" fill="#7EE04A"/></svg><div class="wrap ab-st-grid"><div><p class="ab-eb2">Who we are</p><h2>Our story.</h2></div>
<div><div class="ab-st-card" style="--k:0"><p>We aim to teach critical, up-to-date Super Intelligence skills to students from Class 9 onwards, undergraduate students and working professionals. Our learners improve their skills, prepare for industry-recognised certifications and improve their chances of employment across industries, including but not limited to IT and ITES.</p><p style="margin-top:12px">The gaps in the education system deprive learners of these critical skills. This skill gap differentiates a professional who has industry-relevant skills, and is therefore employable, from a professional who has not acquired them. We at Neuronetworks aspire to skill those who are willing, so that they are either employment-ready or able to pursue entrepreneurship.</p><p style="margin-top:12px"><b>Our five streams:</b> <a href="/programs/software-development">Software Development</a>, <a href="/programs/ai-ml-engineering">AI/ML Engineering</a>, <a href="/programs/data-science-ai">Data Science &amp; AI</a>, <a href="/programs/cybersecurity">Cybersecurity</a> and <a href="/programs/product-ux-ai-design">Product and UX/UI Design</a>, with the <a href="/programs/ai-foundation">AI Foundation</a> course as the first step.</p></div><div class="ab-st-stats">{stats}</div></div></div></section>'''
    pr = [("box", "Hands-on learning", "Learn by doing, with labs and projects in every month."), ("check", "Checked progress", "A one-hour exam closes every module, with review and a retry."), ("chart", "Real-world skills", "Build a portfolio that shows what you can do."), ("bolt", "Open to beginners", "Start from Class 9. No prior coding or AI experience needed.")]
    cards = "".join(f'<li style="--k:{i}"><span class="n">{i+1:02d}</span><span class="ic">{pi(ic,24)}</span><h3>{a}</h3><p>{b}</p></li>' for i, (ic, a, b) in enumerate(pr))
    words = "We skill as many willing people as possible in the five streams of Super Intelligence, so they can gain employment or start their own venture.".split()
    manifesto = '<section class="ab-mani" data-ab-mani><div class="wrap"><p class="ab-mani-eb">Our mission</p><p class="ab-mani-t">' + " ".join(f'<span style="--i:{i}">{w}</span>' for i, w in enumerate(words)) + '</p></div></section>'
    bento = "".join(f'<li class="b{i}" style="--k:{i}"><span class="n">{i+1:02d}</span><span class="ic">{pi(ic,24)}</span><h3>{a}</h3><p>{b}</p></li>' for i, (ic, a, b) in enumerate(pr))
    principles = f'''<section class="ab-sec ab-sec--tint" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Our principles")}<h2>Practical. Measured.<br>Future-ready.</h2></div><p class="pd-p">Four principles guide everything we do at Neuronetworks AI Ed.</p></div><ol class="ab-bento">{bento}</ol></div></section>'''
    env = f'''<section class="ab-sec" data-pd><img class="ab-wind ab-wind--2" src="/assets/r-full.webp" alt="" width="600" height="600" loading="lazy" aria-hidden="true"><div class="wrap ab-env-grid"><div>{eb("Students first")}<h2>A clear learning<br>environment.</h2>
<p class="pd-p">Hours, assessments and projects are published in full, so students and parents can see exactly what each month involves. Students under 18 apply through a parent or guardian.</p>
<div class="pd-actions"><a class="le-link" href="/admissions">Admissions for parents {ARW}</a></div><p class="le-small">Class sizes and mentor support are shared on enquiry.</p></div>
<div class="ab-photo ab-photo--wide ab-photo--real"><img src="/assets/students.webp" alt="Teenage students learning together in a classroom" width="1400" height="933" loading="lazy"><div class="ab-chip ab-chip--r"><i></i>Learn together.<br>Build together.</div></div></div></section>'''
    big = [("cap", "Real skills", "For higher education and careers"), ("target", "Greater opportunities", "In a technology-driven world"), ("user", "Capable people", "Curious, confident builders")]
    PI.setdefault("cap", '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5M22 9v6"/>')
    bg = "".join(f'<li style="--k:{i}"><span class="ic">{pi(ic,26)}</span><b>{a}</b><small>{b}</small></li>' for i, (ic, a, b) in enumerate(big))
    bigger = f'''<section class="ab-sec ab-dark" data-pd><div class="wrap ab-big-grid"><div>{eb("The bigger picture")}<h2>Better people.<br>A brighter tomorrow.</h2><p class="pd-p">We believe technology education can open doors and help build a more capable, confident generation. No program guarantees a job, internship or salary: we teach skills and help you build a portfolio.</p></div><ul class="ab-big">{bg}</ul></div></section>'''
    cta = f'''<section class="ab-cta" data-pd><div class="wrap"><div class="ab-cta-in"><div>{eb("Be part of our story")}<h2>Talk to the people behind it.</h2><p>Ask us about our approach, programs, fees and intake dates.</p>
<div class="pd-actions"><a class="le-btn le-btn--w" href="/admissions">Apply now {ARW}</a><a class="le-btn le-btn--g" href="/contact">Talk to us</a></div></div><img class="ab-cta-art" src="/assets/r-full.webp" alt="" width="600" height="600" loading="lazy" aria-hidden="true"></div></div></section>'''
    vals = [("Value learning &amp; alignment", "We value learning, and we keep what we teach aligned with what industry needs."), ("Accountability", "Every module, hour and exam is published, and we stand by it."), ("Beyond narrow intelligence", "We teach students to think across fields, not only to use one tool."), ("Human sensitivity &amp; safety", "We teach AI that is safe, fair and respectful of people."), ("Stakeholder value", "We create lasting value for our investors, learners and employees.")]
    vl = "".join(f'<li style="--k:{i}"><b>{a}</b> {b}</li>' for i, (a, b) in enumerate(vals))
    mvv = f'''<section class="ab-sec ab-sec--tint" data-pd><div class="wrap"><div class="pd-head"><div>{eb("Mission, vision and values")}<h2>What we stand for.</h2></div><p class="pd-p">The purpose behind every program we teach.</p></div>
<div class="ab-mvv"><div class="ab-st-card" style="--k:0"><h3>Our mission</h3><p>To skill as many willing people as possible in one or more of the five streams of Super Intelligence, so their skills meet the needs of any industry that uses it, and so they can gain employment or start their own venture.</p></div>
<div class="ab-st-card" style="--k:1"><h3>Our vision</h3><p>To be the institution of choice for learners who want to upgrade their skills in Super Intelligence and add value to their lives, their stakeholders and India.</p><p style="margin-top:10px">A place where all seekers of Super Intelligence choose to learn, all employees wish to work, and all stakeholders wish to own.</p></div></div>
<h3 class="ab-vals-h">Our values</h3><ul class="ab-guides ab-vals">{vl}</ul></div></section>'''
    guides_box = f'''<section class="ab-sec" data-pd><div class="wrap"><div class="pd-head"><div>{eb("About our guides")}<h2>How our guides<br>are written.</h2></div><p class="pd-p">Our <a href="/guides">guides</a> are written by the Neuronetworks AI Ed team for students and parents.</p></div>
<ul class="ab-guides"><li><b>Program facts come from our curriculum.</b> Hours, modules, projects and certificates are taken from the published program roadmaps, never estimated.</li>
<li><b>Outside facts are sourced.</b> Every guide lists the official pages we checked, such as certification bodies, the National Testing Agency and Nasscom, with the date we checked them.</li>
<li><b>We review before publishing.</b> Each guide is checked against the program data and our rules: no invented numbers, no fees, and no promise of jobs, salaries or exam passes.</li>
<li><b>We update them.</b> Each guide shows the date it was last updated. If a fact changes, we correct the page.</li></ul></div></section>'''
    return layout("/about", "About Neuronetworks AI Ed: online AI courses for students", hero + manifesto + story + mvv + principles + env + bigger + guides_box + cta, "about")


def link_projects(html):
    for href, name in [("/projects/image-classification", "Image classification application"), ("/projects/document-rag-assistant", "Document RAG assistant"), ("/projects/agentflow-ai", "Tool-using AI agent")]:
        html = re.sub(r'(<a class="(?:pj|fcard)[^"]*"[^>]*?)href="[^"]*"([^>]*>(?:(?!</a>).)*?<h3>' + re.escape(name) + '</h3>)', lambda m: m.group(1) + 'href="' + href + '"' + m.group(2), html, flags=re.S)
    return html

def write(route, content):
    p = os.path.join(OUT, ("index" if route == "/" else route.lstrip("/")) + ".html")
    os.makedirs(os.path.dirname(p), exist_ok=True); open(p, "w").write(content)

def main():
    if os.path.exists(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT + "/assets")
    for f in os.listdir(HERE + "/assets"):
        shutil.copy(os.path.join(HERE, "assets", f), OUT + "/assets/" + f)
    shutil.move(OUT + "/assets/favicon.svg", OUT + "/favicon.svg")
    shutil.copy(HERE + "/site.css", OUT + "/assets/site.css"); shutil.copy(HERE + "/site.js", OUT + "/assets/site.js")
    os.remove(OUT + "/assets/module-stack.source.js")
    write("/", home()); write("/programs", programs_page())
    for p in PROGRAMS: write("/programs/" + p[0], program_detail(p[0]))
    write("/curriculum", curriculum_page()); write("/learning-experience", learning_page()); write("/projects", link_projects(projects_page()));
    for r, fn in PROJECT_PAGES.items(): write(r, fn())
    for r, fn in GUIDE_PAGES.items(): write(r, fn())
    write("/about", about_page())
    write("/admissions", admissions_page()); write("/faqs", faq_page()); write("/contact", contact_page()); write("/privacy", privacy_page()); write("/terms", terms_page())
    open(OUT + "/robots.txt", "w").write("User-agent: *\nAllow: /\n\n# AI search and answer engines\nUser-agent: OAI-SearchBot\nAllow: /\n\nUser-agent: ChatGPT-User\nAllow: /\n\nUser-agent: PerplexityBot\nAllow: /\n\nUser-agent: Claude-SearchBot\nAllow: /\n\nUser-agent: Claude-User\nAllow: /\n\n# AI training crawlers: allowed by the owner (decision 14 Oct 2026)\nUser-agent: GPTBot\nAllow: /\n\nUser-agent: ClaudeBot\nAllow: /\n\nUser-agent: anthropic-ai\nAllow: /\n\nUser-agent: Google-Extended\nAllow: /\n\nUser-agent: Applebot-Extended\nAllow: /\n\nUser-agent: CCBot\nAllow: /\n\nUser-agent: Meta-ExternalAgent\nAllow: /\n\nUser-agent: cohere-ai\nAllow: /\n\nUser-agent: Amazonbot\nAllow: /\n\nUser-agent: DuckAssistBot\nAllow: /\n\nUser-agent: Bytespider\nAllow: /\n\nSitemap: https://neuronetwrks.com/sitemap.xml\n")
    import datetime as _dt
    today = _dt.date.today().isoformat()
    urls = sorted("/" + os.path.relpath(f, OUT)[:-5].replace("index", "") for f in glob.glob(OUT + "/**/*.html", recursive=True) if not f.endswith("404.html"))
    pri = lambda u: "1.0" if u == "/" else "0.9" if u.startswith("/programs") else "0.8" if u.startswith("/guides") else "0.7"
    # Real last-changed dates: a guide's own date; otherwise the date the page's HTML last changed, tracked by a content
    # hash in sitemap_dates.json (asset version strings ignored, so a CSS change does not touch every page).
    import hashlib, subprocess
    dates_f = os.path.join(HERE, "sitemap_dates.json")
    store = json.load(open(dates_f)) if os.path.exists(dates_f) else {}
    gdate = {f"/guides/{g['slug']}": g.get("date", GUIDE_DATE) for g in GUIDES}
    gdate.update({f"/guides/{c['slug']}": CAREER_DATE for c in CAREERS}); gdate.update({f"/guides/{p['slug']}": p.get("modified", p["date"]) for p in SEO_BY.values()})
    def lastmod(u):
        key = u if u == "/" else u.rstrip("/")
        f = OUT + ("/index" if key == "/" else key) + ".html"
        h = hashlib.sha1(re.sub(r'data-v="[^"]*"|\?v=[0-9a-f]+', "", open(f).read()).encode()).hexdigest()[:16]
        old = store.get(key)
        if old and old[0] == h: d = old[1]
        elif old: d = today
        else:
            rel = os.path.relpath(f, os.path.join(HERE, "..", ".."))
            d = subprocess.run(["git", "log", "-1", "--format=%cs", "--", rel], cwd=os.path.join(HERE, "..", ".."), capture_output=True, text=True).stdout.strip() or today
        store[key] = [h, d]
        return gdate.get(key, d)
    rows = "".join(f"  <url><loc>{SITE}{u if u == '/' else u.rstrip('/')}</loc><lastmod>{lastmod(u)}</lastmod><priority>{pri(u)}</priority></url>\n" for u in urls)
    json.dump(dict(sorted(store.items())), open(dates_f, "w"), indent=0)
    open(OUT + "/sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + rows + "</urlset>\n")
    lines = ["# Neuronetworks AI Ed", "", "> Practical AI and technology education in India. Six-month AI Foundation course (104 hours, open from Class 9) and five three-year specialisations for students from Class 11 onwards (624 hours each). Every three-year month ends with a project and a one-hour exam. Fees are shared on enquiry.", "", "Contact: Hussain@neuronetwrks.com", "", "## Programs"]
    for p in PROGRAMS: lines.append(f"- [{p[2]}]({SITE}/programs/{p[0]}): {p[4]}, {p[3]} hours. {D[p[0]]['summary']}")
    lines += ["", "## Key pages", f"- [Curriculum]({SITE}/curriculum): every module and project, month by month.", f"- [Learning experience]({SITE}/learning-experience): how lessons, labs, projects and exams work.", f"- [Admissions]({SITE}/admissions): eligibility, how to apply, parents and guardians.", f"- [FAQs]({SITE}/faqs): straight answers on eligibility, hours, certification and privacy.", f"- [Projects]({SITE}/projects): projects from the program roadmaps.", f"- [About]({SITE}/about)", f"- [Contact]({SITE}/contact)", "", "## Notes", "- No program guarantees a job, internship or salary.", "- Certifications are awarded by the certifying organisations, not by Neuronetworks AI Ed."]
    lines += ["", "## Career roadmaps (how to become [role] after 10th)"] + [f"- [{c['title']}]({SITE}/guides/{c['slug']}): {c['desc']}" for c in CAREERS]
    for _pat in SEO_PATTERNS.values():
        lines += ["", f"## {_pat['name']}"] + [f"- [{p['title']}]({SITE}/guides/{p['slug']}): {p['desc']}" for p in _pat["pages"]]
    lines += ["", "## Guides"] + [f"- [{g['title']}]({SITE}/guides/{g['slug']}): {g['desc']}" for g in GUIDES]
    open(OUT + "/llms.txt", "w").write("\n".join(lines) + "\n")
    full = ["# Neuronetworks AI Ed: full program reference", "", "> " + ORG["description"] + " Tagline: Learn · Develop · Create. Website: " + SITE + ". Contact: Hussain@neuronetwrks.com. Fees are shared on enquiry.", ""]
    for p in PROGRAMS:
        d = D[p[0]]
        full += [f"## {p[2]} ({p[4]}, {p[3]} hours, {d['hoursPerWeek']} hours a week)", f"URL: {SITE}/programs/{p[0]}", "", d["answer"], "", f"Entry: {d['entry']}.", f"Assessment: {d['assessment']}", ""]
        for y in d["years"]: full.append(f"- {y['title']} ({y['hours']} hours): " + "; ".join(f"{m} ({d['moduleHours'][i]} h)" if d.get("moduleHours") else m for i, m in enumerate(y["modules"])))
        full += ["", "Projects: " + "; ".join(d["projects"]), "", "Tools: " + ", ".join(d["tools"]), "", "Certification preparation (awarded by the certifying organisations; passing not guaranteed): " + "; ".join(d["certifications"])]
        if d["careerRoles"]: full += ["", "Roles the curriculum is designed around (directions, not guarantees): " + "; ".join(d["careerRoles"])]
        if p[0] in SALARY: full += ["", "Indicative India salary (not guaranteed): " + "; ".join(f"{b} {v}" for b, v in zip(SAL_BANDS, SALARY[p[0]][0])) + ". " + SAL_NOTE]
        full += ["", "Completion: students receive a Neuronetworks AI Ed certificate on completing the program. Laptop specifications are recommendations."]
        full += ["", "FAQs:"] + [f"- Q: {f['q']} A: {conf(f['a'])}" for f in d["faqs"] if "{{CONFIRM" not in f["a"]] + [""]
    full += ["## Notes", "- No program guarantees a job, internship, salary or exam pass. Salary figures are indicative market ranges only.", "- Certifications are awarded by the certifying organisations, not by Neuronetworks AI Ed."]
    open(OUT + "/llms-full.txt", "w").write("\n".join(full) + "\n")
    # RSS 2.0 feed of every guide (course guides, career roadmaps and other SEO pages), newest first
    from email.utils import format_datetime as _fd
    import datetime as _d2
    _items = [(g["title"], g["slug"], g["desc"], g.get("date", GUIDE_DATE)) for g in GUIDES] + [(c["title"], c["slug"], c["desc"], CAREER_DATE) for c in CAREERS] + [(p["title"], p["slug"], p["desc"], p.get("modified", p["date"])) for p in SEO_BY.values()]
    _items.sort(key=lambda x: x[3], reverse=True)
    _rss = "".join(f"<item><title>{E(t)}</title><link>{SITE}/guides/{sl}</link><guid isPermaLink=\"true\">{SITE}/guides/{sl}</guid><description>{E(ds)}</description><pubDate>{_fd(_d2.datetime.fromisoformat(dt + 'T09:00:00+05:30'))}</pubDate></item>" for t, sl, ds, dt in _items)
    open(OUT + "/guides/feed.xml", "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>Neuronetworks AI Ed guides</title><link>{SITE}/guides</link><atom:link href="{SITE}/guides/feed.xml" rel="self" type="application/rss+xml"/><description>Guides for students and parents on AI and technology courses and careers after Class 10.</description><language>en-in</language><lastBuildDate>{_fd(_d2.datetime.now(_d2.timezone.utc))}</lastBuildDate>{_rss}</channel></rss>\n')
    from PIL import Image as _I
    _I.open(os.path.join(HERE, "assets", "favicon-src.png")).convert("RGBA").save(OUT + "/favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    open(OUT + f"/{INDEXNOW_KEY}.txt", "w").write(INDEXNOW_KEY)
    open(OUT + "/vercel.json", "w").write(json.dumps({"cleanUrls": True, "trailingSlash": False, "redirects": [{"source": "/faculty-and-team", "destination": "/about", "permanent": True}] + [{"source": "/guides/" + o, "destination": "/guides/" + n, "permanent": True} for o, n in json.load(open(os.path.join(HERE, "redirects_merged.json"))).items()], "headers": [
        {"source": "/(.*)", "headers": [{"key": "X-Content-Type-Options", "value": "nosniff"}, {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"}, {"key": "X-Frame-Options", "value": "DENY"}, {"key": "Permissions-Policy", "value": "camera=(), microphone=(), geolocation=(), interest-cohort=()"}, {"key": "Content-Security-Policy-Report-Only", "value": "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; connect-src 'self' https://www.google-analytics.com https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com; img-src 'self' data: https://www.google-analytics.com https://www.googletagmanager.com; style-src 'self' 'unsafe-inline'; font-src 'self'; object-src 'none'; base-uri 'self'; form-action 'self' mailto:; frame-ancestors 'none'"}]},
        {"source": "/assets/(.*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600, must-revalidate"}]}, {"source": "/((?!assets/).*)", "headers": [{"key": "Cache-Control", "value": "public, max-age=0, must-revalidate"}]}]}, indent=1))
    open(OUT + "/404.html", "w").write('<!doctype html><html lang="en-IN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page not found | Neuronetworks AI Ed</title><meta name="robots" content="noindex"><body style="font-family:system-ui;padding:80px 24px;background:#F6F9FD;color:#0B1B33"><h1>Page not found</h1><p><a href="/" style="color:#006DEE">Go to the home page</a></p></body></html>')
    print("built", len(glob.glob(OUT + "/**/*.html", recursive=True)), "pages")

if __name__ == "__main__":
    main()
