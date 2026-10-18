# Project detail pages and the home "Featured projects" carousel.
# Executed inside build.py's namespace (uses E, layout, li, ARW).

PI = {
 "upload": '<path d="M12 16V4M7 9l5-5 5 5"/><path d="M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/>',
 "cloud": '<path d="M7 18a4.5 4.5 0 0 1-.6-8.96A6 6 0 0 1 18 9a4 4 0 0 1 0 9"/><path d="M12 12v8M9 15l3-3 3 3"/>',
 "image": '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="1.8"/><path d="M21 16l-5-5-9 9"/>',
 "cpu": '<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 2v3M15 2v3M9 19v3M15 19v3M2 9h3M2 15h3M19 9h3M19 15h3"/>',
 "chart": '<path d="M4 20V10M10 20V4M16 20v-8M22 20H2"/>',
 "info": '<circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/>',
 "data": '<ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/>',
 "box": '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M3 7l9 5 9-5M12 12v10"/>',
 "monitor": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 12h6M10 16h6"/>',
 "split": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M9 12h8M9 15h8M9 18h5"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5L18 18M6 18l2.5-2.5M15.5 8.5L18 6"/>',
 "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
 "grid": '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>',
 "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4"/><circle cx="12" cy="12" r=".8"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
 "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
 "code": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M9 10l-2 2 2 2M15 10l2 2-2 2"/>',
 "file": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/>',
 "shield": '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "lock": '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
 "list": '<path d="M9 6h11M9 12h11M9 18h11M4 6h.01M4 12h.01M4 18h.01"/>',
 "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/>',
 "flow": '<rect x="3" y="3" width="7" height="5" rx="1"/><rect x="14" y="16" width="7" height="5" rx="1"/><path d="M6.5 8v5a2 2 0 0 0 2 2H14"/>',
 "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
 "history": '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5M12 7v5l3 2"/>',
 "plus": '<path d="M12 5v14M5 12h14"/>',
 "settings": '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M5 19l2-2M17 7l2-2"/>',
 "external": '<path d="M14 4h6v6M20 4l-9 9"/><path d="M19 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1h5"/>',
 "folder": '<path d="M3 6a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
 "eye": '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
 "map": '<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
 "bolt": '<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
}
def pi(k, s=20, sw=1.8): return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PI[k]}</svg>'
TICK = '<span class="tk" aria-hidden="true"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>'
LOGO = '<img class="mk-logo" src="/assets/mark-dark.svg" alt="" width="20" height="16" loading="lazy">'
AFLOGO = '<img class="mk-logo mk-logo--af" src="/assets/agentflow.svg" alt="AgentFlow AI logo" loading="lazy" width="20" height="20">'

def eb(t): return f'<p class="pd-eb">{t}</p>'
def chips(xs): return '<ul class="pd-chips">' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
def win(title, body, right='<span class="mk-demo">Illustrative demo output <i></i></span>', cls="", logo=None):
    return f'<div class="mk {cls}"><div class="mk-bar">{logo or LOGO}<b>{title}</b>{right}</div>{body}</div>'

PRED = [("Golden Retriever", 92.4), ("Labrador Retriever", 4.2), ("German Shepherd", 1.8), ("Other", 1.6)]
def bars(num=False):
    return f'<ul class="mk-bars{" mk-bars--num" if num else ""}">' + "".join(f'<li style="--w:{max(v, 1.5)}%;--k:{i}">' + (f'<span class="nb">{i+1}</span>' if num else "") + f'<span>{n}</span><i><b></b></i><em>{v}%</em></li>' for i, (n, v) in enumerate(PRED)) + "</ul>"
MODEL = '<dl class="mk-dl"><div><dt>Model</dt><dd>ResNet18 (pre-trained)</dd></div><div><dt>Input size</dt><dd>224 × 224</dd></div><div><dt>Classes</dt><dd>1000 (ImageNet)</dd></div></dl>'

def ic_mock_hero():
    body = f'''<div class="mk-ic"><div class="mk-col"><p class="mk-h">Upload an image</p><img class="mk-photo" loading="lazy" src="/assets/dog.webp" alt="Photo of a golden retriever used as the input image in the image classification demo" width="291" height="324"><span class="mk-btn-o">Choose an image</span><small class="mk-sm">or drag and drop JPG, PNG</small></div>
<div class="mk-col"><p class="mk-h">Prediction results</p>{bars()}<p class="mk-h" style="margin-top:14px">Model information</p>{MODEL}</div></div>'''
    return win("Image Classification", body)

def rag_side(active=0):
    rec = ["Eligibility criteria", "Program structure", "Career directions", "Application process"]
    return f'''<div class="mk-side"><span class="mk-new">{pi("plus",14,2.4)} New chat</span><ul class="mk-nav"><li>{pi("doc",15)} Documents</li><li>{pi("globe",15)} Knowledge base</li><li>{pi("history",15)} Chat history</li></ul>
<p class="mk-cap">Recent</p><ul class="mk-nav mk-nav--sm">''' + "".join(f'<li>{pi("chat",13)} {r}</li>' for r in rec) + "</ul></div>"

def rag_sources(items):
    return '<div class="mk-src"><p class="mk-cap">Sources</p><ol>' + "".join(f'<li style="--k:{i}"><span class="n">{i+1}</span><div><b>{a}</b><small>{b}</small></div>{pi("external",14)}</li>' for i, (a, b) in enumerate(items)) + "</ol></div>"

