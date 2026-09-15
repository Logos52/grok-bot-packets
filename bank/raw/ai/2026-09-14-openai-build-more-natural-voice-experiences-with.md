---
id: 2026-09-14-openai-build-more-natural-voice-experiences-with
kind: article
title: Build more natural voice experiences with GPT-Live-1 in the API
source: "https://openai.com/index/introducing-gpt-live-1-in-the-api/"
author: OpenAI
published: 2026-09-10
captured: 2026-09-14
via: grok-bot/多恩刊
lane: ai
status: raw
private: false
---

GPT‑Live‑1 brings ChatGPT’s natural, full-duplex conversations to the API, with more control over how voice agents speak and act.

For the API release of GPT‑Live‑1, we’ve focused on new capabilities that let developers steer and customize voice experiences around their users, workflows, and goals. A core GPT‑Live‑1 strength, smooth interruption handling, is already delivering business impact: in early evaluations, Speak found that GPT‑Live‑1 gave learners more time to think before the language tutor responded, cutting interruptions by almost 80% versus previous turn-based systems.

Talk over it—naturally. Ask for help, then interrupt mid-response to change the question or add detail.Take it with you. Try a conversation while walking outside or with everyday background noise, and see how it stays with you.Make it playful. Laugh, hesitate, use short acknowledgments, or briefly talk to someone nearby—then continue the conversation.This demo is time-limited. By using it, you agree to OpenAI&#x27;s Terms and acknowledge our Privacy Policy.

Traditional voice agents stitch together speech-to-text, a reasoning model, and text-to-speech. Each handoff adds latency and creates more opportunities to lose timing, context, or the natural rhythm of a conversation. Developers are often the ones left coordinating those stages, including what happens when someone interrupts, pauses, or changes direction.

GPT‑Live‑1 handles listening and speaking in a single model, simplifying the voice layer. It can respond to interruptions and acknowledgements as they happen, while delegating deeper reasoning to the back end. This lets the conversation continue while work happens in the background.

Developers choose the models, tools, and agent harness behind the conversation. For example, they might pair GPT‑Live‑1 with a model like Luna for high-volume tasks like scheduling or order updates, and use a model like Astra for complex customer issues that require reasoning. That flexibility lets developers match reasoning depth, speed, and cost to each task.

GPT‑Live‑1 natively provides ASR transcripts and response text. It also offers strong alphanumeric understanding and supports keyword biasing. Although GPT‑Live‑1 is not a turn-based model, it natively supports turn detection, so developers can continue to build around explicit turn boundaries.

Across our evaluations, GPT‑Live‑1 improves Full Duplex Bench performance by 30 percentage points over GPT‑Realtime‑2.1, with large gains in turn-taking latency and interactive behavior. Paired with GPT‑6 Astra at medium reasoning effort, it also ranks #1 on Tau3, which measures frontier voice-agent intelligence on end-to-end tasks.

Evaluates spoken customer-service tasks in airline, retail, and telecom domains. Pass@1 measures task success; the headline gives each domain equal weight.

Evaluates spoken banking support with knowledge retrieval and account tools. Pass@1 is the fraction of 97 banking_knowledge tasks completed successfully.

Evaluates pause handling, conversational turn taking, interruptions, and backchannels.

Tests reactions to background speech, speech to another person, listener backchannels, and interruptions.

Tests tool use from spoken requests containing natural pauses, hesitations, and self-corrections. Pass@1 scores the tool-call sequence.

Evaluates the spoken answer to tool-using requests containing pauses, hesitations, and self-corrections. Scores how well the answer matches the reference intent.

Developers need voices that fit their product and sound natural to the people using it. With GPT‑Live‑1, we’re expanding from a small set of real-time voices to a broader selection across accents, dialects, and languages giving developers more choice in how their assistants sound.

We’ll continue to expand voice options and language availability over the coming months.

1import { Codex } from &quot;@openai/codex-sdk&quot;;23const thread = new Codex().startThread({4 workingDirectory: &quot;./repo&quot;,5 sandboxMode: &quot;read-only&quot;,6 approvalPolicy: &quot;never&quot;,7});89async function answer(live, delegationId, context) {10 const { finalResponse } = await thread.run(11 `Answer the latest question using this repo.12 Reply in two short spoken sentences.\n${context}`13 );1415 live.send({16 type: &quot;session.commentary.append&quot;,17 delegation_id: delegationId,18 content: finalResponse,19 });20}Connecting GPT-Live-1 to Codex. This excerpt shows how an application passes conversation context to Codex and returns its answer to GPT-Live-1. Connection setup and delegation handling are omitted.

For custom voice access, contact sales to learn more about eligibility and the request process.

Another way to build voice workflows on top of GPT‑Live‑1 is with OpenAI Presence, which uses the model to power real-time voice interactions. Presence helps enterprises deploy trusted AI agents that can answer questions, resolve issues, use company systems, take approved actions, and escalate to people when needed. Reach out to your OpenAI account director to learn more.
