// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({});

import netlify from '@astrojs/netlify';

export default defineConfig({
  output: 'static',
  adapter: netlify()
});
