<template>
  <span
    ref="el"
    class="bg-blue-200/60 dark:bg-blue-400/30 rounded px-0.5 cursor-pointer"
    @click="onMobileClick"
  >
    <slot />
  </span>
</template>

<script setup lang="ts">
const props = defineProps<{ scene: string }>()
const el = ref<HTMLElement | null>(null)
const { activeScene, mobileScene, dismissedScene } = useLectureViz()
const { width } = useWindowSize()

const { pause, resume } = useIntersectionObserver(
  el,
  ([entry]) => {
    if (entry.isIntersecting) {
      if (dismissedScene.value !== props.scene) {
        activeScene.value = props.scene
      }
    } else {
      if (activeScene.value === props.scene) activeScene.value = null
      if (dismissedScene.value === props.scene) dismissedScene.value = null
    }
  },
  { threshold: 0.3, immediate: false }
)

onMounted(() => resume())

const onMobileClick = () => {
  if (width.value < 768) {
    mobileScene.value = props.scene
  }
}
</script>
