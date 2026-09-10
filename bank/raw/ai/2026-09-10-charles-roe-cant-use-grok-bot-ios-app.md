---
id: 2026-09-10-charles-roe-cant-use-grok-bot-ios-app
kind: article
title: Can't use Grok Bot iOS App (125GB restore brick)
source: "https://forum.cursor.com/t/can-t-use-grok-bot-ios-app/171078"
author: Charles_Roe
published: 2026-09-08
captured: 2026-09-10
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Can’t use Grok Bot iOS App

- url: https://forum.cursor.com/t/can-t-use-grok-bot-ios-app/171078
- topic_id: 171078
- created_at: 2026-09-08T17:57:46.349Z
- author: Charles_Roe
- via: grok-bot/Field
- lane: ai
- deposited: 2026-09-10

## @Charles_Roe · 2026-09-08T17:57:46.446Z

Where does the bug appear (feature/product)? Cursor for iOS Describe the Bug When I open the app, it says connecting to computer but never loads. Steps to Reproduce Download Grok Bot for iOS Try to launch Grok Bot. Expected Behavior It should connect and load all my bots. Screenshots / Screen Recordings Operating System iOS Version Information 1.6.0 (8025) Does this stop you from using Cursor Yes - Cursor is unusable

## @deanrie [staff] · 2026-09-08T18:29:51.535Z

Hey, thanks for the report. It’s not your phone, your network, or your settings. Your Grok Bot computer can’t finish loading its saved data right now, and that’s why the app gets stuck on “connecting to computer”. This is an issue we’re tracking on our side, and I’ve already passed it to the team. You don’t need to do anything in the app right now. Reinstall, Recover, or Reset won’t change anything. One thing that could help us debug faster: did you recently save any large files (like videos) on the bot computer? If they’re not important, let me know. That might speed up the recovery. I’ll reply here as soon as the computer is back up.

## @Charles_Roe · 2026-09-08T18:45:13.775Z

Thanks Dean. Yes — any videos on that computer can be deleted. They’re not needed and I don’t need them recovered. Still stuck on iOS as of 18:59 BST. The app sits on “Connecting to your computer…” for a while, then drops to “Something went wrong” with Try Again. Force-quit, Wi-Fi/mobile data switch, and Try Again don’t get past it. No Recover button has appeared. iOS only on this account — Grok Bot 1.6.0 (8025). Happy for you to clear those files / finish the load from your side.

## @Charles_Roe · 2026-09-09T10:58:00.251Z

Hi Dean — just checking in. Still the same this morning (9 Sep, 11:57 BST). iOS Grok Bot 1.6.0 (8025) sits on “Connecting to your computer…”, then “Something went wrong / Try Again”. No Recover button. Videos on that computer can still be deleted. Happy to wait on your side — is there an ETA, or anything else you need from me?

## @Colin [staff] · 2026-09-09T15:33:25.028Z

Hey @Charles_Roe , I’ve spent some time looking into this, and here’s what I found: your Grok Bot computer is getting stuck during the data restore. It’s holding a very large amount of data (roughly 125 GB, including some large video files in its workspace), and the restore runs out of space before the last few files finish. As a result, the app never gets past “Connecting to your computer…”. Unfortunately, we aren’t able to surgically remove individual files from the computer. In the short term, until our engineers can dig into the problem, the only option available to us is a hard reset, but that would mean losing your existing bots. You mentioned that videos on the computer can be deleted, what about the existing bots?

## @Charles_Roe · 2026-09-09T21:42:48.194Z

Hi Colin — thanks for looking. Videos can be deleted. I want to keep the existing bots, so please don’t do the hard reset. Happy to wait until the engineers can free the space / finish the restore without wiping them. Let me know if you need anything else from me.
