<template>
  <div class="space-y-6">
    <NuxtImg
      src="/avatar.png"
      alt="Fayaz Ahmed"
      class="ring-2 border ring-gray-200 border-gray-300 dark:ring-white/10 dark:border-gray-800 hover:ring-4 transition-all duration-300 rounded-full h-12 w-12 sm:h-16 sm:w-16"
      sizes="48px sm:64px"
      placeholder
      format="webp"
    />
    <h1
      class="text-xl font-bold tracking-tight text-gray-800 dark:text-gray-100"
    >
      {{ $t("home.greeting") }}
    </h1>
    <p class="text-gray-900 dark:text-gray-400">
      {{ $t("home.bio.intro") }}
    </p>
    <p class="text-gray-900 dark:text-gray-400">
      <i18n-t keypath="home.bio.work" tag="span">
        <template #company>
          <a href="https://headshotpro.com" target="_blank" class="underline"
            >Headshotpro</a
          >
        </template>
      </i18n-t>
    </p>
  </div>
</template>

<script setup>
const { t } = useI18n();

useSeoMeta({
  title: () => t("seo.home.title"),
  description: () => t("seo.home.description"),
});
</script>
