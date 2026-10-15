# 30-day organic launch plan

NeuroNetworks AI Ed · neuronetwrks.com · Learn · Develop · Create

This plan uses free, organic channels only. No paid ads unless you decide to add them later (see the end of this file). It assumes about 1 hour a day of your time.

**Day 1 = [start date].** Fill in the date when you begin, then follow the weekly table.

---

## 1. What we are trying to achieve

The site is new. It has no social profiles, no backlinks and no history with Google yet. The first 30 days are about **getting found and getting the first enquiries**, not about big numbers.

| Goal | How we measure it | Where to look | 30-day target |
|---|---|---|---|
| Google knows every page | Indexed pages | Search Console > Indexing > Pages | Every URL in the sitemap shows "Indexed" (the sitemap currently lists 30 URLs) |
| People start seeing us in Google | Impressions | Search Console > Performance | Impressions rise week on week; first impressions on the /guides/ pages |
| People click through | Clicks | Search Console > Performance | First clicks from Google; note which pages get them |
| People visit from social and outreach | Sessions by source | GA4 > Reports > Acquisition > Traffic acquisition | Visits from linkedin.com, instagram.com, youtube.com, quora.com, reddit.com and WhatsApp |
| Parents and students get in touch | Enquiries via /contact | Your inbox (Hussain@neuronetwrks.com) plus GA4 views of /contact | First enquiries; count every one in the tracking sheet below |
| The brand exists outside the website | Profiles and listings live | `social-setup.md` and `listings.md` | 5 social profiles and at least 6 free listings live |

Set exact numbers for months 2 and 3 after you see the first 4 weeks of data. Do not compare yourself with large, older brands yet.

### Where the numbers come from

- **GA4** property **G-1D2KJQ9RCF**. Open analytics.google.com, pick the NeuroNetworks property.
- **Google Search Console** (GSC). Open search.google.com/search-console, pick neuronetwrks.com.

Two things to know:

1. GA4 only counts visitors who accept the cookie banner, so GA4 numbers will be **lower than real traffic**. Search Console counts everyone who saw or clicked you in Google. Trust GSC for search, GA4 for "where did visitors come from".
2. The contact form opens the visitor's email app, so each enquiry arrives as an email. Count enquiries from your inbox. If you want GA4 to count form sends too, ask Claude: "add a GA4 event when the contact form is sent and mark it as a key event".

### Simple tracking sheet

Make a Google Sheet with one row per week and these columns:

`Week | GSC impressions | GSC clicks | Indexed pages | GA4 users | Top traffic source | Enquiries (inbox) | Posts published | Listings added | Notes`

Fill it every Monday during the 15-minute SEO routine (section 5).

### Tag your links so GA4 knows where visitors came from

When you share a link outside Google, add a short tag to the end. Example for LinkedIn:

`https://neuronetwrks.com/guides/ai-courses-after-10th?utm_source=linkedin&utm_medium=social&utm_campaign=launch`

Change `utm_source` to `instagram`, `youtube`, `whatsapp`, `quora`, `reddit` or `school_email` as needed. Keep `utm_campaign=launch` for these 30 days. Do not tag links on directory listings or in your social profile "website" field; use the plain `https://neuronetwrks.com` there.

---

## 2. Channels and what each one is for

| Channel | Who it reaches | What to post or do | Link to |
|---|---|---|---|
| **LinkedIn** (company page + your personal profile) | Parents who work, school staff, educators, investors | 3 posts a week from `first-posts.md`. Share each company post from your personal profile too | Program pages and parent-focused guides |
| **Instagram** | Students aged 15 to 17, older siblings | 3 posts a week (carousels work best), plus Stories reshares | "Link in bio" to a guide; change the bio link to match the week's theme |
| **YouTube Shorts** | Students searching "what to do after 10th" | 2 Shorts a week, 30 to 50 seconds, screen-recording or slide style. No faces needed | Pinned comment and description link to one guide |
| **WhatsApp parent groups** | Parents, mostly through people you know | Share one guide at a time with a two-line personal note. Never mass-forward or add people to groups without asking | Parent-focused guides |
| **School and coaching-centre outreach** | Principals, counsellors, coaching-centre owners | Email the template in `pr-and-partnerships.md`. Offer a free "AI for students" session | /guides/career-options-after-10th and /admissions |
| **Quora and Reddit answers** | Students and parents asking "which course after 10th" | Answer real questions fully in the answer itself, then add one link to the matching guide. Say you run NeuroNetworks AI Ed | The guide that matches the question |
| **Directories and listings** | Google, Bing, AI search tools, education portals | Follow `listings.md` | Home page |

### Quora and Reddit rules (to avoid being banned)

