const activeScene = ref<string | null>(null)
const mobileScene = ref<string | null>(null)
const dismissedScene = ref<string | null>(null)

const closeScene = () => {
  dismissedScene.value = activeScene.value
  activeScene.value = null
}

export const useLectureViz = () => {
  return { activeScene, mobileScene, dismissedScene, closeScene }
}
