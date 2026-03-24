<template>
  <div
    class="pointer-events-none absolute left-0 top-0 h-full w-full"
    style="z-index: 0"
  >
    <TresCanvas
      alpha
      clear-color="transparent"
      class="h-full w-full"
    >
      <TresOrthographicCamera
        :args="[-1, 1, 1, -1, 0.1, 1000]"
        :position="[0, 0, 1]"
      />
      <HomeBackgroundScene />
    </TresCanvas>
    <div
      class="absolute left-0 top-0 h-full w-full backdrop-blur-sm"
      style="z-index: 1"
    />
  </div>
</template>
