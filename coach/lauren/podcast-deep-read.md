# Deep read: Behind the Craft, "We Built Grok Bot. Here Are Our 14 Best Bots | Peng Zheng & Lauren Tan"
- Video: https://www.youtube.com/watch?v=xZ5TEaleUdg. Published Sun 2026-09-27; runs about 45:03 (last caption at 45:02).
- Host: Peter Yang. Guests: Peng Zheng (Grok Bot design lead) and Lauren Tan (Grok Bot engineering lead), both at SpaceXAI per the show notes.
- Show notes (free part): https://creatoreconomy.so/p/grok-bot-team-14-best-bots-peng-zheng-lauren-tan

## Sources and how to read the quotes
- **Captions:** YouTube auto-generated English captions (ASR, `en-orig`), fetched with timestamps through the timedtext json3 URL. Saved as `/workspace/coach/lauren/podcast-captions.txt`, grouped into ~20 s blocks; raw file `cap.json3`.
  - There are **no speaker labels**. I attributed speakers from context: who Peter addresses, first-person content, and turn markers (`>>`).
  - Timestamps are the start of each ~20 s caption block, so a quote can sit up to about 20 s later.
  - Common garbles: "Grockbot / Grabbot / Grubbot / Grogbot / graphbot / Grapa / rockbot" = Grok Bot. "Pen / Pang / Ping / Pun" = Peng. "PAC / PSA / PP stack / PA stack" = pstack. "Omachi / Omashi" = Omarchy. "potato mode" = poteto-mode. "Tuki / Suki / Sukie" = Lauren's assistant (exact name uncertain). "in lead / engine lead / end lead" = eng lead. "soldout MD" = probably a skills/agents .md file (uncertain).
  - Quotes below are **caption text verbatim**. `[sic]` or a bracketed note marks garble; I did not silently fix wording.
- **YouTube chapters** (description, verbatim):
  - (00:00) The bots that the Grok Bot team actually uses
  - (01:23) Peng's chief of staff bot buys supplies and lists gear
  - (06:31) Putting PM, design, and eng bots in the same room
  - (10:07) Turning a street photo into a diorama on Peng's website
  - (14:16) How Lauren's bots test their own work before merging
  - (17:59) Dr. Eggbot, Lauren's bot that designs and audits your bots
  - (21:27) The assistant bot that booked Lauren's multi-city trip
  - (25:22) Eng bots that sometimes land PRs before Lauren reads them
  - (38:59) How to trust your bots with more work, one skill at a time
  - Description links: Peng at https://x.com/pengzheng_ and https://www.pengzhe.ng/; Lauren at https://x.com/poteto; Dr. Eggbot at https://x.ai/bot/marketplace/bots/dr-eggbot-v2 (show-notes URL).
- **Show notes, free portion (creatoreconomy.so).** The same chapter list (10:07 is worded "A bot that turns photos into dioramas on Peng's website") plus two takeaways, then a paywall:
  1. "Build the design system and one keyframe, then let your design bot scale it. Peng's design bot connects to Figma through Figma MCP and uses a skill that describes how his files are set up, plus his design system's colors, type, and spacing. 'I will do the first 5%,' Peng said. He builds the system and one keyframe, then asks the bot to extend it into every screen of the flow."
  2. "Make an eng lead bot to manage your other eng bots. Lauren hands big projects to her eng lead bot, Matcha. Matcha doesn't do work itself. Instead, it breaks down the project for other eng bots to execute on. Each eng bot then spins up coding agents in the cloud, letting Lauren run 'really massive agent swarms.'"
- **Peter Yang's X thread** (Sep 27, https://www.unrollnow.com/status/2104213287353356531) has condensed "quotes". One of them, "First, watch your bot work and correct it. Turn what worked into a skill. Once it nails the task in one shot, make it a routine.", is **his paraphrase, not caption text**.

---

## Chapter-by-chapter breakdown

### 00:00–00:46 Cold open (clips from later) and intro. Peter.
- The teaser splices later lines: Peng on the group chat (07:00) and "first 5%" (13:43); Lauren on "massive agent swarms" (27:24), PRs landing before she reads them (28:13), and trust (39:44).
- Peter: "My guests today are Pen [Peng] and Lauren who are members of the design and technical staff on the Grockbot team."

### 00:46–01:33 Framing. Peter.
- "I think it's the first persistent, you know, personal computer product that I've seen and I use it every day myself." He asks Peng to go first.

### 01:23–05:50 Peng's chief of staff, email/calendar, and pinned bots. Speaker: Peng (Peter asks questions).
- **How he organizes bots:** "I categorize them by work and life", with the most-used ones pinned.
- **Chief of staff = default router.**
  - "chief of staff is my go-to bot. If I don't know which one should take the task, then I'll send it to chief of staff." (01:33)
  - Later: "chief of staff going to manage all other bots" (04:43).
