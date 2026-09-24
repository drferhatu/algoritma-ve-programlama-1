// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import mdx from '@astrojs/mdx';
import tailwindcss from '@tailwindcss/vite';
import remarkCallouts from './src/lib/remark-callouts.mjs';
import rehypeBaseLinks from './src/lib/rehype-base-links.mjs';

// GitHub Pages: https://<kullanıcı>.github.io/<depo>/
// Özel alan adına geçilirse SITE_URL ve BASE_PATH ortam değişkenleriyle değiştirilebilir.
const site = process.env.SITE_URL ?? 'https://drferhatu.github.io';
const base = process.env.BASE_PATH ?? '/algoritma-ve-programlama-1';

export default defineConfig({
  site,
  base,
  trailingSlash: 'ignore',
  integrations: [mdx(), sitemap()],
  markdown: {
    remarkPlugins: [remarkCallouts],
    rehypePlugins: [[rehypeBaseLinks, { base }]],
    shikiConfig: { theme: 'github-light', wrap: true },
  },
  // Tailwind kendi vite tipini getirir; Astro paketindeki vite sürümüyle tip uyuşmazlığı yalnızca tip düzeyindedir.
  vite: { plugins: [/** @type {any} */ (tailwindcss())] },
});
