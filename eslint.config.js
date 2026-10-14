import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import astro from 'eslint-plugin-astro';

export default [
  { ignores: ['dist/', '.astro/', '.wrangler/', 'node_modules/', 'docs/'] },
  {
    files: ['scripts/**/*.mjs', '*.config.*'],
    languageOptions: {
      globals: {
        console: 'readonly',
        process: 'readonly',
        URL: 'readonly',
        fetch: 'readonly',
        globalThis: 'readonly',
      },
    },
  },
  {
    // Rule from CLAUDE.md: only src/scripts/motion may import gsap, lenis or three.
    files: ['src/**/*.{ts,astro}'],
    ignores: ['src/scripts/motion/**'],
    rules: {
      'no-restricted-imports': [
        'error',
        { patterns: ['gsap', 'gsap/*', 'lenis', 'three', 'three/*'] },
      ],
    },
  },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...astro.configs.recommended,
];
