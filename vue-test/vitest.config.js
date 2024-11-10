import { fileURLToPath } from 'node:url'
import { mergeConfig, defineConfig, configDefaults } from 'vitest/config'
import viteConfig from './vite.config'
import { VitestMarkdownReporter } from "vitest-markdown-reporter";

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      environment: 'jsdom',
      exclude: [...configDefaults.exclude, 'e2e/**'],
      root: fileURLToPath(new URL('./', import.meta.url)),
      reporters: ["default", new VitestMarkdownReporter()],
      outputFile: {
        markdown: "test-report.md",
      },
    },
  }),
)
