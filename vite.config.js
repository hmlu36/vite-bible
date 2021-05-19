import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/WeddingForm/', //發佈對應路徑
  assetsDir: 'assets',
})
