<template>
  <main class="min-h-full">
    <AppHeader class="mb-16" title="Lecture Notes" description="Visual notes from things I'm learning." />
    <ul v-if="lectures?.length" class="space-y-16">
      <li v-for="(lecture, id) in lectures" :key="id">
        <NuxtLink :to="lecture._path" class="group">
          <article>
            <time
              class="relative z-10 order-first mb-3 flex items-center text-sm text-gray-400 dark:text-gray-500 pl-3.5"
            >
              <span class="absolute inset-y-0 left-0 flex items-center" aria-hidden="true">
                <span class="h-4 w-0.5 rounded-full bg-gray-200 dark:bg-gray-500"></span>
              </span>
              {{ getReadableDate(lecture.date) }}
            </time>
            <h2
              class="text-base font-semibold font-display tracking-tight text-gray-800 dark:text-gray-100 group-hover:text-primary-600"
            >
              {{ lecture.title }}
            </h2>
            <div v-if="lecture.tags?.length" class="mt-2 flex gap-2">
              <span
                v-for="tag in lecture.tags"
                :key="tag"
                class="text-xs text-gray-500 dark:text-gray-400"
              >
                #{{ tag }}
              </span>
            </div>
          </article>
        </NuxtLink>
      </li>
    </ul>
    <div v-else class="text-center py-12">
      <p class="text-gray-600 dark:text-gray-400">No lecture notes yet.</p>
    </div>
  </main>
</template>

<script setup lang="ts">
const { locale } = useI18n()

useSeoMeta({
  title: "Lecture Notes",
  description: "Visual notes from things I'm learning.",
})

const { data: lectures } = await useAsyncData(
  `all-lectures-${locale.value}`,
  () =>
    queryContent(`/${locale.value}/lectures`)
      .where({ draft: { $ne: true } })
      .sort({ date: -1 })
      .find(),
  { watch: [locale] }
)

const getReadableDate = (dateString: string) => {
  const date = new Date(dateString)
  const localeCode = locale.value === "th" ? "th-TH" : "en-US"
  return date.toLocaleDateString(localeCode, {
    year: "numeric",
    month: "short",
    day: "numeric",
  })
}
</script>
