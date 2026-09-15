---
id: 2026-09-15-huanl-grok-bot-is-stuck-on-reconnecting
kind: article
title: Grok Bot is stuck on Reconnecting — no Grok Bot access (SuperGrok inactive)
source: "https://forum.cursor.com/t/grok-bot-is-stuck-on-reconnecting-to-your-computer-and-cannot-connect-to-my-existing-bot-computer-since-september-14/171563"
author: huanl
published: 2026-09-14
captured: 2026-09-15
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot is stuck on "Reconnecting to your computer…" and cannot connect to my existing Bot computer since September 14
url: https://forum.cursor.com/t/grok-bot-is-stuck-on-reconnecting-to-your-computer-and-cannot-connect-to-my-existing-bot-computer-since-september-14/171563
created: 2026-09-14T03:57:13.953Z

--- @huanl 2026-09-14T03:57:13.981Z (#1) ---
Where does the bug appear (feature/product)?
Somewhere else…

Describe the Bug
What I tried:

Clicked Retry multiple times - no effect

Reset / Restore Grok Bot’s computer - failed

Switched to a mobile hotspot - still cannot connect

Fully quit and reopened the app

Additional info: grok.com web chat works fine on the same account and network. Only Grok Bot cannot connect, so it looks like the Bot computer instance is stuck. I can attach screenshots below.

Steps to Reproduce

Open Grok Bot and try to connect to my existing Bot computer

It gets stuck on “Reconnecting to your computer…” and never completes

Click Retry - no effect

Try “Restore Grok Bot’s computer” - reset fails

Try again from a mobile hotspot - still stuck

Expected Behavior
Grok Bot should reconnect to my existing Bot computer and resume the session as it did before September 14.

Screenshots / Screen Recordings
屏幕截图 2026-09-14 115045.png1033×752 62.2 KB

Operating System
Windows 10/11

Version Information
Grok Bot: Version: 0.20.0, Release Track: stable

Does this stop you from using Cursor
Sometimes - I can sometimes use Cursor

--- @deanrie 2026-09-14T06:36:03.237Z (#5) ---
Hey @huanl, thanks for the detailed report.

Good news: your Bot computer and saved Bots are fine, so it’s not a connection issue. The “Reconnecting to your computer…” message is misleading here. Please look at the banner at the bottom, above the input box: “Start a Grok Bot trial to send messages / This account can try Grok Bot now”. That’s the real status. Your account doesn’t currently have active Grok Bot access. That’s why Retry / Restore / Reset don’t help. They all send the same request.

Grok Bot access comes from an active paid Cursor plan (or Teams), or from an active linked SuperGrok subscription. On a free account, it’s usually SuperGrok, and it looks like it isn’t active right now.

What to check:

Open grok.com > Settings and see if your SuperGrok subscription is still active.

If it is active, make sure it’s the same Grok account linked to Cursor. You can check and re-link if needed at Sign in by signing in with your email.

If SuperGrok ended, you can get access back in one of three ways: renew SuperGrok, subscribe to Cursor Pro, or start the Grok Bot trial from the same onboarding page. The trial asks for a card for verification. If that step doesn’t work in your region, SuperGrok or Pro is the more reliable option.

As soon as the account has access again, the app will reconnect to your existing computer automatically. I wouldn’t wait too long on this.

Let me know what grok.com shows for SuperGrok and I’ll take a look further.
