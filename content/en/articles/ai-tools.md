---
title: "Two AI tools worth trying: GSD and RTK"
description: "Quick thoughts on Get-Shit-Done and RTK — tools that improve AI coding workflows through better prompting structure and token optimization."
published: 2026/04/04
slug: "ai-tools"
tags:
  - ai
  - tools
  - coding
  - productivity
---

Hi, recently I just had a shot to try out few tools on top of my usual coding agent like Claude and would like to have a quick sharing of thoughts over it.

### Get-Shit-Done and why metaprompting tends to be a great meta

One problem I found during usual coding tasks is its attention span, large context could make agent suffered and lead to invalid result. There are couple of techniques and practices to improve it e.g. few-shot prompting. One thing that many people tends to do is skills or persona at initial state, that's from concept called "metaprompting".

Metaprompting is techniques that building prompts that is focused on problem and tasks' aspects. We could called it "abstraction" in prompt engineering. If we take a look to prompts of tools that is based on these concept e.g. speckit. We will found these patterns.

1. A format/pattern of problems and solutions
2. Has syntax of expected response/solutions
3. Abstracted examples to show structure of problems and solutions
4. Draw from type theory to show categorization and logical arrangement

Sounds like AI memory but more generalized. right?

This is what "Get-Shit-Done" do, it has set of prompts for defining requirements, planning, research and executing stuff. User needed to have a clear objective of what to do, actually you could have only one sentence and it will find details of requirements and ask back to you. This also solve pain point of "not sure what you're doing".

![[[GSD usage](https://images.yuttakhanb.dev/Screenshot%202569-04-04%20at%2012.44.33.png)]]

From my usage for few days, I found that it is aligned with what many developers do (or at least me?). I like to do research and planning a lots before implement it. GSD imitates what I'm doing well, plus it helps refining on possible decisions too. You can also blindly accept what AI recommends you to do too.

### Optimizing tokens with RTK

Since coding tasks used up lots of tokens, having some tools to help optimizing tokens usage would be nice. RTK played around as CLI proxy that cutting out noises  (comments, whitespace, boilerplate), group similar items, truncate context and collapse repeated log lines. RTK is available for various programs that AI usually used e.g. Git, test runners, compliers.

```
  Without rtk:                                    With rtk:

  Claude  --git status-->  shell  -->  git         Claude  --git status-->  RTK  -->  git
    ^                                   |            ^                      |          |
    |        ~2,000 tokens (raw)        |            |   ~200 tokens        | filter   |
    +-----------------------------------+            +------- (filtered) ---+----------+
```

From my usage I found that it helps reducing tokens for many CLI calls and help lengthen a bit on LLM usage before it hits limits again. RTK also provides commands for monitoring reduced usage for it too.

### Conclusion

At least from 2 tools that I found I think it helps me on using AI as assistant a bit further. You can try out these 2 tools here.

GSD: https://github.com/gsd-build/get-shit-done
RTK: https://github.com/rtk-ai/rtk

Thanks for reading.
