1-Year AI Foundations, Python & AI Applications Program

104 guided hours • 52 weeks • 2 hours/week • 10th-pass entry

Rebuilt teacher-ready curriculum \| 8 months core + 2 months Microsoft AI-901 + 2 months AWS AIF-C01

# 1. Program promise and realistic outcome

This beginner course helps a 10th-pass learner progress from AI literacy to building and evaluating small AI-enabled applications. It includes certification preparation but does not guarantee passing an external exam or qualify the learner as an AI/ML engineer.

- Write, run, debug and explain beginner Python programs; use functions, files, JSON and APIs.

- Clean and summarise a small dataset with Pandas; create basic charts; train and evaluate an introductory scikit-learn model.

- Explain common AI, ML, computer-vision, NLP and generative-AI workloads, their limits and responsible-use requirements.

- Build a small AI API workflow and a basic retrieval-augmented generation (RAG) prototype with evaluation evidence.

- Understand introductory Microsoft Azure AI and AWS AI service choices, security responsibilities, pricing concepts and exam-style scenarios.

- Present a documented portfolio project with a README, architecture, test evidence, limitations and responsible-use notes.

# 2. Entry requirements and learner support

| Item          | Requirement / explanation                                                                                                                                  |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Entry level   | 10th standard passed (or equivalent). No prior coding, AI or cloud experience required.                                                                    |
| Useful basics | Can read simple English instructions, use a browser and manage files/folders; comfortable with school-level arithmetic.                                    |
| Device        | Laptop/desktop with internet, browser and ability to install/use Python or a browser-based notebook. A phone alone is not sufficient for programming labs. |
| Support       | Provide glossary, worked examples, starter code, guided practice, error explanations and catch-up exercises.                                               |
| Time          | 2 guided hours/week. Plan 10–15 minutes of homework after each lecture; this homework is outside the 104 guided hours.                                     |
| Assessment    | Recommended pass mark 80%. Students below threshold receive targeted remediation and a retry.                                                              |
| Safety        | Use fictional, public or anonymised data. Never paste personal, school, client or secret credentials into public AI tools.                                 |

# 3. Structure and hours

| Phase                         | Months | Hours | Focus                                                                                                             |
|-------------------------------|--------|-------|-------------------------------------------------------------------------------------------------------------------|
| Core learning                 | 1–8    | 64    | AI basics, Python/data, ML, vision/NLP, GenAI, prompt evaluation, RAG and application foundations.                |
| Microsoft certification block | 9–10   | 20    | AI-901 objective coverage, Azure/Microsoft Foundry implementation concepts, labs, timed practice and remediation. |
| AWS certification block       | 11–12  | 20    | AIF-C01 domain coverage, AWS service recognition, scenarios, mock exams and remediation.                          |
| Total                         |        | 104   | 104 one-hour lectures; no assessment hours added outside the total.                                               |

The core phase deliberately allocates 20 hours to Python and data programming in Months 3–4. Python is then reinforced through ML, API, RAG and application exercises. This is a beginner applied-AI foundation, not a full software engineering course.

# 4. One-hour teaching pattern

| Minutes | Teaching activity                                                              |
|---------|--------------------------------------------------------------------------------|
| 0–3     | Set a concrete problem and explain why it matters.                             |
| 3–15    | Teach the first concept in plain language, then introduce precise vocabulary.  |
| 15–23   | Walk through a worked example, diagram or code snippet.                        |
| 23–28   | Scenario MCQ 1; learners choose and justify an answer.                         |
| 28–40   | Teach the second concept or extend the example; correct common misconceptions. |
| 40–45   | Scenario MCQ 2; compare distractors and explain why they are wrong.            |
| 45–55   | Guided practice: students perform a task and inspect the result.               |
| 55–60   | Exit check: learner explains the result, limitation or next debugging step.    |

Each lecture below has its own explanation, worked example, two non-identical MCQs with varying answer positions, exercise and homework. The time pattern stays consistent; the actual teaching content changes by topic.

# 5. Detailed lecture-by-lecture curriculum

## Month 1 — AI Foundations & How Modern AI Works

Allocation: 4 hours \| 4 lectures. All lecture time is included in the 104-hour total.

### Lecture 1 — AI around us: identify a task, not just a product

Learning outcome: Distinguish AI-enabled tasks from ordinary digital features.

Teacher explanation: AI is a way to make a computer perform tasks that usually require capabilities such as recognising patterns, interpreting language or generating content. A product may combine AI with ordinary rules; do not label every digital feature as AI.

Worked example / demonstration: Classify four examples: calculator arithmetic (usually rules), photo face grouping (pattern recognition), spam filtering (classification), and a fixed alarm (rule-based). Explain the evidence for each label.

Guided exercise: Create a two-column audit of five familiar apps: likely AI task and evidence you would need to confirm it.

Scenario MCQ 1: A shop app sorts orders by a fixed date rule. What is the safest initial classification?

- A. It must be generative AI

- B. It may be ordinary rule-based software

- C. It is necessarily deep learning

- D. It is an autonomous agent

Correct answer: B. A fixed rule can work without a learned model; inspect the mechanism before labelling it AI.

Scenario MCQ 2: A photo app groups similar faces. Which capability is most relevant?

- A. Spreadsheet formulas

- B. Network routing

- C. Pattern recognition / computer vision

- D. Text translation

Correct answer: C. Grouping faces relies on visual patterns, though the exact implementation can vary.

Specific homework (10–15 minutes, outside guided hours): Ask an adult about one repeated task at home or in a small business; describe whether AI would help and what could go wrong.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 2 — AI, machine learning, deep learning and generative AI

Learning outcome: Explain how the terms relate without treating them as synonyms.

Teacher explanation: AI is the broad field. Machine learning is one approach in which a system learns patterns from examples. Deep learning uses multi-layer neural networks. Generative AI creates new content such as text, images or audio; not all AI is generative.

Worked example / demonstration: Draw nested circles: AI contains ML; deep learning is a type of ML; many modern generative systems use deep learning. Place a spam classifier and a text generator in the diagram.

Guided exercise: Give learners six use cases and ask them to select the narrowest accurate term, then defend one borderline case.

Scenario MCQ 1: Which statement is most accurate?

- A. Every AI system is a large language model

- B. Machine learning is one approach within AI

- C. Generative AI and AI mean exactly the same thing

- D. Deep learning never uses data

Correct answer: B. ML is a subset of AI; the other options overgeneralise or are false.

Scenario MCQ 2: A model writes a new product description from a prompt. What capability is central?

- A. Generative AI

- B. A fixed sorting rule

- C. Disk compression

- D. A database index

Correct answer: A. The system generates new text rather than only retrieving or sorting records.

Specific homework (10–15 minutes, outside guided hours): Explain the four terms to a family member using one example for each.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 3 — How an AI model learns and makes a prediction

Learning outcome: Describe training, inference, output and uncertainty.

Teacher explanation: Training adjusts a model using examples; inference is the later use of that model to produce an output. Outputs are not guaranteed truths. Data quality, task framing and conditions outside training examples affect reliability.

Worked example / demonstration: Use a toy classifier with labelled fruit examples. Show examples used to learn, then present a new fruit description and ask for a prediction. Discuss confidence versus correctness.

Guided exercise: Learners label five training examples and test the model conceptually on one unusual example; record why it may fail.

Scenario MCQ 1: What happens during inference?

- A. The model is always retrained from scratch

- B. The model is used to produce an output for an input

- C. The dataset is automatically proven unbiased

- D. The computer is disconnected from data

Correct answer: B. Inference is the use of a trained model to generate a result.

Scenario MCQ 2: A model gives a confident but incorrect answer. What should the user conclude?

- A. Confidence proves truth

- B. The model has no limitations

- C. The output needs verification for the task's risk level

- D. The training data must be public

Correct answer: C. Confidence is not proof; use verification proportionate to the risk.

Specific homework (10–15 minutes, outside guided hours): Write a short 'AI can / AI cannot guarantee' note with one prediction example.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 4 — Traditional software versus AI: choose the right approach

Learning outcome: Choose between explicit rules, a learned model and human review.

Teacher explanation: Traditional programs are often best when rules are clear and stable. AI is useful when patterns are difficult to express as rules, but it introduces uncertainty and needs evaluation. Many useful systems combine rules, AI and human approval.

Worked example / demonstration: For invoice processing, use rules for required fields and totals, OCR for extracting text, and a person for high-value exceptions. Sketch the hand-offs.

Guided exercise: Teams choose a method for three cases: tax calculation, customer email categorisation and approving a large refund. Explain the cost of a wrong result.

Scenario MCQ 1: Which task is usually best handled by explicit deterministic code?

- A. Writing a creative story

- B. Recognising emotion in every voice perfectly

- C. Calculating an invoice total from known numeric fields

- D. Predicting an ambiguous future trend

Correct answer: C. Exact arithmetic over known fields should be deterministic and testable.

Scenario MCQ 2: A system recommends a refund amount. What is a safer design for high-value refunds?

- A. Automatically pay every recommendation

- B. Use AI support plus rules and human approval

- C. Remove all logs

- D. Hide the uncertainty

Correct answer: B. Risk-based controls reduce the harm from a wrong recommendation.

Specific homework (10–15 minutes, outside guided hours): Write a one-page AI opportunity audit for a school or small shop, including one reason not to use AI.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 2 — AI Tools, Safety, Ethics & Responsible AI

Allocation: 4 hours \| 4 lectures. All lecture time is included in the 104-hour total.

### Lecture 5 — AI assistants: useful instructions and verification

Learning outcome: Use an assistant with a clear task, context, format and verification step.

Teacher explanation: An AI assistant responds to instructions and context. A useful request says what to do, for whom, with what information, and in what format. The response still needs checking, especially facts, calculations and consequential advice.

Worked example / demonstration: Prompt: 'Turn these teacher-provided notes into a 5-bullet revision sheet for a 10th-standard learner. Use only the notes; mark missing information as unknown.' Compare with 'Explain this'.

