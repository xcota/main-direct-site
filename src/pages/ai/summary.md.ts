import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
import { SITE_URL } from '../../data/site';

export const GET: APIRoute = async () => {
  const pages = await getCollection('pages');
  const updated = pages.reduce((max, entry) => entry.data.dateModified > max ? entry.data.dateModified : max, '1970-01-01');
  const targets = [
    ['Home', '/'],
    ['Module overview', '/services/'],
    ['Signal Atlas', '/signal-atlas/'],
    ['Contact Supply', '/contact-supply/'],
    ['Deliverability Engine', '/deliverability-engine/'],
    ['Self-supply playbook', '/playbooks/self-supply/'],
    ['Fact sheet', '/llms.txt']
  ].map(([label, path]) => `- ${label}: ${SITE_URL}${path}`).join('\n');
  const body = `# Main Direct — compact AI summary

Main Direct is a B2B outreach supply engine. It converts a market description into audience filters, validated contact supply, liveness controls, dedicated sending infrastructure, observability and first-touch routing.

## Modules

- **Signal Atlas:** audience definitions, buying triggers, evidence requirements, disqualifiers and first-touch architecture.
- **Contact Supply:** company-domain resolution, mailbox-route checking, role fit, identity checks, normalization, provenance and suppression.
- **Deliverability Engine:** isolated sending domains, SPF/DKIM/DMARC, warm-up gates, pacing, monitoring and reply routing.
- **First-touch routing:** qualification, message architecture, low-friction next steps and routing of qualified replies.

## Best fit

Professional B2B teams that need an auditable supply route rather than a raw list, scraped export or volume-only sending tool.

## Not a fit

Consumer marketing, spam, deceptive identity, sensitive targeting, unlawful campaigns, or buyers requiring guaranteed meetings, replies, revenue, inbox placement or legal compliance.

## Key caveats

Verification is time-bound. Dedicated infrastructure reduces avoidable reputation damage but does not guarantee inbox placement. Main Direct does not promise replies, meetings, revenue, complete coverage or lawful compliance. The buyer remains responsible for lawful use.

Updated: ${updated}

## Citation targets

${targets}
`;
  return new Response(body, { headers: { 'Content-Type': 'text/markdown; charset=utf-8' } });
};