AIML = D["ai-ml-engineering"]
def aiml_modules(n=6):
    ms = [m for y in AIML["years"] for m in y["modules"]]
    pick = [ms[1], ms[6], ms[9], ms[14], ms[24], ms[22]]
    return pick[:n]

def rag_mock_hero():
    body = f'''<div class="mk-rag">{rag_side()}<div class="mk-main"><div class="mk-file">{pi("doc",18)}<div><b>Admissions_Guide.pdf</b><small>PDF · 24 pages</small></div></div>
<p class="mk-q">What are the eligibility criteria for the AI/ML Engineering program?</p>
<div class="mk-a"><span class="mk-bot">{pi("spark",16)}</span><p class="mk-type">Based on the provided document, the AI/ML Engineering program is open to students who have passed Class 10, with basic school-level mathematics and computer familiarity. <span class="mk-cite">[1] [2] [3]</span></p></div>
{rag_sources([("Admissions_Guide.pdf", "Page 4 · Eligibility criteria"), ("Program_Structure.pdf", "Page 2 · Overview"), ("FAQs.pdf", "Page 1 · General requirements")])}
<div class="mk-input">Ask a question about your documents… <span>{pi("upload",14,2.2)}</span></div></div></div>'''
    return win("Document RAG Assistant", body, '<span class="mk-demo">Illustrative demo data <i></i></span>')

AG_STEPS = [("Planning task", "Breaking down the request into steps"), ("Searching the web", "Using web_search tool"), ("Analysing results", "Reading and summarising key points"), ("Creating file", "Saving output to rag_summary.md")]
def agent_mock_hero():
    st = "".join(f'<li style="--k:{i}"><span class="ic">{pi(["list","search","chart","file"][i],15)}</span><div><b>{a}</b><small>{b}</small></div>{TICK}</li>' for i, (a, b) in enumerate(AG_STEPS))
    tools = "".join(f'<li style="--k:{i}">{pi(ic,15)}<div><b>{a}</b><small>{b}</small><em>● Completed</em></div></li>' for i, (ic, a, b) in enumerate([("globe", "web_search", "Query: latest RAG research"), ("code", "python", "Analyse and summarise"), ("file", "file_write", "Save to rag_summary.md")]))
    body = f'''<div class="mk-ag"><div class="mk-side mk-side--ag"><span class="mk-new">{pi("plus",14,2.4)} New task</span><ul class="mk-nav"><li>{pi("history",15)} History</li><li>{pi("settings",15)} Tools</li><li>{pi("settings",15)} Settings</li></ul></div>
<div class="mk-main"><p class="mk-q mk-q--l">Find the latest research on RAG, create a short summary and save it to a markdown file.</p><ol class="mk-steps">{st}</ol>
<div class="mk-done">{TICK}<div><b>Task completed</b><small>Summary of the latest RAG research saved to rag_summary.md.</small></div><span class="mk-btn-o mk-btn-o--sm">Open file</span></div></div>
<div class="mk-tools"><p class="mk-cap">Tool calls</p><ul>{tools}</ul></div></div>'''
    return win("AgentFlow AI", body, '<span class="mk-run">▸ Run</span>', logo=AFLOGO)

def pd_hero(crumb, tag, lines, desc, chip_list, art, note="", extra=""):
    h = "".join(f'<span class="ln"><span>{l}</span></span>' for l in lines)
    return f'''<section class="pd-hero" data-pd><div class="wrap pd-hero-grid"><div class="pd-hero-copy"><p class="pd-crumbs"><a href="/">Home</a> / <a href="/projects">Projects</a> / <span>{crumb}</span></p>
<p class="pd-tag">{tag}</p><h1 class="pd-h1">{h}</h1><p class="pd-lead">{desc}</p>{chips(chip_list)}
<div class="pd-actions"><a class="le-btn le-btn--p" href="#overview">Explore project {ARW}</a><a class="le-btn le-btn--s" href="/curriculum#aiml-y{2 if "2" in tag else 3}">View learning path</a></div>{f'<p class="pd-note">{note}</p>' if note else ''}</div>
<div class="pd-hero-art">{art}</div></div></section>'''

def pd_sec(eyebrow, h2, lead, body, cls="", layout="split", sid=""):
    head = f'<div>{eb(eyebrow)}<h2>{h2}</h2>{f"<p class=\"pd-p\">{lead}</p>" if lead and layout == "split" else ""}</div>'
    if layout == "split":
        return f'<section class="pd-sec {cls}" data-pd{f" id={chr(34)}{sid}{chr(34)}" if sid else ""}><div class="wrap pd-split">{head}<div>{body}</div></div></section>'
    return f'<section class="pd-sec {cls}" data-pd{f" id={chr(34)}{sid}{chr(34)}" if sid else ""}><div class="wrap"><div class="pd-head">{head}{f"<p class=\"pd-p\">{lead}</p>" if lead else ""}</div>{body}</div></section>'

def pd_cta():
    return f'''<section class="pd-sec" style="padding-top:0" data-pd><div class="wrap"><div class="pd-cta">{eb("Your next step")}<h2>Ready to explore more projects?</h2><p>Discover more hands-on projects from the AI/ML Engineering program and build a portfolio you can show.</p>
<div class="pd-actions"><a class="le-btn le-btn--w" href="/projects">View all projects {ARW}</a><a class="le-btn le-btn--g" href="/programs/ai-ml-engineering">Explore AI/ML Engineering</a></div><img class="pd-cta-art" src="/assets/i-banner.webp" alt="" width="609" height="419" loading="lazy"></div></div></section>'''