Guided exercise: Rewrite a vague request into task + context + constraints + output format + check.

Scenario MCQ 1: Which prompt is most likely to produce a usable result?

- A. Tell me everything

- B. Do it well

- C. Summarise the supplied notes in five bullets for a beginner; do not add facts

- D. Write something

Correct answer: C. It specifies source, audience, format and a constraint.

Scenario MCQ 2: An assistant states a new legal rule without a source. What is the best next step?

- A. Repeat the claim until it sounds convincing

- B. Verify it with an authoritative current source

- C. Assume the fluent wording proves accuracy

- D. Share it publicly immediately

Correct answer: B. Fluency does not establish factual correctness.

Specific homework (10–15 minutes, outside guided hours): Keep a prompt diary: prompt, what improved, what remained unreliable.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 6 — Privacy, security and safe data handling

Learning outcome: Recognise sensitive data and avoid exposing secrets to AI tools.

Teacher explanation: Prompts and uploaded files may contain personal, confidential or regulated information. Follow the organisation's approved tools and data rules. API keys are credentials, not ordinary text; never publish them in code or a screenshot.

Worked example / demonstration: Replace names, phone numbers and student IDs with fictional placeholders before making a sample summarisation prompt. Show a fake API key stored in an environment variable rather than pasted into source code.

Guided exercise: Identify sensitive fields in a mock student spreadsheet and produce a minimised, anonymised version.

Scenario MCQ 1: A student wants help summarising real classmates' medical notes. What should they do?

- A. Upload them to any free chatbot

- B. Remove names only and ignore all other policy

- C. Use approved handling rules and avoid uploading sensitive records without authorisation

- D. Post them in a public forum

Correct answer: C. Sensitive data needs authorised handling and minimisation, not casual upload.

Scenario MCQ 2: Where should a production API key normally be stored?

- A. In a public GitHub repository

- B. In a protected secret/environment configuration

- C. Inside a screenshot

- D. In a prompt sent to a public model

Correct answer: B. Secrets should be kept out of source control and public prompts.

Specific homework (10–15 minutes, outside guided hours): Create a personal checklist: what never to paste into a public AI service and where to report accidental disclosure.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 7 — Bias, hallucination and responsible AI

Learning outcome: Identify common failure modes and choose proportionate safeguards.

Teacher explanation: AI can reproduce skewed patterns, invent unsupported details or behave inconsistently across groups. Responsible use includes testing representative cases, checking sources, monitoring failures and involving people when decisions affect rights or safety.

Worked example / demonstration: Compare two fictional loan-assistance outputs for similar applicants. Ask which fields may create unfairness and what evidence would be needed before deployment.

Guided exercise: Design five test cases for a school FAQ bot, including ambiguous, out-of-scope and sensitive questions.

Scenario MCQ 1: A hiring model performs worse for one group. What is the most responsible response?

- A. Deploy because average accuracy is high

- B. Investigate data and subgroup performance before use

- C. Hide subgroup results

- D. Assume the difference is harmless

Correct answer: B. Average performance can conceal uneven harm.

Scenario MCQ 2: A chatbot invents a school policy. Which control directly helps?

- A. Increase the font size

- B. Use approved source documents, citations where possible and verification

- C. Remove the test set

- D. Ask it to sound confident

Correct answer: B. Grounding and verification target unsupported answers.

Specific homework (10–15 minutes, outside guided hours): Write three limitations for an AI tool you use and one safeguard for each.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 8 — Responsible AI audit workshop

Learning outcome: Apply a simple risk audit before recommending an AI tool.

Teacher explanation: An AI audit asks what problem is being solved, what data is used, who can be harmed, how performance is checked, who reviews failures and how people can appeal. A tool should not be used merely because it is novel.

Worked example / demonstration: Complete an audit for an AI study assistant: purpose, data, error consequences, test cases, human oversight and stop conditions.

Guided exercise: Teams audit a fictional school chatbot and present a go / limited pilot / no-go recommendation with reasons.

Scenario MCQ 1: Which is the strongest pre-deployment test plan?

- A. Test only easy examples

- B. Test typical, edge, harmful and subgroup cases with documented criteria

- C. Ask the vendor if it works

- D. Skip monitoring after launch

Correct answer: B. Representative and adversarial cases plus criteria reveal failure modes.

Scenario MCQ 2: A tool processes sensitive records but has no clear retention policy. What is the best decision?

- A. Proceed and hope

- B. Pause until approved data handling and retention are clear

- C. Upload more data to test it

- D. Delete the policy question

Correct answer: B. Data handling uncertainty is a launch blocker for sensitive data.

Specific homework (10–15 minutes, outside guided hours): Complete the audit for one proposed AI use case and name the evidence still missing.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 3 — Python Programming Fundamentals I

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 9 — Python setup, notebooks and the first program

Learning outcome: Run a Python program and interpret its output

Teacher explanation: Python executes instructions in order. A notebook is useful for short experiments; a script is useful for reusable work. Errors are clues: read the message and inspect the line rather than randomly changing code.

Worked example / demonstration: print('Hello, Neuromind!') then print(2 + 3). Explain output order and the difference between text in quotes and a numeric expression.

Guided exercise: Run two print statements, intentionally remove a quote, read the error, fix it and rerun.

Scenario MCQ 1: A beginner is working on 'python setup, notebooks and the first program'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for python setup, notebooks and the first program, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'python setup, notebooks and the first program'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Submit a screenshot or notebook with three outputs and one error you diagnosed.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 10 — Variables, types and conversion

Learning outcome: Store values and distinguish strings, integers, floats and booleans

Teacher explanation: A variable is a label pointing to a value. The type affects which operations make sense. Input from a user is usually text, so convert it before arithmetic.

Worked example / demonstration: age_text = '16'; age = int(age_text); print(age + 1). Contrast '16' + '1' with 16 + 1.

Guided exercise: Write a program storing learner name, age and enrolled status; print a readable summary.

Scenario MCQ 1: A beginner is working on 'variables, types and conversion'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for variables, types and conversion, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'variables, types and conversion'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Add a conversion check and explain one type error in your own words.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 11 — Operators and expressions

Learning outcome: Evaluate arithmetic, comparison and logical expressions

Teacher explanation: Operators transform values or compare them. Parentheses make intent clear. Boolean expressions power conditions, filters and validation.

Worked example / demonstration: score = 82; passed = score \>= 80; print(passed). Show why 82 \>= '80' is a type mismatch.

Guided exercise: Create a fee discount calculation and a Boolean eligibility rule using fictional values.

Scenario MCQ 1: A beginner is working on 'operators and expressions'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for operators and expressions, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'operators and expressions'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Test boundary values below, at and above a threshold.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 12 — Conditions and decision-making

Learning outcome: Use if/elif/else to implement a rule

Teacher explanation: Conditions choose a path. Check boundaries and mutually exclusive cases; an else branch catches remaining cases but should not conceal invalid input.

Worked example / demonstration: score = 76; if score \>= 80: result='Pass'; else: result='Retry'. Discuss the policy meaning of the threshold.

Guided exercise: Classify a fictional order as small, medium or large using clearly stated thresholds.

Scenario MCQ 1: A beginner is working on 'conditions and decision-making'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for conditions and decision-making, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'conditions and decision-making'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Add tests for the exact threshold and one invalid value.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 13 — Loops and repeated work

Learning outcome: Use for and while loops safely

Teacher explanation: Loops avoid duplicated code. A for loop is natural when iterating through a collection; a while loop repeats while a condition remains true. Every while loop needs a path to stop.

Worked example / demonstration: for score in \[70, 85, 91\]: print(score). Add a running total and explain each iteration.

Guided exercise: Calculate total and average for five sample quiz scores.

Scenario MCQ 1: A beginner is working on 'loops and repeated work'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for loops and repeated work, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'loops and repeated work'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Trace a loop by hand and include the final value of the accumulator.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 14 — Strings and text cleaning

Learning outcome: Use string operations to normalise text

Teacher explanation: Strings are sequences of characters. strip removes surrounding whitespace, lower standardises case and split separates text. Normalisation helps matching but can remove meaningful distinctions if used carelessly.

Worked example / demonstration: email = ' STUDENT@EXAMPLE.COM '; clean = email.strip().lower(); print(clean).

Guided exercise: Clean a list of fictional names and email addresses; preserve original data separately.

Scenario MCQ 1: A beginner is working on 'strings and text cleaning'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for strings and text cleaning, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'strings and text cleaning'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Provide before/after examples and explain why cleaning rules should be documented.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 15 — Lists and tuples

Learning outcome: Store ordered collections and access elements

Teacher explanation: Lists are mutable ordered collections; tuples are commonly used for fixed grouped values. Indexes start at zero. Check list length before indexing.

Worked example / demonstration: scores=\[72,88,91\]; print(scores\[0\]); scores.append(95). Explain index 0 and append.

Guided exercise: Build a shopping list and compute the number of items; handle an empty list.

Scenario MCQ 1: A beginner is working on 'lists and tuples'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for lists and tuples, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'lists and tuples'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Write a short program that finds the highest value and explain how it handles ties.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 16 — Dictionaries and sets

Learning outcome: Represent key-value records and unique items

Teacher explanation: A dictionary maps keys to values, making records readable. A set stores unique values and is useful for de-duplication. Missing keys require a deliberate strategy.

Worked example / demonstration: student={'name':'Asha','score':88}; print(student.get('score')); unique_subjects=set(\['AI','Python','AI'\]).

Guided exercise: Represent a fictional product record and count unique category names.

Scenario MCQ 1: A beginner is working on 'dictionaries and sets'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for dictionaries and sets, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'dictionaries and sets'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Add a safe lookup for a missing key and describe the returned value.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 17 — Functions and parameters

Learning outcome: Create reusable functions with clear inputs and outputs

Teacher explanation: A function names a task, accepts parameters and can return a result. Functions make testing easier when one job is performed per function.

