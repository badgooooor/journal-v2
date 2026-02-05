export default defineNuxtConfig({
  compatibilityDate: "2026-01-25",
  devtools: { enabled: true },
  modules: [
    "@nuxt/ui",
    "nuxt-icon",
    "@nuxt/fonts",
    "@nuxt/image",
    "@nuxt/content",
    "@nuxthq/studio",
    "@vueuse/nuxt",
    "@nuxtjs/i18n",
    "nuxt-module-feed",
  ],
  css: ["~/assets/css/main.css"],
  ui: {
    icons: ["heroicons", "lucide"],
  },
  app: {
    pageTransition: { name: "page", mode: "out-in" },
    head: {
      htmlAttrs: {
        class: "h-full",
      },
      bodyAttrs: {
        class: "antialiased bg-gray-50 dark:bg-black min-h-screen",
      },
      link: [{ rel: "icon", type: "image/svg+xml", href: "/favicon.svg" }],
    },
  },
  content: {
    highlight: {
      theme: "github-dark",
    },
  },
  fonts: {
    families: [{ name: "Inter", provider: "google" }],
  },
  i18n: {
    locales: [
      {
        code: "en",
        name: "English",
        file: "en.json",
        iso: "en-US",
      },
      {
        code: "th",
        name: "ไทย",
        file: "th.json",
        iso: "th-TH",
      },
    ],
    defaultLocale: "en",
    lazy: true,
    langDir: "locales",
    strategy: "prefix_and_default",
    detectBrowserLanguage: {
      useCookie: true,
      cookieKey: "i18n_redirected",
      redirectOn: "root",
    },
    vueI18n: "./i18n/i18n.config.ts",
  },
  feed: {
    sources: [
      {
        path: "/feed.xml",
        type: "rss2",
        cacheTime: 60 * 15,
      },
    ],
  },
  nitro: {
    minify: true,
    sourceMap: false,
    externals: {
      inline: ["three"], // Don't inline large deps
    },
    rollupConfig: {
      output: {
        manualChunks: (id) => {
          if (id.includes("three")) {
            return "three-vendor";
          }

          if (id.includes("node_modules")) {
            return "vendor";
          }
        },
      },
    },
    prerender: {
      routes: ["/feed.xml"],
    },
  },
});
