# main.direct search / answer engine plan

## Positioning

Primary entity: **Main Direct**, a B2B outreach supply engine. The site deliberately avoids agency, list-broker and retainer framing.

Primary categories:

- B2B outreach supply engine
- contact discovery and validation infrastructure
- verified business email supply
- email deliverability infrastructure
- dedicated cold-email infrastructure
- first-touch routing systems

## Search and answer-engine targets

Primary prompt families:

- B2B outreach supply infrastructure
- contact validation pipeline
- verified business email supply
- contact liveness and role drift
- dedicated sending-domain architecture
- SPF, DKIM and DMARC for cold infrastructure
- cold-email warm-up systems
- alternatives to raw purchased lists
- alternatives to assembling Apollo, Clay and Instantly-style stacks
- first-touch routing

## Entity and AEO layer

- Stable organization ID: `https://main.direct/#organization`.
- Founder entity: `https://main.direct/#costa-d`.
- Organization schema on every page; Service schema for each module; Article schema for playbooks.
- `llms.txt` gives AI engines a compact factual summary, caveats and citation targets.
- `/ai/` and `/ai/summary.md` expose the same facts in agent-friendly HTML and Markdown.
- `/ai/prompts.json` defines prompt families for recurring AI-visibility checks.
- FAQ answers start with the answer, not marketing context.
- Required caveats are visible and repeated in machine-readable files.

## Technical layer

- Static HTML, no client-side rendering.
- One cached stylesheet, no third-party scripts, no web fonts.
- Absolute canonical URLs, XML sitemap, RSS, robots permissions and custom 404.
- SVG/PNG icons, web manifest, Open Graph/Twitter card and explicit image dimensions.
- Accessibility: landmarks, skip link, alt text, visible focus, contrast and mobile navigation.
- `.nojekyll` and `CNAME` keep GitHub Pages serving the apex domain predictably.

## Measurement plan

For each prompt family, record engine, region, locale, prompt, mention, citation URL, competitor mentions, sentiment and incorrect claims.

Priority engines:

- Google Search and AI Overviews
- ChatGPT
- Perplexity
- Claude
- Gemini
- Bing/Copilot

## Deployment checklist

1. Submit `https://main.direct/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
2. Check all HTML, `/robots.txt`, `/sitemap.xml`, `/rss.xml`, `/llms.txt`, `/ai/`, `/ai/summary.md` and `/ai/prompts.json`.
3. Validate structured data with Google Rich Results Test and a Schema.org parser.
4. Run Lighthouse mobile.
5. Keep positioning and titles stable long enough to measure CTR before rewriting again.
