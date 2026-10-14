# Launch checklist: neuronetwrks.com

Last updated: 14 October 2026. Live site: https://neuronetwrks.com (Vercel project `neuronetwrks-preview`, built from `tools/preview-gen`).

When the owner asks "what's pending?", answer from this file.

## Done
- [x] Domain live on Vercel: apex `neuronetwrks.com`, `www` redirects to it, HTTPS certificate issued. Google email records (MX, SPF) kept.
- [x] SEO, AEO and GEO:
  - titles, descriptions and canonicals;
  - Open Graph and Twitter cards with a share image;
  - JSON-LD (organisation, website, breadcrumbs, FAQs, courses, projects);
  - sitemap, robots.txt allowing AI search bots, llms.txt;
  - favicons.
- [x] Google Analytics live (ID G-1D2KJQ9RCF) behind the cookie banner; loads only after "Allow analytics".
- [x] AI training bots explicitly allowed in robots.txt (owner decision, 14 Oct 2026): GPTBot, ClaudeBot, Google-Extended, Applebot-Extended, CCBot and others.
- [x] Search Console verified (Domain property). Sitemap submitted with the full URL.
- [x] SEO growth push (14 Oct 2026):
  - 10 answer-first guides at /guides, chosen from India keyword research (`docs/seo/keyword-map.md`);
  - "after 10th" titles on program pages;
  - guide links on the home and program pages;
  - organisation schema with knowsAbout and a course catalogue;
  - llms-full.txt for AI engines;
  - a smaller hero image for phones.
  The guides use an organisation byline ("NeuroNetworks AI Ed team"), chosen by the owner. CLAUDE.md asks for a named author; switch to a named person later for stronger trust signals.
- [x] Promotion kit in `docs/marketing/`: launch plan, social setup, first posts, listings, PR and partnerships, banner images.
- [x] IndexNow set up. The key file is served from the site, and `python3 tools/preview-gen/indexnow.py` notifies Bing after each deploy.

## Waiting on the owner

### 1. Google Analytics: finish settings (ID received and live)
1. Go to analytics.google.com. Open Admin, then Create, then Property, and name it "NeuroNetworks AI Ed". Choose time zone India and currency INR.
2. Choose Data streams, then Web. Enter the URL `https://neuronetwrks.com` and the stream name "Website".
3. Copy the **Measurement ID** (it starts with `G-`) and send it to Claude.
4. In the property, open Admin, then Data collection, and leave **Google signals off**. Open Data retention and set it to 2 months.

Claude then sets `GA_ID` in `tools/preview-gen/build.py`, rebuilds and deploys. From then on:
- the banner appears for visitors;
- Google loads only after a visitor clicks "Allow analytics";
- events are tracked: `program_view`, `talk_click`, `scroll_75` and `outbound_click`. `apply_submit` will follow once the form is wired.

### 2. Google Search Console (ownership verified 14 Oct 2026)
1. Go to search.google.com/search-console, choose Add property, then **Domain**, and enter `neuronetwrks.com`.
2. Copy the TXT value Google shows (it starts with `google-site-verification=`).
3. In Squarespace, open Domains, then neuronetwrks.com, then DNS, then **Custom records**, and choose Add record:
   - Type: **TXT**
   - Host: **@**
   - Data: the value from step 2.
   Save it. Keep the existing SPF TXT record.
4. Back in Search Console, click Verify. If it fails, wait an hour and try again.
5. Open Sitemaps and enter the **full URL** `https://neuronetwrks.com/sitemap.xml` (a Domain property rejects a bare `sitemap.xml` as "Invalid sitemap address"), then click Submit. "Couldn't fetch" for the first few hours is normal.
6. In Settings → Associations, link the GA4 property (G-1D2KJQ9RCF).
7. Optional: use URL inspection on `https://neuronetwrks.com/`, then click Request indexing.

### 3. Bing Webmaster Tools
1. Go to bing.com/webmasters and sign in. Choose **Import from Google Search Console**, so no DNS record is needed. Do this after step 2.
2. Check that the sitemap `https://neuronetwrks.com/sitemap.xml` is listed.
3. Bing also powers ChatGPT search, so this matters for AI answers.

### 4. Google Business Profile (needs a real address or service area and a phone number first)
1. Go to business.google.com, choose Add business, and enter the name **NeuroNetworks AI Ed**, exactly as on the website.
2. Category: "Educational institution", or "Computer training school" / "Training centre".
3. If students don't visit a public address, choose **"I deliver goods and services to my customers"** and set service areas (cities or states). Don't list a home address.
4. Add the phone, the website `https://neuronetwrks.com` and the email `Hussain@neuronetwrks.com`.
5. Verify by video or postcard, as Google offers.
6. After verification, add the logo (`tools/preview-gen/assets/logo-512.png`), real photos and opening hours. Don't add any prices.
7. Send Claude the profile link. Claude adds the address, phone and profile link to the site's structured data.

## Still to do before promoting the site
- [ ] Claim the social profiles (`docs/marketing/social-setup.md`) and send Claude the links, so they can be added to the site's `SAME_AS` list in build.py.
- [ ] In Search Console, request indexing for /guides and the 10 guide pages.
- [ ] Create the free directory listings (`docs/marketing/listings.md`).
- [ ] Post on the 30-day plan (`docs/marketing/launch-campaign.md`). Refresh the guides in February–March, before the April–May "after 10th" search peak.
- [ ] Confirm whether the programs award a diploma or certificate. "Diploma after 10th" is the most-searched phrase.
- [ ] Replace the "[to be confirmed]" placeholders: postal address, phone, faculty and team, intake dates, social profiles, founding story, admissions steps.
- [ ] Wire the enquiry form to the Google Sheet and email (it does not send yet). This is the most important item.
- [ ] Have a lawyer review the privacy notice and consent flow (DPDP). The footer's Privacy Policy and Terms links point to /contact for now.
- [ ] Optional: replace the Unsplash classroom photo with real photos of your students.
- [ ] Optional: move hosting to Cloudflare, as in the original plan (the site is currently on Vercel).
- [ ] After the GSC and Bing steps: Claude checks the TXT record and sitemap status.
