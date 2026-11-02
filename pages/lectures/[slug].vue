<template>
  <main class="min-h-full">
    <div class="flex gap-0 min-h-full relative">
      <!-- Left: prose content, shifts left when viz active -->
      <div
        class="flex-1 min-w-0 transition-all duration-300 ease-in-out prose dark:prose-invert prose-blockquote:not-italic prose-pre:bg-gray-900 prose-img:ring-1 prose-img:ring-gray-200 dark:prose-img:ring-white/10 prose-img:rounded-lg"
      >
        <ContentDoc :path="`/${locale}/lectures/${slug}`" tag="article">
          <template #default="{ doc }">
            <article>
              <h1 class="text-2xl font-semibold text-white">{{ doc.title }}</h1>
              <div v-if="doc.tags?.length" class="not-prose flex gap-2 mb-6 -mt-4">
                <span
                  v-for="tag in doc.tags"
                  :key="tag"
                  class="text-xs text-gray-500 dark:text-gray-400"
                >
                  #{{ tag }}
                </span>
              </div>
              <ContentRenderer :value="doc" />
            </article>
          </template>
          <template #not-found>
            <div class="not-prose text-center py-12">
              <p class="text-gray-600 dark:text-gray-400 mb-4">Lecture note not found.</p>
              <NuxtLink to="/lectures" class="text-teal-500 hover:text-teal-600">
                ← All lectures
              </NuxtLink>
            </div>
          </template>
        </ContentDoc>
      </div>

      <!-- Right: sticky viz panel, expands in when active (client-only to avoid hydration conflict) -->
      <ClientOnly>
        <div
          class="shrink-0 transition-[width,opacity] duration-300 ease-in-out overflow-hidden hidden md:block"
          :style="{ width: activeScene ? '45%' : '0px', opacity: activeScene ? '1' : '0' }"
        >
          <div class="sticky top-0 h-[70vh] pl-8 flex flex-col gap-2">
            <div class="flex items-center justify-between">
              <span class="text-xs text-gray-500 dark:text-gray-400">{{ activeScene }}</span>
              <button
                class="text-gray-400 hover:text-white transition-colors p-1"
                @click="closeScene"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
            <LectureViz :scene="activeScene" class="w-full flex-1 rounded-lg overflow-hidden" />
          </div>
        </div>
      </ClientOnly>
    </div>

    <!-- Mobile fullscreen overlay -->
    <Teleport to="body">
      <Transition name="mobile-viz">
        <div
          v-if="mobileScene"
          class="fixed inset-0 z-50 bg-gray-950 flex flex-col"
        >
          <div class="flex items-center justify-between p-4 border-b border-gray-800">
            <span class="text-sm text-gray-400">{{ mobileScene }}</span>
            <button
              class="text-gray-400 hover:text-white transition-colors p-1"
              @click="mobileScene = null"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
          <div class="flex-1">
            <LectureViz :scene="mobileScene" class="w-full h-full" />
          </div>
        </div>
      </Transition>
    </Teleport>
  </main>
</template>

<script setup lang="ts">
const route = useRoute()
const { locale } = useI18n()
const { slug } = route.params as { slug: string }
const { activeScene, mobileScene, closeScene } = useLectureViz()

onUnmounted(() => {
  activeScene.value = null
  mobileScene.value = null
})

useSeoMeta({
  title: () => `Lecture Notes`,
})
</script>

<style>
.mobile-viz-enter-active,
.mobile-viz-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.mobile-viz-enter-from,
.mobile-viz-leave-to {
  opacity: 0;
  transform: translateY(8px);
}

.prose h2 a,
.prose h3 a {
  @apply no-underline;
}
</style>
