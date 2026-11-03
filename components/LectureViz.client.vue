<template>
  <div class="w-full h-full relative">
    <div ref="containerRef" class="w-full h-full" />
    <div
      v-if="loading"
      class="absolute inset-0 flex items-center justify-center text-xs text-gray-500"
    >
      Loading visualization…
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ scene: string | null }>()
const containerRef = ref<HTMLElement | null>(null)
const loading = ref(false)
let playerEl: HTMLElement | null = null
let manimgxReady = false

const ensureManimgx = async () => {
  if (!manimgxReady) {
    await import("manimgx")
    manimgxReady = true
  }
}

const renderScene = async (sceneName: string) => {
  loading.value = true
  try {
    await ensureManimgx()
    if (props.scene !== sceneName) return

    if (!containerRef.value) return

    const response = await fetch(`/scenes/${sceneName}.py`)
    if (!response.ok) {
      console.error(`[LectureViz] scene not found: /scenes/${sceneName}.py`)
      return
    }
    const pythonCode = await response.text()

    if (playerEl) {
      playerEl.remove()
      playerEl = null
    }

    const player = document.createElement("manimgx-player") as any
    player.setAttribute("autoplay", "")
    player.style.cssText = "display:block;width:100%;height:100%;"
    containerRef.value.appendChild(player)
    playerEl = player
    player.source = pythonCode
  } finally {
    if (props.scene === sceneName) loading.value = false
  }
}

watch(
  () => props.scene,
  async (newScene) => {
    if (newScene) {
      await renderScene(newScene)
    } else {
      playerEl?.remove()
      playerEl = null
      loading.value = false
    }
  },
  { immediate: true }
)

onMounted(() => {
  ensureManimgx()
})

onUnmounted(() => {
  playerEl = null
})
</script>

<style scoped>
.viz-fade-enter-active,
.viz-fade-leave-active {
  transition: opacity 0.2s ease;
}
.viz-fade-enter-from,
.viz-fade-leave-to {
  opacity: 0;
}
</style>