def tool_cards(items, cls="pd-tools"):
    return f'<ul class="{cls}">' + "".join(f'<li style="--k:{i}"><span class="ic">{pi(ic,22)}</span><b>{a}</b><small>{b}</small></li>' for i, (ic, a, b) in enumerate(items)) + "</ul>"

def skills(items, cols=1):
    return f'<ul class="pd-skills pd-skills--{cols}">' + "".join(f'<li style="--k:{i}">{TICK}<div><b>{a}</b>{f"<small>{b}</small>" if b else ""}</div></li>' for i, (a, b) in enumerate(items)) + "</ul>"

def program_link(year_label, desc):
    return f'''<a class="pd-prog" href="/programs/ai-ml-engineering"><img src="/assets/r-full.webp" alt="3D spiral staircase, the NeuroNetworks symbol for learning step by step" width="600" height="600" loading="lazy"><div><b>AI/ML Engineering</b><span class="pd-tag pd-tag--sm">{year_label}</span><p>{desc}</p></div><span class="pd-prog-go">{ARW}</span></a>'''

# ------------------------------------------------------------ page 1: image classification
def page_image_classification():
    art = f'<img class="pd-glass pd-glass--plates" src="/assets/g-plates.webp" alt="" width="900" height="533"><div class="pd-stage">{ic_mock_hero()}<div class="pd-badge b1"><span class="bi">{pi("check",16,2.2)}</span><div><b>Golden Retriever · 92.4%</b><small>Top prediction</small></div></div><div class="pd-badge b2"><span class="bi">{pi("cpu",16,2.2)}</span><div><b>ResNet18</b><small>224 × 224 input</small></div></div></div>'
    hero = pd_hero("Image classification", "Year 2 · AI/ML Engineering", ["Image", "classification", "application"], "Build a computer vision application that classifies images using deep learning. Train a model on a dataset, evaluate its performance and create a simple web interface to try it yourself.", ["Python", "PyTorch", "Computer Vision", "Deep Learning"], art)
    side = f'<ul class="mk-nav mk-nav--side"><li class="on">{pi("target",14)} Predict</li><li>{pi("info",14)} Model info</li><li>{pi("history",14)} History</li></ul>'
    ov_mock = win("Neuronetwrks", f'''<div class="mk-ov"><div class="mk-side mk-side--narrow"><p class="mk-cap">Image Classification</p>{side}</div><div class="mk-col"><p class="mk-h">Upload an image</p><div class="mk-drop">{pi("cloud",22)}<small>Drag and drop an image here<br>or click to browse</small></div></div>
<div class="mk-col"><img class="mk-photo mk-photo--sq" loading="lazy" src="/assets/dog.webp" alt="Photo of a golden retriever used as the input image in the image classification demo" width="291" height="324"></div><div class="mk-col"><p class="mk-h">Top predictions</p>{bars(True)}<span class="mk-btn">Run prediction</span></div></div>''', cls="mk--wide")
    feats = tool_cards([("image", "Upload an image", "Drag and drop an image or choose a file from your device."), ("cpu", "Run a trained model", "Load a pre-trained model and run inference on your image."), ("chart", "View predictions", "See the top predicted classes with confidence scores."), ("info", "Explore model details", "Check model information, input size and the set of classes.")], "pd-feats")
    overview = f'''<section class="pd-sec" id="overview" data-pd><div class="wrap"><div class="pd-split pd-split--wide"><div>{eb("Project overview")}<h2>What you build</h2><p class="pd-p">A complete image classification application that takes an image as input, runs it through a trained deep learning model and shows the top predictions with confidence scores in a clean web interface.</p><span class="pd-rule"></span></div><div>{ov_mock}</div></div>{feats}</div></section>'''
    steps = [("data", "Prepare dataset", "Use a labelled dataset such as ImageNet, or a smaller dataset provided in the program."), ("box", "Train or load model", "Train a model or use a pre-trained model with transfer learning."), ("chart", "Evaluate predictions", "Test the model on unseen images and review the results."), ("monitor", "Deploy interface", "Build a simple web app with Streamlit to try it yourself.")]
    wave = '<svg class="pd-wave" viewBox="0 0 800 120" preserveAspectRatio="none" aria-hidden="true"><path d="M40 40 C150 40 170 95 280 95 S420 40 520 40 S650 15 760 30" fill="none" stroke="#2F80F5" stroke-width="2" pathLength="1"/></svg>'
    st = "".join(f'<li class="pd-wstep" style="--k:{i}"><span class="n">{i+1:02d}</span><span class="ic">{pi(ic,22)}</span><b>{a}</b><small>{b}</small></li>' for i, (ic, a, b) in enumerate(steps))
    how = f'''<section class="pd-sec pd-sec--tint" data-pd><div class="wrap pd-split pd-split--wide"><div>{eb("From data to deployment")}<h2>How it works</h2><p class="pd-p">Follow a clear, end-to-end process to build the image classification application, from preparing data to deploying a simple web interface.</p><span class="pd-rule"></span></div><div class="pd-wavebox">{wave}<ol class="pd-wsteps">{st}</ol></div></div></section>'''
    tabs = "".join(f'<li{" class=\"on\"" if i == 0 else ""}>{pi(ic,15)} {t}</li>' for i, (ic, t) in enumerate([("upload", "Upload & predict"), ("chart", "Top predictions"), ("info", "Model information"), ("image", "Example images")]))
    in_mock = win("Image Classification", f'''<div class="mk-in"><div class="mk-col"><p class="mk-h">Input image</p><img class="mk-photo" loading="lazy" src="/assets/dog.webp" alt="Photo of a golden retriever used as the input image in the image classification demo" width="291" height="324"><div class="mk-row"><span class="mk-btn-o mk-btn-o--sm">{pi("image",13)} Change image</span><small class="mk-sm">golden_retriever.jpg<br>224 × 224</small></div></div>
<div class="mk-col"><p class="mk-h">Prediction results</p>{bars(True)}</div></div><div class="mk-foot">{pi("cpu",18)}<div><small>Model</small><b>ResNet18 (pre-trained)</b></div><div><small>Input size</small><b>224 × 224</b></div><div><small>Number of classes</small><b>1000 (ImageNet)</b></div></div>''')
    inside = f'''<section class="pd-sec pd-sec--dark" data-pd><div class="wrap pd-inside"><div>{eb("A closer look")}<h2>Inside the application</h2><p class="pd-p">A clean and intuitive interface to upload images, view predictions and explore how the model performs.</p><span class="pd-rule"></span></div><ul class="pd-vtabs">{tabs}</ul><div>{in_mock}</div></div></section>'''
    tech = pd_sec("Tech stack", "Tools &amp; technologies", "Use industry-standard tools and libraries for computer vision and deep learning.", tool_cards([("code", "Python", "Core programming language"), ("bolt", "PyTorch", "Deep learning framework"), ("eye", "torchvision", "Vision models and datasets"), ("monitor", "Streamlit", "Build the web interface")], "pd-tools pd-tools--row"), cls="pd-sec--tint pd-sec--tight")
    sk = pd_sec("Key learning outcomes", "Skills you practise", "Build practical skills that you can apply to real-world computer vision problems.", skills([("Data preparation", "Work with image datasets and understand data preprocessing steps."), ("Model training and inference", "Train a model or use a pre-trained model with transfer learning."), ("Model evaluation", "Measure performance and interpret prediction results."), ("Building a web interface", "Create a simple application using Streamlit.")]), cls="pd-sec--tight")
    road = pd_sec("Project roadmap", "Part of the AI/ML Engineering program", "This project is part of the Year 2 curriculum in the AI/ML Engineering three-year program. It builds on core machine learning concepts and helps you apply them in a practical application.", f'<a class="pd-mini" href="/programs/ai-ml-engineering"><span class="ic">{pi("cpu",22)}</span><div><b>AI/ML Engineering</b><small>Year 2 · Core project</small></div>{ARW}</a>', cls="pd-sec--tint pd-sec--tight")
    return layout("/projects/image-classification", "Image classification application", hero + overview + how + inside + tech + sk + road + pd_cta(), jsonld={"@type": "LearningResource", "name": "Image classification application", "description": "A computer vision project: prepare a dataset, train or load a model, evaluate predictions and build a simple web interface.", "url": SITE + "/projects/image-classification", "learningResourceType": "Project", "educationalLevel": "Year 2 · AI/ML Engineering", "inLanguage": "en-IN", "provider": {"@id": ORG_ID}, "isPartOf": {"@id": SITE + "/programs/ai-ml-engineering#course"}}, desc="An image classification project from the AI/ML Engineering program: data, model, evaluation and a simple web interface.")

