# main.direct search / answer engine plan

## Positioning

Primary entity: **Main Direct**, a B2B contact-data and email-deliverability infrastructure practice. The site deliberately avoids the old “consulting / retainers” framing and does not claim client results that are not evidenced.

## Search targets

Primary:

- B2B contact data infrastructure
- contact validation pipeline
- email deliverability infrastructure
- cold email sending domain architecture
- SPF DKIM DMARC cold email setup
- cold email warm-up system
- B2B outreach data pipeline

Secondary:

- investor outreach contact validation
- clean B2B contact database
- sender reputation guardrails
- first-touch email architecture

## Entity and AEO layer

- Stable organization ID: `https://main.direct/#organization`.
- Founder entity: `https://main.direct/#costa-d`.
- Organization schema on every page; Service, Article, FAQ, About, Contact and Privacy schemas where relevant.
- `llms.txt` gives AI engines a compact factual summary and preferred citation.
- Every FAQ answer begins with the answer, not marketing context.
- The playbook contains a reusable definition, score, checklist and sequence, making it quotable by answer engines.

## Technical layer

- Static HTML, no client-side rendering.
- One cached stylesheet, no third-party scripts, no web fonts.
- Absolute canonical URLs, XML sitemap, RSS, robots permissions and custom 404.
- SVG/PNG icons, web manifest, Open Graph/Twitter card and explicit image dimensions.
- Accessibility: landmarks, skip link, alt text, visible focus, contrast and mobile navigation.
- `.nojekyll` and `CNAME` keep GitHub Pages serving the apex domain predictably.

## Next operational checks after deploy

1. Submit `https://main.direct/sitemap.xml` in Google Search Console and Bing Webmaster Tools.
2. Test `/`, `/services/`, `/playbooks/contact-to-inbox/`, `/faq/`, `/contact/`, `/robots.txt`, `/sitemap.xml`, `/rss.xml` and `/llms.txt`.
3. Validate structured data in Google Rich Results and Schema.org parser.
4. Run Lighthouse mobile and check image dimensions, contrast and tap targets.
5. Keep page titles/descriptions stable long enough to measure CTR before changing wording again.
