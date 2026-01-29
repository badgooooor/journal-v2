---
title: Vendor code splitting in Vite
description: "Optimizing initial load time on dependencies in VIte application."
published: 2023/11/19
slug: "vendor-code-splitting-vite"
tags:
  - frontend
  - code-splitting
  - optimization
  - short-note
---

Things started out when I found that bundle size on built code is a bit large. And this is its log during build. So, it's right time to take your app exercised.

```bash
...others css files, fonts and index.html
../../dist/app/assets/index-3b99fee0.css                            1,618.15 kB │ gzip:   160.35 kB
../../dist/app/assets/index-ab979bee.js                             3,775.49 kB │ gzip: 1,029.77 kB

(!) Some chunks are larger than 500 kBs after minification. Consider:
```

### So what is chunk?

Browser cannot read `.ts`, `.vue` or `.tsx` directly, so these files are needed to be converted to `.js` files. And there are a lots of "module bundlers" which is for converting these files and minimize them in order to make chunk files much more smaller (Smaller files makes initial load takes less time). These are some of existing module bundlers.

- [Webpack](https://webpack.js.org/)
- [Parcel](https://parceljs.org/)
- [Rollup, this is used by Vite](https://rollupjs.org/)

**Is that just enough?**

Well, initial load time (reflected in web vitals e.g. FCP, LCP) can be increased over time from larger codebases and more dependencies is being used. If built code is seperate to smaller files, browser can load more files at the same time which make web application startups much faster.
That's when code splitting like seperating vendor code from application code or splitting code from routes can help.

### What normal configuration do?

If we run build without any configuration, we'll see some log like above. Let's take it here again.

```bash
...others css files, fonts and index.html
../../dist/app/assets/index-3b99fee0.css                            1,618.15 kB │ gzip:   160.35 kB
../../dist/app/assets/index-ab979bee.js                             3,775.49 kB │ gzip: 1,029.77 kB

(!) Some chunks are larger than 500 kBs after minification. Consider:
```

As you can see, Rollup will build only `index-xxxxxxx.js` with everything putted in there both your source code and dependencies. The larger the size is, it can be much more slower on loading.

### Split vendor code from built code.

Vite provides plugin for seperating vendor code from source code called `splitVendorChunkPlugin`.

```typescript
import { splitVendorChunkPlugin } from "vite";

export default defineConfig({
  plugins: [react(), nxViteTsPaths(), splitVendorChunkPlugin()],
});
```

Here is its result.

```bash
../../dist/app/assets/index-3b99fee0.css                            1,618.15 kB │ gzip: 160.35 kB
../../dist/app/assets/index-1bc1072e.js                               139.54 kB │ gzip:  41.27 kB
../../dist/app/assets/vendor-096aa33c.js                            3,598.30 kB │ gzip: 982.89 kB
```

That's quite a lot. But is there anyways to split more vendor chunk.

### Rollup plugin visualizer

There is this plugin for analysing which code is main villian (too large) called [rollup-plugin-visualizer](https://www.npmjs.com/package/rollup-plugin-visualizer). For Vite, this can be used with `npx`.

```bash
npx vite-bundle-visualizer
```

### Rollup manualChunks

Rollup provides `manualChunks` in case we want to configure more than just using plugins. This can be used for grouping some vendor code to specific chunk or even dynamically seperate the chunk. Here is some example on how to use `manualChunks`.

```typescript
build: {
  rollupOptions: {
    output: {
      manualChunks: (id: string) => {
        if (id.includes('a-very-large-dependency')) {
          return 'big-chungus';
        }

        if (
            id.includes('react-router-dom') ||
            id.includes('react-router')
        ) {
          return '@react-router';
        }
      },
    },
  },
},
```

There is some concern when using `manualChunks`. We need to know which dependencies needed to be in the same chunk or your application can be broken on running. For my personal uses, it is pretty useful for splitting large dependencies (decrease average chunk size on built).
And here is its result after applied `manualChunks`.

```bash
../../dist/app/assets/form-renderer-eedcabe5.css                      545.63 kB │ gzip:  59.68 kB
../../dist/app/assets/index-f0f082d7.css                            1,072.52 kB │ gzip: 101.02 kB
../../dist/app/assets/@react-router-3dd16f73.js                        20.15 kB │ gzip:   7.38 kB
../../dist/app/assets/index-44c351ae.js                               139.60 kB │ gzip:  41.30 kB
../../dist/app/assets/vendor-f98a079f.js                            1,592.18 kB │ gzip: 446.07 kB
../../dist/app/assets/form-renderer-6007bd59.js                     1,910.33 kB │ gzip: 514.00 kB
```

The largest chunk takes 1,900kB (gzipped 514.kB) which is much better than single `index-xxxxxxx.js` with 3.9MB.

## Conclusion

Vendor code splitting can helps initial load time. I hope you saw how to apply it in Vite via `splitVendorChunkPlugin` and `manualChunks` and analyse dependencies with Rollup plugin visualizer.

However, there are more code splitting that is useful when codebase gets larger e.g. lazy loading on routes (or modules) and tree shaking. (which I would write some blog on this later, I guess.)
