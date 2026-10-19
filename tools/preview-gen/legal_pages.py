# Privacy policy and terms of use. exec'd from build.py (shares its namespace).
# Written from what the site really does (checked against site.js on 18 Oct 2026). Interim wording chosen 19 Oct 2026; the owner plans to review it in 5-6 months.

LEGAL_DATE, LEGAL_DATE_TXT = "2026-10-19", "19 October 2026"

def legal_body(sections):
    secs = "".join(f'<section class="gd-sec" id="l{i+1}"><h2>{E(h)}</h2>{b}</section>' for i, (h, b) in enumerate(sections))
    toc = "".join(f'<li><a href="#l{i+1}">{E(h)}</a></li>' for i, (h, _) in enumerate(sections))
    return f'<div class="wrap gd-wrap"><aside class="gd-toc" aria-label="On this page"><p>On this page</p><ol>{toc}</ol></aside><article class="gd-art">{secs}</article></div>'

def privacy_page():
    S = [
     ("Who we are", "<p>Neuronetworks AI Ed teaches AI and technology programs online to students in India. This page explains what personal information this website collects and how we use it. "
      'For any question, write to <a href="mailto:Hussain@neuronetwrks.com">Hussain@neuronetwrks.com</a>.</p>'),
     ("What we collect when you enquire", "<p>The enquiry form asks for a name, an email address and the program you are interested in, plus anything you choose to write in your message. "
      "When you press send, the form opens your own email app with these details filled in. Nothing is sent until you send that email yourself.</p>"
      "<p>Your enquiry arrives in our email inbox, and we note it in a private enquiry tracker that only our team can open. We use it only to reply to you and to follow up about the program you asked about.</p><p>If you join, we also ask for the student's latest marksheet, a photo ID for the student and for the parent or guardian, and a signed consent form.</p>"),
     ("Students under 18", "<p>Students under 18 enquire and apply through a parent or guardian, who gives consent. We ask only for what we need to reply. "
      "We do not run advertising aimed at children and do not use tracking for advertising.</p>"),
     ("Cookies and Google Analytics", "<p>We use Google Analytics 4 to see which pages help visitors. It loads only after you choose <strong>Allow analytics</strong> in the cookie banner. "
      "If you do not allow it, Google Analytics does not load. Your choice is saved in your browser so we do not ask again, and you can change it at any time with <strong>Cookie settings</strong> in the footer.</p>"
      "<p>We do not use advertising cookies, remarketing or ad pixels, and we do not sell personal information.</p>"),
     ("Who can see your information", "<p>Only our team. We use Google services to store enquiries and, if you allow it, to measure page visits. We do not share enquiry details with anyone else unless the law requires it.</p>"),
     ("How long we keep it, and deletion", "<ul><li><strong>Enquiries:</strong> if you do not join, we delete your details 12 months after our last contact.</li>"
      "<li><strong>Student records:</strong> kept for the length of the program plus two years, so certificates can be verified, then deleted.</li>"
      "<li><strong>Your requests:</strong> you can ask us at any time to see, correct or delete what we hold about you, and we act on it within 30 days. A parent or guardian can ask on behalf of a student under 18.</li></ul>"),
     ("Grievance contact", '<p>If you have a concern about how we handle personal data, write to our grievance contact, Hussain, at <a href="mailto:Hussain@neuronetwrks.com">Hussain@neuronetwrks.com</a>. '
      "We acknowledge every message within 7 working days and aim to resolve it within 30 days. This follows the Digital Personal Data Protection Act, 2023.</p>"),
     ("Changes to this policy", f"<p>If we change how we handle personal information, we will update this page and its date. Last updated {LEGAL_DATE_TXT}.</p>"),
    ]
    hero = page_hero("Privacy", "Privacy policy.", "Plain and short.", f"What this website collects, why, and how to ask us to delete it. Last updated {LEGAL_DATE_TXT}.")
    body = hero + legal_body(S) + cta_panel("Questions about your data?", "Write to Hussain@neuronetwrks.com. A person replies.")
    return layout("/privacy", "Privacy policy: how we handle your enquiry data", body, "none",
                  desc="How Neuronetworks AI Ed handles enquiry details, cookies and Google Analytics, students under 18, and how to ask for your data to be deleted.")

def terms_page():
    S = [
     ("About these terms", "<p>These terms cover your use of the neuronetwrks.com website. By using the site you agree to them. "
      'Questions go to <a href="mailto:Hussain@neuronetwrks.com">Hussain@neuronetwrks.com</a>.</p>'),
     ("Information on this site", "<p>We work to keep program details, hours, modules and projects accurate and current. They come from our own curriculum and can change. "
      "Fees, intake dates and batch timings are shared on enquiry and confirmed in writing when you apply.</p>"),
     ("No guarantee of jobs, salaries or exam passes", "<p>Our programs teach skills and help students build a portfolio. No program guarantees a job, internship, salary or exam pass. "
      "Salary figures on this site are indicative market ranges, not promises. Pay depends on the employer, city, role and skills.</p>"),
     ("Certificates", "<p>Students who complete a program receive a Neuronetworks AI Ed certificate. External certifications, such as those from Microsoft, AWS, Google, CompTIA or ISC2, "
      "are awarded by those organisations after their own exams. Our programs prepare students for them, and passing is not guaranteed.</p>"),
     ("Links to other websites", "<p>Our guides link to official pages run by other organisations. We do not control those sites and are not responsible for their content.</p>"),
     ("Using our content", "<p>The text, images and designs on this site belong to Neuronetworks AI Ed. You may share links to our pages. Please do not copy our content for commercial use without asking us.</p>"),
     ("Students under 18", "<p>Students under 18 enquire and apply through a parent or guardian.</p>"),
     ("Changes to these terms", f"<p>We may update these terms. The date below shows the latest version. Last updated {LEGAL_DATE_TXT}.</p>"),
    ]
    hero = page_hero("Terms", "Terms of use.", "In plain words.", f"The rules for using this website, what our information covers and what we do not promise. Last updated {LEGAL_DATE_TXT}.")
    body = hero + legal_body(S) + cta_panel("Questions about these terms?", "Write to Hussain@neuronetwrks.com. A person replies.")
    return layout("/terms", "Terms of use for the Neuronetworks AI Ed website", body, "none",
                  desc="The terms for using neuronetwrks.com: how program information is kept current, no job or salary guarantees, certificates, links and content use.")

CRUMB["privacy"] = "Privacy policy"; CRUMB["terms"] = "Terms of use"
