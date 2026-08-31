---
id: 2026-08-31-olivier-guilloux-grok-bot-zoom-plugin-oauth-hardcodes
kind: article
title: "Grok Bot Zoom plugin OAuth hardcodes http://localhost:8787/callback — Zoom rejects hostname localhost (error 4700)"
source: "https://forum.cursor.com/t/grok-bot-zoom-plugin-oauth-hardcodes-http-localhost-8787-callback-zoom-rejects-hostname-localhost-error-4700/169991"
author: Olivier GUILLOUX
published: 2026-08-30
captured: 2026-08-31
via: grok-bot/Field
lane: grok-bot
status: raw
private: false
---

Olivier GUILLOUX: Connecting catalog Zoom plugin from Grok Bot always starts OAuth with redirect_uri=http://localhost:8787/callback. Zoom rejects hostname localhost (error 4700); Marketplace will not add localhost to the allow list (only 127.0.0.1, [::1], or HTTPS). Grok Bot has no parameter to change redirect URI. Recreating Zoom app does not help. Cursor docs already document https://www.cursor.com/agents/mcp/oauth/callback for Web and Cursor Agents (Zoom authorize then shows login). Grok Bot still behaves like desktop and forces localhost. Plugin stays needsAuth with 0 tools. Live probes: localhost → 4700; 127.0.0.1 and HTTPS agents callback → login HTML. macOS desktop; privacy mode. Staff Dean Rie (2026-08-30 17:23 UTC): diagnosed correctly; redirect not configurable; no workaround on user side; tracking switch to 127.0.0.1.
