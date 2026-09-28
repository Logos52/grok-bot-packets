---
id: 2026-09-26-joe-levy1-grok-bot-computer-use-agents-stall
kind: article
title: Grok Bot computer-use agents stall — new message restarts helper (Colin)
source: "https://forum.cursor.com/t/grok-bot-computer-use-agents-stall-and-fail-to-complete-simple-tasks/173037"
author: Joe_Levy1; Colin
published: 2026-09-26
captured: 2026-09-26
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot computer-use agents stall and fail to complete simple tasks
URL: https://forum.cursor.com/t/grok-bot-computer-use-agents-stall-and-fail-to-complete-simple-tasks/173037
created: 2026-09-26T07:01:12.323Z

## Post 1 @Joe_Levy1 · 2026-09-26T07:01:12.427Z
Describe the Bug

Product: Grok Bot – Agent Computer / Computer Use

My Grok Bot’s computer is working normally and is accessible. However, when I assign tasks that require interacting with the computer, the bot performs a few clicks or actions and then stops making meaningful progress.

Simple tasks that should take only a few minutes can take hours or remain unfinished. The problem is not that the computer is unreachable; the bot can initially control it but fails to complete the assigned work.

Please investigate whether this is related to the computer-use agent, task execution, tool-call handling or a stalled agent runner.

I can provide request IDs, screenshots and examples of failed tasks if needed.

Steps to Reproduce

The bot begins executing tasks but stalls or becomes extremely slow, leaving tasks incomplete.

Expected Behavior

The bot should continue executing computer actions until the task is completed or report a specific error if it cannot proceed.

Operating System

Windows 10/11

Version Information

1.12.0 (308)

For AI issues: add Request ID with privacy disabled

Bot Id: 96b8522f-4d6d-4c3f-8f69-3d9e7ad77202

Does this stop you from using Cursor

No - Cursor works, but with this issue

## Post 5 @Colin [staff] · 2026-09-26T15:14:58.851Z
Hey
@Joe_Levy1
, thanks for the report!

I looked at your bot and the computer itself is healthy, and each click or keystroke completes in a few seconds. What’s slowing things down is how the work gets handed off. For computer tasks, your bot hands the job to a separate computer-use helper that keeps working in the background after the chat reply. When a new message arrives while that helper is still working, the bot tends to stop it and start over, so the task never gets far.

I can provide request IDs, screenshots and examples of failed tasks if needed.

That would be very helpful!

## Post 7 @Joe_Levy1 · 2026-09-26T15:40:30.267Z
Hi Colin

Thank you for getting back to me. I actually was not able to pull the request ID and the screenshot are not going to help much.

Yes the computer looks healthy and responsive but the bot is not able to complete simple tasks and looks like it stopped working. I have compared this with other solutions and it looks very unresponsive. I’m also familiar with browser use tool and it looks the bot forgets about the task until I ask for progress and that’s when it does one more thing and then stops again. Publishing a simple X post was about 1 hour when I was already logged in on the session. After sending this message I created another bot within Grok Bot and asked a simple question to look for a flight at
united.com
 and was not able to complete the task after 20 minutes. It was not even able to do a simple search. I’m worried not only because I moved all my flows to Grok Bot and that took me more than 1 week but also because it has been consuming a good chunk of my super grok plus weekly limit without completing the tasks (the main issue I found is managing the browser the rest works very good).

I really appreciate your help on this. I have updated to the latest version for the computer and grok desktop and is still happening.

Joe