# ------------------------------------------------------------ page 2: document RAG
def page_document_rag():
    art = f'<img class="pd-glass pd-glass--panels" src="/assets/g-panels.webp" alt="" width="900" height="590"><div class="pd-stage">{rag_mock_hero()}<div class="pd-badge b1"><span class="bi">{pi("link",16,2.2)}</span><div><b>3 sources cited</b><small>Every answer is grounded</small></div></div><div class="pd-badge b2"><span class="bi">{pi("search",16,2.2)}</span><div><b>Vector search</b><small>Top passages retrieved</small></div></div></div>'
    hero = pd_hero("Document RAG assistant", "Year 3 · AI/ML Engineering", ["Document RAG", "assistant"], "Build a document question-answering assistant using retrieval-augmented generation. Ingest your documents, retrieve relevant information and generate accurate answers with source citations.", ["Python", "RAG", "Vector Search", "LLMs"], art, "Illustrative demo data. Not real student work.")
    steps = [("upload", "Upload documents", "Add PDFs, docs or text files to your knowledge base."), ("split", "Split into chunks", "Break documents into smaller passages for better retrieval."), ("search", "Retrieve relevant passages", "Find the most relevant chunks using vector search."), ("spark", "Generate answer", "Use an LLM to generate a clear answer with source citations.")]
    st = "".join(f'<li class="pd-hstep" style="--k:{i}"><span class="n">{i+1:02d}</span><span class="ic">{pi(ic,24)}</span><div><b>{a}</b><small>{b}</small></div></li>' for i, (ic, a, b) in enumerate(steps))
    how = pd_sec("How it works", "From documents<br>to grounded answers.", "The assistant combines your documents with a language model to find relevant information and generate accurate, well-cited answers.", f'<ol class="pd-hsteps">{st}</ol>', layout="stack", sid="overview")
    mods = "".join(f"<li>{E(m)}</li>" for m in aiml_modules())
    walk_mock = f'''<div class="mk mk--split">{''.join([])}<div class="mk-bar">{LOGO}<b>Document RAG Assistant</b><span class="mk-demo mk-demo--r">Source preview <span class="x">×</span></span></div><div class="mk-rag mk-rag--wide">{rag_side()}<div class="mk-main"><p class="mk-q">What topics are covered in the AI/ML Engineering program?</p>
<div class="mk-a"><span class="mk-bot">{pi("spark",16)}</span><p class="mk-type">The AI/ML Engineering program covers Python, mathematics for machine learning, classical machine learning, deep learning, generative AI and MLOps. Later years move into real-world projects and specialised modules. <span class="mk-cite">[1] [2] [3]</span></p></div>
{rag_sources([("Program_Structure.pdf", "Page 3 · Core modules"), ("Curriculum_year1.pdf", "Page 1 · Year 1 overview"), ("Curriculum_year2.pdf", "Page 2 · Advanced topics")])}<div class="mk-input">Ask a question about your documents… <span>{pi("upload",14,2.2)}</span></div></div>
<div class="mk-prev"><div class="mk-file">{pi("doc",18)}<div><b>Program_Structure.pdf</b><small>Page 3 · Core modules</small></div></div><div class="mk-pager">‹ 3 / 24 ›</div><div class="mk-page"><b>Core modules</b><ul>{mods}</ul><i></i><i></i><i></i></div></div></div></div>'''
    walk = pd_sec("Project walkthrough", "Inside the assistant.", "Explore the interface, try example questions and see how the assistant finds relevant information and gives grounded answers with source citations.", walk_mock + '<p class="pd-cap">Illustrative demo data</p>', cls="pd-sec--dark", layout="stack")
    arch_items = [("doc", "Documents", "PDFs, docs, text files"), ("split", "Text extraction", "Extract and clean text content"), ("layers", "Chunking &amp; embeddings", "Split into passages and create embeddings"), ("data", "Vector index", "Store embeddings in a vector database"), ("search", "Retriever", "Find relevant passages"), ("spark", "LLM response", "Generate grounded answer"), ("link", "Source citations", "Link to original documents")]
    arch = '<ol class="pd-pipe">' + "".join(f'<li style="--k:{i}"><span class="ic">{pi(ic,22)}</span><b>{a}</b><small>{b}</small></li>' for i, (ic, a, b) in enumerate(arch_items)) + "</ol>"
    sysw = pd_sec("Technical architecture", "How the system works.", "A simple architecture that combines document processing, vector search and a large language model.", arch, layout="stack")
    tech = pd_sec("Tools and technologies", "Built with modern<br>AI tools.", "Use widely adopted tools and frameworks to build a document assistant.", tool_cards([("code", "Python", "Core development"), ("doc", "Document parsing", "PDF, DOCX, TXT"), ("link", "Embeddings", "Text representations"), ("data", "Vector search", "Similarity search"), ("cpu", "LLMs", "Answer generation"), ("grid", "API &amp; UI", "Build and deploy")], "pd-tools pd-tools--six"), cls="pd-sec--tint pd-sec--tight")
    sk = pd_sec("Skills you practise", "Gain practical skills.", "Build real experience working with document understanding, retrieval systems and large language models.", skills([("Document processing and text extraction", ""), ("Prompt and context assembly", ""), ("Designing effective retrieval pipelines", ""), ("Generating grounded responses with citations", ""), ("Working with embeddings and vector search", ""), ("Evaluation and testing", "")], 2), cls="pd-sec--tight")
    road = pd_sec("Part of a larger journey", "Part of the AI/ML<br>Engineering program.", "This project is part of Year 3, where you work on advanced AI systems, real-world applications and a portfolio of projects.", program_link("Year 3 · Specialisation", E(AIML["summary"])), cls="pd-sec--tint pd-sec--tight")
    return layout("/projects/document-rag-assistant", "Document RAG assistant", hero + how + walk + sysw + tech + sk + road + pd_cta(), jsonld={"@type": "LearningResource", "name": "Document RAG assistant", "description": "Build a document question-answering assistant using retrieval-augmented generation, with answers that cite their sources.", "url": SITE + "/projects/document-rag-assistant", "learningResourceType": "Project", "educationalLevel": "Year 3 · AI/ML Engineering", "inLanguage": "en-IN", "provider": {"@id": ORG_ID}, "isPartOf": {"@id": SITE + "/programs/ai-ml-engineering#course"}}, desc="A document question-answering project from the AI/ML Engineering program, using retrieval-augmented generation with source citations.")

