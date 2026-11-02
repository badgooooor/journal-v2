<template>
  <div class="w-full h-full">
    <Transition name="viz-fade" mode="out-in">
      <div v-if="scene" :key="scene" ref="containerRef" class="w-full h-full" />
    </Transition>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{ scene: string | null }>()
const containerRef = ref<HTMLElement | null>(null)
let playerEl: HTMLElement | null = null
let manimgxReady = false

const ensureManimgx = async () => {
  if (!manimgxReady) {
    await import("manimgx")
    manimgxReady = true
  }
}

const renderScene = async (sceneName: string) => {
  await ensureManimgx()
  await nextTick()
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
}

watch(
  () => props.scene,
  async (newScene) => {
    if (newScene) {
      await renderScene(newScene)
    } else {
      playerEl?.remove()
      playerEl = null
    }
  },
  { immediate: true }
)

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
