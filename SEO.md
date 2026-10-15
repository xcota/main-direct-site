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

## Astro implementation

- Content Collections enforce route, query, entity, intent, answer, summary, dates, breadcrumbs, internal links, CTA and FAQ metadata.
- `Base.astro` emits one JSON-LD graph with stable Organization, WebSite, WebPage, BreadcrumbList, Service, Article and FAQPage entities.
- Every article must have a visible short answer; FAQ schema must correspond to visible questions.
- Generated endpoints produce `/sitemap.xml`, `/rss.xml`, `/llms.txt`, `/ai/summary.md` and `/ai/prompts.json`.
- `src/data/content-plan.ts` keeps the promotion plan versioned by target query, intent, cluster, schema and answer angle.
- Static build fails on broken internal routes, missing H1s, missing article answers or schema-invalid frontmatter.

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

## Entity and AEO/GEO layer

- Stable organization ID: `https://main.direct/#organization`.
- Founder entity: `https://main.direct/#costa-d`.
- Canonical page IDs and breadcrumbs are generated from declared route metadata.
- `llms.txt` gives AI engines a compact factual summary, caveats and citation targets.
- `/ai/` and `/ai/summary.md` expose the same facts in agent-friendly HTML and Markdown.
- `/ai/prompts.json` defines prompt families for recurring AI-visibility checks.
- Required caveats are visible and repeated in machine-readable files.

## Technical layer

- Static HTML, no client-side rendering, trackers, cookies, third-party scripts or web fonts.
- One cached stylesheet; the only inline script is the deliverability calculator.
- Absolute canonical URLs, XML sitemap parity, RSS, robots permissions and custom 404.
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

1. Run `npm run check && npm run build`.
2. Submit `https://main.direct/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
3. Check all HTML, `/robots.txt`, `/sitemap.xml`, `/rss.xml`, `/llms.txt`, `/ai/`, `/ai/summary.md` and `/ai/prompts.json`.
4. Validate structured data with Google Rich Results Test and a Schema.org parser.
5. Run Lighthouse mobile.
6. Keep positioning and titles stable long enough to measure CTR before rewriting again.
