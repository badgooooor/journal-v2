<template>
  <main class="min-h-full">
    <AppHeader
      class="mb-16"
      :title="$t('articles.title')"
      :description="$t('articles.description')"
    />
    <ul v-if="articles?.length" class="space-y-16">
      <li v-for="(article, id) in articles" :key="id">
        <AppArticleCard :article="article" />
      </li>
    </ul>
    <div v-else class="text-center py-12">
      <p class="text-gray-600 dark:text-gray-400 mb-4">
        {{ $t("common.noArticlesYet") }}
      </p>
      <NuxtLink
        v-if="locale !== 'en'"
        to="/articles"
        class="text-teal-500 hover:text-teal-600 dark:text-teal-400 dark:hover:text-teal-300"
      >
        {{ $t("common.viewInEnglish") }} →
      </NuxtLink>
    </div>
  </main>
</template>

<script setup>
const { t, locale } = useI18n();

useSeoMeta({
  title: () => t("seo.articles.title"),
  description: () => t("articles.description"),
});

const { data: articles } = await useAsyncData(
  `all-articles-${locale.value}`,
  () =>
    queryContent(`/${locale.value}/articles`).sort({ published: -1 }).find(),
  { watch: [locale] }
);
</script>
