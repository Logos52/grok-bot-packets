---
id: 2026-09-16-kostadin-s-grok-bot-android-all-bots-fail
kind: article
title: Grok Bot Android — all bots fail to generate after Reset; computer view works; weekly usage 72% (not capped)
source: "https://forum.cursor.com/t/grok-bot-android-all-bots-fail-to-generate-after-reset-computer-view-works-weekly-usage-72-not-capped/171735"
author: Kostadin_S
published: 2026-09-15
captured: 2026-09-16
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot Android — all bots fail to generate after Reset; computer view works; weekly usage 72% (not capped)
URL: https://forum.cursor.com/t/grok-bot-android-all-bots-fail-to-generate-after-reset-computer-view-works-weekly-usage-72-not-capped/171735
Created: 2026-09-15T11:17:47.221Z

## Post #1 @Kostadin_S (2026-09-15T11:17:47.252Z)
Where does the bug appear (feature/product)?
 Grok Bot

 Describe the Bug
 See ticket: T-F76591

 Where does the bug appear?

Grok Bot (Android). Desktop Grok Bot was closed for most of the incident. Same account.

Describe the bug

Every Bot fails to generate a reply. The shared Agent Computer desktop still opens and works.

Errors:

Bot failed to respond — Something went wrong while generating the reply. Try again.

Message not delivered — Something went wrong talking to your computer.

Couldn’t refresh — showing the last loaded messages

The red toast also appears as soon as the app opens, before a new send (on Master in the roster).

hello / Hi / status? fail on:

Master

Lingxi’s Engineer Bot

Site Audit

Hustle / CareerOps (previews show Hello, no reply)

Failed sends stay local (Retry). No request ID on Android toasts.

What still works

Agent Computer view: /workspace, Chrome, terminal box@cursor. OpenCode on that VM answered hi (~2026-09-13 16:00 ET).

Timeline

2026-09-13 ~15:17 ET — chat generation dies; computer view still up

Followed Sam (in-app): force-stop, one hello — still failed

Reinstalled Android app — error on launch

Later: Reset Agent Computer — same errors

2026-09-15 ~07:00 ET — still broken

Not weekly usage

Grok Bot → Settings → Usage: Weekly usage 72%, resets in 4 days (28% remaining).

 Cursor.com Overview on this email shows Cursor included usage 0% / reset Oct 13 — that is the IDE meter, not Grok Bot.

Already tried (no fix)

Force-stop / reopen Android

Reinstall app

hello on multiple bots and new sends

Agent Computer Reset

Did not keep hammering Reset after it failed to restore chat

In-app ticket with Sam (Sep 13); no follow-up after the hello test

Expected

A short hello gets a reply. App open does not toast a generation failure.

Request

Please inspect the chat generation / sendPrompt path for this account. Computer stream is healthy; Reset did not fix generation. Keep bots, history, and /workspace. Do not wipe again.

 Plan: SuperGrok / Grok Bot on this account

I can attach: roster toast, Engineer Bot not-delivered, Site Audit not-delivered

 Steps to Reproduce
 Send Hello to a bot

 Expected Behavior
 Computer reaches and replies to bots

 Operating System
 Windows 10/11

 Version Information
 Latest version of Android and Windows app

 Additional Information
 See ticket for screenshots.

 Does this stop you from using Cursor
 Yes - Cursor is unusable

## Post #5 @deanrie (2026-09-15T11:54:45.765Z)
Hey, thanks for the detailed report. Your diagnosis is spot on.

 You’re right on both points. It’s not your weekly usage, and it’s not the Android app. The issue is on the cloud computer that runs all your bots. It lost the ability to reach our backend in the second half of September 13, so every bot stopped generating replies, even though the computer’s desktop view still works. Both the Update from your phone and the later Reset were rejected or timed out on our side. So you didn’t break anything, and there’s nothing you can do on your side to fix it.

 I’ve passed your account to the team so they can restore access or move you to a fresh computer while keeping your data. Your bots, chats, and /workspace are still there, and we have a recent backup. While the team is working, please don’t run Reset or Update, and don’t reinstall the app.

 We’ll reply here once everything’s ready. After that, please do this: fully close the Android app, open it again, and send a short “hello” to the Master bot.

## Post #7 @Colin (2026-09-15T11:57:44.574Z)
Hey there @Kostadin_S

 Please restart Grok Bot and try again!
