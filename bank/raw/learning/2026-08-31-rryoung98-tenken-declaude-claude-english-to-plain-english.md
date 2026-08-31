---
id: 2026-08-31-rryoung98-tenken-declaude-claude-english-to-plain-english
kind: article
title: "declaude: Claude-English to plain English"
source: "https://speak-english.tenken.co/"
author: rryoung98 / Tenken
published: 2026-08-26
captured: 2026-08-31
via: grok-bot/Field
lane: learning
status: raw
private: false
---

declaude: Claude-English to plain English de claude Account Use it Pricing GitHub Claude writes like this. You don't have to read it. declaude rewrites assistant-voice into plain English. Meaning, code, and structure survive intact. Before After One thing I didn't cover is the migration script. When you're ready, I can go through it with you. Translate No sign-in needed. Type, paste, or drop a file. Get a free key Translate a document Three ways to use it 1 Claude Code plugin Two commands install the hook. Replies render in plain English, and your transcript and token bill stay untouched. 2 MCP server Browser sign-in, no key pasting. 3 Documents Drop a Markdown file, get it back rewritten. /plugin marketplace add tenkenco/declaude /plugin install declaude@tenken /declaude:setup claude mcp add --transport http declaude \ https://speak-english.tenken.co/mcp curl -X POST https://speak-english.tenken.co/v1/translate \ -H "Authorization: Bearer $DECLAUDE_TOKEN" \ -d '{"text": "Certainly! Let me delve into that."}' {"translation": "Sure, here you go.", "model": "qwen2.5-14b-instruct"} Runs on an open-source model (Qwen2.5-14B) on our own GPUs. Your text is processed in memory and discarded: never written to disk, a database, or logs. Pricing Free $5 / month Translations 100 / month Unlimited Documents 5 / month, 200 KB 500 / month, 2 MB Card required No Yes $0 $5 / mo At the free limit the API returns 402 with a payment link. Subscribing keeps the same key. GitHub Documents Account Pricing Built by Tenken . Based on claudish-to-english by gvzdv , the original local-Ollama hook this service grew out of.
