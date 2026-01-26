<script setup>
const { locale } = useI18n();
const switchLocalePath = useSwitchLocalePath();

const toggleLocale = () => {
  const nextLocale = locale.value === "en" ? "th" : "en";
  navigateTo(switchLocalePath(nextLocale));
};
</script>

<template>
  <UTooltip
    :text="$t('common.toggleLanguage')"
    :ui="{ popper: { strategy: 'absolute' } }"
  >
    <button
      class="relative px-3 py-4 flex items-center justify-center transition hover:text-primary-500 dark:hover:text-primary-400"
      @click="toggleLocale"
    >
      <span class="text-sm font-medium">
        {{ locale === "en" ? "TH" : "EN" }}
      </span>
      <span class="sr-only">{{ $t("common.toggleLanguage") }}</span>
    </button>
  </UTooltip>
</template>
