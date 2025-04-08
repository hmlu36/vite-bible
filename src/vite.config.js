import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: import.meta.env.MODE === 'production' ? '/vite-bible/' : '/', 
  plugins: [vue()]
})