- Answer the question properly first. The link is a footnote, not the answer.
- Always say "I run NeuroNetworks AI Ed" in the answer. Hiding it is against both sites' rules.
- One link per answer. Never post the same text twice.
- On Reddit, read each subreddit's rules first. Many ban self-promotion. Useful places to read and answer: r/JEENEETards, r/Indian_Academia, r/developersIndia (career questions only), r/IndianTeenagers. If a subreddit bans links, answer without one.
- Good Quora searches: "courses after 10th", "AI course after 10th", "coding after class 10", "data science after 10th", "cyber security after 10th", "career options after 10th".

### Which guide answers which question

| If the question is about... | Link to |
|---|---|
| AI course after 10th | https://neuronetwrks.com/guides/ai-courses-after-10th |
| Which course after 10th (general) | https://neuronetwrks.com/guides/courses-after-10th |
| Coding or computer course after 10th | https://neuronetwrks.com/guides/computer-coding-courses-after-10th |
| Cyber security after 10th | https://neuronetwrks.com/guides/cyber-security-course-after-10th |
| Data science after 10th | https://neuronetwrks.com/guides/data-science-after-10th |
| UI/UX design after 10th | https://neuronetwrks.com/guides/ui-ux-designer-after-10th |
| AI vs software vs data science (parents) | https://neuronetwrks.com/guides/ai-vs-software-vs-data-science |
| AI project ideas for students | https://neuronetwrks.com/guides/ai-projects-for-students |
| Career options after 10th | https://neuronetwrks.com/guides/career-options-after-10th |
| How to become an AI engineer | https://neuronetwrks.com/guides/become-ai-engineer-after-10th |

---

## 3. Week-by-week actions

Each week has a theme so your posts, Shorts and answers point to the same few pages.

### Week 1: Set up and get indexed

| Day | Action | Time | Done |
|---|---|---|---|
| 1 | Confirm Search Console and Bing Webmaster Tools are verified and the sitemap is submitted (see `docs/launch-checklist.md`) | 20 min | [ ] |
| 1 | In GSC, use **URL Inspection** on the home page and the 6 program pages, then click **Request indexing** for each one not yet indexed | 20 min | [ ] |
| 2 | Claim all 5 social profiles (follow `social-setup.md`) | 60 min | [ ] |
| 3 | Fill in bios, images and website links on all profiles | 45 min | [ ] |
| 3 | Send the profile links to Claude for the website's sameAs schema | 2 min | [ ] |
| 4 | Create the free listings that need no address: LinkedIn, Crunchbase, YouTube, GitHub (from `listings.md`) | 60 min | [ ] |
| 5 | Publish LinkedIn post 1 and Instagram post 2 from `first-posts.md` | 20 min | [ ] |
| 6 | Request indexing for the 10 /guides/ pages in GSC (a few per day if GSC limits you) | 15 min | [ ] |
| 7 | Set up the tracking sheet and record the first baseline row | 15 min | [ ] |

### Week 2: Theme "What can you study after Class 10?"

Main pages: /guides/courses-after-10th, /guides/career-options-after-10th, /programs/ai-foundation

| Day | Action | Time | Done |
|---|---|---|---|
| 8 | 15-minute GSC routine (section 5) | 15 min | [ ] |
| 8 | Publish LinkedIn post 3 | 10 min | [ ] |
| 9 | Publish Instagram post 4; record and upload YouTube Short 1 ("6 tech paths after Class 10 in 40 seconds") | 45 min | [ ] |
| 10 | Answer 3 Quora questions using the guide table above | 45 min | [ ] |
| 11 | Publish LinkedIn post 5; share it from your personal profile | 10 min | [ ] |
| 12 | Share /guides/courses-after-10th in 2 or 3 WhatsApp groups where you know people, with a personal note | 15 min | [ ] |
| 13 | Publish Instagram post 6; upload YouTube Short 2 | 40 min | [ ] |
| 14 | List 20 schools and coaching centres in your area to contact in week 3 (name, principal or counsellor, email) | 45 min | [ ] |

### Week 3: Theme "What students actually build"

Main pages: /projects, /guides/ai-projects-for-students, /guides/computer-coding-courses-after-10th, /curriculum

| Day | Action | Time | Done |
|---|---|---|---|
| 15 | 15-minute GSC routine | 15 min | [ ] |
| 15 | Publish LinkedIn post 7 | 10 min | [ ] |
| 16 | Send the outreach email (`pr-and-partnerships.md`) to the first 10 schools and centres | 45 min | [ ] |
| 17 | Publish Instagram post 8; upload YouTube Short 3 ("What a Class 10 pass student builds in month 1") | 40 min | [ ] |
| 18 | Answer 2 Quora questions and 1 Reddit question | 40 min | [ ] |
| 19 | Publish LinkedIn post 9; send outreach email to the next 10 | 45 min | [ ] |
| 20 | Create listings on Shiksha, CollegeDunia and Careers360 (they may take days to approve) | 60 min | [ ] |
| 21 | Publish Instagram post 10; upload YouTube Short 4 | 40 min | [ ] |

### Week 4: Theme "Choosing a path, for parents"

