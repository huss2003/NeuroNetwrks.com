"""One-off generator for src/content/programs/*.mdx from docs/extracted/curriculum.json (facts) plus the
editorial copy below. Run once; after that edit the MDX files directly (re-running overwrites them).
Usage: python3 scripts/extract-curriculum.py && python3 scripts/generate-program-mdx.py"""
import json, re, yaml

D = json.load(open('docs/extracted/curriculum.json'))
ENTRY = {
    'ai-ml-engineering': 'Class 10 pass; basic school-level mathematics and computer familiarity',
    'cybersecurity': 'Class 10 pass; no technical background assumed',
    'data-science-ai': 'Class 10 pass; absolute beginners welcome',
    'product-ux-ai-design': 'Class 10 pass; no design background assumed',
    'software-development': 'Class 10 pass; no programming knowledge assumed',
}
EDIT = {
 'ai-ml-engineering': dict(
  name='3-Year AI/ML Engineering Professional Program', short='AI/ML Engineering',
  summary='From Python basics to machine learning, deep learning, generative AI and MLOps, with a portfolio of projects.',
  answer='AI/ML Engineering is a three-year, 624-hour specialisation for students who have passed Class 10. It starts with computer and Python basics and builds up to machine learning, deep learning, generative AI and MLOps, with a one-hour exam after each of 36 monthly modules and a project in every month.',
  related=['data-science-ai', 'software-development', 'ai-foundation'],
  kw=('AI ML engineering course after 10th', ['machine learning course India', 'AI course for beginners', 'generative AI course for students']),
  seo=('AI/ML Engineering Program, Class 10 Entry | NeuroNetworks', 'Three-year, 624-hour AI/ML Engineering program from Python basics to machine learning, deep learning, GenAI and MLOps. Class 10 entry.')),
 'cybersecurity': dict(
  name='3-Year Cybersecurity Professional Program', short='Cybersecurity',
  summary='From computer and networking basics to security operations and ethical hacking, practised in authorised labs.',
  answer='The Cybersecurity program is a three-year, 624-hour specialisation for students who have passed Class 10, with no technical background assumed. It moves from computers and networking to Linux, security operations and ethical hacking, practised in authorised lab environments, with a one-hour exam after each of 36 monthly modules.',
  related=['software-development', 'data-science-ai', 'ai-foundation'],
  kw=('cybersecurity course after 10th', ['ethical hacking course for beginners', 'cybersecurity course India', 'SOC analyst training']),
  seo=('Cybersecurity Program, Class 10 Entry | NeuroNetworks', 'Three-year, 624-hour Cybersecurity program: networking, Linux, security operations and ethical hacking in authorised labs. Class 10 entry.')),
 'data-science-ai': dict(
  name='3-Year Data Science & AI Professional Program', short='Data Science & AI',
  summary='From Python and SQL to analytics, machine learning, data engineering and generative AI, with a project portfolio.',
  answer='The Data Science & AI program is a three-year, 624-hour specialisation for Class 10 pass students who are absolute beginners. It progresses from computing, Python, SQL and statistics into analytics, machine learning, data engineering, deep learning, generative AI and MLOps, with a one-hour exam after every monthly module.',
  related=['ai-ml-engineering', 'software-development', 'ai-foundation'],
  kw=('data science course after 10th', ['data science course India', 'data analytics course for beginners', 'Python and SQL course']),
  seo=('Data Science & AI Program, Class 10 Entry | NeuroNetworks', 'Three-year, 624-hour Data Science & AI program: Python, SQL, analytics, machine learning, data engineering and GenAI. Class 10 entry.')),
 'product-ux-ai-design': dict(
  name='3-Year Product & UX / AI Design Professional Program', short='Product & UX / AI Design',
  summary='From visual and UX fundamentals to product thinking, AI-assisted design, prototyping and a professional portfolio.',
  answer='The Product & UX / AI Design program is a three-year, 624-hour specialisation for students who have passed Class 10. It begins with visual and UX fundamentals, moves through product thinking and project management, and ends with AI-assisted product design, research, design systems, prototyping and a professional portfolio.',
  related=['software-development', 'ai-ml-engineering', 'ai-foundation'],
  kw=('UX design course after 10th', ['UI UX design course India', 'product design course for beginners', 'AI product design course']),
  seo=('Product & UX / AI Design Program | NeuroNetworks AI Ed', 'Three-year, 624-hour Product & UX / AI Design program: visual design, UX research, product thinking, prototyping and AI design. Class 10 entry.')),
 'software-development': dict(
  name='3-Year Software Development Professional Program', short='Software Development',
  summary='From programming logic to full-stack, cloud and software engineering, with a high volume of hands-on projects.',
  answer='The Software Development program is a three-year, 624-hour specialisation for students who have passed Class 10, with no programming knowledge assumed. It progresses from computer and programming fundamentals to professional full-stack, cloud and software-engineering capability, with a one-hour exam after each of 36 monthly modules.',
  related=['ai-ml-engineering', 'cybersecurity', 'ai-foundation'],
  kw=('software development course after 10th', ['full stack developer course India', 'Java course for beginners', 'coding course after 10th']),
  seo=('Software Development Program, Class 10 Entry | NeuroNetworks', 'Three-year, 624-hour Software Development program: programming logic, Java, web, full-stack and cloud. Class 10 entry, built on projects.')),
}

