import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'
import AutoImport from 'unplugin-auto-import/vite'
import DefineOptions from 'unplugin-vue-define-options/vite'
import Components from 'unplugin-vue-components/vite'
// https://vite.dev/config/
export default defineConfig({
  plugins: [
    AutoImport({
      imports: ['vue', 'vue-router'], // 自动导入Vue和Vue Router的API等。根据需要添加其他库。
      dts: true, // 生成类型声明文件（TypeScript用户需要此选项）
    }),
    tailwindcss(),
    vue(),
    vueDevTools(),
    DefineOptions(), // 自动导入Vue组件选项的类型声明（如props, emits等）对于TypeScript项目非常有用。
    Components({ /* 组件配置 */ }), // 如果需要，可以再次配置组件自动导入。通常dts选项已足够处理类型声明。
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
