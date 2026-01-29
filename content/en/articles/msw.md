---
title: mock-service-worker for mocking API
description: "Short note on mock-service-worker for mocking API"
published: 2025/01/31
slug: "msw"
tags:
  - frontend
  - mocking
  - testing
  - short-note
---

tl:dr;

In this read, you will get insights on:

- Overview on `mock-service-worker` and how to use it
- How can we use `mock-service-worker` aside from only as a mock server

In front-end development, API is heavily relied in order to implement a feature. But we know that it is not always perfect. Sometimes it’s down due to some problem or not ready to use. I would like to introduce `mock-service-worker` , a tool for implementing mock server for browser and extend its actual capability that we can utilize beyond mock server.

## What is mock-service-worker?

`mock-service-worker` (or `msw`) is a library for implementing mock on browser (or node runtime) using service worker to intercept request that is matched the pattern as it is shown in this sequence diagram.

![image.png](https://images.yuttakhanb.dev/msw-sequence-diagram.webp)

(Ref: https://adamdonaghy.medium.com/mock-the-network-with-mock-service-workers-cf7ea671ebe3)

This sets a real difference to other service mocking approaches:

- Traditional mock server (or set your own server) — this requires additional efforts (more of grinding works) and maintainence cost
- `nock` — this library is useful for mocking requests in test runtime but is not able to mock server requests in browser runtime, also it is only able to mock REST-API (`msw` can mock Websocket server and GraphQL server)

## Small example on using msw

`msw` mock handlers can be implemented like this.

```tsx
import { setupWorker } from "msw/browser";
import { http, HttpResponse } from "msw";

// 1. Create handler for HTTP endpoint
const petHandler = http.get("/pets", ({ request }) => {
  return HttpResponse.json(["Tom", "Jerry", "Spike"]);
});

// 2. Set array of handlers and instantiate worker
const handlers = [petHandler];

export const worker = setupWorker(...handlers);
```

For using mock, just apply worker before frontend module started and we’re good to go.

```tsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";

async function enableMocking() {
  if (process.env.NODE_ENV !== "development") {
    return;
  }

  const { worker } = await import("./mock/node.ts");
  return worker.start();
}

enableMocking().then(() =>
  createRoot(document.getElementById("root")!).render(
    <StrictMode>
      <App />
    </StrictMode>
  )
);
```

For other details on using `msw`, there’s [a documentation here](https://mswjs.io/docs/).

## More than “mock server”?

I think for prior use case tends to target mock requests from browser. But actually it can be more than that.

1. Intercepting requests in unit test
   It is hinted from the beginning. I think this is pretty useful since mocking requests is painful in tests. Compare to other libraries, this setup is more simple and straightforward. Let’s see some example here.

```tsx
import { renderHook, waitFor, act, cleanup } from "@testing-library/react";
import { http, HttpResponse } from "msw";
import { setupWorker } from "msw/node";

// 1. Setup handlers.
const petHandler = http.get("/pets", ({ request }) => {
  return HttpResponse.json(["Tom", "Jerry", "Spike"]);
});

const petNotFoundHandler = http.get("/pets", ({ request }) => {
  return HttpResponse.json([]);
});

// 2.Setup worker for intercept requests.
const server = setupWorker(petHandler);

// Suppose usePet is a hook that fetch API from routes in handlers
describe("usePet", () => {
  // 3. Set server to listen for requests, reset handlers and close on test finished.
  beforeAll(() => {
    server.listen({ onUnhandledRequest: `error` });
  });

  afterAll(() => server.close());

  afterEach(() => {
    server.resetHandlers();
    cleanup();
  });

  it("should return pets", async () => {
    // 4. Add required handlers before hook renders for imitating server behavior.
    server.use(petHandler);
    const { result } = renderHook(usePet);

    // ...additional test logic here.
  });

  it("should return not found", async () => {
    server.use(petNotFoundHandler);
    const { result } = renderHook(usePet);

    // ...additional test logic here.
  });
});
```

As you can see, we don’t need to mock on the codebase directly. All we need to do is applying handlers that are used in mocking server to test cases and let us focus more on test logic.

There are more on detail about implementing tests with mock-service-worker. I think this is a good blog that shows how to implement it ([Article](https://tkdodo.eu/blog/testing-react-query)).

1. Specification design
   This can be used as shared information for coordinating team based on spec. Decoupling front end and backend tasks and could speed up implementation.

And that’s all about using msw. I hope it is useful for you and please share.
