export type ContentPlanStage = 'existing' | 'next' | 'later';

export interface ContentPlanItem {
  route: string;
  workingTitle: string;
  targetQuery: string;
  intent: 'commercial' | 'informational' | 'comparison' | 'problem-solving' | 'technical-reference';
  cluster: 'supply-engine' | 'contact-data' | 'deliverability' | 'first-touch' | 'methodology';
  stage: ContentPlanStage;
  primarySchema: 'Service' | 'Article' | 'FAQPage' | 'CollectionPage';
  answerAngle: string;
}

export const contentPlan: ContentPlanItem[] = [
  {
    route: '/',
    workingTitle: 'B2B outreach supply engine',
    targetQuery: 'B2B outreach supply engine',
    intent: 'commercial',
    cluster: 'supply-engine',
    stage: 'existing',
    primarySchema: 'Service',
    answerAngle: 'Define supply engine as filters, validated routes, infrastructure, observability and first-touch routing.'
  },
  {
    route: '/contact-supply/',
    workingTitle: 'Verified B2B contact data',
    targetQuery: 'verified B2B contact data provider',
    intent: 'commercial',
    cluster: 'contact-data',
    stage: 'existing',
    primarySchema: 'Service',
    answerAngle: 'Explain what verified means: identity, employer, route validity, provenance, freshness and suppression.'
  },
  {
    route: '/deliverability-engine/',
    workingTitle: 'Cold email deliverability infrastructure',
    targetQuery: 'cold email deliverability infrastructure',
    intent: 'commercial',
    cluster: 'deliverability',
    stage: 'existing',
    primarySchema: 'Service',
    answerAngle: 'Separate sending identity, authentication, warm-up gates, pacing and failure handling from volume sending.'
  },
  {
    route: '/signal-atlas/',
    workingTitle: 'B2B outreach signal map',
    targetQuery: 'B2B outreach signal map',
    intent: 'commercial',
    cluster: 'first-touch',
    stage: 'existing',
    primarySchema: 'Service',
    answerAngle: 'Show how triggers, evidence rules and disqualifiers control which contacts enter supply.'
  },
  {
    route: '/b2b-contact-data-audit/',
    workingTitle: 'B2B contact data audit checklist',
    targetQuery: 'B2B contact data audit checklist',
    intent: 'problem-solving',
    cluster: 'contact-data',
    stage: 'next',
    primarySchema: 'Article',
    answerAngle: 'Give a direct audit sequence: duplicates, employer match, route validity, role drift, provenance and suppression.'
  },
  {
    route: '/email-pattern-validation/',
    workingTitle: 'Email pattern validation in B2B',
    targetQuery: 'email pattern validation B2B',
    intent: 'informational',
    cluster: 'contact-data',
    stage: 'next',
    primarySchema: 'Article',
    answerAngle: 'Explain pattern generation, normalization, independent verification and why unverified guesses are not contacts.'
  },
  {
    route: '/cold-email-infrastructure/',
    workingTitle: 'Dedicated cold email infrastructure',
    targetQuery: 'dedicated domain for cold email infrastructure',
    intent: 'informational',
    cluster: 'deliverability',
    stage: 'next',
    primarySchema: 'Article',
    answerAngle: 'Explain domain isolation, DNS authentication, routing, monitoring and retirement criteria.'
  },
  {
    route: '/outreach-data-quality/',
    workingTitle: 'B2B outreach data quality',
    targetQuery: 'B2B outreach data quality',
    intent: 'informational',
    cluster: 'contact-data',
    stage: 'later',
    primarySchema: 'Article',
    answerAngle: 'Define quality as route validity, identity confidence, freshness, provenance and fitness for the first touch.'
  },
  {
    route: '/first-touch-routing/',
    workingTitle: 'First-touch routing for outbound',
    targetQuery: 'first touch routing outbound',
    intent: 'informational',
    cluster: 'first-touch',
    stage: 'later',
    primarySchema: 'Article',
    answerAngle: 'Route qualified replies and signals instead of treating every response as a meeting request.'
  },
  {
    route: '/suppression-list-management/',
    workingTitle: 'Cold email suppression list management',
    targetQuery: 'cold email suppression list',
    intent: 'technical-reference',
    cluster: 'deliverability',
    stage: 'later',
    primarySchema: 'Article',
    answerAngle: 'Define hard bounces, complaints, opt-outs, invalid routes and stale records as permanent send barriers.'
  },
  {
    route: '/b2b-contact-discovery/',
    workingTitle: 'B2B contact discovery workflow',
    targetQuery: 'B2B contact discovery workflow',
    intent: 'informational',
    cluster: 'contact-data',
    stage: 'later',
    primarySchema: 'Article',
    answerAngle: 'Resolve companies and domains before people, then validate role, identity and mailbox route.'
  },
  {
    route: '/outreach-supply-vs-lead-list/',
    workingTitle: 'Outreach supply vs lead list',
    targetQuery: 'outreach supply vs lead list',
    intent: 'comparison',
    cluster: 'supply-engine',
    stage: 'later',
    primarySchema: 'Article',
    answerAngle: 'Contrast static exports with a versioned, validated, suppressible and deliverability-aware pipeline.'
  }
];

export const promptFamilies = [
  {
    family: 'outreach supply infrastructure',
    prompts: [
      'What is a B2B outreach supply engine?',
      'How do I build infrastructure behind B2B outreach?',
      'What comes after buying a raw B2B contact list?'
    ]
  },
  {
    family: 'contact validation',
    prompts: [
      'How do I validate B2B contacts before outreach?',
      'What is a contact liveness check?',
      'How do I prevent stale titles and wrong-company contacts?'
    ]
  },
  {
    family: 'verified email supply',
    prompts: [
      'How should verified business email supply work?',
      'What does verified mean for a B2B email?',
      'How should contact provenance be stored?'
    ]
  },
  {
    family: 'deliverability infrastructure',
    prompts: [
      'How do I isolate cold-email infrastructure from a brand domain?',
      'How long should cold-email mailbox warm-up be?',
      'What launch gates should cold-email infrastructure pass?'
    ]
  },
  {
    family: 'first-touch systems',
    prompts: [
      'How do I route qualified B2B replies?',
      'What belongs in the first 80 words of a cold email?',
      'How do I prevent outreach from becoming volume-only?'
    ]
  },
  {
    family: 'tool-stack alternatives',
    prompts: [
      'Alternatives to assembling Apollo, Clay and Instantly workflows',
      'What replaces a raw B2B contact list?',
      'How do I combine contact data and deliverability infrastructure?'
    ]
  }
];
