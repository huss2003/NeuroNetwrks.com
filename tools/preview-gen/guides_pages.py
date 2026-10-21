# Guides: answer-first articles for search and AI answer engines. exec'd from build.py (shares its namespace).
# Every fact comes from the program data in src/content/programs (D, PROGRAMS). No invented numbers, outcomes or prices.

GUIDE_DATE = "2026-10-14"
GUIDE_DATE_TXT = "14 October 2026"

def g_prog_link(slug, label=None):
    return f'<a href="/programs/{slug}">{E(label or prog(slug)[2])}</a>'

def g_facts(slugs):
    rows = ""
    for s in slugs:
        d, p = D[s], prog(s)
        rows += (f'<tr><th scope="row">{g_prog_link(s)}</th><td>{p[4]}</td><td>{p[3]} hours</td><td>{d["hoursPerWeek"]} hours a week</td>'
                 f'<td>{E(d["entry"].split(";")[0])}</td></tr>')
    return ('<div class="gd-table"><table><caption class="vh">Program facts</caption><thead><tr><th scope="col">Program</th><th scope="col">Length</th>'
            '<th scope="col">Total</th><th scope="col">Pace</th><th scope="col">Entry</th></tr></thead><tbody>' + rows + '</tbody></table></div>')

def g_list(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"

def g_years(slug):
    out = ""
    for y in D[slug]["years"]:
        out += f'<li><strong>{E(y["title"])} ({y["hours"]} hours):</strong> {E(", ".join(y["modules"]))}.</li>'
    return f'<ol class="gd-years">{out}</ol>'

def g_join(xs, n=None):
    xs = list(xs)[:n] if n else list(xs)
    return E(", ".join(xs[:-1]) + " and " + xs[-1]) if len(xs) > 1 else E(xs[0])

NOTE_JOBS = "No program guarantees a job, internship, salary or exam pass. Certification exams are run and awarded by the certifying organisations."

# ------------------------------------------------------------------ guide content
GUIDES = [
 {"slug": "ai-courses-after-10th", "title": "AI courses after 10th: eligibility, duration, projects",
  "h1": ("AI courses after 10th:", "eligibility, duration and projects"),
  "desc": "What an AI course after Class 10 covers, how many hours it takes, what students build, and how to choose between a 6-month and a 3-year path.",
  "lead": "Yes, a student who has just passed Class 10 can start learning AI properly. Here is what a real course covers, how long it takes and how to pick the right length.",
  "tldr": ["A beginner AI course after Class 10 should start with AI literacy and Python, then move to data, machine learning and generative AI.",
           "Neuronetworks AI Ed offers a 6-month, 104-hour AI Foundation course and a 3-year, 624-hour AI/ML Engineering program.",
           "No prior coding is needed for AI Foundation. Choose the 3-year path if you want depth: deep learning, MLOps and a portfolio of projects."],
  "progs": ["ai-foundation", "ai-ml-engineering"],
  "sections": [
   ("Can you learn AI after Class 10?",
    f"<p>Yes. Learning AI after Class 10 is realistic if the course starts from zero. Students need basic school mathematics and computer familiarity, not prior coding. A good course teaches what AI is, then Python, data handling and machine learning step by step, with a project at each stage so understanding is tested by building, not just reading.</p>"
    f"<p>The {g_prog_link('ai-foundation')} course is open from Class 9 and assumes no coding, AI or cloud experience. The {g_prog_link('ai-ml-engineering')} program is open from Class 11 and asks for basic school-level mathematics.</p>"),
   ("What does an AI course after 10th cover?",
    "<p>A complete beginner AI course covers six areas: how modern AI works, responsible use of AI tools, Python programming, working with data, machine learning, and generative AI with large language models. Better courses add computer vision, natural language processing and a first retrieval-augmented generation (RAG) prototype.</p>"
    "<p>The AI Foundation course is 104 one-hour lectures in this order:</p>" + "<ol>" + "".join(f"<li>{E(m)}</li>" for m in D["ai-foundation"]["years"][0]["modules"]) + "</ol>"),
   ("How long does it take: 6 months or 3 years?",
    "<p>It depends on the goal. Six months at four hours a week (104 hours) is enough to understand AI, write Python, train a simple model and build a small generative AI app. Three years at four hours a week (624 hours) is the depth needed for machine learning engineering: deep learning, transformers, MLOps, cloud AI and a professional portfolio.</p>"
    + g_facts(["ai-foundation", "ai-ml-engineering"])),
   ("What will a student build?",
    "<p>Students should finish every stage with something they made. In AI Foundation that includes "
    + g_join(D["ai-foundation"]["projects"][2:7]).lower() + ". In AI/ML Engineering every one of the 36 months ends with a project, including a house-price regression model, an "
    '<a href="/projects/image-classification">image classification application</a>, a <a href="/projects/document-rag-assistant">document RAG assistant</a> and <a href="/projects/agentflow-ai">AgentFlow AI</a>, a tool-using agent.</p>'),
   ("Which certifications can students prepare for?",
    f"<p>AI Foundation includes preparation for {E(D['ai-foundation']['certifications'][0])} and {E(D['ai-foundation']['certifications'][1])}. AI/ML Engineering prepares for {g_join(D['ai-ml-engineering']['certifications'])}. {NOTE_JOBS}</p>"),
   ("How to choose the right AI course",
    g_list(["<strong>Check the hours, not just the months.</strong> Total guided hours tell you how much is really taught.",
            "<strong>Ask what is built each month.</strong> A project list is the clearest sign of practical learning.",
            "<strong>Look for regular assessment.</strong> At Neuronetworks AI Ed, three-year programs have a one-hour exam after each of 36 monthly modules.",
            "<strong>Make sure Python is taught from the start.</strong> Almost all AI work uses it.",
            "<strong>Be wary of promises.</strong> No honest course can guarantee a job or an exam result."])),
  ],
  "faqs": [("Is AI difficult to learn after 10th?", "It is manageable when taught in order. AI Foundation starts with AI literacy and Python basics and needs no prior coding. Each one-hour lecture builds on the last, and a short unit exam closes each major unit."),
           ("Do I need maths to learn AI after 10th?", "School-level mathematics is enough to start. The AI/ML Engineering program teaches the mathematics needed for machine learning itself, in two modules called Math for ML I and II."),
           ("What laptop is needed for an AI course?", "For the full AI/ML Engineering roadmap, the recommended setup is an Intel i5 or Ryzen 5 processor or better, 16 GB RAM (32 GB recommended) and a 512 GB SSD. A dedicated NVIDIA GPU helps for deep learning but is not needed at the start."),
           ("Do students get a certificate?", "Yes. Students who complete AI Foundation or AI/ML Engineering receive a Neuronetworks AI Ed certificate. External certifications such as Microsoft AI-901 are separate and awarded by Microsoft or AWS after their exams."),
           ("How much does the course cost?", 'Fees are shared on enquiry. <a href="/contact?topic=fees">Ask us about fees</a>.')]},

 {"slug": "courses-after-10th", "title": "Courses after 10th: 6 technology paths compared",
  "h1": ("Best courses after 10th:", "six technology paths compared"),
  "desc": "Compare six technology courses after Class 10: AI, AI/ML, coding, data science, UI/UX design and cyber security, by hours, skills and projects.",
  "lead": "Six technology paths are open to students straight after Class 10. This guide compares them side by side so a student and parent can choose together.",
  "tldr": ["Technology courses after Class 10 include AI, machine learning, software development, data science, UI/UX design and cybersecurity.",
           "At Neuronetworks AI Ed, AI Foundation is a 6-month, 104-hour start; the other five are 3-year, 624-hour specialisations.",
           "Choose by what the student enjoys doing: building apps, finding patterns in data, designing screens or defending systems."],
  "progs": [p[0] for p in PROGRAMS],
  "sections": [
   ("Which technology courses can you do after 10th?",
    "<p>After Class 10, a student can begin six technology tracks: a six-month AI foundation course, or a three-year specialisation in AI/ML engineering, software development, data science and AI, product and UX design with AI, or cybersecurity. The five specialisations accept students from Class 11 onwards and AI Foundation is open from Class 9; all assume little or no technical background.</p>" + g_facts([p[0] for p in PROGRAMS])),
   ("What does each path teach?",
    "<dl class=\"gd-dl\">" + "".join(f"<dt>{g_prog_link(p[0])}</dt><dd>{E(D[p[0]]['summary'])}</dd>" for p in PROGRAMS) + "</dl>"),
   ("Which path suits which student?",
    g_list(["<strong>Likes making things work:</strong> " + g_prog_link("software-development") + " (Java, JavaScript, React, Spring Boot, cloud).",
            "<strong>Curious how AI thinks:</strong> " + g_prog_link("ai-ml-engineering") + " or start with " + g_prog_link("ai-foundation") + ".",
            "<strong>Enjoys numbers and questions:</strong> " + g_prog_link("data-science-ai") + " (Python, SQL, statistics, dashboards, ML).",
            "<strong>Notices how apps feel to use:</strong> " + g_prog_link("product-ux-ai-design") + " (research, wireframes, prototypes, design systems).",
            "<strong>Likes puzzles and protecting things:</strong> " + g_prog_link("cybersecurity") + " (networking, Linux, SOC, ethical hacking in authorised labs)."])),
   ("How are the three-year programs structured?",
    "<p>Each three-year specialisation runs for 36 months at four hours a week. Every month is one module, ends with a project and closes with a one-hour exam. Exam time is included in the 624 hours. Year 1 builds foundations, Year 2 builds depth, and Year 3 focuses on advanced topics, a capstone and a professional portfolio.</p>"
    '<p>See every module month by month on the <a href="/curriculum">curriculum page</a>.</p>'),
   ("Can you study this alongside Class 11 and 12?",
    "<p>The pace is designed to sit beside school: four hours a week for both AI Foundation and the three-year programs. Families should still plan around board exam periods; ask us about batch timings when you enquire.</p>"),
  ],
  "faqs": [("Which is the best technology course after 10th?", "There is no single best course. The right one matches what the student enjoys. If unsure, the 6-month AI Foundation course is a low-commitment way to try programming, data and AI before choosing a three-year specialisation."),
           ("Are these diploma or certificate courses?", "They are certificate programs. Students who complete a program receive a Neuronetworks AI Ed certificate. External certifications from Microsoft, AWS, Google and others are separate, optional, and awarded by those organisations after their own exams."),
           ("Do these courses guarantee a job?", NOTE_JOBS)]},

 {"slug": "computer-coding-courses-after-10th", "title": "Computer and coding courses after 10th: which to choose",
  "h1": ("Computer and coding courses after 10th:", "which one to choose"),
  "desc": "What a coding course after Class 10 teaches: Java, JavaScript, React, databases and cloud over 3 years and 624 hours, with a project every month.",
  "lead": "Coding is a strong choice after Class 10 for students who like solving problems step by step. Here is what a serious software development course teaches, year by year.",
  "tldr": ["A coding course after Class 10 should start with programming logic, then a main language, web basics, databases and teamwork with Git.",
           "The Software Development program is 3 years and 624 hours, with no programming knowledge assumed.",
           "Students build 36 projects, from a first program portfolio to a full production software product."],
  "progs": ["software-development", "ai-foundation"],
  "sections": [
   ("Is coding a good option after Class 10?",
    "<p>Coding is a good option after Class 10 for students who enjoy logic, puzzles and making things work. Starting early gives time to practise, which matters more than talent. A structured course turns that practice into skills employers recognise: a main programming language, web development, databases, testing and working in a team with Git.</p>"),
   ("What does a 3-year software development course cover?",
    "<p>The " + g_prog_link("software-development") + " program covers these modules, one per month:</p>" + g_years("software-development")),
   ("Which languages and tools are taught?",
    f"<p>Students work with {g_join(D['software-development']['tools'])}. Java is the main language in Year 1 and the backend language in Year 2 with Spring Boot; JavaScript, TypeScript and React cover the front end.</p>"),
   ("What do students build?",
    "<p>Every month ends with a project. Examples: " + g_join(D["software-development"]["projects"][::4]).lower() + ". By Year 3 students build a full-stack SaaS application and a final production software product with a complete GitHub portfolio.</p>"),
   ("Which certifications does it prepare for?",
    f"<p>The program prepares students for {g_join(D['software-development']['certifications'])}. {NOTE_JOBS}</p>"),
  ],
  "faqs": [("Which coding language should I learn first after 10th?", "The Software Development program starts with programming logic and then Java, followed by HTML, CSS and JavaScript. If AI interests you more, the AI Foundation course starts with Python."),
           ("Can I learn coding without a computer science background?", "Yes. The Software Development program assumes no programming knowledge. The first module is Computer & Software Foundations, followed by Programming Logic & Problem Solving."),
           ("How many hours a week is the coding course?", "Four hours a week, 208 hours a year, 624 hours over three years, including a one-hour exam after each monthly module.")]},

 {"slug": "cyber-security-course-after-10th", "title": "Cyber security course after 10th: what you study",
  "h1": ("Cyber security course after 10th:", "what you actually study"),
  "desc": "A cyber security course after Class 10, explained: networking, Linux, SOC work, ethical hacking in authorised labs, cloud security and 6 certifications.",
  "lead": "Cybersecurity after Class 10 starts with how computers and networks work, not hacking. Here is the full path, from first networks to security operations.",
  "tldr": ["A real cybersecurity course begins with computers, networking, Linux and Windows before moving to defence and testing.",
           "The Neuronetworks AI Ed Cybersecurity program is 3 years and 624 hours, with no technical background assumed.",
           "Ethical hacking is taught only in authorised lab environments, alongside SOC monitoring, incident response and cloud security."],
  "progs": ["cybersecurity", "software-development"],
  "sections": [
   ("Can you study cyber security after 10th?",
    "<p>Yes. Cybersecurity can be learned from Class 10 if the course starts with fundamentals. Security work depends on understanding how computers, operating systems and networks behave. A good course spends its first year there, then teaches defence, monitoring and authorised testing, so students learn to protect systems responsibly.</p>"),
   ("What is taught each year?",
    "<p>The " + g_prog_link("cybersecurity") + " program runs one module per month:</p>" + g_years("cybersecurity")),
   ("Is ethical hacking part of it?",
    "<p>Yes, in Year 2, and only in authorised lab environments. Students cover ethical hacking foundations, web application security, network penetration testing, Active Directory security and privilege escalation, then write professional reports. The aim is to understand attacks in order to defend against them.</p>"),
   ("Which tools do students use?",
    f"<p>Students practise with {g_join(D['cybersecurity']['tools'])}.</p>"),
   ("What does a cyber security analyst do?",
    "<p><strong>A cyber security analyst protects an organisation by watching for attacks and responding when one happens.</strong> Most start in a security operations centre (SOC), reading alerts and logs, deciding what is real, and following a playbook to contain it, often as part of a shift team.</p>"
    "<p>This program builds that path: SOC foundations, logs and SIEM, and endpoint security in year 1, incident response in year 2, then SOC engineering, Splunk, Microsoft Sentinel and KQL, Defender XDR, threat hunting with MITRE ATT&amp;CK, digital forensics and SC-200 preparation in year 3. Microsoft describes SC-200 as its certification for security operations analysts.</p>"),
   ("Which certifications does it prepare for?",
    f"<p>{g_join(D['cybersecurity']['certifications'])}. {NOTE_JOBS}</p>"),
  ],
  "faqs": [("Is cyber security hard for a 10th pass student?", "It is demanding but structured. The program assumes no technical background and spends Year 1 on computer, networking, Linux and Windows fundamentals before security operations."),
           ("Is ethical hacking legal to learn?", "Learning it is legal when practised only on systems you are authorised to test. In this program all testing happens in authorised lab environments."),
           ("What roles does the curriculum prepare students for?", "The curriculum is designed around roles such as " + g_join(D["cybersecurity"]["careerRoles"], 4) + ". " + NOTE_JOBS)]},

 {"slug": "data-science-after-10th", "title": "Data science course after 10th: is it possible?",
  "h1": ("Data science after 10th:", "skills, path and projects"),
  "desc": "A data science course after Class 10, explained: Python, SQL, statistics, dashboards, machine learning and generative AI over 3 years and 624 hours.",
  "lead": "Data science teaches a student to ask good questions of data and answer them with code. This is what the path looks like from Class 10.",
  "tldr": ["Data science after Class 10 starts with Python, SQL and statistics, then analytics and dashboards, then machine learning.",
           "The Data Science & AI program is 3 years and 624 hours, and absolute beginners are welcome.",
           "Students finish with a portfolio including dashboards, data pipelines, an ML API, a RAG application and a capstone."],
  "progs": ["data-science-ai", "ai-ml-engineering"],
  "sections": [
   ("What is data science, in simple words?",
    "<p>Data science is using data to answer questions and make decisions. A data scientist collects and cleans data, explores it with statistics and charts, builds models that predict or group things, and explains the results clearly. It combines programming, mathematics and communication, which is why it suits students who like both numbers and explaining ideas.</p>"),
   ("What does the 3-year course cover?",
    "<p>The " + g_prog_link("data-science-ai") + " program, one module per month:</p>" + g_years("data-science-ai")),
   ("Data science or AI/ML engineering?",
    "<p>Both use Python and machine learning. Data science leans towards analysis, statistics, dashboards and data engineering. " + g_prog_link("ai-ml-engineering") + " leans towards building and deploying AI systems: deep learning, transformers, agents and MLOps. Students who enjoy explaining findings often prefer data science; those who enjoy building software with AI often prefer AI/ML.</p>"),
   ("What do students build?",
    "<p>Examples include " + g_join(D["data-science-ai"]["projects"][::5]).lower() + ".</p>"),
   ("Which certifications does it prepare for?",
    f"<p>{g_join(D['data-science-ai']['certifications'])}. {NOTE_JOBS}</p>"),
  ],
  "faqs": [("Can a 10th pass student learn data science?", "Yes. The program welcomes absolute beginners and starts with computer, data and Python foundations before SQL and statistics."),
           ("Do I need to be good at maths for data science?", "Comfort with school mathematics helps. Statistics is taught inside the program in two modules, Statistics I and II, before machine learning."),
           ("Which tools are used?", g_join(D["data-science-ai"]["tools"]) + ".")]},

 {"slug": "ui-ux-designer-after-10th", "title": "How to become a UI/UX designer after 10th",
  "h1": ("How to become a UI/UX designer", "after 10th"),
  "desc": "A UI/UX design course after Class 10: user research, wireframes, prototypes, design systems and AI product design over 3 years and 624 hours.",
  "lead": "UI/UX design is about making products easy and pleasant to use. Here is how a student can learn it from Class 10, including designing AI products.",
  "tldr": ["UI/UX design after Class 10 starts with visual design and user research, then wireframes, interaction design and prototyping.",
           "The Product and UX/UI Design program is 3 years and 624 hours, with no design background assumed.",
           "Years 2 and 3 add product management, design systems, AI UX patterns and a portfolio of 6 to 10 flagship projects."],
  "progs": ["product-ux-ai-design", "software-development"],
  "sections": [
   ("What is UI/UX design?",
    "<p>UX (user experience) design is deciding how a product works for the people using it: what they need, how they move through it and where they get stuck. UI (user interface) design is how it looks: layout, type, colour and components. Together they turn research about real users into screens that are clear and easy to use.</p>"),
   ("What does the 3-year course cover?",
    "<p>The " + g_prog_link("product-ux-ai-design") + " program, one module per month:</p>" + g_years("product-ux-ai-design")),
   ("Where does AI come in?",
    "<p>From Year 2, students study AI product fundamentals, AI UX patterns, AI product discovery and AI prototyping, and in Year 3 AI research and evaluation, accessible and inclusive AI, and AI design systems. They learn to design products that use AI well, such as an AI assistant prototype, not just to use AI tools.</p>"),
   ("What do students build?",
    "<p>Examples include " + g_join(D["product-ux-ai-design"]["projects"][::5]).lower() + ".</p>"),
   ("Which certifications does it prepare for?",
    f"<p>{g_join(D['product-ux-ai-design']['certifications'])}. {NOTE_JOBS}</p>"),
  ],
  "faqs": [("Do I need to draw well for UI/UX design?", "No. UI/UX is about solving problems for users. Visual design fundamentals are taught in Year 1, and the program assumes no design background."),
           ("Is coding needed for UI/UX design?", "Coding is not the focus of this program. Students learn research, wireframing, prototyping and design systems. Those who want to build interfaces in code can look at Software Development."),
           ("How long is the UI/UX course?", "Three years, 624 hours, four hours a week, with a project and a one-hour exam every month.")]},

 {"slug": "ai-vs-software-vs-data-science", "title": "AI vs software vs data science: a parent's guide",
  "h1": ("AI, software or data science?", "A guide for parents"),
  "desc": "Help your child choose between AI/ML engineering, software development and data science after Class 10: what each teaches, tools, projects and pace.",
  "lead": "Three tech paths sound similar but lead to different daily work. This guide is written for parents deciding with their child after Class 10.",
  "tldr": ["AI/ML engineering builds AI systems; software development builds applications; data science answers questions with data.",
           "All three are 3 years, 624 hours, 4 hours a week, with a project and a one-hour exam every month.",
           "Not sure yet? The 6-month AI Foundation course lets a student try Python, data and AI first."],
  "progs": ["ai-ml-engineering", "software-development", "data-science-ai", "ai-foundation"],
  "sections": [
   ("What is the difference in one line each?",
    '<dl class="gd-dl"><dt>' + g_prog_link("ai-ml-engineering") + '</dt><dd>Builds systems that learn from data: models, deep learning, generative AI, agents and MLOps.</dd>'
    '<dt>' + g_prog_link("software-development") + '</dt><dd>Builds websites and applications: Java, JavaScript, React, databases, APIs and cloud.</dd>'
    '<dt>' + g_prog_link("data-science-ai") + '</dt><dd>Answers questions with data: SQL, statistics, dashboards, machine learning and data pipelines.</dd></dl>'),
   ("How do they compare side by side?",
    g_facts(["ai-ml-engineering", "software-development", "data-science-ai"]) +
    '<div class="gd-table"><table><caption class="vh">Main tools</caption><thead><tr><th scope="col">Program</th><th scope="col">Main tools</th></tr></thead><tbody>'
    + "".join(f'<tr><th scope="row">{g_prog_link(s)}</th><td>{g_join(D[s]["tools"])}</td></tr>' for s in ["ai-ml-engineering", "software-development", "data-science-ai"]) + "</tbody></table></div>"),
   ("How can a parent tell which suits their child?",
    g_list(["If your child enjoys <strong>building and fixing things</strong> on a computer, software development fits.",
            "If they ask <strong>how ChatGPT or face unlock works</strong>, AI/ML engineering fits.",
            "If they like <strong>charts, sports statistics or spotting patterns</strong>, data science fits.",
            "If you cannot tell yet, " + g_prog_link("ai-foundation") + " (6 months, 4 hours a week) is a sensible first step."])),
   ("What should parents check before enrolling?",
    g_list(["The total guided hours and weekly time commitment.",
            "What is built and assessed each month.",
            "Recommended laptop specification.",
            'Fees, intake dates and batch timings (<a href="/contact?topic=fees">ask us</a>).',
            "How the institute handles consent and data for students under 18."])),
  ],
  "faqs": [("Which has better career scope: AI, software or data science?", "All three are active fields. Scope depends far more on the skills and portfolio a student builds than on the label. " + NOTE_JOBS),
           ("Can my child switch paths later?", "The first months of all three overlap in computer and programming foundations, so early skills carry over. Ask us about switching when you enquire."),
           ("Who do we contact for a student under 18?", 'For students under 18, a parent or guardian is the main contact. <a href="/admissions">See admissions</a>.')]},

 {"slug": "ai-projects-for-students", "title": "AI projects for students: from classifier to AI agent",
  "h1": ("AI projects for students:", "from image classifier to AI agent"),
  "desc": "Real AI projects students build in the AI/ML Engineering program: an image classifier, a document RAG assistant and AgentFlow AI, a tool-using agent.",
  "lead": "The best way to learn AI is to build with it. These are projects from the AI/ML Engineering roadmap, in the order students meet them.",
  "tldr": ["Students build one project every month across 36 months of the AI/ML Engineering program.",
           "Three flagship examples: an image classification app (Year 2), a document RAG assistant and AgentFlow AI, a tool-using agent (Year 3).",
           "Beginners start smaller: Python exercises, data cleaning and a regression model in Year 1."],
  "progs": ["ai-ml-engineering", "ai-foundation"],
  "sections": [
   ("Why do projects matter when learning AI?",
    "<p>Projects turn ideas into skills. Training a model, testing it on new data and building a simple interface teaches more than reading about it, and every finished project becomes portfolio evidence. That is why each monthly module in the three-year programs ends with a project, followed by a one-hour exam.</p>"),
   ("Which AI projects come first?",
    "<p>Year 1 of " + g_prog_link("ai-ml-engineering") + " builds foundations: " + g_join(D["ai-ml-engineering"]["projects"][:12]).lower() + ".</p>"),
   ("Image classification application",
    '<p>In Year 2, students prepare an image dataset, train or load a model, evaluate its predictions and build a simple web interface. <a href="/projects/image-classification">See the image classification project</a>.</p>'),
   ("Document RAG assistant",
    '<p>In Year 3, students build an assistant that answers questions from documents using retrieval-augmented generation, with answers that cite their sources. <a href="/projects/document-rag-assistant">See the document RAG assistant</a>.</p>'),
   ("AgentFlow AI: a tool-using agent",
    '<p>Also in Year 3, students build an AI agent that plans tasks, calls tools such as web search, code execution and file operations, and verifies its results safely. <a href="/projects/agentflow-ai">See AgentFlow AI</a>.</p>'),
   ("Can beginners do AI projects?",
    "<p>Yes, at the right scale. The 6-month " + g_prog_link("ai-foundation") + " course includes " + g_join(D["ai-foundation"]["projects"][:8]).lower() + ".</p>"),
  ],
  "faqs": [("What is a good first AI project for a student?", "A small machine learning project on a clean CSV dataset, such as predicting a number or a category, is a good start. AI Foundation includes an ML mini-project of this kind."),
           ("Do students need a GPU for these projects?", "Not at first. Integrated graphics are enough for basic ML. An NVIDIA RTX 4060 8 GB or better is recommended for the full AI/ML roadmap, mainly for deep learning."),
           ("Where can I see all projects?", 'Every project, month by month, is on the <a href="/curriculum">curriculum page</a> and the <a href="/projects">projects page</a>.')]},
 {"slug": "career-options-after-10th", "title": "Career options after 10th in AI and technology",
  "h1": ("Career options after 10th:", "AI and technology paths"),
  "desc": "Confused about career options after 10th? A clear map of AI, software, data, design and cyber security paths, the skills each needs and how to start.",
  "lead": "Feeling unsure after Class 10 is normal. This guide maps the technology career paths, what each involves day to day and how a student can start building skills now.",
  "tldr": ["Technology careers after 10th fall into five families: AI/ML, software, data, product and UX design, and cyber security.",
           "Students can start building real skills alongside Class 11 and 12, at two to four hours a week.",
           "Start broad if unsure: a 6-month AI Foundation course covers Python, data and AI before a student commits."],
  "progs": ["ai-foundation", "ai-ml-engineering", "software-development", "cybersecurity"],
  "sections": [
   ("What are the main technology career options after 10th?",
    "<p>The main technology career families open to a student after Class 10 are AI and machine learning, software development, data science, product and UX design, and cyber security. Each needs different strengths: building, analysing, designing or protecting. Students can begin skills training for any of them now, alongside school, and choose a stream or degree later with more confidence.</p>"),
   ("What roles does each path lead towards?",
    "<p>These are the roles each Neuronetworks AI Ed curriculum is designed around. They are entry-level roles a student can work towards over several years, not promises.</p>"
    '<dl class="gd-dl">' + "".join(f"<dt>{g_prog_link(s)}</dt><dd>{g_join(D[s]['careerRoles'], 5)}.</dd>" for s in ["ai-ml-engineering", "software-development", "data-science-ai", "product-ux-ai-design", "cybersecurity"]) + "</dl>"
    f"<p>{NOTE_JOBS}</p>"),
   ("Which stream should I take in Class 11 for a tech career?",
    "<p>Science with mathematics keeps the most options open for engineering degrees in computer science, AI and data. Skills courses like these accept any student from Class 11 onwards, though, so a student in any stream can build programming, design or security skills and a project portfolio in parallel.</p>"),
   ("I am confused about my career after 10th. Where do I start?",
    g_list(["List what you enjoy: building, puzzles, numbers, drawing or helping people.",
            "Try a small project in each area before committing: a Python program, a data chart, a screen design.",
            "Talk it through with a parent and someone working in the field.",
            "If you want a structured start, " + g_prog_link("ai-foundation") + " takes six months at four hours a week and touches programming, data and AI.",
            'Read <a href="/guides/courses-after-10th">the six paths compared</a> to see hours, tools and projects side by side.'])),
  ],
  "faqs": [("Which career is best after 10th?", "The best career is one that matches the student's strengths and interests. Technology paths reward steady practice and a portfolio of projects more than early talent."),
           ("Can I start a tech career without science in Class 11?", "Skills programs here accept any student from Class 11 onwards. Some degree routes, such as B.Tech, need science with mathematics, so check the course you plan for later."),
           ("Do these paths guarantee a job?", NOTE_JOBS)]},

 {"slug": "become-ai-engineer-after-10th", "title": "How to become an AI engineer after 10th: step by step",
  "h1": ("How to become an AI engineer", "after 10th, step by step"),
  "desc": "A step-by-step path to becoming an AI engineer after Class 10: Python, maths for ML, machine learning, deep learning, generative AI, MLOps and a portfolio.",
  "lead": "Becoming an AI engineer is a multi-year path. Here are the steps in order, with the hours and projects for each.",
  "tldr": ["The path is: Python, maths for machine learning, data preparation, classical ML, deep learning, generative AI and MLOps.",
           "The AI/ML Engineering program covers these steps over 3 years and 624 hours, with a project every month.",
           "A portfolio of 6 to 10 flagship projects is the main evidence of skill at the end."],
  "progs": ["ai-ml-engineering", "ai-foundation", "data-science-ai"],
  "sections": [
   ("What does an AI engineer do?",
    "<p>An AI engineer builds software that uses machine learning and generative AI: preparing data, training or adapting models, testing them and running them reliably for real users. The work combines programming, mathematics and engineering practice such as version control, containers, cloud services and monitoring.</p>"),
   ("Step 1: Learn Python and computer basics",
    "<p>Start with how computers work and Python programming. In " + g_prog_link("ai-ml-engineering") + " this is the first three months: Computer + AI Foundations, Python Fundamentals and Python for AI.</p>"),
   ("Step 2: Learn the maths and data skills for ML",
    "<p>Machine learning rests on statistics, linear algebra and careful data handling. The program covers Math for ML I and II, then Data Preparation, before any models are trained.</p>"),
   ("Step 3: Machine learning foundations",
    "<p>Next come ML foundations, model evaluation, classical ML and unsupervised ML, ending Year 1 with a capstone. Projects include a house-price regression model, a customer-risk classifier and customer segmentation.</p>"),
   ("Step 4: Deep learning, vision and language",
    '<p>Year 2 covers deep learning with PyTorch and TensorFlow, computer vision, NLP, transformers and MLOps. One project is an <a href="/projects/image-classification">image classification application</a>.</p>'),
   ("Step 5: Generative AI, agents and a portfolio",
    '<p>Year 3 covers generative AI, embeddings and RAG, agents, fine-tuning, AI safety, cloud AI engineering and system design, ending with a portfolio of 6 to 10 flagship projects and a final capstone. Examples are the <a href="/projects/document-rag-assistant">document RAG assistant</a> and <a href="/projects/agentflow-ai">AgentFlow AI</a>.</p>'),
   ("Not ready for 3 years?",
    "<p>The 6-month " + g_prog_link("ai-foundation") + " course (104 hours, 4 hours a week) covers Python, data, machine learning, generative AI, RAG and AI agents, ending with a deployed AI application and a capstone, and is a good test of interest first.</p>"),
  ],
  "faqs": [("How many years does it take to become an AI engineer after 10th?", "The AI/ML Engineering program takes three years at four hours a week (624 hours). Many students also pursue a degree; skills and a project portfolio are built alongside."),
           ("Is maths compulsory for AI engineering?", "Yes, to a working level. The program teaches the needed maths in two dedicated modules, starting from school-level mathematics."),
           ("What should I learn first for AI?", "Python. It is the first programming language in both AI Foundation and AI/ML Engineering.")]}
]


# ------------------------------------------------------------------ sources, fresh facts and in-text links (SEO pass, 18 Oct 2026)
# Each entry: date of the content change, extra sentences/links appended to a section (by index), and the sources checked.
CHK = "checked 18 October 2026"
SRC_NASSCOM = ("Technology Sector in India: Strategic Review 2026", "https://nasscom.in/knowledge-center/publications/technology-sector-india-strategic-review-2026", "Nasscom, February 2026")
SRC_JEE = ("JEE (Main) 2026 Information Bulletin", "https://cdnbbsr.s3waas.gov.in/s3f8e59f4b2fe7c5705bf878bbd494ccdf/uploads/2025/11/202511021649722475.pdf", "National Testing Agency, November 2025")
SRC_SO = ("Stack Overflow Developer Survey 2025: Technology", "https://survey.stackoverflow.co/2025/technology", "Stack Overflow, " + CHK)
SRC_AI901 = ("Microsoft Certified: Azure AI Fundamentals (AI-901)", "https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-fundamentals/", "Microsoft Learn, page updated 14 July 2026")
SRC_AIF = ("AWS Certified AI Practitioner", "https://aws.amazon.com/certification/certified-ai-practitioner/", "Amazon Web Services, " + CHK)
SRC_AZ900 = ("Microsoft Certified: Azure Fundamentals (AZ-900)", "https://learn.microsoft.com/en-us/credentials/certifications/azure-fundamentals/", "Microsoft Learn, page updated 20 July 2026")
SRC_DP900 = ("Microsoft Certified: Azure Data Fundamentals (DP-900)", "https://learn.microsoft.com/en-us/credentials/certifications/azure-data-fundamentals/", "Microsoft Learn, page updated 21 July 2026")
SRC_GDA = ("Google Data Analytics Certificate", "https://grow.google/certificates/data-analytics/", "Google, " + CHK)
SRC_ISC2 = ("ISC2 Certified in Cybersecurity (CC)", "https://www.isc2.org/certifications/cc", "ISC2, " + CHK)
SRC_SECPLUS = ("CompTIA Security+", "https://www.comptia.org/en-us/certifications/security/", "CompTIA, " + CHK)
SRC_SC200 = ("Microsoft Certified: Security Operations Analyst Associate (SC-200)", "https://learn.microsoft.com/en-us/credentials/certifications/security-operations-analyst/", "Microsoft Learn, " + CHK)
SRC_PY = ("Python for beginners: getting started", "https://www.python.org/about/gettingstarted/", "Python Software Foundation, " + CHK)
SRC_PCEP = ("PCEP: Certified Entry-Level Python Programmer", "https://pythoninstitute.org/pcep", "Python Institute, " + CHK)
SRC_NCS = ("National Career Service", "https://www.ncs.gov.in/", "Ministry of Labour & Employment, Government of India, " + CHK)
def gl(slug, text):
    return f'<a href="/guides/{slug}">{text}</a>'
GUIDE_EXTRA = {
 "ai-courses-after-10th": {"date": "2026-10-18", "sources": [SRC_AI901, SRC_AIF, SRC_NASSCOM], "add": {
   2: "<p>For the full career route, read " + gl("become-ai-engineer-after-10th", "how to become an AI engineer after 10th") + ", or " + gl("become-machine-learning-engineer-after-10th", "how to become a machine learning engineer after 10th") + ".</p>",
   3: "<p>Want ideas to try at home first? See these " + gl("python-project-ideas-for-students", "Python project ideas for students") + ".</p>",
   4: "<p>Microsoft lists AI-901 as the exam for its Azure AI Fundamentals certification, with the English version updated in April 2026. AWS describes its AI Practitioner certification as a foundational exam of 65 questions in 90 minutes.</p>"}},
 "courses-after-10th": {"date": "2026-10-18", "sources": [SRC_NASSCOM, SRC_JEE], "add": {
   0: "<p>Nasscom's Strategic Review 2026 puts India's technology industry at about $315 billion in revenue, with employment near 6 million.</p>",
   2: "<p>Each path has a career roadmap: " + gl("become-software-engineer-after-10th", "how to become a software engineer after 10th") + ", " + gl("become-data-scientist-after-10th", "how to become a data scientist after 10th") + " and " + gl("become-ethical-hacker-after-10th", "how to become an ethical hacker after 10th") + ".</p>",
   4: "<p>If B.Tech is the plan, keep Physics and Mathematics in Class 12. The JEE Main 2026 rules require both for B.E. and B.Tech seats at the NITs.</p>"}},
 "computer-coding-courses-after-10th": {"date": "2026-10-18", "sources": [SRC_SO, SRC_AZ900], "add": {
   0: "<p>For the career side, read " + gl("become-software-engineer-after-10th", "how to become a software engineer after 10th") + " or " + gl("become-programmer-after-10th", "how to become a programmer after 10th") + ".</p>",
   2: "<p>In the 2025 Stack Overflow Developer Survey, JavaScript (66%), HTML/CSS (62%) and SQL (59%) were the most-used languages among respondents. All three are in Year 1 of this roadmap.</p>",
   3: "<p>Building websites first? See " + gl("become-web-developer-after-10th", "how to become a web developer after 10th") + ".</p>"}},
 "cyber-security-course-after-10th": {"date": "2026-10-18", "sources": [SRC_ISC2, SRC_SECPLUS, SRC_SC200, SRC_NASSCOM], "add": {
   2: "<p>To see where this leads, read " + gl("become-ethical-hacker-after-10th", "how to become an ethical hacker after 10th") + " and the " + g_prog_link("cybersecurity", "Cybersecurity program") + ".</p>",
   5: "<p>ISC2 lists no work experience requirement for its Certified in Cybersecurity credential. CompTIA expects Security+ V8 on or around 17 November 2026, with more coverage of AI-related risks.</p>"}},
 "data-science-after-10th": {"date": "2026-10-18", "sources": [SRC_GDA, SRC_DP900, SRC_SO], "add": {
   0: "<p>For the career question, read " + gl("become-data-scientist-after-10th", "how to become a data scientist after 10th") + " or " + gl("become-data-analyst-after-10th", "how to become a data analyst after 10th") + ".</p>",
   4: "<p>Google says its Data Analytics Certificate needs no prior experience, only high-school-level maths, and takes about 240 hours. Microsoft rates DP-900 as a beginner-level exam on core data concepts.</p>"}},
 "ai-vs-software-vs-data-science": {"date": "2026-10-18", "sources": [SRC_SO, SRC_NASSCOM], "add": {
   1: "<p>In the 2025 Stack Overflow Developer Survey, Python was the most-used language among people learning to code (72%). It is the main language in both AI/ML Engineering and Data Science &amp; AI.</p>",
   2: "<p>Each path has a step-by-step roadmap: " + gl("become-ai-engineer-after-10th", "how to become an AI engineer after 10th") + ", " + gl("become-software-engineer-after-10th", "how to become a software engineer after 10th") + " and " + gl("become-data-scientist-after-10th", "how to become a data scientist after 10th") + ".</p>"}},
 "ai-projects-for-students": {"date": "2026-10-18", "sources": [SRC_PY, SRC_PCEP], "add": {
   0: "<p>Python's official site describes it as easy for beginners to use and learn. Both AI programs here start with it.</p>",
   5: "<p>For smaller projects to try at home, see these " + gl("python-project-ideas-for-students", "Python project ideas for students") + ". To see where AI projects lead, read " + gl("become-ai-developer-after-10th", "how to become an AI developer after 10th") + ".</p>"}},
 "career-options-after-10th": {"date": "2026-10-18", "sources": [SRC_NASSCOM, SRC_JEE, SRC_NCS], "add": {
   1: "<p>Each path has its own roadmap, for example " + gl("become-software-engineer-after-10th", "how to become a software engineer after 10th") + ", " + gl("become-data-scientist-after-10th", "how to become a data scientist after 10th") + " and " + gl("ui-ux-designer-after-10th", "how to become a UI/UX designer after 10th") + ".</p>",
   2: "<p>The JEE Main 2026 rules require Physics and Mathematics in Class 12 for B.E. and B.Tech seats at the NITs.</p>",
   3: "<p>The Government of India's National Career Service portal, run by the Ministry of Labour &amp; Employment, also lists career counsellors and career information.</p>"}},
}
for _g in GUIDES:
    _x = GUIDE_EXTRA.get(_g["slug"])
    if not _x: continue
    _g["sections"] = [(h, b + _x["add"].get(i, "")) for i, (h, b) in enumerate(_g["sections"])]
    _g["date"], _g["sources"] = _x["date"], _x["sources"]

def g_date_txt(iso):
    import datetime as _d
    return _d.date.fromisoformat(iso).strftime("%-d %B %Y")

def g_sources(g):
    if not g.get("sources"): return ""
    li = "".join(f'<li><a href="{E(u)}" rel="noopener" target="_blank">{E(t)}</a>, {E(n)}</li>' for t, u, n in g["sources"])
    return ('<section class="gd-sec" id="sources"><h2>Sources</h2><p>We checked these sources for the facts on this page. '
            f'Program details come from our own curriculum.</p><ol class="cr-sources">{li}</ol></section>')

GUIDE_BY = {g["slug"]: g for g in GUIDES}
GUIDE_SAL = {"cyber-security-course-after-10th": ["cybersecurity"], "data-science-after-10th": ["data-science-ai"], "ui-ux-designer-after-10th": ["product-ux-ai-design"],
             "computer-coding-courses-after-10th": ["software-development"], "become-ai-engineer-after-10th": ["ai-ml-engineering"],
             "career-options-after-10th": ["ai-ml-engineering", "software-development", "data-science-ai", "product-ux-ai-design", "cybersecurity"],
             "ai-vs-software-vs-data-science": ["ai-ml-engineering", "software-development", "data-science-ai"]}

def g_salary(slugs):
    if len(slugs) == 1:
        b = SALARY[slugs[0]][0]
        lead = f"<p>Entry-level roles in this field typically pay {b[0]} a year in India, rising to {b[2]} with 3–5 years' experience and {b[-1]} at senior level. These are indicative market ranges, not guarantees.</p>"
    else:
        lead = "<p>Indicative starting salaries in India differ by field, and all rise with experience. These are market ranges, not guarantees.</p>"
    rows = "".join(f'<tr><th scope="row">{g_prog_link(x)}</th><td>{SALARY[x][0][0]}</td><td>{SALARY[x][0][2]}</td><td>{SALARY[x][0][-1]}</td></tr>' for x in slugs)
    tbl = ('<div class="gd-table"><table><caption class="vh">Indicative salary in India</caption><thead><tr><th scope="col">Path</th><th scope="col">Fresher</th>'
           '<th scope="col">3–5 years</th><th scope="col">Senior</th></tr></thead><tbody>' + rows + '</tbody></table></div>')
    return lead + tbl + f'<p class="small muted" style="margin-top:12px">{SAL_NOTE}</p>' 
CRUMB["guides"] = "Guides"

def guide_minutes(html):
    return max(3, round(len(re.sub(r"<[^>]+>", " ", html).split()) / 200))

def guide_page(slug):
    g = GUIDE_BY[slug]
    sections = list(g["sections"])
    if slug in GUIDE_SAL: sections.append(("What can you earn in India?", g_salary(GUIDE_SAL[slug])))
    g = dict(g, sections=sections)
    secs = "".join(f'<section class="gd-sec" id="s{i+1}"><h2>{E(h) if "<" not in h else h}</h2>{body}</section>' for i, (h, body) in enumerate(g["sections"]))
    toc = "".join(f'<li><a href="#s{i+1}">{E(h)}</a></li>' for i, (h, _) in enumerate(g["sections"]))
    tldr = "".join(f"<li>{E(x)}</li>" for x in g["tldr"])
    faq = f'<section class="gd-sec" id="faq"><h2>Frequently asked questions</h2><div class="faq gd-faq">{faq_items(g["faqs"], first_open=False)}</div></section>'
    rel = "".join(f'<a class="gd-card" href="/programs/{s}"><small>{prog(s)[4]} · {prog(s)[3]} hours</small><strong>{E(prog(s)[2])}</strong><span>{E(D[s]["summary"])}</span></a>' for s in g["progs"])
    others = "".join(f'<li><a href="/guides/{o["slug"]}">{E(o["title"])}</a></li>' for o in GUIDES if o["slug"] != slug)[:2000]
    mins = guide_minutes(secs + faq)
    hero = f'''<section class="page-hero gd-hero"><div class="wrap"><div><p class="crumbs"><a href="/">Home</a> / <a href="/guides">Guides</a> / {E(g["h1"][0].rstrip(":?"))}</p>
<h1>{headline(E(g["h1"][0]), E(g["h1"][1]))}</h1><p class="lead">{E(g["lead"])}</p>
<p class="gd-meta">By the Neuronetworks AI Ed team · Updated <time datetime="{g.get('date', GUIDE_DATE)}">{g_date_txt(g.get('date', GUIDE_DATE))}</time> · {mins} min read</p></div></div></section>'''
    body = f'''{hero}<div class="wrap gd-wrap"><aside class="gd-toc" aria-label="On this page"><p>On this page</p><ol>{toc}<li><a href="#faq">FAQs</a></li>{'<li><a href="#sources">Sources</a></li>' if g.get("sources") else ""}</ol></aside>
<article class="gd-art"><div class="gd-tldr"><h2>In short</h2><ul>{tldr}</ul></div>{secs}{faq}{g_sources(g)}
<section class="gd-sec"><h2>Programs in this guide</h2><div class="gd-cards">{rel}</div></section>
<section class="gd-sec gd-more"><h2>More guides</h2><ul>{others}</ul></section></article></div>{cta_panel("Questions about the right path?", "Tell us what the student enjoys. We will explain the options, fees and intake dates.")}'''
    ld = {"@type": "Article", "@id": f"{SITE}/guides/{slug}#article", "headline": g["title"], "description": g["desc"], "image": SITE + "/assets/og.png",
          "datePublished": g.get("date", GUIDE_DATE), "dateModified": g.get("date", GUIDE_DATE), "inLanguage": "en-IN", "author": {"@id": ORG_ID}, "publisher": PUBLISHER,
          "mainEntityOfPage": f"{SITE}/guides/{slug}", "about": [{"@id": f"{SITE}/programs/{s}#course"} for s in g["progs"]]}
    return layout(f"/guides/{slug}", g["title"], body, "resources", desc=g["desc"], jsonld=ld)

def guides_index():
    cards = "".join(f'<a class="gd-card gd-card--lg" href="/guides/{g["slug"]}"><strong>{E(g["title"])}</strong><span>{E(g["desc"])}</span><em>Read the guide <i aria-hidden="true">→</i></em></a>' for g in GUIDES)
    hero = page_hero("Guides", "Guides for students", "and parents.", "Plain answers to the questions families ask after Class 10: which tech course, how long it takes, what students build and how to choose.")
    body = hero + f'<section class="sec"><div class="wrap"><div class="gd-grid">{cards}</div></div></section>' + cta_panel()
    ld = {"@type": "CollectionPage", "@id": SITE + "/guides#collection", "name": "Guides", "hasPart": [{"@id": f"{SITE}/guides/{g['slug']}#article"} for g in GUIDES]}
    return layout("/guides", "Guides: AI and tech courses after Class 10", body, "resources", desc="Guides for students and parents: AI, coding, data science, UI/UX and cybersecurity courses after Class 10, explained with real hours and projects.", jsonld=ld)

GUIDE_PAGES = {"/guides": guides_index, **{f"/guides/{g['slug']}": (lambda s=g["slug"]: guide_page(s)) for g in GUIDES}}
