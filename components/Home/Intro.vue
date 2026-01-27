<template>
  <div class="text-right space-y-2">
    <p class="text-gray-900 dark:text-gray-400">
      {{ $t("home.bio.intro") }}
    </p>
    <p class="text-gray-900 dark:text-gray-400">
      <i18n-t keypath="home.bio.work" tag="span">
        <template #company>
          <a href="https://earnin.com" target="_blank" class="underline"
            >Earnin</a
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
