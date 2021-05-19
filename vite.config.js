import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default ({ mode }) => {
  return defineConfig({
    plugins: [vue()],
    base: loadEnv(mode, process.cwd()).VITE_BASE, //發佈對應路徑
    assetsDir: 'assets',
  })
}
