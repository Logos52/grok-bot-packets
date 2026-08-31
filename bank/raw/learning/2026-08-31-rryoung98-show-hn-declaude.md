---
id: 2026-08-31-rryoung98-show-hn-declaude
kind: article
title: "Show HN: Declaude"
source: "https://news.ycombinator.com/item?id=49443296"
author: rryoung98
published: 2026-08-26
captured: 2026-08-31
via: grok-bot/Field
lane: learning
status: raw
private: false
---

Title: Show HN: Declaude
Author: rryoung98
URL: https://speak-english.tenken.co/
Created: 2026-08-26T02:04:04.000Z

I had to develop a course related to quantum chemistry and unfortunately, Claude just kept writing it in its own very annoying claude-speak. It actually cost our team a lot of time and tokens to wrestle it to just speak like a normal human. We used skills, as well as initial prompts and subagents to make sure that all of the tics were gone, but there was one too many times where it just wouldn't fix itself despite telling it in the prior prompt! I made speak-english based off of  https://github.com/gvzdv/claudish-to-english/commits/main/  and it runs a qwen model on my gcp servers. It can convert documents or respond in-line in sessions with claude and I anticipate building a solution for prime-agent.
---
tsamuels: This is very cool! Claude says a lot of unnecessary things. It gets annoying.
---
DerrickDevo1: Super cool! This has been annoying me for quite a long time. Feels like Claude models’ natural language ability is squeezed out for the improvements of coding and reasoning. I think that’s why a weaker model can possibly do better in English. However, I was wondering if any skills or CLAUDE.md would help as a simpler alternative, by better context management and instructions?
