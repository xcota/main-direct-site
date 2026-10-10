# main.direct

Static production site for `main.direct`, deployed by GitHub Pages from `main` at the repository root.

## Rebuild

```bash
python3 make_assets.py # icons, manifest and Open Graph image
python3 build.py       # all HTML pages
```

No package manager, runtime dependency or external font/script is required.

## Product architecture

The site presents Main Direct as a B2B outreach supply engine, not a list broker or agency:

- **Signal Atlas** — audience research, buying triggers, evidence rules and targeting filters.
- **Contact Supply** — company resolution, mailbox validation, identity checks, provenance and normalization.
- **Deliverability Engine** — dedicated sending domains, SPF/DKIM/DMARC, warm-up gates, pacing, suppression and reply routing.
- **First-touch routing** — qualification, message architecture, reply routing and campaign learning.

## SEO / AEO / GEO implementation

- Clean absolute canonical URLs on every indexable page.
- Self-hosted favicon, PNG icons, web manifest and 1200×630 Open Graph image.
- `robots.txt`, XML sitemap, RSS, custom 404 and explicit AI-crawler permissions.
- JSON-LD for Organization, WebSite, WebPage, Service, Article, AboutPage, ContactPage and FAQPage.
- `llms.txt`, `/ai/`, `/ai/summary.md` and `/ai/prompts.json` for answer engines and research agents.
- Product modules, public methodology and required caveats are stated in visible HTML, not only schema.
- No trackers, cookies, external fonts or client-side rendering. The deliverability calculator is inline vanilla JavaScript.
- `CNAME` pins the apex domain; `.nojekyll` keeps the generated site deterministic.

## Quality gates

No invented customer counts, reply rates, inbox-placement promises, revenue or funding claims. Verification and deliverability are explicitly time-bound and planning-only.
