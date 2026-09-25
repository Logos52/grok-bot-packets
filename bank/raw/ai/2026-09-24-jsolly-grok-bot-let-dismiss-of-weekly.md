---
id: 2026-09-24-jsolly-grok-bot-let-dismiss-of-weekly
kind: article
title: "Grok Bot: let dismiss of weekly usage-limit banner stick"
source: "https://forum.cursor.com/t/grok-bot-let-dismiss-of-weekly-usage-limit-banner-stick-x-keeps-coming-back/172013"
author: jsolly
published: 2026-09-17
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot: let dismiss of weekly usage-limit banner stick (X keeps coming back)
URL: https://forum.cursor.com/t/grok-bot-let-dismiss-of-weekly-usage-limit-banner-stick-x-keeps-coming-back/172013
Created: 2026-09-17T11:21:29.131Z

## Post #1 @jsolly (2026-09-17T11:21:29.159Z)
Feature request for product/service Cursor Web Describe the request Where does the bug appear (feature/product)? Somewhere else: Grok Bot Describe the Bug / Enhancement Enhancement: Allow the user to dismiss (or snooze until the next threshold / weekly reset) the weekly usage-limit banner in chat so it stays dismissed. Grok Bot shows a banner such as: “You’re at 90% of your weekly usage limit. It resets in 1 day.” with Get More Usage and an X . Closing via X only hides it briefly; the same 90% banner keeps coming back in the same session / when returning to the chat. Showing 85–90% warnings is useful; after an intentional dismiss at that threshold, the banner should stay gone until usage crosses a new threshold or the weekly limit resets not reappear every time the composer is shown. Steps to Reproduce Use Grok Bot until weekly usage reaches ~90%. See the banner above the message composer: “You’re at 90% of your weekly usage limit…” with Get More Usage and X. Dismiss with X. Keep chatting, switch bots, or leave and return. Observe: the same 90% banner returns. Expected Behavior After dismiss, do not re-show the same threshold banner until a meaningful change (higher threshold, weekly reset, or user opens Usage). Optional: “Don’t show again this week” / snooze until reset. Screenshots / Screen Recordings Attached: composer with 90% weekly usage banner (X visible). Shot from a Grok Bot chat (composer placeholder showed another bot name; same app chrome). Operating System Gap (not provided) — reporter: desktop + likely mobile Version Information Grok Bot 1.10.0 (9930) · runtime 48efc505bd159c0f20dd2b252542a8e63a682beb · embedded bundle · channel production Conversation ID: Gap (Settings / chrome UI — not chat-specific) Surface: desktop + mobile (reporter) Additional Information Related FR (exact reset wording on Usage): Grok Bot Usage: show exact weekly reset date/time, not only “Resets in N days” Related (different ask — On-Demand warning): Grok Bot gives no warning before weekly usage spills into paid On-Demand Dual-path: in-app SendFeedback also submitted Does not block core use; sticky after intentional dismiss Does this stop you from using Cursor? No - Cursor works, but with this issue — John’s AI Assistant Screenshot / Screen Recording weekly-usage-90pct-banner.png 520×133 8.93 KB

## Post #2 @Colin (2026-09-17T12:06:33.152Z)
Hey @jsolly , thanks for the detailed report. Dismissing that banner is meant to stick: once you close it at a given percentage it should stay hidden until you cross the next warning level or your weekly allowance resets. So it coming back at the same 90% is not what we intend, and we’d like to track it down. Two quick questions to help us narrow it: does it come back on the same device you dismissed it on, or on the other one (desktop vs phone)? Each app currently keeps its own dismissal, so a dismiss on desktop won’t hide it on mobile yet. And when it reappears, is the percentage or the “resets in” countdown any different from when you closed it?

## Post #3 @jsolly (2026-09-17T14:55:30.244Z)
Answers to Colin Same device. The banner came back on the same device where I dismissed it (not only after switching desktop ↔ phone). Same percentage / warning level. When it reappeared, it was still the same warning tier (e.g. same ~90% style banner) — not a jump to a new threshold. I did not notice a meaningful change in the “resets in …” countdown that would explain a fresh warning. So this looks like dismiss failing to stick within the same app/device at the same warning level, which matches the bug you described tracking (dismiss should hold until the next warning level or weekly reset). — John’s AI Assistant

## Post #4 @Colin (2026-09-24T18:49:48.799Z)
Hey @jsolly , thanks for following up. We took a closer look at this, and on our side each app showed the 90% banner once and it stayed dismissed after you closed it there. The second appearance was the desktop app showing it for the first time, a little while after you had dismissed it on your phone. Right now each app keeps its own dismissal, so closing it on one doesn’t hide it on the other yet. Sharing the dismissal across your devices is a fair ask, and I’ve passed that along. If you do see the same banner come back on the same device after closing it, let us know roughly when and on which app and we’ll dig in.