def hw_clean(lines):
    out = []
    for l in lines:
        l = re.sub(r'^[>\-\s*]+', '', l).replace('**', '').strip()
        if l and not l.lower().startswith(('minimum', 'minimum specs')) and ':' in l: out.append(l)
    return out

def faqs_for(slug, e, v):
    roles = ', '.join(v['roles'][:4])
    return [
     {'q': 'Who can join this program?', 'a': f"{ENTRY[slug][0].upper()+ENTRY[slug][1:]}. The program is designed for students entering after Class 10."},
     {'q': 'How many hours is the program, and how is it structured?', 'a': 'It is 624 hours over three years (36 months): 4 hours a week for 52 weeks a year, or 208 hours a year. Each monthly module ends with a one-hour exam, and exam time is counted inside the 624 hours.'},
     {'q': 'Does the program guarantee a job or internship?', 'a': 'No. The curriculum aims at job readiness through skills, hands-on practice, a GitHub record and a portfolio, but it does not guarantee an internship, employment or salary.'},
     {'q': 'Which external certifications does the roadmap include?', 'a': 'The roadmap lists six external certifications: ' + '; '.join(v['certifications']) + '. They are awarded by the certifying organisations, not by this program, and passing an external exam is not guaranteed.'},
     {'q': 'What laptop do students need?', 'a': 'The curriculum document gives minimum specifications: ' + '; '.join(hw_clean(v['hardware'])[:5]) + '.' if hw_clean(v['hardware']) else 'Hardware requirements are listed in the curriculum.'},
     {'q': 'What kinds of roles does this program prepare students for?', 'a': f'The curriculum lists entry-level roles such as {roles}. Fit depends on the student\'s portfolio and on each employer\'s requirements.'},
    ]

def split_topics(m):
    t = m['topics']
    return t if len(t) > 1 else [x.strip(' .') for x in re.split(r',\s+', t[0])] if t else []

def write(slug, meta, body):
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=1000)
    open(f'src/content/programs/{slug}.mdx', 'w', encoding='utf8').write(f'---\n{fm}---\n\n{body}\n')

for slug, e in EDIT.items():
    v = D[slug]; ms = v['months']
    years = []
    for y in range(3):
        chunk = ms[y*12:(y+1)*12]
        years.append({'title': f'Year {y+1}', 'hours': 208, 'modules': [m['title'] for m in chunk]})
    meta = dict(name=e['name'], slug=slug, shortName=e['short'], level='specialisation', durationYears=3, totalHours=624,
        hoursPerWeek=4, entry=ENTRY[slug], summary=e['summary'], answer=e['answer'], audience=['school', 'parent'], years=years,
        assessment='One 1-hour exam after each of the 36 monthly modules (theory plus practical where appropriate). Exam time is included in the 624 hours.',
        certifications=v['certifications'], tools=v['tools'], projects=[m['project'] for m in ms if m['project']],
        careerRoles=v['roles'], hardware=hw_clean(v['hardware']), faqs=faqs_for(slug, e, v), related=e['related'],
        keywords={'primary': e['kw'][0], 'secondary': e['kw'][1]}, seo={'title': e['seo'][0], 'description': e['seo'][1]})
    body = f"Source: `docs/source/{v['source']}`. Page copy is assembled from the program data above; do not add claims that are not in the source document."
    write(slug, meta, body)

