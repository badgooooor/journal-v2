---
title: "an invisbly adventure at invisible garden 0"
description: "A long blog about adventure in learning ZKP and other stuffs from hacker house invisible garden at Chiang Mai, Thailand"
published: 2024/11/11
slug: "invisible-garden-0"
tags:
  - hackerhouse
  - zero-knowledge proof
  - ethereum
  - web3
  - experience
---

I would like to share my experience on participating Invisible Garden in Chiang Mai during October-November. It took me almost 4 weeks in total (first two weeks on October and 1.5 weeks on November). There are many sessions/workshops which leads up to build project on web3, focused on zero-knowledge proof and related topics. A lots of fun activities aside from works is hosted and occurred too. It is one of hacker house amongs others in Chiang Mai that hosted before Devcon in Bangkok (You could say that it is "pre-event"). Let's dive in.

## what's invisible garden? (tell primary on this one and mention others a bit)

Invisible garden is a hacker house project focused on knowledge sharing and buiding project based on zero-knowledge proof and other related topics e.g. MPC, FHE and web3 stuffs. The hacker house hosted during October-November for 6 weeks full of workshops, sessions, activities and bustling crowd of people.

There are a lots of people in this hacker house varies from developers, researchers, some are web3 OGs, some are newcomers. There are mentors from many groups e.g. PSE (Privacy and Scaling Exploration - Etheruem Foundation), Antalpha Labs, Secbit and many more. Lots of participants come from different places e.g. Latin America, China, Vietnam, EUs and Thailand! Bunch of Thai people here are as different roles, some are university students who is new to web3/ZKP, some are working and even as mentors.

## Workshops

There are a lots of workshops. It covers from basic stuff on Solidity course or query data from oracle to some real-deal workshops. In this case, I'm going to highlight on some workshops I found it is spectacular.

### The whiteboard sessions by Dr. Guo Yu (SECBIT)

It's sessions with theme on building zero-knowledge proof protocol from simple and start to add more components which becomes an applicable protocol. There are also explanation on some existed protocols. The lectures itself is more on "whiteboard" with explanation and some thought-provoking breakout during session. There are even some off-script session which even more mind-blowing. To be honest, this can be a free master-degree subject course for me since there are a lot of sessions (which takes about 2-3 weeks).

