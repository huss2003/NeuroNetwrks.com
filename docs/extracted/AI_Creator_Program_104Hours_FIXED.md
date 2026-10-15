**AI Foundations, AI Application & AI Creator Program**

**104 Hours · 52 Weeks · 2 Hours/Week · Class 8+ Entry**

*Absolute Beginner → AI-Literate → AI Builder → AI Creator*

Teacher-Ready Curriculum · 104 Numbered Lectures, Every One Written to Its Own Topic

**1. Program Purpose and Graduate Outcome**

This is a project-oriented, one-year AI Creator program for students from Class 8 entry. It builds, in order: AI foundations and responsible-use habits, real Python programming, data handling, classical machine learning, computer vision and NLP, generative AI and LLMs, prompt and context engineering, retrieval-augmented generation, Python-based AI APIs and agents, full application development/testing/deployment, and finally cloud-certification preparation and a capstone project.

By graduation, a student can: write and debug real Python programs; load, clean and visualise data with Pandas/NumPy/Matplotlib; train and honestly evaluate a simple ML model; use computer vision, NLP and generative AI services appropriately for a task; integrate an AI API securely, handling errors and secrets correctly; design, build and evaluate a RAG-based knowledge assistant; build, test, deploy and security-audit a complete AI application; and present a documented, evaluated capstone project as a public GitHub portfolio.

**2. Twelve-Month Hour Allocation**

This allocation was checked for internal consistency against the full lecture list: every month's stated hours equal exactly its number of numbered lectures, and the twelve months sum to exactly 104.

| **Month**    | **Module**                                        | **Hours / Lectures** |
|--------------|---------------------------------------------------|----------------------|
| **Month 1**  | AI Foundations & How Modern AI Works              | **4**                |
| **Month 2**  | AI Tools, Safety, Ethics & Responsible AI         | **4**                |
| **Month 3**  | Python Programming Fundamentals I                 | **10**               |
| **Month 4**  | Python Programming Fundamentals II & Data Science | **8**                |
| **Month 5**  | Machine Learning Fundamentals with Python         | **10**               |
| **Month 6**  | Computer Vision, NLP & Multimodal AI              | **6**                |
| **Month 7**  | Generative AI, LLMs & Foundation Models           | **8**                |
| **Month 8**  | Prompt Engineering & AI Evaluation                | **7**                |
| **Month 9**  | Context Engineering, Embeddings & RAG             | **8**                |
| **Month 10** | Python AI APIs, Agents & Automation               | **9**                |
| **Month 11** | AI Application Development, Testing & Deployment  | **12**               |
| **Month 12** | Cloud AI, Final Capstone & Graduation             | **18**               |
| **TOTAL**    | **104 one-hour lectures**                         | **104**              |

Month 12's 18 hours split as: 6 hours Azure AI-901 preparation (Lectures 87-92), 6 hours AWS AIF-C01 preparation (Lectures 93-98), and 6 hours capstone implementation, evaluation and graduation (Lectures 99-104).

**3. Teaching and Assessment Model**

**•** Each numbered lecture is one guided teaching hour, plus 10-15 minutes of homework outside the guided hour.

**•** Every lecture's content below (explanation, examples, knowledge checks, evaluation question, homework and checklist) is written specifically for that lecture's own topic — nothing is copied boilerplate with only the topic name swapped in.

**•** A dedicated 30-question unit exam closes every major unit; both certification tracks (Lectures 87-98) end in a full-length mock exam before the real certification attempt.

**•** Mandatory practicals: Month 4 (a full Python/Pandas data-cleaning practical, Lecture 25) and Month 5 (an independent end-to-end ML practical assessment, Lecture 36) are graded individually.

**•** Generic, cross-field skills — prompt engineering and context engineering — are deliberately built to Level 4 (independent, novel-task capable) rather than capped at Level 3, across Months 8-9.

**•** Every project-style lecture ends with a GitHub publication habit (introduced Lecture 26): code plus a README stating purpose, approach/data and limitations.

**What Was Fixed in This Edition**

This document was produced after a structural and content review of an earlier 104-lecture draft. That review found the lecture-by-lecture structure (104 numbered lectures, monthly hour totals, topic sequencing) was already sound, but that nearly every lecture body reused one identical template sentence, one identical pair of multiple-choice questions, and — in the ten certification-preparation lectures specifically — body content about an unrelated placeholder topic instead of the stated Azure AI-901 / AWS AIF-C01 material. The fixes made in this edition:

**•** Every one of the 104 lectures below has its own teacher explanation, real-world example, in-class activity, two knowledge-check questions, evaluation question, homework task and checklist, written for that lecture's specific topic — none of the generic template sentences or reused MCQ pairs from the earlier draft remain.

**•** Lectures 87-92 (previously generic "cloud fundamentals" placeholder text under an AI-901 title) now actually teach AI-901's exam structure, domain weightings, Microsoft Foundry implementation concepts, and exam-style practice.

**•** Lectures 93-98 (previously generic "capstone requirements/implementation" placeholder text under an AIF-C01 title) now actually teach AIF-C01's five domains, named AWS AI services, and exam-style practice, using the certification facts (domain weightings, question counts, passing score) verified earlier against the official exam guides.

**•** The verified-correct skeleton is unchanged: 12 months, 104 sequential lectures, and the same month-by-month hour allocation, which was confirmed to sum to exactly 104 and to match the lecture count in every month.

**Month 1 AI Foundations & How Modern AI Works**

*Allocation: 4 hours \| 4 lectures*

**Lecture 1 What AI Is and Where We Use It**

*Month 1 · AI Foundations & How Modern AI Works · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Identify everyday AI applications and explain, in plain language, what makes them "AI" rather than ordinary software.                                                                                                                                                                                                                                                                                                                      |
| **Key concepts**        | Definition of AI · Narrow vs general AI · Where AI already shows up in daily life                                                                                                                                                                                                                                                                                                                                                          |
| **Teacher explanation** | Open by asking students to list five apps they used this week, then sort them into "AI" and "not AI." Introduce the working definition: AI is software that makes decisions or predictions from data and patterns, rather than following a fixed set of if-this-then-that instructions written in advance. Contrast a calculator (fixed rules) with a photo app that recognises faces (learned patterns) to make the distinction concrete. |
| **Real-world example**  | A food-delivery app predicting your delivery time from traffic and order data; a phone camera automatically recognising faces to group photos.                                                                                                                                                                                                                                                                                             |
| **In-class activity**   | In pairs, students audit 3 apps on a phone/tablet and tag each feature as "rule-based" or "AI-based," giving one reason for each tag.                                                                                                                                                                                                                                                                                                      |

**Knowledge check 1:** A washing machine has a dial with fixed wash cycles (Cotton, Wool, Quick Wash). Is this AI?

**(A) No -- it follows a fixed set of pre-programmed rules with no learning from data.**

\(B\) Yes -- it has electronic buttons.

\(C\) Yes -- all modern appliances use AI.

***Correct answer: A***

**Knowledge check 2:** A spam filter gets better at catching new spam the more emails it sees. What makes this AI rather than a fixed rule list?

\(A\) It uses electricity.

**(B) It changes its behaviour based on patterns learned from data rather than a hand-written rule list.**

\(C\) It runs on a server instead of a phone.

***Correct answer: B***