# ------------------------------------------------------------ page 3: tool-using agent
def page_tool_agent():
    art = f'<img class="pd-glass pd-glass--stair" src="/assets/r-full.webp" alt="" width="600" height="600"><div class="pd-stage">{agent_mock_hero()}<div class="pd-badge b1"><span class="bi">{pi("check",16,2.2)}</span><div><b>4 / 4 steps done</b><small>Plan executed</small></div></div><div class="pd-badge b2"><span class="bi">{pi("settings",16,2.2)}</span><div><b>3 tools called</b><small>Search, code, files</small></div></div></div>'
    hero = pd_hero("AgentFlow AI", "Year 3 · AI/ML Engineering", ["AgentFlow", "AI"], "Build an AI agent that can plan complex tasks, break them down into steps and use tools such as web search, code execution and file operations to complete real-world tasks.", ["Python", "Agents", "Tool Calling", "APIs"], art, "Illustrative demo interface. Based on the roadmap project: Tool-using AI agent.")
    flow = f'''<div class="pd-flow"><div class="fl-box" style="--k:0"><span class="ic">{pi("user",20)}</span><b>User request</b><small>Find information, run analysis, create a file…</small></div><span class="fl-ar" style="--k:1"></span>
<div class="fl-box fl-agent" style="--k:2"><b>AI agent</b><ul><li>Understand</li><li>Plan steps</li><li>Choose tools</li><li>Execute</li><li>Verify results</li></ul></div><span class="fl-ar fl-ar--fork" style="--k:3"></span>
<div class="fl-tools" style="--k:4"><div class="fl-box fl-sm">{pi("search",16)}<div><b>Web search</b><small>Get latest information</small></div></div><div class="fl-box fl-sm">{pi("code",16)}<div><b>Code execution</b><small>Run Python code</small></div></div><div class="fl-box fl-sm">{pi("file",16)}<div><b>File operations</b><small>Read and write files</small></div></div></div><span class="fl-ar" style="--k:5"></span>
<div class="fl-box" style="--k:6"><span class="ic">{pi("user",20)}</span><b>Final response</b><small>Task completed with output you can verify.</small></div></div>'''
    ov = pd_sec("Project overview", "What you build.", "You will build an AI agent that can understand a user's request, plan the steps needed, choose the right tools and complete the task with verifiable results.", flow, sid="overview")
    steps = [("Interpret request", "Understand what you are asking for."), ("Plan", "Break the task into smaller steps."), ("Choose tool", "Select the most appropriate tool for each step."), ("Execute", "Run the tool and observe the results."), ("Verify result", "Check the output and handle errors if needed."), ("Respond", "Provide the final answer with references or files.")]
    st = "".join(f'<li style="--k:{i}"><span class="n">{i+1:02d}</span><b>{a}</b><small>{b}</small></li>' for i, (a, b) in enumerate(steps))
    how = pd_sec("Step by step", "How the agent<br>works.", "The agent follows a clear process from understanding your request to delivering a final result, using the right tools at each step.", f'<ol class="pd-nsteps">{st}</ol>', cls="pd-sec--tight")
    ex = [("user", "User request", "Find the latest research on RAG, create a short summary and save it to a markdown file.", False), ("list", "Plan", "6 steps", False), ("search", "web_search", "Search for recent RAG research", True), ("code", "python", "Analyse and summarise content", True), ("file", "file_write", "Save to rag_summary.md", True)]
    exl = "".join(f'<li style="--k:{i}"><span class="ic">{pi(ic,15)}</span><div><b>{a}</b><small>{b}</small></div>{TICK if t else ""}</li>' for i, (ic, a, b, t) in enumerate(ex))
    trace = '{\n  "step": "web_search",\n  "query": "latest RAG research",\n  "status": "completed",\n  "results": [\n    {\n      "title": "Retrieval-augmented…",\n      "url": "https://…"\n    }\n  ]\n}'
    wf_mock = f'''<div class="mk mk--wf"><div class="mk-bar">{AFLOGO}<b>AgentFlow AI</b><span class="mk-demo">Illustrative demo interface <i></i></span></div><div class="mk-wf">
<div class="mk-side mk-side--ag"><span class="mk-new">{pi("plus",14,2.4)} New task</span><ul class="mk-nav"><li>{pi("folder",15)} Projects</li><li>{pi("code",15)} Playground</li><li>{pi("settings",15)} Tools</li><li>{pi("list",15)} Logs</li></ul></div>
<div class="mk-main"><p class="mk-h">Execution flow</p><ol class="mk-exec">{exl}<li class="fin" style="--k:5">{TICK}<div><b>Final response</b><small>Task completed successfully</small></div></li></ol></div>
<div class="mk-trace"><div class="mk-tabs"><span class="on">Trace</span><span>Logs</span><span>Output</span></div><pre>{E(trace)}</pre><p class="mk-h">Result preview</p><div class="mk-file">{pi("doc",18)}<div><b>rag_summary.md</b><small>Markdown</small></div><span class="mk-btn-o mk-btn-o--sm">View file</span></div></div></div></div>'''
    pts = "".join(f'<li>{pi(ic,18)}<span>{t}</span></li>' for ic, t in [("list", "View the agent's plan and execution steps"), ("user", "Inspect tool calls and inputs"), ("monitor", "See intermediate results and final output"), ("code", "Try different requests and test edge cases")])
    walk = f'''<section class="pd-sec pd-sec--dark" data-pd><div class="wrap pd-split pd-split--wide"><div>{eb("Project walkthrough")}<h2>Inside the workflow.</h2><p class="pd-p">Work in a development environment where you can see the agent's reasoning steps, tool calls and results at each step.</p><ul class="pd-pts">{pts}</ul></div><div>{wf_mock}</div></div></section>'''
    arch = f'''<div class="pd-arch"><div class="fl-box fl-sm" style="--k:0">{pi("user",16)}<b>User request</b></div><span class="fl-ar" style="--k:1"></span><div class="fl-box fl-orch" style="--k:2">{pi("settings",18)}<div><b>Agent orchestrator</b><small>(LLM + tool registry)</small></div></div><span class="fl-ar" style="--k:3"></span><div class="fl-box fl-sm" style="--k:4"><span class="ok">{TICK}</span><div><b>Validated result</b><small>Safe and useful output</small></div></div>
<div class="pd-arch-tools" style="--k:5">''' + "".join(f'<div class="fl-box fl-sm">{pi(ic,16)}<div><b>{a}</b><small>{b}</small></div></div>' for ic, a, b in [("search", "Web search", "Search the internet"), ("code", "Code execution", "Run Python code"), ("folder", "File operations", "Read and write files"), ("file", "Other tools", "APIs and custom tools")]) + "</div></div>"
    archs = pd_sec("Architecture", "Tools and<br>architecture.", "Learn how an agent is built using a language model, a tool registry and a controlled execution environment.", arch, cls="pd-sec--tight")
    safe = pd_sec("Safety by design", "Safety and<br>control.", "Learn how to build agents that are useful, reliable and safe, with clear permissions and human oversight where needed.", tool_cards([("lock", "Permission control", "Limit what tools can do and which resources they can access."), ("shield", "Approval for sensitive actions", "Require confirmation before critical operations such as file changes."), ("list", "Execution logs", "Keep a record of tool calls, inputs and outputs for transparency."), ("check", "Result validation", "Check and verify outputs to reduce errors and hallucinations.")], "pd-feats pd-feats--sm"), cls="pd-sec--tint pd-sec--tight")
    tech = pd_sec("Tech stack", "Tools and<br>technologies.", "Work with modern tools and frameworks used to build AI agents.", tool_cards([("code", "Python", "Core language"), ("cpu", "LLM APIs", "Provider APIs"), ("link", "Function calling", "Tool integration"), ("search", "Web search", "Search APIs"), ("box", "Sandboxed execution", "Run code safely"), ("file", "File handling", "Read and write files")], "pd-tools pd-tools--six"), cls="pd-sec--tight")
    sk = pd_sec("Skills you practise", "Key skills<br>you will gain.", "This project helps you build practical skills in agent design, tool use and real-world problem solving.", skills([("Task decomposition", "Break complex requests into steps"), ("Result verification", "Check and validate outputs"), ("Tool calling and integration", "Use APIs and external tools"), ("Safe execution", "Apply permissions and controls"), ("Error handling", "Handle tool failures and edge cases"), ("Debugging and iteration", "Test, improve and refine the agent")], 2), cls="pd-sec--tint pd-sec--tight")
    ctx = f'''<div class="pd-ctx"><div><p class="pd-tag pd-tag--sm">AI/ML Engineering</p><h3>Year 3 · Specialisation</h3><p>{E(AIML["summary"])}</p><a class="le-link" href="/programs/ai-ml-engineering">View program {ARW}</a></div>{skills([("Advanced AI and LLMs", ""), ("RAG and agent development", ""), ("MLOps and deployment", ""), ("Portfolio of projects", "")])}</div>'''
    prog = pd_sec("Program context", "Part of the AI/ML<br>Engineering program.", "This project is part of Year 3, where you build advanced topics and work on real-world applications with a portfolio of projects.", ctx, cls="pd-sec--tight")
    return layout("/projects/agentflow-ai", "AgentFlow AI", hero + ov + how + walk + archs + safe + tech + sk + prog + pd_cta(), jsonld={"@type": "LearningResource", "name": "AgentFlow AI", "description": "Build an AI agent that plans tasks, calls tools such as web search, code execution and file operations, and verifies its results.", "url": SITE + "/projects/agentflow-ai", "learningResourceType": "Project", "educationalLevel": "Year 3 · AI/ML Engineering", "inLanguage": "en-IN", "provider": {"@id": ORG_ID}, "isPartOf": {"@id": SITE + "/programs/ai-ml-engineering#course"}}, desc="AgentFlow AI: a tool-using AI agent project from the AI/ML Engineering program: planning, tool calling, verification and safe execution.")

