import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE_NAME, SITE_URL } from '../data/site';

const escapeXml = (value: string) => value
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;');

export const GET: APIRoute = async () => {
  const articles = (await getCollection('pages'))
    .filter((entry) => entry.data.pageType === 'ArticlePage')
    .sort((a, b) => (b.data.datePublished ?? b.data.dateModified).localeCompare(a.data.datePublished ?? a.data.dateModified));
  const updated = articles.reduce((max, entry) => entry.data.dateModified > max ? entry.data.dateModified : max, '1970-01-01');
  const items = articles.map((entry) => {
    const link = `${SITE_URL}${entry.data.path}`;
    const pubDate = new Date(`${entry.data.datePublished ?? entry.data.dateModified}T00:00:00Z`).toUTCString();
    return `    <item>\n      <title>${escapeXml(entry.data.article?.headline ?? entry.data.title)}</title>\n      <link>${escapeXml(link)}</link>\n      <guid isPermaLink="true">${escapeXml(link)}</guid>\n      <pubDate>${pubDate}</pubDate>\n      <description>${escapeXml(entry.data.article?.description ?? entry.data.description)}</description>\n    </item>`;
  }).join('\n');
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n    <title>${SITE_NAME} playbooks</title>\n    <link>${SITE_URL}/</link>\n    <description>Infrastructure-first B2B contact supply and email deliverability playbooks.</description>\n    <language>en</language>\n    <lastBuildDate>${new Date(`${updated}T00:00:00Z`).toUTCString()}</lastBuildDate>\n    <atom:link href="${SITE_URL}/rss.xml" rel="self" type="application/rss+xml"/>\n${items}\n  </channel>\n</rss>\n`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
