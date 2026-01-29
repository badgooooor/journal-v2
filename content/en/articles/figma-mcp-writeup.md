---
title: "Writeups on automating generating code with Figma MCP"
description: "Very quick review on codecrafters"
published: 2025/07/19
slug: "figma-mcp-writeup"
tags:
  - mcp
  - figma
  - playwright
  - end-to-end testing
---

Hi, this’s a small writeups for experiment I’ve done with Figma MCP to build consistent code generator based on selection in Figma.

## Starting point

I found that Figma has released Dev mode MCP. With features on extracting design contexts, this enabling generating code result much better than relying only on screenshots.

[Figma MCP](https://www.figma.com/blog/introducing-figmas-dev-mode-mcp-server/)

However, most of the code that is generated are more of web/mobile codebases. I tried a bit on using Cursor to help me generate page object codebase for composing tests, but found out the result for selectors are a bit unstable. So I decided to make small prototype on this problem with these 2 targets.

- Make a full-loop workflow for generating page object codebase from design to my code project
- Generated code should be consistent

This could be a good point to make an MCP as a code generator for me.

## Extracting node from Figma

Currently Figma MCP has this documentation over provided interfaces, one thing that I focused a lot is get_code which will generate codebase from Figma. The result at least retrieves elements from design, make it a usable interfaces awaits for polishing.

![Figma MCP result](https://images.yuttakhanb.dev/mcp-playwright-figma.webp)

## Building up code generator

In my case, this is good enough for implementing test generator. It requires 2 components, the comprehensive typing for elements as input and code generator. There’re reason behind on using AST instead of just using string template for build up class and methods aside from “I just wanna try this”. String result from Typescript AST is much more consistent due to its code structure, it’s also leads to maintainability aspect too. This could be extended to several methods for functionality e.g. clicking the button, type the input.

The typing for elements is simple one, it is simple Typescript type. Refining types can enabling more functionalities for generated code. This is some simple types I did for prototype.

```typescript
export type FigmaComponentStructure = {
  /** HTML element type (div, p, img, etc.) */
  type: string /** CSS classes applied to the element */;
  className?: string /** Data attributes */;
  "data-name"?: string;
  /** Unique identifier for the node */
  id?: string;
  /** Text content for text elements */
  text?: string;
  /** Image source for img elements */
  src?: string;
  /** Child elements */
  children?: FigmaComponentStructure[];
};
```

Another component is code generation. Typescript provided tools for building an AST for typings and code e.g. `factory`, `createSourceFile` and `createPrinter`. This is some code from AST compared to its result.

```typescript
const isPresentMethod = ts.factory.createMethodDeclaration(
        [ts.factory.createModifier(ts.SyntaxKind.AsyncKeyword)],
        undefined,
        'verifyDivWidgetWrapperPresent',
        undefined,
        undefined,
        [],
        ts.factory.createTypeReferenceNode('Promise', [ts.factory.createKeywordTypeNode(ts.SyntaxKind.VoidKeyword)]),
        ts.factory.createBlock([
          ts.factory.createExpressionStatement(
            ts.factory.createAwaitExpression(
              ts.factory.createCallExpression(
                ts.factory.createPropertyAccessExpression(
                  ts.factory.createCallExpression(
                    ts.factory.createIdentifier('expect'),
                    undefined,
                    [
                      ts.factory.createPropertyAccessExpression(
                        ts.factory.createThis(),
                        name
                      )
                    ]
                  ),
                  ts.factory.createIdentifier('toBeVisible')
                ),
                undefined,
                []
              )
            )
          )
        ], true)
      );

const sourceFile = ts.createSourceFile('pageObject.ts', '', ts.ScriptTarget.ESNext, false, ts.ScriptKind.TS);
const printer = ts.createPrinter({ newLine: ts.NewLineKind.LineFeed });

return printer.printNode(ts.EmitHint.Unspecified, isPresentMethod
```

```typescript
async verifyDivWidgetWrapperPresent(): Promise<void> {
  await expect(this.divWidgetWrapper).toBeVisible();
}
```

## Exposing as a tool in MCP server

This is simple part but finishing all the loop we have. This includes setting MCP server and add those code generator to a tool. One thing that irritated me a bit is input schema itself, but it makes sense since it need structure of essential elements to generate the test.

```typescript
const generatePageObjectTool: Tool = {
  name: "generate_page_object",
  description:
    "Generates a Playwright page object class from Figma component structure",
  inputSchema: {
    type: "object",
    properties: {
      component: {
        type: "string",
        description: "The name of the Figma component",
      },
      structure: {
        type: "array",
        description: "The component structure from Figma",
        items: {
          type: "object",
          properties: {
            type: {
              type: "string",
              description: "HTML element type (div, p, img, etc.)",
            },
            className: {
              type: "string",
              description: "CSS classes applied to the element",
            },
            "data-name": {
              type: "string",
              description: "Data attributes for element identification",
            },
            id: {
              type: "string",
              description: "Unique identifier for the node",
            },
            text: {
              type: "string",
              description: "Text content for text elements",
            },
            src: {
              type: "string",
              description: "Image source for img elements",
            },
            children: {
              type: "array",
              description: "Child elements",
              items: {
                type: "object",
              },
            },
          },
        },
      },
    },
    required: ["component", "structure"],
  },
};
```

This is how it works in action in Cursor IDE. From Figma selection straight to Playwright page object codebase.

![Call result using Figma MCP and home-built MCP](https://images.yuttakhanb.dev/mcp-playwright-result-1.webp)

![Call result using Figma MCP and home-built MCP](https://images.yuttakhanb.dev/mcp-playwright-result-2.webp)

## Conclusion

This is a good small project during few weeks that I learned a bit more on implementing MCP server, chaining it together to automate a complex workflow. I also learned more on implementing code generator using Typescript factory code generator.

There are some few improvement ideas I which I would love to do. Here are some of them:

- Generate page object for other frameworks e.g. Cypress, Selenium or Serenity.
- Add more functionalities to page object, basically more interactions for composing tests.
- Make casing more proper for some selector
- Let LLM generate `data-testid` for page object code and as-is codebase in order to reduce labor works

Aside from improvements, I would love to test out more e.g. compare with using only LLM to generate in various aspects. There are still more to explore.

That’s all for my short prototype project during late June and July. Here’s my repository to check out that I don’t know what to name. [frame-pottery](https://github.com/badgooooor/frame-pottery). Thanks for reading.
