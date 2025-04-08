import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/vite-bible/',  // 設定 Base URL
  plugins: [vue()]
})
