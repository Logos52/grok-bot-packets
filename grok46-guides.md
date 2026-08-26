# Grok 4.6 guides and useful how-to posts

Compiled Saturday 2026-08-15 (Asia/Saigon). Public first-party fetches only. No titles, dates, or quotes invented. If a page was not opened, that is stated.

**Coverage note:** Grok 4.6 shipped **12 August 2026** (three days before this compile). Official xAI / Grok Build / API docs are usable how-tos (call the model, set `reasoning_effort` including `xhigh`, cache, compact, run Grok Build). Independent named-person writeups with real prompts and workflows are **thin**. The one substantial first-person field guide found is Eric Zakariasson’s LinkedIn post. Most third-party “guides” are launch recaps of the xAI announcement.

---

## OPENED and useful

### 1. Introducing Grok 4.6
- **Who:** Official xAI / SpaceXAI
- **Date:** 12 August 2026 (shown on page)
- **URL:** https://x.ai/news/grok-4-6
- **Opened:** yes
- **What it teaches:** Official launch post: 4.6 is aimed at long-running agents and more ambitious interactive/visual work; xAI says it is especially strong at turning a broad product idea into a working first version (research, structure, implement, refine) and at stronger first-pass visual language; more self-testing on longer trajectories; available in Cursor, Grok Build, the API, OpenRouter, Vercel, Cloudflare; pricing starts at $2 / $6 per million input/output tokens plus a 2x fast variant; first-week 2x included usage in Cursor and Grok Build; Grok Build install one-liner.

### 2. Grok 4.6 (developer overview)
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/developers/grok-4-6
- **Opened:** yes
- **What it teaches:** How to call `grok-4.6` with the xAI SDK, Vercel AI SDK, OpenAI SDK, and curl (sample task: find and fix a bug in a `median` function); table of context (500,000 tokens), knowledge cutoff (1 February 2026), modalities, no output limit, reasoning levels (low / medium / high default / xhigh), tools; recommends `prompt_cache_key` / `x-grok-conv-id` and context compaction for long agent loops; lists where it runs (API, Grok Build, Cursor, OpenRouter, Vercel, Cloudflare).

### 3. Grok 4.6 (model detail)
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/developers/models/grok-4.6
- **Opened:** yes
- **What it teaches:** Model card facts for integration: text+image → text, 500k context, function calling / structured outputs / reasoning; short- vs long-context (≥200k) pricing ($2/$0.50/$6 vs $4/$1/$12 per 1M); rate limits (150 rps, 50M TPM); regions us-east-1 and us-west-2.

### 4. Reasoning
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/developers/model-capabilities/text/reasoning
- **Opened:** yes
- **What it teaches:** How to set `reasoning_effort` on `grok-4.6` (low / medium / high default / **xhigh**, which is 4.6+ only); when each level is for (latency-sensitive tools vs hardest problems); cannot disable reasoning; code samples for a math-proof prompt and for streaming reasoning-summary deltas on a projectile-motion problem.

### 5. Models
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/developers/models
- **Opened:** yes
- **What it teaches:** Official routing advice: dedicated models for audio/image/video; “For everything else, including code, use Grok 4.6”; knowledge cutoff 1 February 2026; need Web Search / X Search for realtime events; image-input limits.

### 6. Grok Build
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/build/overview
- **Opened:** yes
- **What it teaches:** How to install and start the coding agent that is now powered by Grok 4.6: `curl` / PowerShell install, `cd` + `grok`, API-key auth, suggested first prompts (“Explain this repo.” / walk a file), headless `-p`, custom models in `~/.grok/config.toml`, plus the same `grok-4.6` API samples as the model overview.

### 7. Modes and Commands
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/build/modes-and-commands
- **Opened:** yes
- **What it teaches:** How to operate Grok Build (default model 4.6) in the TUI: Plan / Auto / Always-approve; `/model` (`/m`) and `/effort` to pick the model and reasoning depth; `/plan`, `/create-workflow`, `/workflow`, `/deep-research`, `/loop`, `/imagine`, `/compact`, `/fork`, and the rest of the command table.

