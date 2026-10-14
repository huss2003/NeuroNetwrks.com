// Single source of truth for entity data. Unknowns stay as {{CONFIRM}} until the owner confirms them;
// the production build fails while any placeholder is left in dist/ (scripts/check-confirm.mjs).
export const site = {
  name: 'NeuroNetworks AI Ed',
  alternateNames: ['NeuroNetworks', 'Neuronetworks', 'neuronetwrks'],
  url: 'https://neuronetwrks.com',
  tagline: 'Learn · Develop · Create',
  locale: 'en-IN',
  noticeVersion: '2026-10-v1',
  contact: {
    email: '{{CONFIRM: public contact email}}',
    phone: '{{CONFIRM: public phone, optional}}',
    address: '{{CONFIRM: postal address}}',
  },
  grievanceOfficer: {
    name: '{{CONFIRM: grievance officer name}}',
    email: '{{CONFIRM: grievance officer email}}',
  },
  social: {
    linkedin: '{{CONFIRM: LinkedIn URL}}',
    youtube: '{{CONFIRM: YouTube URL}}',
    instagram: '{{CONFIRM: Instagram URL}}',
  },
} as const;