Worked example / demonstration: def total_with_tax(price, rate): return price \* (1 + rate). Test with a small fictional price.

Guided exercise: Write a function that converts minutes to hours and minutes; test normal and boundary inputs.

Scenario MCQ 1: A beginner is working on 'functions and parameters'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for functions and parameters, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'functions and parameters'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Submit function, three tests and a sentence explaining its contract.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 18 — Debugging and programming challenge

Learning outcome: Use a repeatable debugging process

Teacher explanation: Reproduce the error, read the traceback, isolate the smallest failing example, inspect types/values, fix one cause and retest. Guessing can create hidden regressions.

Worked example / demonstration: Demonstrate a TypeError caused by adding a string to an integer; print(type(value)) and convert intentionally.

Guided exercise: Repair a supplied program with two bugs; record the symptom, cause and fix for each.

Scenario MCQ 1: A beginner is working on 'debugging and programming challenge'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for debugging and programming challenge, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'debugging and programming challenge'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Create a debugging log for one issue, including the final regression test.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 4 — Python Programming Fundamentals II & Data Science

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 19 — Functions, scope and modules

Learning outcome: Organise a small program into reusable pieces

Teacher explanation: Local variables belong to a function call; global state makes behaviour harder to reason about. Modules group related code and can be imported rather than copied.

Worked example / demonstration: Move a currency-formatting function into helpers.py and import it from main.py.

Guided exercise: Split a 30-line script into two modules with one clear responsibility each.

Scenario MCQ 1: A beginner is working on 'functions, scope and modules'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for functions, scope and modules, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'functions, scope and modules'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Explain one benefit and one risk of global variables.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 20 — Files, paths and exceptions

Learning outcome: Read/write files and handle expected failures

Teacher explanation: Files let a program preserve results. Use context managers so files close reliably. Exceptions should be handled narrowly; do not silently discard all errors.

Worked example / demonstration: with open('notes.txt','w',encoding='utf-8') as f: f.write('practice'). Add try/except for a missing input file.

Guided exercise: Read a provided text file, count lines and show a friendly message when it is absent.

Scenario MCQ 1: A beginner is working on 'files, paths and exceptions'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for files, paths and exceptions, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'files, paths and exceptions'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Test the missing-file case and include the exact user-facing message.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 21 — JSON and structured data

Learning outcome: Parse and serialise JSON safely

Teacher explanation: JSON represents structured data exchanged between programs. A JSON object maps naturally to a Python dictionary; arrays map to lists. Validate required keys before using them.

Worked example / demonstration: import json; record=json.loads('{"name":"Mira","score":90}'); print(record\['score'\]).

Guided exercise: Load a fictional JSON product record, validate two fields and write a changed copy.

Scenario MCQ 1: A beginner is working on 'json and structured data'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for json and structured data, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'json and structured data'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Include a valid and invalid JSON example and explain how the program responds.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 22 — Basic object-oriented programming

Learning outcome: Explain classes, objects, attributes and methods

Teacher explanation: A class describes a kind of object; an instance stores its own state. Use a class when related data and behaviour naturally belong together, not simply to make code look advanced.

Worked example / demonstration: Create a Book class with title and a describe() method; instantiate one book.

Guided exercise: Model a library book or product with two attributes and one method.

Scenario MCQ 1: A beginner is working on 'basic object-oriented programming'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for basic object-oriented programming, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'basic object-oriented programming'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Explain the class-instance difference using your own example.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 23 — HTTP, REST and requests

Learning outcome: Describe request/response and call a simple API

Teacher explanation: An HTTP request has a method, URL, headers and sometimes a body. The response has a status code and content. Handle timeouts, errors and external service limits.

Worked example / demonstration: Use requests.get against a documented public demo endpoint with timeout=10; inspect status_code before json().

Guided exercise: Call a safe public demo API or instructor mock endpoint and display two fields.

Scenario MCQ 1: A beginner is working on 'http, rest and requests'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for http, rest and requests, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'http, rest and requests'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Document the endpoint, status code, timeout behaviour and one possible failure.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 24 — NumPy fundamentals

Learning outcome: Use arrays for simple numerical operations

Teacher explanation: NumPy arrays support efficient numerical operations. For this course, learners need to create arrays, inspect shape and perform simple elementwise calculations—not advanced numerical methods.

Worked example / demonstration: import numpy as np; scores=np.array(\[70,80,90\]); print(scores.mean()).

Guided exercise: Compare average and maximum of a small fictional score array.

Scenario MCQ 1: A beginner is working on 'numpy fundamentals'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for numpy fundamentals, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'numpy fundamentals'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Show array shape and calculate mean; explain what each output means.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 25 — Pandas and data cleaning

Learning outcome: Load, inspect, clean and summarise tabular data

Teacher explanation: A DataFrame is a table with labelled rows and columns. Inspect first; identify missing values, duplicates and types; clean deliberately; preserve raw data and document assumptions.

Worked example / demonstration: import pandas as pd; df=pd.read_csv('sales.csv'); print(df.head()); print(df.isna().sum()).

Guided exercise: Load an instructor-provided fictional CSV, clean missing categories and calculate totals by category.

Scenario MCQ 1: A beginner is working on 'pandas and data cleaning'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for pandas and data cleaning, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'pandas and data cleaning'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Submit raw/cleaned comparison, missing-value decisions and a brief data-quality note.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 26 — Charts and interpreting data

Learning outcome: Choose a chart that answers a question

Teacher explanation: Charts make patterns visible but can mislead through scale, labels or selective data. Match chart type to the question and explain the unit, population and limitations.

Worked example / demonstration: Plot monthly sales as a line chart and category totals as a bar chart; label axes and title.

Guided exercise: Produce two charts from a fictional business CSV and write two observations plus one caveat.

Scenario MCQ 1: A beginner is working on 'charts and interpreting data'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for charts and interpreting data, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'charts and interpreting data'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Upload chart images and the code; state what the chart cannot establish.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 27 — Git and GitHub portfolio basics

Learning outcome: Track changes and publish a safe project repository

Teacher explanation: Git records versions; GitHub hosts repositories. A useful README tells a reader what the project does, how to run it, what data it uses and what its limitations are. Never commit secrets or private data.

Worked example / demonstration: Create README.md with objective, setup, example output and limitations; inspect files before commit.

Guided exercise: Create a repository for the Month 4 data workflow using fictional data only.

Scenario MCQ 1: A beginner is working on 'git and github portfolio basics'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for git and github portfolio basics, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'git and github portfolio basics'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Add a README and verify the repository contains no credentials or personal records.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 28 — Python/data practical assessment

Learning outcome: Complete a small data workflow independently

Teacher explanation: A reliable workflow is: load, inspect, clean, summarise, visualise, save and explain. The goal is not to produce a chart at any cost; it is to make defensible decisions and communicate them.

Worked example / demonstration: Demonstrate a tiny CSV pipeline from pd.read_csv through isna(), groupby(), plot and to_csv.

Guided exercise: Practical rubric: load file; inspect shape/types; identify missing values; clean; calculate summaries; create two charts; write a function; save results; explain findings; publish README. Pass target 80%.

Scenario MCQ 1: A beginner is working on 'python/data practical assessment'. Which approach best matches the lesson?

- A. Ignore the output and continue

- B. Use the demonstrated concept, inspect the result and test a boundary case

- C. Copy code without understanding

- D. Remove all error handling

Correct answer: B. The lesson focuses on a repeatable, testable workflow for python/data practical assessment, not blind copying.

Scenario MCQ 2: Why should the learner test an edge case while practising 'python/data practical assessment'?

- A. Edge cases are never important

- B. To make the program longer

- C. To reveal assumptions and failure modes before relying on the result

- D. To guarantee that every possible input works

Correct answer: C. A small number of targeted tests exposes boundary problems, although no small test set proves perfection.

Specific homework (10–15 minutes, outside guided hours): Finish corrections from assessor feedback and resubmit the repository.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 5 — Machine Learning Fundamentals with Python

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 29 — What machine learning is and when to use it

Learning outcome: Separate prediction problems from rule-based tasks

Teacher explanation: ML learns patterns from examples and applies them to new inputs. It is appropriate when examples exist and the output can be evaluated; it is not automatically the best choice for exact rules or tiny datasets.

Worked example / demonstration: Compare fixed tax calculation with predicting product demand. Identify inputs, output and cost of error.

Guided exercise: For three fictional business problems, choose rules, ML or human review and justify each.

Scenario MCQ 1: In 'what machine learning is and when to use it', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'what machine learning is and when to use it'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Write one suitable and one unsuitable ML use case.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 30 — Datasets, rows, features and labels

Learning outcome: Identify records, features and target labels

Teacher explanation: Rows usually represent examples; columns represent attributes. A feature is an input signal; the label/target is what the model is asked to predict. Leakage occurs when a feature reveals the answer improperly.

Worked example / demonstration: Student performance dataset: attendance and practice attempts as features, pass outcome as target; exclude final exam score if predicting before exam.

Guided exercise: Mark features and target in a small instructor dataset and identify a possible leakage column.

Scenario MCQ 1: In 'datasets, rows, features and labels', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'datasets, rows, features and labels'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Explain why the target must not be included as an input feature.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 31 — Data preparation and train/test split

Learning outcome: Prepare data and keep an honest test set

Teacher explanation: A model should be evaluated on examples it did not train on. Cleaning and splitting choices must avoid leakage. For small beginner exercises, use a simple train/test split and explain that results vary.

Worked example / demonstration: Use train_test_split(X,y,test_size=0.2,random_state=42); fit preprocessing only on training data when relevant.

Guided exercise: Split a fictional dataset, inspect class balance and write down the target before training.

Scenario MCQ 1: In 'data preparation and train/test split', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'data preparation and train/test split'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Explain why testing only on training rows gives an overly optimistic estimate.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 32 — Regression

Learning outcome: Train a model that predicts a numeric value

