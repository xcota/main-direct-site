# main.direct

Astro-based static production site for `main.direct`, deployed by GitHub Pages from `main` at the repository root.

## Source model

- `src/content/pages/` — every route as Markdown with strict SEO/AEO/GEO frontmatter.
- `src/layouts/Base.astro` — shell, navigation, canonical/OG/Twitter metadata and JSON-LD graph.
- `src/pages/[...page].astro` — renders content collections and rejects broken internal links.
- `src/pages/*.xml.ts` and `src/pages/ai/*` — generated `sitemap.xml`, `rss.xml`, `llms.txt` and AI surfaces.
- `src/data/content-plan.ts` — versioned promotion plan by route, target query, intent, cluster and schema.
- `public/` — static deploy assets copied verbatim by Astro.
- Repository-root HTML/files — generated deploy output committed for branch-based GitHub Pages.

## Commands

```bash
npm install
npm run dev        # local Astro server
npm run check      # Astro/TypeScript diagnostics
npm run build      # build, publish dist/ to repo root, verify static output
```

Asset regeneration is optional and requires Pillow:

```bash
python3 make_assets.py
```

## Content contract

Every indexable page must declare a canonical path, target query, entity, intent, direct answer, AI summary, page type, modification date, breadcrumbs, at least three internal links and a CTA. Article pages must expose a visible short answer. FAQ pages need visible questions matching `FAQPage` schema. Build fails when those constraints or internal routes break.

## Product architecture

Main Direct is presented as a B2B outreach supply engine, not a list broker or agency:

- **Signal Atlas** — audience research, buying triggers, evidence rules and targeting filters.
- **Contact Supply** — company resolution, mailbox validation, identity checks, provenance and normalization.
- **Deliverability Engine** — dedicated sending domains, SPF/DKIM/DMARC, warm-up gates, pacing, suppression and reply routing.
- **First-touch routing** — qualification, message architecture, reply routing and campaign learning.

## Quality gates

`scripts/verify_static.py` checks generated HTML counts, canonical URLs, metadata, H1/main landmarks, JSON-LD, internal/asset links, the FormSubmit route, sitemap parity, RSS, `llms.txt`, AI JSON and Pages assets. The build also rejects invented-proof language boundaries by keeping required caveats in the content model.

No invented customer counts, reply rates, inbox-placement promises, revenue or funding claims.
