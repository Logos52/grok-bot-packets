# Claude Opus 5.5 vs Sonnet 5.5: which one to use (draft)

*Draft, Sep 29, 2026. The facts come only from first-party Anthropic pages (linked inline). The sentiment section uses real X posts pulled through fxtwitter and Techmeme's aggregation pages.*

## 1. Bottom line

Start with **Sonnet 5.5** as the default for well-scoped work: bug fixes, fast feature iteration, repeatable agent tasks (investigation, review, drafting), high-volume pipelines, and polished documents, slides and spreadsheets. It costs half as much per token as Opus 5.5 ($2/$10 vs $4/$20 per MTok, input/output). Anthropic's docs rate its latency "Fast" against Opus's "Moderate". On Anthropic's own benchmarks it lands within a few points of Opus on most evals, and it tops Opus on Terminal-Bench 4.0 (70.6% vs 66.4%, with Opus's figure measured at Xhigh effort). Step up to **Opus 5.5** for complex, open-ended work that needs sustained judgment: long-horizon agentic coding, codebase-wide migrations and audits, ambiguous multi-part tasks, and "the hardest problems, where you need the most intelligence." Anthropic says Opus "remains clearly stronger at complex, open-ended work requiring sustained judgment," even where the benchmark numbers look close. A practical rule: if the task has a clear spec and a way to check the result, use Sonnet. If it doesn't, or a miss is expensive, use Opus. If you find yourself pushing Sonnet to `xhigh`/`max` effort, Anthropic suggests considering Opus instead.

## 2. When to use which

### Use Sonnet 5.5 for
Anthropic's guidance: "Sonnet 5.5 fits best when the task has a clear spec and a way to check the result." ([claude.dev guide](https://claude.dev/blog/building-with-claude-sonnet-5-5/))