Teacher explanation: Regression predicts a number, such as demand or price. Evaluate error size and compare against a simple baseline. A correlation in the data does not prove that a feature causes the outcome.

Worked example / demonstration: Fit LinearRegression to a tiny prepared dataset and compare predictions with actual values; calculate MAE.

Guided exercise: Predict fictional weekly sales and discuss why extrapolating far beyond the observed range is risky.

Scenario MCQ 1: In 'regression', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'regression'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Report MAE and one limitation of the data or model.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 33 — Classification

Learning outcome: Predict a category and interpret errors

Teacher explanation: Classification predicts a class such as pass/fail or spam/not spam. Accuracy can be misleading with imbalanced data; false positives and false negatives have different consequences.

Worked example / demonstration: Use LogisticRegression or a decision tree for a fictional binary label; inspect confusion matrix.

Guided exercise: Train a simple classifier and explain one false positive and one false negative.

Scenario MCQ 1: In 'classification', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'classification'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Write which error matters more for your use case and why.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 34 — Clustering

Learning outcome: Group similar records without known labels

Teacher explanation: Clustering looks for structure without a supplied target. The resulting groups are not automatically meaningful categories; inspect their characteristics and avoid assigning human meaning without evidence.

Worked example / demonstration: Use KMeans on scaled fictional purchase-frequency and spend features; describe cluster centres cautiously.

Guided exercise: Cluster a small synthetic customer dataset and label groups based on observed features, not assumptions.

Scenario MCQ 1: In 'clustering', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'clustering'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Describe one useful interpretation and one risk of over-interpreting clusters.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 35 — Evaluation metrics

Learning outcome: Choose a metric aligned to the cost of error

Teacher explanation: Regression metrics measure numeric error; classification metrics include precision, recall and F1. Choose metrics according to the question and error costs; never report a number without describing the evaluation data.

Worked example / demonstration: Show a confusion matrix for a disease-screening toy example and discuss why recall may matter, while warning that real clinical use needs expert validation.

Guided exercise: Select a metric for spam filtering versus fraud flagging and defend the choice.

Scenario MCQ 1: In 'evaluation metrics', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'evaluation metrics'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Explain why 95% accuracy could still be poor on a dataset with 99% negatives.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 36 — Overfitting and generalisation

Learning outcome: Recognise a model that memorises training data

Teacher explanation: Overfitting occurs when a model performs well on training examples but poorly on unseen examples. More complexity is not always better; more representative data, simpler models and sound validation can help.

Worked example / demonstration: Compare train and test scores for a shallow and deep decision tree on a small dataset.

Guided exercise: Inspect two model score pairs and recommend the more generalisable one with evidence.

Scenario MCQ 1: In 'overfitting and generalisation', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'overfitting and generalisation'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Write a short note distinguishing underfitting from overfitting.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 37 — Scikit-learn end-to-end workflow

Learning outcome: Build a simple repeatable ML pipeline

Teacher explanation: A basic workflow defines target, separates data, chooses a model, fits on training data, predicts on test data and evaluates. Record the random seed and limitations so results can be reproduced.

Worked example / demonstration: Use train_test_split, DecisionTreeClassifier, fit, predict and classification_report on a fictional CSV.

Guided exercise: Complete a guided classifier notebook and explain every major line.

Scenario MCQ 1: In 'scikit-learn end-to-end workflow', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'scikit-learn end-to-end workflow'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Submit code plus a plain-language summary of the evaluation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 38 — ML mini-project and practical assessment

Learning outcome: Train, evaluate and communicate a simple model

Teacher explanation: A project is not finished when code runs. Explain the problem, data source, features, target, split, metric, limitations and what decision the model should not make alone.

Worked example / demonstration: Student Performance Predictor using fictional/anonymised data; compare a simple baseline with one model; disclose that it is educational only.

Guided exercise: Independent assessment: inspect data, prepare features, split, train, evaluate, interpret error and present limitations. Target 80%.

Scenario MCQ 1: In 'ml mini-project and practical assessment', what is the best practice?

- A. Choose the most complicated model by default

- B. Use a method aligned to the target, data and evaluation goal

- C. Report only the best-looking score

- D. Ignore data quality

Correct answer: B. Model and metric choices should follow the problem and evidence.

Scenario MCQ 2: A learner gets a result for 'ml mini-project and practical assessment'. What should they do before making a real-world claim?

- A. State the model is always correct

- B. Hide the data source

- C. Check assumptions, evaluation evidence and limitations

- D. Use the result as proof of causation

Correct answer: C. A responsible claim requires context and limitations, not just a model output.

Specific homework (10–15 minutes, outside guided hours): Revise the README and add evidence of evaluation and limitations.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 6 — Computer Vision, NLP & Multimodal AI

Allocation: 8 hours \| 8 lectures. All lecture time is included in the 104-hour total.

### Lecture 39 — Computer vision workloads

Learning outcome: Match image tasks to appropriate capabilities

Teacher explanation: Computer vision systems process images or video. Image classification assigns a label to an image; object detection locates objects; OCR extracts text. The task definition matters more than the brand name.

Worked example / demonstration: For a warehouse photo, choose classification for 'contains a helmet?', detection for bounding boxes, and OCR for reading a label.

Guided exercise: Match six image problems to classification, detection, OCR or human inspection.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Explain one reason an OCR result needs validation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 40 — Image classification, object detection and OCR

Learning outcome: Compare outputs and common failure cases

Teacher explanation: These tasks return different outputs: labels, boxes or extracted text. Lighting, blur, occlusion and unusual layouts can reduce quality. Never assume one vision service performs all tasks equally well.

Worked example / demonstration: Use a small labelled image set or approved demo; inspect prediction confidence and errors across clear and blurry images.

Guided exercise: Design a test set with normal, low-light and partially obscured images.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Record two failure cases and one mitigation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 41 — NLP fundamentals

Learning outcome: Identify common text-processing tasks

Teacher explanation: NLP works with human language. Tasks include sentiment, classification, entity extraction, summarisation and translation. Language, slang, context and cultural differences affect performance.

Worked example / demonstration: For a customer review, identify sentiment, product entity and complaint category as separate possible outputs.

Guided exercise: Annotate ten fictional reviews for sentiment and product issue; compare with an AI suggestion.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Write where a sentiment label may misread sarcasm.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 42 — Text classification and information extraction

Learning outcome: Distinguish assigning a label from extracting fields

Teacher explanation: Classification chooses a category; extraction identifies specific spans or values. Validate extracted information against source text and avoid inferring facts that are not present.

Worked example / demonstration: Turn a fictional support email into category='delivery' and order_id='A123' only if the identifier appears in the text.

Guided exercise: Build a small extraction table from fictional messages and mark missing fields as unknown.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Add two examples where the system should return 'not found'.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 43 — Speech and language services

Learning outcome: Choose transcription, translation or speech generation

Teacher explanation: Speech-to-text transcribes audio; translation changes language; text-to-speech produces audio. Audio quality, accent and domain terms affect performance; transcripts need review in high-stakes settings.

Worked example / demonstration: Map a classroom recording use case to transcription, then show how translating the transcript is a separate stage.

Guided exercise: Create a flow diagram for a multilingual help desk and mark consent/privacy risks.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): List three checks before publishing an automated transcript.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 44 — Multimodal AI

Learning outcome: Explain systems that process more than one modality

Teacher explanation: Multimodal systems may accept or produce combinations of text, images, audio and video. The model may miss visual details or infer incorrectly; specify what evidence supports each answer.

Worked example / demonstration: Ask a vision-language system about a supplied non-sensitive image, then verify its claims directly against visible evidence.

Guided exercise: Write three questions about an image and separate observable facts from guesses.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Document one incorrect or unsupported image interpretation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 45 — Choosing an AI workload and service

Learning outcome: Map a user problem to a capability and a test

Teacher explanation: Start from the required output and risk. OCR, classification, language generation and retrieval are different capabilities. Choose a managed service when it fits, and compare quality, cost, latency, privacy and operational effort.

Worked example / demonstration: A shop wants to digitise receipts: OCR extracts text; validation rules check totals; a person reviews low-confidence records.

Guided exercise: Create a decision matrix for three use cases with capability, test, risk and human fallback.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Add one reason to build less and reuse a proven service.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 46 — Vision/NLP mini-lab and assessment

Learning outcome: Evaluate a small vision or language task

Teacher explanation: A useful mini-lab states the task, test examples, expected output, observed errors and limits. The assessment rewards the reasoning and validation, not merely obtaining an API response.

Worked example / demonstration: Run an approved demo on synthetic/public examples and save input/output pairs with a simple error log.

Guided exercise: Submit a one-page evaluation with at least five examples, error analysis and responsible-use note.

Scenario MCQ 1: A team is selecting an AI capability. Which decision is strongest?

- A. Choose a product before defining the output

- B. Map the required output to the task and test realistic examples

- C. Assume all AI services do the same job

- D. Skip privacy review

Correct answer: B. A precise task and representative evaluation reduce mismatched solutions.

Scenario MCQ 2: An AI output contains a detail not supported by the image or text. What should the learner do?

- A. Treat it as a fact

- B. Remove the source material

- C. Mark it unsupported and verify against the evidence

- D. Increase the confidence label

Correct answer: C. The output must be checked against available evidence.

Specific homework (10–15 minutes, outside guided hours): Fix one weakness identified in the evaluation and document the change.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 7 — Generative AI, LLMs & Foundation Models

Allocation: 8 hours \| 8 lectures. All lecture time is included in the 104-hour total.

### Lecture 47 — Generative AI and use-case selection

Learning outcome: Explain what generative models produce and where they fit

Teacher explanation: Generative models create outputs based on learned patterns. They are useful for drafts, summaries and transformations but can fabricate details. Use deterministic code for exact calculations and retrieval when the source must be authoritative.

Worked example / demonstration: Compare generating a marketing draft, calculating tax and answering a policy question from a supplied document; choose a different approach for each.