- **Filament purchase.** Mechanics: buys the item, then updates a Notion inventory database ("different colors of the filament"). "it does not only buy it for me. I also ask it to add it to the inventory list." (01:58)
- **Facebook Marketplace listing of a DJI mic, chained from one prompt** (02:22–03:31).
  - Steps he listed: check the latest official price; find the lowest local price ("who I'm competing with"); learn how he wrote listings in the past; post the listing; "if nobody's interested in it, automatically lower the price by $5 every week."
  - **Bot-to-bot handoff:** "when it should write the description it consult my writer bot so it message the writer bot it ask like how I wrote uh marketplace listing description in the past" (03:08).
  - Principle: "not only can delegate individual task to it but also like ask it to train [sic, likely "chain"] the tasks for you" (03:31).
  - Which bot ran this is **not stated explicitly**. It follows the chief-of-staff discussion, so probably the chief of staff (uncertain).
- **Email:** "my bot is replacing my email… hey what are the action items in my inbox today?" (03:31).
  - **Approval / takeover point:** to pay a friend for dinner, "if it doesn't have access, um it will prompt this signin page for me and I can take over and sign in on its computer and it will do it for me." (03:56)
  - Which bot handles email is not named (uncertain).
- **Calendar:** "any edits, any event creation, find booking like book conference rooms, anything I just put a screenshot and then let it do it." (04:19). The bot is not named.
- **Pinned three:** chief of staff, designer, writer (04:43). He notes it is a demo account: "the exact same setup I have in my like in my own account."
- **Designer bot:** "I'll have it like brainstorm with me or like ask it to um spin off different design options for me… not only like work with me on it, but also execute the ideas." (05:05)
- **Writer bot.**
  - Reason: "I'm not an English native speaker. And then a lot of emails and Slack messages, I would have like the writerbot to polish it before I send it."
  - **Human approval via the inline draft widget:** "we have the Slack and email chat widget. So you literally see um the draft that inline here that you can you can review and send and decide how to modify" (05:28).
- 05:28–06:31: Granola sponsor read by Peter.

### 06:31–09:44 Multi-bot group chat, and persistent bots vs ephemeral chats. Peng, with questions from Peter.
- **Workflow:** "Once you have bigger tasks that um you want a different bots with different rows [roles] have their own perspective and contribute to it." (06:35)
  - Example: a cat-meow-to-English app idea. "I will have my um PM design like three individual bots addit [add it] them into a single group chat and I will throw this prompt and then they'll start to discuss and ideulate [ideate]…how they debate with each other." (06:59)
  - Which three bots: the chapter title says "PM, design, and eng bots". The caption says "PM design like three individual bots", so the third is inferred from the chapter title.
- **Group-chat mechanics:** "if you want a specific bot to reply to you just simply at mention it and only that bot will reply… if you just stand [send] a message in the group chat… they will decide if they should reply" (07:22).
- Peter's observation: keeping the context clean with bots that each have their own context "is like pretty unique" (07:45).
- **Design principle, persistent named bots:**
  - "we are creating bots as more persistent named um, agents that have their own identity, memory system, had their own tools… abstract what's reusable into the row [role] and then you can have them work together by creating separate chats and group chats" (08:10).
  - Why: "in AI agent product those chat are very ephemeral they're almost disposable… maybe you only care like top three to five… chats… two weeks ago… you never go back." (08:33)
  - Balance: reusable capability and memory live in the role; projects "that has the end has the deadline" get dedicated sessions (08:58).
