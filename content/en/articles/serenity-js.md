---
title: "Screenplay Pattern Testing with Serenity.js"
description: "Let's make E2E Test more readable with Serenity.js."
published: 2024/01/28
slug: "screenplay-serenity"
tags:
  - frontend
  - end-to-end testing
  - playwright
  - short-note
---

Recently I've attended [BKK.JS at Siam Paragon](https://www.facebook.com/events/1163252551312047) and there is session about [Javascript Testing by P'Somkiat](https://www.somkiat.cc/sharing-javascript-testing-every-day/) and I also forgot that I've done some proof-of-concept on end-to-end testing (which is ready for lightning talk stuff). I guess I should share here.

### Problems on E2E Testing

1. Messy test code

   - Current codebase pattern e.g. page object pattern is unintuitive, duplicate
   - Explicit waits
   - It's so free-form that

2. Test code cannot be documentated or maintained easily

   - From (1), onboarding application is hard for developers and maintainers.
   - This is even harder on knowing as-is requirements/features of a project

### What if it is not page object pattern.

Screenplay pattern proposed test involved around these components.

1. Actor

This is a person (or some system) interacting with the application play as specific role e.g. Bob as an admin or Alice as a user.

2. Ability

Actor has "abilities" that can do some interaction with interfaces of application e.g. use a browser

3. Interaction

Abilities enable user to do some interactions e.g. navigating to page or click a some buttons

4. Question

Actor can answer "questions", asserting if it is correct or not. This is the same as `expect`.

5. Task

From all those component above, it can be formed as sequences of activities, describing business requirement of what we can do in a test in a normal human readable form.

### Serenity.js

This library is for implementing tests with screenplay pattern, including all business logic of screenplay pattern on top of your favorite end-to-end testing library e.g.

- [Playwright](https://serenity-js.org/handbook/getting-started/serenity-js-with-playwright-test/) -- this is my preference
- [Protractor](https://serenity-js.org/handbook/getting-started/serenity-js-with-protractor/)
- [WebdriverIO](https://serenity-js.org/handbook/getting-started/serenity-js-with-webdriverio/)

Easy setup, just click and go along.

Let's take a look at code, here is some example of my first attempt and it is "perfection".

```typescript
import { describe, it } from "@serenity-js/playwright-test";
import { Navigate, PageElements, By } from "@serenity-js/web";
import { Ensure, equals } from "@serenity-js/assertions";
import { displayItemCounts } from "../app/questions";
import { useAppActor } from "../fixtures/actors";

describe("Todo List", () => {
  useAppActor();

  it("list should be empty", async ({ actorCalled }) => {
    // Actor doing stuff in test.
    await actorCalled("Alice").attemptsTo(
      // Task.
      Navigate.to("https://todo-app.serenity-js.org/"),
      // Question.
      Ensure.that(displayItemCounts(), equals(0))
    );
  });
});
```

From the code, everything component can be seperated as functions or classes and combined as a test. Let's take a look at task and question in this test case.

```typescript
import { By, PageElements } from "@serenity-js/web";

// Interaction to page.
export const displayedItems = (): PageElements =>
  PageElements.located(By.css(".todo-list li")).describedAs("displayed items");

export const displayItemCounts = () => displayedItems().count();
```

![Test report](https://images.yuttakhanb.dev/serenity-test-report.png)

For full code of example test, please checkout at [this repository](https://github.com/badgooooor/tryout-serenity).