- **Well-scoped everyday coding**: fixing bugs, quickly iterating on features, verifying against requirements. ([claude.dev guide table](https://claude.dev/blog/building-with-claude-sonnet-5-5/))
- **High-volume everyday development** and **well-defined agent tasks you run repeatedly** (investigation, review, drafting). (same)
- **Polished documents, slides and spreadsheets**: one-pagers, diagrams, summary slides, document edits, spreadsheet cleanup, "where an eye for design helps." (same) In one internal test, Anthropic gave it a public company's earnings materials plus a slide template and asked for a 10-slide operating review. "Two experts judged its first draft to be ready to send as is." ([Anthropic Sonnet 5.5 launch](https://www.anthropic.com/claude-sonnet-5-5))
- **Code review at simple/moderate complexity**: CodeRabbit says it plans "to move simple and moderate reviews over now." (Anthropic launch page, customer quote)
- **Support and ops agents where speed matters**: Zendesk reports tickets "processed 20% faster". Atlassian says Rovo Agents run "up to 30% faster" than on Sonnet 5. Slack reports it beat Sonnet 5 on almost all offline Slackbot evals "with about 14% fewer output tokens" and no prompt changes. (Anthropic launch page, customer quotes)
- **High-volume finance/retrieval work**: Balyasny found it "had the best quality-to-cost tradeoff of the seven models we ran" and used about 121k tokens per answer where Sonnet 5 used 497k. (Anthropic launch page)
- **Implementing a plan Opus designed**: "When Claude Opus 5.5 sets the architecture and general framework for a game, I would feel confident in letting Sonnet 5.5 implement it." (Kevin Ngo, Anthropic launch page)
- **Latency-sensitive chat**: for chat, the guide says to start at `medium` or `low` effort. For well-specified agentic coding, start at `medium`. ([claude.dev guide](https://claude.dev/blog/building-with-claude-sonnet-5-5/))

### Use Opus 5.5 for
- **Complex work requiring careful judgment, including long-horizon agentic coding and knowledge work**, and "the hardest problems, where you need the most intelligence." ([claude.dev guide table](https://claude.dev/blog/building-with-claude-sonnet-5-5/)) The prompting guide it cites says: "for the hardest long-horizon work, an Opus model is the better choice."
- **Long, sprawling jobs like codebase-wide migrations and audits.** One early tester audited and fixed a 200,000-line codebase in under three hours. Opus 5 took over 20 hours. In Anthropic's HAProxy C-to-Rust port, Opus 5.5 finished in 9.5 hours vs 12 for Fable 5.1, at 51% less cost. ([Anthropic Opus 5.5 launch](https://www.anthropic.com/news/claude-opus-5-5))
- **Unattended multi-hour or overnight runs across many repos.** Clio reports "over 18 hours" on a six-repo task. Stripe reports a multi-day rebase of 40 stacked PRs, where one Opus session directed "a dozen more sessions." (Opus launch page, customer quotes)
- **Orchestrating subagents** on audits, migrations and large reviews. ([Getting the most out of Opus 5.5](https://claude.dev/blog/getting-the-most-out-of-opus-5-5/))
- **Research and analysis where invented figures are unacceptable.** In Anthropic's earnings-report test, "16 out of 18 of Opus 5.5's reports cleared our quality bar," while Fable 5.1 and Opus 5 cleared it in no attempt. (Opus launch page)
- **High-stakes code review.** Deloitte: "Even at its lowest effort setting, Claude Opus 5.5 caught 72% of known bugs in our code reviews to Opus 5's 56% at high effort." (Opus launch page)
- **Interactive work where you want frontier quality with lower latency.** Opus 5.5 has **fast mode** (up to 2.5x speed, $8/$40 per MTok). Sonnet 5.5 has no fast mode. ([pricing docs](https://platform.claude.com/docs/en/about-claude/pricing), [claude.dev guide](https://claude.dev/blog/building-with-claude-sonnet-5-5/))

### Common pattern: split the work
- **Opus plans or coordinates, Sonnet executes.** Anthropic's Kevin Ngo quote above supports this, and Claude Code's `opusplan` alias works the same way (Opus plans, Sonnet carries out the plan). Note that Addy Osmani's Sep 25 cost post, written *before* Sonnet 5.5 shipped, recommended the opposite for code edits. It advised moving "down to Sonnet or Haiku for lookups, not for writing code" and told readers to measure `opusplan` before making it a default. ([What a task costs on Opus 5.5](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/)) The Sep 28 Sonnet 5.5 guide explicitly recommends Sonnet for well-scoped coding, so treat the older advice as superseded for Sonnet 5.5 and measure on your own tasks.
- **Claude Code defaults:** the `default` model stays Opus 5.5. The `sonnet` alias now resolves to Sonnet 5.5 (at `medium` effort) from v2.1.284, and Anthropic suggests "switch with `/model sonnet` for well-scoped tasks." ([claude.dev guide](https://claude.dev/blog/building-with-claude-sonnet-5-5/))

### Benchmarks (as stated by Anthropic, Sonnet 5.5 launch table)
| Benchmark | Sonnet 5.5 | Opus 5.5 | Sonnet 5 |
|---|---|---|---|
| Terminal-Bench 4.0 (agentic coding) | 70.6% | 66.4%¹ | 10.3% |
| FrontierCode 1.1 Main | 46.2%* | 54.4% | 42.4%* |
| CursorBench 4.0 | 55.5% | 57.8% | 34.1% |
| GDPval-AA v2.1 (Elo) | 1844 | 1846 | 1449 |
| AA-Briefcase v1.1 (Elo) | 1811 | 1822 | 1359 |
| Humanity's Last Exam (with tools) | 64.5% | 67.7% | 54.9% |
| OSWorld 2.1 (partial) | 80.1% | 81.8% | 57.0% |
| Chartography (no tools) | 61.6% | 64.4% | 15.6% |

Source: [anthropic.com/claude-sonnet-5-5](https://www.anthropic.com/claude-sonnet-5-5). ¹ Footnote: Opus 5.5's Terminal-Bench figure is at Xhigh effort, its highest score. ² Footnote: Sonnet 5.5 scores lower at Max than at Xhigh on FrontierCode, because at Max it ran extra review subagents that caused timeouts and out-of-scope edits. \*The FrontierCode row in the captured page text is ambiguous. Its cells read in order "46.2% / Max² / 42.4% / 54.4% / 49.3% / 52.1% / Xhigh" across columns for Sonnet 5.5, Sonnet 5, Opus 5.5 and GPT-6 Sol. 46.2% for Sonnet 5.5 is the most likely reading, but which number belongs to which effort level is unclear. Check the live chart before quoting Sonnet's FrontierCode figures. Anthropic's own caveat: "benchmark scores capture only one facet… Opus 5.5 remains clearly stronger at complex, open-ended work requiring sustained judgment."

## 3. Cost and speed facts

| Item | Sonnet 5.5 | Opus 5.5 | Source |
|---|---|---|---|
| Input / MTok | $2 | $4 | [pricing docs](https://platform.claude.com/docs/en/about-claude/pricing) |
| Output / MTok | $10 | $20 | pricing docs |
| Cache write, 5 min / MTok | $2.50 | $5 | pricing docs |
| Cache write, 1 h / MTok | $4 | $8 | pricing docs |
| Cache read (hit) / MTok | $0.20 (0.1x input) | $0.20 (0.05x input) | pricing docs |
| Batch API (input/output) | $1 / $5 | $2 / $10 | pricing docs |
| Fast mode | Not available | $8 / $40 per MTok, "up to 2.5x speed" | pricing docs; [Opus launch](https://www.anthropic.com/news/claude-opus-5-5) |
| US-only inference (`inference_geo: "us"`) | 1.1x | 1.1x | pricing docs |
| Context window | 1M tokens (native, no beta header) | 1M tokens | [models overview](https://platform.claude.com/docs/en/models/overview) |
| Max output | 128K (300K on Batches with beta header) | 128K (300K on Batches with beta header) | models overview |
| Comparative latency | "Fast" | "Moderate" | models overview |
| Speed vs predecessor | outputs "30%+ faster than Sonnet 5" | output "more than 30% faster than Opus 5" | [Sonnet launch](https://www.anthropic.com/claude-sonnet-5-5); Opus launch |
| Cost vs predecessor | "up to 30% less per task" than Sonnet 5 (same per-token price) | "40% less than Opus 5 on typical workloads" at default settings | Sonnet launch; Opus launch |
| Default effort (Claude API) | `high` | `medium` | models overview |
| Default effort (Claude Code / apps) | `medium` | `medium` | [claude.dev guide](https://claude.dev/blog/building-with-claude-sonnet-5-5/); [Opus task-cost post](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/) |
| Thinking | Adaptive, on by default (`between_tools` can turn off upfront thinking) | Adaptive, always on | models overview; claude.dev guide |
| Knowledge cutoff | Jun 2026 | Jun 2026 | models overview |
| Retirement (not sooner than) | Sep 28, 2027 | Sep 22, 2027 | models overview |

Notes for the reader:
- **Cache-heavy agent loops narrow the gap.** Cache reads are $0.20 on both models, so long agentic sessions dominated by cache reads cost relatively closer. The 2x gap shows up mainly in fresh input and output, and thinking is billed as output. ([task-cost post](https://claude.dev/blog/what-a-task-costs-on-opus-5-5/))
- **Anthropic publishes no absolute tokens-per-second figures.** Speed claims are relative, both to predecessors and within the current lineup.
- **Effort choice can flip the cost comparison.** Anthropic: Sonnet 5.5 "complements Opus 5.5 best when running at lower effort settings… At higher settings, it can perform comparably at a similar cost." (Sonnet launch)
- **Image-heavy inputs cost more.** Sonnet 5.5 uses the high-resolution image tier (up to 2576 px on the long edge). A 2000×1500 image costs about 2.5x the tokens it did on Sonnet 4.6/4.5/Haiku 4.5. (claude.dev guide)
- **Both models have safeguards that can reroute requests.** Sonnet 5.5 cyber declines can fall back to Sonnet 5. Opus 5.5 reroutes most cybersecurity tasks to Opus 4.8. Anthropic says routine finding and fixing of bugs is unaffected. (both launch pages; claude.dev guide)

## 4. X sentiment summary

**Method.** I collected two pools of real posts. I excluded Anthropic employees and off-topic posts from the counts.
- **Pool A: replies to the @ClaudeDevs launch post** ([link](https://x.com/ClaudeDevs/status/2104687805876367793), posted Sep 28, 5:40 PM ET). These are the first 35 replies returned by the fxtwitter conversation API. The post shows 158 replies and 102 quotes, and paging past the first batch failed.
- **Pool B: general posts about Opus 5.5 / Sonnet 5.5** as surfaced on Techmeme's launch clusters ([Sonnet, Sep 28](https://www.techmeme.com/260928/p32); [Opus, Sep 22](https://www.techmeme.com/260922/p37)). Each post was re-fetched via fxtwitter to confirm handle, text and URL. That gave 29 on-topic posts from non-Anthropic accounts.

**Rough split.**
| Pool | Positive | Mixed | Negative | Neutral/unclear | Total |
|---|---|---|---|---|---|
| A: replies to @ClaudeDevs | 4 | 1 | 22 | 8 | 35 |
| B: general posts (Techmeme-surfaced) | 21 | 6 | 2 | 0 | 29 |

The two pools point in opposite directions, and the difference comes from how each was sampled. Reply-thread negativity is mostly **not about model quality**. Of the 22 negative replies, 12 demand a usage-limit reset and 7 object to the launch video using an uncredited photo. Only about 3 criticize cost or quality. The Techmeme-surfaced posts skew toward prominent accounts and early-access testers, which pushes that pool positive.

**Top themes**
1. **Sonnet 5.5 is "near-Opus at half the price."** This is the dominant general theme: @MatthewBerman, @AlexFinn, @synthwavedd, @haider1, @cursor_ai, @TokenGremlin. Some go further and question whether Opus is worth it (@DeryaTR_).
2. **Rate limits and resets.** Repeated requests for a banked usage reset like the one that came with Opus 5.5 (e.g., @outsource_, @sepTND, @DeckardBuilds).
3. **Token consumption.** Artificial Analysis says Sonnet 5.5 has "the highest Output Tokens per Task we've seen." @synthwavedd called Opus 5.5 "a token-gobbling monster" on that index. This sits in tension with Anthropic's per-task efficiency claims, but it is benchmarked at max effort.
4. **Speed and price as the headline wins for Opus 5.5.** "~30% faster and ~40% cheaper per task" (@Yuchenj_UW), along with praise for clearer writing (@kunchenguid, @kieranklaassen). One dissent: @emollick says it "still hasn't fully solved the dense language issue."
5. **Launch-video image credit.** High-engagement replies (e.g., @fire, 197 likes) say the reference photo belongs to @IceSolst and wasn't credited in the post. For balance: the linked blog page *does* credit "@IceSolst for the reference image."
6. **Skepticism and safeguards.** @natolambert calls a model topping the index "normally a bit of a red flag". @xlr8harder alleges the classifiers target Chinese hardware. @shub0414's "please don't nerf Opus 5.5" and @InvictusManus's "no sneaky degradation" reflect worry about quality degradation.
7. **Workflow split.** Keep Opus as coordinator and Sonnet as worker (@dani_avila7), or use Sonnet for "day to day queries, quick bits of work, and sub agents" (@RobertJBye).

**Representative posts**
- Positive (Sonnet): @MatthewBerman: "Sonnet 5.5 basically Opus 5.5 but 50% cheaper and much faster. I've been early testing it and it's incredible." https://x.com/MatthewBerman/status/2104634635234005025
- Mixed (Sonnet vs Opus value): @DeryaTR_: "Benchmarks also appear very similar to Opus 5.5, so the advantage of using Opus is unclear, slightly better but more expensive?" https://x.com/DeryaTR_/status/2104660036186452057
- Mixed (tokens): @ArtificialAnlys: Sonnet 5.5 "scores 56 on the Artificial Analysis Intelligence Index, just 2 points behind Opus 5.5 (max), but at the highest Output Tokens per Task we've seen." https://x.com/ArtificialAnlys/status/2104640155843989864
- Negative (limits): @sepTND: "We can't follow your guide if we're running out of weekly limits!" https://x.com/sepTND/status/2104688823192224102
- Negative (quality/cost): @r3tsamffuH says Opus 5.5 "made more mistakes in the last few hours than opus 4.8" on mid-level Python (https://x.com/r3tsamffuH/status/2104691368249512079). @promptacisi calls the cost-per-task economy claim "a complete lie" (https://x.com/promptacisi/status/2104690955991621687).

**Caveats.** This is a small, non-random sample: 64 posts in total, 35 replies plus 29 general posts. Pool A covers only the first page of replies (35 of 158 shown) and no quote posts. Pool B inherits Techmeme's editorial selection, which favors high-follower and early-access accounts. Several of those accounts had pre-release access (the posts themselves say so for @MatthewBerman, @AlexFinn and @levie) or are vendor accounts (@cursor_ai). Posts by accounts I identified as Anthropic staff, from their post content or known roles, were read but excluded from the counts: @trq212, @alexalbert__, @ambricken, @bcherny, @addyosmani, @adocomplete, @_catwu, @mikeyk, @rlancemartin, @jacksonkernion, @lydiahallie, @sleepinyourhat, @amorriscode. Classification was done by hand by one reader. Direct X search (site:x.com) returned nothing, and nitter/xcancel mirrors were down. Read the split as directional, not as a measurement.
