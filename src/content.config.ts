import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const seo = z.object({ title: z.string().max(60), description: z.string().max(155) });
const faq = z.object({ q: z.string(), a: z.string() });

const programs = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/programs' }),
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    shortName: z.string(),
    level: z.enum(['foundation', 'specialisation']),
    durationYears: z.number(),
    totalHours: z.number(),
    hoursPerWeek: z.number(),
    entry: z.string(),
    summary: z.string().max(200),
    answer: z.string().min(150).max(420), // answer-first paragraph for AEO
    audience: z.array(z.enum(['school', 'college', 'professional', 'parent', 'institution'])),
    years: z
      .array(
        z.object({ title: z.string(), hours: z.number().optional(), modules: z.array(z.string()) }),
      )
      .min(1),
    assessment: z.string(),
    certifications: z.array(z.string()).default([]), // external; named only as in the owner's document
    tools: z.array(z.string()).default([]),
    projects: z.array(z.string()).default([]),
    careerRoles: z.array(z.string()).default([]), // only roles the curriculum document lists
    hardware: z.array(z.string()).default([]),
    faqs: z.array(faq).min(4),
    related: z.array(z.string()).default([]),
    keywords: z.object({ primary: z.string(), secondary: z.array(z.string()) }),
    seo,
  }),
});

const posts = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/posts' }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      description: z.string().max(155),
      pubDate: z.coerce.date(),
      updatedDate: z.coerce.date().optional(),
      author: z.string(),
      category: z.enum(['guides', 'careers', 'schools', 'parents', 'professionals']),
      cover: image().optional(),
      coverAlt: z.string().optional(),
      tldr: z.string().max(320),
      primaryKeyword: z.string(),
      faqs: z.array(faq).default([]),
      related: z.array(z.string()).default([]),
      draft: z.boolean().default(false),
    }),
});

const faqs = defineCollection({
  loader: glob({ pattern: '**/*.yaml', base: './src/content/faqs' }),
  schema: z.object({ q: z.string(), a: z.string(), group: z.string() }),
});

const audiences = defineCollection({
  loader: glob({ pattern: '**/*.mdx', base: './src/content/audiences' }),
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    answer: z.string(),
    seo,
    programs: z.array(z.string()),
  }),
});

export const collections = { programs, posts, faqs, audiences };
