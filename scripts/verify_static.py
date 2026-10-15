#!/usr/bin/env python3
"""Fail-closed checks for the generated main.direct static site."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

BASE = 'https://main.direct'
ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'


@dataclass
class PageData:
    path: str
    file: Path
    title: str = ''
    description: str = ''
    robots: str = ''
    canonical: str = ''
    h1_count: int = 0
    main_count: int = 0
    internal_links: set[str] = field(default_factory=set)
    asset_links: set[str] = field(default_factory=set)
    json_ld: list[object] = field(default_factory=list)
    scripts: list[str] = field(default_factory=list)
    forms: list[str] = field(default_factory=list)


class HtmlAuditParser(HTMLParser):
    def __init__(self, data: PageData):
        super().__init__(convert_charrefs=True)
        self.data = data
        self.in_ld = False
        self.ld_chunks: list[str] = []
        self.ld_type = ''
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or '' for key, value in attrs}
        if tag == 'title':
            self.in_title = True
        elif tag == 'meta':
            name = values.get('name')
            prop = values.get('property')
            content = values.get('content', '')
            if name == 'description': self.data.description = content
            elif name == 'robots': self.data.robots = content
            elif prop == 'og:url': self.data.canonical = content
        elif tag == 'link':
            rel = values.get('rel', '')
            href = values.get('href', '')
            if rel == 'canonical': self.data.canonical = href
            elif href.startswith('/') and not href.startswith('//'):
                target = urlparse(href).path
                if re.search(r'\.(css|png|ico|svg|webmanifest|json|txt|xml)$', target):
                    self.data.asset_links.add(target)
                elif not target.startswith('/#'):
                    self.data.internal_links.add(target)
        elif tag == 'h1': self.data.h1_count += 1
        elif tag == 'main': self.data.main_count += 1
        elif tag == 'script':
            self.data.scripts.append(values.get('src', ''))
            if values.get('type') == 'application/ld+json':
                self.in_ld = True
                self.ld_type = values.get('type')
        elif tag == 'form': self.data.forms.append(values.get('action', ''))

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.data.title += data
        if self.in_ld:
            self.ld_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == 'title': self.in_title = False
        if tag == 'script' and self.in_ld:
            self.in_ld = False
            try:
                parsed = json.loads(''.join(self.ld_chunks))
            except json.JSONDecodeError as exc:
                raise AssertionError(f'Invalid JSON-LD in {self.data.path}: {exc}') from exc
            self.data.json_ld.append(parsed)
            self.ld_chunks = []


def public_path(file: Path) -> str:
    relative = file.relative_to(DIST).as_posix()
    if relative == 'index.html': return '/'
    if relative == '404.html': return '/404.html'
    if relative.endswith('/index.html'):
        return '/' + relative[:-len('/index.html')] + '/'
    return '/' + relative


def target_exists(path: str) -> bool:
    clean = urlparse(path).path
    if clean in ('', '/'): return (DIST / 'index.html').is_file()
    if clean.endswith('/'):
        return (DIST / clean.lstrip('/') / 'index.html').is_file()
    return (DIST / clean.lstrip('/')).is_file()


def main() -> int:
    if not DIST.is_dir():
        raise SystemExit('dist/ does not exist')

    pages: list[PageData] = []
    for file in sorted(DIST.rglob('*.html')):
        data = PageData(path=public_path(file), file=file)
        parser = HtmlAuditParser(data)
        parser.feed(file.read_text(encoding='utf-8'))
        pages.append(data)

    if not pages: raise AssertionError('No generated HTML pages')
    page_by_path = {page.path: page for page in pages}
    if len(page_by_path) != len(pages): raise AssertionError('Duplicate generated page path')

    indexable: set[str] = set()
    for page in pages:
        if page.path in ('/404.html', '/contact/thanks/') or 'noindex' in page.robots.lower():
            continue
        indexable.add(page.path)
        assert page.title, f'Missing title: {page.path}'
        assert 30 <= len(page.description) <= 170, f'Bad description length: {page.path}: {len(page.description)}'
        assert page.h1_count == 1, f'Expected one H1, got {page.h1_count}: {page.path}'
        assert page.main_count == 1, f'Expected one main, got {page.main_count}: {page.path}'
        assert page.canonical == BASE + page.path, f'Bad canonical: {page.path}: {page.canonical}'
        assert page.json_ld, f'Missing JSON-LD: {page.path}'
        graph = page.json_ld[0].get('@graph') if isinstance(page.json_ld[0], dict) else None
        assert graph, f'Missing JSON-LD graph: {page.path}'
        assert page.robots, f'Missing robots meta: {page.path}'

        for link in sorted(page.internal_links):
            assert target_exists(link), f'Broken internal link {link} on {page.path}'
        for asset in sorted(page.asset_links):
            assert target_exists(asset), f'Broken asset link {asset} on {page.path}'
        for src in page.scripts:
            assert not src, f'Unexpected external script on {page.path}: {src}'

    contact = page_by_path.get('/contact/')
    assert contact and any(action.startswith('https://formsubmit.co/') for action in contact.forms), 'Contact form route changed'
    contact_text = contact.file.read_text(encoding='utf-8')
    assert 'name="_next" value="https://main.direct/contact/thanks/"' in contact_text, 'Form thank-you redirect changed'

    sitemap_root = ET.parse(DIST / 'sitemap.xml').getroot()
    sitemap_urls = {node.text for node in sitemap_root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
    assert sitemap_urls == {BASE + path for path in indexable}, f'Sitemap mismatch: {sitemap_urls ^ {BASE + path for path in indexable}}'

    rss_root = ET.parse(DIST / 'rss.xml').getroot()
    rss_links = {node.text for node in rss_root.findall('.//link') if node.text and node.text.startswith(BASE)}
    assert BASE + '/' in rss_links
    assert all(target_exists(url.removeprefix(BASE)) for url in rss_links if url != BASE + '/'), 'RSS contains a broken link'

    llms = (DIST / 'llms.txt').read_text(encoding='utf-8')
    for path in indexable:
        assert BASE + path in llms, f'llms.txt missing canonical page: {path}'
    assert 'does not guarantee inbox placement' in llms

    prompts = json.loads((DIST / 'ai/prompts.json').read_text(encoding='utf-8'))
    assert prompts['canonicalUrl'] == BASE + '/'
    assert len(prompts['citationTargets']) >= 7
    assert prompts['requiredCaveats']

    for required in ['CNAME', '.nojekyll', 'robots.txt', 'favicon.svg', 'apple-touch-icon.png', 'og.png', 'site.webmanifest']:
        assert (DIST / required).is_file(), f'Missing deploy asset: {required}'

    print(f'Verified {len(pages)} HTML pages, {len(indexable)} indexable routes, {len(sitemap_urls)} sitemap URLs, {len(rss_links)} RSS routes.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (AssertionError, ET.ParseError, json.JSONDecodeError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
