<template>
  <div>
    <h2 class="uppercase text-xs font-semibold text-gray-400 mb-6">
      {{ $t("home.recentArticles") }}
    </h2>
    <ul class="space-y-16">
      <li v-for="(article, id) in articles" :key="id">
        <AppArticleCard :article="article" />
      </li>
    </ul>
    <div class="flex items-center justify-center mt-6 text-sm">
      <UButton
        :label="`${$t('home.allArticles')} →`"
        :to="localePath('/articles')"
        variant="link"
        color="gray"
      />
    </div>
  </div>
</template>

<script lang="ts" setup>
const { locale } = useI18n();
const localePath = useLocalePath();

const { data: articles } = await useAsyncData(
  `articles-home-${locale.value}`,
  () =>
    queryContent(`/${locale.value}/articles`)
      .sort({ published: -1 })
      .limit(3)
      .only(["title", "description", "published", "slug", "_path"])
      .find(),
  { watch: [locale] }
);
</script>
