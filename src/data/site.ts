export const SITE_URL = 'https://main.direct';
export const SITE_NAME = 'Main Direct';
export const SITE_DESCRIPTION =
  'Main Direct is a B2B outreach supply engine: audience filters, verified contact supply, liveness controls, dedicated deliverability infrastructure and first-touch routing.';
export const DEFAULT_DATE_MODIFIED = '2026-10-16';
export const FOUNDER_LINKEDIN = 'https://www.linkedin.com/in/xcota/';
export const GITHUB = 'https://github.com/xcota/main-direct-site';

export const NAV_ITEMS = [
  { href: '/', label: 'Home', key: 'home' },
  { href: '/services/', label: 'Modules', key: 'services' },
  { href: '/signal-atlas/', label: 'Signal Atlas', key: 'signal' },
  { href: '/contact-supply/', label: 'Contact Supply', key: 'supply' },
  { href: '/deliverability-engine/', label: 'Deliverability', key: 'engine' },
  { href: '/playbooks/contact-to-inbox/', label: 'Playbook', key: 'playbook' },
  { href: '/contact/', label: 'Contact', key: 'contact' }
] as const;

export type NavKey = 'home' | 'services' | 'signal' | 'supply' | 'engine' | 'playbook' | 'about' | 'contact' | 'none';

export function absoluteUrl(path: string): string {
  return `${SITE_URL}${path === '/' ? '/' : path}`;
}
