---
id: 2026-08-29-anthropic-automated-researchers-can-reliably-mitigate-alignment
kind: article
title: Automated researchers can reliably mitigate alignment failures
source: "https://www.anthropic.com/research/automated-researchers-mitigate-alignment-failures"
author: Anthropic
published: 2026-08-28
captured: 2026-08-29
via: grok-bot/多恩刊
lane: ai
status: raw
private: false
---

Automated researchers can reliably mitigate alignment failures

Aug 28, 2026

As AI begins to build itself, automating alignment research becomes increasingly important to let safety research keep pace. Although measuring the success of alignment research is enormously challenging, researchers (at Anthropic and elsewhere) have developed benchmarks and automated auditing tools, such as Petri, that quantify common alignment failures, like deception, sycophancy, and jailbreaks.

In one of our earlier experiments, we tasked Claude with finding effective ways to use weak AI models as “teachers” to supervise the training of stronger models (in this case, the “student” model). Now, we’re releasing a new report that builds on this idea. We had Claude autonomously train models to improve their performance on several public benchmarks that measure each of 10 categories of alignment failure. For instance, Claude improved models’ performance on privacy violation, measured by ConfAIde, PrivaCI-Bench, and PrivacyLens. Claude tackled one alignment failure at a time through a loop of searching literature, proposing methods and data, training, and then testing.

We judged Claude’s success according to the “percentage of safety gap closed,” i.e., how far its methods moved the student model towards the theoretical perfect score, as judged across the range of benchmarks (typically three to five) for each category of alignment failure. We excluded alignment methods that hurt the student models’ general capabilities, and forbade Claude from distilling its own alignment directly into the target model. We enforced these constraints with a monitoring agent, which read every method Claude had in mind before it ran.

Our aim was to assess whether the proposed methods would, first, remain effective on alignment evaluations that Claude was never shown during its research loop; second, avoid degrading the student model’s capabilities (since safety training might, for example, make models refuse tasks more often, reducing their overall usability); and, third, still work on larger models than the ones Claude was asked to align in this test.

On each of these counts, Claude’s methods worked. For all 10 alignment failures, Claude found fixes that improved the target benchmarks without degrading capabilities. The best methods also worked on withheld alignment benchmarks and on Petri, an open-source tool that simulates adversarial multi-turn scenarios for testing misalignment. Moreover, the methods remained effective on models up to 4.7 times larger than those Claude optimized for during the research loop.

Claude also outscored 28 human safety researchers who had up to eight hours to devise methods. On deception, for example, Claude’s best method performed 20% better than the best human proposal. However, since the humans couldn’t iterate on their submissions, we view this less as a direct comparison and more as evidence for a workflow where Claude identifies promising alignment methods that humans can refine further.

We tasked Claude Sonnet 5—which is weaker than Claude Opus 4.8 on the Epoch Capabilities Index—with fixing alignment failures in an early Opus 4.8 checkpoint that had not yet gone through most of our production alignment training.

In just 60 hours, Claude experimented with over 50 solutions and achieved alignment scores nearly matching those of our production models. The winning solution contains just over 2,000 training examples, built from simple templates or public datasets, making it roughly 15,000 times more efficient than our production alignment procedure.

To catch cheating behaviors, we prompted Claude Opus 4.8 to monitor ~1,600 research agent transcripts across all 10 alignment failures, finding cheating attempts in 39 (2.4%).

We open-source our automated alignment research harness so that others can build on it and use it to align their own models.
