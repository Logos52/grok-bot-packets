---
id: 2026-09-24-anthropic-claude-discovers-a-novel-enzyme-system
kind: article
title: Claude discovers a novel enzyme system with CRISPR-like repeats
source: "https://www.anthropic.com/news/claude-discovers-novel-enzyme-system"
author: Anthropic
published: 2026-09-23
captured: 2026-09-24
via: grok-bot/多恩刊
lane: ai
status: raw
private: false
---

Claude discovers a novel enzyme system with CRISPR-like repeats

Sep 23, 2026

We’re introducing a new life sciences research group and laboratory at Anthropic. Our focus is on fundamental biology research using Claude: exploring datasets of DNA to identify uncharacterized protein families, generating hypotheses at scale, and testing them through experiments in the lab. This post introduces the team behind this work and shares early results in which Claude discovered a novel enzyme system with properties reminiscent of CRISPR, with only high-level direction from our scientists.

Many discoveries that have revolutionized biology and medicine started with a scientist noticing something odd in the staggering diversity of molecular machines found in nature. Restriction enzymes, proteins that cut DNA at specific short sequences, were found in bacterial immune systems. Taq polymerase was identified in a Yellowstone hot spring bacterium and became the basis for PCR. CRISPR was first noticed as an unusual repeat sequence in bacterial DNA.

In the spring of 2026, Anthropic formed a research group to see whether general AI models can systematize and accelerate such discoveries. Agents collaborate with humans in every step; the team built its own lab and works from training Claude in biology to running experiments.

Today’s early results: Claude autonomously discovered a novel enzyme system associated with an array of DNA repeats, a pattern reminiscent of CRISPR. Function is still unknown. The system has characteristics found together in only a handful of other systems, all of which are programmable and perform operations like cutting, copying, and pasting DNA.

The system is based on a reverse transcriptase (RT) found in a jumbo phage. The underlying RT had been identified in previous studies, but Claude appears to be the first to notice the system’s defining features—an associated array of non-coding DNA sequences and an additional accessory protein of unknown function.

Feng Zhang (MIT / Broad): “This is an exciting example of how AI agents can contribute to biological discovery. The identification of RNA-repeat arrays associated with reverse transcriptases is genuinely intriguing and merits further investigation.”

Claude was prompted to search a massive DNA database for interesting new RTs. Involvement was limited to the initial prompt and lab work. After 21 hours, roughly 950 agents, and 210 million tokens, one agent spotted a repeating pattern of DNA next to an odd-looking RT. After further analysis and lab testing, the team recognized a previously uncharacterized enzyme system in bacteriophages called array-associated reverse transcriptases (ART).

Work to understand ART’s primary function is ongoing. A pre-print discusses this in more detail.

Claude agents gathered over 200,000 RTs, picked out 3,500 new candidate systems, and narrowed those to the 20 most compelling. During research, Claude noticed an unusual RT family and examined raw DNA beside it: “[The DNA next to the RT] is spectacular: I can see by eye a tandem repeat array … that's a CRISPR-like … repeat array?!”

ART is found mainly in bacteriophages and consists of three parts: the RT, a partner gene beside it, and a long array of evenly spaced DNA repeat sequences. First experiments show the ART array is expressed as a set of distinct short RNAs. Further experiments are underway.