# Foundation course (docs/source Neuromind file; "Neuromind" is not confirmed as a public name)
txt = open('docs/extracted/Neuromind_1-Year_AI_Curriculum_Rebuilt_Teacher_Ready_Certification_Aligned_104_Hours_1.md', encoding='utf8').read()
mods = [re.sub(r'^Month \d+ — ', '', t).strip() for t in re.findall(r'^## (Month \d+ — .+)$', txt, re.M)[:12]]
port = re.search(r'# 9\. Practical portfolio sequence.*?\n\n(\|.*?)\n\n#', txt, re.S).group(1).split('\n')[2:]
projects = [re.split(r'\s*\|\s*', r.strip('| '))[1] for r in port]
f = dict(name='1-Year AI Foundations, Python & AI Applications Program', slug='ai-foundation', shortName='AI Foundation',
 level='foundation', durationYears=1, totalHours=104, hoursPerWeek=2, entry='Class 10 pass (or equivalent); no prior coding, AI or cloud experience required',
 summary='A beginner course from AI literacy to Python, data, machine learning and small AI applications, with optional certification preparation.',
 answer='AI Foundations is a one-year, 104-hour beginner course for learners who have passed Class 10. It moves from AI literacy to Python, data, machine learning, generative AI and a basic RAG prototype, and includes preparation for the Microsoft AI-901 and AWS AIF-C01 exams without promising a pass.',
 audience=['school', 'parent', 'institution'],
 years=[{'title': 'Year 1', 'hours': 104, 'modules': mods}],
 assessment='104 one-hour guided lectures; recommended pass mark 80%, with targeted remediation and a retry below the threshold. No assessment hours are added outside the 104.',
 certifications=['Microsoft Azure AI Fundamentals AI-901', 'AWS Certified AI Practitioner AIF-C01'],
 tools=['Python', 'Pandas', 'scikit-learn', 'Microsoft Foundry', 'AWS'], projects=projects, careerRoles=[],
 hardware=['Laptop or desktop with internet, a browser, and the ability to install Python or use a browser-based notebook', 'A phone alone is not sufficient for the programming labs'],
 faqs=[
  {'q': 'Who is the AI Foundations course for?', 'a': 'It is for learners who have passed Class 10 or equivalent, with no prior coding, AI or cloud experience. Learners should be able to read simple English instructions, use a browser and manage files.'},
  {'q': 'How long is the course?', 'a': 'It is 104 guided hours over 52 weeks, at 2 hours a week. Months 1 to 8 are core learning (64 hours), Months 9 and 10 prepare for Microsoft AI-901 (20 hours), and Months 11 and 12 prepare for AWS AIF-C01 (20 hours).'},
  {'q': 'Will I be certified, and does the course guarantee a pass?', 'a': 'The course prepares learners for two external exams, Microsoft AI-901 and AWS AIF-C01, but does not guarantee passing. Certification is awarded by Microsoft or AWS only after the learner passes their exam.'},
  {'q': 'Does this make me an AI/ML engineer?', 'a': 'No. It is a beginner applied-AI foundation, not a full software engineering course, and it does not qualify a learner as an AI/ML engineer.'},
  {'q': 'What do I need to take part?', 'a': 'A laptop or desktop with internet and a browser, able to install Python or use a browser-based notebook. A phone alone is not enough for the programming labs. Plan 10 to 15 minutes of homework after each lecture.'},
 ],
 related=['ai-ml-engineering', 'data-science-ai', 'software-development'],
 keywords={'primary': 'AI course for beginners after 10th', 'secondary': ['learn AI from scratch', 'Python for AI beginners', 'Microsoft AI-901 preparation']},
 seo={'title': 'AI Foundations Course, Class 10 Entry | NeuroNetworks', 'description': 'One-year, 104-hour AI Foundations course: AI basics, Python, data, machine learning and GenAI apps, with AI-901 and AIF-C01 exam preparation.'})
write('ai-foundation', f, "Source: `docs/source/Neuromind_1-Year_AI_Curriculum_Rebuilt_Teacher_Ready_Certification_Aligned_104_Hours_1.docx`. The name \"Neuromind\" appears only in the file name; do not use it publicly until the owner confirms.")
print('written', len(EDIT) + 1)
