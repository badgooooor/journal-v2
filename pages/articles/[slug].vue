<template>
  <main class="min-h-screen">
    <div
      class="prose dark:prose-invert prose-blockquote:not-italic prose-pre:bg-gray-900 prose-img:ring-1 prose-img:ring-gray-200 dark:prose-img:ring-white/10 prose-img:rounded-lg"
    >
      <ContentDoc :path="`/${locale}/articles/${slug}`" tag="article">
        <template #default="{ doc }">
          <article>
            <h1>{{ doc.title }}</h1>
            <ContentRenderer :value="doc" />
          </article>
        </template>

        <template #not-found>
          <div class="not-prose text-center py-12">
            <p class="text-gray-600 dark:text-gray-400 mb-4">
              {{ $t("common.contentNotTranslated") }}
            </p>
            <div class="flex gap-4 justify-center">
              <NuxtLink
                v-if="locale !== 'en'"
                :to="`/articles/${slug}`"
                class="text-teal-500 hover:text-teal-600 dark:text-teal-400 dark:hover:text-teal-300"
              >
                {{ $t("common.viewInEnglish") }} &rarr;
              </NuxtLink>
              <NuxtLink
                v-if="locale === 'en'"
                :to="`/th/articles/${slug}`"
                class="text-teal-500 hover:text-teal-600 dark:text-teal-400 dark:hover:text-teal-300"
              >
                {{ $t("common.viewInThai") }} &rarr;
              </NuxtLink>
            </div>
          </div>
        </template>
      </ContentDoc>
    </div>
  </main>
</template>

<script setup>
const route = useRoute();
const { locale, t } = useI18n();
const { slug } = route.params;

useSeoMeta({
  title: () => `${t("articles.title")} | ${t("seo.home.title")}`,
  ogImage: `https://fayazahmed.com/articles/${slug}.png`,
  twitterCard: "summary_large_image",
  articleAuthor: "Fayaz Ahmed",
});
</script>

<style>
.prose h2 a,
.prose h3 a {
  @apply no-underline;
}
</style>