Guided exercise: Classify eight business tasks as generative, predictive, retrieval, rules or human-led.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Write a build-versus-buy recommendation for one small task.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 48 — How LLMs work at a conceptual level

Learning outcome: Describe token prediction without claiming human understanding

Teacher explanation: A large language model processes tokens and predicts likely continuations based on learned patterns and context. It can be useful without having reliable factual grounding; outputs vary with prompt and settings.

Worked example / demonstration: Show a sentence with several possible continuations and explain that model output is generated, not looked up as a guaranteed fact.

Guided exercise: Create a diagram from prompt to tokens/model inference to generated response and verification.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Explain why a fluent answer may still be false.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 49 — Tokens, context windows and inference settings

Learning outcome: Explain token limits and basic generation controls

Teacher explanation: Models process text as tokens rather than exactly as words. Context limits constrain how much input can be considered. Temperature and output limits affect generation behaviour, but they do not guarantee accuracy.

Worked example / demonstration: Compare a short and long prompt; identify what must be retained when a context window is limited. Demonstrate lower versus higher temperature conceptually.

Guided exercise: Compress a long instruction into a concise prompt while preserving requirements.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Write what information you removed and why it was safe to remove.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 50 — Training, fine-tuning and inference

Learning outcome: Distinguish model creation, adaptation and use

Teacher explanation: Training learns model parameters from data; fine-tuning further adapts a model; inference uses it. Fine-tuning is not a magic way to insert up-to-date facts; retrieval may be better for changing documents.

Worked example / demonstration: Compare three options for a policy bot: prompt-only, RAG over approved policy files, and fine-tuning. Choose based on update frequency and behaviour required.

Guided exercise: Recommend an approach for a changing product catalogue and justify the maintenance cost.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Explain why a new policy document often belongs in retrieval rather than model retraining.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 51 — Embeddings and semantic similarity

Learning outcome: Explain vector representations and similarity search

Teacher explanation: An embedding represents content as a numeric vector designed to capture useful relationships. Similarity search finds nearby representations, not guaranteed truth. Quality depends on the embedding model, chunking and query.

Worked example / demonstration: Compare exact keyword search with semantic search for 'refund' versus 'money back'; discuss why either can fail.

Guided exercise: Create five query/document pairs and predict which might be semantically similar.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Write one false-match example and a test to detect it.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 52 — Hallucinations and verification

Learning outcome: Use risk-based verification for generated answers

Teacher explanation: Hallucinations are unsupported or false outputs. Reduce risk with source grounding, retrieval, constrained formats, test suites and human review; none is a universal guarantee. High-impact decisions need stronger controls.

Worked example / demonstration: Give a model a fictional policy excerpt and ask it a question whose answer is absent; the expected answer is 'not stated in the source'.

Guided exercise: Build a five-question factuality checklist for a study assistant.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Add an out-of-scope test and describe the expected safe response.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 53 — Model selection: quality, latency, cost and modality

Learning outcome: Choose a model using explicit trade-offs

Teacher explanation: Model choice depends on task quality, context length, supported modalities, latency, privacy, availability, price and integration. The largest model is not always the best fit; benchmark on representative examples.

Worked example / demonstration: Compare two hypothetical models with quality, cost and response-time columns; select for low-risk FAQ versus complex reasoning.

Guided exercise: Build a model-selection scorecard and mark which criteria are non-negotiable.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Explain why a benchmark from another task may not predict your task's performance.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 54 — Build a small generative AI application

Learning outcome: Connect input, model call, response handling and evaluation

Teacher explanation: A basic application validates input, sends a request securely, handles errors and displays output with appropriate caveats. Do not expose secrets, log sensitive prompts carelessly or trust output blindly.

Worked example / demonstration: Trace the flow: user input → validation → API call → parse response → display → feedback/test log.

Guided exercise: Create a small approved demo or mock-API workflow that transforms fictional text and handles a failure response.

Scenario MCQ 1: A team wants an AI solution for this lesson's scenario. What should guide the choice?

- A. Brand popularity alone

- B. Task fit, evidence, cost, privacy and failure impact

- C. The longest possible output

- D. Avoid all testing

Correct answer: B. A sound decision uses the task and constraints rather than a single attractive feature.

Scenario MCQ 2: What is the most responsible way to handle an uncertain model output?

- A. Present it as guaranteed

- B. Hide the uncertainty

- C. Verify against appropriate evidence and communicate limitations

- D. Assume a higher temperature fixes it

Correct answer: C. Verification and transparent limitations are more reliable than style changes.

Specific homework (10–15 minutes, outside guided hours): Add a README with setup, safety considerations and a known limitation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 8 — Prompt Engineering, RAG & AI Application Foundations

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 55 — Prompt structure: task, context, constraints and format

Learning outcome: Construct prompts that make requirements explicit

Teacher explanation: A prompt can specify the task, audience, source material, constraints and output shape. Clear instructions improve consistency but do not remove the need for evaluation.

Worked example / demonstration: Prompt template: Role/task; context; provided data; constraints; output schema; checks. Compare a vague and a structured request.

Guided exercise: Write a prompt to produce a revision quiz from supplied notes without adding outside facts.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Submit initial prompt, revised prompt and two observed differences.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 56 — Few-shot examples and structured outputs

Learning outcome: Use examples and schemas to reduce ambiguity

Teacher explanation: Few-shot prompting supplies examples of desired input/output behaviour. Structured output such as JSON helps downstream code, but must still be parsed and validated.

Worked example / demonstration: Give two fictional support messages and their categories; request JSON with category and evidence fields; validate required keys.

Guided exercise: Create a three-example prompt and test a message unlike the examples.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Include a malformed response test and a recovery strategy.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 57 — Prompt testing and iteration

Learning outcome: Improve prompts through controlled comparisons

Teacher explanation: Change one element at a time and use the same test set. Otherwise, it is difficult to know what caused improvement. Keep failure cases rather than cherry-picking successful outputs.

Worked example / demonstration: Run baseline and revised prompts against five fixed fictional questions; score correctness and format adherence.

Guided exercise: Build a small prompt test table with expected answer, actual answer and score.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Document one change that improved results and one that did not.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 58 — Build an evaluation dataset

Learning outcome: Create representative tests before claiming success

Teacher explanation: A test set should include typical, boundary, ambiguous and out-of-scope cases. Keep expected outputs or scoring criteria, and protect private data. Reuse the same cases after changes.

Worked example / demonstration: Create a 10-row test set for a school FAQ assistant: answerable, missing policy, ambiguous, sensitive and adversarial questions.

Guided exercise: Design ten cases and define pass/fail criteria before running the model.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Add two cases that could expose unsupported claims.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 59 — Prompt benchmark mini-project

Learning outcome: Compare prompt versions with evidence

Teacher explanation: A benchmark measures performance against defined criteria such as correctness, completeness, format and safe refusal. Human judgement may be needed; note evaluator limitations and do not overstate a small test set.

Worked example / demonstration: Score two prompts on the same dataset using a rubric; calculate pass rate and review error types.

Guided exercise: Deliver prompt v1/v2, dataset, results table and a short recommendation.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Repeat the benchmark after one targeted improvement.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 60 — Context engineering and source selection

Learning outcome: Give a model relevant, trusted information

Teacher explanation: Context engineering chooses what information is supplied at inference time. Prefer current, authoritative and permitted sources. More context is not always better if it is irrelevant or contradictory.

Worked example / demonstration: For a school policy question, select the current policy version and exclude an outdated draft; label source date and owner.

Guided exercise: Rank five mock documents by authority, freshness and relevance.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Explain how the system should respond when sources conflict.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 61 — Chunking, metadata and document preparation

Learning outcome: Prepare documents for useful retrieval

Teacher explanation: Chunking divides content into retrievable pieces; metadata records source, date, topic or access class. Chunks that are too small lose meaning; chunks that are too large dilute relevance. Preserve source traceability.

Worked example / demonstration: Split a short policy into sections with headings; compare a chunk that splits a sentence with one that preserves a complete rule.

Guided exercise: Chunk a supplied public document and attach source/title/section metadata.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Inspect three chunks and identify missing context.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 62 — RAG architecture and retrieval

Learning outcome: Explain retrieve-then-generate and its limits

Teacher explanation: RAG retrieves relevant source chunks and supplies them to a generative model. It can improve grounding but cannot guarantee correct retrieval or reasoning. Measure retrieval quality separately from answer quality.

Worked example / demonstration: Draw: question → embed/search → top chunks → prompt with sources → answer/citations → evaluation.

Guided exercise: For five queries, manually rank relevant document chunks and explain one miss.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Add a case where the correct answer is absent and define the expected response.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 63 — Build a simple RAG knowledge assistant

Learning outcome: Connect document loading, retrieval and answer generation

Teacher explanation: A small RAG pipeline loads permitted files, chunks text, creates embeddings, retrieves candidates and asks a model to answer using that context. Keep API keys private and retain source identifiers for checking.

Worked example / demonstration: Implement or walk through a minimal pipeline using a small public document set; show retrieved chunks before showing the generated answer.

Guided exercise: Build a small assistant over two public documents or a provided mock retrieval layer; test at least five questions.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Submit architecture, test questions, source evidence and limitations.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 64 — AI application foundations and portfolio planning

Learning outcome: Define a feasible capstone with measurable acceptance criteria

Teacher explanation: A project begins with a real problem, intended user, allowed data, success criteria and failure plan. Scope should fit a beginner's time; a narrow tested application is stronger than a broad untested promise.

Worked example / demonstration: Example: answer questions from a public handbook with source snippets, abstain when evidence is missing and record a small evaluation set.

Guided exercise: Write a one-page capstone brief: problem, user, data, architecture, acceptance tests, risks and demo plan.

Scenario MCQ 1: Which evidence best supports a claim that the solution works?

- A. A polished demo only

- B. A defined test set, results, error review and limitations

- C. A confident vendor statement

- D. One successful example

