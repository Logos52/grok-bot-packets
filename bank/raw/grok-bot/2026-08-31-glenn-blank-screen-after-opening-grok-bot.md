---
id: 2026-08-31-glenn-blank-screen-after-opening-grok-bot
kind: article
title: Blank screen after opening Grok Bot
source: "https://forum.cursor.com/t/blank-screen-after-opening-grok-bot/169966"
author: Glenn
published: 2026-08-30
captured: 2026-08-31
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

Glenn (glenn0): After install, reopen shows Setting up Grok Bot's Computer then blank. 0.28.0 then 0.30.0; hotspot no help; Windows PC on same account works. Staff Dean Rie: blank usually cannot reach cloud computer; try update + hotspot/DNS. OP found Cloudflare WARP on the Mac was the cause. Staff: WARP intercepts Grok Bot traffic (why hotspot didn't help); turn off WARP or split-tunnel/exclude Grok Bot routes.
