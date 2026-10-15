import { defineCollection } from 'astro:content';
import { z } from 'astro/zod';
import { glob } from 'astro/loaders';

const linkSchema = z.object({
  anchor: z.string().min(3),
  url: z.string().startsWith('/')
});

const faqSchema = z.object({
  question: z.string().min(10),
  answer: z.string().min(50)
});

const serviceSchema = z.object({
  name: z.string().min(3),
  serviceType: z.string().min(3),
  description: z.string().min(50),
  path: z.string().startsWith('/')
});

const pageSchema = z.object({
  title: z.string().min(10),
  description: z.string().min(30).max(170),
  path: z.string().regex(/^\/(?:.*\/)?$/, { message: 'Path must be root or slash-ending.' }).or(z.literal('/404.html')),
  targetQuery: z.string().min(8),
  entity: z.string().min(8),
  intent: z.enum([
    'brand',
    'informational',
    'commercial',
    'transactional',
    'comparison',
    'problem-solving',
    'technical-reference'
  ]),
  answer: z.string().min(50),
  summary: z.string().min(35),
  pageType: z.enum([
    'WebPage',
    'AboutPage',
    'ContactPage',
    'CollectionPage',
    'ServicePage',
    'ArticlePage',
    'FAQPage'
  ]),
  dateModified: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
  datePublished: z.string().regex(/^\d{4}-\d{2}-\d{2}$/).optional(),
  robots: z.string().default('index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1'),
  includeCta: z.boolean().default(true),
  navCurrent: z.enum(['home', 'services', 'signal', 'supply', 'engine', 'playbook', 'about', 'contact']).default('home'),
  breadcrumbs: z.array(linkSchema).min(1),
  internalLinks: z.array(linkSchema).default([]),
  keywords: z.array(z.string()).default([]),
  services: z.array(serviceSchema).default([]),
  faq: z.array(faqSchema).default([]),
  article: z.object({
    headline: z.string().min(10),
    alternativeHeadline: z.string().optional(),
    description: z.string().min(70),
    wordCount: z.number().int().positive().optional(),
    articleSection: z.array(z.string()).default([])
  }).optional()
}).superRefine((value, ctx) => {
  if (!value.robots.includes('noindex')) {
  if (value.description.length < 70) ctx.addIssue({ code: 'custom', path: ['description'], message: 'Indexable pages need a description of at least 70 characters.' });
  if (value.answer.length < 80) ctx.addIssue({ code: 'custom', path: ['answer'], message: 'Indexable pages need a direct answer of at least 80 characters.' });
  if (value.summary.length < 80) ctx.addIssue({ code: 'custom', path: ['summary'], message: 'Indexable pages need an AI summary of at least 80 characters.' });
 }
 if (!value.robots.includes('noindex') && value.internalLinks.length < 3) {
    ctx.addIssue({
      code: 'custom',
      path: ['internalLinks'],
      message: 'Indexable pages need at least three internal links.'
    });
  }
  if (value.pageType === 'FAQPage' && value.faq.length < 3) {
    ctx.addIssue({
      code: 'custom',
      path: ['faq'],
      message: 'FAQ pages need at least three visible questions.'
    });
  }
  if (value.pageType === 'ArticlePage' && !value.article) {
    ctx.addIssue({
      code: 'custom',
      path: ['article'],
      message: 'Article pages need Article metadata.'
    });
  }
});

export const collections = { pages: defineCollection({ loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/pages' }), schema: pageSchema }) };