Correct answer: B. Repeatable evaluation is stronger than a single success story.

Scenario MCQ 2: The expected answer is missing from trusted sources. What should a grounded assistant do?

- A. Invent a plausible answer

- B. State that the sources do not provide the answer

- C. Cite an unrelated source

- D. Remove all citations

Correct answer: B. Abstaining is safer than fabricating information.

Specific homework (10–15 minutes, outside guided hours): Get instructor approval and revise scope based on feedback.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 9 — Microsoft Azure AI Fundamentals AI-901: Concepts & Workloads

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 65 — AI-901 exam blueprint and study plan

Learning outcome: Map the official exam objectives to a personal revision plan

Teacher explanation: AI-901 assesses identifying AI concepts/capabilities and implementing AI solutions using Microsoft Foundry. The official guide is the source of truth; this lesson turns its current objectives into a checklist.

Worked example / demonstration: Learners mark each objective green/amber/red and schedule revision based on evidence, not confidence alone.

Guided exercise: Complete an objective checklist and identify three weak areas.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Use the official Microsoft AI-901 study guide to update this checklist before exam day.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 66 — AI workloads and considerations

Learning outcome: Choose AI workloads and identify responsible-use constraints

Teacher explanation: Different tasks call for different workloads: prediction, vision, language and generation. Selection should consider data, expected output, risk and responsible AI. AI-901 asks candidates to identify concepts and capabilities, not merely memorise labels.

Worked example / demonstration: Map image inspection, language translation, sales prediction and document Q&A to workload families; explain one safeguard for each.

Guided exercise: Complete a workload selection table with evidence and limitations.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Write five workload-to-capability flashcards.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 67 — Machine learning principles on Azure

Learning outcome: Connect ML concepts to a basic Azure AI use case

Teacher explanation: Features, labels, training and inference describe common ML workflows. Learn the Azure service category that fits the scenario, but avoid claiming that every Azure AI solution requires training a custom model.

Worked example / demonstration: Given a labelled product dataset, explain training/testing and compare a prebuilt capability with a custom model path.

Guided exercise: Answer scenario cards about classification, regression, training data and evaluation.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Review any ML objective you marked amber and add one worked scenario.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 68 — Computer vision workload selection in Azure

Learning outcome: Recognise image, object and OCR use cases

Teacher explanation: Image classification identifies a category, object detection localises objects and OCR extracts text. The current AI-901 guide should determine the precise service names and capabilities taught.

Worked example / demonstration: Match product-photo tagging, safety-helmet detection and invoice text extraction to workload and likely service family.

Guided exercise: For each scenario, state output, service category, limitation and validation check.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Create a one-page vision service comparison based on the official guide.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 69 — NLP workloads on Azure

Learning outcome: Identify language, text and speech use cases

Teacher explanation: Language tasks include sentiment, entity extraction, summarisation, translation and speech-related workflows. Select a capability based on the output needed and consider language coverage and errors.

Worked example / demonstration: Map review analysis, entity extraction, translation and transcription to different capabilities.

Guided exercise: Complete a set of scenario cards and explain why the distractor service is less suitable.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Revise language workload terms with one example each.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 70 — Generative AI workloads on Azure

Learning outcome: Explain foundation models and generative AI scenarios

Teacher explanation: Generative AI creates text, code, images or other outputs. Selection requires attention to modality, context, cost, latency, grounding and safety. A fluent output may be wrong or unsupported.

Worked example / demonstration: Choose between text generation, document-grounded Q&A and a deterministic calculation; explain why a model alone is not ideal for the calculation.

Guided exercise: Evaluate four GenAI use cases and choose one safety test for each.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Write a generative AI decision tree.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 71 — Microsoft Foundry overview and model catalogue

Learning outcome: Explain Foundry's role in selecting and using models

Teacher explanation: The current AI-901 exam emphasizes implementing AI solutions using Microsoft Foundry. Teach the current portal/service terminology, model catalogue concepts and approved hands-on steps directly from Microsoft Learn; UI labels can change.

Worked example / demonstration: Instructor demonstrates selecting a model for a sandbox scenario, reviewing deployment/usage prerequisites and recording expected cost controls.

Guided exercise: Use a guided sandbox or annotated screenshots to identify the model, deployment and test steps.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Capture a current official Learn reference for each UI step.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 72 — Model selection and deployment concepts

Learning outcome: Select a model using requirements and constraints

Teacher explanation: Model selection considers task, modality, language, context, quality, latency, cost and permitted data. A deployment choice is not complete until access, quotas, monitoring and failure behaviour are considered.

Worked example / demonstration: Compare two hypothetical models for a student FAQ bot and choose using a weighted scorecard.

Guided exercise: Fill in a model selection matrix for two contrasting tasks.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Explain one trade-off your chosen model creates.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 73 — Build/use an AI solution through a guided workflow

Learning outcome: Trace a request from user input to model response

Teacher explanation: Implementation requires more than selecting a model: validate input, call the endpoint through approved methods, parse output and handle failures. Follow current Microsoft guidance for the specific sandbox.

Worked example / demonstration: Trace a simple request-response example and identify endpoint, credential, payload, response and error branch.

Guided exercise: Use a provided code sample or mock response to identify each component; do not expose secrets.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Annotate the workflow with three failure cases and remedies.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 74 — Python syntax and techniques required by AI-901

Learning outcome: Read basic Python used in AI solution examples

Teacher explanation: The exam expects foundational Python syntax and programming techniques. Focus on variables, strings, lists/dictionaries, conditions, functions, JSON and reading a short API example; do not promise advanced software engineering.

Worked example / demonstration: Read a short snippet that builds a request payload dictionary and prints a selected response field.

Guided exercise: Answer code-reading questions and fix a type/key error in a short example.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Practise ten short code-reading questions.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 10 — Microsoft Azure AI Fundamentals AI-901: Foundry & Exam Readiness

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 75 — REST APIs, SDKs and CLI concepts

Learning outcome: Distinguish common ways to interact with services

Teacher explanation: REST APIs use HTTP requests; SDKs provide language-specific helpers; command-line interfaces expose operations through commands. Understand what each is for and how credentials are supplied securely.

Worked example / demonstration: Compare the same conceptual operation via a REST request, Python SDK and CLI; label authentication and output handling.

Guided exercise: Select an interaction method for a scripted app versus a one-off administrative task.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Create a comparison card with one strength and one risk for each method.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 76 — Azure resources, identity and access fundamentals

Learning outcome: Recognise resources, authentication and least privilege

Teacher explanation: AI solutions run within cloud resources and require controlled access. Authentication establishes identity; authorisation controls actions. Use least privilege and protect credentials; the course introduces concepts, not full cloud administration.

Worked example / demonstration: Draw user → identity/authentication → permission check → AI resource → response. Identify where a key could leak.

Guided exercise: Review a fictional configuration and mark excessive permissions or exposed secrets.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Write three safe credential-handling rules.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 77 — Responsible AI and workload limitations

Learning outcome: Apply fairness, reliability, safety, privacy and transparency

Teacher explanation: Responsible AI is not an optional final slide. Evaluate who may be harmed, how output can fail and what oversight is appropriate. In certification scenarios, choose controls tied to the risk rather than generic 'be careful' answers.

Worked example / demonstration: For a student support assistant, map a privacy risk, a hallucination risk and a fairness risk to controls.

Guided exercise: Complete a responsible AI checklist for one scenario.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Review Microsoft's current responsible AI guidance and add one example.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 78 — AI-901 scenario lab: workload selection

Learning outcome: Answer mixed scenarios using the exam's language

Teacher explanation: Exam questions test choosing appropriate capabilities under constraints. Read the entire scenario, identify the requested output and constraints, then eliminate answers that solve a different problem or add unnecessary complexity.

Worked example / demonstration: Work a scenario: extract text from receipts and flag uncertain totals. Separate OCR, deterministic validation and human review.

Guided exercise: Complete ten instructor-written scenario questions with explanations for every distractor.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Rework missed questions and note the misconception, not only the correct letter.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 79 — AI-901 scenario lab: Foundry implementation

Learning outcome: Apply implementation reasoning to a model workflow

Teacher explanation: The implementation-heavy portion requires familiarity with current Microsoft Foundry concepts and how a model is selected, accessed and tested. Practise with the current official materials rather than stale screenshots.

Worked example / demonstration: Order the steps from task definition to model selection, approved access, test request, output review and monitoring.

Guided exercise: Complete a sequence/order task and explain the purpose of each step.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Review any step you placed incorrectly and update your notes.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 80 — AI-901 timed practice set 1

Learning outcome: Manage time and identify weak objective areas

Teacher explanation: A timed practice set tests recall and scenario reasoning under exam conditions. Review by objective category and explain why each wrong option is wrong; memorising answer keys is fragile.

Worked example / demonstration: Complete a timed mini-mock assembled from instructor-created questions and current official practice resources where available.

Guided exercise: Sit the mini-mock without notes and calculate performance by topic.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Create a targeted remediation plan for the two lowest areas.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 81 — AI-901 remediation and targeted labs

Learning outcome: Close gaps with focused practice

Teacher explanation: Remediation should change what the learner can do: explain a concept, choose a capability and complete a simple task. Repeating a quiz without correcting the misconception is not enough.

Worked example / demonstration: Re-teach the three most commonly missed items using a worked example, then retest with a new scenario.

Guided exercise: Complete targeted practice for the learner's lowest-scoring objectives.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Submit evidence of improvement on new questions.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 82 — AI-901 timed mock exam

Learning outcome: Simulate exam pacing and post-exam analysis

Teacher explanation: Use a current practice assessment and timed mock under exam-like conditions. The pass score and rules must be verified on the official exam page. A practice score is evidence of readiness, not a guarantee.

Worked example / demonstration: After the mock, classify every miss: knowledge gap, misread scenario, service confusion or time pressure.

Guided exercise: Complete the mock and review every incorrect or guessed answer.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Repeat missed objective areas with a fresh question set.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 83 — AI-901 final revision and exam readiness gate

