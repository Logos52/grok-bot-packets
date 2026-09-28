---
id: 2026-09-27-noah1-colin-grokbot-1password-long-website-url-kills
kind: article
title: Grokbot & 1Password — long website URL kills vault connect
source: "https://forum.cursor.com/t/grokbot-1password/173142"
author: Noah1; Colin
published: 2026-09-27
captured: 2026-09-27
via: grok-bot/Field
lane: ai
status: raw
private: false
---

--- @Noah1 post 1 2026-09-27T18:54:30.031Z ---
Been trying to connect Grokbot and 1Password for days now through the official connector, it creates the bot but won’t let me connect.
I’ve tried service accounts, other methods. Keep getting this “credential delivery method is unknown”
If I go to 1password, it shows it tried to connect and created something but never works!
Any ideas?
Screenshot 2026-09-27 at 2.53.31 PM1628×794 42.4 KB
Screenshot 2026-09-27 at 2.53.00 PM1848×1422 152 KB

--- @system post 2 2026-09-27T18:54:37.486Z ---
Hi there!
We detected that this may be a bug report, so we’ve moved your post to the Bug Reports category.
To help us investigate and fix this faster, could you edit your original post to include the details from the template below?

Bug Report Template - Click to expand
Where does the bug appear (feature/product)?

 Editor, Tab & Chat (autocomplete, Composer, in-editor agent)
 Terminal & commands
 Models, pricing & API keys (availability, Auto/Max, BYOK/Bedrock)
 MCP & tools
 Cloud Agents & Automations (cursor.com/agents, scheduled/event)
 BugBot & Code Review
 Cursor CLI
 Cursor Mobile
 Remote (SSH / Dev Containers / WSL)
 Account, billing & login
 Something else…

Describe the Bug
A clear and concise description of what the bug is.

Steps to Reproduce
How can you reproduce this bug? We have a much better chance at fixing issues if we can reproduce them!

…
…
…

Expected Behavior
What is meant to happen here that isn’t working correctly?

Screenshots / Screen Recordings
If applicable, attach images or videos (.jpg, .png, .gif, .mp4, .mov)

Operating System

 Windows 10/11
 MacOS
 Linux

Version Information

For Cursor IDE: Menu → About Cursor → Copy
For Cursor CLI: Run agent about in your terminal

IDE:
Version: 2.xx.x
VSCode Version: 1.105.1
Commit: ......

CLI:
CLI Version 2026.01.17-d239e66

For AI issues: which model did you use?
Model name (e.g., Sonnet 4, Tab…)

For AI issues: add Request ID with privacy disabled
Request ID: f9a7046a-279b-47e5-ab48-6e8dc12daba1
For Background Agent issues, also post the ID: bc-…

Additional Information
Add any other context about the problem here.

Does this stop you from using Cursor?

 Yes - Cursor is unusable
 Sometimes - I can sometimes use Cursor
 No - Cursor works, but with this issue

The more details you provide, the easier it is for us to reproduce and fix the issue. Thanks!

--- @Colin post 8 2026-09-27T19:55:49.659Z ---
Hey @Noah1, thanks for the report and the screenshots!
We looked into it. The connection is failing because one of the logins in the vault you’re sharing with Grok Bot has an extremely long website address saved on it (over 2,000 characters, usually a sign-in link with a long redirect or tracking string copied from the address bar). Right now that one item stops the whole connection, and the app only shows the generic “delivery outcome is unknown” message. I’ve flagged this to the team.
In the meantime, this should get you connected:

In 1Password, open the “Shared with Grok Bot” vault (or whichever vault you picked when connecting).
Go through the Login items and look at each item’s website field. Find any with a very long address.
Edit that website down to just the site’s normal address (for example https://example.com) and save.
Fully quit Grok Bot with Cmd+Q. Closing the window isn’t enough, since the connect dialog stays blocked until the app restarts.
Reopen Grok Bot and click Connect 1Password again.

If you can’t spot the item, move everything out of that vault temporarily, connect with the empty vault, then move the items back in.
Also, each failed attempt created a leftover service account named “Grok Bot agents” plus a date in your 1Password account. You can safely delete the extra ones in 1Password.com under Developer, then Service Accounts.
Let me know if it still fails after that!

--- @Noah1 post 14 2026-09-27T20:13:16.762Z ---
Interesting! I don’t see anything weird like that, but removing everything worked and allowed me to connect, now I’ll slowly move things back in.
Thanks so much for that!

--- @Noah1 post 15 2026-09-27T20:22:09.288Z ---
Colin:

Hey @Noah1, thanks for the report and the screenshots!
We looked into it. The connection is failing because one of the logins in the vault you’re sharing with Grok Bot has an extremely long website address saved on it (over 2,000 characters, usually a sign-in link with a long redirect or tracking string copied from the address bar). Right now that one item stops the whole connection, and the app only shows the generic “delivery outcome is unknown” message. I’ve flagged this to the team.
In the meantime, this should get you connected:

In 1Password, open the “Shared with Grok Bot” vault (or whichever vault you picked when connecting).
Go through the Login items and look at each item’s website field. Find any with a very long address.
Edit that website down to just the site’s normal address (for example https://example.com) and save.
Fully quit Grok Bot with Cmd+Q. Closing the window isn’t enough, since the connect dialog stays blocked until the app restarts.
Reopen Grok Bot and click Connect 1Password again.

If you can’t spot the item, move everything out of that vault temporarily, connect with the empty vault, then move the items back in.
Also, each failed attempt created a leftover service account named “Grok Bot agents” plus a date in your 1Password account. You can safely delete the extra ones in 1Password.com under Developer, then Service Accounts.
Let me know if it still fails after that!

Great support! All fixed!
