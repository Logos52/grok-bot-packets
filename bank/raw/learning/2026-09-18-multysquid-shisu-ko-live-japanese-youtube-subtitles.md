---
id: 2026-09-18-multysquid-shisu-ko-live-japanese-youtube-subtitles
kind: article
title: "Shisu-ko: live Japanese YouTube subtitles (Whisper) + Yomitan + one-key Anki mine"
source: "https://github.com/Multysquid/shisu-ko"
author: Multysquid
published: 2026-09-17
captured: 2026-09-18
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# Shisu-ko — Multysquid/shisu-ko
Source: https://github.com/Multysquid/shisu-ko
Created: 2026-09-17T23:40:05Z · pushed through 2026-09-18T00:20:25Z · MIT · ★1
Lane: education / immersion / generated-input / teach-once

Named runner: Shisu-ko — live Japanese subtitles for YouTube in Firefox, transcribed locally with Whisper, readable by Yomitan, one-key mine into Anki.

Problem: YouTube JA captions often missing, bad auto-gen, or burned-in (dictionary cannot reach). Shisu-ko runs Whisper large-v3 locally, transcribes ahead of playhead, renders as real DOM text over the player.

Portable loop:
1. Firefox addon on youtube.com posts video id + playhead to local server :8790
2. Server: yt-dlp audio → PyAV 16kHz mono → faster-whisper windows starting at playhead then ahead
3. Cues as ordinary DOM text → Yomitan scans; hover pauses video; leave popup resumes
4. Mine (button or Alt+Shift+M): screenshot + MP3 sentence clip → AnkiConnect attach to newest card OR Downloads folder
5. Cache per video in ~/.shisu-ko/cache so rewatch is instant

Model choice: large-v3 default; flag for kotoba-whisper-v2.0-faster (~6x JA) or small CPU. Native setup or Docker+GPU. Optional Anki/Yomitan — not required for live subtitles.

Distinct from ColinHouse/kotobako (Galgame/anime capture companion with FSRS-native cards): this is live YouTube Whisper→DOM→Yomitan→Anki mine, day-0 NEW URL 2026-09-17.