Learning outcome: Decide readiness from evidence and plan exam logistics

Teacher explanation: Before booking, verify the live exam page, candidate identity requirements, language, price, availability and current study guide. A learner who has not reached the programme's readiness threshold should receive remediation, not pressure to book.

Worked example / demonstration: Use a readiness checklist: objective coverage, timed practice, weak-area closure, device/ID and scheduling plan.

Guided exercise: Teacher signs off readiness only after the defined practice threshold and review.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Prepare a final one-page exam-day checklist.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 84 — AI-901 capstone-to-exam bridge and reflection

Learning outcome: Connect practical learning to exam concepts

Teacher explanation: The capstone demonstrates applied judgement, while the exam tests its defined objectives. Explain which design decisions map to AI workload selection, responsible AI and implementation concepts; do not confuse project quality with exam coverage.

Worked example / demonstration: Students annotate their capstone architecture with workload, model choice, input handling, test plan and responsible-use controls.

Guided exercise: Present a five-minute explanation and answer two new exam-style scenarios.

Scenario MCQ 1: In an AI-901 scenario, what should determine the answer?

- A. Which product name sounds newest

- B. The requested capability, constraints and current Microsoft exam guidance

- C. The longest option

- D. The first service mentioned

Correct answer: B. The scenario's requirements and the official current scope determine the best fit.

Scenario MCQ 2: A learner is unsure about a current portal label. What is the best study action?

- A. Guess based on an old screenshot

- B. Verify against current Microsoft Learn material and practise the workflow

- C. Skip all implementation objectives

- D. Memorise a third-party answer key

Correct answer: B. Cloud interfaces and objectives can change; use current official material.

Specific homework (10–15 minutes, outside guided hours): Revise the project README to include architecture and evaluation evidence.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 11 — AWS Certified AI Practitioner AIF-C01: AI/GenAI & Services

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 85 — AIF-C01 exam blueprint and weighted study plan

Learning outcome: Use domain weights to allocate revision time

Teacher explanation: AWS AIF-C01 covers AI/ML fundamentals (20%), GenAI fundamentals (24%), foundation-model applications (28%), responsible AI (14%) and security/compliance/governance (14%). Use the current AWS exam guide and in-scope services list.

Worked example / demonstration: Allocate practice effort across domains, giving the largest revision share to foundation-model applications while maintaining coverage of every domain.

Guided exercise: Create a weighted checklist and mark confidence against each task statement.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Verify the exam guide version and in-scope services before each cohort.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 86 — AI and ML terminology and use cases

Learning outcome: Explain models, training, inference, features and labels

Teacher explanation: The exam expects foundational concepts and practical use-case selection, not building complex algorithms. Distinguish AI, ML, deep learning, computer vision, NLP, generative AI, agentic AI, training and inference.

Worked example / demonstration: Match fraud flagging, image tagging, text summarisation and demand forecasting to appropriate capability families.

Guided exercise: Complete a terminology matching task with one real-world example per term.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Write a glossary in plain language.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 87 — AI/ML lifecycle and data concepts

Learning outcome: Describe problem definition through evaluation

Teacher explanation: A lifecycle includes problem framing, data preparation, model selection/training or service choice, evaluation, deployment/use and monitoring. Data quality and leakage can undermine outcomes before model choice matters.

Worked example / demonstration: Map a demand prediction task from business goal to data, split, metric, review and monitoring.

Guided exercise: Order lifecycle cards and identify where a biased sample could enter.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Add a lifecycle diagram to your revision notes.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 88 — Generative AI fundamentals and use cases

Learning outcome: Explain tokens, prompts, embeddings, foundation models and modalities

Teacher explanation: GenAI terms include tokens, chunking, embeddings, vectors, prompts, transformer LLMs, foundation models and multimodal models. Know use cases and limits, not only definitions.

Worked example / demonstration: Match summarisation, translation, image generation, code assistance and document Q&A to model capabilities and safeguards.

Guided exercise: Build a term-to-use-case matrix and explain one limitation for each.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Revise the terms with scenario-based flashcards.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 89 — Foundation-model selection trade-offs

Learning outcome: Choose a model using cost, latency, modality and quality

Teacher explanation: Model selection considers intended task, model size, supported input/output, context length, languages, customisation, response time and cost. A bigger model may be slower or more expensive without improving the target task.

Worked example / demonstration: Choose between a low-latency FAQ model and a higher-quality complex summarisation model using a fictional requirements table.

Guided exercise: Score three hypothetical models against explicit requirements.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Explain the trade-off that matters most in your scenario.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 90 — Prompt engineering techniques

Learning outcome: Use instructions, examples and constraints intentionally

Teacher explanation: Prompt techniques include clear instructions, context, few-shot examples, output constraints and decomposition. Evaluate prompts on a fixed test set rather than assuming one prompt is universally best.

Worked example / demonstration: Compare zero-shot and few-shot classification on the same fictional support messages; score format and accuracy.

Guided exercise: Write and test two prompt variants against the same five cases.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Document failures and which prompt change addressed them.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 91 — Inference parameters and output control

Learning outcome: Explain temperature, token limits and response variability

Teacher explanation: Generation settings influence style, variability and length. They do not guarantee truth. A low-variance setting may suit structured tasks, while creative tasks may tolerate more variation; always evaluate the actual output.

Worked example / demonstration: Use a hypothetical temperature/output-token comparison and choose settings for a JSON classification versus a brainstorming task.

Guided exercise: Recommend settings for two scenarios and explain what must still be tested.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Add a note distinguishing output control from factual verification.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 92 — RAG, chunking, embeddings and vector search

Learning outcome: Describe how retrieval supports foundation-model applications

Teacher explanation: RAG combines retrieved external context with generation. Chunk size, metadata, embeddings, retrieval strategy and source freshness affect results. Retrieval can miss evidence; generated answers can misinterpret retrieved evidence.

Worked example / demonstration: Trace query → embedding → vector search → retrieved chunks → model prompt → answer and source checks.

Guided exercise: Diagnose a mock RAG failure caused by outdated document metadata or poor chunking.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Create a failure-mode table for retrieval and generation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 93 — Agents and tool use

Learning outcome: Recognise when a model calls tools and why guardrails matter

Teacher explanation: An agent may choose tools and sequence actions toward a goal. Tool permissions, validation, audit trails and human approval matter because a model can select the wrong action. Not every workflow needs an agent.

Worked example / demonstration: Compare a fixed three-step workflow with an agent that chooses tools; identify when deterministic steps are safer.

Guided exercise: Design a bounded agent for searching public FAQs, with read-only tools and a stop condition.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Document allowed tools, prohibited actions and human escalation.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 94 — Fine-tuning, adaptation and model evaluation

Learning outcome: Distinguish prompting, retrieval and fine-tuning

Teacher explanation: Fine-tuning adapts model behaviour using examples; RAG supplies changing external knowledge; prompting directs a model at inference time. Evaluate quality, robustness, cost and latency using representative tests.

Worked example / demonstration: Choose between prompt-only, RAG and fine-tuning for changing policies, consistent tone and domain-specific output format.

Guided exercise: Choose an adaptation approach for three cases and justify maintenance costs.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Write one reason your chosen approach could still fail.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

## Month 12 — AWS Certified AI Practitioner AIF-C01: Governance & Exam Readiness

Allocation: 10 hours \| 10 lectures. All lecture time is included in the 104-hour total.

### Lecture 95 — AWS AI service map: Amazon Bedrock and SageMaker AI

Learning outcome: Recognise foundation-model access versus model-building workflows

Teacher explanation: Amazon Bedrock provides access to foundation-model capabilities and tools for building GenAI applications. SageMaker AI supports building, training and deploying ML workflows. Learn the current in-scope service definitions from the official AIF-C01 guide.

Worked example / demonstration: Choose Bedrock for a managed foundation-model application scenario and SageMaker AI for a custom model lifecycle scenario; state that actual service fit depends on requirements.

Guided exercise: Complete a service-purpose matching activity from the current official service list.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Update service names and scope from the current AWS exam guide.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 96 — AWS AI service map: vision, text, speech and documents

Learning outcome: Match managed AI services to common tasks

Teacher explanation: Foundational service recognition includes understanding the purpose of services such as Rekognition, Textract, Comprehend, Lex, Polly, Transcribe and Translate where included in the current guide. Avoid memorising names without knowing the task each supports.

Worked example / demonstration: Map image/video analysis, document text extraction, text analysis, conversational interfaces, speech synthesis, transcription and translation to the relevant service family.

Guided exercise: Complete ten scenario cards with service choice and one limitation.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Create a service map with a sample use case for each in-scope service.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 97 — AWS core services, storage, identity and shared responsibility

Learning outcome: Explain core cloud concepts relevant to AI solutions

Teacher explanation: The exam expects familiarity with core services and security concepts, including S3, compute, IAM, pricing and the shared responsibility model. AWS secures the cloud; customers remain responsible for appropriate configuration and data use in their workloads.

Worked example / demonstration: For a fictional AI app, map data storage, model access, permissions and logging; distinguish provider responsibilities from customer configuration.

Guided exercise: Identify an over-permissive IAM policy and propose least-privilege access conceptually.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Revise shared-responsibility examples and credential-handling controls.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 98 — Responsible AI, transparency and sustainability

Learning outcome: Recognise fairness, robustness, safety, veracity and explainability

Teacher explanation: Responsible AI includes fairness, inclusivity, robustness, safety, veracity and transparency. Consider environmental/cost impact and legal risks such as IP issues, biased outputs, hallucinations and loss of trust.

Worked example / demonstration: Review a fictional AI content assistant and identify risks, user disclosures, evaluation tests and human review.

Guided exercise: Complete a responsible-AI risk matrix with mitigation and owner.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Create one scenario per responsible AI concept.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 99 — Security, compliance and governance

Learning outcome: Identify safeguards for AI data and systems

