# Create seo/<pattern>/ with pattern.json and an OUTLINE.md stub. Usage: new_pattern.py <pattern-slug> "<Name>" "<keyword pattern>"
import json, os, sys
slug, name, kw = sys.argv[1], sys.argv[2], sys.argv[3]
d = os.path.join('/home/user/NeuroNetwrks.com/tools/preview-gen/seo', slug)
os.makedirs(d, exist_ok=True)
p = os.path.join(d, 'pattern.json')
if not os.path.exists(p):
    json.dump({"name": name, "headline": name + ".", "intro": "", "keyword_pattern": kw, "required_faq": []}, open(p, 'w'), indent=1)
o = os.path.join(d, 'OUTLINE.md')
if not os.path.exists(o):
    open(o, 'w').write(f"# {name}\n\nKeyword pattern: {kw}\n\n## Sections (each H2 is a question)\n1. \n\n## Program mapping\n\n## Keywords\n| Keyword | Searches/month | Program | Status |\n|---|---|---|---|\n")
print('created', d)