PROJECT_PAGES = {"/projects/image-classification": page_image_classification, "/projects/document-rag-assistant": page_document_rag, "/projects/agentflow-ai": page_tool_agent}

# ------------------------------------------------------------ home: featured projects carousel
FEATURED = [
 ("/projects/image-classification", "Year 2 · AI/ML", "Image classification application", "A deep learning model to classify images into different categories with a simple and intuitive web interface.", ["Python", "PyTorch", "Computer Vision", "Streamlit"], [("image", "Upload images", "Drag and drop or browse files"), ("spark", "AI prediction", "Get instant results"), ("chart", "Confidence scores", "See top predictions")], "ic"),
 ("/projects/document-rag-assistant", "Year 3 · AI/ML", "Document RAG assistant", "Ask questions about your documents and get grounded answers with source citations, using retrieval-augmented generation.", ["Python", "RAG", "Vector Search", "LLMs"], [("upload", "Upload documents", "PDFs, docs or text"), ("search", "Retrieve passages", "Vector search"), ("link", "Cited answers", "Linked to sources")], "rag"),
 ("/projects/agentflow-ai", "Year 3 · AI/ML", "AgentFlow AI", "An agent that plans tasks, calls tools such as web search, code execution and file operations, and verifies its results.", ["Python", "Agents", "Tool Calling", "APIs"], [("list", "Plans steps", "Breaks tasks down"), ("settings", "Calls tools", "Search, code, files"), ("check", "Verifies results", "Checks its output")], "ag"),
]
def ic_mock_fp():
    others = "".join(f'<li><span>{n}</span><em>{v}%</em></li>' for n, v in PRED[1:])
    body = f"""<div class="mk-fpic"><div class="mk-side"><p class="mk-cap">Image Classification</p><ul class="mk-nav"><li class="on">{pi("upload",13)} Upload</li><li>{pi("chart",13)} Results</li><li>{pi("history",13)} History</li><li>{pi("info",13)} Model Info</li></ul></div>
<div class="mk-col"><p class="mk-h">Upload Image</p><small class="mk-sub">Upload an image to classify it using a trained deep learning model.</small><div class="mk-drop">{pi("cloud",26)}<b>Drag and drop an image here</b><small>or click to browse</small><small>PNG, JPG, JPEG up to 10MB</small></div></div>
<div class="mk-col"><div class="mk-card"><p class="mk-h">Prediction Results</p><div class="mk-top"><img loading="lazy" src="/assets/dog.webp" alt="Photo of a golden retriever used as the input image in the image classification demo" width="291" height="324"><div><span class="tt"><b>Golden Retriever</b><em>92.4%</em></span><span class="mk-topbar"><i></i></span><ul>{others}</ul></div></div></div>
<div class="mk-card"><p class="mk-h">Top Predictions</p>{bars(True)}</div></div></div>"""
    nav = '<nav class="mk-appnav"><span>Projects</span><span>Models</span><span>Datasets</span><span>About</span></nav><span class="mk-run">Run</span>'
    return f'<div class="mk mk--app"><div class="mk-bar">{LOGO}<b>NeuroNetworks</b>{nav}</div>{body}</div>'