Teacher explanation: Security topics include IAM roles/policies, encryption, data access, privacy, source lineage and governance. Know relevant AWS security/governance service purposes from the official in-scope list. This is foundational recognition, not a promise of expert security engineering.

Worked example / demonstration: Trace a sensitive document through access control, storage, retrieval, model call and logging; identify where exposure can occur.

Guided exercise: Review a mock architecture and mark five security or governance risks.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Update service references against the current AWS guide.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 100 — AIF-C01 mixed-domain scenario workshop

Learning outcome: Apply service and concept knowledge to business scenarios

Teacher explanation: Exam questions may ask for the best option under constraints. Identify the goal, data sensitivity, risk, cost and output, then eliminate choices that solve a different problem or overcomplicate the design.

Worked example / demonstration: A company needs internal policy Q&A with source-grounded answers: consider Bedrock, RAG, access controls, evaluation and abstention when no evidence is found.

Guided exercise: Answer a set of mixed-domain questions and explain every distractor.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Create a miss log grouped by official domain.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 101 — AIF-C01 timed practice set and domain analysis

Learning outcome: Use timed practice to identify objective gaps

Teacher explanation: Timed practice should reflect the official exam format and domain scope. AWS uses multiple question types; practise single-answer, multiple-response, matching and ordering where appropriate. Use current official exam guidance for exact logistics.

Worked example / demonstration: Complete a timed mini-mock with questions spread across all five domains and review guessed answers as well as wrong ones.

Guided exercise: Score by domain and select two targeted remediation areas.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Repeat only missed objectives using new questions, not the same answer key.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 102 — AIF-C01 remediation: services and scenario reasoning

Learning outcome: Correct weak service mappings and misconceptions

Teacher explanation: A weak domain needs a concrete repair: revisit definitions, compare similar services, then answer a new scenario. Service lists can change, so the official in-scope list must be refreshed before delivery.

Worked example / demonstration: Run a service-mapping drill where learners explain why each distractor is unsuitable.

Guided exercise: Complete a fresh targeted quiz and explain corrections aloud.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Add unresolved questions to an instructor update list.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 103 — AIF-C01 timed mock exam and review

Learning outcome: Assess readiness across all five domains

Teacher explanation: A mock exam is a readiness signal, not a guarantee. Review missed and guessed answers, especially foundation-model applications and security/governance. Do not advertise a guaranteed pass based on attendance.

Worked example / demonstration: Run a timed mock, produce a domain breakdown and create a remediation plan.

Guided exercise: Complete mock exam and oral review of three difficult questions.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Revisit the lowest domain and retest with a fresh set.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

### Lecture 104 — AIF-C01 final readiness gate and AI portfolio bridge

Learning outcome: Confirm exam readiness and connect concepts to a project

Teacher explanation: A learner should verify current exam details, price, registration rules and guide version before booking. Connect capstone decisions to model choice, RAG, evaluation, responsible AI and security without assuming project completion replaces exam preparation.

Worked example / demonstration: Annotate a portfolio project with relevant AWS service categories, data protection controls, model trade-offs and evaluation evidence.

Guided exercise: Present a short project explanation and answer two unseen certification-style scenarios.

Scenario MCQ 1: For an AIF-C01 scenario, which reasoning is strongest?

- A. Choose the most complex service

- B. Match the need, constraints, risk and relevant in-scope service

- C. Assume every question requires model training

- D. Ignore data security

Correct answer: B. The exam focuses on selecting appropriate foundational concepts and services for the scenario.

Scenario MCQ 2: A service name appears in an older study note. What should the instructor do?

- A. Assume it is still in scope

- B. Verify the current official AIF-C01 guide and in-scope services list

- C. Delete all AWS service teaching

- D. Teach it as an exam guarantee

Correct answer: B. AWS updates guides; current official material takes precedence.

Specific homework (10–15 minutes, outside guided hours): Prepare exam-day checklist and a final portfolio update.

Teacher check: Ask the learner to explain the result in their own words, identify one limitation and show evidence of the exercise.

# 6. Certification alignment and exam facts

## Microsoft Azure AI Fundamentals — AI-901

Verified against Microsoft's current AI-901 exam page on 12 October 2026. Microsoft lists two assessed areas: Identify AI concepts and capabilities (40–45%) and Implement AI solutions by using Microsoft Foundry (55–60%). Microsoft states a passing score of 700. The English exam guide was updated on 15 April 2026. AI-900 retired on 30 June 2026; do not advertise AI-900 as current.

Course mapping: Months 1–2 teach AI concepts and responsible use; Month 5 teaches ML principles; Month 6 covers vision and NLP; Month 7 covers generative AI; Months 9–10 provide 20 dedicated hours for AI-901 objectives, Microsoft Foundry concepts, Python/API/SDK/CLI familiarity, scenario practice, mock testing and remediation.

Current listed price: Microsoft Learn's India-localised AI-901 page lists ₹3,691 before applicable taxes/promotional adjustments. Price is subject to change; confirm with Microsoft/Pearson VUE before registration.

Official reference: https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/

## AWS Certified AI Practitioner — AIF-C01

Verified against the current AWS exam guide. Domains: AI/ML fundamentals 20%; GenAI fundamentals 24%; applications of foundation models 28%; responsible AI 14%; security, compliance and governance 14%. AWS lists 700 as the scaled passing score for foundational exams. AIF-C01 is the current exam code used in this curriculum.

Course mapping: Months 1, 5, 7 and 8 introduce AI/ML, GenAI, prompts, embeddings, RAG, evaluation and responsible use; Months 11–12 provide 20 dedicated hours for AWS domains, service recognition, scenarios, practice formats, mock testing and remediation.

Current AWS foundational exam price listed for India: ₹8,553 when purchasing exam vouchers through the Pearson VUE/Mindhub channel; the final price may vary by purchase route, taxes or changes. Verify before advertising or booking.

Official references: https://docs.aws.amazon.com/aws-certification/latest/ai-practitioner-01/ai-practitioner-01.html and https://aws.amazon.com/certification/policies/before-testing/

## Market value and honest positioning

These are entry-level/foundational credentials. They can help demonstrate structured learning and vocabulary, but they do not by themselves prove job readiness or guarantee employment or salary. The course's stronger differentiator should be the student's practical portfolio, ability to explain decisions, responsible-use judgement and tested projects.

Exam fees are separate from course fees. Re-attempts may require paying again. Confirm the live official price, taxes, availability and exam policies before publishing a brochure.

# 7. NVIDIA certification appendix (optional pathway, not included in 104 hours)

NVIDIA currently lists the NVIDIA-Certified Associate Generative AI LLMs credential (NCA-GENL) at USD \$125, with a 60-minute remotely proctored exam, 50–60 multiple-choice questions and two-year validity. Its published topic areas include ML/neural-network fundamentals, prompt engineering, alignment, data analysis/visualisation, experimentation, preprocessing/feature engineering, experiment design, software development, Python libraries for LLMs, and LLM integration/deployment.

This NVIDIA credential is not part of the 104-hour certification promise. It is an optional extension: Months 3–8 build some relevant foundations, but a separate objective-by-objective mapping and dedicated preparation would be needed before marketing it as an aligned exam pathway. The \$125 fee is subject to change and currency/tax effects.

Official reference: https://www.nvidia.com/en-us/learn/certification/generative-ai-llm-associate/

# 8. Certification readiness policy

- Before every cohort, compare lecture materials against the current official exam guide and study guide; exam objectives and service names can change.

- Use at least one full timed mock per certification, plus domain-level remediation. The 20 hours per exam are dedicated blocks, not a guarantee of passing.

- Set an internal readiness gate (recommended: 80% on two fresh practice sets and no major unresolved objective gap) before recommending students book.

- Use official Microsoft/AWS training and practice resources where available. Do not reproduce live exam questions or promise leaked questions.

- Tell students that exam fees are separate and certification is awarded by the certifying organisation only after passing its exam.

# 9. Practical portfolio sequence

| Stage        | Deliverable                    | Evidence expected                                                               |
|--------------|--------------------------------|---------------------------------------------------------------------------------|
| Month 1      | AI observation and task audit  | Use-case table; identify rule-based vs AI; risk note.                           |
| Month 2      | Responsible AI audit           | Data risks, failure cases, safeguards and go/no-go recommendation.              |
| Month 3      | Python mini-program            | Runnable code, test cases and debugging note.                                   |
| Month 4      | CSV data workflow              | Cleaned fictional dataset, two charts, function, README and data-quality notes. |
| Month 5      | ML mini-project                | Dataset, features/target, split, model, metric, error analysis and limitations. |
| Month 6      | Vision/NLP evaluation          | Input-output examples, failure log and responsible-use note.                    |
| Month 7      | Generative AI mini-app         | Prompt, API/mock workflow, validation and test cases.                           |
| Month 8      | Prompt/RAG prototype plan      | Evaluation dataset, architecture, source strategy and capstone brief.           |
| Months 9–10  | Azure AI-901 revision evidence | Objective checklist, Foundry workflow notes, timed mock and remediation log.    |
| Months 11–12 | AWS AIF-C01 revision evidence  | Domain checklist, service map, timed mock and remediation log.                  |

# 10. Curriculum QA checklist before launch

- Exactly 104 numbered lectures; each is one guided hour; homework remains outside the 104 hours.

- Core phase is 8 months / 64 hours; AI-901 is 2 months / 20 hours; AIF-C01 is 2 months / 20 hours.

- Entry requirement says 10th-pass, not Class 8+.

- Each lecture has topic-specific explanation, worked example, exercise, two distinct scenario MCQs with varied answer positions, answer rationale and specific homework.

- Month 9–10 lecture bodies teach AI-901 topics; Month 11–12 bodies teach AIF-C01 topics; no certification titles are attached to unrelated capstone content.

- All prices and exam details are labelled as checked on 12 October 2026 and must be rechecked before publication.

- Course marketing does not guarantee passing, employment or salary.
