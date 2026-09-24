---
id: 2026-09-24-gfp-grokbot-cant-connect-reset-failed-partial
kind: article
title: GrokBot can't connect (Reset failed / partial = no access)
source: "https://forum.cursor.com/t/grokbot-cant-connect/171703"
author: GFP
published: 2026-09-15
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grokbot cant connect
URL: https://forum.cursor.com/t/grokbot-cant-connect/171703
Created: 2026-09-15T06:56:31.479Z

## Post #1 @GFP (2026-09-15T06:56:31.505Z)
Launch grokbot on OSX cant connect to groks computer. Ive tried: Closing all vpn and malware scanning Closing and opening grokbot Uninstalling/reinstalling grokbot The desktop client throws the following errors: Cant reach your computer Reset/recovery just consistently fails Grok is having trouble connecting There is a connection issue somewhere but I cant find it. Anyone faced/solved this?

## Post #2 @system (2026-09-15T06:56:40.993Z)
Hi there! We detected that this may be a bug report, so we’ve moved your post to the Bug Reports category. To help us investigate and fix this faster, could you edit your original post to include the details from the template below? Bug Report Template - Click to expand Where does the bug appear (feature/product)? Editor, Tab &amp; Chat (autocomplete, Composer, in-editor agent) Terminal &amp; commands Models, pricing &amp; API keys (availability, Auto/Max, BYOK/Bedrock) MCP &amp; tools Cloud Agents &amp; Automations ( cursor.com/agents , scheduled/event) BugBot &amp; Code Review Cursor CLI Cursor Mobile Remote (SSH / Dev Containers / WSL) Account, billing &amp; login Something else… Describe the Bug A clear and concise description of what the bug is. Steps to Reproduce How can you reproduce this bug? We have a much better chance at fixing issues if we can reproduce them! … … … Expected Behavior What is meant to happen here that isn’t working correctly? Screenshots / Screen Recordings If applicable, attach images or videos (.jpg, .png, .gif, .mp4, .mov) Operating System Windows 10/11 MacOS Linux Version Information For Cursor IDE: Menu → About Cursor → Copy For Cursor CLI: Run agent about in your terminal IDE: Version: 2.xx.x VSCode Version: 1.105.1 Commit: ...... CLI: CLI Version 2026.01.17-d239e66 For AI issues: which model did you use? Model name (e.g., Sonnet 4, Tab…) For AI issues: add Request ID with privacy disabled Request ID: f9a7046a-279b-47e5-ab48-6e8dc12daba1 For Background Agent issues, also post the ID: bc-… Additional Information Add any other context about the problem here. Does this stop you from using Cursor? Yes - Cursor is unusable Sometimes - I can sometimes use Cursor No - Cursor works, but with this issue The more details you provide, the easier it is for us to reproduce and fix the issue. Thanks!

## Post #5 @GolfCarter (2026-09-19T16:03:46.520Z)
I have had intermitted issues the last two days. GrokBot simply stops working while in a conversation. Currently it is not responding on my MBPro (AppleM5, Golden Gate 27.0) and will not connect through my iPhone GrokBot app as well. This had never occured before GoldenGate was installed

## Post #6 @deanrie (2026-09-19T16:51:44.661Z)
Hey, thanks for the detailed report, and sorry it took so long to diagnose the network issue. This isn’t a network issue on your Mac, so VPN, antivirus, and reinstalling wouldn’t have helped. The cause is access: the account you’re signed into has already used up its free trial for Grok Bot, and it doesn’t have access to Grok Bot right now. Because of that, our servers reject the app’s requests, and the desktop app shows it as “Can’t reach your computer” and failed Reset/Recover attempts. The wording is misleading and we’re tracking this issue. To start working again, you need a plan that includes Grok Bot: any paid individual Cursor plan, Cursor Teams, or a linked eligible SuperGrok subscription. The access matrix is here: Plans and billing | Cursor Docs . After you subscribe, fully quit Grok Bot from the menu bar icon, reopen it, and sign in with the same account. Until access is restored, don’t click Reset/Recover. They won’t work while the account doesn’t have access to Grok Bot. If you have a paid Cursor plan or SuperGrok on a different account, tell me which email it’s under and I’ll check. @GolfCarter , yours looks like a different case. It worked before and now drops intermittently on both Mac and iPhone. To avoid mixing issues, please start a separate thread and include the Grok Bot version, your macOS version, and the Request ID from the failing session. That’ll help us look into it faster.

## Post #7 @GFP (2026-09-23T05:37:50.663Z)
Yeh I have been trying to upgrade thats what triggered the issue in the first place. Cursor have said - Those screenshots show Reset failed with a partial computer state, then Grok Bot stuck on trouble connecting, so this needs a teammate to inspect the computer state on the account. So upgrading seems to be irrelevant right now

## Post #8 @deanrie (2026-09-23T18:24:08.479Z)
Hey, let’s tie this together. This isn’t two different issues, it’s one. “Reset failed / partial computer state” and “no access / needs upgrade” are the same root cause. If your account doesn’t have active access to Grok Bot, the server rejects all computer requests. That’s why Reset/Recover consistently fail, and it shows up as a “stuck” or “partial” computer state. So the upgrade is relevant. Until access is active, you can’t rebuild the computer cleanly, and any teammate inspection will hit the same wall. Order is: access first, then a clean rebuild. A couple questions so I can understand where you are right now: Did the upgrade actually complete? On the account adam.abb***.com (or another one, tell me which), do you now have an active paid Cursor plan or a linked eligible SuperGrok subscription? If the payment or upgrade isn’t going through or didn’t apply, email hi@cursor.com and they’ll check your specific case. If the plan is already active but Grok Bot still shows “trouble connecting”, then it’s on us and we can check the computer state. For the second case, we need the Request ID from a failing session after access became active. Privacy Mode must be off. With that Request ID, the team can look up the computer state on the account. And like I said above, until access is active, don’t hit Reset/Recover, they won’t work. Let me know the answers to the points above and we’ll get it sorted.
