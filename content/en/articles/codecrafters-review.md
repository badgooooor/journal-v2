---
title: "Very quick review on Codecrafters"
description: "Very quick review on codecrafters"
published: 2024/07/27
slug: "codecrafters-review"
tags:
  - coding
  - side-project
  - review
---

Let's talk about side projects first, what would you do as a side project? Well, It has various ranges from just a small things that can solve your own problem to indie-hacker,solopreneur scale startup. Some would just do some random tutorials, trying to learn new tools, langauges or framework to gear up their arsenal.

I think it's more on purpose, and recently I want to build up skill on system programming using Golang. (I've tried Rust but it's too pain for me now.) But what should I do on this? Some random API tutorial with framework like "go-fiber" wouldn't make me having more understanding on this.

### So what is codecrafters?

After a bit of scrolling, I found this.

[build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)

So the concept is simple, why not build tool you using everyday? It's a good article even though it sells out their platform. This concept buys me in quickly that why don't I just checkout?

Codecrafters is more of intermediate-level which provide guided challenges on building stuff e.g. Redis, HTTP Server. It is not that kind of tutorial that will really guide you along, more of problem you need to solve with their test cases like LeetCode but more on build stuff. It is also provides CLI for running test and submitting solution too.

![Codecrafter UI](https://images.yuttakhanb.dev/codecrafter-ui.png)

![Codecrafter Test via CLI](https://images.yuttakhanb.dev/codecrafter-test.png)

For my challenge, I take up the free course in this month, build your own "HTTP" server. End up realizing that this can be hacked through chapters and chapters, get away from it and just complete the challenge.

```golang
    req := make([]byte, 1024)
    conn.Read(req)
    data_str := string(req)

	request_line := strings.TrimSpace(data_str)
	parts := strings.Split(request_line, " ")

	// Path section
	if parts[1] != "/" {
		conn.Write([]byte("HTTP/1.1 404 Not Found\r\n\r\n"))
		conn.Close()
	} else {
		conn.Write([]byte("HTTP/1.1 200 OK\r\n\r\n"))
	}
```

This is a part of my earlier attempts in the beginning, very ugly.

But it is not fun, right. For many challenges (as it goes on), you're going to realize the pattern and build something worthy out of it. In this case, I end up with my homemade API framework. Here's [my repository of my finished project on this challenge](https://github.com/badgooooor/cct-http-server-go).

### Personal take on "maxxing out" codecrafters challenges

In order to maximize benefits from learning this, I think it is good to explore a bit on what you're building since many of these things are based on fundamental stuff (which you wouldn't found in typical online course in these days). This can be vary from,

- Internal mechanics, see how modules are correlated
- Data structure behind the scene
- Leverage your solution from implementing langauge
- Optimization
- Organizing modules
- Writing test
- ...many more

Its awesomeness on building things from scratch is not the finished project, but it is more of what you've learned during the journey. I hope you enjoy my article and try this out.
