---
id: 2026-09-14-enescanguven-token-not-available-in-grok-bot
kind: article
title: Token Not Available in Grok Bot Environment
source: "https://forum.cursor.com/t/token-not-available-in-grok-bot-environment/171441"
author: enescanguven
published: 2026-09-12
captured: 2026-09-14
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Token Not Available in Grok Bot Environment
URL: https://forum.cursor.com/t/token-not-available-in-grok-bot-environment/171441
created: 2026-09-12T16:05:43.669Z

## @enescanguven · 2026-09-12T16:05:43.699Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug I’m having an issue with Grok Bot where the token appears to be saved successfully, but it is not available inside the execution environment. The token field shows that it has been saved, but when the executor starts a fresh process, the token is still missing/not accessible. As a workaround, I currently have to provide the token as a file, similar to the GSC setup. Steps to Reproduce Add the token in the token field. Save it successfully. Check the environment for the token. The token is missing/not accessible. Expected Behavior Expected behavior: Once the token is saved, it should be available to the executor in new processes. Operating System iOS Version Information Version: 0.47.0 Release Track: stable OS: darwin Does this stop you from using Cursor Sometimes - I can sometimes use Cursor

## @Colin · 2026-09-13T07:57:56.981Z
Hey @enescanguven , thanks for the report. We can see what is happening on your Grok Bot computer. The token you save through the secure card is stored correctly and is added to the computer’s main environment, but agents that run in their own window on that computer start their shell processes from a separate session that does not pick up values added after that session started. That is why the card says Saved while the executor’s new process cannot see it. This is a known issue and I have added your report to it. Two things that should work in the meantime: After saving the token, create a brand new agent and give it the task. A fresh agent’s session inherits everything saved before it started, so the variable should be there. Keep doing what you are doing with the file, the way you set up GSC. Files on the computer are visible to every agent. Re-saving the same token in an existing agent will not help, so no need to keep re-entering it!

## @enescanguven · 2026-09-13T12:07:51.393Z
The second workaround works better for me since I don’t want to lose my existing agent history. Would it be possible to update this thread, or publish a bug fix/update, once this issue is resolved? Thanks!
