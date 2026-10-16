import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import astro from 'eslint-plugin-astro';

export default [
  { ignores: ['dist/', '.astro/', '.wrangler/', 'docs/', 'node_modules/'] },
  js.configs.recommended,
  ...tseslint.configs.recommended,
  ...astro.configs.recommended,
  {
    files: ['scripts/**/*.mjs'],
    languageOptions: { globals: { process: 'readonly', console: 'readonly', URL: 'readonly' } },
  },
  {
    // Chrome extension (tools/flow-prompt-queue): browser + extension globals, plain JS.
    files: ['tools/flow-prompt-queue/**/*.{js,mjs}'],
    languageOptions: {
      globals: {
        chrome: 'readonly',
        globalThis: 'readonly',
        window: 'readonly',
        document: 'readonly',
        location: 'readonly',
        console: 'readonly',
        setTimeout: 'readonly',
        clearTimeout: 'readonly',
        setInterval: 'readonly',
        clearInterval: 'readonly',
        getComputedStyle: 'readonly',
        fetch: 'readonly',
        FileReader: 'readonly',
        DataTransfer: 'readonly',
        ClipboardEvent: 'readonly',
        InputEvent: 'readonly',
        KeyboardEvent: 'readonly',
        MouseEvent: 'readonly',
        PointerEvent: 'readonly',
        MutationObserver: 'readonly',
        Event: 'readonly',
      },
    },
  },
];
