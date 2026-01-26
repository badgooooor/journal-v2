<template>
  <header
    class="sticky top-0 z-50 flex items-center justify-between px-6 sm:px-12 py-4 bg-white dark:bg-gray-900"
  >
    <ULink
      :to="localePath('/')"
      class="font-mono text-lg font-medium text-gray-800 dark:text-gray-200 hover:text-primary-500 dark:hover:text-primary-400 transition"
    >
      yuttakhan.b
    </ULink>

    <nav class="flex items-center gap-1">
      <template v-for="item in items" :key="item.path">
        <UTooltip
          :text="$t(item.labelKey)"
          :ui="{ popper: { strategy: 'absolute' } }"
        >
          <ULink
            :to="localePath(item.path)"
            class="relative p-2 flex items-center justify-center transition hover:text-primary-500 dark:hover:text-primary-400 text-gray-600 dark:text-gray-400"
            active-class="text-primary-600 dark:text-primary-400"
          >
            <Icon aria-hidden="true" :name="item.icon" class="w-5 h-5" />
            <span class="sr-only">{{ $t(item.labelKey) }}</span>
          </ULink>
        </UTooltip>
      </template>
      <div class="w-px h-5 bg-gray-300 dark:bg-gray-700 mx-2"></div>
      <AppLanguageSwitcher />
      <AppThemeToggle />
    </nav>
  </header>
</template>

<script setup>
const localePath = useLocalePath();
const route = useRoute();

const items = [
  { labelKey: "nav.home", path: "/", icon: "solar:home-smile-outline" },
  {
    labelKey: "nav.projects",
    path: "/projects",
    icon: "solar:folder-with-files-outline",
  },
  {
    labelKey: "nav.articles",
    path: "/articles",
    icon: "solar:document-add-outline",
  },
];

const isActive = (path) => {
  const currentPath = route.path;
  if (path === "/") {
    return currentPath === "/" || currentPath === "/th";
  }
  return currentPath.includes(path);
};
</script>
