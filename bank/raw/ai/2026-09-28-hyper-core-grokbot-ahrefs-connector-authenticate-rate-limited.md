---
id: 2026-09-28-hyper-core-grokbot-ahrefs-connector-authenticate-rate-limited
kind: article
title: GrokBot - Ahrefs connector Authenticate rate-limited 429 / SyntaxError (Colin; related 170891)
source: "https://forum.cursor.com/t/grokbot-ahref-connector-rate-limited/173206"
author: hyper_core; Colin
published: 2026-09-28
captured: 2026-09-28
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# GrokBot - Ahref connector rate-limited
- id: 173206
- url: https://forum.cursor.com/t/grokbot-ahref-connector-rate-limited/173206
- created: 2026-09-28T11:01:11Z (UTC)
- last: 2026-09-28T13:18:33Z
- tags: [{'id': 416, 'name': 'grok-bot', 'slug': 'grok-bot'}]
- posts: 2
- staff: ['Colin']

## #1 hyper_core · 2026-09-28T11:01:11Z
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Can not connect to Ahref using marketplace connector. Throws SyntaxError with rate-limit reasons Steps to Reproduce Goto your grokbot account Select marketplace, search for Ahref connector Add connector, wait for Authenticate button to appear Press “Authenticate” Get Error string at bottom Expected Behavior Connector should be able to authenticate and get added properly. No SyntaxError should occur as well Screenshots / Screen Recordings Screenshot 2026-09-28 152538.png 759×653 23.6 KB Operating System Windows 10/11 Version Information Version: 0.61.0 Built: 2026-09-26T22:07:58.825Z Release Track: stable OS: win32 Does this stop you from using Cursor No - Cursor works, but with this issue

## #6 Colin [STAFF] · 2026-09-28T13:18:33Z
Hey @hyper_core , thanks for the report. This is a known issue we’re already tracking, and I’ve added your report to it. Ahrefs is rate limiting the setup requests Grok Bot sends before the Ahrefs sign-in page opens, so pressing Authenticate fails right away with that 429 message. The “SyntaxError” part is just the error text from Ahrefs not being formatted the way the app expects. The underlying problem is the rate limit. It’s not something you can fix on your side. Reinstalling the connector, adding another account, or retrying won’t get past it right now.