**Evaluation question:** Pick one app you used today. Explain in 3-4 sentences what decision it makes, what data it likely uses to make that decision, and why you think it counts (or doesn't count) as AI.

**Homework (10-15 min):** List 5 AI-powered features you encounter in a normal day (apps, devices, services) and write one sentence per feature on what data you think it is using.

**Teacher checklist**

**✓** Can state the working definition of AI without reading it off a slide

**✓** Correctly classifies at least 2 of 3 audited app features

**✓** Gives a data-based reason, not a vague one ("it's smart")

**Lecture 2 AI, ML, Deep Learning and Generative AI**

*Month 1 · AI Foundations & How Modern AI Works · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Place AI, machine learning, deep learning and generative AI correctly inside one another and give one example of each.                                                                                                                                                                                                                                                                                                                                                                          |
| **Key concepts**        | AI as the umbrella term · Machine learning = learning from data · Deep learning = neural networks · Generative AI = creates new content                                                                                                                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Draw four nested circles on the board live: AI (outermost) contains Machine Learning, which contains Deep Learning, which contains today's Generative AI. Walk through why each is a subset of the one before it -- ML is the main way we build AI today; deep learning is one powerful technique within ML that uses layered neural networks; generative AI is a deep-learning system trained specifically to produce new text, images or audio rather than just classify or predict a number. |
| **Real-world example**  | A spam filter (classic machine learning); a face-unlock system (deep learning); ChatGPT writing an essay or Midjourney drawing an image (generative AI).                                                                                                                                                                                                                                                                                                                                        |
| **In-class activity**   | Give students 6 real tool names (e.g. a spam filter, a self-driving car's pedestrian detector, a chatbot, a recommendation engine, a voice-to-text app, an image generator) and have them place each into the correct ring of the nested-circle diagram with a one-line justification.                                                                                                                                                                                                          |

**Knowledge check 1:** Which statement correctly describes the relationship between the four terms?

\(A\) They are four unrelated, competing technologies.

\(B\) Generative AI is the oldest term and AI is the newest.

**(C) AI is the broadest category; machine learning, deep learning and generative AI are each progressively narrower subsets inside it.**

***Correct answer: C***

**Knowledge check 2:** A system is trained on millions of product photos and can now write a short, original description for a brand-new photo it has never seen. This is best classified as:

\(A\) Classic rule-based software.

**(B) Generative AI (it produces new content, not just a label or number).**

\(C\) A spreadsheet formula.

***Correct answer: B***

**Evaluation question:** Draw the nested-circle diagram from memory and place ChatGPT, a spam filter, and a self-driving car's object detector in the correct rings, with one sentence justifying each placement.

**Homework (10-15 min):** Find one more real AI tool (not used in class) and write 2-3 sentences placing it correctly among AI / ML / deep learning / generative AI, justifying your placement.

**Teacher checklist**

**✓** Draws the nesting order correctly without prompting

**✓** Places at least 2 of 3 example tools in the right ring

**✓** Explains generative AI as "creates new content" rather than just "advanced AI"

**Lecture 3 How AI Systems Work**

*Month 1 · AI Foundations & How Modern AI Works · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Describe, step by step, the path data takes from training to a working prediction (input -\> model -\> output).                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | Training data · The model as a pattern-matcher · Input -\> processing -\> output · Why more/better data usually improves results                                                                                                                                                                                                                                                                                                                                                                                       |
| **Teacher explanation** | Use a concrete, traceable example: a model trained to tell cats from dogs. Walk through the three stages on the board: (1) Training -- thousands of labelled cat/dog photos are shown to the model so it can learn visual patterns; (2) The model -- stores those learned patterns as adjustable numbers (weights), not as explicit rules a human wrote; (3) Inference -- a brand-new, unlabelled photo goes in, the model compares it against the patterns it learned, and a label comes out with a confidence score. |
| **Real-world example**  | A photo-sorting app that learned from millions of labelled photos and now sorts a brand-new photo of your own pet without ever having seen that specific photo before.                                                                                                                                                                                                                                                                                                                                                 |
| **In-class activity**   | Students build a simple flowchart (on paper) tracing one photo from "camera captures image" through "model compares patterns" to "label + confidence score displayed," labelling where training happened versus where today's single prediction happens.                                                                                                                                                                                                                                                               |

**Knowledge check 1:** A cat/dog classifier is shown a blurry photo and outputs "Dog -- 54% confidence." What does the 54% most likely tell you?

\(A\) The photo is 54% dog pixels.

**(B) The model is uncertain -- this input only weakly matches the patterns it learned, so the result should be checked rather than trusted blindly.**

\(C\) The app is 54% broken.

***Correct answer: B***

**Knowledge check 2:** Why can't you just open up the trained model and read a list of rules like "if ears are pointy, it's a cat"?

**(A) Because the model stores learned numerical patterns (weights) across many features at once, not a human-readable rule list.**

\(B\) Because the model is encrypted.

\(C\) Because cats don't have rules.

***Correct answer: A***

**Evaluation question:** Using the cat/dog example, explain in your own words what happens during training versus what happens when the finished model sees one new photo. Where in that pipeline could a wrong answer come from?

**Homework (10-15 min):** Pick any AI feature you use and write a 3-step version of its input -\> model -\> output pipeline, naming what you think its "training data" probably was.

**Teacher checklist**

**✓** Separates training-time from prediction-time correctly

**✓** Explains a confidence score as a measure of uncertainty, not literal percentage ownership

**✓** Identifies at least one plausible source of error in the pipeline

**Lecture 4 Traditional Software vs AI + Practical AI Audit**

*Month 1 · AI Foundations & How Modern AI Works · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Compare traditional rule-based programs with AI systems on inputs, logic and failure modes, and conduct a hands-on audit of real apps.                                                                                                                                                                                                                                                                                                                                                      |
| **Key concepts**        | Deterministic rules vs learned patterns · Predictable failure vs probabilistic failure · When to choose each approach                                                                                                                                                                                                                                                                                                                                                                       |
| **Teacher explanation** | Build a two-column comparison live: traditional software (a tax calculator, a traffic light timer) always gives the same output for the same input, and when it fails, it fails the same way every time until a programmer fixes the exact rule. AI systems give probabilistic outputs, can give different confidence levels for near-identical inputs, and their failures are harder to predict -- which is exactly why we need the testing and evaluation habits built up in this course. |
| **Real-world example**  | A fixed shipping-cost calculator (traditional: \$5 under 1kg, \$10 over) versus a product-recommendation engine (AI: ranks items by learned preference patterns, and that ranking can shift as it sees more data).                                                                                                                                                                                                                                                                          |
| **In-class activity**   | Full practical AI audit: students pick 3 real tools/apps and classify each feature as traditional or AI-based, then for each AI feature they must name (a) what data it likely learned from and (b) one way it could fail.                                                                                                                                                                                                                                                                  |

**Knowledge check 1:** A bug is found in a traditional, rule-based tax calculator. What should you expect?

**(A) It will produce the exact same wrong answer every time that same input is given, until the rule is fixed.**

\(B\) It will sometimes be wrong and sometimes right on the same input.

\(C\) It cannot be debugged.

***Correct answer: A***

**Knowledge check 2:** An AI recommendation engine suggests different products to two users who typed the identical search term. Is this a bug?

\(A\) Yes, identical input must always give identical output.

**(B) Not necessarily -- AI systems commonly use additional learned signals (past behaviour, timing) beyond the literal search text, so different results for the same text aren't automatically a defect.**

\(C\) Yes, this proves the system is broken.

***Correct answer: B***

**Evaluation question:** From your audit, pick one AI-based feature you tagged. Explain what evidence told you it was AI rather than rule-based, and describe one realistic way it could give a wrong or unhelpful answer.

**Homework (10-15 min):** Write a half-page audit report on one app of your choice: list 2 traditional features and 2 AI features, and justify each classification with evidence (not a guess).

**Teacher checklist**

**✓** Can state at least 2 real differences between rule-based and AI-based behaviour

**✓** Audit report gives evidence, not guesses, for each classification

**✓** Names a plausible failure mode for an AI feature, not just "it might be wrong"

**Month 2 AI Tools, Safety, Ethics & Responsible AI**

*Allocation: 4 hours \| 4 lectures*

**Lecture 5 Using AI Assistants Effectively**

*Month 2 · AI Tools, Safety, Ethics & Responsible AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Use an AI chat assistant productively for a real task, and recognise when its answer needs to be checked rather than trusted outright.                                                                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Clear task instructions · Giving the assistant context · Verifying answers against a known source · Assistants as a tool, not an authority                                                                                                                                                                                                                                                                                                                                             |
| **Teacher explanation** | Demonstrate live: ask an AI assistant a vague question ("tell me about volcanoes") versus a well-specified one ("explain in 3 bullet points, for a 13-year-old, why Mount Vesuvius erupted in 79 AD, and name one primary source"). Show how the second gets a more usable answer. Then deliberately ask a question you already know the true answer to, so students see the assistant can still be confidently wrong, and practice the habit of checking a claim before acting on it. |
| **Real-world example**  | Using an assistant to summarise a long article into 5 bullet points for revision, then checking one fact from the summary against the original article.                                                                                                                                                                                                                                                                                                                                |
| **In-class activity**   | Each student asks an assistant the same homework-style question twice -- once vaguely, once with clear instructions and context -- and compares the two answers, noting which was more usable and why.                                                                                                                                                                                                                                                                                 |

**Knowledge check 1:** An AI assistant confidently states a historical date that you know, from your textbook, is wrong. What is the correct response?

\(A\) Trust the assistant since it sounds confident.

**(B) Treat the confident tone as no guarantee of accuracy, and go with the verified textbook source, flagging the discrepancy.**

\(C\) Assume the textbook must be outdated.

***Correct answer: B***

**Knowledge check 2:** Which of these prompts is most likely to produce a usable, specific answer?

\(A\) "Tell me about space."

**(B) "Explain, in 4 bullet points suitable for a 13-year-old, why the Moon has no atmosphere, and name one cause."**

\(C\) "Space???"

***Correct answer: B***

**Evaluation question:** Write down one vague question and one well-specified version of the same question. Explain in 2-3 sentences what information you added and why it should produce a better answer.

**Homework (10-15 min):** Use an AI assistant to help plan one real study task (e.g. revising a topic). Write down your exact prompt, the assistant's answer, and one part of the answer you verified independently.

**Teacher checklist**

**✓** Prompt shows clear task, context, and format instructions

**✓** Identifies at least one claim that needed independent verification

**✓** Does not treat a confident-sounding answer as automatically correct

**Lecture 6 AI Safety, Privacy and Security**

*Month 2 · AI Tools, Safety, Ethics & Responsible AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Identify personal and sensitive data that should never be typed into a public AI tool, and explain why.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Key concepts**        | What counts as personal/sensitive data · Where typed data can go (logs, training data, third parties) · Safe vs unsafe AI tool habits                                                                                                                                                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Start with a concrete scenario: a student considers pasting their full name, home address, school ID number and a photo of their report card into a public AI chatbot to get homework help. Walk through what can happen to that text after it's sent -- it may be stored in logs, reviewed by humans for quality checks, or in some tools even used to improve future models -- and why that makes it unsafe to share identity details, passwords, financial information, or other people's private data with a public tool. |
| **Real-world example**  | Asking an assistant to "explain this chemistry concept" is safe; pasting your actual exam answer sheet with your name and roll number on it, into a public tool, is not.                                                                                                                                                                                                                                                                                                                                                      |
| **In-class activity**   | Students review 6 sample prompts and sort them into "safe to send to a public AI tool" and "redact or rewrite first," rewriting the unsafe ones to remove the risky details while keeping the question useful.                                                                                                                                                                                                                                                                                                                |

**Knowledge check 1:** A student wants help debugging a Python error that includes a line with their real email password hardcoded in it. What should they do before pasting the code into an AI tool?

\(A\) Paste it as-is, it's just a chatbot.

**(B) Remove or replace the real password with a placeholder like "MY_PASSWORD" before pasting.**

\(C\) Only paste it if the chatbot promises not to save it.

***Correct answer: B***

**Knowledge check 2:** Why is "the tool said it deletes chats after 30 days" not, by itself, a reason to share sensitive personal data freely?

\(A\) It's always a lie.

**(B) Even with a stated retention policy, the safest habit is to never share data you wouldn't want seen if a policy, setting, or your assumption about it turns out to be wrong.**

\(C\) Chats are never actually deleted by any tool.

***Correct answer: B***

**Evaluation question:** Rewrite this unsafe prompt to be safe while keeping it useful: "My name is \[X\], my student ID is \[Y\], and I got question 4 wrong on my exam -- here's a photo of my answer sheet, what did I do wrong?"

**Homework (10-15 min):** List 5 categories of information you will never paste into a public AI tool, with one real example of each.

**Teacher checklist**

**✓** Correctly identifies sensitive categories (identity, credentials, financial, others' data)

**✓** Rewrite preserves the useful question while removing risky details

**✓** Does not rely on "the tool promised to delete it" as a safety justification

**Lecture 7 Bias, Fairness, Hallucinations and Ethics**

*Month 2 · AI Tools, Safety, Ethics & Responsible AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain how training data can cause biased or unfair AI outputs, and define a hallucination with a concrete example.                                                                                                                                                                                                                                                                                                                                                                      |
| **Key concepts**        | Bias from unrepresentative training data · Fairness across different groups of people · Hallucination: confident but false output · Why these matter ethically                                                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Use a real, well-documented pattern: an image generator asked for "a CEO" or "a doctor" producing images skewed toward one gender or ethnicity far more often than reality, because its training data overrepresented certain groups in those roles. Connect this directly to hallucination: a language model asked for a citation that doesn't exist will often invent a plausible-looking but fake book title, author and page number -- confidently, with no signal that it's made up. |
| **Real-world example**  | An AI assistant inventing a fake scientific paper title and author when asked to cite a source for a claim, stated with the same confident tone as a real citation.                                                                                                                                                                                                                                                                                                                       |
| **In-class activity**   | Students generate 3 outputs from an AI image or text tool using an identical prompt template with only one variable changed (e.g. a profession), and discuss any patterns that emerge across the group's combined results.                                                                                                                                                                                                                                                                |

**Knowledge check 1:** An AI assistant gives you a book title, author and page number for a claim, but the book does not exist. This is best described as:

**(A) A hallucination -- a confident, fabricated answer with no real basis.**

\(B\) A privacy violation.

\(C\) A hardware malfunction.

***Correct answer: A***

**Knowledge check 2:** A hiring-screening AI was trained mostly on resumes from one demographic group and performs worse at fairly ranking other groups' resumes. What is the root cause?

\(A\) The AI is intentionally malicious.

**(B) Unrepresentative training data, which caused the model to learn skewed patterns rather than fair ones.**

\(C\) The resumes were formatted incorrectly.

***Correct answer: B***

**Evaluation question:** Explain the difference between bias and hallucination using one original example of each (not from class). Why does each one require a different kind of fix?

**Homework (10-15 min):** Ask an AI assistant for a citation or statistic on a topic you know well, verify it against a real source, and write 3-4 sentences on whether it hallucinated and how you caught it.

**Teacher checklist**

**✓** Defines bias and hallucination correctly and distinctly

**✓** Gives an original example, not a repeated class example

**✓** Explains verification as the practical defence against hallucination

**Lecture 8 Responsible AI Workshop**

*Month 2 · AI Tools, Safety, Ethics & Responsible AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Apply a responsible-AI checklist (privacy, bias, hallucination-checking, appropriate use) to evaluate a real AI tool end-to-end.                                                                                                                                                                                                                                                                          |
| **Key concepts**        | Consolidating Lectures 5-7 into one evaluation checklist · Appropriate vs inappropriate use cases · Documenting a responsible-use decision                                                                                                                                                                                                                                                                |
| **Teacher explanation** | This is a consolidation workshop, not new theory: give each group a real AI tool and a realistic task. Have them run the full checklist built across the unit -- Is this prompt safe to send (no sensitive data)? Is the output likely biased for this use case? Did we check the output for hallucinated facts? Is this tool appropriate for this task at all, or should a human expert be used instead? |
| **Real-world example**  | Evaluating whether it's appropriate to use a general AI chatbot to get mental-health advice versus to summarise class notes -- same tool, very different appropriateness.                                                                                                                                                                                                                                 |
| **In-class activity**   | Groups complete a structured Responsible AI Decision Sheet for an assigned scenario: tool used, data shared (and whether it was safe), bias risk considered, hallucination check performed, final appropriate-use verdict with reasoning.                                                                                                                                                                 |

**Knowledge check 1:** A group is asked to use an AI tool to get a medical diagnosis for a described symptom. Using the checklist, what is the correct verdict?

\(A\) Appropriate, AI tools are accurate enough for medical diagnosis.

**(B) Inappropriate for a real diagnosis -- a general AI assistant is not a substitute for a qualified medical professional, even if its answer sounds confident.**

\(C\) Appropriate only if the tool says it's 95% confident.

***Correct answer: B***

**Knowledge check 2:** A group used an AI tool to draft a factual summary and skipped the hallucination-check step because "it looked fine." What is wrong with this process?

\(A\) Nothing, a confident-looking answer is reliable.

**(B) Skipping verification means any fabricated fact would go unnoticed and get passed on as if it were true.**

\(C\) The process is fine as long as the summary is short.

***Correct answer: B***

**Evaluation question:** Using your group's Decision Sheet, write a 4-5 sentence justification for your final appropriate-use verdict, citing which specific checklist item most influenced your decision.

**Homework (10-15 min):** Apply the full Responsible AI checklist to one AI tool you personally use regularly, and write up your Decision Sheet as homework, including at least one checklist item that changed how you'll use the tool going forward.

**Teacher checklist**

**✓** Decision Sheet addresses all four checklist areas, not just one

**✓** Verdict is justified with a specific reason, not just "yes/no"

**✓** Shows evidence of actually running a hallucination check, not just asserting one was done

**Unit Exam — Unit 1 — AI Foundations, Safety & Responsible Use**

|              |                                                                                                                                                                                     |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                                     |
| **Coverage** | Lectures 1-8: what AI is, how it works, traditional vs AI software, using assistants effectively, safety/privacy, bias/fairness/hallucinations, and responsible-AI decision-making. |

**Month 3 Python Programming Fundamentals I**

*Allocation: 10 hours \| 10 lectures*

**Lecture 9 Python Setup, IDE and First Program**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Install and run Python in an IDE, and write/execute a first working program.                                                                                                                                                                                                                                                                                  |
| **Key concepts**        | Installing Python · Using an editor (VS Code / Replit) · print() · Running a .py file · Reading an error message                                                                                                                                                                                                                                              |
| **Teacher explanation** | Walk through installing Python (or using a browser-based IDE such as Replit to avoid setup issues), creating a file named hello.py, and running it. Live-type \`print("Hello, World!")\`, run it, then deliberately introduce a typo (e.g. \`pint(...)\`) to show students what a real error message looks like and how to read the line number it points to. |
| **Real-world example**  | A program that prints a personalised greeting using the student's own name, e.g. \`print("Hello, Aarav! Welcome to Python.")\`.                                                                                                                                                                                                                               |
| **In-class activity**   | Each student writes and runs a 3-line program that prints their name, their favourite subject, and a math fact (e.g. \`print(7 \* 6)\`), then intentionally breaks one line to practice reading the resulting error.                                                                                                                                          |

**Knowledge check 1:** Running \`print("Hi")\` produces \`NameError: name 'pint' is not defined\`. What does this tell you?

\(A\) Python is broken.

**(B) There is likely a typo -- \`print\` was probably misspelled as \`pint\` somewhere in the code.**

\(C\) The computer has no internet connection.

***Correct answer: B***

**Knowledge check 2:** Which of these correctly prints the text Hello?

\(A\) print(Hello)

**(B) print("Hello")**

\(C\) print = Hello

***Correct answer: B***

**Evaluation question:** Write a 3-line Python program that prints your name, age, and one hobby, each on a separate line. Then describe what error you'd expect if you forgot the closing quotation mark on one line.

**Homework (10-15 min):** Write and run a program that prints 5 facts about yourself, one per line, using 5 separate \`print()\` statements. Save a screenshot of the successful output.

**Teacher checklist**

**✓** Successfully runs a Python file without help

**✓** Can explain what print() does

**✓** Can read a basic error message and identify roughly where the problem is

**Lecture 10 Variables, Data Types and Type Conversion**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Create variables of different data types and convert between them correctly.                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Variables as named storage · int, float, str, bool · type() · int()/str()/float() conversion · Common TypeError                                                                                                                                                                                                                                 |
| **Teacher explanation** | Introduce variables as labelled boxes that hold a value: \`age = 14\`, \`name = "Riya"\`, \`height = 1.52\`, \`is_student = True\`. Show \`type(age)\` to reveal int, then deliberately run \`print("Age: " + age)\` to trigger a TypeError, and fix it with \`str(age)\`, explaining why Python won't silently glue text and numbers together. |
| **Real-world example**  | A program that stores a student's name (str), age (int), and height in metres (float), then prints a sentence combining all three using proper type conversion.                                                                                                                                                                                 |
| **In-class activity**   | Students build a small "profile card" program with 4 variables of different types and print a combined sentence, fixing the TypeError they'll likely hit on the first attempt.                                                                                                                                                                  |

**Knowledge check 1:** What will \`print("Age: " + 14)\` do?

\(A\) Print "Age: 14"

**(B) Raise a TypeError because you cannot concatenate a string and an int directly.**

\(C\) Print "Age: " and skip the number.

***Correct answer: B***

**Knowledge check 2:** What is the correct fix for the error in the previous question?

**(A) print("Age: " + str(14))**

\(B\) print("Age: ", + 14)

\(C\) print("Age": 14)

***Correct answer: A***

**Evaluation question:** Write code that stores your name and age in two variables, then prints them combined into one sentence without causing a TypeError. Explain why the conversion is necessary.

**Homework (10-15 min):** Write a program with at least one variable of each type (int, float, str, bool) and print a sentence that uses all four correctly, with type conversion where needed.

**Teacher checklist**

**✓** Correctly identifies int/float/str/bool

**✓** Fixes a TypeError using str()/int()/float() rather than guessing

**✓** Uses type() to check a variable's type

**Lecture 11 Operators and Expressions**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Use arithmetic, comparison and logical operators correctly, including operator precedence.                                                                                                                                                                                                                                                                                                         |
| **Key concepts**        | \+ - \* / // % \*\* · == != \> \< \>= \<= · and / or / not · Order of operations                                                                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | Build a simple grade calculator live: \`total = 45 + 38\`, \`percentage = total / 80 \* 100\`. Show the difference between \`/\` (float division) and \`//\` (floor division) with a concrete pair like \`17 / 5\` vs \`17 // 5\`. Then chain a logical condition: \`passed = percentage \>= 40 and attendance \>= 75\`, showing how \`and\`/\`or\` combine multiple comparisons into one boolean. |
| **Real-world example**  | A program that calculates whether a student passes a course based on both a marks threshold AND an attendance threshold -- demonstrating why \`and\` is needed rather than checking each separately.                                                                                                                                                                                               |
| **In-class activity**   | Students build a small eligibility checker (e.g. "can borrow a library book") that combines at least 2 conditions with \`and\`/\`or\` and tests it against 3 different input sets.                                                                                                                                                                                                                 |

**Knowledge check 1:** What does \`17 // 5\` evaluate to?

\(A\) 3.4

**(B) 3**

\(C\) 2

***Correct answer: B***

**Knowledge check 2:** A student needs marks \>= 40 AND attendance \>= 75 to pass. Which expression correctly checks this?

\(A\) marks \>= 40 or attendance \>= 75

**(B) marks \>= 40 and attendance \>= 75**

\(C\) marks \>= 40, attendance \>= 75

***Correct answer: B***

**Evaluation question:** Explain the difference between \`/\` and \`//\` in Python with one concrete numeric example of each, and state what each returns.

**Homework (10-15 min):** Write a program that checks if a number is both even and greater than 10, printing a clear True/False-based message using \`and\`.

**Teacher checklist**

**✓** Correctly distinguishes / from //

**✓** Builds a correct and/or condition for a real scenario

**✓** Understands == is comparison while = is assignment

**Lecture 12 Conditions and Decision Making**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Write correct if/elif/else logic to handle multiple branching outcomes.                                                                                                                                                                                                                                                               |
| **Key concepts**        | if/elif/else · Indentation as structure · Nested conditions · Common off-by-one branch mistakes                                                                                                                                                                                                                                       |
| **Teacher explanation** | Build a grading program live: marks \>= 90 -\> 'A', \>= 75 -\> 'B', \>= 60 -\> 'C', else -\> 'Fail'. Deliberately write the conditions in the wrong order first (checking \>= 60 before \>= 90) to show why elif order matters, then fix it, reinforcing that Python checks conditions top to bottom and stops at the first True one. |
| **Real-world example**  | A grading calculator, or a simple traffic-light simulator that prints "Stop"/"Get Ready"/"Go" based on a colour input string.                                                                                                                                                                                                         |
| **In-class activity**   | Students write a 4-branch grading calculator and deliberately test a boundary value (exactly 90, exactly 60) to confirm their elif order is correct.                                                                                                                                                                                  |

**Knowledge check 1:** Why does condition order matter in an if/elif chain checking marks for grades A/B/C/Fail?

\(A\) It doesn't matter, Python checks all branches.

**(B) Python stops at the first True condition, so checking a looser condition (like \>=60) before a stricter one (like \>=90) would wrongly catch high scorers in the wrong branch.**

\(C\) Order only matters for loops, not conditions.

***Correct answer: B***

**Knowledge check 2:** A student with exactly 90 marks should get an 'A' under \`if marks \>= 90\`. What grade do they get if the code mistakenly uses \`if marks \> 90\` instead?

\(A\) A, no difference.

**(B) They fall through to the next branch (e.g. 'B') because \`marks \> 90\` excludes exactly 90, which is a boundary bug.**

\(C\) An error is raised.

***Correct answer: B***

**Evaluation question:** Explain, with your own example, why testing boundary values (exactly the cutoff number) is an important habit when writing if/elif chains.

**Homework (10-15 min):** Write a 3-branch program that classifies a temperature as 'Cold' (\<15), 'Mild' (15-25), or 'Hot' (\>25), and test it with a boundary value of exactly 15 and exactly 25.

**Teacher checklist**

**✓** elif chain is ordered correctly (strictest first where needed)

**✓** Tests at least one boundary value deliberately

**✓** Understands the difference between \>= and \> in a cutoff

**Lecture 13 Loops**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Use for loops and while loops correctly, including range() and avoiding infinite loops.                                                                                                                                                                                                                                                                                                                      |
| **Key concepts**        | for loop with range() · while loop · break and continue · Infinite loop causes and fixes                                                                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | Start with a for loop counting 1 to 10 using \`range(1, 11)\`, explicitly explaining why \`range(1, 11)\` stops before 11, not after. Then build a while loop that keeps asking for a password until the correct one is entered, and deliberately forget to update a counter variable to produce a real infinite loop on screen, so students see what one looks like and how to stop it (Ctrl+C) and fix it. |
| **Real-world example**  | A while loop that repeatedly asks a user to guess a number until they get it right, versus a for loop that prints the 5-times table using range().                                                                                                                                                                                                                                                           |
| **In-class activity**   | Students write a for loop that sums numbers 1 to 100 using a running-total variable, then write a while loop version of the same task and compare the two approaches.                                                                                                                                                                                                                                        |

**Knowledge check 1:** What does \`range(1, 11)\` produce when looped over?

\(A\) Numbers 1 through 11, including 11.

**(B) Numbers 1 through 10 -- range's second argument is exclusive, not included.**

\(C\) Numbers 0 through 11.

***Correct answer: B***

**Knowledge check 2:** A while loop \`while count \< 10:\` never ends and the program hangs. What is the most likely cause?

**(A) \`count\` is never incremented inside the loop body.**

\(B\) The computer is too slow.

\(C\) while loops can never run more than once.

***Correct answer: A***

**Evaluation question:** Write a while loop that prints numbers 1 to 5 and explain exactly which line, if removed, would turn it into an infinite loop, and why.

**Homework (10-15 min):** Write a for loop that prints the multiplication table (1 to 10) for a number of your choice, and a while loop that counts down from 10 to 1.

**Teacher checklist**

**✓** Understands range()'s exclusive upper bound

**✓** Can identify the missing-increment cause of an infinite loop

**✓** Uses break or continue correctly if required by the task

**Lecture 14 Strings and String Manipulation**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Manipulate strings using indexing, slicing, and common built-in string methods.                                                                                                                                                                                                                                        |
| **Key concepts**        | Indexing \[0\], negative indexing \[-1\] · Slicing \[a:b\] · .upper()/.lower()/.strip()/.split()/.replace() · f-strings                                                                                                                                                                                                |
| **Teacher explanation** | Treat a string as a sequence of characters with numbered positions, starting at 0. Show \`name = "Python"\`, then \`name\[0\]\` ('P'), \`name\[-1\]\` ('n'), \`name\[0:3\]\` ('Pyt'). Introduce f-strings as the clean modern way to build sentences: \`f"Hello, {name}!"\` instead of messy concatenation with \`+\`. |
| **Real-world example**  | Cleaning up messy user input (" JOHN smith ") into a properly formatted name ("John Smith") using .strip(), .lower(), and .title() or capitalize patterns.                                                                                                                                                             |
| **In-class activity**   | Students take a messy raw string (extra spaces, wrong case) and write a short script that cleans it into a presentable format, then use an f-string to build a greeting sentence from it.                                                                                                                              |

**Knowledge check 1:** What does \`"Python"\[0:3\]\` return?

**(A) 'Pyt'**

\(B\) 'ytho'

\(C\) 'Python'

***Correct answer: A***

**Knowledge check 2:** What is the main advantage of \`f"Hello, {name}!"\` over \`"Hello, " + name + "!"\`?

\(A\) There is no difference, both are identical in every way.

**(B) F-strings are generally more readable and let you embed expressions directly inside the string without manual concatenation.**

\(C\) F-strings only work with numbers.

***Correct answer: B***

**Evaluation question:** Given the string " hello WORLD ", write the exact chain of string methods needed to turn it into "Hello World" (trimmed, title case).

**Homework (10-15 min):** Write a script that takes a messy sentence (extra spaces, inconsistent case) and cleans it using at least 3 different string methods, printing the before and after.

**Teacher checklist**

**✓** Correctly uses slicing with the right start/stop boundaries

**✓** Uses at least 2 string methods correctly (not guessed)

**✓** Builds a working f-string

**Lecture 15 Lists and Tuples**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Create, index, slice and modify lists; explain why tuples are immutable and when to use each.                                                                                                                                                                                                                                                                                                                                   |
| **Key concepts**        | List creation and indexing · append()/remove()/sort() · Tuples and immutability · List vs tuple: when to use which                                                                                                                                                                                                                                                                                                              |
| **Teacher explanation** | Build a shopping list live: \`items = \["rice", "milk", "bread"\]\`, then \`items.append("eggs")\`, \`items\[0\]\`, \`items.sort()\`. Contrast with a tuple \`coordinates = (12.9, 77.6)\` and attempt \`coordinates\[0\] = 5\` to show the TypeError that proves tuples can't be changed after creation -- and discuss why that's actually useful for data that should stay fixed (like GPS coordinates or RGB colour values). |
| **Real-world example**  | A to-do list app (list -- items get added/removed/reordered) versus storing a fixed RGB colour value like (255, 0, 0) as a tuple that shouldn't accidentally change.                                                                                                                                                                                                                                                            |
| **In-class activity**   | Students build a list-based task tracker (add, remove, mark items) and separately create a tuple representing something that should never change, then try (and fail) to mutate it to confirm the TypeError.                                                                                                                                                                                                                    |

**Knowledge check 1:** What happens if you run \`coordinates = (12.9, 77.6)\` then \`coordinates\[0\] = 5\`?

\(A\) It works fine, same as a list.

**(B) It raises a TypeError, because tuples are immutable and cannot be changed after creation.**

\(C\) It silently does nothing.

***Correct answer: B***

**Knowledge check 2:** Which data structure would you choose to store a student's 5 quiz scores that may need corrections later?

\(A\) A tuple, since scores shouldn't change.

**(B) A list, since it's mutable and scores may need to be updated or added over time.**

\(C\) A single string.

***Correct answer: B***

**Evaluation question:** Explain, with an original example (not from class), one situation where you would deliberately choose a tuple over a list, and why immutability is an advantage there.

**Homework (10-15 min):** Build a list of your 5 favourite movies, then practice adding one, removing one, and sorting the list alphabetically. Explain each step.

**Teacher checklist**

**✓** Uses append/remove/sort correctly

**✓** Can explain immutability in their own words

**✓** Gives a sensible real-world reason to prefer a tuple over a list in some case

**Lecture 16 Dictionaries and Sets**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Use dictionaries for key-value lookups and sets for removing duplicates/membership checks, and choose correctly between them.                                                                                                                                                                                                                                                                       |
| **Key concepts**        | Dictionary creation and access · keys()/values()/items() · Sets and uniqueness · in for fast membership checks                                                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Build a student record live: \`student = {"name": "Zara", "age": 14, "grade": "8"}\`, access \`student\["name"\]\`, then show \`.get("height", "N/A")\` to safely handle a missing key without crashing. Contrast with a set: \`attendees = {"Zara", "Amit", "Zara"}\` automatically drops the duplicate, and show \`"Amit" in attendees\` as a fast membership check versus scanning a whole list. |
| **Real-world example**  | A dictionary storing a product catalogue (name -\> price) for instant lookup, versus a set used to track which students have already submitted an assignment (no duplicates, fast 'has this person submitted?' checks).                                                                                                                                                                             |
| **In-class activity**   | Students build a small dictionary-based contact book (name -\> phone number) and a set that deduplicates a list of email sign-ups, then measure/compare how each is used.                                                                                                                                                                                                                           |

**Knowledge check 1:** What is the key reason to use a dictionary instead of a list to store \`{"rice": 50, "milk": 30}\`-style data?

\(A\) Dictionaries are always faster to type.

**(B) You need to look values up by a meaningful key (like a product name) instead of by numeric position.**

\(C\) Lists cannot store numbers.

***Correct answer: B***

**Knowledge check 2:** \`attendees = {"Zara", "Amit", "Zara"}\` -- what is len(attendees)?

\(A\) 3

**(B) 2, because sets automatically remove duplicate values.**

\(C\) This raises an error.

***Correct answer: B***

**Evaluation question:** Explain why \`student.get("height", "N/A")\` is safer than \`student\["height"\]\` when you're not sure the key exists, and what would happen with each if the key is missing.

**Homework (10-15 min):** Build a dictionary representing your own weekly timetable (day -\> subject) and a set representing the unique subjects you study, derived from the dictionary's values.

**Teacher checklist**

**✓** Uses correct key-access syntax and .get() with a default

**✓** Explains why sets remove duplicates automatically

**✓** Picks the right structure (dict vs set vs list) for a given scenario with a valid reason

**Lecture 17 Functions and Parameters**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Write reusable functions with parameters, default values and return values.                                                                                                                                                                                                                                                                                                              |
| **Key concepts**        | def and return · Parameters vs arguments · Default parameter values · Why functions reduce repeated code                                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | Start by writing the same 3-line grade calculation three times for three different students to make the repetition visually painful, then refactor it into one function \`def calculate_grade(marks):\` that returns a letter grade, called three times with different arguments. Add a default parameter (\`def greet(name, greeting="Hello"):\`) to show how optional parameters work. |
| **Real-world example**  | A \`calculate_area(length, width)\` function reused for every rectangle in a program, instead of rewriting the same formula repeatedly.                                                                                                                                                                                                                                                  |
| **In-class activity**   | Students refactor a piece of repeated, copy-pasted code (provided) into a single function with parameters, then add one default parameter to make it more flexible.                                                                                                                                                                                                                      |

**Knowledge check 1:** What is the main problem with copy-pasting the same 5 lines of logic into 3 different places in a program instead of writing one function?

\(A\) There is no problem, it's the same thing.

**(B) If the logic needs a fix later, you must find and correct it in every copy, which is error-prone; a function centralises it in one place.**

\(C\) Python runs copy-pasted code slower.

***Correct answer: B***

**Knowledge check 2:** Given \`def greet(name, greeting="Hello"): return f"{greeting}, {name}!"\`, what does \`greet("Zara")\` return?

\(A\) An error, because greeting wasn't supplied.

**(B) "Hello, Zara!" -- the default value is used since greeting wasn't given.**

\(C\) "Zara, Hello!"

***Correct answer: B***

**Evaluation question:** Explain why \`return\` is different from \`print\` inside a function, using an example where you need the function's result stored in a variable for later use.

**Homework (10-15 min):** Write a function \`calculate_bmi(weight, height)\` that returns the BMI value, and call it with 3 different sets of values, printing each result.

**Teacher checklist**

**✓** Function uses return, not just print, when the value is needed later

**✓** Correctly uses a default parameter

**✓** Can explain the repeated-code problem functions solve, in their own words

**Lecture 18 Debugging and Programming Challenge**

*Month 3 · Python Programming Fundamentals I · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Apply systematic debugging (reading tracebacks, isolating the failing line, testing small pieces) to fix broken code under time pressure.                                                                                                                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Reading a traceback bottom-up · print()-based debugging · Isolating one failing piece at a time · Common beginner bug patterns from Lectures 9-17                                                                                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Give students a deliberately broken ~15-line program containing 3-4 realistic bugs drawn from this month's topics (an off-by-one range, a TypeError from missing str(), an indentation mistake in an if block, a typo in a variable name). Model the process: read the traceback from the bottom (the actual error) upward to the line number, isolate just that section, add a temporary print() to inspect a variable's actual value, then fix one bug at a time rather than rewriting everything at once. |
| **Real-world example**  | A traceback ending in \`TypeError: can only concatenate str (not "int") to str\` pointing to line 12 -- the fix is adding str() around the integer, not rewriting the whole program.                                                                                                                                                                                                                                                                                                                         |
| **In-class activity**   | Timed challenge: students receive the same broken program and must find and fix all bugs within a set time, documenting each bug found and its fix in a short bug log.                                                                                                                                                                                                                                                                                                                                       |

**Knowledge check 1:** A traceback shows multiple lines of text. Where should you look first to find the actual cause of the error?

\(A\) The very first line of the whole traceback.

**(B) The bottom of the traceback, which names the actual exception and the specific line it occurred on.**

\(C\) Anywhere, it doesn't matter.

***Correct answer: B***

**Knowledge check 2:** You suspect a variable holds the wrong value partway through a program, but there's no error message. What is the most useful next step?

\(A\) Rewrite the entire program from scratch.

**(B) Insert a temporary print() statement right before the suspect line to inspect the variable's actual value at that point.**

\(C\) Ignore it, since there's no error.

***Correct answer: B***

**Evaluation question:** Describe, step by step, how you would debug a program that runs without crashing but produces the wrong final answer -- where would you add checks, and why there rather than elsewhere?

**Homework (10-15 min):** Take a program you wrote in an earlier lecture, deliberately introduce 2 bugs into a copy of it, and write down the exact debugging steps a classmate would need to find and fix them.

**Teacher checklist**

**✓** Reads the traceback's final line/line-number correctly before guessing

**✓** Uses print()-based isolation rather than rewriting blindly

**✓** Bug log documents the actual fix, not just "fixed it"

**Unit Exam — Unit 2 — Python Fundamentals I**

|              |                                                                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                 |
| **Coverage** | Lectures 9-18: Python setup, variables/types, operators, conditions, loops, strings, lists/tuples, dictionaries/sets, functions, and debugging. |

**Month 4 Python Programming Fundamentals II & Data Science**

*Allocation: 8 hours \| 8 lectures*

**Lecture 19 Functions, Scope and Modular Programming**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain variable scope (local vs global) and organise code into separate, importable modules.                                                                                                                                                                                                                                                                                                                                                                               |
| **Key concepts**        | Local vs global scope · Why global variables are risky · Splitting code into multiple .py files · import                                                                                                                                                                                                                                                                                                                                                                    |
| **Teacher explanation** | Demonstrate a scope bug live: define \`count = 0\` globally, write a function that does \`count = count + 1\` inside it (which creates a \*new local\* variable rather than changing the global one), and show the confusing result. Explain \`global count\` as the explicit fix, but recommend passing values in/out via parameters and return instead, as the safer habit. Then split one program into \`helpers.py\` and \`main.py\`, importing functions across files. |
| **Real-world example**  | A calculator app split into \`operations.py\` (functions: add, subtract, multiply) and \`main.py\` (imports and calls them) instead of one giant file.                                                                                                                                                                                                                                                                                                                      |
| **In-class activity**   | Students take a single large script and refactor it into 2 files, moving at least 2 functions into the helper file and importing them correctly into main.py.                                                                                                                                                                                                                                                                                                               |

**Knowledge check 1:** Inside a function, \`count = count + 1\` where \`count\` is also a global variable -- what happens without \`global count\`?

\(A\) It updates the global variable as expected.

**(B) Python raises an UnboundLocalError, because assigning to \`count\` inside the function makes Python treat it as a new local variable, read before it's set.**

\(C\) It silently does nothing.

***Correct answer: B***

**Knowledge check 2:** Why is passing values through parameters/return generally safer than relying on \`global\`?

\(A\) It isn't safer, global is always better.

**(B) Global variables can be changed from anywhere in the program, making bugs harder to trace; functions with clear inputs/outputs are easier to test and reason about.**

\(C\) global keyword doesn't exist in Python.

***Correct answer: B***

**Evaluation question:** Explain the UnboundLocalError scenario from this lecture in your own words, and give the two possible fixes (global keyword vs refactor to parameters/return), stating which one you'd recommend and why.

**Homework (10-15 min):** Split one of your previous programs into two files: one holding your functions, one that imports and runs them. Submit both files.

**Teacher checklist**

**✓** Can explain local vs global scope correctly

**✓** Successfully imports a function across two files

**✓** Prefers parameters/return over global where appropriate

**Lecture 20 Files, Paths and Exception Handling**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Read and write text files safely, and handle predictable errors using try/except instead of letting the program crash.                                                                                                                                                                                                                                           |
| **Key concepts**        | open()/read()/write()/close() · with open(...) as context manager · try/except/finally · Catching specific exceptions                                                                                                                                                                                                                                            |
| **Teacher explanation** | Write a small program that reads a file that doesn't exist, letting it crash with a FileNotFoundError on screen first. Then wrap it: \`try: ... except FileNotFoundError: print("File not found, check the path.")\`. Introduce \`with open("notes.txt") as f:\` as the standard safe pattern that auto-closes the file even if an error occurs partway through. |
| **Real-world example**  | A notes-saving app that writes user input to a file and, when loading, gracefully tells the user "No saved notes found yet" instead of crashing if the file doesn't exist.                                                                                                                                                                                       |
| **In-class activity**   | Students build a small file-based notes app: write notes to a file, read them back, and wrap the read step in try/except so a missing file produces a friendly message instead of a crash.                                                                                                                                                                       |

**Knowledge check 1:** What is the main advantage of \`with open("file.txt") as f:\` over a plain \`f = open("file.txt")\`?

\(A\) There is no difference.

**(B) The \`with\` block automatically closes the file afterwards, even if an error happens inside the block, preventing file-handle leaks.**

\(C\) \`with\` makes the file read faster.

***Correct answer: B***

**Knowledge check 2:** A program should keep running and show a friendly message if a file is missing, instead of crashing. What is the correct structure?

\(A\) if file exists: open it

**(B) try: open and read the file; except FileNotFoundError: show a friendly message instead of crashing.**

\(C\) Ignore the possibility of a missing file entirely.

***Correct answer: B***

**Evaluation question:** Explain why catching the specific exception \`FileNotFoundError\` is better practice than a bare \`except:\` that catches everything.

**Homework (10-15 min):** Build a program that tries to open a file the user names, and uses try/except to handle both a missing file and, separately, a file that exists but is empty.

**Teacher checklist**

**✓** Uses \`with open(...)\` rather than manual open/close

**✓** Catches a specific exception type, not a bare except

**✓** Program does not crash on the missing-file test case

**Lecture 21 JSON, Dictionaries and Structured Data**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Read and write JSON data, mapping it correctly to Python dictionaries and lists.                                                                                                                                                                                                                                                                                                                                                          |
| **Key concepts**        | JSON as text-based structured data · json.load()/json.dump() · Mapping JSON objects to dicts, arrays to lists · Nested JSON structures                                                                                                                                                                                                                                                                                                    |
| **Teacher explanation** | Show a small JSON file representing a student record with nested data (\`{"name": "Dev", "subjects": \["Math", "Science"\], "address": {"city": "Pune"}}\`), and load it with \`json.load()\`, showing that it becomes a normal Python dict you can index exactly as in Lecture 16. Then save a Python dict back out with \`json.dump()\`, pointing out this round-trip is exactly how most real APIs (covered next month) exchange data. |
| **Real-world example**  | A weather app that receives data from a weather service as JSON text and must parse it into a Python dict before it can read \`data\["temperature"\]\`.                                                                                                                                                                                                                                                                                   |
| **In-class activity**   | Students write a program that builds a dict representing a small product catalogue, saves it to a JSON file with json.dump(), then loads it back and prints one nested value to confirm the round-trip worked.                                                                                                                                                                                                                            |

**Knowledge check 1:** After \`data = json.load(f)\` on a JSON object, what Python type is \`data\`?

\(A\) A string containing the raw JSON text.

**(B) A Python dictionary, with JSON arrays converted to Python lists.**

\(C\) A Python function.

***Correct answer: B***

**Knowledge check 2:** Given \`data = {"address": {"city": "Pune"}}\`, how do you access the city value?

\(A\) data\["city"\]

**(B) data\["address"\]\["city"\]**

\(C\) data.address.city

***Correct answer: B***

**Evaluation question:** Explain why JSON is a useful format for exchanging data between two different programs (e.g. a Python script and a web service), rather than just using plain text.

**Homework (10-15 min):** Create a JSON file representing 3 of your friends (name, age, favourite subject as nested fields), load it in Python, and print a formatted sentence for each person.

**Teacher checklist**

**✓** Correctly parses nested JSON into nested dict/list access

**✓** Successfully performs a full save-then-load round trip

**✓** Explains JSON's role as a structured, language-independent data format

**Lecture 22 Basic Object-Oriented Programming**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Define a simple class with attributes and methods, and create multiple objects (instances) from it.                                                                                                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | class and \_\_init\_\_ · self · Attributes vs methods · Creating multiple instances                                                                                                                                                                                                                                                                                                                                                                                        |
| **Teacher explanation** | Build a \`Student\` class live: \`class Student: def \_\_init\_\_(self, name, grade): self.name = name; self.grade = grade\`, then add a method \`def introduce(self): return f"Hi, I'm {self.name} in grade {self.grade}"\`. Create two different Student objects to show each keeps its own separate data (self refers to "this particular object"), connecting it back to the dictionaries from Lecture 16 as an alternative way to bundle related data with behaviour. |
| **Real-world example**  | A simple \`BankAccount\` class with a balance attribute and deposit()/withdraw() methods, where each customer gets their own independent account object.                                                                                                                                                                                                                                                                                                                   |
| **In-class activity**   | Students define a class representing something personal (a Pet, a Book, a Playlist) with at least 2 attributes and 1 method, then create 2 different instances and print each one's introduce()-style output to show they're independent.                                                                                                                                                                                                                                  |

**Knowledge check 1:** In \`def \_\_init\_\_(self, name, grade): self.name = name\`, what does \`self\` refer to?

\(A\) The class itself, shared by all objects.

**(B) The specific object instance being created/used, so each object keeps its own separate copy of name.**

\(C\) A reserved Python keyword with no real meaning.

***Correct answer: B***

**Knowledge check 2:** You create \`s1 = Student("Zara", 8)\` and \`s2 = Student("Amit", 8)\`. If you then run \`s1.name = "Zoya"\`, what happens to s2.name?

\(A\) It also changes to "Zoya".

**(B) It stays "Amit" -- each instance has its own independent attributes.**

\(C\) Both become "Zoya" because they're the same class.

***Correct answer: B***

**Evaluation question:** Explain, in your own words, the difference between a class and an instance (object), using your own Pet/Book/Playlist example from the activity.

**Homework (10-15 min):** Define a class for something you use daily (e.g. a Playlist with songs added/removed) with at least one method that changes its own data, and demonstrate it with 2 separate objects.

**Teacher checklist**

**✓** \_\_init\_\_ and self used correctly

**✓** Demonstrates 2 instances with independent data

**✓** Defines at least one working method beyond \_\_init\_\_

**Lecture 23 APIs, HTTP and Requests**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Make a basic HTTP GET request to a public API using Python's requests library and extract data from the JSON response.                                                                                                                                                                                                                                                                                  |
| **Key concepts**        | What an API is · HTTP methods (focus on GET) · requests.get() · Status codes (200, 404) · Parsing .json() response                                                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Explain an API as a defined way for one program to ask another program for data or an action, over the internet, using HTTP. Live-demo \`response = requests.get("https://api.example.com/...")\`, check \`response.status_code\` (200 = success, 404 = not found), then \`data = response.json()\` to get a Python dict exactly like Lecture 21, closing the loop between JSON and real network calls. |
| **Real-world example**  | Calling a free public weather API to get today's temperature for a city, by sending a GET request and reading the temperature field out of the returned JSON.                                                                                                                                                                                                                                           |
| **In-class activity**   | Students make a GET request to a provided free/public API, check the status code before trusting the response, and print one specific field extracted from the JSON.                                                                                                                                                                                                                                    |

**Knowledge check 1:** A request returns \`response.status_code == 404\`. What does this tell you?

\(A\) The request succeeded and data was found.

**(B) The requested resource was not found -- you should not try to parse response.json() as if it succeeded.**

\(C\) The internet connection is down.

***Correct answer: B***

**Knowledge check 2:** Why should you check \`response.status_code\` before calling \`response.json()\`?

\(A\) You shouldn't, .json() always works.

**(B) If the request failed (e.g. 404, 500), the response body may not be valid JSON in the shape you expect, so parsing it blindly can crash or give wrong data.**

\(C\) status_code and .json() are unrelated.

***Correct answer: B***

**Evaluation question:** Explain what could go wrong if your program calls \`.json()\` immediately after \`requests.get()\` without ever checking status_code, with a concrete failure scenario.

**Homework (10-15 min):** Using a free public API of your choice, write a script that fetches data, checks the status code, and prints one specific value from the result in a readable sentence.

**Teacher checklist**

**✓** Checks status_code before parsing

**✓** Successfully extracts a specific field from the JSON response

**✓** Can explain what an API call actually does over the network, in plain language

**Lecture 24 NumPy Fundamentals**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Create and manipulate NumPy arrays, and explain why NumPy is faster than plain Python lists for numeric work.                                                                                                                                                                                                                                                                                                                         |
| **Key concepts**        | np.array() · Element-wise operations · Shape and indexing · Why vectorised operations beat Python loops                                                                                                                                                                                                                                                                                                                               |
| **Teacher explanation** | Show the contrast directly: adding 1 to every element of a plain Python list requires a for loop or list comprehension, but \`arr = np.array(\[1,2,3\]); arr + 1\` does it instantly, element-wise, across the whole array in one operation. Briefly explain that NumPy does this fast because it operates on data stored in a compact, uniform block of memory and runs the loop in optimised C code underneath, not in slow Python. |
| **Real-world example**  | Converting a list of 10,000 exam scores into a NumPy array to instantly compute the mean, max, and a scaled (curved) version of every score in one line each, instead of writing manual loops.                                                                                                                                                                                                                                        |
| **In-class activity**   | Students convert a list of sample scores into a NumPy array, then compute mean, max, min and a +5 curve adjustment using array operations (no manual loops).                                                                                                                                                                                                                                                                          |

**Knowledge check 1:** Why is \`np_array + 1\` generally much faster than looping through a plain Python list to add 1 to each element?

\(A\) NumPy arrays are not actually faster.

**(B) NumPy performs the operation on all elements at once using optimised, compiled code, instead of Python interpreting a loop one element at a time.**

\(C\) NumPy arrays only store 1 number.

***Correct answer: B***

**Knowledge check 2:** Given \`arr = np.array(\[10, 20, 30\])\`, what does \`arr.mean()\` return?

**(A) 20.0**

\(B\) 60

\(C\) \[10, 20, 30\]

***Correct answer: A***

**Evaluation question:** Explain, using the exam-scores example, why converting a list to a NumPy array is worthwhile before doing numeric analysis on thousands of values.

**Homework (10-15 min):** Create a NumPy array of 10 numbers of your choice and compute its mean, max, min, and standard deviation using NumPy's built-in methods.

**Teacher checklist**

**✓** Creates and manipulates arrays correctly

**✓** Uses vectorised operations instead of manual loops

**✓** Can explain the speed advantage in their own words

**Lecture 25 Pandas and Data Cleaning**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Load a CSV into a Pandas DataFrame and clean common real-world data problems (missing values, wrong types, duplicates).                                                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | pd.read_csv() · DataFrame basics: head(), info(), describe() · Handling missing values (dropna/fillna) · Removing duplicates                                                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Load a deliberately messy fictional CSV (some blank cells, a duplicate row, a numeric column stored as text) with \`pd.read_csv()\`, run \`.info()\` to spot the problems (wrong dtype, missing values), then fix them step by step: \`.fillna()\` for missing values with a sensible default, \`.astype()\` to fix a numeric column's type, \`.drop_duplicates()\` to remove the duplicate row -- this directly feeds the Month 4 mandatory practical. |
| **Real-world example**  | A fictional CSV of 50 students' marks where 3 rows have a blank marks field, one mark is stored as the text "85 " with a trailing space, and one student row is accidentally duplicated.                                                                                                                                                                                                                                                                |
| **In-class activity**   | Month 4 mandatory practical: students load the provided messy fictional CSV, identify every problem using .info() and .describe(), and write the cleaning code to fix each one, documenting what they found and fixed.                                                                                                                                                                                                                                  |

**Knowledge check 1:** A marks column shows as \`dtype: object\` instead of a number, and \`.describe()\` doesn't calculate its mean. What is the most likely cause?

**(A) The column actually contains text values (e.g. extra spaces, or non-numeric entries) mixed into what should be numbers.**

\(B\) Pandas cannot calculate means, ever.

\(C\) The CSV file is corrupted beyond use.

***Correct answer: A***

**Knowledge check 2:** Why is \`.fillna(0)\` not always the right choice for handling missing marks data?

\(A\) It's always correct; 0 is a universal safe default.

**(B) Filling missing marks with 0 could badly skew the real average downward, misrepresenting students who simply have unrecorded (not zero) marks -- a more honest default (e.g. the column mean, or explicit flagging) is often better.**

\(C\) fillna() doesn't work on numeric columns.

***Correct answer: B***

**Evaluation question:** Using the messy-CSV scenario, explain what you would check first (.info() vs .describe()) and why, before deciding how to clean each problem column.

**Homework (10-15 min):** Given a CSV with at least one missing value, one duplicate row, and one wrong-type column (provided or self-created), write a cleaning script and document each issue found and the fix applied.

**Teacher checklist**

**✓** Uses .info()/.describe() to diagnose before fixing

**✓** Chooses a justified (not default-by-habit) missing-value strategy

**✓** Successfully removes duplicates and fixes the dtype issue

**Lecture 26 Matplotlib, Data Interpretation and Git/GitHub**

*Month 4 · Python Programming Fundamentals II & Data Science · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Create a basic chart from cleaned data, correctly interpret what it shows, and publish a project to GitHub with a README.                                                                                                                                                                                                                                                                                                                                                                                            |
| **Key concepts**        | plt.plot()/plt.bar() · Choosing the right chart type · Reading a chart correctly (not just making one) · git init/add/commit, GitHub repo, README basics                                                                                                                                                                                                                                                                                                                                                             |
| **Teacher explanation** | Using the cleaned marks data from Lecture 25, build a bar chart of average marks per subject, explicitly discussing why a bar chart (not a line chart) suits categorical subject comparisons. Then walk through publishing the whole month's work to GitHub: \`git init\`, \`git add .\`, \`git commit -m "..."\`, creating a repo, pushing, and writing a README that states what the project does, what data it uses, and its limitations -- establishing the publish habit reinforced for the rest of the course. |
| **Real-world example**  | A bar chart comparing average marks across 5 subjects, correctly interpreted as "Science has the highest average, but only by a small margin over Math" rather than a vague "the chart looks good."                                                                                                                                                                                                                                                                                                                  |
| **In-class activity**   | Students chart their cleaned Lecture 25 data, write 2-3 sentences correctly interpreting what the chart shows (a real claim, not a description of colours), then push the whole mini-project to a GitHub repo with a README covering purpose, data source and limitations.                                                                                                                                                                                                                                           |

**Knowledge check 1:** You want to compare average marks across 5 different subjects. Which chart type is most appropriate?

**(A) A bar chart, since you're comparing distinct categories against each other.**

\(B\) A line chart, since line charts are always the default choice.

\(C\) A pie chart of all 50 students' names.

***Correct answer: A***

**Knowledge check 2:** What should a good project README include at minimum?

\(A\) Only the author's name.

**(B) What the project does, what data it uses, and its known limitations.**

\(C\) Nothing, code should speak for itself.

***Correct answer: B***

**Evaluation question:** Look at your own bar chart from the activity and write 2 sentences of genuine interpretation (a real claim about the data) rather than a description of what the chart looks like.

**Homework (10-15 min):** Push this month's cleaned-CSV mini-project (Lecture 25 code + this lecture's chart) to a new GitHub repository with a README describing purpose, data and limitations.

**Teacher checklist**

**✓** Chart type matches the data being compared

**✓** Interpretation states an actual finding, not just a visual description

**✓** GitHub repo exists with a README covering purpose/data/limitations

**Unit Exam — Unit 3 — Python Fundamentals II & Data Science**

|              |                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                |
| **Coverage** | Lectures 19-26: scope/modules, files/exceptions, JSON, OOP basics, APIs/HTTP, NumPy, Pandas data cleaning, and Matplotlib/Git. |

**Month 5 Machine Learning Fundamentals with Python**

*Allocation: 10 hours \| 10 lectures*

**Lecture 27 What Is Machine Learning?**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain machine learning as learning patterns from examples rather than following hand-written rules, with a concrete contrast.                                                                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Rule-based vs learned patterns (recap from Lecture 1, now with code) · Supervised learning preview · Why ML needs examples (data), not instructions                                                                                                                                                                                                                                                                                                |
| **Teacher explanation** | Recall Lecture 1's AI definition and sharpen it specifically for ML: instead of a programmer writing \`if price \> 500: expensive\`, you show the computer thousands of (price, label) examples and let an algorithm find the pattern itself. Preview today's roadmap for the month: features/labels -\> splitting data -\> regression -\> classification -\> clustering -\> evaluation -\> a real built model, each lecture building on the last. |
| **Real-world example**  | Predicting house prices: instead of a human writing a pricing formula, an ML model is shown thousands of past (size, location, price) examples and learns the relationship itself.                                                                                                                                                                                                                                                                 |
| **In-class activity**   | Students compare 2 approaches to the same problem (e.g. detecting spam) side by side: a hand-written rule list versus "show the computer 1000 labelled examples," listing pros/cons of each.                                                                                                                                                                                                                                                       |

**Knowledge check 1:** Which best distinguishes machine learning from traditional rule-based programming?

\(A\) ML programs run faster on all hardware.

**(B) ML learns the mapping from input to output from labelled examples, rather than a human writing that mapping as explicit rules.**

\(C\) ML never makes mistakes.

***Correct answer: B***

**Knowledge check 2:** Why would hand-writing rules to detect spam email become impractical at scale?

\(A\) It wouldn't, rules always scale perfectly.

**(B) Spammers constantly change tactics and legitimate variation is huge, so an exhaustive rule list would need constant rewriting; a model can generalise from examples instead.**

\(C\) Email servers can't run rule-based code.

***Correct answer: B***

**Evaluation question:** Give one example (not from class) of a task better solved by learning from examples than by hand-written rules, and explain why rules would struggle there.

**Homework (10-15 min):** Pick a real prediction task (e.g. predicting if it will rain) and describe what example data you'd need to collect to teach a model to do it.

**Teacher checklist**

**✓** States the rules-vs-learned-patterns distinction correctly

**✓** Gives a genuinely different example from the lecture's

**✓** Can preview what the month will build toward

**Lecture 28 Datasets, Features and Labels**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Identify features and labels in a real dataset and explain the difference between them.                                                                                                                                                                                                                                                                                              |
| **Key concepts**        | Features (inputs) · Labels (the target to predict) · Rows as examples, columns as features · Labelled vs unlabelled data                                                                                                                                                                                                                                                             |
| **Teacher explanation** | Using the Month 4 Pandas skills, load a small fictional housing dataset with columns size_sqft, bedrooms, location, price. Identify size_sqft/bedrooms/location as features (what we know) and price as the label (what we want to predict). Emphasise: every row is one training example, and the model's whole job is learning how the feature columns relate to the label column. |
| **Real-world example**  | In a dataset predicting exam pass/fail, hours_studied and attendance_pct are features; pass_or_fail is the label.                                                                                                                                                                                                                                                                    |
| **In-class activity**   | Students load a provided dataset, use .columns and .head() to inspect it, and correctly label each column as a feature or the label, justifying their choice for the label specifically.                                                                                                                                                                                             |

**Knowledge check 1:** In a dataset with columns \[hours_studied, attendance_pct, pass_or_fail\], which column is the label?

\(A\) hours_studied

**(B) pass_or_fail -- it's the outcome we want the model to predict.**

\(C\) attendance_pct

***Correct answer: B***

**Knowledge check 2:** What does "unlabelled data" mean?

\(A\) Data with no column names at all.

**(B) Data where we have the feature values but don't yet know the correct output/label for those examples.**

\(C\) Data stored in a CSV instead of JSON.

***Correct answer: B***

**Evaluation question:** For a dataset predicting whether a customer will cancel a subscription, list 3 plausible features and state which column would be the label, and why.

**Homework (10-15 min):** Find or invent a small dataset (5+ rows) for a prediction task of your choice, and clearly mark which columns are features and which is the label.

**Teacher checklist**

**✓** Correctly separates features from the label

**✓** Justifies the label choice (it's the thing being predicted)

**✓** Understands each row as one training example

**Lecture 29 Data Preparation and Train/Test Splits**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Split a dataset into training and test sets correctly, and explain why testing on unseen data matters.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Key concepts**        | train_test_split() · Why you never evaluate on training data alone · Typical 80/20 or 70/30 splits · Data leakage risk                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | Use an analogy: if a student only ever practices the exact questions that will be on the exam, a perfect exam score tells you nothing about whether they actually understand the material. Demonstrate \`from sklearn.model_selection import train_test_split\`, splitting features (X) and labels (y) into X_train/X_test/y_train/y_test, and explain that the model only ever sees X_train/y_train during training -- the test set is held back specifically to check real performance on data the model has never seen. |
| **Real-world example**  | Training a model on 400 of 500 available housing records and testing it on the remaining 100 it has never seen, to get an honest estimate of how it will perform on brand-new houses.                                                                                                                                                                                                                                                                                                                                      |
| **In-class activity**   | Students perform a train_test_split on a provided dataset with an 80/20 split, print the resulting shapes, and explain in one sentence why the test set must not be used during training.                                                                                                                                                                                                                                                                                                                                  |

**Knowledge check 1:** Why is it misleading to evaluate a model's accuracy only on the exact data it was trained on?

\(A\) It isn't misleading, that's the standard approach.

**(B) A model can simply memorise the training examples rather than learning a generalisable pattern, so training accuracy alone overstates real-world performance.**

\(C\) Training data is always too small to evaluate anything.

***Correct answer: B***

**Knowledge check 2:** After \`train_test_split(X, y, test_size=0.2)\`, what proportion of the data is reserved for testing?

\(A\) 80%

**(B) 20%**

\(C\) 50%

***Correct answer: B***

**Evaluation question:** Explain, using the exam-practice analogy, why a model achieving 99% accuracy on its training data but 60% on its test data should worry you rather than impress you.

**Homework (10-15 min):** Take a dataset from a previous lecture, split it 80/20 into train/test sets, and write 2-3 sentences explaining what each set will be used for in the lectures ahead.

**Teacher checklist**

**✓** Correctly performs the split with sensible proportions

**✓** Never evaluates using training data as if it were a fair test

**✓** Can explain data leakage/overstated-accuracy risk in their own words

**Lecture 30 Regression**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what regression predicts (a continuous number) and distinguish it from classification.                                                                                                                                                                                                                                                                                                                                                  |
| **Key concepts**        | Regression = predicting a number · Linear regression intuition (best-fit line) · Example: predicting price/score/temperature                                                                                                                                                                                                                                                                                                                    |
| **Teacher explanation** | Plot a handful of (hours_studied, exam_score) points on the board and draw a best-fit line through them by eye, explaining that linear regression finds exactly this line mathematically -- the one that minimises the overall distance between the line and all the real data points. Emphasise the output is a continuous number (e.g. 78.3 marks), not a category -- which is the key distinction from classification, covered next lecture. |
| **Real-world example**  | Predicting a house's price (a number) from its size, or predicting tomorrow's temperature (a number) from today's weather data.                                                                                                                                                                                                                                                                                                                 |
| **In-class activity**   | Students use sklearn's LinearRegression to fit a model on a small provided (hours_studied, exam_score) dataset and use it to predict a score for a new, unseen number of study hours, then sanity-check if the prediction seems reasonable.                                                                                                                                                                                                     |

**Knowledge check 1:** Which of these is a regression problem (predicts a continuous number)?

\(A\) Predicting whether an email is spam or not spam.

**(B) Predicting a house's exact sale price in rupees.**

\(C\) Predicting which of 3 categories a photo belongs to.

***Correct answer: B***

**Knowledge check 2:** A linear regression model predicts a student's exam score as 142 out of 100. What does this suggest?

\(A\) The model is correct, high scores are possible.

**(B) Something is likely wrong -- a prediction outside the valid/possible range is a signal to check the model or data, not to trust it blindly.**

\(C\) The model should be used exactly as-is.

***Correct answer: B***

**Evaluation question:** Explain why predicting "the exact temperature tomorrow" is a regression problem, while predicting "will it rain tomorrow (yes/no)" is not.

**Homework (10-15 min):** Using a small dataset of your choice (e.g. hours studied vs score), train a simple linear regression model and predict a value for one new input, checking whether the prediction seems sensible.

**Teacher checklist**

**✓** Correctly identifies regression tasks vs non-regression tasks

**✓** Successfully fits and predicts with LinearRegression

**✓** Sanity-checks an out-of-range prediction rather than accepting it blindly

**Lecture 31 Classification**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what classification predicts (a category) and build a simple classifier.                                                                                                                                                                                                                                                                                                                                                         |
| **Key concepts**        | Classification = predicting a category/class · Binary vs multi-class · Example classifier (e.g. KNN or logistic regression) · Decision boundary intuition                                                                                                                                                                                                                                                                                |
| **Teacher explanation** | Contrast directly with Lecture 30: instead of predicting a number, classification predicts which bucket something belongs to -- pass/fail (binary), or species A/B/C (multi-class). Walk through a simple K-Nearest-Neighbours intuition visually: a new point is classified based on the majority class among its closest neighbours in the data -- an intuitive, code-free way to understand classification before the sklearn syntax. |
| **Real-world example**  | Classifying an email as spam/not-spam (binary), or classifying a photo as cat/dog/bird (multi-class).                                                                                                                                                                                                                                                                                                                                    |
| **In-class activity**   | Students train a simple classifier (e.g. KNeighborsClassifier) on a small labelled dataset, predict the class of one new unseen example, and explain the result using the nearest-neighbours intuition.                                                                                                                                                                                                                                  |

**Knowledge check 1:** Which of these is a classification problem?

\(A\) Predicting a car's exact resale price.

**(B) Predicting whether a tumour is benign or malignant.**

\(C\) Predicting next month's rainfall in millimetres.

***Correct answer: B***

**Knowledge check 2:** In K-Nearest-Neighbours classification, how does the model decide a new point's class?

\(A\) By calculating an average of all points in the dataset.

**(B) By looking at the K closest existing labelled points and taking the majority class among them.**

\(C\) By picking a class at random.

***Correct answer: B***

**Evaluation question:** Explain, using the KNN intuition, why the choice of K (how many neighbours to look at) could change a prediction's outcome near a boundary between two classes.

**Homework (10-15 min):** Using a provided small labelled dataset, train a simple classifier and test it on 2 new examples, explaining each predicted class using the nearest-neighbours (or equivalent) intuition.

**Teacher checklist**

**✓** Correctly distinguishes classification from regression tasks

**✓** Successfully trains and predicts with a classifier

**✓** Can explain the classification decision in plain language, not just report the output

**Lecture 32 Clustering**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain unsupervised clustering (grouping unlabelled data) and distinguish it from the supervised tasks in Lectures 30-31.                                                                                                                                                                                                                                                                                                                                |
| **Key concepts**        | Unsupervised learning: no labels given · K-Means intuition · Choosing the number of clusters · Use cases: customer segmentation, grouping similar items                                                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | Draw a scatter of unlabelled points on the board that visually form 3 natural groups, and show how K-Means finds those groups by iteratively assigning points to the nearest of K cluster centres, then moving each centre to the average of its assigned points, repeating until stable. Key distinction from Lectures 30-31: there is no label column at all here -- the model discovers structure in the data rather than being told the right answer. |
| **Real-world example**  | Grouping customers into segments (e.g. frequent small spenders vs occasional big spenders) purely from their purchase patterns, with no predefined 'correct' segment labels provided.                                                                                                                                                                                                                                                                     |
| **In-class activity**   | Students run KMeans with k=3 on a small 2-feature unlabelled dataset, plot the resulting clusters with different colours, and write one sentence describing what each discovered group seems to represent.                                                                                                                                                                                                                                                |

**Knowledge check 1:** What is the key difference between clustering (Lecture 32) and classification (Lecture 31)?

\(A\) There is no difference, they are the same technique.

**(B) Classification uses labelled training data to predict a known category; clustering works on unlabelled data to discover groups with no predefined labels.**

\(C\) Clustering only works on text data.

***Correct answer: B***

**Knowledge check 2:** You run K-Means with k=2 on data that actually has 4 natural groups. What is the likely result?

\(A\) K-Means will automatically detect and correct the mismatch to 4 groups.

**(B) K-Means will still force the data into exactly 2 clusters, which may poorly represent the true underlying structure.**

\(C\) The algorithm will fail to run.

***Correct answer: B***

**Evaluation question:** Explain why choosing the right number of clusters (k) matters, and describe what might go wrong if k is chosen too small or too large for a real dataset.

**Homework (10-15 min):** Run K-Means with two different values of k on the same provided dataset, plot both results, and write 2-3 sentences comparing which grouping seems more meaningful and why.

**Teacher checklist**

**✓** Correctly explains unsupervised vs supervised distinction

**✓** Successfully runs and visualises K-Means clusters

**✓** Reasons about choice of k rather than treating it as arbitrary

**Lecture 33 Model Evaluation**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Calculate and interpret accuracy, precision, recall and a confusion matrix for a classification model.                                                                                                                                                                                                                                                                                                                                                   |
| **Key concepts**        | Accuracy and its limits · Confusion matrix (TP/FP/TN/FN) · Precision vs recall trade-off · Why accuracy alone can be misleading                                                                                                                                                                                                                                                                                                                          |
| **Teacher explanation** | Use a deliberately misleading example: a disease-detection model that always predicts 'healthy' scores 98% accuracy on a dataset where only 2% of patients are actually sick -- impressive-looking but useless, since it never catches a real case. Introduce the confusion matrix (True Positive/False Positive/True Negative/False Negative) and show how recall (catching actual positive cases) matters far more than raw accuracy in this scenario. |
| **Real-world example**  | A spam filter with 99% accuracy that still lets through every single real phishing email (0% recall on the dangerous class) -- accuracy alone would hide this failure.                                                                                                                                                                                                                                                                                   |
| **In-class activity**   | Students compute a confusion matrix and precision/recall for a provided set of predictions vs true labels, and write a verdict on whether the model is actually useful for its stated purpose.                                                                                                                                                                                                                                                           |

**Knowledge check 1:** A disease classifier that always predicts 'healthy' scores 98% accuracy on a dataset where 2% of patients are sick. Is this a good model?

\(A\) Yes, 98% accuracy is excellent.

**(B) No -- it never correctly identifies a sick patient (0% recall on the positive class), which defeats the model's actual purpose.**

\(C\) Accuracy is the only metric that matters, so yes.

***Correct answer: B***

**Knowledge check 2:** What does recall measure?

\(A\) The proportion of all predictions that were correct.

**(B) Out of all the actual positive cases, the proportion the model correctly identified.**

\(C\) How fast the model runs.

***Correct answer: B***

**Evaluation question:** Using the disease-detection example, explain why precision and recall together give a more honest picture than accuracy alone, and describe a scenario where you'd prioritise recall over precision.

**Homework (10-15 min):** Given a provided confusion matrix for a model's predictions, calculate accuracy, precision and recall by hand, and write a short verdict on the model's real-world usefulness.

**Teacher checklist**

**✓** Correctly computes precision and recall from a confusion matrix

**✓** Identifies a scenario where accuracy alone is misleading

**✓** Gives a justified usefulness verdict, not just the raw numbers

**Lecture 34 Overfitting and Generalisation**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Identify overfitting from a train-vs-test performance gap and describe at least one way to reduce it.                                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Overfitting: memorising noise instead of learning the real pattern · Underfitting: model too simple · Train accuracy vs test accuracy gap as the diagnostic signal · Simple fixes: more data, simpler model, regularisation                                                                                                                                                                                           |
| **Teacher explanation** | Connect directly back to Lecture 29's train/test split: show a model scoring 99% on training data but only 55% on test data, and explain this gap as the signature of overfitting -- the model memorised quirks specific to the training examples rather than learning the general pattern. Contrast with underfitting, where both scores are low because the model is too simple to capture the real pattern at all. |
| **Real-world example**  | A model memorising that 'house \#237 in the training set costs exactly ₹52,30,000' instead of learning the general size-to-price relationship, so it fails badly on any new house.                                                                                                                                                                                                                                    |
| **In-class activity**   | Students are given train/test accuracy pairs for 3 different models and must diagnose each as overfit, underfit, or well-generalised, with reasoning for each diagnosis.                                                                                                                                                                                                                                              |

**Knowledge check 1:** A model scores 98% training accuracy and 52% test accuracy. What does this gap most likely indicate?

\(A\) The model is performing perfectly.

**(B) Overfitting -- the model has memorised patterns specific to the training data that don't generalise to new, unseen data.**

\(C\) The test set is broken.

***Correct answer: B***

**Knowledge check 2:** A model scores 55% on both training AND test accuracy. What does this suggest?

\(A\) Severe overfitting.

**(B) Likely underfitting -- the model may be too simple to capture the real underlying pattern, since it performs poorly even on data it trained on.**

\(C\) The model is working exactly as intended.

***Correct answer: B***

**Evaluation question:** Explain, using your own example, why a model that performs identically well (or identically badly) on both training and test data tells you something different from a model with a large gap between the two.

**Homework (10-15 min):** Given 3 provided train/test accuracy pairs, diagnose each as overfit, underfit, or well-generalised, and suggest one concrete fix for each problem case.

**Teacher checklist**

**✓** Correctly diagnoses overfitting vs underfitting from the train/test gap

**✓** Suggests a plausible, specific fix rather than a vague one

**✓** Connects the diagnosis back to the Lecture 29 train/test split concept

**Lecture 35 Building an ML Model with Scikit-learn**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Build a complete, working ML pipeline end-to-end: load data, split it, train a model, and evaluate it correctly.                                                                                                                                                                                                                                                                                                                                              |
| **Key concepts**        | Consolidating Lectures 27-34 into one pipeline · sklearn's consistent .fit()/.predict() pattern · Choosing an appropriate metric for the task                                                                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | This lecture is a guided, hands-on consolidation: using a provided fictional dataset, walk the full pipeline live -- load with Pandas (Month 4), identify features/label (Lecture 28), split train/test (Lecture 29), choose regression or classification based on the label type (Lectures 30-31), train with .fit(), predict with .predict(), and evaluate with the correct metric from Lecture 33, checking for the overfitting signature from Lecture 34. |
| **Real-world example**  | A complete pipeline predicting whether a student passes (classification) from study hours and attendance, built and evaluated in one continuous script rather than disconnected snippets.                                                                                                                                                                                                                                                                     |
| **In-class activity**   | Students build their own end-to-end pipeline on a provided dataset different from the lecture's demo, documenting each pipeline stage with a short comment explaining what it does and why.                                                                                                                                                                                                                                                                   |

**Knowledge check 1:** When building an sklearn pipeline, what determines whether you should use a regression model or a classification model?

\(A\) Personal preference.

**(B) Whether the label you're predicting is a continuous number (regression) or a category (classification).**

\(C\) The number of rows in the dataset.

***Correct answer: B***

**Knowledge check 2:** After training a model with .fit(X_train, y_train), what should you do before trusting its performance?

\(A\) Immediately deploy it.

**(B) Evaluate it on X_test/y_test (data it has never seen) using an appropriate metric for the task.**

\(C\) Nothing further is needed once .fit() runs without error.

***Correct answer: B***

**Evaluation question:** Walk through, in order, the 6 pipeline stages you used in your own activity model, explaining what each stage does and why it comes in that order.

**Homework (10-15 min):** Build a complete pipeline (load -\> split -\> train -\> predict -\> evaluate) on a dataset of your choice, with every stage documented in comments.

**Teacher checklist**

**✓** Pipeline stages are in the correct order and each is necessary

**✓** Chooses an appropriate model type for the label

**✓** Evaluates on held-out test data with a sensible metric

**Lecture 36 ML Mini-Project and Practical Assessment**

*Month 5 · Machine Learning Fundamentals with Python · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Independently complete and present a small end-to-end ML project, demonstrating the full Month 5 skill set under practical assessment conditions.                                                                                                                                                                                                                                                                |
| **Key concepts**        | Month 5 mandatory practical: train/evaluate a full ML model independently · Presenting results and limitations clearly                                                                                                                                                                                                                                                                                           |
| **Teacher explanation** | This is the Month 5 mandatory practical, assessed individually: students are given a new fictional dataset they have not seen before and must independently choose the right task type, build the full pipeline, evaluate it honestly, and state at least one real limitation of their model (not just report a number). This mirrors exactly what a junior ML practitioner is asked to do on a first real task. |
| **Real-world example**  | Given a new fictional dataset of café orders, independently deciding whether to predict a number (order total) or a category (will the customer return), and justifying that choice before building anything.                                                                                                                                                                                                    |
| **In-class activity**   | Individual practical assessment: build, evaluate and document a complete pipeline on a provided unseen dataset within the class period, submitting code plus a short written verdict on performance and limitations.                                                                                                                                                                                             |

**Knowledge check 1:** A classmate's practical submission reports "My model got 91% accuracy!" with no other detail. What is missing from a complete evaluation?

\(A\) Nothing, accuracy alone is sufficient.

**(B) Context: what the task actually was, whether accuracy was the right metric for it, train-vs-test comparison, and at least one stated limitation.**

\(C\) The model's file size.

***Correct answer: B***

**Knowledge check 2:** Why does the practical specifically require stating at least one real limitation of your model?

\(A\) It's just a formality with no practical value.

**(B) Because every real model has limitations, and recognising them honestly is what separates responsible use from blind trust in a number.**

\(C\) Because all models are too flawed to be useful at all.

***Correct answer: B***

**Evaluation question:** Summarise your own mini-project in 4-5 sentences: the task, your approach, your evaluation result, and one genuine limitation you identified.

**Homework (10-15 min):** Finalise your mini-project write-up (if not completed in class) and publish the code and a short README to GitHub, following the Lecture 26 documentation habit.

**Teacher checklist**

**✓** Chose an appropriate task type (regression/classification/clustering) independently

**✓** Evaluation uses a metric suited to the task, not just accuracy by default

**✓** States a genuine, specific limitation, not a generic disclaimer

**Unit Exam — Unit 4 — Machine Learning Fundamentals**

|              |                                                                                                                                                                    |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                    |
| **Coverage** | Lectures 27-36: what ML is, features/labels, train/test splits, regression, classification, clustering, evaluation, overfitting, and a full built/evaluated model. |

**Month 6 Computer Vision, NLP & Multimodal AI**

*Allocation: 6 hours \| 6 lectures*

**Lecture 37 Computer Vision Fundamentals**

*Month 6 · Computer Vision, NLP & Multimodal AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain how a digital image is represented as numeric pixel data, and why that representation is what a CV model actually learns from.                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | Images as arrays of pixel values (height x width x colour channels) · Grayscale vs RGB · Why resizing/normalising matters                                                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | Connect directly to Lecture 24's NumPy skills: open a small image and show it's literally a NumPy array of numbers -- e.g. shape (224, 224, 3) for a 224x224 RGB image, where each of the 3 channels holds red/green/blue intensity values 0-255. This demystifies 'the AI looks at the picture' into 'the model receives a big grid of numbers and learns patterns across them,' the same core idea introduced in Lecture 3. |
| **Real-world example**  | A 100x100 pixel colour photo is stored as a 100x100x3 array of numbers -- 30,000 individual values -- which is what the model actually processes, not a 'picture' in any human sense.                                                                                                                                                                                                                                         |
| **In-class activity**   | Students load a sample image, print its NumPy shape and a slice of raw pixel values, and convert it to grayscale, comparing the shape before and after.                                                                                                                                                                                                                                                                       |

**Knowledge check 1:** A colour image has shape (224, 224, 3). What does the 3 represent?

\(A\) 3 copies of the same image.

**(B) The 3 colour channels (red, green, blue) for each pixel.**

\(C\) 3 seconds of video.

***Correct answer: B***

**Knowledge check 2:** Why is resizing all training images to the same dimensions typically required before training a CV model?

\(A\) It isn't required, models accept any size automatically.

**(B) Most CV models expect a fixed input shape, so inconsistent image sizes would break the batch processing and the model's input layer.**

\(C\) Resizing makes images load faster from disk only.

***Correct answer: B***

**Evaluation question:** Explain, in your own words, what it means to say an image classifier 'sees' a photo, grounding your answer in how the image is actually represented as data.

**Homework (10-15 min):** Load 3 images of different sizes, print each one's NumPy shape, and resize all three to a common size, confirming the new shapes match.

**Teacher checklist**

**✓** Correctly interprets an image's shape tuple

**✓** Successfully converts/resizes an image using code, not just description

**✓** Explains 'seeing' in terms of pixel data, not anthropomorphised vision

**Lecture 38 Image Classification, Object Detection and OCR**

*Month 6 · Computer Vision, NLP & Multimodal AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Distinguish image classification, object detection and OCR by what each one actually outputs, and try each on a sample image.                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Classification: one label for the whole image · Object detection: multiple labelled bounding boxes · OCR: extracting text from an image                                                                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | Use one single photo containing a street scene with a shop sign to show all three side by side: a classifier might output just 'street scene'; an object detector draws boxes around 'car,' 'person,' 'sign' individually with coordinates; OCR reads the literal text on the sign into a string. The key teaching point is that these solve different problems and picking the wrong one wastes effort -- you wouldn't use OCR to find where a car is. |
| **Real-world example**  | A warehouse app that uses object detection to count how many boxes are in a photo, and OCR separately to read the shipping label text off one of those boxes.                                                                                                                                                                                                                                                                                           |
| **In-class activity**   | Students run a pretrained classifier, detector and OCR tool (provided via a simple API/library) on the same sample image and write a short comparison of what each one actually returned.                                                                                                                                                                                                                                                               |

**Knowledge check 1:** You need to find exactly where in a photo each of 4 different vehicles is located. Which technique is correct?

\(A\) Image classification, since it labels the whole image.

**(B) Object detection, since it locates and labels multiple individual objects with bounding boxes.**

\(C\) OCR, since it reads text.

***Correct answer: B***

**Knowledge check 2:** A receipt-scanning app needs to pull out the total amount printed on a receipt photo. Which technique fits?

**(A) OCR, to extract the actual text/numbers printed on the receipt.**

\(B\) Clustering.

\(C\) Object detection, to draw a box around the receipt.

***Correct answer: A***

**Evaluation question:** Given a single photo of a classroom, describe what output you'd expect from a classifier, a detector, and OCR respectively, and explain why each differs.

**Homework (10-15 min):** Pick a real photo and describe, in writing, what a classifier, a detector and OCR would each be useful for on that specific photo -- not a generic answer.

**Teacher checklist**

**✓** Correctly matches each technique to its actual output type

**✓** Picks the right technique for a given real task, not just by familiarity

**✓** Avoids describing all three as interchangeable

**Lecture 39 Natural Language Processing Fundamentals**

*Month 6 · Computer Vision, NLP & Multimodal AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain tokenisation and why text must be converted to numbers before any model can process it.                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Tokenisation (splitting text into words/subwords) · Why models need numeric input, not raw text · Vocabulary and token IDs                                                                                                                                                                                                                                                                                                |
| **Teacher explanation** | Connect back to Lecture 37's insight that models process numbers, not human concepts: text has the exact same problem. Show live how a sentence "AI is powerful" gets split into tokens \["AI", "is", "power", "ful"\] (subword tokenisation) and each token is mapped to an integer ID from a fixed vocabulary before any processing happens -- foreshadowing the tokens concept that returns in Month 7's LLM lectures. |
| **Real-world example**  | The word "unbelievable" might be split into subword tokens like \["un", "believ", "able"\] rather than kept as one whole-word token, which lets the model handle rare or new words it hasn't seen as a complete unit before.                                                                                                                                                                                              |
| **In-class activity**   | Students use a provided simple tokeniser to tokenise 3 sentences of their choice and inspect the resulting token list and IDs, noting any surprising splits (e.g. a word broken into unexpected pieces).                                                                                                                                                                                                                  |

**Knowledge check 1:** Why can't a neural network process the raw text "Hello world" directly?

\(A\) It can -- text goes in exactly as typed.

**(B) Neural networks operate on numbers; text must first be tokenised and converted into numeric IDs before any computation can happen.**

\(C\) Networks only accept images.

***Correct answer: B***

**Knowledge check 2:** What is subword tokenisation useful for?

\(A\) It makes text files smaller on disk.

**(B) It lets a model represent rare, new or compound words as combinations of familiar smaller pieces, instead of needing every possible whole word in its vocabulary.**

\(C\) It removes all punctuation permanently.

***Correct answer: B***

**Evaluation question:** Tokenise the sentence "Artificial intelligence is transforming education" by hand into a reasonable guess at word or subword tokens, and explain your reasoning for any word you chose to split.

**Homework (10-15 min):** Using a provided tokeniser tool, tokenise 3 sentences you write yourself and note which tokens surprised you (e.g. a word split in an unexpected place).

**Teacher checklist**

**✓** Explains why raw text can't be fed directly into a model

**✓** Correctly distinguishes tokens from whole words

**✓** Identifies at least one real example of subword splitting from their own test

**Lecture 40 Text Classification, Sentiment and Information Extraction**

*Month 6 · Computer Vision, NLP & Multimodal AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Build and evaluate a basic sentiment classifier, and extract specific entities from text.                                                                                                                                                                                                                                                                                                                                                                       |
| **Key concepts**        | Sentiment analysis as a classification task (links to Lecture 31) · Entity extraction (names, places, dates) · Evaluating NLP output critically, not just reading it                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Frame sentiment analysis explicitly as classification from Lecture 31, just with text features instead of numeric ones: a movie review is classified positive/negative/neutral. Then show entity extraction on a sentence ("Priya met Raj in Mumbai on Tuesday" -\> PERSON: Priya, Raj; LOCATION: Mumbai; DATE: Tuesday), and deliberately test a tricky sarcastic review ("Oh great, another broken feature") to show where sentiment analysis commonly fails. |
| **Real-world example**  | An app that reads product reviews and automatically flags negative ones for a support team to follow up on, while extracting the product name mentioned in each review.                                                                                                                                                                                                                                                                                         |
| **In-class activity**   | Students run a provided sentiment tool on 5 real or sample reviews including at least one sarcastic/ambiguous one, and write up where the tool got it right and where it likely failed.                                                                                                                                                                                                                                                                         |

**Knowledge check 1:** A sentiment tool labels the sarcastic review "Oh great, ANOTHER broken feature" as Positive. What does this reveal?

\(A\) The tool is working perfectly.

**(B) A real limitation -- sarcasm and tone are hard for standard sentiment models, which often key off surface words like "great" without grasping the sarcastic intent.**

\(C\) Sarcasm cannot exist in written text.

***Correct answer: B***

**Knowledge check 2:** What does entity extraction on "Priya met Raj in Mumbai" aim to identify?

\(A\) The overall sentiment of the sentence.

**(B) Specific named things in the text, such as people (Priya, Raj) and places (Mumbai).**

\(C\) Whether the sentence is grammatically correct.

***Correct answer: B***

**Evaluation question:** Using your own sarcastic-review test case, explain specifically why the model got the sentiment wrong, in terms of what surface cues it likely relied on.

**Homework (10-15 min):** Collect or write 5 short reviews/comments, including at least one sarcastic one, run them through a sentiment tool, and write up the accuracy and one clear failure case.

**Teacher checklist**

**✓** Correctly frames sentiment as classification

**✓** Tests at least one deliberately tricky input, not just easy cases

**✓** Identifies a real, specific limitation rather than a generic one

**Lecture 41 Multimodal AI: Text, Images, Audio and Video**

*Month 6 · Computer Vision, NLP & Multimodal AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what makes an AI system multimodal and give a real example combining at least two modalities.                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Modality: text, image, audio, video as distinct data types · Multimodal = processing/relating more than one modality together · Why multimodal models are powerful (and harder to build)                                                                                                                                                                                              |
| **Teacher explanation** | Review Lectures 37 (images) and 39 (text) as two separate modalities each needing their own numeric representation, then show how a multimodal model (e.g. one that answers questions about a photo) must combine both representations meaningfully -- not just run two separate models side by side, but relate the image content to the text question to produce a grounded answer. |
| **Real-world example**  | An app that takes a photo of a fridge's contents and answers the typed question "what can I cook with this?" -- requiring the model to connect visual content (the ingredients seen) with the text task.                                                                                                                                                                              |
| **In-class activity**   | Students try a provided multimodal tool with one image and one related text question, then try the same image with a deliberately unrelated question to see how the model handles a mismatch.                                                                                                                                                                                         |

**Knowledge check 1:** What distinguishes a multimodal AI system from simply running an image model and a text model separately, side by side?

\(A\) There is no real distinction.

**(B) A multimodal system relates information across modalities together (e.g. grounding a text answer in actual image content), rather than processing each in isolation with no connection.**

\(C\) Multimodal systems only work with video.

***Correct answer: B***

**Knowledge check 2:** You ask a multimodal tool about a photo of a cat, but your question is actually about an unrelated topic entirely. What is a responsible expectation?

\(A\) The tool will always correctly realise the mismatch and refuse to answer.

**(B) The tool might still attempt an answer grounded in what it can see, so the output should be checked for relevance, not trusted automatically.**

\(C\) The tool will crash immediately.

***Correct answer: B***

**Evaluation question:** Describe one real app or use case that genuinely needs multimodal AI (not just two separate single-modality tools), and explain why combining modalities specifically matters there.

**Homework (10-15 min):** Try a provided multimodal tool with an image of your choice and 2 different questions about it (one relevant, one irrelevant), and write up what happened with each.

**Teacher checklist**

**✓** Correctly explains multimodal as combining/relating modalities, not just using several tools

**✓** Tests a mismatch case, not only an easy matching case

**✓** Gives a genuine real-use-case example

**Lecture 42 Practical Multimodal AI Application**

*Month 6 · Computer Vision, NLP & Multimodal AI · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Build a small working application combining at least two modalities to accomplish a real task.                                                                                                                                                                                                                                                                                                                                                   |
| **Key concepts**        | Consolidating Lectures 37-41 into one application · Combining a vision/OCR step with a text-generation step                                                                                                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Guide students to build a complete small pipeline: take a photo (e.g. of handwritten or printed notes), run OCR (Lecture 38) to extract the text, then feed that extracted text into a simple text-processing step (e.g. summarise it or classify its topic, from Lecture 40) -- a genuine two-modality pipeline rather than a single-step demo, mirroring how real multimodal apps are commonly built from combined single-modality components. |
| **Real-world example**  | A study-notes app: photograph a page of handwritten notes, OCR extracts the text, then a summarisation step produces 3 bullet-point takeaways from that extracted text.                                                                                                                                                                                                                                                                          |
| **In-class activity**   | Students build and test the OCR-then-text-processing pipeline on 2 different input images, documenting the extracted text, the processing output, and one failure or limitation they observed.                                                                                                                                                                                                                                                   |

**Knowledge check 1:** In the OCR-then-summarise pipeline, what happens if the OCR step misreads a word in the original photo?

\(A\) The error has no effect on anything downstream.

**(B) The mistake propagates forward -- the text-processing step will summarise or classify based on the wrong extracted text, so OCR quality directly limits the whole pipeline's accuracy.**

\(C\) The summarisation step automatically corrects any OCR errors.

***Correct answer: B***

**Knowledge check 2:** Why is building a 2-step pipeline (OCR -\> text processing) a legitimate example of multimodal application, rather than just 'using two separate tools'?

\(A\) It isn't a legitimate example.

**(B) Because the output of the vision step (extracted text) becomes the deliberate input to the text step, meaningfully combining information across modalities toward one task.**

\(C\) Because both steps use the same programming language.

***Correct answer: B***

**Evaluation question:** Describe one failure you observed in your pipeline (e.g. a misread word, or a poor summary caused by it), and trace exactly which stage introduced the error.

**Homework (10-15 min):** Extend your pipeline to a third input image of your choice and document the full extracted text, processed output, and one concrete way you'd improve the pipeline's reliability.

**Teacher checklist**

**✓** Pipeline genuinely chains two modalities together, output to input

**✓** Documents a specific observed failure, tracing its source stage

**✓** Proposes a concrete, specific improvement, not a vague one

**Unit Exam — Unit 5 — Computer Vision, NLP & Multimodal AI**

|              |                                                                                                                                                 |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                 |
| **Coverage** | Lectures 37-42: image representation, classification/detection/OCR, NLP tokenisation, sentiment/entity extraction, and multimodal applications. |

**Month 7 Generative AI, LLMs & Foundation Models**

*Allocation: 8 hours \| 8 lectures*

**Lecture 43 What Is Generative AI?**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what makes generative AI distinct from the classification/regression models built in Month 5, with examples across text, image and audio.                                                                                                                                                                                                                                   |
| **Key concepts**        | Generative vs predictive models (recap nested-circles from Lecture 2) · Generating new content vs predicting a label/number · Foundation models as large, general-purpose generative systems                                                                                                                                                                                        |
| **Teacher explanation** | Return to Lecture 2's nested circles and zoom into the innermost ring. Contrast directly with Month 5: a classifier (Lecture 31) picks from a fixed set of known categories; a generative model produces brand-new output (a sentence, an image, a sound clip) that didn't exist in that exact form before, by sampling from patterns learned across huge amounts of training data. |
| **Real-world example**  | A Month 5 classifier can only ever say 'cat' or 'dog'; a generative image model can produce an entirely new, never-before-seen picture of a cat wearing a hat that was never in its training data in that exact form.                                                                                                                                                               |
| **In-class activity**   | Students generate 3 outputs from a text or image generative tool using the same prompt, and compare the outputs to confirm none are identical -- demonstrating the 'new content, not fixed lookup' property.                                                                                                                                                                        |

**Knowledge check 1:** Why can't a Lecture 31-style classifier ever write an original poem?

\(A\) Classifiers are simply too slow for creative tasks.

**(B) A classifier only selects among a fixed, predefined set of output categories; it has no mechanism to produce novel, open-ended content.**

\(C\) Classifiers don't use Python.

***Correct answer: B***

**Knowledge check 2:** You run the same generative image prompt twice and get two visibly different images. What does this tell you?

\(A\) The tool is broken.

**(B) This is expected -- generative models sample from learned patterns rather than retrieving one fixed stored answer, so outputs can vary run to run.**

\(C\) The second run always ignores the prompt.

***Correct answer: B***

**Evaluation question:** Explain, using your own words and the classifier-vs-generator contrast, why 'select from known options' and 'create new content' require fundamentally different kinds of models.

**Homework (10-15 min):** Generate 3 outputs from the same text prompt using a generative tool, and write 2-3 sentences comparing them and explaining why they differ despite an identical prompt.

**Teacher checklist**

**✓** Correctly distinguishes generative from predictive/classification models

**✓** Demonstrates run-to-run output variation and explains why it happens

**✓** Avoids describing generative models as simply 'looking up' an answer

**Lecture 44 How Large Language Models Work**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain next-token prediction as the core mechanism behind how an LLM generates text, one token at a time.                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Key concepts**        | Next-token prediction · Probability distribution over possible next tokens · Autoregressive generation (feeding output back in)                                                                                                                                                                                                                                                                                                                                                                                          |
| **Teacher explanation** | Connect directly to Lecture 39's tokenisation: an LLM doesn't 'know' a whole sentence in advance -- it predicts one token at a time, picking (or sampling) the most likely next token given everything so far, then feeds that choice back in as part of the new context to predict the next one, repeating until the response is complete. Demonstrate by hand: given "The capital of France is", ask students to guess the probability distribution over a few candidate next tokens (Paris: high, banana: near zero). |
| **Real-world example**  | Typing "Once upon a" into a text predictor and seeing "time" suggested as overwhelmingly likely, versus an unlikely word like "giraffe" -- the same mechanism LLMs use at much larger scale.                                                                                                                                                                                                                                                                                                                             |
| **In-class activity**   | Students manually play 'next-token predictor' on 3 incomplete sentences, ranking 4 candidate next words by estimated likelihood, then compare their rankings with an actual LLM's completion.                                                                                                                                                                                                                                                                                                                            |

**Knowledge check 1:** How does an LLM generate a full paragraph of text?

\(A\) It retrieves the entire paragraph from a database in one step.

**(B) It predicts one token at a time, each time feeding the growing text back in as context for predicting the next token.**

\(C\) It translates the prompt directly into output with no intermediate steps.

***Correct answer: B***

**Knowledge check 2:** Given the prompt "The capital of France is", which next token is the model almost certainly most likely to predict?

\(A\) "banana"

**(B) "Paris"**

\(C\) "purple"

***Correct answer: B***

**Evaluation question:** Explain, step by step, what "autoregressive" generation means, using the "Once upon a time" example to illustrate feeding output back in as new context.

**Homework (10-15 min):** Pick an incomplete sentence, write your own guess at the 3 most likely next tokens with rough probabilities, then compare against what a real LLM actually predicts.

**Teacher checklist**

**✓** Correctly explains one-token-at-a-time generation

**✓** Understands that prior output becomes part of the next prediction's context

**✓** Avoids describing LLM output as retrieved rather than generated

**Lecture 45 Tokens, Context Windows and Model Outputs**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what a context window is, why it has a limit, and what happens when that limit is exceeded.                                                                                                                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | Context window as the model's total 'working memory' in tokens · Prompt + conversation history + output all count toward the limit · Truncation/forgetting when the limit is exceeded                                                                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Build directly on Lecture 44: since every prediction depends on 'everything so far,' that 'everything so far' can't be infinite -- it's capped at a fixed number of tokens, the context window (e.g. 128,000 tokens for some current models). Show concretely that a long conversation, a long document pasted in, and the model's own reply all count against the same shared budget, and that once the limit is hit, the oldest content is typically dropped or the request is rejected. |
| **Real-world example**  | Pasting an entire 300-page book into a chat and asking detailed questions about chapter 2 may fail or give vague answers if the book's size exceeds the model's context window and parts get truncated.                                                                                                                                                                                                                                                                                    |
| **In-class activity**   | Students estimate (using a rough token-per-word rule of thumb) whether a given long document would fit inside a stated context window size, and discuss what practical strategy (summarising first, chunking) would help if it doesn't.                                                                                                                                                                                                                                                    |

**Knowledge check 1:** A user has a very long chat conversation with an AI assistant. Partway through, the assistant seems to 'forget' something said much earlier. What is the most likely cause?

\(A\) The assistant is deliberately lying.

**(B) The conversation has likely exceeded the context window, so the earliest tokens were dropped to make room for newer ones.**

\(C\) This should never happen under any circumstances.

***Correct answer: B***

**Knowledge check 2:** Does a long AI-generated response count against the same context window limit as the user's input?

\(A\) No, output is free and unlimited.

**(B) Yes -- input, conversation history and the model's own output typically all draw from the same total token budget.**

\(C\) Only images count toward the limit, never text.

***Correct answer: B***

**Evaluation question:** Explain why a very long pasted document plus a long back-and-forth conversation could cause an AI assistant to lose track of details mentioned early on, connecting this to the context-window concept.

**Homework (10-15 min):** Estimate the rough token count of a page of text you have (using ~0.75 words per token as a rule of thumb), and write 2-3 sentences on what you'd do differently if you needed to discuss a document 10x that length with an AI assistant.

**Teacher checklist**

**✓** Correctly explains the context window as a shared, finite token budget

**✓** Understands that history, prompt and output all draw from the same budget

**✓** Proposes a sensible practical workaround for oversized input (chunking/summarising)

**Lecture 46 Training, Fine-Tuning and Inference -- Conceptual Overview**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Distinguish pretraining, fine-tuning and inference, and explain why most learners use pretrained models rather than training one from scratch.                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Key concepts**        | Pretraining: learning general language patterns from huge data · Fine-tuning: adapting a pretrained model to a narrower task · Inference: using the already-trained model to answer a new input (what every lecture so far has actually been doing)                                                                                                                                                                                                                                                                                              |
| **Teacher explanation** | Clarify a common confusion directly: every time students have 'used' an AI assistant this course, they were doing inference on an already-trained model, not training one. Explain pretraining as an enormous, expensive, specialist process (processing huge amounts of text over powerful hardware for days/weeks), and fine-tuning as a much smaller follow-up step that adapts an already-pretrained model to a narrower task using a much smaller, focused dataset -- which is realistic for a small team, unlike pretraining from scratch. |
| **Real-world example**  | A general-purpose LLM fine-tuned on a company's own customer-support transcripts to answer in that company's specific tone and product knowledge, without retraining the whole model from zero.                                                                                                                                                                                                                                                                                                                                                  |
| **In-class activity**   | Students sort 5 given scenarios (e.g. 'asking a chatbot a question,' 'training GPT-style model from scratch,' 'adapting a model to legal documents') into pretraining, fine-tuning, or inference.                                                                                                                                                                                                                                                                                                                                                |

**Knowledge check 1:** Every time you've typed a question into an AI chat assistant this course and gotten a reply, what were you doing?

\(A\) Pretraining the model.

**(B) Inference -- using an already-trained model to produce an output for a new input.**

\(C\) Fine-tuning the model permanently.

***Correct answer: B***

**Knowledge check 2:** Why would a small team realistically choose fine-tuning over pretraining a model from scratch?

\(A\) Fine-tuning and pretraining cost exactly the same amount of effort.

**(B) Pretraining from scratch requires enormous data and compute resources; fine-tuning adapts an already-capable pretrained model using a much smaller, focused dataset.**

\(C\) Fine-tuning is illegal for small teams.

***Correct answer: B***

**Evaluation question:** Explain, using the customer-support example, why fine-tuning is a more realistic option than pretraining for most real organisations wanting a specialised AI assistant.

**Homework (10-15 min):** Classify 5 real-world AI scenarios you can think of (not from class) as pretraining, fine-tuning, or inference, with a one-line justification for each.

**Teacher checklist**

**✓** Correctly identifies that normal usage = inference, not training

**✓** Explains the resource difference between pretraining and fine-tuning

**✓** Classifies novel scenarios correctly, not just memorised examples

**Lecture 47 Embeddings and Semantic Similarity -- Introduction**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what an embedding is (a numeric vector representing meaning) and why similar meanings produce similar vectors.                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Key concepts**        | Embeddings as numeric representations of meaning · Similar meaning -\> vectors close together in embedding space · Cosine similarity intuition (not formula-heavy yet)                                                                                                                                                                                                                                                                                                                                                             |
| **Teacher explanation** | Build directly on Lecture 39's tokenisation: tokens get IDs, but IDs alone don't capture meaning ('cat' and 'dog' as plain IDs are no more related than 'cat' and 'car'). Embeddings solve this by representing each word/sentence as a list of numbers (a vector) positioned in a meaning-space, such that semantically similar things end up with similar vectors -- 'cat' and 'dog' end up closer together than 'cat' and 'airplane.' This foundational idea is what Month 9's RAG/vector search will build directly on top of. |
| **Real-world example**  | The sentences "I love my pet dog" and "My puppy is wonderful" would have embeddings that are close together in meaning-space, even though they share almost no identical words.                                                                                                                                                                                                                                                                                                                                                    |
| **In-class activity**   | Students use a provided tool to generate embeddings for 5 short sentences (some similar in meaning, some unrelated) and compute pairwise similarity scores, checking that similar-meaning pairs score higher than unrelated pairs.                                                                                                                                                                                                                                                                                                 |

**Knowledge check 1:** Why would "I love my pet dog" and "My puppy is wonderful" have similar embeddings despite sharing almost no identical words?

\(A\) Embeddings only look at shared letters.

**(B) Embeddings represent meaning, not literal word overlap, so semantically related sentences land close together in the embedding space.**

\(C\) This shouldn't happen; embeddings require exact word matches.

***Correct answer: B***

**Knowledge check 2:** Two sentences about completely unrelated topics (a recipe and a car engine) are embedded. What would you expect their similarity score to be?

\(A\) Very high, since both are text.

**(B) Relatively low, since their meanings are unrelated, even though both are valid English sentences.**

\(C\) Exactly identical.

***Correct answer: B***

**Evaluation question:** Using your activity results, pick one pair of sentences that scored high similarity and one that scored low, and explain in your own words why the embeddings captured that difference correctly.

**Homework (10-15 min):** Write 4 original sentences -- 2 similar in meaning, 2 unrelated -- generate their embeddings with a provided tool, and confirm the similarity scores match your expectation.

**Teacher checklist**

**✓** Correctly explains embeddings as meaning-based, not word-overlap-based

**✓** Successfully computes and compares similarity scores

**✓** Picks a genuinely informative example pair to justify in the evaluation

**Lecture 48 Hallucinations and Model Limitations**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Identify and verify a hallucinated claim from an LLM, building directly on the Lecture 7 definition with LLM-specific detail.                                                                                                                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Hallucination recap and why it happens (predicting plausible tokens, not looking up truth) · Common hallucination triggers: citations, statistics, niche facts, recent events · Practical verification habits                                                                                                                                                                                                                                                                                    |
| **Teacher explanation** | Deepen Lecture 7's definition with the mechanism now available from Lecture 44: because an LLM generates the most statistically plausible next token rather than consulting a verified fact database, it can produce a completely fabricated but fluent-sounding citation, statistic, or event with no internal signal that it's wrong. Demonstrate live by asking an assistant for a specific, obscure statistic or citation, then verifying it against a real source and showing the mismatch. |
| **Real-world example**  | Asking an assistant for the exact publication year and journal of a specific, somewhat obscure research paper, and discovering the year or journal name was fabricated, even though the response was stated with full confidence.                                                                                                                                                                                                                                                                |
| **In-class activity**   | Students ask an assistant for 3 specific factual claims (a date, a statistic, a citation) on a topic of their choice, then independently verify each one, documenting which (if any) were hallucinated.                                                                                                                                                                                                                                                                                          |

**Knowledge check 1:** Why are specific citations, exact statistics, and very recent events especially common hallucination triggers for LLMs?

\(A\) LLMs are specifically programmed to lie about these topics.

**(B) These require precise, verifiable facts the model may not have reliably learned, so it defaults to generating a plausible-sounding but potentially fabricated answer instead of admitting uncertainty.**

\(C\) These topics are technically impossible for any computer to discuss.

***Correct answer: B***

**Knowledge check 2:** An assistant gives a confident, detailed answer to a very specific statistical question. What is the appropriate response?

\(A\) Trust it completely because the detail makes it sound credible.

**(B) Treat the detail and confidence as no guarantee of accuracy, and verify the specific claim against an independent, reliable source.**

\(C\) Assume detailed answers are always hallucination-free.

***Correct answer: B***

**Evaluation question:** From your activity, describe one claim you verified and found to be either accurate or hallucinated, and explain exactly how you checked it.

**Homework (10-15 min):** Ask an AI assistant 3 specific factual questions on a topic you know well, verify each answer independently, and write a short report on the accuracy rate you found.

**Teacher checklist**

**✓** Successfully identifies at least one real or plausible hallucination risk area

**✓** Shows an actual, specific verification process, not just a claim of having checked

**✓** Explains the generation mechanism behind hallucination, not just the definition

**Lecture 49 Comparing Models and AI Services**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Compare 2-3 different AI models/services on a shared task using defined criteria (cost, speed, quality, context window), rather than by reputation alone.                                                                                                                                                                                                                                    |
| **Key concepts**        | Defined comparison criteria · Trade-offs: bigger/slower/costlier isn't always better for a given task · Fit-for-purpose model selection                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Give students the same small task (e.g. summarise the same paragraph) to run through 2-3 different available AI tools/models, and have them score each on 4 defined criteria: output quality for this specific task, response speed, any cost implication, and context window size if relevant to the task -- making the point that the 'best' model is task-dependent, not a fixed ranking. |
| **Real-world example**  | A fast, smaller model might be perfectly adequate (and cheaper) for simple summarisation, while a more capable model is worth the extra cost for a complex multi-step reasoning task.                                                                                                                                                                                                        |
| **In-class activity**   | Students run the identical task through 2-3 tools, fill in a comparison table with the 4 criteria, and write a one-line recommendation for which tool fits this specific task best, and why.                                                                                                                                                                                                 |

**Knowledge check 1:** Why might a smaller, cheaper, faster model be the better practical choice for a simple task, rather than always using the largest available model?

\(A\) Smaller models are never usable for any task.

**(B) If the simpler model's output quality is already sufficient for the task, the larger model's extra cost/latency may not be worth it.**

\(C\) Larger models always produce worse results.

***Correct answer: B***

**Knowledge check 2:** What is the main risk of choosing an AI model/service based purely on brand reputation rather than defined criteria?

\(A\) There is no risk, reputation is a perfectly reliable signal for every task.

**(B) The model that's 'best' in general reputation may not actually be the best fit for your specific task's requirements (cost, speed, context size, quality on that task type).**

\(C\) Reputation-based choices are always technically impossible to make.

***Correct answer: B***

**Evaluation question:** From your comparison table, justify your final recommendation using at least 2 of the 4 defined criteria, not just overall impression.

**Homework (10-15 min):** Pick a real task you might use an AI tool for, compare 2 available tools against it using the same 4 criteria, and write a one-paragraph recommendation.

**Teacher checklist**

**✓** Uses defined criteria consistently across both/all tools compared

**✓** Recommendation is justified by specific criteria, not just general impression

**✓** Recognises that model choice is task-dependent, not a fixed ranking

**Lecture 50 Build a Small Generative AI Application**

*Month 7 · Generative AI, LLMs & Foundation Models · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Build a small, working generative AI application end-to-end, consolidating Lectures 43-49.                                                                                                                                                                                                                                                                                  |
| **Key concepts**        | Consolidating Month 7 into one working app · Handling model output responsibly (verification habit from Lecture 48)                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Guide a complete small build: students design a simple generative application (e.g. a study-flashcard generator that takes a topic and produces Q&A pairs), call a text-generation model with a clear prompt, and -- critically, enforcing the Lecture 48 habit -- manually verify at least 2 of the generated facts before accepting the output as a finished deliverable. |
| **Real-world example**  | A flashcard generator that takes "World War II" as input and produces 5 question/answer pairs, with the student independently verifying 2 of the generated factual answers before trusting the set.                                                                                                                                                                         |
| **In-class activity**   | Students build and run their chosen small generative application, then complete a verification pass on at least 2 generated facts/claims, documenting the process and result.                                                                                                                                                                                               |

**Knowledge check 1:** A student's flashcard generator produces a factually wrong answer in one of its 5 generated question/answer pairs. What does this demonstrate about shipping generative AI output directly?

\(A\) This proves generative AI should never be used for anything.

**(B) It demonstrates exactly why a verification step (Lecture 48) is a required part of the application, not an optional extra.**

\(C\) Generated content is always 100% accurate, so this shouldn't be possible.

***Correct answer: B***

**Knowledge check 2:** What should happen if your verification pass finds one of your app's generated facts is wrong?

\(A\) Ship it anyway since it's just a small error.

**(B) Flag or correct it before presenting the output as finished, and note the issue in your project documentation.**

\(C\) Delete the whole project.

***Correct answer: B***

**Evaluation question:** Describe your application's design in 3-4 sentences, and report the result of your fact-verification pass, including what you did if you found an error.

**Homework (10-15 min):** Finish and publish your Month 7 generative application to GitHub with a README noting the verification steps you performed and any issues you found.

**Teacher checklist**

**✓** Application genuinely generates new content, not a fixed template

**✓** Performs and documents an actual verification pass

**✓** GitHub README follows the Lecture 26 documentation habit

**Unit Exam — Unit 6 — Generative AI, LLMs & Foundation Models**

|              |                                                                                                                                                                                |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                                |
| **Coverage** | Lectures 43-50: generative vs predictive AI, how LLMs generate text, tokens/context windows, training/fine-tuning/inference, embeddings, hallucinations, and model comparison. |

**Month 8 Prompt Engineering & AI Evaluation**

*Allocation: 7 hours \| 7 lectures*

**Lecture 51 Prompt Structure and Clear Instructions**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Write a well-structured prompt with explicit task, role, and constraints, and show the measurable difference versus a vague prompt.                                                                                                                                                                                                                                                                                            |
| **Key concepts**        | Task + role + constraints structure · Specificity reduces ambiguity · Reusing the Lecture 5 vague-vs-specific habit, now formalised                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Formalise the Lecture 5 habit into a repeatable structure: (1) Role -- who should the model act as; (2) Task -- exactly what to produce; (3) Constraints -- length, format, audience, tone. Rewrite a vague prompt ("explain photosynthesis") step by step into a structured one ("Act as a biology tutor. Explain photosynthesis in 4 bullet points for a 13-year-old, using one everyday analogy.") and run both to compare. |
| **Real-world example**  | "Write about dogs" versus "Act as a vet. In 3 bullet points for a new pet owner, explain what a dog needs in its first week home."                                                                                                                                                                                                                                                                                             |
| **In-class activity**   | Students take a vague prompt they wrote in Lecture 5 and rewrite it using the Role+Task+Constraints structure, then run both versions and compare usefulness.                                                                                                                                                                                                                                                                  |

**Knowledge check 1:** Which element is missing from the prompt "Explain climate change"?

\(A\) Nothing is missing, it's complete.

**(B) Role, audience/constraints and output format are all unspecified, making the response's depth and style unpredictable.**

\(C\) The word 'please'.

***Correct answer: B***

**Knowledge check 2:** Why does specifying a role (e.g. "Act as a biology tutor") tend to improve a response's usefulness?

\(A\) It has no real effect on output.

**(B) It helps frame the appropriate tone, depth and vocabulary level for the response.**

\(C\) It makes the model respond faster.

***Correct answer: B***

**Evaluation question:** Rewrite the prompt "Tell me about the French Revolution" using the Role+Task+Constraints structure, specifying an audience and output format.

**Homework (10-15 min):** Pick 2 vague prompts (your own) and rewrite each using the Role+Task+Constraints structure, running both the before and after versions and comparing results.

**Teacher checklist**

**✓** Prompt includes an explicit role, task and constraint

**✓** Can explain why each element improves the response

**✓** Compares before/after rather than only writing the improved version

**Lecture 52 Context, Constraints and Output Formats**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Add relevant background context to a prompt and request a specific output format (e.g. a table or JSON), and verify the format is followed correctly.                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Providing context the model doesn't already have · Requesting structured output (bullets, table, JSON) · Checking the output actually matches the requested format                                                                                                                                                                                                                                                       |
| **Teacher explanation** | Show that a model answering "How should I respond to this email?" with no context guesses blindly, versus pasting the actual email as context first -- producing a grounded, specific answer. Then request output in a specific structure (e.g. "respond only in a 3-column table: Issue \| Cause \| Fix") and demonstrate checking whether the model actually honoured that exact structure, since it sometimes drifts. |
| **Real-world example**  | Asking for a trip itinerary as free-flowing prose versus asking for the same itinerary as a day-by-day table with columns Day \| Activity \| Time -- the table version is far easier to actually use.                                                                                                                                                                                                                    |
| **In-class activity**   | Students provide a real piece of context (a short email, a paragraph of notes) and request output in a specific structured format, then check the result against the exact format requested, fixing the prompt if it drifted.                                                                                                                                                                                            |

**Knowledge check 1:** Why would pasting the actual email text into the prompt produce a better response than just asking "how do I reply to an email" with no context?

\(A\) There is no difference.

**(B) The model can only ground its suggested reply in the specific content, tone and details of that particular email if it's given.**

\(C\) Pasting text always makes responses shorter.

***Correct answer: B***

**Knowledge check 2:** You ask for output as a 3-column table but the model replies in a paragraph instead. What should you do?

\(A\) Accept the paragraph as equivalent.

**(B) Point out the format mismatch and re-request the exact structure, or re-specify the format more explicitly.**

\(C\) Assume tables are impossible for AI to produce.

***Correct answer: B***

**Evaluation question:** Explain why checking that requested output format was actually followed is a necessary step, not an optional nice-to-have, using a scenario where format matters for downstream use (e.g. feeding the output into another program).

**Homework (10-15 min):** Write a prompt that provides real context and requests a specific structured format (table or JSON), run it, and verify whether the format was followed correctly, fixing the prompt if not.

**Teacher checklist**

**✓** Prompt includes genuine, specific context, not generic filler

**✓** Requested output format is explicit and verifiable

**✓** Actually checks the result against the requested format rather than assuming compliance

**Lecture 53 Few-Shot Examples and Structured Responses**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Use few-shot examples inside a prompt to steer the model's output style and format more reliably than instructions alone.                                                                                                                                                                                                                                 |
| **Key concepts**        | Zero-shot vs few-shot prompting · Showing 2-3 input/output examples inside the prompt · Why examples can succeed where instructions alone fail                                                                                                                                                                                                            |
| **Teacher explanation** | Show a case where plain instructions fail to get a consistent output style (e.g. asking for a specific tone of product description), then add 2-3 example input/output pairs directly in the prompt before the real request, demonstrating the model mimics the demonstrated pattern far more reliably than from a text description of the pattern alone. |
| **Real-world example**  | Instead of describing "write playful, short product descriptions," showing 2 actual example product-description pairs in that exact style, then asking for a third in the same style.                                                                                                                                                                     |
| **In-class activity**   | Students take a task where zero-shot prompting produced an inconsistent or wrong-style output, add 2-3 few-shot examples to the same prompt, and compare the consistency of results.                                                                                                                                                                      |

**Knowledge check 1:** Why might showing 2-3 example input/output pairs work better than a long text description of the desired style?

\(A\) Examples are shorter so they're always better.

**(B) Concrete demonstrations let the model directly pattern-match the desired structure/tone, which can be more reliable than an abstract verbal description of style.**

\(C\) Few-shot prompting is identical to zero-shot in every way.

***Correct answer: B***

**Knowledge check 2:** What is "zero-shot" prompting?

**(A) Asking the model to perform a task with no examples given, relying only on instructions.**

\(B\) Providing 10 or more examples before the real request.

\(C\) A prompt that always fails.

***Correct answer: A***

**Evaluation question:** Using your own before/after comparison, explain specifically what changed in the output's consistency once few-shot examples were added, and why.

**Homework (10-15 min):** Design a task where you expect style/format consistency to matter (e.g. consistent tone across 5 generated captions), and compare a zero-shot attempt against a 2-3-shot version.

**Teacher checklist**

**✓** Correctly distinguishes zero-shot from few-shot

**✓** Few-shot examples genuinely match the intended pattern (not sloppy ones)

**✓** Demonstrates a real, observed improvement, not just an assertion of one

**Lecture 54 Prompt Testing and Iterative Improvement**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Systematically test a prompt against multiple inputs, identify failure cases, and iteratively revise the prompt to fix them.                                                                                                                                                                                                                                                                                                              |
| **Key concepts**        | Testing one prompt across several different inputs, not just one lucky example · Diagnosing why a specific input failed · Revising and re-testing (iteration loop)                                                                                                                                                                                                                                                                        |
| **Teacher explanation** | Model the habit directly: take one prompt and deliberately run it against 5 different inputs, including at least one edge case likely to break it (e.g. unusually short input, or an input in a different format than expected). When a failure appears, diagnose specifically why that input broke the prompt, revise the prompt to handle it, and re-test all 5 inputs again to confirm the fix didn't break a previously working case. |
| **Real-world example**  | A summarisation prompt that works well on long articles but produces a nonsensical 'summary' when given a single-sentence input -- revised to add an instruction handling the short-input edge case explicitly.                                                                                                                                                                                                                           |
| **In-class activity**   | Students take a prompt from an earlier lecture, test it against 5 varied inputs including 1 deliberate edge case, diagnose any failure, revise the prompt, and re-test all 5 to confirm the fix.                                                                                                                                                                                                                                          |

**Knowledge check 1:** Why is testing a prompt against only one 'lucky' example a weak evaluation process?

\(A\) It isn't weak, one working example is sufficient proof.

**(B) A prompt that works on one input may fail on edge cases (unusual length, format or content) that weren't tested, giving a false sense of reliability.**

\(C\) Testing multiple inputs is only needed for code, not prompts.

***Correct answer: B***

**Knowledge check 2:** After revising a prompt to fix one failing edge case, what is the correct next step?

\(A\) Ship the revised prompt immediately without further checks.

**(B) Re-test all the original inputs (not just the one that failed) to confirm the fix didn't break a previously working case.**

\(C\) Nothing further is needed once one case is fixed.

***Correct answer: B***

**Evaluation question:** Describe one edge case you found that broke your prompt, your diagnosis of why, and the specific change you made to fix it.

**Homework (10-15 min):** Take any prompt you've written this month, test it on 5 varied inputs including one deliberate edge case, and document your revision process and final re-test results.

**Teacher checklist**

**✓** Tests across multiple inputs, including a genuine edge case

**✓** Diagnosis identifies the specific cause of failure, not a vague guess

**✓** Re-tests previously passing cases after revising, not just the fixed one

**Lecture 55 Hallucination Testing and Fact Verification**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Design a deliberate test to check whether a prompt/model combination is prone to hallucinating on a specific task, and apply a mitigation.                                                                                                                                                                                                                                                                                                                                                                              |
| **Key concepts**        | Deliberately probing for hallucination (not just hoping not to encounter one) · Asking for sources/evidence as a mitigation · Instructing the model to say "I don't know" rather than guess                                                                                                                                                                                                                                                                                                                             |
| **Teacher explanation** | Build directly on Lecture 48, moving from passive noticing to active testing: deliberately ask the model about an obscure or partly fictional topic designed to tempt a hallucination (e.g. a plausible-sounding but nonexistent historical event), and observe whether it confidently answers anyway. Then apply a mitigation: adding an explicit instruction ("If you are not confident this is a real event, say so explicitly rather than guessing") and re-test to see whether that reduces confident fabrication. |
| **Real-world example**  | Asking "Describe the Treaty of Alexandria signed in 1850" (a deliberately invented, nonexistent treaty) to see whether the model fabricates plausible-sounding details rather than flagging uncertainty.                                                                                                                                                                                                                                                                                                                |
| **In-class activity**   | Students design one deliberately tricky, partly-fictional probe question for their chosen topic, run it with and without an explicit "say so if unsure" instruction, and compare the two responses.                                                                                                                                                                                                                                                                                                                     |

**Knowledge check 1:** Why deliberately ask about a fictional or obscure topic instead of only testing with topics you know are well-covered?

\(A\) It's a waste of time since models never hallucinate on obscure topics.

**(B) It stress-tests the specific failure mode (confident fabrication) you're trying to catch, rather than only confirming the easy cases work.**

\(C\) Fictional topics are the only valid thing to ask a model.

***Correct answer: B***

**Knowledge check 2:** Adding the instruction "If you are not confident this is real, say so rather than guessing" is an example of:

**(A) A mitigation that can reduce, though not fully eliminate, confident fabrication on uncertain topics.**

\(B\) A guaranteed, complete fix for all hallucinations.

\(C\) An instruction with no measurable effect.

***Correct answer: A***

**Evaluation question:** Report your probe question's two results (with and without the uncertainty instruction) and assess honestly whether the mitigation measurably helped or not.

**Homework (10-15 min):** Design and run your own fictional-topic probe test with and without an uncertainty-encouraging instruction, and report the comparison honestly, including if the mitigation didn't fully work.

**Teacher checklist**

**✓** Probe question is genuinely designed to tempt fabrication, not an easy real-fact question

**✓** Tests both with and without the mitigation instruction

**✓** Reports results honestly, including partial or no improvement

**Lecture 56 Building an Evaluation Dataset**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Build a small evaluation dataset of test cases with known correct answers, to systematically score a prompt's performance.                                                                                                                                                                                                                                                                                                                                              |
| **Key concepts**        | Evaluation dataset: test inputs + known correct/expected outputs · Why this must be built before you can measure 'improvement' meaningfully · Linking back to Lecture 29's train/test philosophy, now applied to prompts                                                                                                                                                                                                                                                |
| **Teacher explanation** | Draw the parallel explicitly to Lecture 29: just as an ML model needs held-out test data to measure real performance, a prompt needs a fixed set of test cases with known correct answers to measure whether a prompt change is actually an improvement, rather than relying on a gut feeling from one or two examples. Guide students to build 8-10 test cases for their chosen task, each with an input and a clearly correct expected output they can check against. |
| **Real-world example**  | For a math-word-problem-solving prompt, a 10-item evaluation set where each item has a known, verifiably correct numeric answer, so any prompt version can be scored out of 10.                                                                                                                                                                                                                                                                                         |
| **In-class activity**   | Students build an 8-10 item evaluation dataset for a prompt task of their choice, with verified correct answers for each item, ready to use for scoring in Lecture 57.                                                                                                                                                                                                                                                                                                  |

**Knowledge check 1:** Why build a fixed set of test cases with known correct answers before trying to improve a prompt?

\(A\) It's unnecessary, you can just judge improvement by feel.

**(B) Without a fixed, scoreable benchmark, you can't reliably tell whether a prompt change actually improved performance or you just got lucky/unlucky on a different random example.**

\(C\) Evaluation datasets are only used for training ML models, never prompts.

***Correct answer: B***

**Knowledge check 2:** What is the key requirement for each item in a good evaluation dataset?

\(A\) It should be as vague as possible.

**(B) It needs a known, verifiable correct (or clearly acceptable) answer to score against.**

\(C\) It must be identical to every other item.

***Correct answer: B***

**Evaluation question:** Explain the parallel between Lecture 29's ML train/test split and this lecture's prompt evaluation dataset -- what is each one protecting you from believing falsely?

**Homework (10-15 min):** Build a 10-item evaluation dataset (inputs + known correct answers) for a prompt task of your choice, ready to score a prompt against in the next lecture.

**Teacher checklist**

**✓** Every evaluation item has a genuinely verifiable correct answer

**✓** Dataset covers varied cases, not 10 near-identical examples

**✓** Can explain the ML-parallel reasoning behind building this dataset

**Lecture 57 Prompt Evaluation Benchmark Project**

*Month 8 · Prompt Engineering & AI Evaluation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Score 2-3 competing prompt versions against the Lecture 56 evaluation dataset and select the best one with evidence.                                                                                                                                                                                                                         |
| **Key concepts**        | Scoring each prompt version against every evaluation item · Comparing scores objectively rather than by impression · Making a final, evidence-based prompt choice                                                                                                                                                                            |
| **Teacher explanation** | Consolidate Lectures 51-56: students write 2-3 different versions of a prompt for their Lecture 56 task (e.g. one plain, one with few-shot examples, one with explicit constraints), run each version against all 8-10 evaluation items, score each version's accuracy, and select a winner backed by the actual scores rather than a hunch. |
| **Real-world example**  | Testing a plain prompt (6/10 correct), a few-shot version (8/10 correct), and a constraint-heavy version (9/10 correct) against the same benchmark, and selecting the third version with the score as evidence.                                                                                                                              |
| **In-class activity**   | Full benchmark project: students run all prompt versions against every evaluation item, tabulate scores, and write a short justified recommendation naming the winning version and its score.                                                                                                                                                |

**Knowledge check 1:** Prompt A scores 6/10 and Prompt B scores 9/10 on the identical evaluation dataset. Which should you adopt, and why?

\(A\) Prompt A, because it was written first.

**(B) Prompt B, because it demonstrably performs better on the same objective benchmark.**

\(C\) Either, since both are 'pretty good.'

***Correct answer: B***

**Knowledge check 2:** Why must all prompt versions be scored against the exact same evaluation dataset to make a fair comparison?

\(A\) It doesn't matter which test cases each version uses.

**(B) Using different test cases for each version would make the scores incomparable -- you need a controlled, identical benchmark to attribute score differences to the prompt itself.**

\(C\) Fair comparison is impossible for prompts in general.

***Correct answer: B***

**Evaluation question:** Report your benchmark project's final scores for each prompt version and justify your chosen winner using those specific numbers.

**Homework (10-15 min):** If not completed in class, finish scoring all prompt versions against your evaluation dataset and publish your benchmark results and final prompt choice to GitHub with a short README.

**Teacher checklist**

**✓** All versions scored against the identical evaluation dataset

**✓** Final recommendation is justified with actual scores, not impression

**✓** GitHub README documents the benchmark process and result

**Unit Exam — Unit 7 — Prompt Engineering & AI Evaluation**

|              |                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                          |
| **Coverage** | Lectures 51-57: prompt structure, context/format, few-shot examples, iterative testing, hallucination testing, evaluation datasets, and a full prompt benchmark project. |

**Month 9 Context Engineering, Embeddings & RAG**

*Allocation: 8 hours \| 8 lectures*

**Lecture 58 What Is Context Engineering?**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain context engineering as deliberately designing what information surrounds a prompt, distinct from (and broader than) prompt engineering.                                                                                                                                                                                                                                                                   |
| **Key concepts**        | Prompt engineering = wording the instruction well · Context engineering = designing what information the model has access to · Why this matters once answers depend on external knowledge, not just general training                                                                                                                                                                                              |
| **Teacher explanation** | Draw a clear boundary with Month 8: prompt engineering (Lectures 51-57) is about how you phrase the instruction; context engineering is about what information you deliberately supply alongside it -- retrieved documents, conversation history, tool outputs, user profile data -- so the model can answer accurately about things it was never trained on, like a company's private documents or today's date. |
| **Real-world example**  | A support chatbot can't know your specific order status from training alone; context engineering is the system that retrieves your actual order record and inserts it into the prompt before the model answers.                                                                                                                                                                                                   |
| **In-class activity**   | Students take a question an AI assistant could NOT answer correctly from general training alone (e.g. "what's in my own fridge right now") and design, on paper, what specific piece of context would need to be supplied for the model to answer it correctly.                                                                                                                                                   |

**Knowledge check 1:** What is the key difference between prompt engineering and context engineering?

\(A\) There is no real difference, they're the same thing.

**(B) Prompt engineering focuses on how the instruction is worded; context engineering focuses on what external information is supplied alongside it.**

\(C\) Context engineering only applies to image models.

***Correct answer: B***

**Knowledge check 2:** Why can't a general-purpose LLM answer "What's my current account balance?" correctly just from good prompt wording alone?

\(A\) It can, with a sufficiently clever prompt.

**(B) The model was never trained on your specific private account data, so no amount of wording alone supplies that missing information -- the actual balance must be retrieved and provided as context.**

\(C\) Account balance questions are impossible for any AI to answer.

***Correct answer: B***

**Evaluation question:** Using your own designed example, explain exactly what context would need to be supplied, and from where, for the model to answer correctly.

**Homework (10-15 min):** Think of 2 real questions that depend on information outside an LLM's training data, and describe what specific context source would need to be engineered in for each.

**Teacher checklist**

**✓** Correctly distinguishes prompt engineering from context engineering

**✓** Identifies a genuine training-data gap, not a general knowledge question

**✓** Names a plausible real source for the needed context

**Lecture 59 Documents, Chunking and Metadata**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Split a long document into appropriately sized chunks with metadata, and explain why chunk size affects retrieval quality.                                                                                                                                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Why whole documents can't be stuffed into one prompt (Lecture 45 context window link) · Chunking strategies (by paragraph/section, with overlap) · Metadata: source, section, date attached to each chunk                                                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | Connect directly to Lecture 45's context window limit: a 50-page manual can't be pasted whole into most prompts, so it must be split into smaller chunks that can each be retrieved individually when relevant. Demonstrate chunking a sample document by paragraph, discuss why chunks too small lose context and chunks too large waste retrieval budget and dilute relevance, and attach metadata (source file name, section title) to each chunk so retrieved results can be traced back to their origin. |
| **Real-world example**  | A 50-page employee handbook split into roughly 200-400-word chunks, each tagged with its chapter name, so a question about leave policy retrieves just the relevant chunk instead of the whole handbook.                                                                                                                                                                                                                                                                                                      |
| **In-class activity**   | Students chunk a provided multi-page sample document into reasonably sized pieces with overlap, attach simple metadata (section name) to each chunk, and justify their chosen chunk size.                                                                                                                                                                                                                                                                                                                     |

**Knowledge check 1:** Why can't a 50-page document simply be pasted whole into every prompt that needs to reference it?

\(A\) There's no reason not to, it's always fine.

**(B) It would likely exceed the context window (Lecture 45) and waste most of the budget on irrelevant sections for any specific question.**

\(C\) Documents longer than 1 page are technically unreadable by any model.

***Correct answer: B***

**Knowledge check 2:** What is a risk of making document chunks too small (e.g. splitting by single sentence)?

\(A\) No risk at all, smaller is always better.

**(B) Each chunk may lose important surrounding context, making retrieved pieces hard to understand or answer from in isolation.**

\(C\) Small chunks always retrieve faster with perfect accuracy.

***Correct answer: B***

**Evaluation question:** Explain your chosen chunk size and overlap strategy from the activity, and justify why it balances context-preservation against retrieval precision.

**Homework (10-15 min):** Take a document of your own (an article, a set of notes) and chunk it into sensible pieces with metadata tags, documenting your reasoning for the chunk size chosen.

**Teacher checklist**

**✓** Chunk size is justified, not arbitrary

**✓** Metadata correctly tags each chunk's source/section

**✓** Explains the context-window link to why chunking is needed at all

**Lecture 60 Embeddings and Semantic Search**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Embed a set of document chunks and retrieve the most relevant ones for a query using semantic similarity, building directly on Lecture 47.                                                                                                                                                                                                                                                                                                                          |
| **Key concepts**        | Embedding chunks (from Lecture 59) instead of whole documents · Embedding the query the same way · Retrieving by similarity rather than exact keyword match                                                                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Extend Lecture 47 directly: instead of embedding single sentences for a demo, embed every chunk from Lecture 59's document, then embed an incoming user query the same way, and retrieve the chunks whose embeddings are most similar to the query's -- explicitly contrasting this with old-style keyword search, which would miss a relevant chunk that uses different wording for the same meaning (e.g. query says 'vacation days,' chunk says 'annual leave'). |
| **Real-world example**  | A query "how many vacation days do I get" correctly retrieves a chunk discussing "annual leave entitlement," even though no words match exactly -- something keyword search would likely miss.                                                                                                                                                                                                                                                                      |
| **In-class activity**   | Students embed the chunks from their Lecture 59 document plus a test query using different wording than the document, and confirm semantic search retrieves the right chunk despite the wording mismatch.                                                                                                                                                                                                                                                           |

**Knowledge check 1:** A query asks about "vacation days" and the correct answer chunk only uses the phrase "annual leave entitlement." Why would semantic search still retrieve it, while basic keyword search might not?

**(A) Semantic search matches based on meaning similarity in embedding space, not exact word overlap.**

\(B\) Semantic search always requires identical wording too.

\(C\) This is not actually possible with any search method.

***Correct answer: A***

**Knowledge check 2:** In semantic search, what exactly is compared to decide which chunks to retrieve?

\(A\) The file sizes of each chunk.

**(B) The similarity between the query's embedding and each chunk's embedding.**

\(C\) The alphabetical order of chunk titles.

***Correct answer: B***

**Evaluation question:** Using your own wording-mismatch test, explain why semantic search succeeded (or, if it failed, what might have caused that), connecting it back to the embeddings concept from Lecture 47.

**Homework (10-15 min):** Write 3 queries using deliberately different wording than your source document's actual phrasing, and confirm whether semantic search still retrieves the correct chunks for each.

**Teacher checklist**

**✓** Successfully embeds both chunks and query consistently

**✓** Demonstrates at least one correct wording-mismatch retrieval

**✓** Explains the similarity-based retrieval mechanism, not just reports a result

**Lecture 61 Vector Search and Retrieval**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Store chunk embeddings in a vector index and retrieve the top-k most relevant chunks efficiently for a query.                                                                                                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Vector index/database as efficient storage for embeddings · top-k retrieval · Why a vector index matters at scale (thousands+ of chunks)                                                                                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Build on Lecture 60 at scale: comparing a query's embedding against 20 chunks by hand is feasible, but against 50,000 chunks it isn't practical to brute-force compare one by one in real time -- introduce a vector index/database as the structure that makes this retrieval fast even at large scale, and top-k (e.g. top 3) as the practical choice of how many chunks to pull back per query rather than returning everything above an arbitrary threshold. |
| **Real-world example**  | A company's 10,000-document knowledge base stored in a vector index, retrieving only the top 3 most relevant chunks per user question instead of scanning the whole base each time.                                                                                                                                                                                                                                                                              |
| **In-class activity**   | Students store a batch of chunk embeddings (from Lecture 59-60's document) in a provided simple vector index tool, run several queries, and inspect the top-k results and their similarity scores.                                                                                                                                                                                                                                                               |

**Knowledge check 1:** Why is a vector index/database used instead of just comparing a query embedding to every stored chunk embedding one by one, especially at scale?

\(A\) There's no real benefit, both approaches perform identically.

**(B) A vector index is structured to make similarity search efficient even across very large numbers of embeddings, which naive one-by-one comparison can't scale to.**

\(C\) Vector indexes only work with images.

***Correct answer: B***

**Knowledge check 2:** What does "top-k retrieval" with k=3 mean in this context?

**(A) Retrieve exactly 3 chunks: the 3 most similar to the query.**

\(B\) Retrieve every chunk with any similarity above zero.

\(C\) Retrieve chunks in alphabetical order.

***Correct answer: A***

**Evaluation question:** Explain, using your own query's results, what the similarity scores of your top-k results tell you about how confidently relevant each retrieved chunk actually is.

**Homework (10-15 min):** Run 3 different queries against your stored chunk index with k=3, and write up which retrieved chunks seemed genuinely relevant versus borderline, using the similarity scores as evidence.

**Teacher checklist**

**✓** Successfully stores and queries a vector index

**✓** Correctly interprets top-k as a fixed retrieval count, not a threshold

**✓** Uses similarity scores to judge result relevance, not just accepts them blindly

**Lecture 62 RAG Architecture**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Diagram and explain the full RAG (retrieval-augmented generation) pipeline end to end, connecting every prior lecture in the unit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Full pipeline: query -\> embed -\> retrieve top-k chunks -\> insert into prompt as context -\> generate answer · Why RAG reduces (but doesn't eliminate) hallucination · Grounded vs ungrounded generation                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | Draw the complete pipeline on the board, explicitly naming which earlier lecture built each piece: user query (new) -\> embed the query (Lecture 60) -\> retrieve top-k relevant chunks from the vector index (Lecture 61) -\> insert those chunks into the prompt as context (Lecture 58's context engineering) -\> the LLM generates an answer grounded in that retrieved context (Lecture 44's generation, now with real supplied facts instead of relying on training alone). Explicitly state that RAG reduces hallucination risk on the specific retrieved facts, but doesn't eliminate it entirely -- the model can still misread or embellish the retrieved context. |
| **Real-world example**  | A company support assistant that retrieves the actual current return-policy document chunk before answering a customer's question, rather than relying on the model's possibly outdated general training knowledge.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **In-class activity**   | Students draw the full RAG pipeline diagram from memory, labelling each stage with which earlier lecture's skill it uses, then explain in writing why this architecture reduces (not eliminates) hallucination risk.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

**Knowledge check 1:** In a RAG pipeline, what is inserted into the prompt before the LLM generates its final answer?

\(A\) Nothing extra, RAG is identical to a plain prompt.

**(B) The top-k chunks retrieved as most relevant to the query, supplying grounding context the model wasn't necessarily trained on.**

\(C\) A random sample of unrelated documents.

***Correct answer: B***

**Knowledge check 2:** Does RAG completely eliminate the risk of hallucination?

\(A\) Yes, RAG makes hallucination impossible.

**(B) No -- it reduces the risk by grounding answers in retrieved facts, but the model can still misinterpret, misquote or embellish that retrieved context.**

\(C\) RAG has no effect on hallucination at all.

***Correct answer: B***

**Evaluation question:** Explain, stage by stage, what would go wrong with the final answer's accuracy if the retrieval stage (Lecture 61) returned the wrong chunks for a query.

**Homework (10-15 min):** Draw your own labelled RAG pipeline diagram and write a short paragraph explaining, in your own words, why each stage is necessary and what would break if it were removed.

**Teacher checklist**

**✓** Diagram correctly orders all pipeline stages

**✓** Explains the grounding benefit accurately, without overclaiming hallucination is eliminated

**✓** Connects each stage to the specific earlier lecture that built that skill

**Lecture 63 Building a Simple RAG Pipeline**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Implement a working RAG pipeline end to end in code, from a document to a grounded generated answer.                                                                                                                                                                                                                                                                                                                         |
| **Key concepts**        | Consolidating Lectures 58-62 into working code · Wiring chunking, embedding, retrieval and generation together                                                                                                                                                                                                                                                                                                               |
| **Teacher explanation** | Guided, hands-on build: starting from a provided sample document, students write the code to chunk it (Lecture 59), embed the chunks and store them (Lectures 60-61), accept a user query, retrieve the top-k relevant chunks, insert them into a prompt template, and call a generation model to produce the final grounded answer -- the complete architecture from Lecture 62, now as working code rather than a diagram. |
| **Real-world example**  | A working mini-assistant that answers questions about a provided school policy document by retrieving the relevant section and generating an answer grounded in it.                                                                                                                                                                                                                                                          |
| **In-class activity**   | Students build and run their own RAG pipeline on the provided document, testing it with 3 different questions and checking each answer is actually grounded in a retrieved chunk (not just a plausible-sounding guess).                                                                                                                                                                                                      |

**Knowledge check 1:** After generating an answer in your RAG pipeline, how do you check it's actually grounded in the retrieved context rather than invented?

\(A\) Trust it automatically since RAG is used.

**(B) Compare the answer's specific claims against the actual retrieved chunk text to confirm they match what was really retrieved.**

\(C\) Grounding cannot be checked.

***Correct answer: B***

**Knowledge check 2:** Your RAG pipeline answers a question correctly for 2 test queries but gives an oddly generic answer for a third. What should you check first?

\(A\) Assume the model is broken and restart the whole project.

**(B) Check what chunks were actually retrieved for that third query -- the retrieval step may have failed to find a relevant chunk, forcing the model to answer with no real grounding.**

\(C\) Ignore it, 2 out of 3 is good enough.

***Correct answer: B***

**Evaluation question:** Walk through what happened for one of your 3 test questions: what was retrieved, and how you confirmed (or failed to confirm) the final answer was properly grounded in it.

**Homework (10-15 min):** Test your RAG pipeline with 2 additional questions, including one you suspect it might struggle with, and document the retrieved chunks and whether the final answer was properly grounded.

**Teacher checklist**

**✓** Pipeline runs end-to-end without manual intervention

**✓** At least one grounding check is actually performed, not assumed

**✓** Diagnoses a weak/generic answer by inspecting retrieval, not by guessing

**Lecture 64 Evaluating Retrieval and Answers**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Evaluate a RAG pipeline's retrieval quality and answer quality separately, since each can fail independently.                                                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Retrieval evaluation: did the right chunk get retrieved? · Answer evaluation: is the final answer correct and grounded? · Why these two failure modes must be diagnosed separately                                                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Make the key diagnostic point explicit: a RAG pipeline can fail in two independent ways -- the retrieval step might pull the wrong (or no) relevant chunk, or the retrieval might be correct but the generation step still produces a wrong or ungrounded answer anyway. Build an evaluation set (echoing Lecture 56) of query/expected-chunk/expected-answer triples, and score retrieval accuracy and answer accuracy as two separate numbers, not one blended score. |
| **Real-world example**  | A RAG pipeline that retrieves the exact correct policy chunk but then generates an answer that contradicts it -- a generation-stage failure, not a retrieval-stage one, requiring a different fix (prompt/context instructions, not better chunking).                                                                                                                                                                                                                   |
| **In-class activity**   | Students build a small evaluation set of 5-8 query/expected-chunk/expected-answer triples for their Lecture 63 pipeline, and score retrieval accuracy and answer accuracy separately, diagnosing any mismatches.                                                                                                                                                                                                                                                        |

**Knowledge check 1:** A RAG pipeline retrieves the exactly correct chunk for a query, but the final generated answer still contradicts that chunk's actual content. Where is the real problem?

\(A\) In the retrieval stage -- the wrong chunk was found.

**(B) In the generation stage -- the correct context was provided, but the model failed to use it faithfully.**

\(C\) There is no problem if retrieval was correct.

***Correct answer: B***

**Knowledge check 2:** Why score retrieval accuracy and answer accuracy as two separate numbers instead of one combined score?

\(A\) Separating them has no diagnostic value.

**(B) Because the two stages can fail independently, and a single blended score would hide which specific stage needs fixing.**

\(C\) Combined scores are always more informative.

***Correct answer: B***

**Evaluation question:** From your evaluation results, report your retrieval accuracy and answer accuracy separately, and identify which stage (if either) needs improvement and why.

**Homework (10-15 min):** Add 3 more query/expected-chunk/expected-answer triples to your evaluation set, re-score both metrics, and write a short diagnosis of your pipeline's weakest stage.

**Teacher checklist**

**✓** Scores retrieval and answer quality as genuinely separate metrics

**✓** Correctly attributes a specific failure to the right stage

**✓** Evaluation set has verifiable expected chunks/answers, not vague ones

**Lecture 65 RAG Knowledge Assistant Project**

*Month 9 · Context Engineering, Embeddings & RAG · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Build, evaluate and present a complete RAG-based knowledge assistant on a self-chosen document set, consolidating the full Month 9 unit.                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Full consolidation: chunking, embeddings, retrieval, generation, grounding evaluation · Presenting limitations honestly                                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | This is the Month 9 capstone project: students choose their own small document set (class notes, a hobby topic, a short guide), build the complete RAG pipeline from Lecture 63's pattern, run the two-metric evaluation from Lecture 64, and present their assistant along with an honest account of at least one real limitation they found (a retrieval miss, a grounding failure, or a chunking issue). |
| **Real-world example**  | A personal RAG assistant built over a student's own revision notes for one subject, correctly answering specific questions by retrieving and grounding on the actual notes rather than guessing from general knowledge.                                                                                                                                                                                     |
| **In-class activity**   | Students finalise their RAG knowledge assistant, run their evaluation set, and prepare a short presentation covering their document choice, pipeline design, evaluation scores, and one honestly reported limitation.                                                                                                                                                                                       |

**Knowledge check 1:** A project presentation claims "My RAG assistant works perfectly" with no evaluation numbers or limitations mentioned. What is missing?

\(A\) Nothing, a confident claim is sufficient.

**(B) Evidence -- the actual retrieval/answer accuracy scores from Lecture 64's evaluation method, and an honest account of at least one real limitation found.**

\(C\) A longer project title.

***Correct answer: B***

**Knowledge check 2:** Why does the project specifically require reporting a genuine limitation, rather than presenting the assistant as flawless?

\(A\) To be artificially negative about otherwise good work.

**(B) Because every real RAG system has failure modes, and identifying them honestly demonstrates genuine understanding of the system's actual behaviour, not just that it ran once successfully.**

\(C\) Because RAG systems never actually work.

***Correct answer: B***

**Evaluation question:** Present your project's document choice, evaluation scores, and one genuine limitation in a 4-5 sentence summary, as you would for the class presentation.

**Homework (10-15 min):** Finalise your RAG Knowledge Assistant project and publish the full pipeline, evaluation results, and README (including limitations) to GitHub, following the Lecture 26 documentation habit.

**Teacher checklist**

**✓** Pipeline is fully functional end-to-end on the student's own document set

**✓** Evaluation scores are reported, not just an impression

**✓** At least one genuine, specific limitation is honestly documented

**Unit Exam — Unit 8 — Context Engineering, Embeddings & RAG**

|              |                                                                                                                                                                                      |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                                      |
| **Coverage** | Lectures 58-65: context engineering, chunking, semantic search, vector retrieval, RAG architecture, a built RAG pipeline, retrieval/answer evaluation, and the RAG capstone project. |

**Month 10 Python AI APIs, Agents & Automation**

*Allocation: 9 hours \| 9 lectures*

**Lecture 66 HTTP, REST APIs and Authentication**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain REST API authentication methods and make an authenticated API request correctly and securely.                                                                                                                                                                                                                                                                                                                      |
| **Key concepts**        | Recap HTTP GET (Lecture 23), add authentication · API keys / bearer tokens in headers · Why credentials go in headers, not the URL                                                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Extend Lecture 23 directly: most real APIs (especially AI model APIs) require proof of identity before answering. Show the standard pattern: \`headers = {"Authorization": "Bearer " + api_key}\` passed into \`requests.get(url, headers=headers)\`, and explain explicitly why the key goes in a header rather than the URL -- URLs can end up logged in browser history, server logs, or screenshots, exposing the key. |
| **Real-world example**  | Calling a real AI model API requires sending your API key as a Bearer token in the request header, not pasted into the URL where it could leak into logs.                                                                                                                                                                                                                                                                  |
| **In-class activity**   | Students make an authenticated request to a provided test API using a header-based API key, and deliberately compare it against a (non-working) attempt that puts the key in the URL, explaining why the header approach is correct practice.                                                                                                                                                                              |

**Knowledge check 1:** Why is putting an API key directly into a URL (e.g. ?api_key=abc123) considered poor practice compared to sending it in a request header?

\(A\) There is no real difference in risk.

**(B) URLs are commonly logged by servers, proxies, and browser history, which could expose a key that's embedded directly in the URL text.**

\(C\) URLs cannot technically contain API keys at all.

***Correct answer: B***

**Knowledge check 2:** What does \`headers = {"Authorization": "Bearer " + api_key}\` accomplish?

\(A\) It deletes the API key after one use.

**(B) It attaches the API key as a credential in the request header, in the standard Bearer token format many APIs expect.**

\(C\) It encrypts the entire request body.

***Correct answer: B***

**Evaluation question:** Explain, using a concrete scenario, what could go wrong if an API key is accidentally committed to a public GitHub repository instead of being kept out of version control.

**Homework (10-15 min):** Using a provided test API, make an authenticated GET request with the key passed correctly in a header, and print the response status code and one field from the result.

**Teacher checklist**

**✓** Correctly sends the API key in a header, not the URL

**✓** Can explain the specific logging/exposure risk of URL-embedded keys

**✓** Successfully receives and reads an authenticated API response

**Lecture 67 Calling an LLM API from Python**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Call a real LLM API from Python with a correctly structured request, and extract the generated text from the response.                                                                                                                                                                                                                                                                                                                                   |
| **Key concepts**        | LLM API request structure (model, prompt/messages, parameters) · Extracting the response text from the JSON structure · Linking back to Lecture 44's generation concept, now in code                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | Build the first real LLM API call: construct the request body with the model name, the prompt/messages list, and basic parameters, send it with the authenticated pattern from Lecture 66, and parse the returned JSON (Lecture 21 skill) to pull out just the generated text field, which sits nested inside the response structure. This is the first time students call the actual 'next-token prediction' mechanism from Lecture 44 as working code. |
| **Real-world example**  | Sending the prompt "Summarise this paragraph in one sentence" to an LLM API and printing just the generated summary text extracted from the JSON response.                                                                                                                                                                                                                                                                                               |
| **In-class activity**   | Students write a script that sends a prompt of their choice to a provided LLM API, correctly extracts the generated text, and prints it cleanly (not the full raw JSON).                                                                                                                                                                                                                                                                                 |

**Knowledge check 1:** An LLM API response is a JSON object with the generated text nested several levels deep (e.g. response\['choices'\]\[0\]\['message'\]\['content'\]). Why is this nesting typical?

\(A\) It's a mistake in the API design.

**(B) APIs often return metadata (model used, token counts, multiple candidate responses) alongside the text, so the actual content is nested inside a structured result rather than being the entire response.**

\(C\) Nested JSON cannot be parsed in Python.

***Correct answer: B***

**Knowledge check 2:** What is the correct first step before trying to extract text from an LLM API's response?

\(A\) Assume the call succeeded and extract text immediately.

**(B) Check the response's status code (Lecture 23/66) to confirm the call actually succeeded before parsing the expected structure.**

\(C\) Restart the whole script regardless of the outcome.

***Correct answer: B***

**Evaluation question:** Explain why printing the full raw JSON response is a reasonable debugging step the first time you call a new API, even though your final script should extract just the needed field.

**Homework (10-15 min):** Write a script that sends 2 different prompts to the provided LLM API and extracts/prints just the generated text for each, handling the JSON structure correctly.

**Teacher checklist**

**✓** Correctly builds the API request structure

**✓** Successfully extracts only the needed text field from a nested response

**✓** Checks status/success before parsing, per Lecture 66's habit

**Lecture 68 Handling JSON Responses, Errors and Retries**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Handle real-world API failures gracefully using try/except and a retry strategy, rather than letting the program crash on the first failure.                                                                                                                                                                                                                                                                                             |
| **Key concepts**        | Common failure modes: timeouts, rate limits, malformed responses · try/except around API calls (recap Lecture 20) · Simple retry logic with a limited attempt count                                                                                                                                                                                                                                                                      |
| **Teacher explanation** | Deliberately simulate 2 realistic failure types: a rate-limit error (too many requests too quickly) and a timeout, and show both crashing an unguarded script. Then wrap the API call in try/except per Lecture 20's pattern, and add a simple retry loop that tries again (with a short pause) up to a fixed number of times before giving up and reporting a clear failure message -- a key reliability habit for any real automation. |
| **Real-world example**  | A script that calls an LLM API 50 times in a row hits a rate limit on call 23; without retry handling, the whole batch job crashes and loses all remaining work.                                                                                                                                                                                                                                                                         |
| **In-class activity**   | Students add try/except and a 3-attempt retry loop around their Lecture 67 API call, then deliberately test it against a simulated failing endpoint (provided) to confirm the retry logic actually engages and eventually reports failure cleanly if all attempts fail.                                                                                                                                                                  |

**Knowledge check 1:** A script making 50 API calls in a row crashes entirely on the 23rd call due to a temporary rate limit. What is the most useful fix?

\(A\) Nothing can be done, rate limits always end the whole job.

**(B) Wrap each call in try/except with a limited retry (and a short wait) so a temporary failure doesn't take down the entire batch.**

\(C\) Remove all error handling to simplify the code.

***Correct answer: B***

**Knowledge check 2:** Why should a retry loop have a maximum attempt limit rather than retrying forever?

\(A\) There's no reason to limit it.

**(B) An unlimited retry against a persistent failure (e.g. an invalid API key) would loop forever instead of reporting a clear, actionable failure.**

\(C\) APIs block unlimited retries automatically in all cases.

***Correct answer: B***

**Evaluation question:** Explain the difference in outcome between a script with no error handling and one with a 3-attempt retry loop, when a temporary network blip occurs mid-batch.

**Homework (10-15 min):** Add retry logic (max 3 attempts, with a short delay between tries) to your Lecture 67 API script, and test it against a deliberately broken endpoint or invalid key to confirm it fails cleanly after exhausting retries.

**Teacher checklist**

**✓** try/except correctly wraps the API call, not the whole unrelated script

**✓** Retry logic has a sensible maximum, not an infinite loop

**✓** Reports a clear failure message after retries are exhausted, rather than crashing silently

**Lecture 69 Environment Variables and API Key Security**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Store and load an API key securely using environment variables instead of hardcoding it in source code.                                                                                                                                                                                                                                                                                                                                                                                     |
| **Key concepts**        | Why hardcoded keys are a security risk (recap Lecture 6) · Environment variables and .env files · Adding .env to .gitignore before pushing to GitHub                                                                                                                                                                                                                                                                                                                                        |
| **Teacher explanation** | Directly connect to Lecture 6's safety habit and Lecture 66's auth: show a hardcoded key \`api_key = "sk-abc123..."\` sitting in plain sight in a script, then explain what happens if that script is pushed to a public GitHub repo (Lecture 26) -- the key is now public and can be used/billed by anyone who finds it. Fix it by moving the key into a \`.env\` file, loading it with \`os.getenv("API_KEY")\`, and critically, adding \`.env\` to \`.gitignore\` before any git commit. |
| **Real-world example**  | A real, well-documented pattern: students accidentally committing an API key to a public repo, after which the key is scraped by bots within minutes and used for unauthorized billing.                                                                                                                                                                                                                                                                                                     |
| **In-class activity**   | Students refactor their Lecture 67/68 script to load the API key from a \`.env\` file via os.getenv() instead of hardcoding it, and confirm \`.env\` is listed in \`.gitignore\` before any commit.                                                                                                                                                                                                                                                                                         |

**Knowledge check 1:** A student commits a script containing a hardcoded \`api_key = "sk-abc123"\` to a public GitHub repository. What is the realistic risk?

\(A\) No risk, GitHub repos are private by default.

**(B) The key becomes publicly visible and can be found and misused by others (including automated scanning bots) often within minutes, potentially running up usage/billing on the owner's account.**

\(C\) GitHub automatically removes all secrets from commits.

***Correct answer: B***

**Knowledge check 2:** What is the purpose of adding \`.env\` to \`.gitignore\`?

\(A\) It makes the script run faster.

**(B) It prevents the file containing your real secret keys from ever being included in a git commit, keeping it out of version control entirely.**

\(C\) It has no real effect on security.

***Correct answer: B***

**Evaluation question:** Explain the full chain of events, step by step, that leads from 'hardcoded key in a script' to 'key is misused by a stranger,' and identify exactly which step this lecture's fix breaks.

**Homework (10-15 min):** Refactor any script you've written this month to load its API key from a \`.env\` file instead of hardcoding it, and verify \`.env\` is excluded from git tracking before you push anything.

**Teacher checklist**

**✓** No API key appears as plain text anywhere in committed code

**✓** .env is correctly excluded via .gitignore

**✓** Script successfully loads the key via os.getenv() or equivalent

**Lecture 70 Building a Python AI Workflow**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Chain multiple API calls together into one automated workflow that accomplishes a multi-step task.                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Workflow = a sequence of steps, each possibly an API call, passing data between them · Consolidating Lectures 66-69 into one pipeline · Designing the step order deliberately                                                                                                                                                                                                                                |
| **Teacher explanation** | Guide a concrete multi-step build: a workflow that (1) fetches data from one API (e.g. a news headline), (2) passes that data into an LLM API call asking for a one-line summary, and (3) saves the result to a file (Lecture 20) -- three steps chained together, each one's output feeding the next one's input, with the security (Lecture 69) and error-handling (Lecture 68) habits applied throughout. |
| **Real-world example**  | A daily news-digest script: fetch 3 headlines from a news API, summarise each with an LLM call, and save all 3 summaries to a dated text file.                                                                                                                                                                                                                                                               |
| **In-class activity**   | Students build and run their own 3-step workflow (fetch -\> process with LLM -\> save), applying secure key loading and basic error handling from the preceding lectures.                                                                                                                                                                                                                                    |

**Knowledge check 1:** In a 3-step workflow (fetch -\> summarise -\> save), what happens if step 1's fetch fails and there's no error handling around it?

\(A\) Steps 2 and 3 will simply skip ahead safely.

**(B) The whole workflow likely crashes immediately, since step 2 depends on step 1's output which never arrived.**

\(C\) Nothing, later steps don't depend on earlier ones.

***Correct answer: B***

**Knowledge check 2:** Why does step order matter in this workflow (fetch before summarise, summarise before save)?

\(A\) Order doesn't matter, Python runs steps in any order.

**(B) Each step depends on the previous step's output as its own input, so running them out of order would mean operating on missing or stale data.**

\(C\) Only the first step matters.

***Correct answer: B***

**Evaluation question:** Describe your own 3-step workflow's design, explicitly stating what data passes from each step to the next, and where you applied error handling.

**Homework (10-15 min):** Design and build your own 3-step (or more) Python AI workflow on a task of your choice, applying secure key storage and error handling, and document the data flow between steps.

**Teacher checklist**

**✓** Workflow genuinely chains multiple steps with real data dependency

**✓** Applies secure key handling and basic error handling throughout

**✓** Can explain why the step order is necessary, not arbitrary

**Lecture 71 Agent Fundamentals and Tool Calling**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Explain what an AI agent is (an LLM that can decide to call external tools) and build a minimal example with one tool.                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Key concepts**        | Agent = LLM + ability to call external functions/tools + decide when to use them · Tool calling / function calling pattern · Difference from a fixed workflow (Lecture 70)                                                                                                                                                                                                                                                                                                                                                        |
| **Teacher explanation** | Draw the key distinction from Lecture 70: a fixed workflow always runs the same steps in the same order; an agent is given a set of available tools (e.g. a calculator function, a weather-lookup function) and the LLM itself decides, based on the user's request, whether and which tool to call, then uses the tool's result to form its final answer. Demonstrate a minimal single-tool agent: given "What's 847 times 392?", the model recognises it should call a calculator tool rather than guess the arithmetic itself. |
| **Real-world example**  | An agent given a \`get_weather(city)\` tool correctly decides to call it when asked "Is it raining in Mumbai right now?" rather than guessing an answer from training data alone.                                                                                                                                                                                                                                                                                                                                                 |
| **In-class activity**   | Students build a minimal agent with one simple tool (e.g. a calculator or unit-converter function) and test it with 3 queries: one that should trigger the tool, one that shouldn't, and one ambiguous case, observing the agent's tool-use decisions.                                                                                                                                                                                                                                                                            |

**Knowledge check 1:** What is the key difference between the Lecture 70 workflow and an agent (this lecture)?

\(A\) There is no difference.

**(B) A workflow always executes the same fixed step sequence; an agent's LLM decides, per request, whether and which available tool to call based on the specific input.**

\(C\) Agents never use APIs.

***Correct answer: B***

**Knowledge check 2:** Why would an agent with a calculator tool be expected to call that tool for "What's 847 times 392?" rather than answer directly from its own generation?

\(A\) LLMs are always perfectly accurate at large multiplication from generation alone.

**(B) A dedicated calculator tool guarantees an exact, reliable arithmetic result, which is more trustworthy than an LLM's learned-pattern guess at a specific large multiplication.**

\(C\) Agents are physically incapable of outputting numbers directly.

***Correct answer: B***

**Evaluation question:** Describe the ambiguous test case from your activity: did the agent call the tool or not, and do you think that decision was the right one? Explain your reasoning.

**Homework (10-15 min):** Add a second tool to your minimal agent (e.g. a second simple function) and test 3 new queries to see whether the agent correctly chooses between the two tools or no tool at all.

**Teacher checklist**

**✓** Agent correctly calls the tool for an unambiguous matching query

**✓** Agent correctly avoids the tool for a clearly unrelated query

**✓** Can explain, not just observe, why the agent's decision was or wasn't appropriate

**Lecture 72 Workflow Automation and External Tools**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Integrate a real external tool/service into an agent or workflow (beyond a toy function), handling its specific input/output requirements.                                                                                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Real external tools (file operations, a real API, a search function) vs toy demo functions · Matching tool input/output formats correctly · Scoping what a tool is and isn't allowed to do                                                                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | Move from Lecture 71's toy calculator to a real integration: wire in an actual external tool (e.g. a real search API or a file-writing function) as an agent tool, paying close attention to exactly what input format the tool expects and what output format it returns, since mismatches here are a common real bug. Discuss scoping: deliberately limiting what the tool is allowed to do (e.g. a file-writing tool that can only write to one specific folder) to avoid unsafe or unintended actions. |
| **Real-world example**  | An agent with a real 'save_note(text)' tool that writes to a specific notes file -- scoped so it cannot be redirected to overwrite arbitrary system files.                                                                                                                                                                                                                                                                                                                                                 |
| **In-class activity**   | Students integrate one real external tool into their agent from Lecture 71, test it with a request that should trigger it, and document one scoping limit they deliberately built in to keep the tool safe.                                                                                                                                                                                                                                                                                                |

**Knowledge check 1:** Why is it important to deliberately scope what a file-writing tool given to an agent is allowed to do (e.g. restrict it to one folder)?

\(A\) Scoping is unnecessary if the agent is well-behaved.

**(B) Without restriction, a tool could be used (intentionally or via a flawed agent decision) to write to or overwrite files outside its intended, safe scope.**

\(C\) Scoping only matters for calculator tools.

***Correct answer: B***

**Knowledge check 2:** An agent's search tool expects input as \`{"query": "..."}\` but the agent sends \`{"q": "..."}\` instead. What is the likely result?

\(A\) The tool automatically adapts to any input format.

**(B) The call likely fails or returns an error/empty result, since the tool's expected input format wasn't matched.**

\(C\) This has no effect on the outcome.

***Correct answer: B***

**Evaluation question:** Describe the real external tool you integrated and the specific scoping limit you applied, explaining what risk that limit protects against.

**Homework (10-15 min):** Document your integrated tool's exact expected input/output format, and test one deliberately malformed input to confirm your error handling (Lecture 68) catches the mismatch gracefully.

**Teacher checklist**

**✓** Real external tool (not a toy function) is successfully integrated

**✓** A genuine scoping/safety limit is applied and explained

**✓** Malformed-input test is handled gracefully, not left to crash

**Lecture 73 Testing and Monitoring AI Workflows**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Add logging and basic monitoring to an AI workflow/agent so failures and unusual behaviour can be detected after the fact, not just during a live test.                                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Logging key events (calls made, tool choices, errors) to a file · Why 'it worked when I tested it' isn't enough for a running system · Basic monitoring: counting successes/failures over multiple runs                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | Make the case directly: a workflow tested once by hand looking successful tells you little about how it behaves across 100 unattended runs overnight. Add structured logging (timestamp, action taken, success/failure) to the workflow/agent from Lectures 70-72, then run it multiple times against varied inputs and review the log to spot patterns -- e.g. a particular input type that consistently fails, which a single manual test would have missed entirely. |
| **Real-world example**  | A logged overnight batch run reveals that 8 out of 50 requests failed, all involving the same unusual input pattern -- invisible from a single successful manual test earlier in the day.                                                                                                                                                                                                                                                                               |
| **In-class activity**   | Students add logging to their Lecture 70-72 workflow/agent, run it against 10 varied test inputs, and review the resulting log to identify any failure pattern.                                                                                                                                                                                                                                                                                                         |

**Knowledge check 1:** A workflow worked correctly in a single manual test this morning. Why might logging still reveal problems across an unattended overnight batch of 100 runs?

\(A\) It can't, one successful test guarantees correctness forever.

**(B) A single test only covers one specific input; across many varied unattended runs, different inputs or transient issues (API errors, edge cases) can surface failures the single test never encountered.**

\(C\) Logging has no diagnostic value.

***Correct answer: B***

**Knowledge check 2:** What is the main value of recording a timestamp and success/failure status for each workflow run in a log?

\(A\) It makes the code run faster.

**(B) It lets you later analyse patterns across many runs (e.g. which inputs or times correlate with failures) rather than relying on memory of one test.**

\(C\) Logs are only useful for security audits, not debugging.

***Correct answer: B***

**Evaluation question:** Describe any failure pattern you found (or didn't find) in your 10-run log, and explain what you would investigate next based on that evidence.

**Homework (10-15 min):** Run your logged workflow against 10 more varied inputs, including at least 2 you expect might be tricky, and write a short report on any pattern found in the combined 20-run log.

**Teacher checklist**

**✓** Logging captures enough detail to diagnose failures after the fact

**✓** Draws a conclusion from actual log evidence across multiple runs, not a single test

**✓** Identifies, or rules out with evidence, a specific failure pattern

**Lecture 74 AI Workflow/Agent Project**

*Month 10 · Python AI APIs, Agents & Automation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Design, build, log and present a complete AI workflow or agent project, consolidating the full Month 10 unit.                                                                                                                                                                                                                                                                                                                                                                                |
| **Key concepts**        | Full consolidation: authenticated API calls, error handling, secure keys, chained steps or agent tool-use, logging/monitoring · Presenting the project with evidence from logs                                                                                                                                                                                                                                                                                                               |
| **Teacher explanation** | This is the Month 10 capstone project: students design their own multi-step workflow or simple agent solving a real small task of their choice, applying every habit built this month -- secure key storage (Lecture 69), error handling and retries (Lecture 68), a sensible step/tool design (Lectures 70-72), and logging across multiple test runs (Lecture 73) -- then present the project with actual log evidence of its behaviour across several runs, not just one successful demo. |
| **Real-world example**  | A personal study-helper agent that can look up a topic, summarise it, and save the summary to a notes file, with a tool-scoping limit and a 10-run log showing 9/10 successful runs and the one documented failure.                                                                                                                                                                                                                                                                          |
| **In-class activity**   | Students finalise their chosen workflow/agent project, run it across at least 10 varied test inputs with logging enabled, and prepare a short presentation covering design, security/error-handling choices, and log-based evidence of reliability.                                                                                                                                                                                                                                          |

**Knowledge check 1:** A project presentation shows one successful live demo and claims the system 'always works.' What is missing, based on this month's standards?

\(A\) Nothing, a live demo is sufficient proof.

**(B) Evidence across multiple runs (the Lecture 73 logging habit) showing the actual success/failure rate, not just one cherry-picked successful demonstration.**

\(C\) A more exciting demo topic.

***Correct answer: B***

**Knowledge check 2:** Why does this project specifically require showing log evidence from multiple runs rather than just one working example?

\(A\) To make the project take longer for no real benefit.

**(B) Because a single successful run doesn't reveal a system's real reliability or failure patterns the way evidence across multiple varied runs does.**

\(C\) Logs are only decorative and have no bearing on project quality.

***Correct answer: B***

**Evaluation question:** Summarise your project in 4-5 sentences: what it does, what security/error-handling choices you made, and your actual logged success rate across your test runs.

**Homework (10-15 min):** Finalise your Month 10 project and publish the code, logs, and a README (covering design, security choices, and reliability evidence) to GitHub.

**Teacher checklist**

**✓** Project chains real steps or genuine agent tool-use, not a trivial single call

**✓** Security and error-handling habits from the month are visibly applied

**✓** Presentation is backed by actual multi-run log evidence, not a single demo

**Unit Exam — Unit 9 — Python AI APIs, Agents & Automation**

|              |                                                                                                                                                                                       |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                                       |
| **Coverage** | Lectures 66-74: authenticated API calls, LLM API integration, error handling/retries, secure key storage, chained workflows, agents and tool calling, and the workflow/agent project. |

**Month 11 AI Application Development, Testing & Deployment**

*Allocation: 12 hours \| 12 lectures*

**Lecture 75 AI Application Requirements and Problem Definition**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Write a clear requirements document for an AI application, defining the problem, users, and success criteria before writing any code.                                                                                                                                                                                                                                                                                                       |
| **Key concepts**        | Problem statement vs solution · Defining success criteria upfront · Identifying real users and their actual need                                                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Model the discipline of defining the problem before touching code: for a chosen idea (e.g. a study-help app), write out specifically who the user is, what problem they actually have, what the app must do to solve it, and -- critically -- how you'll know if it worked (a measurable success criterion), rather than jumping straight to 'let's build a chatbot.' Show a vague requirements example versus a specific one side by side. |
| **Real-world example**  | Vague: "Build an AI app to help students." Specific: "Build a tool that takes a student's messy class notes and returns 5 accurate revision flashcards within 10 seconds, verified correct by the student at least 80% of the time."                                                                                                                                                                                                        |
| **In-class activity**   | Students write a one-page requirements document for their own Month 11 capstone idea, including problem statement, target user, core features, and at least one measurable success criterion.                                                                                                                                                                                                                                               |

**Knowledge check 1:** Why is "Build an AI app to help students" an inadequate requirements statement to start coding from?

\(A\) It's perfectly adequate; more detail just slows things down.

**(B) It doesn't specify the actual problem, the particular user need, or any way to measure whether the finished app actually succeeds.**

\(C\) The sentence is grammatically incorrect.

***Correct answer: B***

**Knowledge check 2:** What makes a success criterion 'measurable' rather than vague?

\(A\) It uses impressive-sounding words.

**(B) It states a specific, checkable condition (e.g. a percentage, a time limit, an accuracy threshold) that can be tested against, not just a feeling of 'it works well.'**

\(C\) It is written in the first paragraph of the document.

***Correct answer: B***

**Evaluation question:** Write your own one-sentence problem statement and one measurable success criterion for an AI application idea, and explain why that criterion is genuinely checkable.

**Homework (10-15 min):** Complete a full one-page requirements document for your Month 11 capstone application idea, including user, problem, core features, and at least one measurable success criterion.

**Teacher checklist**

**✓** Problem statement names a specific user and specific need

**✓** Success criterion is genuinely measurable, not vague

**✓** Requirements are written before any code for this project

**Lecture 76 Application Architecture and Component Design**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Design a component-level architecture for an AI application, identifying each piece and how data flows between them.                                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Breaking an app into components (input/UI, processing logic, AI calls, storage, output) · Data flow between components · Why planning architecture before coding saves rework                                                                                                                                                                                                                                                                                  |
| **Teacher explanation** | Using the Lecture 75 requirements as the starting point, sketch a component diagram: where does input come from, what processes it, where do AI API calls (Month 10 skills) happen, where is data stored (files/JSON from Month 4), and what is shown back to the user. Emphasise that this is the same discipline as the ML pipeline (Lecture 35) and RAG architecture (Lecture 62) diagrams -- planning data flow before writing code reduces costly rework. |
| **Real-world example**  | A notes-to-flashcards app's architecture: Input (raw notes text) -\> Chunking component -\> LLM-call component (generate Q&A) -\> Storage component (save as JSON) -\> Output component (display flashcards).                                                                                                                                                                                                                                                  |
| **In-class activity**   | Students draw their own component diagram for their Lecture 75 capstone idea, labelling each component's responsibility and the data that flows between them.                                                                                                                                                                                                                                                                                                  |

**Knowledge check 1:** Why is sketching a component architecture before writing code considered good practice, as it was for the ML pipeline and RAG architecture earlier in the course?

\(A\) It has no practical benefit, it's just paperwork.

**(B) Planning how data flows between components in advance helps catch design problems early and reduces costly rework after code is already written.**

\(C\) Architecture diagrams are only required for very large companies.

***Correct answer: B***

**Knowledge check 2:** In the notes-to-flashcards example, what does the 'Storage component' do?

\(A\) Generates the actual flashcard content.

**(B) Saves the generated flashcard data (e.g. as JSON) so it persists beyond a single session.**

\(C\) Displays the flashcards to the user.

***Correct answer: B***

**Evaluation question:** Walk through your own component diagram, explaining what data enters and leaves each component in order.

**Homework (10-15 min):** Finalise your capstone's component architecture diagram, labelling every component's responsibility and the exact data passed between adjacent components.

**Teacher checklist**

**✓** Diagram includes all necessary components (input, processing, AI calls, storage, output)

**✓** Data flow between components is explicit and logically ordered

**✓** Architecture reflects the Lecture 75 requirements, not an unrelated idea

**Lecture 77 Python Project Structure and Reusable Modules**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Organise an application's code into a clean, multi-file project structure with reusable modules, rather than one long script.                                                                                                                                                                                                                                                                                         |
| **Key concepts**        | Project folder structure (main.py, modules, a config/settings file) · Extending Lecture 19's import skill to a full project · Separating concerns: one module's job, one responsibility                                                                                                                                                                                                                               |
| **Teacher explanation** | Extend Lecture 19's two-file split to a full small project: organise the capstone's components (Lecture 76) into separate files -- e.g. \`ai_calls.py\`, \`storage.py\`, \`main.py\` -- each handling one responsibility, imported together in main.py. Emphasise that this isn't just tidiness: it makes each piece independently testable (coming in Lecture 81) and easier for a reader (or teammate) to navigate. |
| **Real-world example**  | A flashcard app split into \`generate.py\` (LLM calls), \`storage.py\` (save/load JSON), and \`main.py\` (ties them together) -- instead of one 200-line file mixing all concerns.                                                                                                                                                                                                                                    |
| **In-class activity**   | Students begin structuring their capstone project into separate files matching their Lecture 76 component diagram, with each file handling exactly one responsibility.                                                                                                                                                                                                                                                |

**Knowledge check 1:** Why is splitting a 200-line script into purpose-specific files (e.g. generate.py, storage.py) generally better than one large file?

\(A\) It makes no practical difference.

**(B) It makes each piece's responsibility clear, easier to test in isolation, and easier for anyone (including your future self) to navigate and modify safely.**

\(C\) Python runs multi-file projects faster than single-file ones.

***Correct answer: B***

**Knowledge check 2:** A module named \`storage.py\` unexpectedly also contains code that calls the LLM API directly. What does this suggest?

\(A\) This is good design, more code per file is efficient.

**(B) This likely violates separation of concerns -- that LLM-calling logic probably belongs in a dedicated module instead.**

\(C\) Nothing is wrong, module names are purely decorative.

***Correct answer: B***

**Evaluation question:** Describe your project's current file structure and explain, for one file, why its contents belong together under that single responsibility.

**Homework (10-15 min):** Restructure your capstone project (if not already done) into separate files matching your component diagram, with imports wiring them together correctly in main.py.

**Teacher checklist**

**✓** Project is split into multiple purpose-specific files, not one monolithic script

**✓** Each file's contents match a single, clear responsibility

**✓** Imports correctly connect the files into a working whole

**Lecture 78 Connecting Frontend, Backend and AI APIs**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Wire together a basic user-facing interface, backend processing logic, and an AI API call into one working request/response flow.                                                                                                                                                                                                                                                                                      |
| **Key concepts**        | Simple frontend (CLI or basic web form) · Backend logic receiving input and orchestrating the AI call · Full request -\> process -\> AI call -\> response flow                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Using the Lecture 77 project structure, connect a simple user-facing layer (a command-line prompt, or a minimal web form if the toolkit supports one) to the backend logic that takes that input, calls the AI API (Month 10 skills) with it, and returns a result back to the same interface -- making the full loop visible and testable end-to-end for the first time, not just individual components in isolation. |
| **Real-world example**  | A user types their raw notes into a simple CLI prompt, the backend sends them to the LLM for flashcard generation, and the generated flashcards are printed back to the same terminal session.                                                                                                                                                                                                                         |
| **In-class activity**   | Students connect their capstone's input interface to their backend AI-call logic and confirm a full round trip: user input goes in, a processed AI-generated result comes back out, through their own project's code.                                                                                                                                                                                                  |

**Knowledge check 1:** Why is testing the full input -\> backend -\> AI call -\> output loop important, even if each component passed its own isolated test earlier?

\(A\) It's unnecessary if each piece works alone.

**(B) Components that work individually can still fail when connected, due to format mismatches or incorrect wiring between them -- the full loop must be verified directly.**

\(C\) Full-loop testing is only relevant for web applications, not CLI tools.

***Correct answer: B***

**Knowledge check 2:** A user's raw text input is passed directly into an API call that expects a specific JSON structure, and the call fails. What is the most likely issue?

\(A\) The AI API is broken.

**(B) The input likely needs to be formatted/wrapped into the structure the API expects (recall Lecture 67) before being sent, rather than passed as raw text.**

\(C\) This should never be a problem.

***Correct answer: B***

**Evaluation question:** Describe one issue (format mismatch, missing field, etc.) you encountered while connecting your interface to your backend AI call, and how you fixed it.

**Homework (10-15 min):** Complete the full connected loop for your capstone (input -\> backend -\> AI call -\> output) and test it with 3 different realistic inputs end-to-end.

**Teacher checklist**

**✓** Full request/response loop works end-to-end, not just in isolated pieces

**✓** Handles at least one real connection issue (format, wiring) rather than assuming it would just work

**✓** Tested with multiple realistic inputs, not just one

**Lecture 79 Data Handling and Persistent Storage**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Persist application data correctly between runs using file or lightweight database storage, handling corrupted/missing data gracefully.                                                                                                                                                                                                                                                                                                                            |
| **Key concepts**        | Persisting data beyond a single run (recap Lecture 20-21) · Choosing JSON file vs a lightweight database for the task's scale · Handling a missing or corrupted data file gracefully                                                                                                                                                                                                                                                                               |
| **Teacher explanation** | Extend Lectures 20-21 to the application level: the capstone needs its data (saved flashcards, user history, etc.) to survive after the program closes, so wire in persistent storage -- a JSON file is often sufficient at this scale. Deliberately corrupt or delete the data file and show the app crashing, then fix it with try/except that initialises a sensible empty/default state if the file is missing or unreadable, rather than crashing on startup. |
| **Real-world example**  | A flashcard app that saves progress to \`data.json\`; if that file is deleted or becomes corrupted, the app should start with an empty flashcard set rather than crashing on launch.                                                                                                                                                                                                                                                                               |
| **In-class activity**   | Students add persistent storage to their capstone, then deliberately delete or corrupt the data file to confirm their app starts gracefully with a sensible default state instead of crashing.                                                                                                                                                                                                                                                                     |

**Knowledge check 1:** An app crashes on startup because its saved data file was accidentally deleted. What is the correct fix?

\(A\) Nothing can be done; the app must always crash if its data file is missing.

**(B) Wrap the file-loading step in try/except and initialise a sensible default/empty state if the file is missing or unreadable.**

\(C\) Require the user to always manually recreate the file before running the app.

***Correct answer: B***

**Knowledge check 2:** For a small single-user app storing a few hundred flashcards, why might a JSON file be a perfectly adequate storage choice rather than a full database?

\(A\) JSON files are always better than databases in every situation.

**(B) At this small scale and single-user context, a JSON file is simple and sufficient; a full database adds complexity that isn't justified by the actual data volume or access patterns here.**

\(C\) Databases cannot store text data.

***Correct answer: B***

**Evaluation question:** Explain what you tested (deleting/corrupting your data file) and how your app behaved before and after you added the graceful-default handling.

**Homework (10-15 min):** Add persistent storage to your capstone if not already present, then test the missing-file and corrupted-file cases explicitly, documenting the app's behaviour in each case.

**Teacher checklist**

**✓** Data genuinely persists across separate program runs

**✓** Missing/corrupted data file is handled gracefully, not left to crash

**✓** Storage choice (file vs database) is justified for this app's actual scale

**Lecture 80 Input Validation and Error Handling**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Validate user input against expected constraints before processing it, and give clear, specific error messages when input is invalid.                                                                                                                                                                                                                                                                                                                                                             |
| **Key concepts**        | Validating input type, length, and format before use · Clear, specific error messages vs generic crashes · Where validation belongs in the request flow (as early as possible)                                                                                                                                                                                                                                                                                                                    |
| **Teacher explanation** | Deliberately feed the Lecture 78 application empty input, extremely long input, and input in an unexpected format, observing what happens unguarded. Add validation checks as early as possible in the flow -- before the expensive AI API call is even made -- so a clearly invalid request fails fast with a specific, helpful message ("Please enter at least 10 words of notes") rather than wasting an API call on input that was never going to work, or crashing deep inside the pipeline. |
| **Real-world example**  | A user submits an empty notes field to the flashcard app; validating this before calling the LLM API saves an unnecessary API call and gives the user immediate, specific feedback instead of a confusing downstream error.                                                                                                                                                                                                                                                                       |
| **In-class activity**   | Students add input validation to their capstone's entry point, covering at least 3 realistic bad-input cases (empty, too long, wrong type), each with a specific and helpful error message.                                                                                                                                                                                                                                                                                                       |

**Knowledge check 1:** Why should input validation happen as early as possible in the request flow, before an AI API call is made?

\(A\) Timing doesn't matter, validation can happen anywhere.

**(B) Catching clearly invalid input early avoids wasting a costly/slow API call on input that was never going to succeed, and gives faster feedback to the user.**

\(C\) Validation is only possible after the API call returns.

***Correct answer: B***

**Knowledge check 2:** Which error message is more useful to a user who submitted empty notes text?

\(A\) "Error: something went wrong."

**(B) "Please enter at least a few sentences of notes before generating flashcards."**

\(C\) No message at all, just silently do nothing.

***Correct answer: B***

**Evaluation question:** List the 3 bad-input cases you tested and, for each, explain why your chosen validation message is more helpful than a generic error would be.

**Homework (10-15 min):** Add validation for at least 3 realistic bad-input scenarios to your capstone's entry point, each producing a specific, actionable error message rather than a crash or silence.

**Teacher checklist**

**✓** Validation happens before any costly downstream processing

**✓** Error messages are specific and actionable, not generic

**✓** Covers multiple realistic bad-input cases, not just one

**Lecture 81 Testing Python Functions and API Integrations**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Write and run automated tests for individual functions and for an AI API integration, including a mocked test that doesn't require a real API call.                                                                                                                                                                                                                                                                                                     |
| **Key concepts**        | Writing simple unit tests (assert-based or a basic test framework) · Testing pure logic functions directly · Mocking an API call for fast, repeatable tests without real network/cost                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | Separate two testing needs: (1) pure logic functions (e.g. a function that formats flashcard text) can be tested directly with simple assert statements comparing actual vs expected output; (2) AI API calls are slower, cost money, and can vary -- so introduce the idea of a mock (a fake stand-in response) to test that your code correctly handles a given API response shape, without making a real network call every time you run your tests. |
| **Real-world example**  | A unit test asserting that \`format_flashcard("Q", "A")\` returns exactly the expected formatted string, and a separate mocked test confirming your code correctly extracts text from a fake, pre-written API response shape.                                                                                                                                                                                                                           |
| **In-class activity**   | Students write 3 unit tests for a pure logic function in their capstone, plus one mocked test for their API-handling code that doesn't make a real network call, and confirm all tests pass.                                                                                                                                                                                                                                                            |

**Knowledge check 1:** Why mock an API call in a test instead of always calling the real API?

\(A\) Mocking is pointless and provides no benefit.

**(B) Mocking lets you test how your code handles a given response shape quickly, repeatably and without cost or dependence on network/API availability.**

\(C\) Real APIs cannot be tested at all.

***Correct answer: B***

**Knowledge check 2:** What should a unit test for \`format_flashcard("Q", "A")\` check?

\(A\) That the function runs without printing anything.

**(B) That the function's actual return value exactly matches the specific expected formatted output for that input.**

\(C\) That the function takes less than 1 second, regardless of correctness.

***Correct answer: B***

**Evaluation question:** Explain, for your own mocked test, what fake response shape you used and what specific behaviour of your code it verified.

**Homework (10-15 min):** Write at least 3 unit tests for a pure function and 1 mocked test for an API-handling function in your capstone project, and confirm they all pass.

**Teacher checklist**

**✓** Unit tests check specific expected values, not just 'runs without crashing'

**✓** At least one test uses mocking rather than a real API call

**✓** Tests actually run and pass against the current code

**Lecture 82 AI Application Evaluation**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Evaluate the finished application against the Lecture 75 success criteria using real test cases, not just a subjective impression.                                                                                                                                                                                                                                                                                                |
| **Key concepts**        | Returning to the Lecture 75 measurable success criteria · Running the app against a small evaluation set (echoing Lecture 56/64) · Reporting an honest pass/fail or score, not just "it feels good"                                                                                                                                                                                                                               |
| **Teacher explanation** | Close the loop back to Lecture 75: pull up the measurable success criterion written at the very start of the project, build a small set of realistic test cases, run the finished application against them, and score the result against that specific criterion -- directly reusing the evaluation-dataset discipline from Lectures 56 and 64, now applied to the whole application rather than just a prompt or a RAG pipeline. |
| **Real-world example**  | If the Lecture 75 success criterion was "80% of generated flashcards are judged accurate by the student," run the app on 10 real note samples, manually judge each flashcard set's accuracy, and report the actual achieved percentage against that 80% target.                                                                                                                                                                   |
| **In-class activity**   | Students run their finished capstone application against a 8-10 case evaluation set and score it against their own Lecture 75 success criterion, reporting an honest pass/fail/score verdict.                                                                                                                                                                                                                                     |

**Knowledge check 1:** A student built an app with the success criterion "80% flashcard accuracy" but, at evaluation time, simply states "I think it works great." What is missing?

\(A\) Nothing, personal impression is a valid evaluation.

**(B) Actual measurement against the stated 80% criterion, using real test cases scored specifically against that target.**

\(C\) A longer app description.

***Correct answer: B***

**Knowledge check 2:** If an evaluation finds the app achieves only 55% against an 80% target, what is the appropriate response?

\(A\) Report 80% anyway since that was the goal.

**(B) Honestly report the actual 55% result and identify what's causing the shortfall, as a legitimate finding, not a failure to hide.**

\(C\) Stop evaluating and avoid mentioning the result.

***Correct answer: B***

**Evaluation question:** Report your capstone's actual evaluation result against your Lecture 75 success criterion, and explain, if it fell short, what you believe is causing the gap.

**Homework (10-15 min):** Run your evaluation set (8-10 cases) against your capstone application, score it against your stated success criterion, and write an honest short report of the result, including any shortfall.

**Teacher checklist**

**✓** Evaluates against the specific, original Lecture 75 criterion, not a new vague standard

**✓** Uses an actual test set with real scoring, not just impression

**✓** Reports the honest result, including any shortfall, not an inflated claim

**Lecture 83 Logging, Debugging and Observability**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Add structured logging and basic observability to a deployed-style application so issues can be diagnosed after the fact.                                                                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Extending Lecture 73's logging to full application observability · Logging levels (info, warning, error) · What to log (and what NOT to log -- recap Lecture 69/6 for secrets)                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Extend Lecture 73's workflow logging to the whole application: log key events (requests received, AI calls made, errors) with appropriate severity levels, so a problem reported later ("it didn't work for me yesterday") can actually be diagnosed from the log rather than needing to be reproduced live. Critically reinforce Lecture 69's security habit: logs must never capture API keys, passwords, or other sensitive user data, even for debugging convenience. |
| **Real-world example**  | A user reports "the app gave me a weird answer yesterday afternoon"; a properly logged application lets the developer find that exact request in the log and see precisely what happened, instead of being unable to investigate at all.                                                                                                                                                                                                                                  |
| **In-class activity**   | Students add structured logging with appropriate severity levels to their capstone application, deliberately checking that no sensitive data (API keys, raw personal input) ends up in the log file.                                                                                                                                                                                                                                                                      |

**Knowledge check 1:** A user reports an issue that happened yesterday and can't be easily reproduced live. Why does structured logging make this diagnosable?

\(A\) It doesn't help; past issues can never be investigated.

**(B) A log recorded at the time captures what actually happened during that specific request, letting a developer investigate after the fact instead of needing to reproduce the issue live.**

\(C\) Logging only helps with issues happening right now.

***Correct answer: B***

**Knowledge check 2:** Should application logs include the user's raw API key or full personal data for debugging convenience?

\(A\) Yes, more detail in logs is always better for debugging.

**(B) No -- per Lecture 69's security principle, sensitive data like API keys should never appear in logs, even though it might seem convenient for debugging.**

\(C\) Only if the log file is kept on the same server.

***Correct answer: B***

**Evaluation question:** Describe one event your capstone's logging captures and explain what severity level (info/warning/error) you assigned it and why.

**Homework (10-15 min):** Add or review your capstone's logging to ensure it captures diagnosable detail about requests and errors, while explicitly confirming no sensitive data appears in any log entry.

**Teacher checklist**

**✓** Logging uses appropriate severity levels, not everything logged as one level

**✓** No sensitive data (keys, raw credentials) appears in any log entry

**✓** A real problem could plausibly be diagnosed from the log after the fact

**Lecture 84 Basic Deployment and Environment Configuration**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Deploy a working version of the application to a basic hosting environment, with configuration (not hardcoded values) controlling environment-specific settings.                                                                                                                                                                                                                                                                                                                   |
| **Key concepts**        | Deploying to a simple hosting platform · Environment-specific configuration (dev vs deployed settings) · Confirming the deployed version actually works, not just the local copy                                                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | Walk through deploying the capstone to a simple, accessible hosting option (depending on available tooling), using environment variables (Lecture 69's pattern, extended) to configure anything that differs between a student's local machine and the deployed environment, rather than hardcoding paths or settings that only work locally. Critically: test the actual deployed version end-to-end, since 'it works on my machine' is not the same as 'it works once deployed.' |
| **Real-world example**  | A capstone that works perfectly locally fails once deployed because a hardcoded local file path doesn't exist on the hosting server -- fixed by making the path configurable via an environment variable instead.                                                                                                                                                                                                                                                                  |
| **In-class activity**   | Students deploy their capstone to a provided simple hosting option, test the deployed version directly (not just their local copy), and fix any environment-specific issue that surfaces (e.g. a hardcoded path or missing configuration).                                                                                                                                                                                                                                         |

**Knowledge check 1:** A capstone app works perfectly on a student's own laptop but fails immediately once deployed to a server. What is a likely cause?

\(A\) Deployment always breaks working code for no reason.

**(B) The code may rely on something specific to the local environment (a hardcoded local file path, an assumed local setting) that doesn't hold true on the deployed server.**

\(C\) This should never be possible if the code was tested locally.

***Correct answer: B***

**Knowledge check 2:** Why use environment variables for settings that differ between local development and deployment, rather than hardcoding one fixed value?

\(A\) Environment variables have no real purpose here.

**(B) They let the same code run correctly in different environments by supplying the environment-appropriate value at runtime, instead of being locked to one hardcoded setting.**

\(C\) Hardcoding is always safer than configuration.

***Correct answer: B***

**Evaluation question:** Describe one issue that appeared only after deploying your app (if any), and the specific configuration change you made to fix it.

**Homework (10-15 min):** Deploy your capstone application and verify, by testing the deployed version directly, that its core functionality works in that environment, documenting any fix required.

**Teacher checklist**

**✓** Deployed version is actually tested directly, not assumed to work from the local version

**✓** Environment-specific settings are configurable, not hardcoded

**✓** Any deployment-specific issue found is documented along with its fix

**Lecture 85 Application Security and Secrets Management**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Audit a deployed application for common security issues: exposed secrets, unvalidated input, and insecure data handling.                                                                                                                                                                                                                                                                                                             |
| **Key concepts**        | Consolidating Lecture 69's key security and Lecture 80's input validation into a full security review · Checking for exposed secrets in code, logs and config · Basic access/data-protection considerations for a real deployed app                                                                                                                                                                                                  |
| **Teacher explanation** | Run a structured security audit of the capstone, pulling together the course's security threads: confirm no API keys or secrets appear anywhere in the committed code, logs, or public deployment configuration (Lecture 69); confirm user input is validated before use (Lecture 80); and consider what user data the app stores and whether it's handled appropriately (Lecture 6's privacy habits, now at the application level). |
| **Real-world example**  | A security audit catches a debug \`print(api_key)\` statement accidentally left in the deployed app's visible logs -- exactly the kind of leak the earlier security lectures warned about, now caught by a deliberate review process.                                                                                                                                                                                                |
| **In-class activity**   | Students run a security checklist against their own deployed capstone: search code/logs/config for any exposed secret, confirm input validation is present at every entry point, and document the audit's findings.                                                                                                                                                                                                                  |

**Knowledge check 1:** A security audit finds a debug \`print(api_key)\` statement left in code that also writes to a log file accessible in the deployed environment. What is the risk?

\(A\) No risk, debug statements are always removed automatically before deployment.

**(B) The real secret key could be exposed in the log output, violating the security practice established back in Lecture 69.**

\(C\) Print statements never affect log files.

***Correct answer: B***

**Knowledge check 2:** Why does a security audit specifically re-check input validation (Lecture 80) as part of reviewing a deployed app?

\(A\) Validation only matters during development, not after deployment.

**(B) A deployed application is exposed to real, potentially adversarial input from anyone who can reach it, making robust validation even more important than during local testing.**

\(C\) Input validation has nothing to do with security.

***Correct answer: B***

**Evaluation question:** Report one finding from your own security audit (an issue found, or confirmation none was found) for each of the three checklist areas: secrets, input validation, and data handling.

**Homework (10-15 min):** Run a full security audit on your deployed capstone covering secrets exposure, input validation, and data handling, documenting all findings and any fixes applied.

**Teacher checklist**

**✓** Audit actually checks code/logs/config for exposed secrets, not just assumes none exist

**✓** Input validation is confirmed present at every real entry point

**✓** Findings (including 'none found') are documented with evidence, not just asserted

**Lecture 86 Integration, Testing and Project Review**

*Month 11 · AI Application Development, Testing & Deployment · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Complete a final integration pass on the capstone application, confirming every Month 11 requirement (architecture, testing, evaluation, security, deployment) is genuinely in place.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Key concepts**        | Final integration check across all of Lectures 75-85 · Project review against the original Lecture 75 requirements · Preparing for Month 12's certification and capstone phase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | Run a full project review against a single checklist covering every lecture in the unit: does the architecture (Lecture 76) match what was actually built? Is the code properly structured (Lecture 77)? Does the full loop work (Lecture 78)? Is data persisted safely (Lecture 79)? Is input validated (Lecture 80)? Are there passing tests (Lecture 81)? Was it evaluated against the original success criterion (Lecture 82)? Is logging in place (Lecture 83)? Is it deployed and tested there (Lecture 84)? Has a security audit been run (Lecture 85)? Any gap found here must be fixed now, before Month 12's final capstone phase builds on top of this application. |
| **Real-world example**  | A review catches that the deployed version (Lecture 84) was never re-tested after the security fixes from Lecture 85 were applied locally -- requiring one more deployment and verification pass before the project can be considered complete.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **In-class activity**   | Students complete the full Month 11 review checklist against their own capstone, fixing any gap found, and prepare a short status report confirming every checklist item is genuinely satisfied with evidence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

**Knowledge check 1:** A review finds that security fixes (Lecture 85) were applied to the local code but the deployed version (Lecture 84) was never updated and re-tested. What should happen next?

\(A\) Nothing, local fixes are assumed to apply everywhere automatically.

**(B) Redeploy the fixed version and re-test it directly in the deployed environment, since local changes don't automatically propagate to an already-deployed instance.**

\(C\) The review is complete once local code is fixed.

***Correct answer: B***

**Knowledge check 2:** Why is a full review against every lecture's checklist valuable before moving into Month 12's capstone phase?

\(A\) It isn't valuable, Month 12 is unrelated to Month 11's work.

**(B) It catches any gap or regression across the full application before further work builds on top of it, preventing compounded problems later.**

\(C\) Reviews are only needed at the very end of the entire course.

***Correct answer: B***

**Evaluation question:** Report your own review checklist results: which items were already solid, and which (if any) needed a fix during this review.

**Homework (10-15 min):** Complete your full Month 11 review checklist, fix any remaining gaps, and publish the finalised, reviewed capstone project to GitHub with an updated README reflecting its final state.

**Teacher checklist**

**✓** Every checklist item from Lectures 75-85 is verified with actual evidence, not assumed

**✓** Any gap found during review is actually fixed, not just noted

**✓** Final GitHub README accurately reflects the project's finished, reviewed state

**Unit Exam — Unit 10 — AI Application Development, Testing & Deployment**

|              |                                                                                                                                                                                              |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 30 questions, scenario-based where possible, covering the unit listed below. Full class period.                                                                                              |
| **Coverage** | Lectures 75-86: requirements, architecture, project structure, full-stack integration, persistent storage, validation, testing, evaluation, logging, deployment, security, and final review. |

**Month 12 Cloud AI, Final Capstone & Graduation**

*Allocation: 18 hours \| 18 lectures*

**Lecture 87 Azure AI-901: Exam Structure, Skills Measured and Readiness Plan**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Describe the AI-901 exam's structure, the two skill domains it measures, and build a personal 6-hour study plan for the remaining lectures in this unit.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Key concepts**        | AI-901 replaced AI-900 (retired 30 June 2026) · Two skill domains: Identify AI concepts/capabilities (40-45%) and Implement AI solutions using Microsoft Foundry (55-60%) · Passing score 700/1000 · Fundamentals-tier certs never expire                                                                                                                                                                                                                                                                                                                                           |
| **Teacher explanation** | Clarify upfront that this course prepares students for the current AI-901 exam, not the retired AI-900. Break down the two official skill domains and their approximate weightings: roughly 40-45% of the exam covers identifying AI concepts, workloads and responsible AI practices (concepts already built across Months 1-9), while 55-60% covers implementing AI solutions using Microsoft Foundry, including basic Python/REST/SDK usage -- which is why Months 3-4's Python skills and Month 10's API skills matter directly here, not just as general programming practice. |
| **Real-world example**  | A student who has completed Months 1-10 has already covered the great majority of AI-901's concept domain through the regular curriculum; this unit's job is targeted review and exam-specific practice, not learning the material for the first time.                                                                                                                                                                                                                                                                                                                              |
| **In-class activity**   | Students map their own Month 1-10 lecture notes against the two AI-901 skill domains, identifying which topics they feel confident on and which need the most review time across Lectures 88-92.                                                                                                                                                                                                                                                                                                                                                                                    |

**Knowledge check 1:** What was the key change between AI-900 and the current AI-901 exam?

\(A\) No real change, AI-900 and AI-901 are identical.

**(B) AI-900 retired on 30 June 2026 and was replaced by AI-901, which places heavier weight on implementing AI solutions using Microsoft Foundry, including basic coding/API skills.**

\(C\) AI-901 removed all coding content entirely.

***Correct answer: B***

**Knowledge check 2:** Roughly what proportion of the AI-901 exam covers implementing AI solutions using Microsoft Foundry, rather than identifying AI concepts?

\(A\) About 10%

**(B) Roughly 55-60%**

\(C\) 100%

***Correct answer: B***

**Evaluation question:** Using your own Month 1-10 notes, name 2 topics you feel ready for AI-901's concepts domain and 2 you want to prioritise reviewing in the implementation domain, and justify each choice.

**Homework (10-15 min):** Write your personal 6-hour study plan across Lectures 88-92, allocating more time to whichever domain your self-assessment identified as weaker.

**Teacher checklist**

**✓** Correctly states the AI-900 retirement/AI-901 replacement fact

**✓** Correctly states the approximate domain weightings

**✓** Produces a personalised, not generic, study plan

**Lecture 88 Azure AI-901: AI Concepts, Workloads and Responsible AI Review**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Review and self-test on AI-901's "AI concepts, workloads and responsible AI" domain, drawing directly on Months 1, 5 and 7 content.                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Key concepts**        | AI/ML/deep learning/generative AI terminology (Lectures 1-2) · Workload selection: matching a business need to CV/NLP/GenAI/ML (Months 5-7) · Responsible AI pillars: fairness, reliability/safety, privacy/security, inclusiveness, transparency, accountability (Lectures 6-8)                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | This is a structured review lecture, not new content: revisit the AI/ML/DL/GenAI nested-circle distinction (Lecture 2), practice matching a described business scenario to the correct workload type (e.g. 'detect defective products from factory photos' = computer vision, not NLP), and drill Microsoft's named responsible-AI pillars (fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability) against the course's own Lectures 6-8 content, since AI-901 expects these specific named pillars. |
| **Real-world example**  | A scenario "analyse thousands of customer support call transcripts to find common complaint themes" should be matched to NLP (Lecture 39-40), not computer vision or plain classical ML.                                                                                                                                                                                                                                                                                                                                                           |
| **In-class activity**   | Students complete a 10-question self-test matching business scenarios to workload types and responsible-AI pillars, drawn directly from Month 1, 5 and 7 material, then review any missed questions.                                                                                                                                                                                                                                                                                                                                               |

**Knowledge check 1:** A scenario describes using photos from factory cameras to automatically flag defective products. Which AI workload type does this match?

\(A\) Natural language processing.

**(B) Computer vision.**

\(C\) Classic regression only.

***Correct answer: B***

**Knowledge check 2:** Which of these is one of Microsoft's named responsible-AI pillars covered in Lectures 6-8?

\(A\) Profitability.

**(B) Fairness.**

\(C\) Marketability.

***Correct answer: B***

**Evaluation question:** Match 2 new business scenarios of your own invention to the correct AI workload type (CV, NLP, GenAI, or classic ML), explaining your reasoning for each.

**Homework (10-15 min):** Complete a 10-item self-test matching scenarios to workload types and responsible-AI pillars (provided), and review every item you got wrong with the relevant Month 1/5/7 lecture.

**Teacher checklist**

**✓** Correctly names all 6 responsible-AI pillars

**✓** Correctly matches scenarios to workload types, not just by guessing

**✓** Reviews missed self-test items against the specific earlier lecture, closing the gap

**Lecture 89 Azure AI-901: Microsoft Foundry, Models and AI Solution Implementation**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Describe Microsoft Foundry's role in implementing AI solutions and correctly select an appropriate model/service approach for a given scenario.                                                                                                                                                                                                                                                                                                                                         |
| **Key concepts**        | Microsoft Foundry as a platform for building/deploying AI solutions · Model catalogue and choosing an appropriate model for a task · Connecting the Month 7 (generative AI) and Month 9 (RAG) concepts to a concrete implementation platform                                                                                                                                                                                                                                            |
| **Teacher explanation** | Introduce Microsoft Foundry specifically as the implementation platform AI-901 expects candidates to recognise: a catalogue of available models, tools for building and testing an AI solution, and a way to connect a chosen model into an application -- directly connecting to the Month 7 generative-AI and Month 9 RAG concepts students already built from scratch in Python, now framed in terms of how a managed platform like Foundry would support the same kind of solution. |
| **Real-world example**  | A scenario requiring both document retrieval and generated answers (i.e. RAG, from Month 9) maps to choosing a suitable foundation model from Foundry's model catalogue plus a retrieval-augmented implementation pattern, rather than a single plain chatbot model.                                                                                                                                                                                                                    |
| **In-class activity**   | Students work through 4 scenario cards, each requiring them to pick an appropriate implementation approach (e.g. a foundation model for generation, vision model for images, RAG pattern for grounded Q&A) and briefly justify the choice.                                                                                                                                                                                                                                              |

**Knowledge check 1:** What is Microsoft Foundry's role in the AI-901 "implementing AI solutions" domain?

\(A\) It is a spreadsheet tool, unrelated to AI.

**(B) It is Microsoft's platform for selecting, building, testing and connecting AI models into a working solution.**

\(C\) It is a certification exam itself.

***Correct answer: B***

**Knowledge check 2:** A scenario needs answers grounded in a company's own private documents. Which implementation pattern, built from scratch in Month 9, is most relevant here?

\(A\) Basic clustering.

**(B) Retrieval-augmented generation (RAG).**

\(C\) Simple linear regression.

***Correct answer: B***

**Evaluation question:** Pick one of your 4 scenario cards and explain, in 3-4 sentences, why your chosen implementation approach fits that scenario better than an alternative approach would.

**Homework (10-15 min):** Write up 2 new scenarios of your own and the implementation approach (model type/pattern) you'd select for each, justifying your choice using Month 7/9 concepts.

**Teacher checklist**

**✓** Correctly describes Foundry's practical role

**✓** Scenario-to-approach matches are justified, not guessed

**✓** Connects the exam concept back to the actual Month 7/9 work already done

**Lecture 90 Azure AI-901: Python, REST APIs, SDKs, Azure Resources and Implementation Scenarios**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Apply Month 3-4 Python and Month 10 API/authentication skills to AI-901-style implementation scenario questions.                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | Mapping AI-901's "basic coding syntax" expectation to skills already built in Months 3-4 and 10 · REST API calls and SDK usage patterns (recap Lectures 23, 66-68) · Azure resource/configuration concepts at a foundational level                                                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Make explicit that AI-901's implementation domain expects recognising basic Python syntax and API call patterns -- exactly the skills built in Lectures 9-23 and 66-70, just framed around Azure-specific resources and SDK calls instead of a generic API. Work through AI-901-style scenario questions that present a short code snippet or REST call and ask what it does or what's missing, directly reusing the authentication-header pattern from Lecture 66 and the JSON-response-handling pattern from Lecture 67. |
| **Real-world example**  | An exam-style question shows a snippet calling an Azure AI service with an API key passed incorrectly in the URL instead of a header, and asks the candidate to identify the issue -- the exact mistake-and-fix pattern taught in Lecture 66.                                                                                                                                                                                                                                                                              |
| **In-class activity**   | Students work through 6 AI-901-style implementation scenario questions involving short code/REST snippets, identifying correct vs incorrect patterns using their Month 10 API skills.                                                                                                                                                                                                                                                                                                                                      |

**Knowledge check 1:** An AI-901-style question shows an API key being placed directly in a request URL rather than a header. What should a well-prepared candidate recognise?

\(A\) This is standard best practice.

**(B) This is a known poor practice (Lecture 66) -- keys belong in headers, not URLs, due to logging/exposure risk.**

\(C\) There is no issue since URLs are always private.

***Correct answer: B***

**Knowledge check 2:** Why does AI-901's implementation domain expect basic familiarity with Python/REST/SDK patterns rather than pure conceptual knowledge?

\(A\) It doesn't; AI-901 has zero coding content.

**(B) Because implementing AI solutions in practice (as opposed to just describing AI concepts) requires being able to recognise and reason about real code/API patterns used to connect to AI services.**

\(C\) Coding knowledge is only tested in AIF-C01, never AI-901.

***Correct answer: B***

**Evaluation question:** Pick one of the 6 scenario questions from the activity and explain, in your own words, why the correct answer is correct and what specific Month 10 lesson it draws on.

**Homework (10-15 min):** Attempt 6 more AI-901-style implementation scenario questions (provided) and for each wrong answer, identify exactly which earlier Python/API lecture's concept you need to revisit.

**Teacher checklist**

**✓** Correctly applies the Lecture 66 header-vs-URL key pattern to exam-style questions

**✓** Correctly reasons about REST/SDK snippets rather than guessing

**✓** Links each missed question to a specific earlier lecture for targeted review

**Lecture 91 Azure AI-901: Timed Scenario-Based Practice and Weak-Area Review**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Complete a timed set of AI-901-style scenario questions under exam-like time pressure and identify remaining weak areas before the mock exam.                                                                                                                                                                                                                                                                         |
| **Key concepts**        | Timed practice conditions (simulating real exam pacing) · Reviewing wrong answers by root cause, not just marking them wrong · Preparing a targeted weak-area list ahead of Lecture 92's mock exam                                                                                                                                                                                                                    |
| **Teacher explanation** | Run a genuinely timed practice set (e.g. 20 questions in a fixed time matching the real exam's pace) covering both AI-901 domains from Lectures 87-90, then review every wrong answer by tracing it back to its root cause -- a concept gap, a careless misread, or a specific Azure Foundry/implementation detail -- producing a short, honest weak-area list to focus remaining study time on before the mock exam. |
| **Real-world example**  | A student who rushes and misreads "NOT an example of" as "an example of" on 2 questions learns a careless-reading pattern to specifically guard against, distinct from an actual knowledge gap.                                                                                                                                                                                                                       |
| **In-class activity**   | Students complete a timed 20-question practice set, then categorise every wrong answer as either a genuine concept gap or a reading/timing mistake, producing a weak-area list for Lecture 92.                                                                                                                                                                                                                        |

**Knowledge check 1:** A student gets several questions wrong specifically because they misread negatively-phrased questions ("which is NOT...") under time pressure. What category of error is this?

\(A\) A genuine content/concept gap.

**(B) A careless-reading/timing error, distinct from a knowledge gap, and worth specifically guarding against in the real exam.**

\(C\) Proof the student doesn't understand AI-901 at all.

***Correct answer: B***

**Knowledge check 2:** Why distinguish 'concept gap' errors from 'reading/timing' errors when reviewing a timed practice set?

\(A\) There's no value in distinguishing them.

**(B) Each requires a different fix -- a concept gap needs more content review, while a reading/timing error needs a pacing or careful-reading strategy instead.**

\(C\) All wrong answers should be treated identically regardless of cause.

***Correct answer: B***

**Evaluation question:** Report your timed practice set's score and your weak-area list, categorising each wrong answer as a concept gap or a reading/timing error.

**Homework (10-15 min):** Review every concept-gap item on your weak-area list against its specific earlier lecture, and complete one more timed practice set to check for improvement.

**Teacher checklist**

**✓** Practice is genuinely completed under a real time constraint

**✓** Every wrong answer is categorised by root cause, not just marked wrong

**✓** Weak-area list is specific and actionable for the Lecture 92 mock exam

**Lecture 92 Azure AI-901: Mock Exam, Review and Remediation**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Complete a full-length AI-901 mock exam under real exam conditions, score it against the 700/1000 passing bar, and complete targeted remediation on any remaining weak areas.                                                                                                                                                                                                                                                                                                 |
| **Key concepts**        | Full-length mock exam matching real AI-901 format and timing · Passing score 700/1000 · Remediation plan for any domain scoring below target                                                                                                                                                                                                                                                                                                                                  |
| **Teacher explanation** | Run a complete, full-length mock exam under realistic conditions (no notes, timed, same approximate question count and domain split as the real AI-901). Score it against the real passing bar of 700/1000, break the score down by domain (concepts vs implementation) to see which domain, if any, falls short, and spend the remainder of the lecture on targeted remediation specifically for the weaker domain, using the Lecture 91 weak-area list as a starting point. |
| **Real-world example**  | A student scores 760/1000 overall but only 620/1000-equivalent on the implementation domain specifically -- the remediation plan should concentrate the remaining AI-901 study time on Foundry/API-related content (Lectures 89-90), not restudy the already-strong concepts domain.                                                                                                                                                                                          |
| **In-class activity**   | Students complete the full mock exam, calculate their domain-level breakdown, and write a 1-paragraph remediation plan naming specific lectures to revisit for any domain below the 700/1000 bar.                                                                                                                                                                                                                                                                             |

**Knowledge check 1:** What is the actual passing score threshold for the real AI-901 exam?

\(A\) 500/1000

**(B) 700/1000**

\(C\) There is no fixed passing score.

***Correct answer: B***

**Knowledge check 2:** A student's mock exam shows strong concepts-domain performance but weak implementation-domain performance. What should their remediation plan prioritise?

\(A\) Re-studying the concepts domain, since it's already their strongest area.

**(B) Focused review of the implementation domain (Foundry, models, APIs/SDKs -- Lectures 89-90), since that's where the actual gap is.**

\(C\) Taking the real exam immediately regardless of the domain breakdown.

***Correct answer: B***

**Evaluation question:** Report your mock exam's overall score against the 700/1000 bar and your domain-level breakdown, and state your specific remediation priority based on that breakdown.

**Homework (10-15 min):** Complete your remediation plan's recommended review for your weakest domain, and note your confidence level for attempting the real AI-901 exam.

**Teacher checklist**

**✓** Mock exam is completed under genuine timed, unaided conditions

**✓** Score is correctly interpreted against the real 700/1000 passing bar

**✓** Remediation plan is domain-specific and evidence-based, not generic

**Official Certification Exam Window — Microsoft Azure AI Fundamentals (AI-901)**

|              |                                                                                                                                                                        |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 65 (AIF-C01) or variable (AI-901) scenario-based questions, timed, delivered under the real certification exam format and conditions described in Lectures 87/93.      |
| **Coverage** | Lectures 87-92: full AI-901 exam structure, concepts/workloads/responsible AI, Foundry implementation, Python/REST/SDK scenarios, timed practice, and final mock exam. |

**Lecture 93 AWS AIF-C01: Exam Structure, Domain Weightings and Study Plan**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Describe the AIF-C01 exam's five domains and their exact weightings, and build a personal 6-hour study plan across Lectures 94-98.                                                                                                                                                                                                                                                                                                                                                                           |
| **Key concepts**        | 5 scored domains: Fundamentals of AI/ML (20%), Fundamentals of GenAI (24%), Applications of Foundation Models (28%), Guidelines for Responsible AI (14%), Security/Compliance/Governance (14%) · 65 questions (50 scored + 15 unscored), 90 minutes, pass 700/1000 · Foundational-tier exam, candidates 13+ permitted with guardian consent                                                                                                                                                                  |
| **Teacher explanation** | Lay out AIF-C01's exact structure: 5 scored domains weighted 20/24/28/14/14%, delivered as 65 total questions (50 scored, 15 unscored for future exam calibration) in 90 minutes, with a 700/1000 passing score -- directly comparable to AI-901's structure just covered, which helps students see the parallel rather than treating this as an unrelated new system. Note this is the AWS foundational tier, appropriate for the course's age group under AWS's teen testing policy with guardian consent. |
| **Real-world example**  | Since Applications of Foundation Models carries the heaviest weighting at 28%, a student's 6-hour study plan across this unit should allocate more time to Lecture 95 (which covers that domain) than to the lighter-weighted responsible-AI or security domains.                                                                                                                                                                                                                                            |
| **In-class activity**   | Students build their personal 6-hour study plan across Lectures 94-98, weighting their planned review time roughly in proportion to each domain's exam weighting, using the actual percentages.                                                                                                                                                                                                                                                                                                              |

**Knowledge check 1:** Which AIF-C01 domain carries the single highest exam weighting?

\(A\) Guidelines for Responsible AI (14%).

**(B) Applications of Foundation Models (28%).**

\(C\) Security, Compliance and Governance (14%).

***Correct answer: B***

**Knowledge check 2:** How many total questions does the AIF-C01 exam have, and how many of those are scored?

**(A) 65 total, 50 scored.**

\(B\) 100 total, 100 scored.

\(C\) 10 total, 5 scored.

***Correct answer: A***

**Evaluation question:** Explain why allocating study time roughly in proportion to each domain's weighting (rather than equally across all 5) is a more efficient use of limited preparation time.

**Homework (10-15 min):** Write your personal 6-hour study plan across Lectures 94-98, explicitly weighting time allocation using the real domain percentages.

**Teacher checklist**

**✓** Correctly states all 5 domain names and weightings

**✓** Correctly states the 65-question/90-minute/700-pass-score exam structure

**✓** Study plan allocation is proportional to actual domain weighting, not equal split

**Lecture 94 AWS AIF-C01: AI/ML Lifecycle, Generative AI, Foundation Models and Prompt Engineering**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Review AIF-C01's two heaviest early domains (Fundamentals of AI/ML, 20%, and Fundamentals of GenAI, 24%) using Months 5, 7 and 8 content.                                                                                                                                                                                                                                                                                                                               |
| **Key concepts**        | AI/ML lifecycle terminology (recap Month 5: features/labels, training, evaluation) · Generative AI/foundation model terminology (recap Month 7) · Prompt engineering as explicitly examinable content (recap Month 8)                                                                                                                                                                                                                                                   |
| **Teacher explanation** | This review lecture maps directly onto two exam domains at once: Domain 1 (Fundamentals of AI/ML, 20%) draws on Month 5's full ML pipeline vocabulary (features, labels, training/test split, overfitting, evaluation metrics), while Domain 2 (Fundamentals of GenAI, 24%) draws on Month 7's tokens/foundation models/limitations content plus Month 8's prompt-engineering techniques -- which AIF-C01 explicitly tests as exam content, not just a practical skill. |
| **Real-world example**  | An exam-style question asking which prompting technique (zero-shot vs few-shot, Lecture 53) would most help ensure consistent output format maps directly to AIF-C01's GenAI domain content, not a separate unrelated topic.                                                                                                                                                                                                                                            |
| **In-class activity**   | Students complete a 12-question self-test split across Domain 1 and Domain 2 terminology, drawn from Month 5, 7 and 8 vocabulary, and review any missed items against the specific source lecture.                                                                                                                                                                                                                                                                      |

**Knowledge check 1:** An exam-style AIF-C01 question asks which technique would most help a model produce consistently-formatted outputs. Which Month 8 concept is most relevant?

\(A\) K-means clustering.

**(B) Few-shot prompting with example input/output pairs (Lecture 53).**

\(C\) Train/test splitting.

***Correct answer: B***

**Knowledge check 2:** A model scoring very differently on training versus test data (Lecture 34's overfitting concept) falls under which AIF-C01 domain?

**(A) Fundamentals of AI and ML (Domain 1).**

\(B\) Security, Compliance and Governance (Domain 5).

\(C\) This concept is not covered by AIF-C01 at all.

***Correct answer: A***

**Evaluation question:** Pick 2 self-test items you answered correctly and explain which specific Month 5 or Month 7/8 lecture gave you that knowledge.

**Homework (10-15 min):** Complete a 12-item self-test on Domain 1 and Domain 2 terminology (provided), reviewing every missed item against its specific source lecture.

**Teacher checklist**

**✓** Correctly maps ML-lifecycle terms to Domain 1

**✓** Correctly maps GenAI/prompting terms to Domain 2

**✓** Reviews missed items against the specific earlier lecture, not generically

**Lecture 95 AWS AIF-C01: Foundation Model Applications, RAG, Agents and AWS AI Services**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Review AIF-C01's heaviest domain (Applications of Foundation Models, 28%) using Month 9-10 RAG/agent content plus named AWS AI services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | Domain 3: Applications of Foundation Models (28%) -- the single heaviest domain · RAG, embeddings, agents/tool use (recap Months 9-10) · Recognising named AWS AI services at a foundational level: Bedrock, SageMaker AI, Rekognition, Textract, Comprehend, Lex, Polly, Transcribe, Translate                                                                                                                                                                                                                                                                                                                                                                                 |
| **Teacher explanation** | Given this domain's 28% weighting -- the largest of all five -- spend real time here: review RAG architecture (Lecture 62) and agent tool-calling (Lecture 71) as directly examinable content, then introduce the specific named AWS AI services AIF-C01 expects candidates to recognise at a foundational level (what each does, not how to configure it): Bedrock (foundation model access), SageMaker AI (ML model building/training), Rekognition (computer vision), Textract (document/OCR extraction -- compare to Lecture 38), Comprehend (NLP), Lex (conversational interfaces), Polly (text-to-speech), Transcribe (speech-to-text), Translate (language translation). |
| **Real-world example**  | An exam-style question describing 'extracting text and form data from scanned documents' should be matched to Amazon Textract, drawing the same OCR concept taught generically in Lecture 38 but now as a specific named AWS service.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **In-class activity**   | Students complete a matching exercise pairing 9 described tasks to the correct named AWS AI service, then review the RAG/agent architecture diagrams from Lectures 62 and 71 as exam-ready summaries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

**Knowledge check 1:** A scenario describes needing to extract printed text and form fields from scanned invoices. Which AWS service matches this foundational-level description?

\(A\) Amazon Polly.

**(B) Amazon Textract.**

\(C\) Amazon Translate.

***Correct answer: B***

**Knowledge check 2:** Why does Domain 3 (Applications of Foundation Models) carry the heaviest weighting (28%) of all 5 AIF-C01 domains?

\(A\) It doesn't; all domains are weighted equally.

**(B) It reflects AWS's emphasis on practical application of foundation models (RAG, agents, model choice) as the most heavily tested area of the exam.**

\(C\) This domain covers only responsible AI topics.

***Correct answer: B***

**Evaluation question:** Pick 2 of the 9 AWS services from the matching exercise and explain, in your own words, what foundational-level task each one solves.

**Homework (10-15 min):** Complete the 9-item AWS-service matching exercise (provided) and write a one-line foundational description of each of the 9 named services in your own words.

**Teacher checklist**

**✓** Correctly matches described tasks to the right named AWS service

**✓** Can explain why Domain 3 is weighted most heavily

**✓** RAG/agent architecture recall is accurate, matching Lectures 62/71

**Lecture 96 AWS AIF-C01: Responsible AI, Security, Compliance and Governance**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Review AIF-C01's Domain 4 (Responsible AI, 14%) and Domain 5 (Security/Compliance/Governance, 14%) using Months 2 and 11 content.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Key concepts**        | Domain 4: bias, fairness, explainability, privacy, safety, robustness, human oversight (recap Lectures 6-8) · Domain 5: credential protection, access control, data privacy, governance, compliance, logging (recap Lecture 69, 79, 83, 85) · Why AWS treats these as two separate, equally-weighted domains                                                                                                                                                                                                                                         |
| **Teacher explanation** | Review both remaining domains together since they're equally weighted at 14% each: Domain 4 draws directly on Lectures 6-8's bias/fairness/hallucination/responsible-AI content, now framed with AWS's own terminology (explainability, robustness, human oversight); Domain 5 draws on the full security thread built across Month 10-11 (secure API key storage, input validation, logging, the Lecture 85 security audit) -- reinforcing that 'responsible AI' and 'security/governance' are related but distinct concern areas on the real exam. |
| **Real-world example**  | A question about whether a hiring-screening model is unfairly biased against one demographic group maps to Domain 4 (Responsible AI), while a question about whether API credentials are stored securely maps to Domain 5 (Security/Compliance/Governance) -- a useful real distinction to practice recognising under exam conditions.                                                                                                                                                                                                               |
| **In-class activity**   | Students complete a 10-question sorting exercise classifying each described scenario as Domain 4 or Domain 5, then review any misclassification against the specific earlier course lecture that covers it.                                                                                                                                                                                                                                                                                                                                          |

**Knowledge check 1:** A scenario describes an AI model that performs worse for one demographic group due to unrepresentative training data. Which AIF-C01 domain does this fall under?

\(A\) Domain 5: Security, Compliance and Governance.

**(B) Domain 4: Guidelines for Responsible AI.**

\(C\) Domain 1: Fundamentals of AI and ML only.

***Correct answer: B***

**Knowledge check 2:** A scenario describes an AI application accidentally logging user API keys in plain text. Which domain does this fall under?

\(A\) Domain 4: Guidelines for Responsible AI.

**(B) Domain 5: Security, Compliance and Governance.**

\(C\) This isn't covered by any AIF-C01 domain.

***Correct answer: B***

**Evaluation question:** Explain, using your own invented scenario, the practical difference between a Domain 4 (responsible AI) issue and a Domain 5 (security/governance) issue.

**Homework (10-15 min):** Complete the 10-item Domain 4/5 sorting exercise (provided) and review every misclassified item against the specific earlier course lecture (6-8 or 69/79/83/85) that covers it.

**Teacher checklist**

**✓** Correctly distinguishes Domain 4 (responsible AI) from Domain 5 (security/governance) scenarios

**✓** Reviews mistakes against the specific earlier lecture, not generically

**✓** Can give an original example of each domain, not just a repeated class example

**Lecture 97 AWS AIF-C01: Timed Practice Questions and Weak-Area Review**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Complete a timed set of AIF-C01-style questions spanning all 5 domains, weighted to match the real exam's domain proportions, and build a weak-area list.                                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | Timed practice matching real exam proportions (20/24/28/14/14 split) · Root-cause review of wrong answers by domain · Preparing for Lecture 98's mock exam                                                                                                                                                                                                                                                                                                       |
| **Teacher explanation** | Run a genuinely timed practice set of questions distributed across all 5 domains in roughly the real exam's proportions (more questions on Domain 3, fewer on Domains 4-5), mirroring Lecture 91's AI-901 practice approach but now for AIF-C01's 5-domain structure. Review every wrong answer, categorising by domain and by root cause (concept gap vs careless reading), to produce a domain-by-domain weak-area list heading into the Lecture 98 mock exam. |
| **Real-world example**  | A student who performs well on Domains 1-2 but struggles specifically on Domain 3 (Applications of Foundation Models) questions about agent tool-selection should prioritise reviewing Lecture 71's agent decision-making content specifically, not restudy already-strong areas.                                                                                                                                                                                |
| **In-class activity**   | Students complete a proportionally-weighted timed practice set across all 5 domains, then build a domain-by-domain weak-area list categorising each wrong answer by root cause.                                                                                                                                                                                                                                                                                  |

**Knowledge check 1:** Why should a timed AIF-C01 practice set include more Domain 3 questions than Domain 4 or 5 questions?

\(A\) It shouldn't; all domains should have equal numbers of questions regardless of real exam weighting.

**(B) To realistically mirror the actual exam's weighting (28% vs 14% each), so practice conditions match the real test's proportions.**

\(C\) Domain 3 is the only domain that matters.

***Correct answer: B***

**Knowledge check 2:** A student's weak-area list shows consistent struggles specifically with Domain 3 questions about agent tool-selection. What should their remediation prioritise?

\(A\) General review of all 5 domains equally.

**(B) Targeted review of Lecture 71's agent/tool-calling content specifically, since that's the identified specific gap.**

\(C\) Skipping Domain 3 entirely on the real exam.

***Correct answer: B***

**Evaluation question:** Report your timed practice set's domain-by-domain performance and identify your single weakest domain with supporting evidence from your results.

**Homework (10-15 min):** Review your weakest domain's specific missed questions against their source lectures, and complete one more timed practice set to check for improvement in that domain.

**Teacher checklist**

**✓** Practice set proportions roughly mirror the real exam's domain weightings

**✓** Weak-area list is domain-specific and root-cause categorised

**✓** Remediation priority is evidence-based from actual practice results

**Lecture 98 AWS AIF-C01: Mock Exam, Review and Remediation**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Complete a full-length AIF-C01 mock exam under real exam conditions (65 questions, 90 minutes), score it against the 700/1000 bar by domain, and complete targeted remediation.                                                                                                                                                                                                                                                                                                                                                  |
| **Key concepts**        | Full-length mock exam matching the real 65-question/90-minute format · Domain-level score breakdown against the 700/1000 passing bar · Final remediation plan before the real certification attempts (both AI-901 and AIF-C01)                                                                                                                                                                                                                                                                                                   |
| **Teacher explanation** | Run the complete, full-length mock exam under realistic timed conditions matching the real AIF-C01 format exactly (65 questions, 90 minutes). Score it overall against the 700/1000 passing bar, break the result down by all 5 domains to see exactly where any remaining gap sits, and use the rest of the lecture for final, domain-targeted remediation -- this is the last dedicated certification-prep lecture before Month 12 shifts fully to the capstone project, so any remaining weak domain should be addressed now. |
| **Real-world example**  | A student scoring comfortably above 700/1000 overall but noticeably lower specifically on Domain 5 (Security/Compliance/Governance) should spend their final remaining prep time reviewing Lectures 69/79/83/85's security content, rather than broadly re-reviewing everything.                                                                                                                                                                                                                                                 |
| **In-class activity**   | Students complete the full 65-question/90-minute mock exam, calculate their 5-domain score breakdown, and write a final remediation plan for their single weakest domain, including a specific next action.                                                                                                                                                                                                                                                                                                                      |

**Knowledge check 1:** The real AIF-C01 exam has how many total questions and how long is it?

**(A) 65 questions, 90 minutes.**

\(B\) 20 questions, 30 minutes.

\(C\) 200 questions, 4 hours.

***Correct answer: A***

**Knowledge check 2:** A mock exam shows an overall score of 740/1000 (above the 700 pass bar) but one domain scoring well below the others. What is the sensible final step?

\(A\) No further action is needed since the overall score already passes.

**(B) Still review that specific weak domain, since real exam variability means a comfortable overall margin isn't a guarantee, and understanding the material well matters beyond just passing.**

\(C\) Stop all further preparation immediately.

***Correct answer: B***

**Evaluation question:** Report your mock exam's overall score and domain breakdown, and state your specific final remediation action based on your weakest domain.

**Homework (10-15 min):** Complete your final domain-specific remediation review, and write a short reflection on your readiness for the real AI-901 and AIF-C01 certification exams.

**Teacher checklist**

**✓** Mock exam matches the real 65-question/90-minute format and is completed under genuine timed conditions

**✓** Domain breakdown is correctly calculated and interpreted

**✓** Final remediation plan is specific, evidence-based, and actually completed

**Official Certification Exam Window — AWS Certified AI Practitioner (AIF-C01)**

|              |                                                                                                                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Format**   | 65 (AIF-C01) or variable (AI-901) scenario-based questions, timed, delivered under the real certification exam format and conditions described in Lectures 87/93.                                      |
| **Coverage** | Lectures 93-98: full AIF-C01 exam structure and domain weightings, AI/ML/GenAI fundamentals, foundation model applications/AWS services, responsible AI/security, timed practice, and final mock exam. |

**Lecture 99 Capstone Problem Definition, Success Criteria and Architecture**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Define the final capstone project's problem statement, measurable success criteria, and architecture, applying the full Month 11 discipline to a final, more ambitious project.                                                                                                                                                                                                                                                                                                                                |
| **Key concepts**        | Reapplying Lecture 75's requirements discipline and Lecture 76's architecture design to the final capstone · Choosing a project ambitious enough to showcase the full year's skills · Defining what 'graduation-ready' means for this specific project                                                                                                                                                                                                                                                         |
| **Teacher explanation** | Launch the final capstone with the same discipline built in Month 11, now at a larger scale: students choose (or finalise, if already planned) a final project that meaningfully draws on at least 3 distinct skill areas from across the year (e.g. Python + an LLM API + RAG, or ML + a deployed application), write a clear problem statement and measurable success criteria (Lecture 75's pattern), and sketch the full component architecture (Lecture 76's pattern) before any further building begins. |
| **Real-world example**  | A final capstone combining a RAG-based study assistant (Month 9) with a simple deployed web interface (Month 11) and basic usage logging (Lecture 73/83) -- deliberately drawing on 3 distinct skill areas rather than repeating a single earlier project almost unchanged.                                                                                                                                                                                                                                    |
| **In-class activity**   | Students write their final capstone's problem statement, measurable success criteria, and component architecture diagram, explicitly naming which 3+ skill areas from the year it will draw on.                                                                                                                                                                                                                                                                                                                |

**Knowledge check 1:** Why does the capstone project specifically require combining at least 3 distinct skill areas from across the year, rather than being a close repeat of one earlier mini-project?

\(A\) There's no real reason; any project is equally acceptable.

**(B) A capstone meant to demonstrate graduation-readiness should showcase integrated use of multiple skill areas built across the year, not just one isolated skill in the same shape as before.**

\(C\) Combining skill areas is impossible at this stage.

***Correct answer: B***

**Knowledge check 2:** What should happen before any further capstone building begins, based on this lecture?

\(A\) Jump straight into writing code.

**(B) Write a clear problem statement, measurable success criteria, and a component architecture diagram, exactly as practiced in Lectures 75-76.**

\(C\) Nothing needs to be planned in advance.

***Correct answer: B***

**Evaluation question:** Present your capstone's problem statement, success criteria, and architecture diagram, explicitly naming the 3+ skill areas it will integrate.

**Homework (10-15 min):** Finalise your capstone's full planning documentation (problem statement, success criteria, architecture) ready to begin implementation in Lecture 100.

**Teacher checklist**

**✓** Project genuinely integrates 3+ distinct skill areas from across the year

**✓** Success criteria are measurable, following the Lecture 75 standard

**✓** Architecture diagram is complete before implementation begins

**Lecture 100 Capstone Implementation and Integration**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Implement the planned capstone project, integrating its multiple components into a working whole.                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Key concepts**        | Applying Month 11's structured project habits (clean file structure, secure keys, error handling) to the final build · Integrating multiple skill areas into one working system · Tracking progress against the Lecture 99 plan                                                                                                                                                                                                                                                                       |
| **Teacher explanation** | This is the main dedicated build lecture: students implement their Lecture 99 architecture, applying every structural habit built in Month 11 -- clean multi-file structure (Lecture 77), secure key handling (Lecture 69), input validation (Lecture 80), and basic error handling (Lecture 68) -- while tracking their actual progress against the planned architecture and flagging any component that needs to be simplified or adjusted from the original plan as real build constraints appear. |
| **Real-world example**  | A student building a RAG-plus-deployment capstone discovers during implementation that their originally planned chunking strategy (Lecture 59) doesn't retrieve well for their specific document set, and adjusts the chunk size based on that real, observed evidence rather than forcing the original plan.                                                                                                                                                                                         |
| **In-class activity**   | Students spend the lecture implementing their capstone's core components, applying Month 11's structural/security habits, and documenting any deviation from the original Lecture 99 plan with a reason.                                                                                                                                                                                                                                                                                              |

**Knowledge check 1:** During implementation, a student finds their planned architecture needs a specific adjustment based on real build results. What is the correct response?

\(A\) Force the original plan exactly regardless of evidence, even if it clearly isn't working.

**(B) Adjust the plan based on the real evidence encountered, documenting the change and the reason for it.**

\(C\) Abandon the project entirely at the first sign of a needed adjustment.

***Correct answer: B***

**Knowledge check 2:** Which Month 11 habits should be applied during this capstone implementation lecture?

\(A\) None; the capstone is exempt from earlier structural practices.

**(B) Clean multi-file structure, secure key handling, input validation and error handling, exactly as practiced throughout Month 11.**

\(C\) Only the UI design, nothing else from Month 11.

***Correct answer: B***

**Evaluation question:** Describe your implementation progress so far and any deviation from your original Lecture 99 plan, with your reasoning for the change.

**Homework (10-15 min):** Continue implementing your capstone toward a fully integrated, working version, applying Month 11's structural and security habits throughout.

**Teacher checklist**

**✓** Implementation genuinely follows (or deliberately, documented-ly adapts) the Lecture 99 architecture

**✓** Month 11 structural/security habits are visibly applied, not skipped

**✓** Any plan deviation is documented with a real reason, not left unexplained

**Lecture 101 Capstone Testing, Evaluation and Error Analysis**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Test the implemented capstone, evaluate it against the Lecture 99 success criteria, and conduct a root-cause error analysis on any failures found.                                                                                                                                                                                                                                                                                                                                                        |
| **Key concepts**        | Applying Lecture 81's testing and Lecture 82's evaluation discipline to the final capstone · Error analysis: tracing a failure to its specific root cause, not just noting that it failed · Honest reporting of the evaluation result                                                                                                                                                                                                                                                                     |
| **Teacher explanation** | Apply the full Month 11 testing/evaluation discipline to the finished (or near-finished) capstone: write and run tests for key functions (Lecture 81), then evaluate the whole system against the original Lecture 99 success criteria using real test cases (Lecture 82's pattern). For any failure found, perform root-cause error analysis -- tracing exactly which component or stage caused the failure, as practiced for RAG pipelines in Lecture 64 -- rather than simply noting 'it didn't work.' |
| **Real-world example**  | A capstone's success criterion of '85% accurate generated answers' is actually measured at 68%; error analysis traces most of the failures to the retrieval stage returning irrelevant chunks for a specific type of question, pointing to a specific, fixable cause rather than a vague 'the AI isn't good enough.'                                                                                                                                                                                      |
| **In-class activity**   | Students run their evaluation set against their capstone, calculate the actual result against their Lecture 99 success criterion, and perform root-cause error analysis on any failing cases found.                                                                                                                                                                                                                                                                                                       |

**Knowledge check 1:** A capstone's evaluation shows a lower-than-target success rate. What is the appropriate next step, based on this lecture's standard?

\(A\) Report the shortfall with no further investigation.

**(B) Perform root-cause error analysis to trace the shortfall to a specific component or stage, so it can be meaningfully addressed.**

\(C\) Change the original success criterion retroactively to match whatever score was achieved.

***Correct answer: B***

**Knowledge check 2:** Why is tracing a failure to a specific stage (e.g. retrieval vs generation, as in Lecture 64) more useful than just noting the overall result fell short?

\(A\) It isn't more useful; the overall number is all that matters.

**(B) A specific root cause points to an actual, targeted fix, whereas a vague 'it fell short' gives no direction for improvement.**

\(C\) Root-cause analysis is only possible for RAG projects, not other capstone types.

***Correct answer: B***

**Evaluation question:** Report your capstone's actual evaluation result against your Lecture 99 success criterion, and describe your root-cause analysis of the largest contributing failure, if any.

**Homework (10-15 min):** Complete your full evaluation and error analysis, documenting the actual result, the root cause of any shortfall, and your planned fix heading into Lecture 102.

**Teacher checklist**

**✓** Evaluation measures against the specific original success criterion

**✓** At least one failure (if present) is traced to a specific root cause, not left vague

**✓** Result is reported honestly, including any shortfall

**Lecture 102 Capstone Improvements, Limitations and Responsible Use**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Apply at least one evidence-based improvement from the Lecture 101 error analysis, and write an honest, specific limitations and responsible-use statement for the finished project.                                                                                                                                                                                                                                                                                                                                                                                          |
| **Key concepts**        | Applying a targeted fix based on root-cause analysis · Writing a genuine limitations statement (not a generic disclaimer) · Responsible-use considerations specific to this project (recap Month 2 and 7-8 habits)                                                                                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | Close the loop on Lecture 101's error analysis: implement at least one concrete fix targeting the specific root cause identified (e.g. adjusting chunk size, adding a validation check, improving a prompt), and re-run the evaluation to check whether the fix actually improved the result. Then write a genuine limitations statement specific to this project -- not a generic AI disclaimer -- and a responsible-use note addressing what this particular application should and shouldn't be relied on for, drawing on the Month 2 and Month 7-8 responsible-AI habits. |
| **Real-world example**  | After fixing a retrieval chunking issue identified in Lecture 101, a student's accuracy improves from 68% to 81%; their limitations statement specifically notes that the assistant still struggles with multi-part questions spanning more than one document chunk, rather than a vague "AI can make mistakes."                                                                                                                                                                                                                                                              |
| **In-class activity**   | Students implement their chosen fix, re-run their evaluation to measure the actual before/after improvement, and write a specific limitations and responsible-use statement for their own project.                                                                                                                                                                                                                                                                                                                                                                            |

**Knowledge check 1:** Why is a limitations statement like "This assistant may struggle with questions spanning more than one document chunk" more valuable than a generic "AI can make mistakes" disclaimer?

\(A\) There is no real difference in value.

**(B) The specific statement tells a future user exactly what kind of failure to watch for, which is actionable; a generic disclaimer gives no real guidance.**

\(C\) Generic disclaimers are always preferred for legal reasons regardless of usefulness.

***Correct answer: B***

**Knowledge check 2:** After applying a fix to a root-cause issue identified in Lecture 101, what should happen next?

\(A\) Assume the fix worked without checking.

**(B) Re-run the evaluation to measure whether the fix actually produced a measurable improvement.**

\(C\) Nothing further; applying a fix is sufficient by itself.

***Correct answer: B***

**Evaluation question:** Report your before-and-after evaluation results from your applied fix, and present your project's specific limitations and responsible-use statement.

**Homework (10-15 min):** Finalise your fix, confirm the before/after improvement with real numbers, and write your project's final limitations and responsible-use statement for inclusion in your presentation.

**Teacher checklist**

**✓** At least one real, evidence-based fix is implemented and re-evaluated

**✓** Limitations statement is specific to this project, not generic boilerplate

**✓** Responsible-use note draws genuinely on the course's earlier responsible-AI content

**Lecture 103 Final Presentation Preparation and Portfolio Review**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Prepare a clear final capstone presentation and assemble a complete, well-documented portfolio of the year's GitHub projects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Key concepts**        | Structuring a clear project presentation (problem, approach, result, limitations) · Reviewing and tidying the full year's GitHub portfolio (recap Lecture 26's documentation habit, applied across every project) · Presenting evaluation evidence, not just a demo                                                                                                                                                                                                                                                                                                                               |
| **Teacher explanation** | Guide presentation preparation using a clear structure: problem and motivation, approach/architecture, a live or recorded demo, evaluation evidence (the actual Lecture 101-102 numbers, not just a claim), and the honest limitations statement. In parallel, review the student's full-year GitHub portfolio built up since Lecture 26, ensuring every major project has a clear README (purpose, data/approach, limitations) so the portfolio reads as a coherent, well-documented body of work -- directly addressing the course's stated graduate outcome of presenting a portfolio project. |
| **Real-world example**  | A portfolio reviewer should be able to open any of the year's pushed repositories and understand, from the README alone, what it does, how it was built, and what its limitations are, without needing the student to explain it in person.                                                                                                                                                                                                                                                                                                                                                       |
| **In-class activity**   | Students draft their final presentation using the 5-part structure and review all of their GitHub repositories from across the year, fixing any README that doesn't clearly cover purpose, approach and limitations.                                                                                                                                                                                                                                                                                                                                                                              |

**Knowledge check 1:** Why must the final presentation include actual evaluation evidence (the Lecture 101-102 numbers) rather than just a live demo?

\(A\) A live demo alone is always sufficient proof of quality.

**(B) A demo shows the system can work in one instance; evaluation evidence shows how reliably it actually performs, which is the more complete and honest picture.**

\(C\) Evaluation evidence is optional and only for extra credit.

***Correct answer: B***

**Knowledge check 2:** What should a reviewer be able to learn just from reading a portfolio project's README, without the student explaining it in person?

\(A\) Nothing useful; READMEs are purely decorative.

**(B) What the project does, its approach/data, and its known limitations -- exactly the Lecture 26 documentation habit applied consistently.**

\(C\) Only the student's name and the date.

***Correct answer: B***

**Evaluation question:** Outline your 5-part final presentation structure for your own capstone, and report on the state of your GitHub portfolio review (what you fixed, if anything).

**Homework (10-15 min):** Finalise your presentation and ensure every project README in your GitHub portfolio clearly covers purpose, approach and limitations before the final graduation presentation.

**Teacher checklist**

**✓** Presentation structure includes problem, approach, demo, evaluation evidence, and limitations

**✓** Portfolio READMEs are reviewed and fixed where incomplete

**✓** Evaluation evidence presented is the actual measured result, not an unverified claim

**Lecture 104 Final Capstone Presentation, Practical Assessment and Graduation**

*Month 12 · Cloud AI, Final Capstone & Graduation · 1 guided hour + 10-15 min homework*

|                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Learning outcome**    | Deliver the final capstone presentation, complete the practical assessment, and graduate with a complete, well-documented AI portfolio.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Key concepts**        | Delivering the final presentation (Lecture 103's structure) · Practical assessment: demonstrating the application live and answering questions about its design and limitations · Graduation: consolidating one year of AI Foundations -\> AI Application -\> AI Creator skill progression                                                                                                                                                                                                                                                                                            |
| **Teacher explanation** | This final lecture is the graduation event: each student delivers their prepared presentation (problem, approach, demo, evaluation evidence, limitations), and completes a practical assessment by answering direct questions about their project's design choices, evaluation results, and known limitations -- testing genuine understanding, not a memorised script. Close the year by explicitly reviewing the full skill progression from Lecture 1's "what is AI" through to a self-built, evaluated, deployed, documented AI application, marking graduation from the program. |
| **Real-world example**  | A graduating student who, when asked "why did you choose RAG instead of fine-tuning for your assistant," can give a genuine, reasoned answer grounded in Month 7/9 concepts, rather than reciting a prepared line -- demonstrating real understanding rather than surface-level completion.                                                                                                                                                                                                                                                                                           |
| **In-class activity**   | Each student delivers their final presentation and practical assessment to the class/assessors, fielding genuine questions about their design choices, results and limitations.                                                                                                                                                                                                                                                                                                                                                                                                       |

**Knowledge check 1:** What is the main purpose of the practical assessment's direct questions about a student's project design and limitations?

\(A\) To catch students out unfairly.

**(B) To verify genuine understanding of the project's design and results, rather than accepting a successful demo alone as proof of understanding.**

\(C\) They serve no real assessment purpose beyond formality.

***Correct answer: B***

**Knowledge check 2:** A graduating student should be able to explain, in their own words, why they chose their project's specific approach (e.g. RAG over fine-tuning). What does this demonstrate?

\(A\) Nothing beyond memorisation.

**(B) Genuine understanding of the underlying concepts (Months 7-9) applied to a real design decision, not just the ability to follow a tutorial.**

\(C\) That the student memorised a script perfectly.

***Correct answer: B***

**Evaluation question:** Reflecting on your full year, name one concept from early in the course (Months 1-4) that directly enabled something you built in your final capstone, and explain the connection.

**Homework (10-15 min):** No new homework -- use this time to ensure your GitHub portfolio and final project documentation are complete and ready to share as your AI Foundations, AI Application and AI Creator portfolio going forward.

**Teacher checklist**

**✓** Presentation and practical assessment both completed

**✓** Student demonstrates genuine understanding of design choices under direct questioning, not a memorised script

**✓** Final GitHub portfolio is complete and ready to be shared beyond the course

**The Certifications We Provide: Cost and Market Value in India**

This course delivers two built-in, industry-recognised certifications as part of Month 12: Microsoft Azure AI Fundamentals (AI-901) and AWS Certified AI Practitioner (AIF-C01). Neither vendor publishes a fixed India-specific rupee price; both price in USD worldwide. The INR figures below are approximate conversions at a recent exchange rate and will drift as the rupee moves — always confirm the exact current fee on the vendor's own registration page before a student books an exam.

| **Certification**                            | **Official USD fee**   | **Approx. INR (at ~₹96/USD)** | **Validity**                                                   |
|----------------------------------------------|------------------------|-------------------------------|----------------------------------------------------------------|
| **Microsoft Azure AI Fundamentals (AI-901)** | \$99                   | **≈ ₹9,500**                  | Never expires (fundamentals-tier certifications do not expire) |
| **AWS Certified AI Practitioner (AIF-C01)**  | \$100 (flat worldwide) | **≈ ₹9,600**                  | 3 years, then recertification required                         |

Who sits each exam and when

| **Exam**               | **Eligibility for this course's age group**                                                                                                                                                           |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AI-901 (Microsoft)** | No vendor-stated minimum age restriction; taught and sat in Lectures 87-92 of Month 12.                                                                                                               |
| **AIF-C01 (AWS)**      | AWS's Teen Testing Policy permits candidates aged 13-17 with parent/guardian consent, which is why this exam is appropriate at this course's age group; taught and sat in Lectures 93-98 of Month 12. |

**What these two certifications are worth**

Both are entry-level, vendor-issued "fundamentals/foundational" tier certifications — they are not expected to replace a degree or years of experience, but they give a graduating student two concrete, resume-visible, third-party-verified credentials that confirm genuine AI/ML and generative-AI literacy at the point many entry-level screening processes now look for exactly this signal (per the job-postings research earlier in this program's planning). Their real market value is as a credible, low-cost first proof point alongside the student's GitHub portfolio built across this course — not as a standalone guarantee of employment.

A genuine caveat: certification exam fees, formats and syllabi are set by Microsoft and AWS and can change; the figures and domain weightings used throughout this document were verified against the exam guides current as of this course's design and should be re-checked by instructors before every cohort, exactly as stated in Lecture 87/93 and the certification map that follows.

**Appendix: NVIDIA AI Certification (Not Currently in This Course)**

NVIDIA offers its own certification track through its NVIDIA-Certified Associate (NCA) tier, delivered via the Certiverse testing platform. This is provided here as reference information only — it is not part of this course's curriculum or Month 12 certification plan, and nothing in Months 1-11 was designed to prepare for it specifically (though the AI/ML and GenAI foundations taught throughout the year do overlap substantially with its content).

| **Exam**                                        | **USD fee** | **Approx. INR (at ~₹96/USD)** | **Format / Validity**                                                                                                                              |
|-------------------------------------------------|-------------|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| **NCA-GENL — Generative AI and LLMs**           | \$125       | **≈ ₹12,000**                 | ~50-60 questions, 60 min, covers core ML/AI, software development, experimentation, data analysis/visualisation and trustworthy AI. Valid 2 years. |
| **NCA-AIIO — AI Infrastructure and Operations** | \$125       | **≈ ₹12,000**                 | 50 questions, 60 min, 70% pass mark, infrastructure/operations-focused (not covered by this course). Valid 2 years.                                |

**Market value**

**•** NCA-GENL is the more directly relevant of the two to this course's content (generative AI, LLMs, prompt-adjacent skills), and could be a reasonable next step for a graduate who wants a third AI credential beyond AI-901 and AIF-C01.

**•** NCA-AIIO is infrastructure/operations-focused and sits outside this course's scope entirely; it is listed here only for completeness, not as a recommended next step for this age group.

**•** NVIDIA's brand carries particular recognition in GPU-accelerated computing, data-centre and AI-infrastructure employers specifically — a narrower, more specialised signal than the broad cloud-platform recognition of the Microsoft and AWS certifications already built into this course.
