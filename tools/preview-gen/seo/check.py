# Generic checker for programmatic SEO pages in seo/<pattern>/<slug>.json. Usage: python3 seo/check.py [files...] (default: all)
import json, re, sys, os, glob
H = os.path.dirname(os.path.abspath(__file__))
full = open(os.path.join(H, '..', '..', '..', 'site-preview', 'llms-full.txt')).read()
sec = {}
for blk in re.split(r'\n## ', full):
    m = re.search(r'URL: https://neuronetwrks.com/programs/([a-z-]+)', blk)
    if m: sec[m.group(1)] = blk
BAN = ['unlock', 'revolutionis', 'revolutioniz', 'cutting-edge', 'seamless', 'journey', 'delve', 'game-changer', 'unleash', 'empower', ' dive ']
BLOCKS = {'p', 'note', 'callout', 'table', 'list', 'cards', 'program_roadmap', 'program_note', 'talk', 'program_certs', 'program_laptop', 'program_salary', 'parents', 'jee'}
REQ = "slug keyword title desc h1 lead in_short sections faqs sources date date_txt".split()
files = sys.argv[1:] or [f for f in glob.glob(os.path.join(H, '*', '*.json')) if not f.endswith('pattern.json')]
bad = 0
for f in files:
    d = json.load(open(f)); errs = []
    pat = json.load(open(os.path.join(os.path.dirname(os.path.abspath(f)), 'pattern.json'))) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(f)), 'pattern.json')) else {}
    for k in REQ:
        if k not in d: errs.append('missing ' + k)
    if os.path.basename(f) != d.get('slug', '') + '.json': errs.append('file name must be <slug>.json')
    s = json.dumps(d, ensure_ascii=False)
    if '—' in s: errs.append('em dash present')
    for w in BAN:
        if w in s.lower(): errs.append('banned word: ' + w.strip())
    if re.search(r'\b(fee|fees|price)\b[^.]{0,30}₹|₹[^.]{0,20}\b(fee|fees)\b', s, re.I): errs.append('looks like a fee/price')
    if len(d.get('title', '')) > 60: errs.append('title > 60 chars')
    if len(d.get('desc', '')) > 155: errs.append('desc > 155 chars')
    if len(d.get('in_short', [])) != 3: errs.append('in_short needs 3 bullets')
    for x in d.get('sections', []):
        if not x.get('h2', '').endswith('?'): errs.append('H2 not a question: ' + x.get('h2', ''))
        n = len(x.get('answer', '').split())
        if not 15 <= n <= 50: errs.append(f'answer {n} words (15-50): ' + x.get('h2', '')[:40])
        for b in x.get('blocks', []):
            if b.get('type') not in BLOCKS: errs.append('unknown block ' + str(b.get('type')))
            if b.get('type') == 'program_roadmap':
                projs = (re.search(r'Projects: (.*)', sec.get(d.get('program'), '')) or [None, ''])[1].split('; ')
                for p in b.get('highlight', []):
                    if p not in projs: errs.append('highlight not a real project: ' + p)
            if b.get('type', '').startswith('program') and d.get('program') not in sec: errs.append('program blocks need a valid program')
    if not any(b.get('type') == 'talk' for x in d.get('sections', []) for b in x.get('blocks', [])) and d.get('program'): errs.append('needs a talk box inside the content')
    if len(d.get('faqs', [])) != 5: errs.append('need exactly 5 FAQs')
    fq = ' '.join(q for q, a in d.get('faqs', [])).lower()
    for must in pat.get('required_faq', []):
        if must not in fq: errs.append(f'FAQ must include "{must}"')
    if not d.get('sources'): errs.append('need at least 1 fresh source')
    for t, u, n in d.get('sources', []):
        if not u.startswith('https://'): errs.append('source url must be https: ' + u)
        if not re.search(r'20\d\d', n): errs.append('source needs a date: ' + t)
    for p in [d.get('program')] + d.get('alt_programs', []):
        if p and p not in sec: errs.append('unknown program ' + p)
    print(os.path.basename(f), 'OK' if not errs else 'FAIL: ' + '; '.join(errs)); bad += bool(errs)
sys.exit(1 if bad else 0)
