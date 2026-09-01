---
id: 2026-09-01-david-stredansky-review-bugbot-missing-on-grok-launched
kind: article
title: /review-bugbot missing on Grok-launched cloud agents
source: "https://forum.cursor.com/t/review-bugbot-is-missing-on-cloud-agents-launched-from-grok-bot/170096"
author: David Stredansky
published: 2026-08-31
captured: 2026-09-01
via: grok-bot/Field
lane: ai
status: raw
private: false
---

/review-bugbot is missing on cloud agents launched from Grok Bot

<h3><a name="p-479176-where-does-the-bug-appear-featureproduct-1" class="anchor" href="#p-479176-where-does-the-bug-appear-featureproduct-1" aria-label="Heading link"></a>Where does the bug appear (feature/product)?</h3>
<p>Grok Bot</p>
<h3><a name="p-479176-describe-the-bug-2" class="anchor" href="#p-479176-describe-the-bug-2" aria-label="Heading link"></a>Describe the Bug</h3>
<p>Not sure if this is a bug or a gap, but it feels like I should be able to run Bugbot from cloud agents that Grok Bot creates.</p>
<p>Docs say /review and /review-bugbot are available in Cursor 3.7+ and at <a href="http://cursor.com/agents" rel="noopener nofollow ugc">cursor.com/agents</a>. High effort exists in the Bugbot dashboard. I expected a cloud agent started from Grok Bot to have that same skill, so I could say “review this PR with Bugbot, high effort, fix findings, loop” without a GitHub bugbot run comment and without sitting in the Agents UI / menu.</p>
<p>That is not what happens.</p>
<p>What I did<br>
Repo: private</p>
<p>From Grok Bot I launched (and later replied to) several Cursor cloud agents, one per existing PR. Each agent was told, in the launch/follow-up prompt:</p>
<p>Stay on the existing PR/branch. Do not open a new PR.<br>
Run Bugbot in this session via /review or /review-bugbot vs the PR base (usually main).<br>
Use high effort if the skill accepts it.<br>
Do not comment bugbot run / cursor review on GitHub.<br>
If the skill is missing, stop and list the skills you actually have. Do not fake a “Bugbot-style” self-review.<br>
I also tried the GitHub comment trigger earlier (bugbot run on the PR). That does not start Bugbot on this repo, which is why I wanted the in-session skill.</p>
<p>What happened<br>
Nine separate cloud agents, same result.</p>
<p>They looked at:</p>
<p>MCP tools (search for “review” hits PostHog review-queue tools, not Bugbot)<br>
~/.cursor/skills-cursor (env-setup, migrate-to-builds, subscribe, canvas)<br>
Installed plugin skills (Cloudflare, Stripe, Neon, PostHog)<br>
Native tools in the session: CreateGoal, GenerateImage, UpdateGoal<br>
There is a cursor-guide subagent that can answer product questions about Bugbot. That is not the review skill.</p>
<p>/review-bugbot and /review are not in the skill list. The agents stopped as instructed. They did not run real Bugbot. They could not attach the skill from inside the session.</p>
<p>Several of them said the only way to run it is for a human to open the agent page and pick /review-bugbot from the / menu in that chat, e.g.:</p>
<p>/review-bugbot compare against main<br>
Grok Bot’s CloudAgent reply cannot type that slash command for them. So from Grok Bot I can start the agent, give it the PR, have it fix code, but I cannot actually start Bugbot.</p>
<p>Why this is frustrating<br>
The loop I want is:</p>
<p>Grok Bot → cloud agent on an existing PR → real Bugbot (high effort) in that session → fix → re-run → report.</p>
<p>What I get instead:</p>
<p>Grok Bot → cloud agent that reviews itself unless I remember to forbid that → or an agent that correctly says “skill missing” → I still have to open <a href="http://cursor.com/agents" rel="noopener nofollow ugc">cursor.com/agents</a> and / the skill by hand, once per agent.</p>
<p>If the product intent is “Bugbot in the agent,” Grok Bot–created cloud agents should get the same /review-bugbot skill as agents I start from the Agents UI. If the intent is “only from the / menu,” the docs should say that cloud agents launched from Grok Bot / the CloudAgent API do not include it, and Grok Bot should be able to attach or invoke that skill on reply.</p>
<p>High effort is the other half: I want Bugbot High, not a coding agent pretending to be Bugbot. That only matters if the real skill is actually there.</p>
<p>Actual (2026-08-31): skill not attached. MCP “review” search is PostHog. Agent asks you to pick /review-bugbot from the / menu on <a href="https://cursor.com/agents/" rel="noopener nofollow ugc">https://cursor.com/agents/</a>.</p>
<p>Happy to share more agent IDs or transcripts if useful.</p>
<h3><a name="p-479176-steps-to-reproduce-3" class="anchor" href="#p-479176-steps-to-reproduce-3" aria-label="Heading link"></a>Steps to Reproduce</h3>
<p>From Grok Bot, launch a Cursor cloud agent on a connected GitHub repo (CloudAgent launch, existing repo, existing branch/PR).<br>
Follow up: “Run /review-bugbot in this session at high effort vs main. If the skill is missing, stop and list your skills. Do not comment on the PR.”<br>
Read the agent report.</p>
<h3><a name="p-479176-expected-behavior-4" class="anchor" href="#p-479176-expected-behavior-4" aria-label="Heading link"></a>Expected Behavior</h3>
<p>from current docs: the agent invokes /review-bugbot / /review.</p>
<h3><a name="p-479176-screenshots-screen-recordings-5" class="anchor" href="#p-479176-screenshots-screen-recordings-5" aria-label="Heading link"></a>Screenshots / Screen Recordings</h3>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/cursor1/original/3X/3/c/3c7cee6cb1008802727a5f9bb9601d80bf136620.png" data-download-href="/uploads/short-url/8D6jmRYtaFyubJNGEFLPj8YMLIY.png?dl=1" title="Screenshot from 2026-08-31 17-52-25.png" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/cursor1/optimized/3X/3/c/3c7cee6cb1008802727a5f9bb9601d80bf136620_2_690x447.png" alt="Screenshot from 2026-08-31 17-52-25.png" data-base62-sha1="8D6jmRYtaFyubJNGEFLPj8YMLIY" width="690" height="447" srcset="https://us1.discourse-cdn.com/cursor1/optimized/3X/3/c/3c7cee6cb1008802727a5f9bb9601d80bf136620_2_690x447.png, https://us1.discourse-cdn.com/cursor1/optimized/3X/3/c/3c7cee6cb1008802727a5f9bb9601d80bf136620_2_1035x670.png 1.5x, https://us1.discourse-cdn.com/cursor1/original/3X/3/c/3c7cee6cb1008802727a5f9bb9601d80bf136620.png 2x" data-dominant-color="EFEFEF"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2026-08-31 17-52-25.png</span><span class="informations">1049×680 74.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<h3><a name="p-479176-operating-system-6" class="anchor" href="#p-479176-operating-system-6" aria-label="Heading link"></a>Operating System</h3>
<p>Linux</p>
<h3><a name="p-479176-version-information-7" class="anchor" href="#p-479176-version-information-7" aria-label="Heading link"></a>Version Information</h3>
<p>Date: 2026-08-31<br>
Client: Grok Bot (Cursor desktop assistant) launching cloud agents<br>
Cloud agents: Cursor-managed VMs, <a href="http://cursor.com/agents/bc-%E2%80%A6" rel="noopener nofollow ugc">cursor.com/agents/bc-…</a><br>
Repo: GitHub clientup-group/clientup (private)<br>
Bugbot GitHub comment trigger on that repo also does not run (separate, maybe Automations / install)</p>
<h3><a name="p-479176-for-ai-issues-which-model-did-you-use-8" class="anchor" href="#p-479176-for-ai-issues-which-model-did-you-use-8" aria-label="Heading link"></a>For AI issues: which model did you use?</h3>
<p>grok 4.6 high</p>
<h3><a name="p-479176-for-ai-issues-add-request-id-with-privacy-disabled-9" class="anchor" href="#p-479176-for-ai-issues-add-request-id-with-privacy-disabled-9" aria-label="Heading link"></a>For AI issues: add Request ID with privacy disabled</h3>
<p>Example agent: <a href="https://cursor.com/agents/bc-50a353b8-41f1-4b84-8f67-1a617d8a77e2" rel="noopener nofollow ugc">https://cursor.com/agents/bc-50a353b8-41f1-4b84-8f67-1a617d8a77e2</a></p>
<h3><a name="p-479176-does-this-stop-you-from-using-cursor-10" class="anchor" href="#p-479176-does-this-stop-you-from-using-cursor-10" aria-label="Heading link"></a>Does this stop you from using Cursor</h3>
<p>No - Cursor works, but with this issue</p>

