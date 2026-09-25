---
id: 2026-09-24-sonya-phillips-grok-bot-android-login-stuck-on
kind: article
title: Grok Bot Android Login Stuck on Waiting for Browser
source: "https://forum.cursor.com/t/grok-bot-android-login-stuck-on-waiting-for-browser/172774"
author: Sonya_Phillips
published: 2026-09-23
captured: 2026-09-24
via: grok-bot/Field
lane: ai
status: raw
private: false
---

# Grok Bot Android Login Stuck on “Waiting for Browser”
URL: https://forum.cursor.com/t/grok-bot-android-login-stuck-on-waiting-for-browser/172774
Created: 2026-09-23T12:19:45.201Z

## Post #1 @Sonya_Phillips (2026-09-23T12:19:45.238Z)
Where does the bug appear (feature/product)? Grok Bot Describe the Bug Hello Cursor / Grok Bot support, I can use Grok Bot successfully on my Chromebook, but I cannot complete login in the Grok Bot Android app. Device: Samsung Android phone Grok Bot app version: 1.11.1 Cursor account email: sonyaphillips56@gmail.com When I tap Log In or Sign Up, the browser opens the Cursor/Grok Bot authentication flow. I successfully sign in and the browser says “All set! Feel free to return to Grok Bot.” It then prompts me to open Grok Bot. When I return to the Grok Bot app, it stays stuck indefinitely on “Waiting for Browser…” and never completes the login. I have already tried multiple fresh login attempts, force-stopping and reopening the app, restarting, confirming Open supported links is enabled, and returning to Grok Bot through the browser prompt. The same loop happens every time. Grok Bot works correctly on my Chromebook. The problem is specifically the Android browser-to-app authentication / deep-link callback. Please tell me how to fix this so I can use my existing Grok Bot account, Bots, and conversations on my Android phone. Thank you, Sonya Phillips Steps to Reproduce Tap Log In or Sign Up in the Grok Bot Android app, sign in through the browser authentication flow, follow the browser prompt to open Grok Bot, and return to the app. Operating System Other Version Information Grok Bot app version: 1.11.1 Device: Samsung Android phone Does this stop you from using Cursor No - Cursor works, but with this issue

## Post #2 @mohitjain (2026-09-24T06:45:58.534Z)
Hey @Sonya_Phillips , The usual fix on Samsung is to stop the phone from sleeping the app mid sign-in: Settings &gt; Apps &gt; Grok Bot &gt; Battery, set it to Unrestricted. Settings &gt; Battery and device care &gt; Background usage limits, and make sure Grok Bot isn’t under Sleeping / Deep sleeping apps. Then sign in again, and the moment the browser says “All set!”, switch straight back to Grok Bot with the Recent apps button. If it still hangs and your default browser is Samsung Internet, set Chrome as your default just for the sign-in and try once more. If that still doesn’t get you in, tell me your default browser and whether Grok Bot was in the Sleeping apps list, and I’ll dig further.
