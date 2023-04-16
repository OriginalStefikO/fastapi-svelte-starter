import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
   plugins: [svelte()],
   base: "./",
   build: {
      emptyOutDir: true,
      outDir: '../public',
      assetsDir: 'assets',
      rollupOptions: {
         input: {
            main: './index.html'
         },
         output: {
            entryFileNames: 'assets/js/[name]-[hash].js',
            chunkFileNames: 'assets/js/[name]-[hash].js',
            assetFileNames: ({ name }) => {
               if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')) {
                  return 'assets/images/[name].[ext]';
               }

               if (/\.css$/.test(name ?? '')) {
                  return 'assets/css/[name]-[hash].[ext]';
               }

               return 'assets/[name]-[hash].[ext]';
            },
         }
      }     
   }
})
