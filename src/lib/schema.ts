// JSON-LD builders. Placeholders ({{CONFIRM}}) are dropped, never emitted. No `offers`: the site shows no prices.
import { site } from '../data/site';
import { abs, isPlaceholder } from './seo';

type Node = Record<string, unknown>;
const ids = { org: `${site.url}/#organization`, website: `${site.url}/#website` };

export const graph = (...nodes: Node[]) => ({ '@context': 'https://schema.org', '@graph': nodes });

export function organization(): Node {
  const sameAs = Object.values(site.social).filter((u) => !isPlaceholder(u));
  return {
    '@type': ['Organization', 'EducationalOrganization'],
    '@id': ids.org,
    name: site.name,
    alternateName: site.alternateNames,
    url: site.url,
    slogan: site.tagline,
    logo: { '@type': 'ImageObject', url: abs('/icon-512.png'), width: 512, height: 512 },
    areaServed: { '@type': 'Country', name: 'India' },
    ...(sameAs.length ? { sameAs } : {}),
    ...(isPlaceholder(site.contact.email)
      ? {}
      : {
          contactPoint: {
            '@type': 'ContactPoint',
            contactType: 'admissions',
            email: site.contact.email,
            areaServed: 'IN',
            availableLanguage: 'en',
          },
        }),
  };
}

export const website = (): Node => ({
  '@type': 'WebSite',
  '@id': ids.website,
  url: site.url,
  name: site.name,
  inLanguage: site.locale,
  publisher: { '@id': ids.org },
});

const providerRef = (): Node => ({
  '@type': 'EducationalOrganization',
  '@id': ids.org,
  name: site.name,
  url: site.url,
});

export function webPage(path: string, name: string, description: string, type = 'WebPage'): Node {
  return {
    '@type': type,
    '@id': `${abs(path)}#webpage`,
    url: abs(path),
    name,
    description,
    inLanguage: site.locale,
    isPartOf: { '@id': ids.website },
    about: { '@id': ids.org },
  };
}

interface ProgramLike {
  name: string;
  slug: string;
  answer: string;
  durationYears: number;
  totalHours: number;
  entry: string;
}

export function course(p: ProgramLike): Node {
  const url = abs(`/programs/${p.slug}`);
  return {
    '@type': 'Course',
    '@id': `${url}#course`,
    name: p.name,
    description: p.answer,
    url,
    inLanguage: site.locale,
    provider: providerRef(),
    timeRequired: `PT${p.totalHours}H`,
    coursePrerequisites: p.entry,
    hasCourseInstance: { '@type': 'CourseInstance', courseWorkload: `PT${p.totalHours}H` },
  };
}

export function educationalProgram(p: ProgramLike): Node {
  const url = abs(`/programs/${p.slug}`);
  return {
    '@type': 'EducationalOccupationalProgram',
    '@id': `${url}#program`,
    name: p.name,
    description: p.answer,
    url,
    provider: providerRef(),
    timeToComplete: `P${p.durationYears}Y`,
    programPrerequisites: p.entry,
    hasCourse: { '@id': `${url}#course` },
  };
}

export function itemList(items: { name: string; path: string }[]): Node {
  return {
    '@type': 'ItemList',
    itemListElement: items.map((it, i) => ({
      '@type': 'ListItem',
      position: i + 1,
      name: it.name,
      url: abs(it.path),
    })),
  };
}

export function blogPosting(p: {
  title: string;
  description: string;
  path: string;
  author: string;
  pubDate: Date;
  updatedDate?: Date;
}): Node {
  return {
    '@type': 'BlogPosting',
    '@id': `${abs(p.path)}#article`,
    headline: p.title,
    description: p.description,
    url: abs(p.path),
    inLanguage: site.locale,
    author: { '@type': 'Person', name: p.author },
    publisher: { '@id': ids.org },
    datePublished: p.pubDate.toISOString(),
    dateModified: (p.updatedDate ?? p.pubDate).toISOString(),
    isPartOf: { '@id': ids.website },
  };
}