### 8. Plan Mode
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/build/features/plan-mode
- **Opened:** yes
- **What it teaches:** When to use plan mode (ambiguous architecture, high-impact restructures) vs skip it (obvious one-path fixes); how to enter (`/plan`, Shift+Tab), review, approve (`a`), request changes (`s`), comment (`c`); caveats that only the plan file is editable until approval and that bash is not edit-gated.

### 9. Headless & Scripting
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/build/cli/headless-scripting
- **Opened:** yes
- **What it teaches:** How to run the Grok Build agent (4.6-powered) in scripts/CI: `grok -p`, model/session flags, output formats (`plain` / `json` / `streaming-json`), `--always-approve`, `--no-auto-update`, and an ACP `grok agent stdio` JSON-RPC example.

### 10. Maximizing Cache Hits
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/developers/advanced-api-usage/prompt-caching/maximizing-cache-hits
- **Opened:** yes
- **What it teaches:** How to make multi-turn `grok-4.6` agent loops cheap: set `x-grok-conv-id` (Chat Completions / gRPC) or `prompt_cache_key` (Responses API / AI SDK) so requests stick to one server; all code samples on the page use `model: "grok-4.6"`.

### 11. Context Compaction
- **Who:** Official xAI docs
- **Date:** not shown on page
- **URL:** https://docs.x.ai/developers/advanced-api-usage/context-compaction
- **Opened:** yes
- **What it teaches:** How to keep long 4.6 agent loops under the context window: when to compact, `POST /v1/responses/compact` with `model: "grok-4.6"`, pass the opaque compaction item back, in-place `chat.compact()` every N turns; do not edit `encrypted_content`; compaction cannot rescue an already-over-limit request.

### 12. Grok 4.6 – A field guide
- **Who:** Eric Zakariasson (byline: Building Cursor)
- **Date:** Published 13 August 2026 (shown on page)
- **URL:** https://www.linkedin.com/pulse/grok-46-field-guide-eric-zakariasson-vgkde
- **Opened:** yes
- **What it teaches:** First-person daily-driver notes after weeks of use. Prompting: “work very hard” did not change outcomes; short prompt + a preference often beat a long spec; the highest-leverage line he found was asking the model to verify function and design after implementation and keep iterating until production-ready (spreadsheet app in Next.js with Cursor SDK). Same idea for 3D: “capture the current frame, list what’s wrong, then fix only those things.” Use cases he actually ran: provider-console click-through for API keys, functional/visual QA, inbox triage, launch posts and a Remotion launch video, a detailed feedback-widget spec, an Age of Empires–style browser game, MSN Messenger recreation, Excalidraw presentation mode, a fictional quarterly board deck, and a 60–90s X TypeScript SDK launch film. Practical limit: verification is easy on websites, harder on 3D/video/physics — give it a way to look, or you check.

### 13. Grok 4.6 now available on AI Gateway
- **Who:** Walter Korman, Jerilyn Zheng (Vercel changelog)
- **Date:** 12 August 2026 (shown on page)
- **URL:** https://vercel.com/changelog/grok-4-6-now-available-on-ai-gateway
- **Opened:** yes
- **What it teaches:** How to call 4.6 through Vercel AI Gateway: `model: 'xai/grok-4.6'`, `reasoning: 'xhigh'`, sample prompt “Analyze this dataset and summarize the key trends.”; `vercel ai-gateway coding-agents setup` then select `xai/grok-4.6` in Claude Code / Codex / OpenCode / Pi; 500K context, text+image in, low/medium/high/xhigh (default high).

### 14. Grok 4.6: xAI's Agent-Focused Update Matches GPT-5.6 Sol at the Same $2/$6 Price
- **Who:** Developers Digest (no personal byline on the article)
- **Date:** Last updated 13 August 2026 (shown on page)
- **URL:** https://www.developersdigest.tech/blog/grok-4-6-release-guide-2026
- **Opened:** yes
- **What it teaches:** Practical “run it today” guide: OpenCode install + `opencode run --model opencode/grok-4.6` / `opencode --model opencode/grok-4.6`; when to pick 4.6 (agentic coding, CursorBench-style first-pass, 500K + image) vs wait for GPT-5.6 Sol / Fable 5 (terminal-heavy / DeepSWE); restates official pricing, `prompt_cache_key`, and Vercel id `xai/grok-4.6`. More setup/routing than original prompts.

