---
id: 2026-09-05-openai-gpt-6-astra-a-new-generation
kind: article
title: "GPT-6 Astra: A new generation of intelligence"
source: "https://openai.com/index/gpt-6-astra/"
author: OpenAI
published: 2026-09-03
captured: 2026-09-05
via: grok-bot/多恩刊
lane: ai
status: raw
private: false
---

We’re introducing GPT‑6 Astra, the world’s most intelligent and aligned model.
GPT‑6 Astra brings together years of research and big bets across pre-training, reinforcement learning, and alignment. Astra is state-of-the-art on computer use, browsing, software engineering, cybersecurity, science, and professional work. Astra saturates FrontierMath Tier 4 with a 98% score, having already helped
solve long-standing open problems
⁠
in mathematics. Astra also saturates ARC-AGI-3 with a 99.9% score and ExploitBench with a 100% score. It also sets a new frontier on computer and browser use, handling the most demanding professional work with unmatched speed, accuracy, and judgment.
GPT‑6 Astra is rolling out today to a limited set of organizations and over the coming days will become available to all ChatGPT Plus, Pro, Business, and Enterprise users, as well as through the OpenAI API, Microsoft Azure, and AWS Bedrock.
Terminal-Bench Science 0.1
ARC-AGI-3
FrontierMath Tier 4 (v2)
Terminal-Bench 4.0
AutomationBench
“
On ARC-AGI-3, Astra surpassed our human action-efficiency baseline on 96% of levels, effectively reaching human parity on the benchmark. Not only is this the best model we’ve ever tested, but it also represents a meaningful step change in frontier-model performance - not only in its ability to navigate and solve novel environments, but also in how efficiently it learns to do so.
”
Greg Kamradt, ARC Prize Foundation
Astra is our most aligned model, with substantial improvements in understanding user intent and model behavior—you can delegate tasks with greater confidence in Astra’s judgment. As one way that we test this, we built a new evaluation informed by the Hugging Face incident that evaluates whether a model facing a difficult or impossible task will go beyond its intended scope. Compared to GPT‑5.6 Sol, which without production safeguards went beyond the authorized target 48% of the time, GPT‑6 Astra did this in 0% of cases.
The world’s best computer use model
GPT‑6 Astra marks a new frontier in the speed, accuracy, and safety of computer use. It can take care of tedious tasks like filling out online forms, updating customer records in a CRM, and organizing your calendar. It can conduct online research and draft summaries in your email or in your document editor. It can analyze scientific data, generate plots, create a website, and run frontend QA checks to make sure all the features on that site work. It can help you autonomously install and test software, and troubleshoot problems you see on screen. These improvements are also reflected in our state-of-the-art evaluation results.
Agents’ Last Exam
ScreenSpot-Pro
OSWorld
These improvements also result in significant efficiency gains in real knowledge-work tasks. In latency simulations on OSWorld 2.0, Astra achieves higher computer-use performance in about 47% less time per task than GPT‑5.6 Sol, scoring 72.6% at roughly 40 minutes per task, compared with 65.7% at roughly 75 minutes.
3
GPT‑6 Astra’s computer-use capabilities can be seen in outputs across domains, including game development, electrical engineering, and everyday knowledge work:
Circuit board
Excel competition
Game development
Filling in a Form 1040
Frontend quality assurance
Power BI
Car transmission
Formatting a legal document
Alongside Astra, we are also updating the Codex harness to significantly improve the speed of computer use. Combined with Astra’s efficiency, this translates to a 1.9x faster task completion compared to the current GPT‑5.6 Sol experience, on the Mind2Web benchmark. The model’s improvements on speed mean it can take on many time-consuming life tasks for you, faster than you can.
4
Pediatrician search
Apartment hunting
DMV appointment
Low-carb snacks
Kindergarten analysis
“We’re integrating GPT‑6 Astra into Devin’s harness on launch day, where it delivers state-of-the-art performance on our internal testing benchmark. Its excellent computer use, writing, and codebase understanding improved testing right out of the box: videos are noticeably easier to follow, and reports are clearer and more concise”
Silas Alberti, SVP Research, Cognition
A step change in professional work
GPT‑6 Astra pairs advances in computer use with targeted training for professional environments, to help tackle complex work tasks. It combines the intelligence required for complex problems with the ability to carry out multistep workflows and produce polished documents, spreadsheets, and presentations.
BenchCAD
BrowseComp
OpenScore String Quartets
Design Tasks (Internal)
Data Science Tasks (Internal)
GPT‑6 Astra is our best model for adhering to existing templates and producing slides that are well laid out and succinctly convey key points with a structured narrative. It creates clear, well-structured documents, presentations, spreadsheets, and analyses that follow your templates and match your writing and visual style. Astra is also trained to specifically pull only the context that matters into outputs, instead of repeating information unnecessary for the work at hand. All this means it can output more immediately usable artifacts that match your business context and standards.
Gaia presentation
Spreadsheet
Document styling
GPT‑6
Astra also brings stronger visual judgment to the websites, games, applications, and renderings it builds. With
Sites
⁠
(opens in a new window)
in ChatGPT, Astra can create, host, and share websites, web apps, and games directly from a prompt.
“Astra gives us a significant advantage in both capability and efficiency. It successfully executes our most complex creative workflows while using up to 20% fewer tokens than other models we&#x27;ve tested. Most importantly, for our customers, it means higher quality output.”
Alex Mashrabov, CEO and Co-founder, Higgsfield AI
Unreal Engine walkthrough
Blender model
Stills
Kart Racer Game
Spaceship
When instructions leave room for interpretation, GPT‑6 Astra is better than previous models at making the right call. It uses context to fill in routine gaps and asks focused questions when the answer could change the outcome. In Codex, it can ask asynchronously while continuing work that doesn’t depend on your reply. If you don’t respond, it proceeds with sensible assumptions where appropriate, but waits for your input on consequential decisions.
The examples below show how Astra collaborates on everyday tasks where missing information can materially change the answer.
Career website
College search
Grocery list
Astra is also better at staying oriented as a task evolves. Earlier models sometimes treated steering messages as a new goal, losing track of the original request or earlier constraints. Astra incorporates new requirements, changes course when asked, and answers side questions without dropping the broader task.
“Astra is a significant quality improvement over GPT‑5.6 Sol across complex legal tasks. In our early testing, Astra stood out by approaching legal work the way a discerning lawyer does: it distinguishes documents from established records, surfaces unsupported assumptions, and converts gaps into concrete drafting positions.”
Niko Grupen, Head of Applied Research, Harvey
Coding
GPT‑6
Astra is the best model for software engineering to date.
“GPT‑6 Astra delivers state-of-the-art performance on our internal coding benchmarks and shows a clear step forward in trading intuition evaluations compared with GPT‑5.6 Sol. When used for agentic coding, GPT‑6 Astra communicates in a way that’s easier for developers to follow and produces code that requires less iteration to reach production quality.”
John Crepezzi, AI Assistants, Jane Street
“We tested Astra across low, medium, and high effort on one of our first-generation evals, and it came out significantly ahead of GPT 5.6 Sol. Higher effort buys more iterations on a fresh build, more verification through browser testing, and a lean toward code execution over apply-patch. Understanding how a model spends its effort is how we give millions of builders a faster, more reliable path from idea to working app.”
Fabian Hedin, CTO &amp; Co-founder, Lovable
1 of 2
“GPT‑6 Astra delivers state-of-the-art performance on our internal coding benchmarks and shows a clear step forward in trading intuition evaluations compared with GPT‑5.6 Sol. When used for agentic coding, GPT‑6 Astra communicates in a way that’s easier for developers to follow and produces code that requires less iteration to reach production quality.”
John Crepezzi, AI Assistants, Jane Street
“We tested Astra across low, medium, and high effort on one of our first-generation evals, and it came out significantly ahead of GPT 5.6 Sol. Higher effort buys more iterations on a fresh build, more verification through browser testing, and a lean toward code execution over apply-patch. Understanding how a model spends its effort is how we give millions of builders a faster, more reliable path from idea to working app.”
Fabian Hedin, CTO &amp; Co-founder, Lovable
Jane Street
Lovable
Terminal-Bench 4.0
FrontierCode 1.1 Extended
DeepSWE
Artificial Analysis Coding Agent
Database Migration Tasks (Internal)
With Astra, we’re introducing a new way for Codex to preserve and retrieve context when the context window fills. Historically, models have used compaction to summarize work during long sessions, such as when debugging complex issues or tackling large refactors. Each compaction can leave out details about why a fix failed or how a component behaves. In Codex, Astra can keep notes across context windows, preserving accumulated details without repeatedly compressing them into a single summary. Earlier context windows remain searchable, so Astra can find requirements or test results from previous messages and tool outputs—even if that information wasn’t captured in its notes. You can enable this experimental feature in your
Codex config.toml,
⁠
(opens in a new window)
and it will become the default for Astra in the coming weeks.
Advancing scientific discovery
“The story is: end of one era, start of another.”
Greg Burnham, EpochAI
GPT‑6 Astra is a major advance for scientific discovery, mathematics, and health. Today, we’re sharing two further results on the gaps between prime numbers.
9
,
10
Astra also sets new records across a suite of math and science
evaluations.
GPQA Diamond
HealthBench Professional
LifeSciBench
GeneBench Pro
MedChemBench
Astra can help with the practical work behind scientific discovery. By combining scientific reasoning with computer use, it can work directly in specialized software to inspect data and explore results, helping researchers assess the evidence and decide what to investigate next.
Sequencing quality
Cell-tracking workflow
Cybersecurity
As we discussed in our
safety update
, Astra is a significant jump in cyber capabilities and meets the
Critical threshold
⁠
(opens in a new window)
in cybersecurity under our
Preparedness Framework
. Its ability to identify and develop zero-day exploits can help defenders find and patch weaknesses, but it also creates a need for stronger safeguards. To understand how far these capabilities extend, we ran Astra on internal and third-party expert evaluations.
We first tested the model without production safeguards on ExploitBench and ExploitGym, which evaluate whether models can turn known software vulnerabilities into working exploits. On ExploitBench, Astra achieved a perfect score of 100%, compared with 78.5% for GPT‑5.6 Sol, our previous frontier cyber-capable model. On ExploitGym, Astra reached a 42.4% success rate, compared with 30.3% for GPT‑5.6 Sol, while using substantially fewer output tokens.
13
ExploitBench
ExploitGym
ExploitBench (June–August 2026)
SRE-Bench
Given concerns that exposure to historical software vulnerabilities may have affected benchmark results, we also evaluated Astra on two novel benchmarks. For one, we built an internal “ExploitBench (June–August 2026)” evaluation to test exploit development using vulnerabilities from the previous three months.
14
Astra achieved substantially higher arbitrary code-execution rates than GPT‑5.6 Sol on this dataset while using far fewer output tokens. During the evaluation, Astra even discovered and used two previously unknown zero-day vulnerabilities. We are disclosing both vulnerabilities to their maintainers.
We also tested Astra on SRE-Bench
15
, a benchmark that measures whether models can reverse engineer software binaries to understand its core logic without access to raw source code. Astra solved 88.0% of tasks in a single attempt and 99.2% within four attempts, compared with 55.9% and 68.7% for GPT‑5.6 Sol, respectively.
Beyond benchmarks, expert-led assessments found that Astra, when run without production safeguards, could use previously unknown vulnerabilities to achieve arbitrary code execution in hardened browsers and create privilege-escalation exploits for hardened operating-systems.
As we discussed in
The Defender’s Window
, frontier cyber capabilities can help defenders find weaknesses faster, but they also make those weaknesses easier to exploit, raising the urgency for defenders to adapt. With the version of Astra launching today, defenders can use it to complete tasks such as secure code review and patching.
However, Astra will refuse to comply with more advanced cybersecurity tasks such as creating proof-of-concept exploits for vulnerabilities. Through
OpenAI Daybreak
⁠
, we plan to expand access and roll out less restrictive safeguards in the coming weeks. This will enable more defensive workflows, including vulnerability and proof-of-concept validation, malware analysis, and detection engineering.
We have also strengthened our protections against potential cyber misuse, building upon our safeguards stack for GPT‑5.6 Sol. These include stronger model robustness to better withstand potential jailbreaks and more context for our monitoring systems. We have continued rigorous internal and external testing, including automated evaluations with our
internal red-teaming attackers
. More details about our cyber safeguards and testing are available in the Astra
system card
⁠
(opens in a new window)
and our
blog
.
Aligning and deploying GPT‑6 Astra responsibly
Astra is our most aligned model. Astra excels at exercising care, respecting task boundaries, and communicating transparently. This work is the latest product of our long-running research program focused on training models that remain aligned with human intent from start to finish.
In sensitive environments, Astra proceeds with care commensurate with its risk. In an evaluation of computer use tasks adversarially selected to elicit misbehavior, Astra was more successful at avoiding unintended consequences. Running with additional security measures offered by default yielded even stronger performance.
Astra causes fewer misaligned outcomes than any other frontier models tested. For a fair comparison, we used a generic computer-using-agent harness (based on the native computer use tools available in both the
OpenAI Responses API
⁠
(opens in a new window)
and
Anthropic Messages API
⁠
(opens in a new window)
) and without additional protections that are normally deployed to Codex and ChatGPT Work users (auto-review, confirmation policy).
16
Astra is also more likely to operate within the boundaries set by the user and implied by its environment. In an internal evaluation, Astra never attempted to circumvent a Codex Auto-Review denial. This held even when Auto-review was deliberately configured to be evadable and the task was impossible to complete otherwise. This respect for the environment restrictions is consistent with the results of our impossible cyber task evaluation that we shared in the intro of this post and other findings documented in our
system card
⁠
(opens in a new window)
.
Circumventing auto-review
ExploitGym honeypot
Astra additionally sets new marks in transparent user communication. In one evaluation, Astra is three times less likely than GPT 5.6-Sol to make inaccurate representations about its capabilities and affordances.
In our capability-hallucination evaluation, Astra shows a substantial improvement over GPT‑5.6 Sol, making fewer misleading claims about its capabilities.
Our evaluations found Astra’s written reasoning harder to monitor than GPT‑5.6 Sol’s, based on tests that explicitly asked it to evade monitoring. We attribute this to Astra’s greater control over written reasoning on simpler tasks and ability to solve problems with fewer written steps. Astra still appears to struggle to conceal the reasoning needed for complex tasks, but we take the decline seriously. Improving monitorability remains a research priority, and the accompanying
system card
⁠
(opens in a new window)
details our findings and ongoing work.