<p>Hey <a class="mention" href="/u/david_stredansky">@David_Stredansky</a>, thanks for the detailed report!</p>
<p>What you are seeing is how this currently works, not something failing in your setup. <code>/review</code> and <code>/review-bugbot</code> attach to cloud agents started from a supported surface (the Agents page at <a href="https://cursor.com/agents">cursor.com/agents</a>, the IDE, or the CLI). Agents launched by Grok Bot do not get those commands. That is decided when the agent is created, so a follow-up from Grok Bot cannot add the skill later. Picking <code>/review-bugbot</code> from the <code>/</code> menu on an agent Grok Bot created may still not run a real Bugbot review.</p>
<p>We’ve let the team know. In the meantime, the reliable loop is to open <a href="https://cursor.com/agents">cursor.com/agents</a>, start a new agent on the same PR branch, and include <code>/review-bugbot</code> in the first message (or pick it from the <code>/</code> menu). That agent can review, fix findings, and re-run in the same session.</p>
<p>On the separate point that commenting <code>bugbot run</code> on the PR does nothing: that trigger only runs when Bugbot is enabled for the repository, so it is worth checking your Bugbot settings in the dashboard.</p>
<p>I’ll post here when I have an update. Thanks for reporting this and thanks for being an early Grok bot user!</p>

<p>Thanks <a class="mention" href="/u/kevinn">@kevinn</a>! Yeah I already ran what I needed from the IDE, thanks.</p>
<p>the <code>bugbot run</code> was both that it was not enabled, and also not my PR - and as I found out it’s only for the author’s PR for individual plans, unlike Codex reviews.</p>
<p>If the agents started from Bot do not get the commands, It would be nice to have it customizable somewhere so we could add it. It feels like Grok Bot is for some users becoming the sole interface for Cursor Agents, but this is worsening the UX.</p>
<p>Thanks for the response and future update! <img src="https://emoji.discourse-cdn.com/fluentui/slight_smile.png?v=15" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
