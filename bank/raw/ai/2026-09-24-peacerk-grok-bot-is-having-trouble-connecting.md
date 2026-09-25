---
id: 2026-09-24-peacerk-grok-bot-is-having-trouble-connecting
kind: article
title: Grok bot is having trouble connecting
source: "https://forum.cursor.com/t/grok-bot-is-having-trouble-connecting/172618"
author: Peacerk
published: 2026-09-22
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok bot is having trouble connecting
URL: https://forum.cursor.com/t/grok-bot-is-having-trouble-connecting/172618
Created: 2026-09-22T09:10:57.853Z

## Post #1 @Peacerk (2026-09-22T09:10:57.887Z)
Hi, I have recently installed the Grok bot on my Windows 11 pc, and it says “can’t reach your computer” and it is trying, and finally it says “Grok bot is having trouble connecting”. I have an AdGuard system. I disabled the protection for some time to check, but same problem.

## Post #2 @deanrie (2026-09-24T09:30:15.821Z)
Hey, thanks for the report. Good news: this isn’t a network issue, so AdGuard isn’t involved. You can safely turn protection back on. Your PC can reach our servers fine. The issue is different: the account you used to sign in to Grok Bot (the one on this forum) is currently on the Free plan, and it doesn’t have access to Grok Bot yet. Because of that, the server doesn’t create a computer for that account. The app then shows “can’t reach your computer” or “having trouble connecting”, but that wording is misleading and isn’t related to networking. There’s nothing to reset or restore here. What to do to make it work: Grok Bot is available on any paid individual plan or a Teams plan, and also if you link SuperGrok. There’s also a free 1-week trial. Plan details: Plans and billing | Cursor Docs Complete onboarding using the same email as in the app: Onboarding | Cursor Docs . You can start the trial or pick a plan there. If you have a SuperGrok subscription, you can link it to the same email. After that, fully quit Grok Bot from the system tray (right-click the icon &gt; Quit), then reopen it and sign in again. If you already paid for something but the page still doesn’t show your plan, tell me where you paid and which email got the receipt, and we’ll figure out which account it landed on.
