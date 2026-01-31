import type { NitroCtx } from "nuxt-module-feed";

const SITE_URL = "https://yuttakhanb.dev";

export default defineNitroPlugin((nitroApp) => {
  nitroApp.hooks.hook("feed:generate", async ({ feed }: NitroCtx) => {
    feed.options = {
      id: SITE_URL,
      title: "yuttakhanb.dev",
      description: "Articles and writings by Yuttakhan",
      link: SITE_URL,
      language: "en",
      favicon: `${SITE_URL}/favicon.svg`,
      copyright: `All rights reserved ${new Date().getFullYear()}`,
      feedLinks: {
        rss: `${SITE_URL}/feed.xml`,
      },
    };

    const articles = await $fetch("/api/_content/query", {
      params: {
        _params: JSON.stringify({
          where: [{ _path: { $contains: "/en/articles" } }],
          sort: [{ published: -1 }],
        }),
      },
    });

    if (!Array.isArray(articles)) return;

    for (const article of articles) {
      feed.addItem({
        title: article.title ?? "",
        id: `${SITE_URL}${article._path}`,
        link: `${SITE_URL}/articles/${article.slug}`,
        description: article.description,
        date: new Date(article.published),
      });
    }
  });
});
