<template>
  <footer
    class="sticky bottom-0 flex items-center justify-between px-6 sm:px-12 py-4 border-t border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 text-sm text-gray-500 dark:text-gray-400"
  >
    <p>{{ $t("footer.copyright", { year: new Date().getFullYear() }) }}</p>
    <nav class="flex items-center gap-3">
      <a
        v-for="social in socialLinks"
        :key="social.name"
        :href="social.url"
        target="_blank"
        rel="noopener noreferrer"
        class="text-gray-400 dark:text-gray-500 hover:text-gray-600 dark:hover:text-gray-300 transition"
        :aria-label="social.name"
      >
        <Icon :name="social.icon" class="w-5 h-5" />
      </a>
    </nav>
  </footer>
</template>

<script setup>
const socialLinks = [
  {
    name: "GitHub",
    icon: "mdi:github",
    url: "https://github.com/",
  },
  {
    name: "LinkedIn",
    icon: "mdi:linkedin",
    url: "https://linkedin.com/in/",
  },
  {
    name: "Twitter",
    icon: "mdi:twitter",
    url: "https://twitter.com/",
  },
  {
    name: "RSS",
    icon: "mdi:rss",
    url: "/rss.xml",
  },
];
</script>
