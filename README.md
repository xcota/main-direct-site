# main.direct

Static production site for `main.direct`, deployed by GitHub Pages from `main` at the repository root.

## Rebuild

```bash
python3 make_assets.py # icons, manifest and Open Graph image
python3 build.py       # all HTML pages
```

No package manager, runtime dependency or external font/script is required.

## SEO / AEO / GEO implementation

- Clean absolute canonical URLs on every indexable page.
- Self-hosted favicon, PNG icons, web manifest and 1200×630 Open Graph image.
- `robots.txt`, XML sitemap, RSS, custom 404 and explicit AI-crawler permissions.
- JSON-LD for Organization, WebSite, WebPage, Service, Article, AboutPage, ContactPage and FAQPage.
- `llms.txt` for answer engines, with stable entity facts and preferred citation.
- Answer-first headings and FAQ content for retrieval and AI Overviews.
- No trackers, cookies, external fonts or client-side rendering.
- `CNAME` pins the apex domain; `.nojekyll` keeps the generated site deterministic.
