import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const env = process.env.NODE_ENV || "development";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: env == 'production' ? '/vite-bible/' : '/', //發佈對應路徑
  assetsDir: 'assets',
})
