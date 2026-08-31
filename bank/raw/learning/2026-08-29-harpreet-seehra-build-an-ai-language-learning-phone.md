---
id: 2026-08-29-harpreet-seehra-build-an-ai-language-learning-phone
kind: article
title: Build an AI Language Learning Phone Tutor with Telnyx Voice AI and AI Inference
source: "https://dev.to/harpreetseehra/build-an-ai-language-learning-phone-tutor-with-telnyx-voice-ai-and-ai-inference-36j1"
author: Harpreet Seehra
published: ""
captured: 2026-08-29
via: grok-bot/Field
lane: learning
status: raw
private: false
---

Vendor walkthrough (Telnyx code examples): a Flask app that turns a phone call into a language practice session. Caller dials, picks a language by digit, talks to an AI tutor that responds in the target language with English support, raises difficulty, corrects gently.

Not a named classroom the author runs. Library: product tutorial + FAQ (reasoning models can eat max_tokens and leave silence on the phone; switch to a non-reasoning chat model or raise max_tokens). Canonical code in team-telnyx/telnyx-code-examples.
