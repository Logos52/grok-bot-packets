---
id: 2026-09-05-remi-grokbot-fails-after-update-cant-reach
kind: article
title: "Grokbot fails after update: Can't reach your computer"
source: "https://forum.cursor.com/t/grokbot-fails-after-update-cant-reach-your-computer/170438"
author: _Remi
published: 2026-09-03
captured: 2026-09-05
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grokbot fails after update: Can't reach your computer

URL: https://forum.cursor.com/t/grokbot-fails-after-update-cant-reach-your-computer/170438

Created: 2026-09-03T08:44:48.787Z

## Post 1 — @_Remi (2026-09-03T08:44:48.884Z)

Describe the Bug
After updating to 0.36.0: messsag Can't reach your computer

Options ‘Retry’ or ‘Recover computer’ fail.

There was no  change in my network; similar bugreports suggest nslookup and subsequent modification of network settings, but lookup results seem fine.

Steps to Reproduce
Update to 0.36.0

Expected Behavior
Loading bots normally

Screenshots / Screen Recordings

  Cursor DNS lookup.png405×573 14.7 KB

Operating System
Windows 10/11

Version Information
Grok Bot 0.36.0

Does this stop you from using Cursor
No - Cursor works, but with this issue

## Post 7 — @deanrie (2026-09-03T09:44:37.012Z)

Hey, thanks for the report. Good news: your computer and bots are OK and reachable. The issue isn’t with them or with your network.

What happened: the Grok Bot desktop app is still using a login session from before you changed your Cursor password on September 2. Changing your password ends all existing sessions, so every request from the app gets rejected after that, and it shows it as “Can’t reach your computer”. The update to 0.36.0 just installed on top of that and isn’t the cause. Your DNS is fine too.

To fix it, sign out in the desktop app and sign back in:

In Grok Bot, click your name or avatar in the bottom left of the sidebar.
Select Sign out and confirm.
Sign in again with your Cursor account using the new password.
Wait about a minute after signing in. The bots should load.

If you don’t see Sign out in that menu, right-click the Grok Bot icon in the system tray, choose Quit, reopen the app, and try again. You don’t need Recover computer or Reset here. The computer itself is fine.

Let me know if it still won’t connect after you sign in again.

## Post 9 — @_Remi (2026-09-03T10:21:22.404Z)

Signing out and signing in again resolved my problem.

It might be helpfull to automatically log out in such case and show the user he/she should login again.

Thanks!

Remi
