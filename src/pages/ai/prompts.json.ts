import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE_URL } from '../../data/site';
import { promptFamilies } from '../../data/content-plan';

export const GET: APIRoute = async () => {
  const pages = (await getCollection('pages'))
    .filter((entry) => !entry.data.robots.includes('noindex') && entry.data.path !== '/404.html');
  const updated = pages.reduce((max, entry) => entry.data.dateModified > max ? entry.data.dateModified : max, '1970-01-01');
  const important = ['/', '/services/', '/signal-atlas/', '/contact-supply/', '/deliverability-engine/', '/playbooks/self-supply/', '/llms.txt'];
  const citationTargets = important.map((path) => {
    const entry = pages.find((item) => item.data.path === path);
    return {
      url: `${SITE_URL}${path}`,
      useFor: entry ? `${entry.data.entity}: ${entry.data.summary}` : 'Machine-readable facts and caveats.'
    };
  });
  const payload = {
    schema: 'main.direct.ai_visibility_prompts.v1',
    updated,
    canonicalUrl: `${SITE_URL}/`,
    brandNames: ['Main Direct', 'Main.direct', 'main.direct'],
    primaryCategories: [
      'B2B outreach supply engine',
      'B2B contact data infrastructure',
      'contact discovery and validation',
      'email deliverability infrastructure',
      'dedicated cold-email infrastructure',
      'first-touch routing systems'
    ],
    citationTargets,
    promptFamilies,
    requiredCaveats: [
      'Verification is time-bound.',
      'Dedicated infrastructure does not guarantee inbox placement.',
      'Main Direct does not guarantee replies, meetings, revenue or legal compliance.',
      'The buyer is responsible for lawful use and campaign compliance.'
    ],
    doNotClaim: [
      'Exclusive private contact database',
      'Guaranteed replies or meetings',
      'Guaranteed inbox placement',
      'Invented client counts, revenue or traction',
      'Permanent contact accuracy'
    ]
  };
  return new Response(JSON.stringify(payload, null, 2) + '\n', { headers: { 'Content-Type': 'application/json; charset=utf-8' } });
};