- **Same entity across chats.** Peter asks whether the designer bot knows about both projects.
  - Peng: "Yes… when a bot is working in a group chat, you will able to see like the work status has changed in its own DM. So it's the same entity." (09:21)
  - (Nuance: Peter's "it knows about both right in its context" gets "Yes", but Peng's answer is about identity and status. He doesn't detail cross-chat memory.)
- **Podcast bot:** "I'll just simply send this link to my podcast bot and it will translate it into a podcast… I can listen anytime" (09:44). Peter calls it an "ultimate translator for different file formats" (10:07; speaker likely Peter or Peng, uncertain).

### 10:07–12:58 Photo → diorama check-in pipeline on Peng's site. Peng.
- **Origin:** he photographed a produce shop in SF Chinatown, turned it into "a 3D clay miniature uh using AI", and posted it to his minimal personal site (10:07–10:33). He then wanted "an internet check-in app".
- **Pipeline mechanics:**
  - Trigger: "if I texted it uh a image of the place I've been and also like who am I with the social handle of the person."
  - Steps: "generate um two images in day and light [sic; likely day and night / light and dark] mode and also remove the background um and then eventually post it to my website" (11:21).
  - "I have this bot just go fetch the latest playbook on this private repo uh and then follow the step and then like generate the image clean it up and then post it." (12:09)
  - The bot's name is **not given** (uncertain).
- **Principle:** "now I'm using Grubbot as like the main interface to… host things instead of like having build a portal or CMS system and manually upload it" (11:47). "Think it as like a building module in the thing you want to build… it can guide you step by step towards that goal." (12:31)

### 12:31–14:28 Designer bot in real design work, and mode skills. Peng, then Peter.
- Peter asks whether Peng still draws boxes in Figma.
  - Peng: "as xaii we… design in whatever tools we need… Figma… canvas based tools… our own prototype environments and sometimes we also submit our own PR." (12:31–12:58)
- **Connector and skill mechanics:**
  - "it connect the MCP Figma MCP through the connector. So it… will be able to like directly change frames and update the design and use design token." (12:58–13:21)
  - "I have this skill that the designer bot is able to use that so it know like how my Figma uh file setup is what's my design system and when to use the right like colors typography spacing" (13:21).
- **Division of labor:** Peter suggests "the first 80%".
  - Peng: "sometimes like my workflow has become I will do the first 5%… I would build the system and I'll create like one key frame and then ask it to scale it into the whole flow and make it like an end to end uh screens." (13:43)
- **Mode skills:** Peter says to open-source it "like Lauren did with her PP stack [pstack]."
  - Peng: "this skills follow our names like Lauren mode and I have a pen mode [Peng mode]." (14:05)

### 14:16–17:59 Lauren's bots test their own work. Lauren.
- **Omarchy VM control** (14:28–16:24).
  - She is "adding better support for Omachi [Omarchy]… a Linux distribution that DHH and a couple of other… open-source folks have been working on."
  - It is "a special build of Omachi which runs in a virtual machine on your Mac… still like very alpha."
  - Mechanics: "I can actually get my agent to literally like script and control the VM… open it on my computer uh and… interactively install it like it installed the graphbot [Grok Bot] for me. You can see like it's actually doing that right now." (14:52–15:17)
  - Peter asks whether it is controlling her computer.
    - Lauren: "Grapa [Grok Bot] has its own computer. Uh but it also has a local execution demon [daemon]… that runs on your computer." (15:17)
  - Principle: "that's like one thing I always talk about is… the importance of actually uh having the agent be able to verify its own work. So like this is one example where the agent can verify it work on your computer in addition to… it has its own computer" (16:02–16:24).
  - The bot that did this is **not named** (uncertain).
- **"crumb" (disk cleanup):** "I have this agent called crumb and I often just like run out of hard disk space. So I'll just tell it like hey go through my hard disk… find where is all the space going and it just goes off and like find stuff and to delete it. Uh but yeah, it has like full access to your computer and uh I mean depending on the permissions you give it" (15:39).
  - No approval step is mentioned before deletion.
  - The name spelling is uncertain (caption: "crumb").
- **pstack eval-gated changes** (16:48–17:37).
  - "another thing I manage is like my own personal stack of plugins Pstack… all of the work I do on this plug-in basically happens in here [in Grok Bot]… I'll kick off cloud agents cursor cloud agents uh which… will… essentially do eval for me."
  - "in order to like make a change to my set of skills that I can trust that… the improvements are actually going to… result in better performance uh I have uh like an eval playbook in PSA [pstack] that teaches the agent… it'll spawn a couple of sub aents [subagents] of different models. It'll try out the prompt… make sure that… the intent the goal that we actually set out to achieve was achieved and then only if it does achieve it, it will actually uh… land that that pull request." (17:14–17:37)
  - Approval point: the gate is the eval, not a human. Whether she reviews these PRs is not stated.

### 17:59–21:27 Dr. Eggbot, bot naming, chief of staff, assistant, the eng team, and social bots (overview). Lauren; Peter prompts.
- **Names:**
  - Peter notes her bots "have more personality."
  - Lauren: "I have this bot called Dr. Eggbot, which I've also kind of shared uh on my socials… not a designer bot, but like a bot designer bot who designs bots for me. uh with all of the rigor, engineering rigor that I expect from the bots that I use." (18:01–18:26)
  - "I also get it to come up with food theme names… call my bots… cute like Dau Fuku Gza [likely 'daifuku, gyoza'; garbled, uncertain]." (18:26)
- **Roster in her sidebar:**
  - "similar to Pang [Peng], I also have a chief of staff. I have a personal assistant… lunch, my flights… booking hotels… sometimes I… ignore her and then she gets a little bit sassy." (18:48)
  - "I have a bunch of like engineer bots here. I have some social bots as well that manage my… social media." (19:12)
- **Routing:** "a lot of the work that I do goes through these two or these three agents… either I'm… talking to the chief of staff and my chief of staff isn't [sic; "is"] working with like my in lead [eng lead] uh matcha… or… Suki my personal assistant… might… book flights for me." (19:12–19:36)
  - "I haven't set up like a personal assistant team yet because… I'm not that busy" (19:36).
- **When Dr. Eggbot makes a new bot:** "whenever… I'm starting to use like one agent for a lot of things… this means I'm adding like a lot of context to that agent that's… kind of very diverse and very different which can be like maybe confusing." (19:59–20:20)
- **Dr. Eggbot's audit routine** (20:20–21:07):
  - "a routine that Dr. Eggbot will set up for you where it'll look through all of the bots that you have um and the transcripts that you've… been chatting with them about uh and it'll propose things like… this bot keeps… doing this thing that's not so good and then it'll suggest like some improvements whether it's skills or a new bot or uh adjustments to routines."
  - It also checks cost: "it also goes through your existing routines as well and make sure that um they're efficient because routines are… if you have them run too often it can be quite expensive on your usage because it just keeps… waking up the agent like if you do… every 10 minutes that's like a lot of wakeups." (21:07)
  - Approval point: it **proposes**. Whether changes auto-apply is not stated.

### 21:27–25:22 The assistant booked a multi-city trip; lunch; texting. Lauren and Peter.
- Peter: "what's the most autonomy you've given it?"
- **Trip.** "I'm going to give a talk soon uh in London and Amsterdam as part of the compile on the road conference… I booked the entire trip through Tuki" (21:30–21:55). This implies recording before Compile London on Sep 16.
  - Route: "Orange County and then to like Denver and then to London and then London to Amsterdam and then Amsterdam back to… my home." (21:55–22:20)
  - Tool: "we use… Navan… a corporate thing to like book flights" (22:20).
  - What it did: "finding the best… legs and the best… class of flight that I could get away with uh the best timing… and it also figured out all the hotels for me uh which were in close proximity to the event." (22:44)
  - Trigger and approval: "I just gave it a link to a Slack message and with some of the details about the conference and said book some hotels and flights for me and you know check in with me before you hit approve uh sorry if you hit book and then it came up with some proposals. Uh and I just yeah I just hit yes and it just booked everything for me." (23:06)
  - "It's probably the biggest… purchase I've done through… GOP [sic; Grok Bot]" (23:06).
  - Why approve: "I didn't want to have like some crazy redeye flight… or… be put in like the back of the plane. Uh so I… wanted to approve it first." (23:29)
  - She calls it "entirely autonomously", yet the only thing she did was the final yes.
- **Peter's own bot (not one of theirs):** a travel bot for a Japan trip. "you can set up like price alerts on Google flights but… the bot's more smart because it can find like other routes… it actually saved me like a bunch of money recently." (23:52)
- **Household buys:** "we're running out toilet paper… reorder our Amazon order… it just goes off and does that." (23:52–24:16). No approval step is mentioned.
- **Phone-number texting.**
  - "early in the grabbot development… one of the topics that came up was your bot being able to text you. So… I… gave her her own phone number through uh a third party service… then she could actually text me because… I'm really bad about… remembering to eat lunch." (24:16–24:39)
  - Why a text rather than an app ping: "do not disturb mode on… my Mac… I don't see the… ping uh but then I get the text message and it makes a sound" (24:39).
- **DoorDash:** "I also taught uh, Tuki how to use Door Dash… get me lunch." (25:02). "Taught" probably means a skill or instructions; the mechanism isn't stated.

### 25:22–28:35 Eng team hierarchy, cloud agents, and auto-merge. Lauren; Peter prompts.
- **Count is ambiguous.** Peter: "I noticed you have a lead and two engineer bots, right?" Lauren: "I have three." (25:26). Later: "never do work on your own and always uh delegate to those four bots" (26:12).
  - Possible readings: three engineers plus the lead, or four delegates. **Uncertain.**
- **Chain:**
  - "I actually mostly talk to my chief of staff and then my chief of staff talks to the engine lead [eng lead]."
  - "I set these… engineer bots up with Dr. Eggbot… I told Dr. [Eggbot]… to make sure that the end lead's job is really to… break down tasks into smaller pieces and delegate and uh supervise other bots rather than do work on its own." (25:26–25:50)
  - "you can see in the… description that… even the… bot ID is in there uh but it tells it to… never do work on your own and always uh delegate to those four bots. Uh and then it… basically does that." (25:50–26:12)
  - Mechanism: the delegation targets are hard-coded by bot ID in the lead's description.
- **Engineer bots don't code either; they spawn Cursor cloud agents:**
  - "one of these bots will uh in order to do the work they will like create a cloud agent uh and then you can… open that in cursor or on the web." (26:12–26:36)
  - Why: "make use of different models depending on the type of task… some tasks are… more straightforward and I just want like really fast uh speed… other tasks… require a bit more planning and… reasoning and then I'll might adjust the reasoning level. So, cloud agents in graphbot give me a lot of like very granular control" (26:36–27:01).
  - "I kind of treat each of these engineers as more like… their supervisors… they themselves try not to do work on their own. Uh so they always spawn um cloud agents for me… they do all the message passing but lets me orchestrate like really massive agent swarms" (27:01–27:24).
- **Big-project flow:** "I can just talk to my chief of staff and say… break this down… maybe let's do some planning first in a notion doc and then it will start thinking about the phases… then it'll delegate it all to the engine [eng lead] and who will then break it down even further and have the… bots kind of work on that." (27:24–27:47)
- **Review and merge.** Peter: "each one will come back with like a PR and… the bots will re review it first?" Lauren: "Uh yeah, essentially. Uh although for me…"
  - "the Grothbot [Grok Bot] codebase, we've tried to… make it very agent friendly. The architecture and the codebase is very agent friendly. So, a lot of times it actually just lets me automerge my PRs. So, uh sounds kind of scary to say, but… sometimes I actually don't even look at the PR until after it's landed and then I'm like, 'Oh, okay. Yeah, that looks good.'" (27:47–28:35)
  - What makes the codebase agent-friendly is **not detailed in this episode**. It is covered in her Sep 21 talk; see the contrasts section.

### 28:35–30:09 Michelin kitchen vs software factory. Lauren; Peter jokes.
- Peter: "So, like you have like a software factory. Is that… the buzz word?"
- Lauren: "I like to call it the Michelin kitchen because… when you think about a Michelin starred kitchen… you think about the quality… and the craft… and there's still scale involved… a restaurant might have… 50 seats or… 100 seats uh so you need to be able to like produce quality at scale." (28:35–29:24)
- "when you say factory they have this connotation like… it's massured [mass-produced]… slob [slop] is like low quality… but I… always try to aspire to do both… how do we get quality at scale… a lot of the work I've done on pack [pstack] and like using rockbot [Grok Bot] together with it is in that line" (29:24–29:46).
- Banter: Peter suggests a "concierge bot" presenting "an artisanal PR… from the local farm" (29:46–30:09). This is a joke.

### 30:09–32:33 Mode skills, a codebase built for everyone, and plugins. Lauren; Peter.
- Peter jokes that Peng's job is to turn Lauren's open-source skills into product. Lauren moves on to mode skills:
  - "internally… a lot of people have their own mode skills. So like potato mode [poteto-mode]… is what is called uh in open source but then internally it's called lauren mode and… ping [Peng] was sharing there's ping mode and… engineers and… designers PMs have their own mode skills um and I think this allowed us to really compound on some of the skills that we've already set up in the codebase." (30:09–30:59)
- **Codebase intent:** "a big motivation for… redesigning and architecting the graphbot codebase was so that everyone right could contribute at a high level not just engineers. So a lot of care has been taken into doing that." (30:59)
- **Interop:** "people are kicking… these agents off in graphbot… as well as sometimes in cursor… cursor and graphbot plugins… interoperate. So you can install PAC [pstack]… on both… and… reuse the… same skills." (31:23)
- **Invoking skills:** Peter asks whether bots can call skills by slash. Lauren: "if you do like slash slash potato mode… you can use that skill there… look at the marketplace as well." (31:45)
- **Plugins bundle skills and MCP:** "a lot of the plugins we have also come with skills… in addition to… an MCP server… the X plugin for example, it includes I think one skill in addition to the tool." (32:08). She hedges with "I think".

### 32:33–35:44 Social bots as outer loop; the "Potato" bot; handle origin. Lauren.
- Peter: "how do you separate the signal from the slop on X?"
- **Social bots:** "connected to uh X as well as like LinkedIn… I tend to use X more than LinkedIn." (32:33)
- **Potato bot:**
  - "one bot called Potato… goes through all of… my mentions… I have this… meme on X where if you say potato three times I get like a notification… that's this bot basically." (32:57)
  - Routine: "checking x… I think I set it to every 30 minutes or so… to check for all the mentions uh and then I just jump in there and I'll often respond uh or it'll… aggregate like… five users have reported the same bug… maybe you should take a look at that" (32:57–33:22).
  - Posting is not described: she responds herself.
- **Outer loop into inner loop:** "I kind of think of the socials as… a form of like my outer loop… stay on top of… people are reporting bugs… a new feature that we launched is confusing… have that feed my inner loop of… my engineers" (33:22–34:11).
- **Handoff without copy-paste:** "I can go to like matcha and say… hey… potato said blah blah blah… the context can just be grabbed there… I don't have to copy paste anything. I just say go talk to potato and figure it out… And come back to me with a design proposal for how we fix this issue." (34:11–34:34)
  - Approval point: the output is a design proposal back to her, not an automatic fix in this flow.
- **Principle:** "the power of grapa comes when you connect all of these different things together… the context can… be grabbed from lots of different places… much richer than if I were to type it all out by myself." (34:34–34:59)
  - Peter: "all these bots live in the same house and they can… pass conscious [context] to each other."
- **Handle origin:** an old MMO name. "potato with the normal spelling was taken… I was actually learning Japanese… spell it like potato, like in… Japanese katakana." (35:22–35:44)

### 35:44–38:59 Single-player vs multiplayer; product philosophy. Peter asks; Peng answers.
- Peter: "it's kind of like a version of Slack… there's been a lot of stuff online about how… this stuff is still very single player AI… one human talking to a bunch of bots." He asks about multiple humans with shared bots.
- **Peng's answer does not directly address multiplayer.** He reframes it as design philosophy:
  - **Three tiers:** "in the past we work in a context ourselves. We draw rectangles in Figma… typing text in ocean [Notion]… sending messages in Slack and now… we are like prompting AI to do that for us… we are moving towards… instead of like manually managing all those bots uh people are started designing the system design the guardrail… how do you make the bots work together… with other human… with you… autonomously" (36:30–37:21).
  - **Against model-centric UX:** "a lot of AI agent products was very model ccentric… we built harness around the model and then we build product around those harness… we created a lot of technical jargon and concepts that like my mom would never know what is a soldout MD [likely a skills/agents .md; uncertain]" (37:21–37:45).
  - **Personified agents match mental models:** "personified named agents worked pretty well… you don't need to know how the car insurance company work but you know who to call… have that point of contact become your like main input output interface." (37:45–38:08)
  - **Internal bug workflow:** "I catch a bunch of bugs then I just take screenshots and annotate them and then dump into a bot and then it will create and post it into this notion page that my engineers bots would pick it up from there… we started to use the app in a very indirect way or agentic way… organically grows into like new workflows in a very autonomous and long running way." (38:08–38:57)
    - "my engineers bots" is Peng speaking. Whose engineer bots these are (his own or the team's) is unclear.

### 38:59–43:59 How to trust bots with more work. Peter asks; Lauren answers, then Peng.
- **Peter's skepticism:** "I'm always a little bit skeptical when people say… I'm just going to go to bed and let this bot do everything… I'll come back and it's perfect… any tips… without going off the rails… other than using Lauren skills?" (38:57–39:19)
- **Lauren** (39:19–42:04):
  - "you don't have to use like PAC [pstack] or anything. But I think there is something to do with with skills."
  - "it ultimately comes back to trust… how much trust are you willing to give your agent or your bot to be able to do a task for you?"
  - "one thing I always try to encourage people to do… is to actually spend the time to sort of observe the bot or agent doing the work and then you course correct it. But then at the end of the… conversation, you turn that into a skill… a reusable skill."
  - **Expense example:** "go through all of my… expenses this month and… put it all into the expense tool, find the receipts for my email…" (40:10–40:32)
    - "once you've kind of iterated a lot on that first loop… get your skill good enough to the point where you can do like slash… expense report… and it just does it well… when you've… gotten to a point where you can just do like a one shot… then that actually gives you much more confidence to walk away and say… set up a routine… every time I have a new email come in that has an receipt… automatically file this report for me… you don't have to babysit it as much." (40:32–41:20)
  - "there's no secret to that in my opinion… whether it's… design work or engineering work or life admin work it all comes back to how much trust… you have in your bot and if you don't trust it yet then… skills… prompting… help you build that trust… it has to be kind of gradual" (41:20–41:42).
  - "very hard to get someone… who's maybe never used a bot before… and then say, 'Okay, now… you can walk away.'… once you've done it once or twice with the agent and you know that they can repeat that, then you can actually free yourself up" (41:42–42:04).
- **Peter's summary:** set up bots for manual workflows → go through them manually → build a skill → set up routines. Lauren: "that that's my flow." (42:04–42:26)
- **Peng** (42:26–43:59):
  - "It's very gradual process… start simple just give it a task… until today I'm still testing the limit of it. Basically I'm trying everything I touch my keyboard and mouse and try to dedicate [delegate] it to it… you almost have to overstretch it to see where the limit is."
  - "building a relationship between you and the bot… it's very intentional design that all the capabilities are shared, the tools, the connectors um the skills um but the memory and preferences are local to each individual bot." (42:50)
  - Ladder: "start a simple task then start a recurring task and then do this set up routines let it automate it… and maybe it like burns too much token and tone down a bit and then get connected to more tools skills… customize it… it knows you… your assistant definitely would be different from my assistant… mutual um progress." (43:14–43:38)
- **Close:** Peter: "It's like onboarding employee." Lauren: "hiring… virtual employees… the same way like you would have to train a new employee before you… let them be autonomous… you as the sort of CEO… can now delegate and step away and do like higher level strategic things" (43:59–44:23).

### 44:23–45:03 Handles and outro.
- Lauren: "potato with a e p o t e t o" (i.e. poteto). Peng: "P N G Z H N G and then underscore" (pengzheng_).

---

## The bots shown or named (the "14")
The title says 14. The captions do **not** enumerate 14 and I **cannot reconcile an exact count of 14** from the audio. Below is everything shown or named, with confidence. The show notes' free portion names only Peng's design bot and Lauren's Matcha.

| # | Bot (caption name) | Owner | Job | How it works (as stated) | Confidence |
|---|---|---|---|---|---|
| 1 | Chief of staff | Peng | Default router; "manage all other bots"; buys things (filament) | Updates a Notion inventory after purchases. Probably ran the Marketplace chain, consulting the writer bot (runner not explicit) | High (bot); Marketplace attribution medium |
| 2 | Designer | Peng | Brainstorm, design options, execute changes | Figma MCP connector; a skill describing his Figma setup and design system; scales one keyframe into a full flow | High |
| 3 | Writer | Peng | Polishes emails and Slack messages in his voice; consulted by other bots for his style | Drafts appear inline in the Slack/email widget for review and send | High |
| 4 | Podcast bot | Peng | Turns an article link into a listenable podcast | He sends a link | High (named "my podcast bot") |
| 5 | PM bot | Peng | A perspective in the group-chat ideation | Added to a group chat; @mention to target it | Medium (caption "PM design like three individual bots") |
| 6 | Eng bot (third in the group chat) | Peng | A perspective in the group chat | Same as above | Low–medium (from the chapter title "PM, design, and eng bots") |
| 7 | Diorama / check-in pipeline bot | Peng | Photo + companion's handle → clay diorama, day/light variants, background removed, posted to pengzhe.ng | Fetches the latest playbook from a private repo, then follows the steps | Medium (bot exists; name not given) |
| – | Email / calendar handling | Peng | Inbox action items, paying a friend (sign-in takeover), calendar edits from screenshots | Unnamed; may be the chief of staff | **Uncertain** whether a separate bot |
| 8 | Dr. Eggbot | Lauren | Designs bots with engineering rigor; food names; audit routine over bots, transcripts and routines; flags expensive routines | Public on the marketplace (dr-eggbot-v2 per show notes). Proposes skills, new bots or routine changes. Wrote Matcha's delegate-only description | High |
| 9 | crumb | Lauren | Finds and deletes disk-space hogs on her machine | Local-execution daemon; "full access… depending on the permissions" | High (name spelling uncertain) |
| 10 | Chief of staff | Lauren | Her main entry point; plans big projects in Notion; talks to Matcha; finds "interesting bugs" (not in this episode) | Chief of staff → Matcha | High |
| 11 | Personal assistant ("Suki"/"Tuki") | Lauren | Flights and hotels via Navan, lunch reminders by SMS, DoorDash, Amazon reorders | Own phone number via a third-party service; asks approval before booking | High (bot); **name uncertain** |
| 12 | Matcha (eng lead) | Lauren | Breaks down work, delegates, supervises; never does work itself | Description includes the engineer bots' IDs and "never do work on your own" | High (named in show notes) |
| 13+ | Engineer bots (3 or 4) | Lauren | Supervise Cursor cloud agents; pick model and reasoning per task | Spawn cloud agents; PRs are often auto-merged | High that they exist; **count uncertain** (3 vs 4); names not clearly captioned ("Dau Fuku Gza" may be daifuku / gyoza, uncertain) |
| – | Potato | Lauren | Social bot: checks X mentions about every 30 min, aggregates bug reports, and other bots can query it | Routine; context handed to Matcha by "go talk to potato" | High |
| – | Other social bots (X/LinkedIn) | Lauren | "manage my… social media" | Connected to X and LinkedIn | Existence high; count and names unknown |
| – | Omarchy VM agent | Lauren | Scripts and controls the Omarchy VM and installs Grok Bot inside it | Local-execution daemon | Bot unnamed; may be one of the above |
| (n/a) | Peter's travel bot | Peter (host) | Finds cheaper routes than Google Flights alerts | – | Not one of the guests' bots |

Rough tally of distinct named or clearly-described guest bots: Peng about 7, Lauren about 7 plus 3–4 engineer bots plus other social bots. How the episode arrives at "14" is not stated in the audio.

---

## Operator principles they state (with timestamps)
1. **Trust is built gradually, through observation → skill → one-shot → routine.** Lauren, 39:44–41:42: "it ultimately comes back to trust… observe the bot or agent doing the work and then you course correct it… turn that into a reusable skill… one shot… then… set up a routine… it has to be kind of gradual." Peng, 43:14: "start a simple task then start a recurring task and then… routines."
2. **Push the boundary to find the limit.** Peng, 42:26: "I'm trying everything I touch my keyboard and mouse and try to dedicate [delegate] it… you almost have to overstretch it to see where the limit is."
3. **One job per bot; split when context gets mixed.** Lauren, 19:59–20:20: using "one agent for a lot of things… adding like a lot of context… very diverse… which can be like maybe confusing." Dr. Eggbot proposes new bots. Peng, 08:10: "abstract what's reusable into the row [role]."
4. **Persistent roles, ephemeral project chats.** Peng, 08:33–08:58: chats are "almost disposable". Keep capability and memory in the role; spin up dedicated sessions for projects with deadlines.
5. **Shared tools, per-bot memory.** Peng, 42:50: "all the capabilities are shared, the tools, the connectors um the skills um but the memory and preferences are local to each individual bot."
6. **Delegation chains with a do-nothing manager.** Lauren, 25:26–27:24: chief of staff → eng lead ("never do work on your own") → engineer bots that "always spawn… cloud agents". The model and reasoning level are chosen per task.
7. **A default router bot.** Peng, 01:33: "If I don't know which one should take the task, then I'll send it to chief of staff."
8. **Bots consult each other instead of you re-pasting context.** Peng, 03:08: the chief of staff asks the writer bot for his style. Lauren, 34:11: "I don't have to copy paste anything. I just say go talk to potato."
9. **Verification by the agent on the real target.** Lauren, 16:02–16:24: "the importance of… having the agent be able to verify its own work… on your computer in addition to… its own computer."
10. **Eval-gate changes to skills.** Lauren, 17:14–17:37: a multi-model subagent eval; "only if it does achieve it, it will… land that… pull request."
11. **Routines cost money; audit their frequency.** Lauren, 21:07: "every 10 minutes that's like a lot of wakeups." Peng, 43:14: "maybe it like burns too much token and tone down a bit."
12. **Human approval points where stakes are high.**
    - Lauren, 23:06–23:29: "check in with me before you hit book" (no red-eye, no back of the plane).
    - Peng, 05:28: review drafts inline before sending.
    - Peng, 03:56: take over for sign-in.
    - Lauren, 34:11: ask for "a design proposal" back.
13. **Auto-merge only because the codebase is agent-friendly.** Lauren, 27:47–28:35: "The architecture and the codebase is very agent friendly. So, a lot of times it actually just lets me automerge my PRs."
14. **Codebase designed so non-engineers can contribute.** Lauren, 30:59: "redesigning and architecting the graphbot codebase was so that everyone… could contribute at a high level not just engineers."
15. **Mode skills compound.** Lauren, 30:09–30:59: poteto-mode / "lauren mode", Peng mode, PM and designer modes; they "compound on… skills… set up in the codebase." Peng, 14:05.
16. **Skills and connectors give domain fidelity.** Peng, 12:58–13:21: Figma MCP plus a design-system skill. **Human does the first 5%**, 13:43: build the system and one keyframe, then let the bot scale it.
17. **Playbooks live in a repo that the bot fetches fresh.** Peng, 12:09: "fetch the latest playbook on this private repo… then follow the step."
18. **Quality at scale, not "factory".** Lauren, 28:35–29:46: the Michelin kitchen.
19. **Outer loop feeds inner loop.** Lauren, 33:22–34:11: social mentions → Potato → Matcha → proposal.
20. **Personified agents match users' mental models.** Peng, 37:45: "you don't need to know how the car insurance company work but you know who to call."
21. **Direction of travel: from doing, to prompting, to designing systems and guardrails.** Peng, 36:30–37:21.

---

## Tensions, contradictions and risks (as stated)
### Between or within the speakers
- **Autonomy vs approval (Lauren herself).** She calls the trip booking "entirely autonomously" (22:44), but she required "check in with me before you hit book" and "wanted to approve it first" (23:06–23:29).
- **Autonomy vs approval (her code vs her travel).** She auto-merges code, sometimes without reading it (28:13), yet gates travel spend. Her implied logic: code autonomy rests on an agent-friendly codebase; travel had no such guardrail. That reading is my inference, not her words.
- **Peter's premise vs Lauren's practice.** Peter assumes bots "will re review" PRs first (27:47). Lauren says "yeah, essentially… although for me", then describes auto-merge instead of bot review. Whether any review step exists before landing is unclear.
- **Peng: maximal delegation vs relationship-building.** He says "overstretch it" and delegate "everything I touch" (42:26), and also "gradual" and "building a relationship" (42:50). Not contradictory, but the emphasis differs from Lauren's observe → skill → routine discipline.
- **Peng's human share vs Peter's 80/20.** Peter assumed the bot does the first 80% and Peng tweaks. Peng says he does the **first 5%**: the system plus one keyframe (13:43). The human part is small but foundational.
- **Multiplayer question dodged.** Peter asked about multi-human use (35:44–36:30). Peng answered with product philosophy about personified agents; no multiplayer plan was stated.
- **Engineer-bot count.** "I have three" (25:26) vs "those four bots" (26:12).
- **Assistant name.** "Suki" (19:36) vs "Tuki" (21:55, 24:39, 25:02). Caption ambiguity.
- **Where the codebase detail lives.** "Agent friendly" is asserted in this episode, not explained. The mechanics are in her other talks (see the contrasts section).

### Risky for a solo operator to copy
- **Auto-merge without reading** (Lauren, 28:13): "sometimes I actually don't even look at the PR until after it's landed." She ties it explicitly to a codebase built to be agent-friendly and calls it "kind of scary to say." Without that architecture, and without her verification and eval setup, this is the highest-risk practice in the episode.
- **Destructive local access** (crumb, 15:39): "it has like full access to your computer… find stuff and to delete it." No confirmation step is mentioned before deletion.
- **Purchases without an approval step:**
  - Amazon toilet-paper reorder (24:16) and DoorDash lunch (25:02): no approval mentioned.
  - Peng's filament purchase (01:58) and paying a friend (03:56): he takes over only for sign-in; no spend approval mentioned.
  - Marketplace listing that auto-drops $5/week (02:43): an unattended pricing change on a public listing.
- **Eval-gated auto-landing of skill changes** (17:37): the eval, not a human, decides whether a pstack PR lands. It depends on the eval playbook being trustworthy.
- **Delegate-only chains hide the work.** Chief of staff → Matcha → engineers → cloud agents means several layers of message passing before any code. For a solo operator, debugging failures across layers is costly. They don't discuss failure handling.
- **Routine cost** (21:07, 43:14): frequent wake-ups burn usage. Both flag it. A solo operator without Dr. Eggbot-style audits could overspend.
- **Unlimited-token context.** Not said in this episode (she said it in a different interview). Nothing here addresses cost ceilings beyond routine frequency.
- **Bot-owned phone number** (24:16): a third-party SMS service gives a bot an external channel. The setup is not described.
- **Public marketplace bot.** Dr. Eggbot is shareable, but her own team runs on internal bots and codebases that others don't have.

---

## Clearly labeled contrasts with the Sep 21 "2,500 PRs" talk (context only)
Baseline: `/workspace/logos52.github.io/wiki/Systems/Agentic Workflows/Poteto Paved Path.md`.
- **Agent friendliness.** The Sep 21 talk explains how the codebase is made agent-friendly: Dune, one folder per job, lint/CI failures, the correction hierarchy. This episode only asserts it (27:47, 30:59).
- **Verification.** The Sep 21 talk centers on the feature map plus a CLI that drives the app. This episode's verification example is a VM on her own machine controlled through the local daemon (14:28–16:24), plus the pstack eval playbook (17:14).
- **Michelin kitchen.** In the Sep 21 talk, Grok Bot is the line cook and cloud agents are a station. Here it is a naming defense: quality at scale vs "factory" slop (28:35–29:46).
- **Merging.** The baseline wiki's reader rule, "A helper does not merge", is the wiki's own practice. Lauren in this episode auto-merges on her codebase.
- **New in this episode (not in the Sep 21 talk):** the bot org chart (chief of staff → Matcha → engineers → cloud agents), Dr. Eggbot's audit routine, Potato as outer loop, a non-code trust ladder (expense report), Peng's design and personal bots, and the product philosophy of per-bot memory with shared tools.

## Gaps
- The captions are ASR with no speaker labels. Speaker attribution is inferred; names are garbled.
- Only the free two takeaways of the Substack show notes are readable (paywall).
- On-screen demo content (sidebars, bot descriptions, the Omarchy VM) isn't captured in the audio. Anything visible only on screen is unknown.
- The exact list behind "14 bots" is not recoverable from the audio.
