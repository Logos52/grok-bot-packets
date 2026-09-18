---
id: 2026-09-15-serene-thornton-grok-bot-windows-chat-blank-weekly
kind: article
title: Grok Bot Windows chat blank / weekly usage limit silent costume
source: "https://forum.cursor.com/t/grok-bot-windows-chat-then-blank-computer-preview-works-please-recover-agent-computer/171615"
author: Serene_Thornton
published: 2026-09-14
captured: 2026-09-15
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot Windows — chat ... then blank; computer preview works; please recover Agent Computer
url: https://forum.cursor.com/t/grok-bot-windows-chat-then-blank-computer-preview-works-please-recover-agent-computer/171615
created: 2026-09-14T13:08:46.195Z

--- @Serene_Thornton 2026-09-14T13:08:46.228Z (#1) ---
Where does the bug appear (feature/product)?
Grok Bot

Describe the Bug
Every message to LEO or Adam fails the same way: a … appears, then the reply vanishes. No completed bot message.

The Agent Computer preview works. I can see the desktop, Chrome, and Dropbox. Bots and chat history are still in the sidebar. Adam stayed on “IN PROGRESS — Credentialing” after that job was idle.

This is not a local network or app-update problem. Grok.com chat works. Grok Bot chat does not.

Started Sunday afternoon 13 Sep 2026. Still broken Monday 14 Sep 2026.

Also emailed hi@cursor.com with the same report.

Please recover the Agent Computer on the backend. Do not wipe bots, files, or Dropbox logins.

Steps to Reproduce
Open Grok Bot on Windows.

Open Adam or LEO.

Send hi or Stop now.

See … then nothing.

Expected Behavior
The bot should complete a reply in chat. Computer preview and chat should both work.

Screenshots / Screen Recordings
Screenshot 2026-09-14 085534.png1920×1032 94.8 KB

Operating System
Windows 10/11

Version Information
Version 0.47.0

For AI issues: which model did you use?
Grok Bot default (LEO / Adam)

Additional Information
Already tried: sign out/in, tray Quit, new chat, Stop now, Update greyed out, Recover not offered, Reset Agent Computer (desktop came back; chat still dies). Same failure on phone earlier.

Does this stop you from using Cursor
No - Cursor works, but with this issue

--- @deanrie 2026-09-14T13:25:14.266Z (#5) ---
Hey, thanks for the detailed report and screenshot. I can see the Adam/LEO conversation and the stuck status IN PROGRESS - Credentialing.

First, the key point: your Agent Computer is fine. You don’t need to restore or reset anything. Your bots, files, chat history, and Dropbox login are still there. Don’t run Reset again. It won’t fix this, and it can actually cost you the Dropbox login and files you’re trying to keep. The fact that the desktop came back after Reset but the chat was still silent is a sign the issue isn’t with the box.

What’s actually happening: it looks like the account hit the weekly Grok Bot usage limit. After that, every message to LEO or Adam gets rejected before the bot can reply. That’s why you see … and then nothing. At this point the app should show a clear notification that you’ve hit the limit, but right now it doesn’t. This is a known issue we’re tracking.

What you can do:

Open Grok Bot Settings > Usage in the app. You’ll see the exact remaining usage and when the weekly limit resets.

If you don’t want to wait for the reset, enable on-demand usage at cursor.com/dashboard under the same account you use for Grok Bot. The bots should pick it up right away.

Once usage is back, just send Adam or LEO a new message. The IN PROGRESS - Credentialing status will update on the next reply. It’s stuck right now not because a task is stuck, but because no turn has completed.

For the future: when bots keep handing tasks back and forth, usage gets consumed much faster. If you give the work to one bot instead of bouncing it between them, the limit lasts a lot longer.

Let me know if the issue still doesn’t change after the usage reset or after you enable on-demand usage.
