# Home page "AI Lab" section with the 30-second prompt challenge. exec'd from build.py (shares its namespace).
# Content is static and version-controlled; site.js ([data-aic]) handles selection, feedback, retry and GA4 events.

AIC = {"id": "prompt-engineering-001", "topic": "Prompt Engineering",
       "question": "Imagine you want AI to explain climate change to a 12-year-old. Which prompt is most likely to get you a useful answer?",
       "options": [("a", "Tell me about climate change.", "Incorrect: broad and underspecified."),
                   ("b", "Explain climate change simply.", "Partly specific, but audience and output format are unclear."),
                   ("c", "Explain climate change to a 12-year-old in simple language. Use three bullet points and one everyday example.",
                    "Correct: states audience, task, language level and output format.")],
       "correct": "c"}

AIC_SVG = {"flask": '<path d="M9 3h6M10 3v6L4.5 18.5A1.6 1.6 0 0 0 5.9 21h12.2a1.6 1.6 0 0 0 1.4-2.5L14 9V3"/><path d="M7.5 15h9"/>',
           "msg": '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9.5h8M8 12.5h5"/>',
           "wrench": '<path d="M14.5 5.5a4 4 0 0 0 4.9 4.9L21 12l-8.5 8.5a2.1 2.1 0 0 1-3-3L18 9"/><path d="M3 21l4-4"/>',
           "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>'}


def aic_icon(k):
    return (f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{AIC_SVG[k]}</svg>')


def ai_lab_section():
    cards = [("flask", "Learn by doing", "Turn AI concepts into hands-on practice."),
             ("msg", "Get guided feedback", "Understand mistakes and learn how to improve."),
             ("wrench", "Build practical skills", "Apply what you learn to useful, real-world-style problems."),
             ("chart", "See your progress", "Review completed work, feedback, and skill development.")]
    cl = "".join(f'<li><span class="aic-ic">{aic_icon(k)}</span><h3>{t}</h3><p>{d}</p></li>' for k, t, d in cards)
    loop = "".join(f"<li>{x}</li>" for x in ["Learn", "Try", "Get feedback", "Improve"])
    opts = "".join(
        f'<label class="aic-opt" data-opt="{oid}"><input type="radio" name="aic" value="{oid}">'
        f'<span class="aic-letter" aria-hidden="true">{oid.upper()}</span>'
        f'<span class="aic-txt"><span class="sr">Option {oid.upper()}: </span>{E(t)}<span class="aic-why" hidden>{E(w)}</span></span></label>'
        for oid, t, w in AIC["options"])
    return f"""<section class="sec aic" id="ai-lab" data-aic="{AIC["id"]}" data-aic-correct="{AIC["correct"]}"><div class="wrap">
<div class="aic-grid"><div class="aic-copy">
<p class="eyebrow">The Neuronetworks difference</p><h2 class="aic-h2">Most courses teach AI. We help you build with it.</h2>
<p class="aic-lead">Don't stop at watching lessons. Experiment with AI, solve practical challenges, learn from mistakes, and put your knowledge to work.</p>
<p class="aic-line">Learn the concept. Try the challenge. Understand the result. Improve your approach.</p>
<ul class="aic-cards">{cl}</ul>
<div class="aic-lab"><p class="eyebrow">Inside the Neuronetworks AI Lab</p><h3>Your learning shouldn't end when the video does.</h3>
<p>Step into a practical learning environment where you can work through guided exercises, tackle independent challenges, test your ideas, and learn from feedback.</p>
<ol class="aic-loop" aria-label="The learning loop">{loop}</ol></div></div>
<div class="aic-card"><p class="aic-badge">30-second AI challenge</p><h3 class="aic-title">Can you write a better AI prompt?</h3>
<form class="aic-form" novalidate><fieldset><legend>{E(AIC["question"])}</legend><div class="aic-opts">{opts}</div></fieldset>
<button type="submit" class="aic-submit" disabled>Check my answer</button></form>
<div class="aic-fb" role="status" aria-live="polite"></div>
<div class="aic-tpl" hidden>
<div data-r="correct"><p class="aic-fb-h"><span aria-hidden="true">&#10003;</span> Exactly right!</p><p>You specified the audience, the task, the language level, and the desired format. That gives the AI clearer instructions.</p></div>
<div data-r="incorrect"><p class="aic-fb-h">Good try: here's the idea.</p><p>The strongest answer is C. A good prompt gives the AI context, a clear task, and guidance on the output you want.</p></div>
<div data-r="common"><p class="aic-take"><b>What you just learned:</b> prompt engineering.</p><p class="aic-note">Clearer instructions can improve relevance and structure, although they cannot guarantee factual accuracy.</p></div></div>
<button type="button" class="aic-retry" hidden>Try again</button>
<p class="aic-nojs">The strongest answer is C. It tells the AI the audience, the task, the language level and the output format. Clearer instructions can improve relevance and structure, although they cannot guarantee factual accuracy.</p>
</div></div>
<div class="aic-cta"><div><h3>That was just the beginning.</h3><p>Explore a learning experience built around practice, problem-solving, feedback, and projects.</p></div>
<div class="aic-cta-b"><a class="btn btn-primary" href="/programs" data-aic-cta="explore_program">Explore the AI program</a><a class="btn btn-secondary" href="/contact" data-aic-cta="ask_course">Ask us about the course</a></div></div>
</div></section>"""
