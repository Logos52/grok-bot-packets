---
id: 2026-09-01-chokkarapu-akhil-vedai-pro-grade-rewritten-tutor-exit
kind: article
title: VedAI Pro — grade-rewritten tutor + exit-quiz resurface
source: "https://github.com/Akhil271-bot/Vedi-AI---Pro-"
author: Chokkarapu Akhil
published: 2026-08-27
captured: 2026-09-01
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# VedAI Pro — Voice-Enabled, Profile-Aware AI Tutor

A working prototype of a grade-adaptive AI tutor, built after auditing three gaps in existing EdTech AI chat products.

Most AI tutors answer a Class 3 student and a Class 12 student identically. VedAI Pro doesn't.

---

## The problems this so
| # | Gap observed | What VedAI Pro does |
|---|---|---|
| 1 | **Grade-blind responses** — same text for every student | System prompt rewrites itself per grade, board, subject and language |
| 2 | **No voice output** — text-only answers | ElevenLabs TTS in English, Hindi and Telugu |
| 3 | **Voice input waits for silence** before transcribing | Live streaming speech-to-text — types words as you speak |

---

## Features

**Grade-adaptive prompting**
Class 1–6 gets emoji concept diagrams, real-life analogies (hot milk, cricket, pressure cooker) and a 120-word cap. Class 7–12 gets structured headings, comparison tables, bolded key terms and exam-focused key points. Same question, genuinely different answer.

**Voice output**
Every response is read aloud via ElevenLabs. The API key is proxied through the Express backend and never reaches the browser.

**Real-time transcription**
Speech appears on screen character by character as the student talks — no dead-air wait, and they can correct mid-sentence.

**Automatic language detection**
Detects English, Hindi (Devanagari) and Telugu (script), including romanised input like "gurinchi cheppandi", and replies in that language.

**Exit quiz — retention loop**
When a session ends, three MCQs are auto-generated from the conversation transcript. Weak topics are stored and resurfaced the next day.

**Graceful rate limiting**
API quota errors render as a friendly retry card instead of a raw stack trace.

---

## Stack

- **Backend** — Node.js, Express
- **LLM** — Google Gemini API
- **Voice output** — ElevenLabs TTS
- **Voice input** — Web Speech API
- **Persistence** — localStorage (student profile, quiz history)

---

## Running locally

```bash
git clone https://github.com/YOUR_USERNAME/vedai-pro.git
cd vedai-pro
npm install

cp .env.example .env
# add your ElevenLabs key to .env

npm start
```

Open http://localhost:3000

You'll be prompted for a Gemini API key in the browser on first load — get one free at [aistudio.google.com](https://aistudio.google.com).

---
## Artifact
https://claude.ai/code/artifact/2297bab4-d2f5-47d7-9fec-308ec7e90a0d

## Architecture note on secrets

The ElevenLabs key lives only in `.env` and is read via `process.env` on the server. The browser calls `/api/tts` and the backend forwards the request — the key is never present in any client-side bundle. `.env` is gitignored.

The Gemini key is supplied by the user at runtime and kept in their own browser's localStorage, so no shared quota and no key in the repo.

---

Built by [Chokkarapu Akhil](https://www.linkedin.com/in/akhil-chokkarapu-841304171/)
