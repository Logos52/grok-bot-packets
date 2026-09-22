---
id: 2026-09-22-spacexai-introducing-grok-4-7
kind: article
title: Introducing Grok 4.7
source: "https://x.ai/news/grok-4-7"
author: SpaceXAI
published: 2026-09-21
captured: 2026-09-22
via: grok-bot/Brief
lane: ai
status: raw
private: false
---

Introducing Grok 4.7

SpaceXAI's most powerful model for coding and knowledge work. Twice as fast, at half the price of comparable models.

Grok 4.7 is our most capable model for coding and knowledge work. It works longer on difficult tasks, checks its own work more carefully, and comes with our best-calibrated safeguards to date. Served at the same price and speed as Grok 4.6, it is highly competitive in its class.

On CursorBench 4.0, which stresses longer-running coding tasks, Grok 4.7 is at the frontier in price-performance.

## Model Improvements

Grok 4.7 uses a new, larger base model compared to Grok 4.6. It was trained with a longer reinforcement learning run on a harder mix of tasks, weighted toward problems that take many hours to complete. The model is better at verifying its own work and managing longer context. We also trained Grok 4.7 to natively understand the Grok Bot harness, making it better at conversational tasks and general knowledge work.

Token prices and selected scores (Grok 4.7 xHigh / Grok 4.6 High / GPT-5.6 Sol Max / Fable 5.1 Max):
- Input $/MTok: $2 / $2 / $4 / $10
- Output $/MTok: $6 / $6 / $20 / $50
- CursorBench 4.0: 46.3% / 40.4% / 41.7% / 51.8%
- DeepSWE v1.1: 71.0%* / 65.2% / 72.7% / 70.0% (* high effort)
- EEBench: 64.0% / 53.0% / 39.4% / 56.4%
- AA Briefcase v1.1: 1,657 / 1,546 / 1,487 / 1,678
- Terminal-Bench 4.0: 38.0% / 20.3% / 37.3% / 57.9%
- Harvey Legal Agent: 19.6% / 15.8% / 2.5% / 6.7%
- HealthBench Professional: 56.7% / 48.5% / 60.5% / 62.1%

Grok 4.7 is better at creating documents and presentations. In GDPval and AA Briefcase, AI is asked to work on tasks done by professionals such as lawyers, nurses, and financial analysts. Grok 4.7 improves upon Grok 4.6 on both benchmarks and performs comparably to other frontier models.

## Safety & Cybersecurity

Grok 4.7 was built with an entirely new safeguard stack. It is the strongest model we've tested on refusals and jailbreak resistance. In dual-use domains like cybersecurity and biological work, it leads on both utility for benign tasks and safe refusal on dangerous ones, topping LatchBio's biosafety benchmark at 62.4%.

Grok 4.7 balances strong cyber defense capabilities with low refusal rates for legitimate use. It shows the highest safety on HackerBench v0.3, our benchmark for risky and malicious cyber tasks, allowing only 3.3% of risky dual-use prompts through while rarely blocking legitimate security work. We've also started giving select cybersecurity partners invite-only access to Grok 4.7's red-team capabilities for defense research.

## Pricing and availability

Grok 4.7 is available today in Cursor and Grok Build. It is also available through the Grok API, third-party coding harnesses, and model routers and cloud platforms.

The model is priced starting at $2 per million input tokens and $6 per million output tokens. We also serve a fast variant with twice the output speed at twice the price.