![Session](https://images.yuttakhanb.dev/invgarden-session.jpg)

### Application on zero-knowledge proof with zkemail

I think I should tell you shortly about `zkemail` first. `zkemail` is a email verification solutions powered by zero-knowledge. Currently there are solutions based on this application e.g.

- Email verification, generating proof out of regex matching in header-body
- Email wallet, using with Account Abstraction layer to create wallet out of email, send ETH or transaction comes with recovery feature

This one is more hands-on workshop on using application that use zero-knowledge proof as fundamental. I tried on creating verification based on various types of email, rechecking things and make it ready for deploying as contract.

Actually there are some workshops and sessions that I missed during flight back to Bangkok (sync up works and plan on side events in Devcon with team). For quick it covered these topics

- More complicated protocols e.g. STARK and SNARK, FFT, Plonky3
- Phantom-zone (mpFHE library)
- Modular stack for zkVM
- PSE Deshittification (applications that care about the user)
- Sponsored sessions e.g. Orbit Finance, Push Protocol

## Project building

Everyone needs to submit at least a project by the end of hacker house. There are bi-weekly checkup on project progress during the hacker house. The final demo is arranged at last week before Invisible Garden concluded. Mentors are available to consult and support for everyone.

## What I've did in Invisible Garden?

I joined up with John, Alok/Surfer, Qing Hao, Harold and Kenil on implementing [`zklings`](https://github.com/rutefig/zklings/pulls), a repository aims to educate developers about implementation around zero-knowledge proofs via dozen of small exercises. This repository is forked from Rust's rustlings.

![Demo](https://images.yuttakhanb.dev/invgarden-demo.jpg)

One thing I as takeaway aside from Rust stuff (it's my first time on really digging into Rust) is it's really good to see someone taking existed works (or hackathon stuff) and make it more functional. It's so satisfying if we think in term of open-source and collaboration.

There are also something I tried out which I intended to do but got sick during late October e.g.

- [Proof of issue completed](https://registry-dev.zkregex.com/try/badgooooor/proof-completed-github-issue) by checking issue completed email
- Attempted to integrate Push Protocol in Lit Action, this is more of 2 days speedrun which I found some flaws on security + worked on `zklings` submission so I paused it

### Other interesting projects in Invisible Garden

- [zk-ninja](https://zk.ninja/), this is from Thai mentor friends. Flipped classroom for learning primers of zero-knowledge stuff
- [apstark](https://github.com/sota-zk-labs/apstark), Layer 2 ZK-Rollup blockchain built on top of the Aptos network. "Building for fun from scratch"
- [Proof of Invisible](https://github.com/invisible-garden/cm24-projects/blob/main/proof-of-invisible/README.md), an automated attendance verification system
- [modity](https://github.com/nishuzumi/modity), a browser-based Jupyter Notebook-like environment for Solidity
- [voizk-ML](https://github.com/Privacy-Lab-Latam-Builders/voizk-ML), attempt at using voice as an authentication method without relying in centralized Big Tech ML servers. There is a Thai data scientist worked one this one alongside the team.
- [Ridepool sharing](https://github.com/pngwaritwg/PSI_ridepooling_matching), research on improvement on "the standard two-party PSI (2P PSI)" with ridepooling matching as use case

![Demo 2](https://images.yuttakhanb.dev/invgarden-pitch-2.jpg)

It looks like a really serious hacker house, isn't it?

What if I tell you that there are even more . . .

## Activities

This is wild and has a lot of variety ranging from sports to full scale trip. It is even more wild when there is not only Invisible Garden hosted in Chiang Mai but 6 e.g. Shanhaiwoo, Megazu, Edge City Lanna. Some events are available for other hacker house residents too.

For me, I'm more of sport-acitivity person so I went to some sport stuff e.g. bouldering, running and frisbee. I also went to trip with new friends here too e.g. elephant santuary visit and market trip around Chiang Mai city

![Elephant](https://images.yuttakhanb.dev/invgarden-elephant.jpg)

![Frisbee](https://images.yuttakhanb.dev/invgarden-frisbee.jpg)

![Football](https://images.yuttakhanb.dev/invgarden-football.jpg)

## Conclusion

I will go quickly since it's more of random thoughts.

- It's one of the hacker house in Chiang Mai with laser focused on tech implementation and theory but also brought people to get closer, make connection, do more fun stuffs in the future
- This is another "just fuck it and dive" experience for me. I took some small review course on basic cryptography, more on zero-knowledge proof and tried building circuits, so this is more of clarification by on-site class. But for implementation, there are lots more to learn.
- There are few Thai tech program which will take this extreme (6-8 weeks of 5 days on workshops/working on project). So actually, this is new thing for me. I think it is because of the context itself e.g. target demographic or objectives which is different. I hope to see more of long term program like this in Thailand
- Many Thai participants are university students, added up with many constraints e.g. schedule which overlapped with examination. They still really determined, focused and tried to reap out the most with limited time (I even saw a guy asking to Dr. Guo after class for hours before dinner and made other fellow hungry lol).
- Life lesson: learn when to slow down the pace, stop, take deep breath, think of next move and move with direction (some people here told me to be a bit more chill).
- I think it is beginning the journey in this field and would love to do some side projects based on this.

And that's end of the line.

![Demo](https://images.yuttakhanb.dev/invgarden-front.jpeg)

Wait, I think I have one more thing for this blog.

## Extra: Appreciations

I would like to leave this space for a huge thanks to

- Organizers: [Leo](https://x.com/leolarav), [Xixi](https://x.com/Odyssey_Leexixi), [Rute](https://x.com/_rutefig), [Maggie](https://x.com/Magcunha), [Will](https://x.com/0xneves) for hosting this intensed but cozy Invisible Garden
- Fellow builders here, especially crewmate on projects: [John](https://x.com/OwnerOfJK), [Alok](https://x.com/surfer__05), [Kenil](https://x.com/KenilShahh) and Harold
- Fellow Thai participants which mostly from [ETHPadthai Web3 Bootcamp #1](https://www.facebook.com/ethpadthai/posts/pfbid031MYuVSEvnhTHZYvkM7giurom4WnQuFfwcxCrGzzW7sj9xQHQwANwx6BF61EpGaYxl). I appreciate you guys for continuing on exploring, learning and growing in this field
- brothers that bounded by actions, not blood. I won't tag but iykyk.

Hope to see you guys and in the future ❤️
