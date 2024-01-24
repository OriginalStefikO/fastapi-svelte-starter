import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	preprocess: vitePreprocess(),

	kit: {
		// We are using adapter-static for static site generation (SSG) 
		// See https://kit.svelte.dev/docs/adapters for more information about adapters.
		adapter: adapter({
			// pages needs to be separated from assets, otherwise the assets will be copied to the public folder
			// pages needs to be in their own folder and be index.html otherwise FastAPI won't serve them
				// Look to "src/routes/+layout.ts" to see how it's done 
			pages: '../public/', // Build output directory
			assets: '../public',
			fallback: undefined,
			precompress: false,
			strict: true,
		}),
		appDir: 'assets', // The assets folder is where the static files will be located
		paths: {
			relative: false,
		}
	},
};

export default config;
