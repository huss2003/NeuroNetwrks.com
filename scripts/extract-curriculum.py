"""Parse docs/extracted/*.md (pandoc output of the owner's curriculum .docx files) into
docs/extracted/curriculum.json. Facts only: nothing here is invented; missing fields stay empty.
Usage: python3 scripts/extract-curriculum.py"""
import json, re, glob, os

SRC = {
    'ai-ml-engineering': '3-Year_AI_ML_Engineering_Professional_Program_624_Hours1.md',
    'cybersecurity': '3-Year_Cybersecurity_Professional_Program_624_Hours1.md',
    'data-science-ai': '3-Year_Data_Science_and_AI_Professional_Program_624_Hours1.md',
    'product-ux-ai-design': '3-Year_Product_and_UX_AI_Design_Professional_Program_624_Hours1.md',
    'software-development': '3-Year_Software_Development_Professional_Program_624_Hours1.md',
}
# Tools are only listed when the word appears in the program's own document.
TOOL_CANDIDATES = ['Python','Java','JavaScript','TypeScript','React','Node.js','SQL','Git','GitHub','Docker','Kubernetes','Linux','Bash','PowerShell','Wireshark','Nmap','Burp Suite','Metasploit','Splunk','Microsoft Sentinel','KQL','NumPy','Pandas','Scikit-learn','PyTorch','TensorFlow','Hugging Face','LangChain','MLflow','FastAPI','Flask','Spring Boot','PostgreSQL','MongoDB','Tableau','Power BI','Excel','Figma','Jupyter','Spark','Airflow','dbt','AWS','Azure','Google Cloud','Terraform','Jenkins','Postman','Selenium','Maven','Kali Linux','Snort','Suricata','Ghidra','Zeek','Elastic','Streamlit','OpenCV','Tableau Public','Notion','Miro','Framer','Adobe XD','Webflow']

def clean(s): return re.sub(r'\s+', ' ', s.replace('\\|', '|').replace('**', '').replace('\\', '')).strip()

def table_rows(lines, start_pat):
    """Return rows (list of cell lists) of the first table after a heading matching start_pat."""
    i = next((k for k, l in enumerate(lines) if re.match(start_pat, l, re.I)), None)
    if i is None: return []
    rows = []
    for l in lines[i+1:]:
        if l.startswith('# '): break
        if l.startswith('|'):
            cells = [clean(c) for c in l.strip().strip('|').split('|')]
            if set(''.join(cells)) <= set('-: '): continue
            rows.append(cells)
        elif rows and not l.strip(): break
    return rows[1:] if rows else []

def months(lines):
    out, cur = [], None
    for l in lines:
        m = re.match(r'## (?:Month|M)\s*(\d+)\s*[—-]\s*(.+)', l)
        if m:
            cur = {'n': int(m.group(1)), 'title': clean(m.group(2)), 'fields': {}}; out.append(cur); continue
        if l.startswith('# ') and cur and not l.startswith('# 6') : pass
        if cur is None: continue
        if l.startswith('# '): cur = None; continue
        m = re.match(r'\**(Stage|Skills|Core topics|Hands-on labs|Portfolio project|Project|Assessment|Exam)[:\*]+\s*(.*)', l)
        if m: cur['fields'][m.group(1)] = clean(m.group(2)); continue
        if l.startswith('Stage:'): cur['fields']['Stage'] = clean(l)
    res = []
    for c in out:
        f = c['fields']
        hrs = re.search(r'(\d+)\s*(?:hours total|hours)|Total hours:\s*(\d+)', f.get('Stage', ''))
        wk = re.search(r'(\d+)\s*weeks?', f.get('Stage', ''))
        res.append({
            'n': c['n'], 'title': c['title'],
            'stage': (f.get('Stage', '').split('|')[0].replace('Stage:', '').strip() or None),
            'weeks': int(wk.group(1)) if wk else None,
            'hours': int(hrs.group(1) or hrs.group(2)) if hrs else None,
            'topics': [t.strip() for t in re.split(r';', f.get('Core topics') or f.get('Skills', '')) if t.strip()],
            'labs': [t.strip() for t in f.get('Hands-on labs', '').split(';') if t.strip()],
            'project': f.get('Portfolio project') or f.get('Project'),
            'assessment': f.get('Assessment') or f.get('Exam'),
        })
    return res

def section(lines, head_pat):
    i = next((k for k, l in enumerate(lines) if re.match(head_pat, l, re.I)), None)
    if i is None: return []
    body = []
    for l in lines[i+1:]:
        if l.startswith('# '): break
        body.append(l)
    return body

out = {}
for slug, fn in SRC.items():
    txt = open(f'docs/extracted/{fn}', encoding='utf8').read()
    lines = txt.split('\n')
    ms = months(lines)
    certs = [r for r in table_rows(lines, r'# \d+\. Certification Roadmap')]
    roles = table_rows(lines, r'# \d+\. Job Roles')
    hw = [clean(l) for l in section(lines, r'# \d+\. Hardware') if l.strip()]
    notes = [clean(re.sub(r'^[-*]\s*', '', l)) for l in section(lines, r'# \d+\. (Important )?Program Notes') if l.strip()]
    purpose = [clean(l) for l in section(lines, r'# 1\. Program Purpose') if l.strip()] or [clean(l) for l in lines[:6] if 'Program purpose' in l]
    cert_names = [(r[1] if r[0].strip().isdigit() else r[0]) for r in certs]
    roles_n = [r[0] for r in roles]
    low = txt.lower()
    tools = [t for t in TOOL_CANDIDATES if re.search(r'(?<![A-Za-z])' + re.escape(t.lower()) + r'(?![A-Za-z])', low)]
    out[slug] = {'source': fn, 'purpose': purpose, 'months': ms, 'certifications': cert_names, 'roles': roles_n,
                 'tools': tools, 'hardware': hw, 'notes': notes}
json.dump(out, open('docs/extracted/curriculum.json', 'w'), indent=1, ensure_ascii=False)
for k, v in out.items():
    hrs = sum(m['hours'] or 0 for m in v['months'])
    print(k, 'months', len(v['months']), 'hours', hrs or 'n/a', 'certs', len(v['certifications']), 'roles', len(v['roles']), 'tools', len(v['tools']),
          'projects', sum(1 for m in v['months'] if m['project']))
