import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE_URL } from '../data/site';

const escapeXml = (value: string) => value
  .replaceAll('&', '&amp;')
  .replaceAll('<', '&lt;')
  .replaceAll('>', '&gt;')
  .replaceAll('"', '&quot;');

export const GET: APIRoute = async () => {
  const pages = (await getCollection('pages'))
    .filter((entry) => !entry.data.robots.includes('noindex') && entry.data.path !== '/404.html')
    .sort((a, b) => a.data.path.localeCompare(b.data.path));
  const order = ['/', '/services/', '/signal-atlas/', '/contact-supply/', '/deliverability-engine/'];
  pages.sort((a, b) => {
    const ao = order.indexOf(a.data.path);
    const bo = order.indexOf(b.data.path);
    return (ao === -1 ? 99 : ao) - (bo === -1 ? 99 : bo) || a.data.path.localeCompare(b.data.path);
  });

  const urls = pages.map((entry) => `  <url><loc>${escapeXml(`${SITE_URL}${entry.data.path}`)}</loc><lastmod>${entry.data.dateModified}</lastmod></url>`);
  const body = `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls.join('\n')}\n</urlset>\n`;
  return new Response(body, { headers: { 'Content-Type': 'application/xml; charset=utf-8' } });
};
