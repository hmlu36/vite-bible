import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'

const env = process.env.NODE_ENV || "development";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), VitePWA()],
  base: env == 'production' ? '/vite-bible/' : '/', //發佈對應路徑
  assetsDir: 'assets',
})
