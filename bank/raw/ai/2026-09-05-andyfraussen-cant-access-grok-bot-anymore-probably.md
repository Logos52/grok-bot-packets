---
id: 2026-09-05-andyfraussen-cant-access-grok-bot-anymore-probably
kind: article
title: Can't access Grok Bot anymore, probably after updating to 0.39.0
source: "https://forum.cursor.com/t/cant-access-grok-bot-anymore-probably-after-updating-to-0-39-0/170568"
author: andyfraussen
published: 2026-09-04
captured: 2026-09-05
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Can't access Grok Bot anymore, probably after updating to 0.39.0

URL: https://forum.cursor.com/t/cant-access-grok-bot-anymore-probably-after-updating-to-0-39-0/170568

Created: 2026-09-04T09:53:23.429Z

## Post 1 — @andyfraussen (2026-09-04T09:53:23.484Z)

Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Suddenly I can’t access Grok Bot anymore. I think updating might have caused it, but I am not sure. Can’t access it on iOS app either. Tried VPN or with mobile network, same problem. Retry connecting, Update Grok Bot’s Computer or Reset Grok Bot’s Computer from desktop app settings also doesn’t work.

I can see multiple threads here, so I think it might be a common issue. I followed one of the steps (enabled Privacy Mode, but did not fix it for me).

Steps to Reproduce
iOS, Mac App.

With VPN, without VPN.

On mobile network, on local WiFi.

Can’t connect on any of them.

Operating System
MacOS

iOS

Version Information
Grok Bot on Mac Version 0.39.0

Does this stop you from using Cursor
No - Cursor works, but with this issue

## Post 5 — @Colin (2026-09-04T12:42:19.519Z)

Hey @andyfraussen, thanks for the report, and sorry for the trouble.

Good news first: your computer and your bots are fine. They are still running on our side, and a couple of routines even completed this morning. The apps just cannot reach them because they are no longer signed in.

From our side it looks like the sessions on your account were revoked from the Active Sessions list on cursor.com this morning (around 07:25 UTC). Revoking sessions signs out every device, including the Grok Bot desktop app and the iOS app. Those apps are still holding on to the old sign-in, and instead of asking you to sign in again they show it as a connection problem. That is also why Retry, Update and Reset do nothing, and why VPN or mobile data made no difference. The 0.39.0 update landed after this had already started and is not the cause.

To fix it, sign out and back in on each device:

In Grok Bot on your Mac, click your name / avatar at the bottom left of the sidebar.
Choose Sign out and confirm.
Sign in again with the same account (Sign in with Grok, andy@fraussen.dev).
Wait a minute after signing in. Your bots should load.
On your iPhone, open Grok Bot, go to Settings, sign out, then sign back in with the same account.

If you cannot find a Sign out option on the Mac, quit Grok Bot completely (right-click its Dock icon and choose Quit), reopen it and try again.

Enabling Privacy Mode was not needed for this and did not cause it, so set it however you prefer. Let me know if either device still does not connect after signing back in!

## Post 7 — @andyfraussen (2026-09-04T12:48:26.962Z)

It is solved, thank you.

## Post 8 — @Liam_Serour (2026-09-04T18:22:21.558Z)

I am having a similar issue. Except mine cannot connect to the cloud computer now. and after exiting and resigning in, all my agents are gone… Help please
