import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';

export default defineConfig({
  site: 'https://main.direct',
  trailingSlash: 'ignore',
  output: 'static',
  integrations: [mdx()],
  build: {
    format: 'directory',
    inlineStylesheets: 'auto'
  }
});
