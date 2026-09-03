---
id: 2026-09-02-damien-sileo-cordisbench-can-language-models-reason-about
kind: article
title: "CordisBench: Can Language Models Reason About Component Lifecycles in Dynamic Agent Harnesses?"
source: "https://arxiv.org/abs/2609.01600"
author: Damien Sileo, Dimitri Kachler
published: 2026-09-01
captured: 2026-09-02
via: grok-bot/多恩刊
lane: ai
status: raw
private: false
---

CordisBench (arXiv:2609.01600, pub 2026-09-01). Dynamic agent harnesses let models change plugins/services that shape their own execution; a local change can propagate through dependencies and order-sensitive cleanup. CordisBench is a 1,200-question benchmark of lifecycle reasoning (localization, schedule prediction, guaranteed/reachable conditions, reconfiguration) with 2–32 relevant interactions, scored against Cordis execution and a finite reference semantics.

Key finding: models usually handle small systems well but grow less reliable as more interactions become relevant—especially predicting final state and reasoning across teardown orders—while localization often stays stronger. Extra reasoning effort recovers marked gains for some models at nontrivial cost (GPT-5.6 Luna ~2,967 reasoning tokens/question at medium effort on the 16-interaction subset). That cost is avoidable for controlled instances: the independent finite reference semantics agrees with Cordis execution on every observation/action outcome used for scoring across all 528 executable questions. Implication: harnesses should compute/verify mechanical lifecycle consequences when dependencies and cleanup are explicit, rather than forcing the model to anticipate them unaided.