### 15. Share your Thoughts on Grok 4.6
- **Who:** Kevin Neilson (Cursor staff) plus named users (Isia Wang, Congzhi, yaireo, joeybab3, and others)
- **Date:** Thread starts 12 August 2026; useful replies through 13 August 2026
- **URL:** https://forum.cursor.com/t/share-your-thoughts-on-grok-4-6/168190
- **Opened:** yes
- **What it teaches:** Cursor-specific how-to, not a polished guide. Official: in Cursor the context window is **256k** (not the API’s 500k); 4.6 adds Extra High / xhigh; xhigh fills the window faster because thinking traces and extra tool/verification stay in the chat — switch back to high or start a new chat for longer sessions; 4.6 draws from the Cursor Models usage pool. User notes: Congzhi found xhigh “quite good” but context fills fast; yaireo found it slower than 4.5 with long thinking even on fast; joeybab3 reported a “finish from here” laziness miss on a grouping query.

---

## Could not open

- **Model Card: Grok 4.6 (PDF)** — https://media.x.ai/v1/website/card-7f81d41b.pdf — fetch returned HTTP 500. Search snippets claimed channels (API, Grok Build, Cursor, Office add-ins, gateways) and that 4.6 is not for autonomous high-stakes decisions without oversight; **not verified from the file**.
- **How to Use Grok in 2026: 25 Advanced Tips (SurePrompts)** — https://sureprompts.com/blog/how-to-use-grok — not fetched. Search snippet is generic Grok (DeepSearch, Fun Mode, X live feed), not Grok 4.6.

---

## Dropped

Opened, then excluded as catalog spam, undated product pages, or launch recaps with no original how-to.

- **Introducing Grok 4.6 · Cursor** — https://cursor.com/blog/grok-4-6 — opened. Date not shown on the page. Near-verbatim of the xAI announcement (training, “idea → working first version,” availability, 2x usage). No extra prompts or workflows. Launch recap.
- **Release Notes (Grok 4.6 blurb)** — https://docs.x.ai/developers/release-notes — opened. August section restates context, pricing, and reasoning levels and links the overview + announcement. No how-to.
- **Grok Build (marketing page)** — https://x.ai/build — opened. Undated product landing (“Meet Grok 4.6 • Now powering Grok Build”) with install command and feature bullets. How-to lives in the docs above.
- **Pricing** — https://docs.x.ai/developers/pricing — opened. Undated price tables (includes grok-4.6 short/long rates). Same numbers already on the model detail page.
- **Grok 4.6 Explained: Capabilities, Pricing, & Comparison** — https://www.layer3labs.io/guides/grok-4-6-explained — opened. Reviewed by Jonathan West; updated 12 August 2026. SEO recap of the xAI post plus a consult CTA; no original prompts or a run they did.
- **Grok 4.6 Capabilities and Use Cases** — https://www.eigent.ai/blog/grok-4-6-capabilities-use-cases — opened. Date not shown (body says “today”). Restates xAI capabilities/benchmarks and four generic use-case buckets, then pitches Eigent. No named workflow they ran.
- **Grok 4.6 Arrives 2026: 1753 Elo at Half the Price** — https://ailearningguides.com/grok-4-6-launch-pricing-api/ — opened. Has API/eval/routing code, but uses model id `grok-4-6` (official id on opened xAI docs is `grok-4.6`) and treats 1753 as LMArena Elo (xAI’s opened announcement lists 1753 as GDPVal-AA v2). Catalog/affiliate page with factual mismatches; not kept.
- **😺 Grok 4.6 is GPT 5.6 level and built for agents that don't quit** — https://www.theneurondaily.com/p/grok-4-6-is-gpt-5-6-level-and-built-for-agents-that-don-t-quit — opened. Eric Gerard Ruiz & Grant Harvey, 13 August 2026. Newsletter launch recap (benchmarks, price, Musk on 4.7). The “skill of the day” is a Claude Voice morning brief, not Grok 4.6.

---

## Method

Searched: `Grok 4.6 (guide OR tutorial OR "how to" OR "use cases" OR prompts OR "I use") 2026` plus official-docs and named-person queries. Fetched each keep/drop candidate with a first-party URL fetch (no Firecrawl). Docs pages generally have no publication date.