Main pages: /guides/ai-vs-software-vs-data-science, /admissions, /faqs, /contact

| Day | Action | Time | Done |
|---|---|---|---|
| 22 | 15-minute GSC routine | 15 min | [ ] |
| 22 | Publish LinkedIn post 11 | 10 min | [ ] |
| 23 | Follow up (one polite reminder) with schools that did not reply | 30 min | [ ] |
| 24 | Publish Instagram post 12; upload YouTube Short 5 ("AI vs software vs data science, for parents") | 40 min | [ ] |
| 25 | Pitch one guest article to an education blog (ideas in `pr-and-partnerships.md`) | 45 min | [ ] |
| 26 | Answer 3 Quora or Reddit questions | 45 min | [ ] |
| 27 | Share /guides/ai-vs-software-vs-data-science in WhatsApp groups; upload YouTube Short 6 | 40 min | [ ] |
| 28 | If you have an address or service area and a phone number by now: create Google Business Profile, then Bing Places, Justdial and Sulekha (`listings.md`) | 60 min | [ ] |

### Days 29 and 30: Review

| Day | Action | Done |
|---|---|---|
| 29 | Fill the tracking sheet. Note which pages got impressions, which posts got clicks, and where enquiries came from | [ ] |
| 30 | Decide what to keep for month 2: the 2 channels that sent the most visits or enquiries get more time; drop or reduce the weakest one. Ask Claude to write the next 12 posts based on what worked | [ ] |

---

## 4. Seasonality: plan the big push for February to March 2027

Searches like "courses after 10th" and "what to do after 10th" are highest in **April and May**, when Class 10 board results come out and families decide on next steps. Google needs time to trust a new site, so the work must be done **before** that peak.

| When | What to do |
|---|---|
| **Now to January 2027** | Run this 30-day plan, then keep a steady routine: 2 to 3 posts a week, 1 to 2 Shorts a week, weekly GSC check. Build listings and backlinks (`pr-and-partnerships.md`). |
| **January 2027** | Ask Claude to refresh every /guides/ page for the 2027 admission season (update dates, add any newly confirmed facts such as intake dates and delivery mode). Confirm intake dates for the [2027 intake]. |
| **February to March 2027: main push** | Double posting (daily on Instagram, 4 a week on LinkedIn, 3 Shorts a week). Run the free "AI for students" webinar. Send the school outreach email to a larger list before schools close for exams. Publish 2 or 3 new guides on questions you saw in GSC. |
| **April to May 2027: peak** | Answer Quora and Reddit questions daily during results week. Pin the most useful guide on every profile. Reply to every enquiry within 24 hours. |
| **June 2027** | Review: which guides ranked, which channels sent enquiries. Plan the next year. |

---

## 5. Weekly SEO routine: 15 minutes in Search Console every Monday

1. **Open Search Console** and choose neuronetwrks.com. (1 min)
2. **Performance > Search results.** Set the date to "Last 7 days" and click "Compare" with the previous 7 days. Write total impressions and clicks in the tracking sheet. (3 min)
3. **Click the "Queries" tab.** Look for searches where you get impressions but few clicks. Copy the top 5 into the "Notes" column. These are ideas for posts, Shorts and new guides. Send them to Claude to improve titles or add an FAQ. (4 min)
4. **Click the "Pages" tab.** Note which page gets the most impressions. Use it in that week's posts. (2 min)
5. **Indexing > Pages.** Check the number of indexed pages. If any page shows "Discovered, currently not indexed" or "Crawled, currently not indexed", open **URL Inspection**, paste the address and click **Request indexing**. (3 min)
6. **Look at the bell icon (messages).** If Google reports any error, forward it to Claude. (1 min)
7. **Open GA4 > Reports > Acquisition > Traffic acquisition** for the last 7 days. Write the top source in the sheet. (1 min)

---

## 6. Rules for every post, answer and email

- Write "NeuroNetworks AI Ed" in full. The website is spelled neuronetwrks.com.
- The tagline is always exactly **Learn · Develop · Create**. Never reword it.
- Use real facts only: hours, months, modules, projects, tools, the certifications prepared for. All are in `site-preview/llms-full.txt`.
- Never claim jobs, placements, exam passes, or student numbers. Salary: only the indicative ranges published on the program pages, always with "indicative, not guaranteed". Never post testimonials or reviews you have not received in writing with permission.
- No prices. Say "Fees are shared on enquiry" if asked.
- Avoid hype words: "unlock your potential", "revolutionise", "cutting-edge", "seamless", "journey", "world-class". No emoji used as icons.
- For students under 18, talk to the parent or guardian.

---

## 7. Paid ads (only if you choose them)

This plan has no paid ads. If you later want them, the cheapest test is a small Google Search campaign on "AI course after 10th" type searches during April to May 2027, sent to the matching guide. Note: the site's rules forbid ad pixels and remarketing, and ads must not target under-18s, so any ads would target parents only. Ask Claude to plan this when you are ready.
