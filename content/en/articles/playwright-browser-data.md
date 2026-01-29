---
title: Verifying browser data via Playwright
description: "Small notes on retrieving data from browser to verify with Playwright"
published: 2025/06/07
slug: "playwright-browser-data"
tags:
  - frontend
  - end-to-end testing
  - playwright
  - short-note
---

There are many scenarios that requires to check data in the application e.g. logging in SSO, validating consent on analytics website. These scenarios have to use browser data and network data to fulfil the objective.

In this blog, I would like to show how can I get these data to in Playwright. I think a good use case that can could showcase these technique is checking tracking analytics that is embedded in website e.g. Google Tag Manager. Usually tracking analytics will attach scripts called “tracking pixel” as invisible (it’s 0 px x 0 px) `img` tag to website with script for tracking, either set cookies or sending requests.

### Network data

This is the easiest one. Playwright provides interface for intercepting or mutating requests as `page.on('request', data => {});`

```typescript
let isTrackingPixelAttached = false;

page.on('request', request => {
	if (request.url.includes('https://gtm') {
		isTrackingPixelAttached = true;
	}
});
```

This is pretty useful for checking since every HTTP requests will be intercepted by this listener even the Javascript file that is used for running analytics. You can verify from URL of intercepted requests since usually there’ll be requests for tracking e.g.

- Request Javascript file for running tracking
- Request for firing custom event

![Network inspect](https://images.yuttakhanb.dev/network-request-inspect.webp)

Aside from above use case, this listener also useful for other techniques too e.g. validating data of request and response.

### Cookies

Cookie is a bit tricky but it is in browser context. With `browserContext.cookies()`, it will return list of cookies attached in the browser at that time.

```typescript
const facebookPixelCookieName = "_fb";

const cookies = await context.cookies();
const isFacebookPixelAttached = cookies.find(
  cookie => cookie.name === facebookPixelCookieName
);
```

I used cookies to verify that if tag script has attached cookie to the browser by check with cookie name since cookies that these analytics service applies has specific name. This is also similiar to other services to e.g. authentication services or data privacy (or consent) service.

![Cookies inspect](https://images.yuttakhanb.dev/cookie-inspect.webp)

A tricky part for checking cookies is requests is it is asynchronous and we cannot predict when these cookies are set. There are some workaround for this problem e.g. simply set timeout to wait for cookies or set up interval to keep track on current state of browser.

And these are what I learnt recently to verify these data. These concept is pretty much useful in other problems like handling single sign-on page or applying these concepts to write test in different framework like Cypress.
