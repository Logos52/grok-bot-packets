---
id: 2026-09-28-ajay-rao-grok-bot-bot-failed-to-respond
kind: article
title: Grok Bot - Bot failed to respond after update and reset - unpaid invoice pauses replies (deanrie)
source: "https://forum.cursor.com/t/grok-bot-bot-failed-to-respond-after-update-and-reset-please-rebind-agent-computer/173176"
author: Ajay_Rao; deanrie
published: 2026-09-28
captured: 2026-09-28
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot - Bot failed to respond after update and reset - please rebind agent computer
- id: 173176
- url: https://forum.cursor.com/t/grok-bot-bot-failed-to-respond-after-update-and-reset-please-rebind-agent-computer/173176
- created: 2026-09-28T05:03:10Z (UTC)
- last: 2026-09-28T05:35:10Z
- tags: [{'id': 416, 'name': 'grok-bot', 'slug': 'grok-bot'}]
- posts: 2
- staff: ['deanrie']

## #1 Ajay_Rao · 2026-09-28T05:03:10Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Account email - ajaysatishrao@gmail.com Platform: iOS and Mac OS Desktop App version: 1.12.0 (12804) Time Zone: IST Started: Around 11:30 pm on 27th September Error on every message: “Bot failed to respond. Sorry something went wrong while generating the reply. Try again” Already tried: full quit, app update, update computer, reset computer, usage not capped, new chat. Still fails on all bots. Please do not ask me to reset again. Please check agent computer / runtime replica for this account and rebind it. Bots, files and history should still be on your side. Steps to Reproduce I am not sure how to reproduce this bug Expected Behavior The bot should be functioning, none of them are responding Operating System MacOS Version Information Grok Bot version: 1.12.0 (12804) Does this stop you from using Cursor No - Cursor works, but with this issue

## #5 deanrie [STAFF] · 2026-09-28T05:35:10Z
Hey Ajay. Good news: you don’t need to restart anything or rebind anything. Your bots, files, and history are still there, and the agent computer itself is fine. When all bots stop replying at the same time, and reset, update, or new chat doesn’t help, it’s usually not a runtime issue. It’s more often something on the account side. For example, if your account has an unpaid payment or invoice, bot replies get paused until it’s paid. Unfortunately, the app shows a generic Bot failed to respond message instead of a clear payment message, so it can look like the computer is the problem. What to check first: Go to cursor.com/dashboard and sign in with the same account you use in Grok Bot. Open the billing section and check if there’s an unpaid invoice. If there is, pay it. If your card fails again, enable international or online payments in your banking app, or try a different card. After payment, replies usually come back within a couple of minutes. For anything specific to your account or the payment itself, our team at hi@cursor.com can look into your situation directly. Let me know if the bots are still silent after you pay, and we’ll dig deeper.
