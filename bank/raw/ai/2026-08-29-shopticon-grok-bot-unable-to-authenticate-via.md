---
id: 2026-08-29-shopticon-grok-bot-unable-to-authenticate-via
kind: article
title: Grok Bot Unable To Authenticate via Gmail Plugin
source: "https://forum.cursor.com/t/grok-bot-unable-to-authenticate-via-gmail-plugin/169782"
author: Shopticon
published: 2026-08-28
captured: 2026-08-29
via: grok-bot/Field
lane: ai
status: raw
private: false
---

Grok Bot is unable to authenticate to Google accounts using the Gmail plug-in.

Steps: Install Grok Bot, add Gmail plugin, add an account, attempt to authenticate to a personal Google account.

Result: Error from Google: This app is blocked. The app tried to access sensitive info in your Google Account. To keep your account safe, Google blocked this access.

Workaround reported by OP: authenticate to a single account in Cursor using the local authentication method. No mechanism to authenticate to multiple Google accounts within Bot.

Colin (Cursor staff): authorizing Gmail from Cursor goes through a different authorization path that isn't affected, and the connection is shared with Grok Bot. On multiple accounts: once authorization from Grok Bot is working again, add more Google accounts from the Gmail plug-in's page in Grok Bot ("Add Another Account").

Jawaz Illavia: no paid Cursor account, same Google block, no workaround.

Amit Dekalo: Cursor settings workaround still not working; asked for ETA on direct plugin authorization.
