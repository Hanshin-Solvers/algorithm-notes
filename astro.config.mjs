import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeFigures from './src/lib/rehype-figures.mjs';
import { createHash } from 'node:crypto';
import { readFileSync, readdirSync } from 'node:fs';

// Inline SVG content is part of Markdown's cache key.
const diagramDir = new URL('./src/assets/diagrams/', import.meta.url);
const diagramDigest = createHash('sha256');
for (const name of readdirSync(diagramDir).filter(name => name.endsWith('.svg')).sort()) {
  diagramDigest.update(name).update(readFileSync(new URL(name, diagramDir)));
}

export default defineConfig({
  site: 'https://hanshin-solvers.github.io',
  base: '/algorithm-notes',
  trailingSlash: 'always',
  output: 'static',
  markdown: {
    processor: unified({
      remarkPlugins: [remarkMath],
      rehypePlugins: [[rehypeKatex, { strict: 'error', throwOnError: true }], [rehypeFigures, { diagramDigest: diagramDigest.digest('hex') }]],
      shikiConfig: { theme: 'github-light' },
    }),
  },
});
