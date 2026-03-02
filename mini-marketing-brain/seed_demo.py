"""Seed Mini Marketing Brain with rich yorCMO demo knowledge entries.

Usage:
    python seed_demo.py

Creates 15 knowledge entries covering marketing audit, opportunities,
ideal client profile, competitive landscape, and more — all tagged
with org_slug "yorcmo" and keyword-optimized for the query engine.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from services.storage import save_knowledge_entry

ENTRIES = [
    # 1 — Marketing Audit
    {
        "doc_id": "demo-marketing-audit",
        "title": "yorCMO Marketing Audit – Q1 2026 Findings",
        "source": "marketing-audit",
        "content": (
            "yorCMO Marketing Audit — Q1 2026 Assessment & Findings\n\n"
            "An audit of yorCMO's current marketing operations was conducted in January 2026 "
            "to evaluate performance across all channels and identify areas for improvement.\n\n"
            "Key Audit Findings:\n"
            "1. Brand Awareness: LinkedIn followers stand at 1,245 with 2,180 monthly impressions "
            "and a 3.4% engagement rate — above the B2B industry average of 2.0%. However, organic "
            "reach has plateaued and needs a content refresh.\n"
            "2. Website Performance: 523 monthly sessions from 378 unique users. Organic search "
            "accounts for only 34% of traffic, indicating an SEO gap. Bounce rate is 52%, suggesting "
            "landing-page messaging could be tighter.\n"
            "3. Email Marketing: Open rate of 27.3% is solid (industry avg ~21%), but click-through "
            "rate of 3.1% lags behind top performers. List hygiene and segmentation recommended.\n"
            "4. Pipeline Health: $112K in active pipeline with a 28% close rate against a 25% target. "
            "Pipeline is healthy but heavily concentrated in two verticals.\n"
            "5. Client Satisfaction: NPS score of 54 and client satisfaction rating of 4.6/5.0 reflect "
            "strong delivery quality. Retention risk is low but upsell motion is under-developed.\n\n"
            "Audit Recommendations:\n"
            "- Invest in SEO content strategy to grow organic traffic by 40% over six months.\n"
            "- Launch a segmented email nurture series for different buyer personas.\n"
            "- Diversify pipeline sources beyond the current two dominant verticals.\n"
            "- Formalize a client upsell/cross-sell playbook to increase average revenue per client.\n"
            "- Implement marketing attribution tracking to measure true channel ROI.\n\n"
            "Overall Assessment: yorCMO's marketing foundation is solid with strong client satisfaction "
            "and above-average engagement metrics. The primary gaps are in organic acquisition and "
            "pipeline diversification. Addressing these will unlock the next phase of growth."
        ),
    },
    # 2 — Marketing Opportunities
    {
        "doc_id": "demo-marketing-opportunities",
        "title": "yorCMO Marketing Opportunities & Growth Potential",
        "source": "marketing-opportunities",
        "content": (
            "yorCMO Marketing Opportunities — Growth & Expansion Potential\n\n"
            "Based on the Q1 2026 marketing audit and current performance data, several high-impact "
            "marketing opportunities have been identified for yorCMO.\n\n"
            "Top Marketing Opportunities:\n\n"
            "1. SEO & Organic Growth Opportunity\n"
            "Current website traffic is 523 sessions/month with only 34% from organic search. "
            "Competitors average 45-60% organic traffic share. By investing in targeted SEO content — "
            "especially long-tail keywords around 'fractional CMO services' and 'outsourced marketing "
            "leadership' — yorCMO could realistically double organic traffic within 6 months, adding "
            "an estimated 250+ qualified monthly visits.\n\n"
            "2. LinkedIn Thought Leadership Expansion\n"
            "With 1,245 followers and a 3.4% engagement rate, yorCMO already outperforms most B2B "
            "companies on LinkedIn. The opportunity is to scale this into a systematic thought-leadership "
            "engine: weekly posts from each of the 26 active CMOs, collaborative content series, and "
            "LinkedIn newsletters. Target: 2,500 followers and 4,500+ monthly impressions by Q3 2026.\n\n"
            "3. Vertical Expansion into Healthcare & SaaS\n"
            "Pipeline analysis shows 70% of the $112K pipeline is concentrated in professional services "
            "and manufacturing. Healthcare and SaaS verticals are under-penetrated but represent the "
            "fastest-growing segments for fractional CMO demand. Two pilot engagements could validate "
            "the opportunity with minimal investment.\n\n"
            "4. Client Upsell & Expansion Revenue\n"
            "With 11 clients under management, NPS of 54, and satisfaction at 4.6/5.0, the upsell "
            "opportunity is significant. Current active MRR is $47,200 against a $45,000 target. "
            "Introducing tiered service packages and quarterly business reviews could increase average "
            "client revenue by 15-20%, pushing MRR toward $55,000.\n\n"
            "5. Email Nurture Automation\n"
            "The 27.3% email open rate indicates a warm, engaged list. Implementing automated drip "
            "sequences for different buyer stages could improve conversion from subscriber to discovery "
            "call by an estimated 25%. This is a low-cost, high-leverage opportunity.\n\n"
            "6. Strategic Partnerships & Referral Program\n"
            "A formalized referral program with complementary service providers (agencies, consultants, "
            "technology vendors) could generate 3-5 qualified leads per month with near-zero CAC.\n\n"
            "Prioritization: Opportunities are ranked by effort-to-impact ratio. SEO and email automation "
            "offer the highest leverage with the lowest investment, while vertical expansion offers the "
            "highest long-term growth ceiling."
        ),
    },
    # 3 — Ideal Client Profile
    {
        "doc_id": "demo-ideal-client-profile",
        "title": "yorCMO Ideal Client Profile & Target Market",
        "source": "ideal-client-profile",
        "content": (
            "yorCMO Ideal Client Profile (ICP) & Target Audience\n\n"
            "Understanding who our ideal client is drives every marketing and sales decision at yorCMO. "
            "The following profile is based on analysis of our most successful engagements across the "
            "11 clients currently under management.\n\n"
            "Primary Ideal Client Profile:\n"
            "- Company Size: 20-200 employees (mid-market and growth-stage)\n"
            "- Revenue Range: $5M-$50M annual revenue\n"
            "- Industries: Professional services, manufacturing, technology/SaaS, healthcare\n"
            "- Geography: United States, with concentration in Northeast and Southeast\n"
            "- Decision Maker: CEO, COO, or VP of Sales — typically a founder or C-suite executive "
            "who recognizes the need for marketing leadership but cannot justify a full-time CMO hire\n"
            "- Budget: $4,000-$8,000/month for fractional CMO engagement\n\n"
            "Ideal Client Characteristics:\n"
            "- Has reached a revenue plateau and needs strategic marketing to break through\n"
            "- Currently relies on word-of-mouth or a single channel for lead generation\n"
            "- Has a sales team but no dedicated marketing leadership or strategy\n"
            "- Recognizes that marketing is an investment, not just an expense\n"
            "- Values accountability, data-driven decision making, and measurable outcomes\n"
            "- Is ready to commit to a 6-12 month engagement for meaningful results\n\n"
            "Pain Points We Solve:\n"
            "- 'We know we need marketing but don't know where to start'\n"
            "- 'We've tried agencies but they don't understand our business'\n"
            "- 'We can't afford a full-time CMO but need that level of expertise'\n"
            "- 'Our sales team needs more and better-qualified leads'\n"
            "- 'We have no marketing strategy — just random tactics'\n\n"
            "Buyer Persona — 'Growth-Stage Greg':\n"
            "Greg is a 45-55 year old CEO/founder of a $10M professional services firm. He built the "
            "company through relationships and referrals but has hit a ceiling. He's analytical, "
            "ROI-focused, and skeptical of 'marketing fluff.' He wants a seasoned marketing executive "
            "who can build a repeatable growth engine without the overhead of a full-time hire.\n\n"
            "Secondary Target Audiences:\n"
            "- Private equity portfolio companies needing interim marketing leadership\n"
            "- Companies in transition (M&A, new product launch, market expansion)\n"
            "- Businesses that recently lost their marketing leader and need bridge coverage"
        ),
    },
    # 4 — Competitive Landscape
    {
        "doc_id": "demo-competitive-landscape",
        "title": "yorCMO Competitive Landscape & Differentiation",
        "source": "competitive-landscape",
        "content": (
            "yorCMO Competitive Landscape & Market Differentiation\n\n"
            "The fractional CMO market has grown significantly, and understanding our competitors is "
            "critical to maintaining yorCMO's position. Here is an analysis of the competitive landscape.\n\n"
            "Direct Competitors:\n\n"
            "1. Chief Outsiders\n"
            "- Largest fractional CMO firm nationally with 80+ CMOs\n"
            "- Strengths: Brand recognition, large team, national presence\n"
            "- Weaknesses: Less personalized service, higher price point, slower to adapt\n"
            "- Differentiator vs yorCMO: We offer more hands-on, embedded engagement with tighter "
            "accountability through our scorecard-driven approach.\n\n"
            "2. Marketri\n"
            "- Mid-size fractional CMO firm focused on B2B\n"
            "- Strengths: Strong B2B focus, good case studies\n"
            "- Weaknesses: Limited geographic reach, smaller team\n"
            "- Differentiator vs yorCMO: Our 26 active CMOs give us broader industry coverage and "
            "the ability to match clients with specialized expertise.\n\n"
            "3. CMOx\n"
            "- Franchise model for fractional CMOs\n"
            "- Strengths: Systematized methodology, growing network\n"
            "- Weaknesses: Inconsistent quality due to franchise model, less collaborative\n"
            "- Differentiator vs yorCMO: Our CMOs operate as a collaborative team, sharing best "
            "practices and resources, rather than as independent franchisees.\n\n"
            "4. Independent Fractional CMOs\n"
            "- Solo practitioners offering similar services\n"
            "- Strengths: Lower cost, direct relationship\n"
            "- Weaknesses: No bench strength, single point of failure, limited tools/resources\n"
            "- Differentiator vs yorCMO: We provide the depth of a full marketing department — "
            "strategy, execution support, analytics, and a network of 26 CMOs to draw upon.\n\n"
            "Indirect Competitors:\n"
            "- Full-service marketing agencies (lack strategic leadership)\n"
            "- Management consulting firms (expensive, not execution-oriented)\n"
            "- In-house marketing hires (full-time cost for part-time need)\n\n"
            "yorCMO's Competitive Advantages:\n"
            "- Scorecard-driven accountability: Every engagement is measured against clear KPIs\n"
            "- Network of 26 specialized CMOs with diverse industry expertise\n"
            "- Proven metrics: 28% close rate, $47,200 active MRR, NPS of 54\n"
            "- Embedded model: Our CMOs integrate with client teams, not just advise from the outside\n"
            "- Technology-enabled: Data-driven approach with real-time performance tracking\n\n"
            "Market Position: yorCMO sits in the sweet spot between expensive consulting firms and "
            "unreliable solo practitioners, offering enterprise-grade marketing leadership at a "
            "fraction of the cost."
        ),
    },
    # 5 — Brand Positioning
    {
        "doc_id": "demo-brand-positioning",
        "title": "yorCMO Brand Positioning & Value Proposition",
        "source": "brand-positioning",
        "content": (
            "yorCMO Brand Positioning, Messaging & Value Proposition\n\n"
            "Brand Promise:\n"
            "yorCMO delivers experienced marketing leadership to growth-stage businesses that need "
            "CMO-level strategy without the full-time executive cost.\n\n"
            "Core Value Proposition:\n"
            "'Get a seasoned Chief Marketing Officer — and the team behind them — for a fraction of "
            "the cost of a full-time hire. Our CMOs don't just advise; they embed in your business, "
            "build your marketing engine, and deliver measurable growth.'\n\n"
            "Brand Pillars:\n"
            "1. Accountability: Every engagement is driven by a scorecard with clear targets. "
            "Current metrics demonstrate this — 28% close rate (target 25%), $47,200 MRR (target "
            "$45,000), and NPS of 54.\n"
            "2. Expertise: A network of 26 active CMOs with deep experience across industries "
            "including professional services, manufacturing, healthcare, and technology.\n"
            "3. Results: We measure success by client outcomes — pipeline growth ($112K active), "
            "revenue acceleration, and market positioning improvement.\n"
            "4. Partnership: Our CMOs become part of your leadership team, not outside consultants "
            "who disappear after delivering a strategy deck.\n\n"
            "Messaging Framework:\n"
            "- Headline: 'Marketing Leadership That Delivers Results'\n"
            "- Subhead: 'Fractional CMO services for growing businesses'\n"
            "- Elevator Pitch: 'yorCMO provides experienced marketing executives to mid-market "
            "businesses on a fractional basis. Our CMOs integrate with your team, build strategic "
            "marketing plans, and execute against measurable scorecards — all at a fraction of the "
            "cost of a full-time CMO.'\n\n"
            "Brand Voice & Tone:\n"
            "- Professional but approachable — not corporate-stiff or startup-casual\n"
            "- Data-driven — always support claims with metrics and outcomes\n"
            "- Confident and direct — we know our value and communicate it clearly\n"
            "- Educational — position yorCMO as a thought leader who helps clients understand "
            "modern marketing\n\n"
            "Key Differentiating Messages:\n"
            "- 'Not an agency. Not a consultant. A marketing leader who becomes part of your team.'\n"
            "- 'Scorecard-driven marketing — because strategy without measurement is just guessing.'\n"
            "- '26 CMOs. One network. Unmatched expertise at your fingertips.'\n"
            "- 'We've helped 11 clients build marketing engines that drive real pipeline — $112K "
            "and growing.'"
        ),
    },
    # 6 — Service Offerings & Packages
    {
        "doc_id": "demo-service-offerings",
        "title": "yorCMO Service Offerings, Packages & Pricing",
        "source": "service-offerings",
        "content": (
            "yorCMO Service Offerings, Packages & Pricing Overview\n\n"
            "yorCMO offers fractional CMO services and marketing leadership packages designed for "
            "mid-market businesses ($5M-$50M revenue) that need senior marketing expertise without "
            "the cost of a full-time executive.\n\n"
            "Core Service: Fractional CMO Engagement\n"
            "- A seasoned CMO embedded in your business 1-3 days per week\n"
            "- Strategic marketing planning and execution oversight\n"
            "- Team leadership and vendor management\n"
            "- Scorecard-driven performance tracking\n"
            "- Access to yorCMO's network of 26 CMOs for specialized expertise\n\n"
            "Service Packages:\n\n"
            "1. Strategy Package — $4,000/month\n"
            "- 1 day/week CMO engagement\n"
            "- Marketing strategy development and quarterly planning\n"
            "- Monthly scorecard review and reporting\n"
            "- Best for: Companies starting their marketing journey\n\n"
            "2. Growth Package — $6,500/month (Most Popular)\n"
            "- 2 days/week CMO engagement\n"
            "- Full marketing strategy and execution oversight\n"
            "- Weekly scorecard reviews and bi-weekly team meetings\n"
            "- Vendor/agency selection and management\n"
            "- Best for: Companies ready to scale their marketing\n\n"
            "3. Accelerator Package — $9,000/month\n"
            "- 3 days/week CMO engagement\n"
            "- Comprehensive marketing leadership and team building\n"
            "- Daily availability and hands-on execution support\n"
            "- Strategic initiatives and market expansion planning\n"
            "- Best for: Companies in rapid growth or transformation\n\n"
            "Add-On Services:\n"
            "- Marketing Audit & Assessment: $3,500 one-time (see audit findings)\n"
            "- Content Strategy & Editorial Calendar: $1,500/month\n"
            "- LinkedIn & Social Media Management: $1,200/month\n"
            "- Email Marketing Automation Setup: $2,500 one-time\n\n"
            "Current Portfolio Metrics:\n"
            "- 11 clients under active management\n"
            "- 26 active CMOs across the network\n"
            "- $47,200 monthly recurring revenue (target: $45,000+)\n"
            "- Average engagement duration: 9.5 months\n"
            "- Client satisfaction: 4.6/5.0, NPS: 54\n\n"
            "Engagement Process:\n"
            "1. Discovery call (30 min) → 2. Marketing assessment → 3. Proposal & CMO matching → "
            "4. Onboarding (2 weeks) → 5. Strategy development (30 days) → 6. Execution & optimization"
        ),
    },
    # 7 — Channel Performance
    {
        "doc_id": "demo-channel-performance",
        "title": "yorCMO Marketing Channel Performance & ROI",
        "source": "channel-performance",
        "content": (
            "yorCMO Marketing Channel Performance & ROI Analysis\n\n"
            "This report summarizes performance across all active marketing channels for yorCMO "
            "as of Q1 2026.\n\n"
            "1. LinkedIn (Primary Social Channel)\n"
            "- Followers: 1,245 (up 12% QoQ)\n"
            "- Monthly Impressions: 2,180\n"
            "- Engagement Rate: 3.4% (industry avg: 2.0%)\n"
            "- Top content types: CMO thought leadership posts, client success stories, industry insights\n"
            "- ROI Assessment: HIGH — lowest CAC channel, drives brand authority and inbound leads\n\n"
            "2. Website / Organic Search\n"
            "- Monthly Sessions: 523\n"
            "- Unique Users: 378\n"
            "- Organic Traffic Share: 34% (target: 50%)\n"
            "- Top Landing Pages: Homepage (38%), Services page (22%), Blog (18%), About (12%)\n"
            "- Bounce Rate: 52%\n"
            "- ROI Assessment: MEDIUM — strong potential but under-invested in SEO content\n\n"
            "3. Email Marketing\n"
            "- List Size: ~1,800 subscribers\n"
            "- Open Rate: 27.3% (industry avg: 21%)\n"
            "- Click-Through Rate: 3.1%\n"
            "- Monthly Sends: 4 (weekly newsletter)\n"
            "- ROI Assessment: HIGH — warm audience with strong engagement, low cost per touch\n\n"
            "4. Referral / Word-of-Mouth\n"
            "- Estimated 40% of new pipeline comes from referrals and existing client introductions\n"
            "- NPS of 54 drives strong organic advocacy\n"
            "- No formalized referral program in place (opportunity identified in audit)\n"
            "- ROI Assessment: HIGHEST — zero acquisition cost, highest quality leads\n\n"
            "5. Direct Outreach / Sales\n"
            "- Outbound contributes approximately 25% of pipeline\n"
            "- Close rate on outbound-sourced opportunities: 22% (vs 28% overall)\n"
            "- Primary outreach channels: LinkedIn DMs, email sequences\n"
            "- ROI Assessment: MEDIUM — positive ROI but lower conversion than inbound\n\n"
            "Channel Mix Summary:\n"
            "- Total Pipeline: $112K (target: $100K+)\n"
            "- Pipeline by Source: Referral 40%, Inbound/Organic 35%, Outbound 25%\n"
            "- Recommended Shift: Increase organic/inbound from 35% to 50% by investing in SEO "
            "and content marketing, reducing reliance on referrals for sustainable growth.\n\n"
            "Digital marketing performance overall is strong. The key gap is organic search, which "
            "represents the biggest channel performance improvement opportunity."
        ),
    },
    # 8 — Marketing Strategy 2026
    {
        "doc_id": "demo-marketing-strategy-2026",
        "title": "yorCMO Marketing Strategy & Plan 2026",
        "source": "marketing-strategy",
        "content": (
            "yorCMO Marketing Strategy & Goals — 2026 Annual Plan\n\n"
            "Vision: Establish yorCMO as the premier fractional CMO firm for mid-market businesses, "
            "growing from 26 to 35 active CMOs and from $47,200 to $65,000 MRR by year-end 2026.\n\n"
            "Strategic Goals:\n"
            "1. Grow active CMO network from 26 to 35 (target: ≥27 near-term)\n"
            "2. Increase MRR from $47,200 to $65,000 (current target: ≥$45,000)\n"
            "3. Expand pipeline from $112K to $200K (current target: ≥$100K)\n"
            "4. Maintain close rate ≥25% (currently 28%)\n"
            "5. Grow LinkedIn followers from 1,245 to 3,000\n"
            "6. Increase website organic traffic by 80%\n\n"
            "Quarterly Tactics:\n\n"
            "Q1 2026 (Current) — Foundation\n"
            "- Complete marketing audit (done — see audit findings)\n"
            "- Launch refreshed website messaging and SEO strategy\n"
            "- Implement marketing attribution tracking\n"
            "- Establish baseline metrics for all channels\n\n"
            "Q2 2026 — Content & SEO Push\n"
            "- Publish 12 SEO-optimized blog posts targeting 'fractional CMO' keywords\n"
            "- Launch CMO thought leadership series on LinkedIn (2 posts/week per CMO)\n"
            "- Implement email segmentation and automated nurture sequences\n"
            "- Goal: Organic traffic +30%, LinkedIn followers to 1,800\n\n"
            "Q3 2026 — Pipeline Acceleration\n"
            "- Launch formal referral program with incentive structure\n"
            "- Enter healthcare and SaaS verticals with targeted campaigns\n"
            "- Host 2 webinars on marketing leadership topics\n"
            "- Goal: Pipeline to $150K, 3 new clients\n\n"
            "Q4 2026 — Scale & Optimize\n"
            "- Optimize top-performing channels based on attribution data\n"
            "- Launch client case study video series\n"
            "- Plan 2027 strategy based on full-year learnings\n"
            "- Goal: MRR to $65K, 35 active CMOs, pipeline to $200K\n\n"
            "Budget Allocation:\n"
            "- Content & SEO: 35% of marketing budget\n"
            "- Social media (LinkedIn focus): 20%\n"
            "- Email marketing & automation: 15%\n"
            "- Events & webinars: 15%\n"
            "- Tools & analytics: 15%\n\n"
            "Key Objectives for the marketing strategy include building a repeatable, scalable "
            "marketing engine that reduces reliance on referral-only growth while maintaining the "
            "high client satisfaction (4.6/5.0) and NPS (54) that drive organic advocacy."
        ),
    },
    # 9 — Content Marketing
    {
        "doc_id": "demo-content-marketing",
        "title": "yorCMO Content Marketing Strategy & Editorial Plan",
        "source": "content-marketing",
        "content": (
            "yorCMO Content Marketing Strategy & Editorial Plan\n\n"
            "Content marketing is a cornerstone of yorCMO's 2026 growth strategy. This plan outlines "
            "the content strategy, blog editorial calendar, and thought leadership approach.\n\n"
            "Content Strategy Overview:\n"
            "- Primary Goal: Drive organic traffic from 523 to 900+ monthly sessions\n"
            "- Secondary Goal: Establish yorCMO CMOs as thought leaders in marketing strategy\n"
            "- Content Pillars: Fractional CMO insights, marketing strategy, industry trends, "
            "client success stories, marketing measurement\n\n"
            "Blog & SEO Content Plan:\n"
            "- Publishing cadence: 3 posts/month (36 annually)\n"
            "- Target keywords: 'fractional CMO,' 'outsourced CMO,' 'marketing leadership,' "
            "'B2B marketing strategy,' 'marketing ROI measurement'\n"
            "- Content types: How-to guides (40%), thought leadership (30%), case studies (20%), "
            "industry analysis (10%)\n\n"
            "Editorial Calendar — Q1-Q2 2026:\n"
            "- January: 'What Is a Fractional CMO?', 'Marketing Audit Checklist for Mid-Market'\n"
            "- February: '5 Signs You Need a CMO', 'ROI of Fractional Marketing Leadership'\n"
            "- March: 'Building a Marketing Scorecard', 'Q1 Marketing Trends'\n"
            "- April: 'Fractional vs Full-Time CMO: Cost Comparison', 'SEO for B2B Companies'\n"
            "- May: 'How to Choose a Marketing Leader', client case study\n"
            "- June: 'Mid-Year Marketing Strategy Check-In', 'LinkedIn for B2B Growth'\n\n"
            "Thought Leadership Program:\n"
            "- Each of the 26 active CMOs contributes at least 1 LinkedIn post per month\n"
            "- Quarterly collaborative whitepapers on marketing trends\n"
            "- Monthly guest appearances on industry podcasts (target: 2/month)\n"
            "- Speaking engagements at 4 industry events per year\n\n"
            "Content Distribution:\n"
            "- Blog posts amplified via LinkedIn (1,245 followers) and email newsletter (~1,800 subs)\n"
            "- Repurpose long-form content into social snippets, email series, and infographics\n"
            "- SEO optimization for every published piece with internal linking strategy\n\n"
            "Content Performance Targets:\n"
            "- Blog traffic: 200+ monthly sessions by Q2 (currently ~94 from blog)\n"
            "- Email newsletter CTR: Improve from 3.1% to 4.5%\n"
            "- LinkedIn content impressions: Grow from 2,180 to 4,000/month\n"
            "- Lead magnet downloads: 25/month from gated content"
        ),
    },
    # 10 — Lead Generation & Pipeline
    {
        "doc_id": "demo-lead-generation-pipeline",
        "title": "yorCMO Lead Generation, Pipeline & Sales Funnel",
        "source": "lead-generation",
        "content": (
            "yorCMO Lead Generation, Pipeline & Sales Funnel Overview\n\n"
            "This document outlines yorCMO's current lead generation performance, pipeline health, "
            "and sales funnel metrics.\n\n"
            "Pipeline Summary:\n"
            "- Total Active Pipeline: $112,000 (target: ≥$100,000)\n"
            "- Pipeline is above target, indicating healthy demand generation\n"
            "- Active Proposals: 8 in various stages\n"
            "- Average Deal Size: $6,200/month\n"
            "- Average Sales Cycle: 45 days from discovery call to close\n\n"
            "Sales Funnel Metrics:\n"
            "- Monthly Inbound Leads: ~18\n"
            "- Discovery Calls Booked: ~12/month\n"
            "- Proposals Sent: ~6/month\n"
            "- Closed Won: ~2/month\n"
            "- Overall Close Rate: 28% (target: ≥25%)\n"
            "- Conversion: Lead → Discovery: 67%, Discovery → Proposal: 50%, Proposal → Close: 33%\n\n"
            "Lead Sources:\n"
            "- Referrals & Word-of-Mouth: 40% of pipeline (highest quality)\n"
            "- Inbound/Organic: 35% (website, LinkedIn, content marketing)\n"
            "- Outbound Prospecting: 25% (LinkedIn outreach, email sequences)\n\n"
            "Pipeline by Vertical:\n"
            "- Professional Services: 38% ($42,560)\n"
            "- Manufacturing: 32% ($35,840)\n"
            "- Technology/SaaS: 18% ($20,160)\n"
            "- Healthcare: 8% ($8,960)\n"
            "- Other: 4% ($4,480)\n\n"
            "Lead Generation Initiatives:\n"
            "1. LinkedIn Lead Gen: CMOs actively engage prospects through thought leadership content "
            "and direct outreach. LinkedIn drives the highest-quality inbound leads.\n"
            "2. Website Conversion: Contact forms and 'Schedule a Discovery Call' CTAs. Current "
            "website-to-lead conversion rate is 2.3% — target 3.5%.\n"
            "3. Email Nurture: Automated sequences for leads not yet ready for a discovery call.\n"
            "4. Referral Pipeline: Strongest source but unformalized. A structured referral program "
            "could increase referral-sourced leads by 50%.\n\n"
            "Pipeline Risks:\n"
            "- Over-concentration in professional services and manufacturing (70% combined)\n"
            "- No formalized lead scoring system — all leads treated equally\n"
            "- Limited marketing attribution makes ROI-by-channel difficult to measure\n\n"
            "Target: Grow pipeline to $150K by Q3 2026 through diversified lead generation and "
            "improved conversion at each funnel stage."
        ),
    },
    # 11 — Client Success & Retention
    {
        "doc_id": "demo-client-success-retention",
        "title": "yorCMO Client Success, Satisfaction & Retention Metrics",
        "source": "client-success",
        "content": (
            "yorCMO Client Success, Satisfaction & Retention Report\n\n"
            "Client satisfaction and retention are core to yorCMO's business model. Strong client "
            "outcomes drive referrals, which represent 40% of pipeline.\n\n"
            "Key Client Metrics:\n"
            "- Clients Under Management: 11\n"
            "- Client Satisfaction Score: 4.6/5.0\n"
            "- Net Promoter Score (NPS): 54 (Excellent — above 50 is world-class)\n"
            "- Client Retention Rate: 89% (annual)\n"
            "- Average Engagement Duration: 9.5 months\n"
            "- Client Churn Rate: 11% annually (~1.2 clients/year)\n\n"
            "NPS Breakdown:\n"
            "- Promoters (9-10): 64% of clients\n"
            "- Passives (7-8): 27% of clients\n"
            "- Detractors (0-6): 9% of clients\n"
            "- Key drivers of satisfaction: Strategic value, CMO expertise, accountability/scorecards\n"
            "- Key driver of detraction: Pace of results (expectation setting opportunity)\n\n"
            "Client Success Framework:\n"
            "1. Onboarding (Week 1-2): Deep-dive into business, market, and goals\n"
            "2. Strategy Phase (Month 1): Marketing audit, strategy development, scorecard setup\n"
            "3. Execution Phase (Month 2+): Implementing strategy, tracking KPIs, optimizing\n"
            "4. Quarterly Business Reviews: Formal review of progress against scorecard targets\n"
            "5. Ongoing: Weekly or bi-weekly check-ins with client leadership\n\n"
            "Retention Strategies:\n"
            "- Scorecard-driven accountability ensures clients see measurable progress\n"
            "- Regular QBRs maintain strategic alignment and demonstrate value\n"
            "- CMO matching process ensures personality and expertise fit\n"
            "- Escalation path: If a client relationship needs adjustment, we can swap CMOs\n\n"
            "Churn Analysis:\n"
            "- Primary churn reason: Client hired full-time CMO (positive outcome — we built the "
            "foundation for them to invest in full-time marketing leadership)\n"
            "- Secondary: Budget constraints or business pivots\n"
            "- Churn due to dissatisfaction: <3% — extremely low\n\n"
            "Upsell Opportunity:\n"
            "- Current average monthly revenue per client: $4,291 ($47,200 MRR ÷ 11 clients)\n"
            "- Target with upsell motion: $5,000-$5,500/client/month\n"
            "- Upsell paths: Package tier upgrades, add-on services (content, social, email)"
        ),
    },
    # 12 — Team Overview
    {
        "doc_id": "demo-team-overview",
        "title": "yorCMO Team Overview, Organization & Leadership",
        "source": "team-overview",
        "content": (
            "yorCMO Team Overview & Organizational Structure\n\n"
            "yorCMO operates as a network-based fractional CMO firm. Here is an overview of the team, "
            "organization structure, and leadership roles.\n\n"
            "Team Size & Composition:\n"
            "- Active CMOs: 26 (target: ≥27)\n"
            "- Core Leadership Team: 5 members\n"
            "- Support Staff: 3 (operations, marketing coordinator, client success)\n"
            "- Total Team: ~34 people across the organization\n\n"
            "Leadership Team:\n"
            "1. CEO / Founder — Overall strategy, vision, and business development\n"
            "2. COO — Operations, CMO onboarding, quality assurance\n"
            "3. VP of Client Success — Client satisfaction, retention, QBR oversight\n"
            "4. VP of Growth — Marketing, lead generation, brand building\n"
            "5. Director of CMO Network — Recruiting, training, and supporting the CMO network\n\n"
            "CMO Network Structure:\n"
            "- 26 active fractional CMOs operating across the United States\n"
            "- Each CMO manages 1-3 client engagements simultaneously\n"
            "- CMOs are W-2 contractors with deep expertise in specific industries and functions\n"
            "- Specializations include: digital marketing, brand strategy, demand generation, "
            "content marketing, product marketing, and marketing analytics\n"
            "- CMOs participate in monthly network calls and quarterly summits\n\n"
            "CMO Industry Expertise:\n"
            "- Professional Services: 8 CMOs\n"
            "- Manufacturing/Industrial: 5 CMOs\n"
            "- Technology/SaaS: 6 CMOs\n"
            "- Healthcare: 4 CMOs\n"
            "- Other (Retail, Education, Nonprofit): 3 CMOs\n\n"
            "Roles and Responsibilities:\n"
            "- CMOs: Client-facing marketing leadership, strategy, and execution oversight\n"
            "- Operations: Billing, contracts, scheduling, tool management\n"
            "- Marketing Coordinator: Internal marketing execution (website, social, email)\n"
            "- Client Success Manager: Onboarding support, satisfaction monitoring, escalations\n\n"
            "Growth Plan:\n"
            "- Recruiting target: 9 additional CMOs in 2026 (26 → 35)\n"
            "- Focus areas for new hires: Healthcare (2), SaaS (3), General (4)\n"
            "- CMO onboarding process: 2-week training on yorCMO methodology, tools, and scorecard "
            "framework before first client assignment"
        ),
    },
    # 13 — Website & SEO
    {
        "doc_id": "demo-website-seo",
        "title": "yorCMO Website Performance, SEO & Analytics",
        "source": "website-seo",
        "content": (
            "yorCMO Website Performance, SEO & Analytics Report\n\n"
            "This report covers yorCMO's website analytics, SEO performance, and optimization "
            "opportunities.\n\n"
            "Website Traffic Overview:\n"
            "- Monthly Sessions: 523\n"
            "- Unique Users: 378\n"
            "- Pages per Session: 2.4\n"
            "- Average Session Duration: 2:15\n"
            "- Bounce Rate: 52%\n\n"
            "Traffic Sources:\n"
            "- Organic Search: 34% (178 sessions) — below target of 50%\n"
            "- Direct: 28% (146 sessions)\n"
            "- Social (primarily LinkedIn): 18% (94 sessions)\n"
            "- Referral: 12% (63 sessions)\n"
            "- Email: 8% (42 sessions)\n\n"
            "Top Landing Pages:\n"
            "1. Homepage — 38% of entrances, 48% bounce rate\n"
            "2. Services / Fractional CMO page — 22%, 41% bounce rate\n"
            "3. Blog (aggregate) — 18%, 62% bounce rate\n"
            "4. About / Team page — 12%, 38% bounce rate\n"
            "5. Contact page — 10%, 22% bounce rate\n\n"
            "SEO Performance:\n"
            "- Ranking Keywords: 142 (47 in top 50 positions)\n"
            "- Top Ranking Keywords: 'fractional CMO services' (#18), 'outsourced CMO' (#24), "
            "'marketing leadership consulting' (#31)\n"
            "- Domain Authority: 32 (target: 45 by end of 2026)\n"
            "- Backlinks: 89 referring domains\n"
            "- Content Gap: Minimal blog content targeting long-tail keywords — major SEO opportunity\n\n"
            "Conversion Metrics:\n"
            "- Website-to-Lead Conversion Rate: 2.3%\n"
            "- Monthly Leads from Website: ~12\n"
            "- Top Converting Pages: Services page (4.1% CVR), Contact page (8.2% CVR)\n"
            "- Primary CTA: 'Schedule a Discovery Call' button\n\n"
            "SEO Optimization Opportunities:\n"
            "1. Content Gap: Only 12 blog posts exist. Target: 48 posts by year-end (3/month)\n"
            "2. Technical SEO: Page speed score is 72/100 — optimize images and caching\n"
            "3. On-Page SEO: Services pages need schema markup and improved meta descriptions\n"
            "4. Local SEO: Claim and optimize Google Business Profile\n"
            "5. Link Building: Target 20 new referring domains per quarter through guest posting "
            "and partnerships\n\n"
            "Website analytics show a solid foundation but significant room for organic traffic growth. "
            "SEO investment is the top recommended priority from the marketing audit."
        ),
    },
    # 14 — Email Marketing
    {
        "doc_id": "demo-email-marketing",
        "title": "yorCMO Email Marketing Performance & Campaigns",
        "source": "email-marketing",
        "content": (
            "yorCMO Email Marketing Performance & Campaign Report\n\n"
            "Email marketing is one of yorCMO's highest-ROI channels. This report covers current "
            "performance, campaigns, and optimization opportunities.\n\n"
            "Email List & Subscribers:\n"
            "- Total Subscribers: ~1,800\n"
            "- List Growth Rate: 4.2% monthly\n"
            "- Subscriber Sources: Website opt-ins (45%), LinkedIn lead magnets (30%), "
            "event registrations (15%), referrals (10%)\n"
            "- List Health: 92% deliverability, 0.3% spam complaint rate\n\n"
            "Campaign Performance Metrics:\n"
            "- Average Open Rate: 27.3% (industry average: 21%)\n"
            "- Average Click-Through Rate (CTR): 3.1% (industry avg: 2.6%)\n"
            "- Unsubscribe Rate: 0.4% per send\n"
            "- Monthly Email Sends: 4 (weekly newsletter)\n\n"
            "Active Email Campaigns:\n"
            "1. Weekly Newsletter — 'The CMO Brief'\n"
            "   - Sent every Tuesday at 9am ET\n"
            "   - Content: Marketing insights, industry trends, yorCMO updates\n"
            "   - Open Rate: 29.1%, CTR: 3.4%\n"
            "   - Best performing segment: CEOs of $5-20M companies\n\n"
            "2. New Subscriber Welcome Series (3-email sequence)\n"
            "   - Email 1: Welcome + 'What is a Fractional CMO?' guide (42% open rate)\n"
            "   - Email 2: Client success story + CTA to schedule call (31% open rate)\n"
            "   - Email 3: Service overview + special offer (28% open rate)\n"
            "   - Series conversion rate to discovery call: 4.8%\n\n"
            "3. Monthly Case Study Spotlight\n"
            "   - Sent first Thursday of each month\n"
            "   - Highlights a client success story with measurable results\n"
            "   - Open Rate: 25.7%, CTR: 4.2% (highest CTR campaign)\n\n"
            "Email Marketing Opportunities:\n"
            "1. Segmentation: Split list by industry, company size, and engagement level to "
            "deliver more targeted content. Expected impact: +15% open rate improvement.\n"
            "2. Automated Nurture Sequences: Build stage-specific drip campaigns for leads at "
            "different points in the buyer journey.\n"
            "3. Re-engagement Campaign: 22% of list hasn't opened in 90 days — run a re-engagement "
            "series before pruning to maintain list health.\n"
            "4. A/B Testing: Systematic subject line and send-time testing to push open rate "
            "toward 30%+.\n\n"
            "Email remains a high-performing channel for yorCMO with above-average engagement metrics. "
            "The primary optimization opportunity is in segmentation and automation to improve "
            "conversion rates at each stage of the funnel."
        ),
    },
    # 15 — Social Media & LinkedIn
    {
        "doc_id": "demo-social-media-linkedin",
        "title": "yorCMO Social Media & LinkedIn Performance",
        "source": "social-media-linkedin",
        "content": (
            "yorCMO Social Media & LinkedIn Performance Report\n\n"
            "LinkedIn is yorCMO's primary social media platform, reflecting the B2B nature of the "
            "fractional CMO business. This report covers social media performance and strategy.\n\n"
            "LinkedIn Company Page Metrics:\n"
            "- Followers: 1,245\n"
            "- Monthly Impressions: 2,180\n"
            "- Engagement Rate: 3.4% (industry average for B2B: 2.0%)\n"
            "- Post Frequency: 3-4 posts/week\n"
            "- Follower Growth Rate: 6.8% monthly\n\n"
            "LinkedIn Content Performance by Type:\n"
            "1. CMO Thought Leadership Posts: Highest engagement (4.2% avg)\n"
            "   - Personal insights from the 26 active CMOs\n"
            "   - Marketing strategy tips and frameworks\n"
            "2. Client Success Stories: Strong engagement (3.8% avg)\n"
            "   - Before/after metrics, testimonials\n"
            "3. Industry Insights & Trends: Good engagement (3.1% avg)\n"
            "   - Market data, survey results, trend analysis\n"
            "4. Company Updates: Lower engagement (2.3% avg)\n"
            "   - Team news, event announcements, hiring\n\n"
            "LinkedIn Engagement Breakdown:\n"
            "- Likes: 62% of all engagements\n"
            "- Comments: 23% (highest-value interaction)\n"
            "- Shares: 11%\n"
            "- Clicks: 4% (drives to website)\n\n"
            "Top Performing Posts (Last 90 Days):\n"
            "1. 'The 5 Signs Your Business Has Outgrown DIY Marketing' — 4,200 impressions, 6.1% engagement\n"
            "2. 'Why Every $10M Company Needs a Marketing Scorecard' — 3,800 impressions, 5.4% engagement\n"
            "3. Client case study: Manufacturing company grew pipeline 40% — 3,100 impressions, 4.8% engagement\n\n"
            "Social Media Strategy for 2026:\n"
            "1. Increase posting frequency to 5x/week on company page\n"
            "2. Launch individual CMO LinkedIn profiles as brand ambassadors (26 CMOs × 1 post/week)\n"
            "3. Test LinkedIn Newsletter format for 'The CMO Brief'\n"
            "4. Experiment with LinkedIn Live for Q&A sessions and webinars\n"
            "5. Target: 2,500 followers by Q3, 3,000 by year-end\n\n"
            "Other Social Platforms:\n"
            "- Twitter/X: Minimal presence (not a priority for B2B fractional CMO audience)\n"
            "- YouTube: Planned for Q3 — client case study video series\n"
            "- Instagram: Not active (not aligned with target audience)\n\n"
            "LinkedIn is the clear winner for yorCMO's social media efforts, with engagement rates "
            "nearly double the B2B industry average. The opportunity is to scale content production "
            "through the CMO network and convert followers into leads more systematically."
        ),
    },
]


def main():
    print("Seeding yorCMO demo knowledge entries...")
    for i, entry in enumerate(ENTRIES, 1):
        entry_id = save_knowledge_entry(
            content=f"{entry['title']}\n\n{entry['content']}",
            org_slug="yorcmo",
            source=entry["source"],
            doc_id=entry["doc_id"],
            metadata={"title": entry["title"], "demo": True},
        )
        print(f"  [{i:>2}/15] {entry['title']} → {entry_id}")
    print(f"\nDone! Seeded 15 knowledge entries.")


if __name__ == "__main__":
    main()