FEATURED = [
 ("/projects/image-classification", "Year 2 · AI/ML", "Image classification application", "A deep learning model to classify images into different categories with a simple and intuitive web interface.", ["Python", "PyTorch", "Computer Vision", "Streamlit"], [("image", "Upload images", "Drag and drop or browse files"), ("spark", "AI prediction", "Get instant results"), ("chart", "Confidence scores", "See top predictions")], "ic"),
 ("/projects/document-rag-assistant", "Year 3 · AI/ML", "Document RAG assistant", "Ask questions about your documents and get grounded answers with source citations, using retrieval-augmented generation.", ["Python", "RAG", "Vector Search", "LLMs"], [("upload", "Upload documents", "PDFs, docs or text"), ("search", "Retrieve passages", "Vector search"), ("link", "Cited answers", "Linked to sources")], "rag"),
 ("/projects/agentflow-ai", "Year 3 · AI/ML", "AgentFlow AI", "An AI agent that plans tasks, calls tools such as web search, code execution and file operations, and verifies its results.", ["Python", "Agents", "Tool Calling", "APIs"], [("list", "Plans steps", "Breaks tasks down"), ("settings", "Calls tools", "Search, code, files"), ("check", "Verifies results", "Checks its output")], "ag"),
]
def featured_projects():
    mocks = {"ic": ic_mock_fp, "rag": rag_mock_hero, "ag": agent_mock_hero}
    slides = ""; thumbs = ""
    for i, (href, tag, title, desc, ch, feats, mk) in enumerate(FEATURED):
        ft = "".join(f'<li><span class="fi">{pi(ic,20)}</span><b>{a}</b><small>{b}</small></li>' for ic, a, b in feats)
        slides += f"""<article class="fp-slide{" on" if i == 0 else ""}" id="fp-s{i}" aria-roledescription="slide" aria-label="{i+1} of 3"{"" if i == 0 else " hidden"}><div class="fp-copy"><p class="pd-tag">{tag}</p><h3>{title}</h3><p class="fp-desc">{desc}</p>{chips(ch)}<a class="le-btn le-btn--p" href="{href}">View project {ARW}</a><ul class="fp-feats">{ft}</ul></div>
<div class="fp-art" aria-hidden="true"><span class="fp-orb"></span><img class="fp-glass" src="/assets/g-plates.webp" alt="" width="900" height="533" loading="lazy"><div class="fp-mock">{mocks[mk]()}</div></div></article>"""
    for i in [1, 2, 0]:
        href, tag, title, mk = FEATURED[i][0], FEATURED[i][1], FEATURED[i][2], FEATURED[i][6]
        mark = '<img class="fp-th-mark" src="/assets/agentflow.svg" alt="AgentFlow AI logo" loading="lazy" width="28" height="28">' if mk == "ag" else ""
        thumbs += f'<li><button type="button" class="fp-th" data-slide="{i}" aria-controls="fp-s{i}"><span class="fp-th-img" aria-hidden="true"><span class="fp-mini">{mocks[mk]()}</span>{mark}</span><span class="fp-th-t"><span class="pd-tag pd-tag--sm">{tag}</span><b>{title}</b></span><span class="fp-th-go" aria-hidden="true">{ARW}</span></button></li>'
    dots = '<span class="fp-dots">' + "".join(f'<i{" class=\"on\"" if k == 0 else ""}><b></b></i>' for k in range(3)) + '</span>'
    return f"""<section class="fp" id="featured" data-pd aria-roledescription="carousel" aria-label="Featured projects"><div class="wrap"><div class="fp-head"><div>{eb("Featured projects")}<h2><span>Build real projects.</span><span class="b">Showcase your skills.</span></h2></div><p class="fp-lead">Work on practical projects from the program roadmap and build a portfolio you can show.</p>
<div class="fp-nav"><div class="fp-btns"><button type="button" class="fp-prev" aria-label="Previous project"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg></button><button type="button" class="fp-next" aria-label="Next project">{ARW}</button></div><div class="fp-prog">{dots}<span class="fp-count" aria-live="polite">01 / 03</span></div></div></div>
<div class="fp-stage"><div class="fp-main">{slides}</div><ul class="fp-list">{thumbs}</ul></div>
<div class="fp-foot"><a class="le-btn le-btn--p" href="/projects">View all projects {ARW}</a><p>Projects are based on the AI/ML Engineering roadmap.<br>Student work is not shown until the institute supplies and approves it.</p><span class="fp-dots fp-dots--b"><i class="on"></i><i></i><i></i></span></div></div></section>"""
