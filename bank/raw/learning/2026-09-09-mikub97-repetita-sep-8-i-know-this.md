---
id: 2026-09-09-mikub97-repetita-sep-8-i-know-this
kind: article
title: Repetita Sep-8 — I-know-this declared≠earned + retirement + offline answers
source: "https://github.com/mikub97/repetita/commit/397a460ed6dcb76c895080c4b33bd03c15f8f6d3"
author: mikub97
published: 2026-09-08
captured: 2026-09-09
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# SOURCE: CHANGELOG.md Unreleased (as of 2026-09-08) + commits

## "I know this" (declared ≠ earned)
One button taking a card out of the queue on the learner's word. Recorded as `declared` and never as `earned`, so a claim stays distinguishable from months of evidence, with an undo at the only moment the learner knows which card they meant. Writes nothing to the review log: declaring is not an answer (would corrupt accuracy figures and the gate that decides how fast new material arrives).

## Cards retire
`should_retire()` existed and was never called; rule moved to `core/retirement.py` as policy over what the store records rather than a memory-model property.

## Offline answers kept
Answers given offline used to be written to a status line and lost. Handles persisted so queued answers survive restart.

## Mount on an application someone else owns (#42)
feat(web): mount repetita on an application someone else owns; tell the client where the app is mounted (#43); reload course content without a restart (#41).

## Choice form rendered
Client previously silently skipped choice cards (546 of 676) because MODES[card.form] was undefined.

Commit atom window 2026-09-08 ~17:05–18:02Z.
