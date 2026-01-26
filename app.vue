<template>
  <UApp>
    <NuxtLoadingIndicator color="#14b8a6" />
    <div class="h-screen w-screen p-4 sm:py-8 sm:px-8">
      <div
        class="w-full h-full flex flex-col border border-gray-300 dark:border-gray-700 bg-white dark:bg-gray-900 overflow-hidden"
      >
        <AppNavbar />
        <main class="flex-1 overflow-auto px-6 sm:px-12 py-8">
          <NuxtPage />
        </main>
        <AppFooter />
      </div>
    </div>
  </UApp>
</template>

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
