<template>
  <UApp>
    <NuxtLoadingIndicator color="#14b8a6" />
    <div class="h-screen w-screen p-4 sm:py-8 sm:px-8">
      <div
        class="w-full h-full flex flex-col border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 overflow-hidden relative"
      >
        <HomeBackground v-if="showBackground" />
        <AppNavbar class="relative z-10" />
        <main class="relative z-10 flex-1 overflow-auto px-6 sm:px-12 py-8">
          <NuxtPage />
        </main>
        <AppFooter class="relative z-10" />
      </div>
    </div>
  </UApp>
</template>

<script setup>
const route = useRoute();

const showBackground = computed(() => {
  // Check route path instead of name for better reliability on initial load
  return route.path === "/" || route.name === "index";
});
</script>

<style>
.page-enter-active,
.page-leave-active {
  transition: all 0.2s;
}

.page-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}

.page-enter-from {
  opacity: 0;
  transform: translateY(5px);
}
</style>
