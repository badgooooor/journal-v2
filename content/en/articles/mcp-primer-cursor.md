---
title: "A very quick overview on Cursor and Integration to Cursor"
description: "A very quick overview from few hours of experiment in MCP and quickly put it to Cursor IDE"
published: 2025/06/12
slug: "mcp-overview-cursor"
tags:
  - mcp
  - ai
  - cursor
---

_Note: Hi, I didn’t have intention to write this blog since it’s a bit fresh for me on this topic. However, I’ll present it to my colleagues so let’s give it a shot._

This blog will cover mostly on what I know so far on Model Context Protocol (MCP). It triggered a bit on what it is and made me did a quick research and tried out implementing it on weekend.

### What is MCP?

MCP is a framework/open protocol that came up due to problem on interaction between AI models and client applications. Think MCP likes USB-C for AI applications e.g. I want AI to interact with Jira ticket then I need to provide module for AI model to interact with Jira. For other benefits, as stated as “open protocol”, it is a standard for many AI models and integrations to interact freely and encourage plug-and-play interfaces on this standard.

![MCP Components](https://images.yuttakhanb.dev/mcp-components.webp)

### Components for MCP

Actually, it is just back to “client-server” model including,

1. Host for running AI Model
2. MCP Client for initiate requests
3. MCP Server which serve contexts and tools

![MCP Components](https://images.yuttakhanb.dev/mcp-components-2.webp)

From this diagram, we can see that MCP Server plays a huge role (and also primary component to implement) since it is the component that will interact with external application, being helping hands for AI model.

### Tested out quickly in Cursor.

I’m currently using Cursor and so I think it is good opportunity to try this quickly. There’re SDK available for various language in MCP e.g.

- Typescript
- C#
- Python
- Java
- Rust (in development)

The code for server is pretty much simple, I think for crucial parts we need to know is the resource that we can implement to serve. There’re 3 resources you need to know first,

1. Resource - these are data that you will expose from MCP server, this act like GET endpoint
2. Tools - these is computation, side-effect function for AI model to interact e.g. calculate data, automation script interact with website
3. Prompts - this is template prompt for AI model to use, similiar to what that is hyped as “prompt engineering” long before.

This is some example of tool I tried to implement quickly.

```typescript
const server = new McpServer({
  name: "my-server",
  version: "1.0.0",
  description: "A simple server that returns a greeting",
});

server.tool("affirmation", { name: z.string() }, async ({ name }) => {
  const response = await fetch("https://www.affirmations.dev/");
  const data = await response.json();
  return {
    content: [
      {
        type: "text",
        text: `Hey ${name}, ${(data as any).affirmation as string}`,
      },
    ],
  };
});
```

But having hands without head is useless, isn’t it? So let’s plug to Cursor.

MCP Server can be plugged in to IDE with only `.cursor/mcp.json` . The configuration including server name, command to run server and arguments. In this case, the absolute path (censor makes this looks a bit ugly).

![MCP JSON File in Cursor](https://images.yuttakhanb.dev/mcp-file.webp)

If everything is okay, the settings will show something like this.

![MCP List in Cursor Settings](https://images.yuttakhanb.dev/mcp-list.webp)

And this some sample usage here.

![Test MCP in chat](https://images.yuttakhanb.dev/test-mcp-cursor.webp)

I think that’s all for what I got from quickly learned this thing for few hours. You can check out quickly in [this repository](https://github.com/badgooooor/my-first-mcp-server).

Actually Cursor has arsenal of MCP Tools for add in to IDE quickly too. I haven’t checked it out yet. But definitely will try to see if it could help on productivity.

As someone who used LLM for various tasks from research to assist on coding, one weakness for LLM is it hard to cover the context that is required. It’s has few workarounds aside from dumping files to the chat e.g. using “ChatGPT wrappers” (I could say that there’re a lots in last year) but tradeoffs with trust on the application or implement an application with LLM based framework e.g. LangChain and pydantic which also requires some curve to understand and also a bit hard to migrate. I could say that this approach and its current ecosystem encourages developers to build more “helping hands” to AI models.

However, there are so many decisions in this protocol that is required a lots of discussion e.g.

- Security between components. There are plenty of papers show us how to abuse the system even though there are some prevention e.g. guardrails. It is still unknown territory that requires to explore.
- Transport between components. My personal sentiment on current decision would be “unstable”. Since there’s some changes (SSE → Streamable HTTP) but it’s minor for me.

For a mean time, I expect current approach for MCP is to implemented as application running based on local environment due to constraints I stated above. But that doesn’t mean it is limited, there’s still have some possibility to see MCP as plug-and-play service when we’re using AI model online.

I think that’s all for my founding. Thanks for reading!
