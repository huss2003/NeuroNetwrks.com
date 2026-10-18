import json, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
full = open('/home/user/NeuroNetwrks.com/site-preview/llms-full.txt').read()
sec = {}
for blk in re.split(r'\n## ', full):
    m = re.search(r'URL: https://neuronetwrks.com/programs/([a-z-]+)', blk)
    if m: sec[m.group(1)] = blk
BAN = ['unlock', 'revolutionis', 'revolutioniz', 'cutting-edge', 'seamless', 'journey', 'delve', 'game-changer', 'unleash', 'empower', ' dive ']
REQ = "slug role keyword program alt_programs title desc h1 lead role_intro in_short start_answer start_bridge streams start_extra roadmap_answer year_focus skills_answer skills build_answer projects certs_answer notfor_answer notfor salary_answer faqs context_fact sources related_guides".split()
bad = 0
for f in sys.argv[1:]:
    p = f if os.path.isabs(f) else os.path.join(H, f)
    d = json.load(open(p)); errs = []
    for k in REQ:
        if k not in d: errs.append('missing ' + k)
    s = json.dumps(d, ensure_ascii=False)
    if '—' in s: errs.append('em dash present')
    for w in BAN:
        if w in s.lower(): errs.append('banned word: ' + w.strip())
    if len(d.get('title', '')) > 60: errs.append('title > 60')
    if len(d.get('desc', '')) > 155: errs.append('desc > 155')
    if len(d.get('faqs', [])) != 5: errs.append('need 5 faqs')
    fq = ' '.join(q for q, a in d.get('faqs', [])).lower()
    if 'how many years' not in fq: errs.append('faq missing "how many years"')
    if 'without maths' not in fq: errs.append('faq missing "without maths"')
    b = sec.get(d.get('program'), '')
    if not b: errs.append('unknown program')
    projs = re.search(r'Projects: (.*)', b).group(1) if b else ''
    for name, _ in d.get('projects', []):
        if name not in projs.split('; '): errs.append('project not in program list: ' + name)
    certs = re.search(r'Certification preparation[^:]*: (.*)', b).group(1) if b else ''
    for c in d.get('cert_notes', {}):
        if c not in certs: errs.append('cert not in program list: ' + c)
    if re.search(r'₹\s?\d[\d,]*\s*(?:fee|per course)', s, re.I) or re.search(r'\bfees? (?:is|are|of) ₹', s, re.I): errs.append('looks like a fee')
    if not (1 <= len(d.get('sources', [])) <= 4): errs.append('need 1-3 role sources')
    for i, a in enumerate(d.get('in_short', [])): pass
    print(os.path.basename(p), 'OK' if not errs else 'FAIL: ' + '; '.join(errs)); bad += bool(errs)
sys.exit(1 if bad else 0)
