# 8. Cost breakdown in INR

This part lists what each tool and service costs, in Indian rupees. The short answer: **the tools needed today cost nothing extra.** The real running costs are hosting (Vercel Pro), the database (Supabase) and the grader server (AWS EC2). Spline and Rive are optional and should be bought only when a specific need appears.

## How the numbers were worked out

- Prices were read from each company's official pricing page on **15 October 2026** (links in each row and in the sources log in the README).
- Exchange rate: **1 USD = ₹95.16** (European Central Bank reference data via frankfurter.dev, 14 October 2026; a second source showed ₹95.25 on 15 October). Rupee figures are rounded to the nearest rupee.
- Your bank will use its own rate and may add a foreign-transaction mark-up (often a few per cent; **unverified**, check your card terms).
- **GST.** Foreign online services sold to an unregistered Indian buyer generally carry 18% IGST charged by the provider; a GST-registered business usually pays it under reverse charge and may claim input credit. This comes from secondary sources ([Treelife](https://treelife.in/legal/oidar-registration-in-india/), [xflowpay](https://www.xflowpay.com/blog/oidar-services)), not from the government notification itself. **Confirm with your chartered accountant.** The "with 18% GST" column assumes GST applies and is not recovered.
- Vercel states its prices "exclude value-added tax (VAT), goods and services tax (GST), and other applicable taxes" ([Pro plan docs](https://vercel.com/docs/plans/pro-plan)).

## 1. Free tools (₹0)

| Tool | Licence or plan | What you get free | Source |
|---|---|---|---|
| Blender 5.1 | GPL | Everything, including commercial use; you own what you make | [blender.org licence](https://www.blender.org/about/license/) |
| Three.js | MIT | Full library | [GitHub](https://github.com/mrdoob/three.js) |
| React Three Fiber + drei | MIT (**unverified** for drei; check its GitHub) | Full library | [R3F docs](https://r3f.docs.pmnd.rs/getting-started/installation) |
| Motion for React | MIT | Full library (Motion+ is a separate paid tier we do not need) | [GitHub](https://github.com/motiondivision/motion) |
| Rive runtime (rive-react) | MIT | Playing `.riv` files in the lab | [GitHub](https://github.com/rive-app/rive-react) |
| glTF Transform, gltfjsx | Open source (**unverified** exact licences) | Compression and conversion | [gltf-transform.dev](https://gltf-transform.dev/cli), [gltfjsx](https://github.com/pmndrs/gltfjsx) |
| Playwright, axe-core, Lighthouse | Open source | Testing | already in use |
| Spline Free | Free plan | Learning; web exports carry a watermark; limited files; no AI | [spline.design/pricing](https://spline.design/pricing) |
| Rive Free | Free plan | Learning; `.riv` exports play a Rive splash screen; 3 collaborative files | [rive.app/pricing](https://rive.app/pricing) |

## 2. Paid design-tool subscriptions (optional)

| Plan | USD | ₹ (before GST) | ₹ with 18% GST | What the money buys | Source |
|---|---|---|---|---|---|
| Spline Hobby, yearly | $12 per seat per month ($144 per year) | ₹1,142 per month (₹13,703 per year) | ₹1,347 per month (₹16,170 per year) | No watermark on web exports (2D embeds still watermarked); unlimited files; AI features with 2,000 credits per month | [Spline pricing](https://spline.design/pricing) |
| Spline Hobby, monthly | $15 per seat per month | ₹1,427 | ₹1,684 | Same | same |
| Spline Pro, yearly | $25 per seat per month ($300 per year) | ₹2,379 per month (₹28,548 per year) | ₹2,807 per month (₹33,687 per year) | Adds code-export download, video export, 3,000 AI credits, "Color & Texture" glTF export | same |
| Spline Pro, monthly | $30 per seat per month | ₹2,855 | ₹3,369 | Same | same |
| Spline Max, yearly | $60 per seat per month | ₹5,710 | ₹6,737 | 10,000 AI credits, priority support | same |
| Rive Cadet | $9 per seat per month | ₹856 | ₹1,011 | Export `.riv` without the splash screen; unlimited files; up to 3 seats | [Rive pricing](https://rive.app/pricing) |
| Rive Voyager | $32 per seat per month | ₹3,045 | ₹3,593 | Libraries, embed URL hosting, bring-your-own agent key | same |

Rive's page has a yearly/monthly switch but showed one price per plan when checked. Whether $9 and $32 are the yearly-billed rates is **unverified**; confirm at checkout.

Spline's self-hosted export (bundling the runtime yourself) is an Enterprise feature with custom pricing ([self-hosted export](https://docs.spline.design/exporting-your-scene/web/exporting-as-self-hosted-project.md)).

## 3. Hosting and running costs (needed regardless of design tools)

| Service | Plan | USD per month | ₹ per month (before GST) | ₹ with 18% GST | Notes | Source |
|---|---|---|---|---|---|---|
| Vercel (website + lab) | Hobby | $0 | ₹0 | ₹0 | "Restricted to non-commercial personal use only." Advertising a product or service counts as commercial. **Not suitable for NeuroNetworks AI Ed.** | [Fair use](https://vercel.com/docs/limits/fair-use-guidelines) |
| Vercel (website + lab) | Pro | $20 platform fee (1 deploying seat, $20 usage credit) | ₹1,903 | ₹2,246 | Extra deploying seats $20 each; viewer seats free; usage beyond the credit billed on demand; default spend alert at $200 | [Pro plan](https://vercel.com/docs/plans/pro-plan) |
| Supabase | Free | $0 | ₹0 | ₹0 | 500 MB database, 50,000 MAU, 5 GB egress, **paused after 1 week of inactivity**, 2 active projects | [Supabase pricing](https://supabase.com/pricing) |
| Supabase | Pro | from $25 | ₹2,379 | ₹2,807 | 8 GB disk, 100,000 MAU, 250 GB egress, $10 compute credit, never paused | same |
| AWS EC2 grader (Mumbai) | t4g.small on demand, 730 h | $8.18 | ₹778 | ₹918 | $0.0112 per hour. ARM (Graviton): grader Docker image must be built for arm64 | [AWS price list, ap-south-1](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonEC2/current/ap-south-1/index.csv) |
| AWS EC2 grader (Mumbai) | t3.small on demand, 730 h | $16.35 | ₹1,556 | ₹1,836 | $0.0224 per hour, x86 | same |
| AWS EBS storage | gp3, 20 GB | $1.82 | ₹174 | ₹205 | $0.0912 per GB-month | same |
| AWS public IPv4 | 1 address, 730 h | $3.65 | ₹347 | ₹410 | $0.005 per hour, in use or idle | [VPC pricing](https://aws.amazon.com/vpc/pricing/) |

**Grader server, typical total:** t4g.small + 20 GB gp3 + one public IPv4 ≈ $13.65 ≈ **₹1,299 per month** before GST (₹1,533 with 18%). With t3.small instead ≈ $21.82 ≈ ₹2,077. Data transfer out of AWS is extra and depends on use (**not calculated**). We do not know which instance type the grader uses today; check the AWS console.

**Free tier.** New AWS accounts can receive up to $200 in credits; on the free plan the account closes after 6 months or when credits run out ([aws.amazon.com/free](https://aws.amazon.com/free/)). The page does not say which EC2 instance hours are free, so do not budget on it (**unverified**).

**Supabase Free pausing** matters: if the lab has no activity for a week, the database pauses. For a product students rely on, Pro is the safer choice once you have real students. Phone MFA would be an extra $75 per month on Pro; the lab uses MFA (aal2), and basic MFA is included on both plans ([pricing](https://supabase.com/pricing)). Check which MFA factor the lab uses before assuming no extra cost.

## 4. One-time asset production

| Item | Cost | Notes |
|---|---|---|
| 11 program models + NN-Bot, script-built in Blender by Claude Code | ₹0 extra | Uses Claude Max time you already pay for, plus your review time |
| A freelance 3D artist (if you want hand-sculpted work) | Not estimated | Get quotes; insist on `.blend` source files being delivered, not only GLB |
| Rive grade badge | ₹0 to design on Free; ₹856 for one month of Cadet to export without splash | Buy one month when ready to ship; cancel after if no more changes (check cancellation terms) |
| Spline scene | ₹0 on Free (watermarked); ₹1,142 to ₹2,855 per month to remove watermark or download code | Only if you decide you want to design scenes yourself |

## 5. Potential API and runtime charges

| Item | When it costs money | Current exposure |
|---|---|---|
| Spline AI credits | Paid Spline plans include monthly credits; heavy use may need more | ₹0 if Spline is not used |
| Rive Agent credits | Voyager adds $20 per seat for monthly agent credits | ₹0 unless Voyager |
| Spline-hosted scenes | Loading scenes from Spline's servers; no runtime fee is listed on the pricing page | **Unverified** whether high traffic has limits |
| Vercel usage beyond $20 credit | Bandwidth, function invocations (lab FastAPI), image optimisation | Set a spend limit in Vercel |
| Supabase overage on Pro | Over 8 GB disk, 100,000 MAU, 250 GB egress | Low at launch |
| CDN downloads of Pyodide and Monaco | Free public CDNs today | No cost; reliability risk (see roadmap) |

## 6. Recommended smallest practical stack

| Need | Tool | Monthly cost |
|---|---|---|
| Website 3D (cards, NN-Bot) | Blender + Three.js + gltf-transform | ₹0 |
| Lab interface motion | Motion for React | ₹0 |
| Lab feedback animation (later) | Rive Free to design; one month of Cadet to ship | ₹0, then about ₹856 once |
| Lab educational 3D (future Guided Simulation) | React Three Fiber | ₹0 |
| Code, tests, screenshots | Claude Code (Claude Max) | Already paid |
| Hosting | Vercel Pro | ₹1,903 (+GST) |
| Database and auth | Supabase Free now; Pro when students depend on it | ₹0 → ₹2,379 (+GST) |
| Grader | AWS EC2 t4g.small or similar | about ₹1,299 (+GST) |

**New monthly spend for the visual work in this manual: ₹0.** Spline and Rive are bought only when a concrete need appears.

**Running costs that exist anyway:** about ₹3,200 per month before GST with Supabase Free (Vercel Pro ₹1,903 + grader ₹1,299), or about ₹5,580 with Supabase Pro.

## 7. Total cost of ownership note

Claude Max is already owned and excluded above. For a full picture: Max is listed "from $100" per month (₹9,516 before GST) ([claude.com/pricing](https://claude.com/pricing)), and the page states "Claude Code is included in all paid plans." With Max, Vercel Pro, Supabase Pro and the grader, the whole operation is roughly ₹15,100 per month before GST at today's rate, or about ₹17,800 with 18% GST if none of it is recovered. Your own time reviewing work is the largest hidden cost.
