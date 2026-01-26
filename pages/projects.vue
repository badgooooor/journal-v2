<template>
  <main class="min-h-screen">
    <AppHeader
      class="mb-12"
      :title="$t('projects.title')"
      :description="$t('projects.description')"
    />
    <div class="space-y-4">
      <AppProjectCard
        v-for="(project, id) in projects"
        :key="id"
        :project="project"
      />
    </div>
  </main>
</template>

<script setup>
const { t } = useI18n();

useSeoMeta({
  title: () => t("seo.projects.title"),
  description: () => t("projects.description"),
});

const { data: projects } = await useAsyncData("projects-all", () =>
  queryContent("/projects").find()
);
</script>
