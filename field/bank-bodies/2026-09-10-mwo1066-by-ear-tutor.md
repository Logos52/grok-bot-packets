# by-ear tutor

A language tutor you talk to. Nothing is typed, nothing is read: it speaks,
your microphone opens on its own, and it stops recording when you go quiet.

It teaches Vietnamese today. The engine is language-agnostic — the language
lives entirely in `content/`.

```
tutor   So — you?
you     bạn
tutor   Exactly. And again — what was healthy?
you     khỏe
tutor   That's it. Once more — what was not?
you     không

tutor   Put two of them together — you healthy?
you     bạn khỏe
tutor   Literally, it goes: you healthy not?
        Give me the whole thing — how are you?
you     bạn khỏe không
Minh    Bạn khỏe không?
```

*Three words, then the sentence climbed out of them one rung at a time — and the
tutor never says the Vietnamese it is asking for.*

*"How are you?" is `bạn khỏe không?` — literally **you healthy not?**. Nobody
guesses that, which is what the literal line is for: it is given out loud one
beat before the learner is asked to produce a sentence they have never heard.
The items, the glosses and the tutor's phrasings above are the course's own.*

## The method

Modelled on audio courses like Michel Thomas's and Paul Noble's, and on what
their transcripts actually show rather than on what they say about themselves.
Four things came out of measuring them:

**You build sentences, you don't repeat them.** The core move is "so how would
you say ___?", never "repeat after me" — a phrase that appears zero times in
twenty-five minutes of the reference course.

**Words are taught because a sentence needs them.** Nothing is introduced for
its own sake. `bạn`, `khỏe` and `không` arrive because `bạn khỏe không?` is about
to be built out of them, and the code guarantees a phrase never surfaces before
the words it is made of.

**The literal scaffold.** Before asking for a sentence whose word order differs
from yours, the tutor gives that order out loud — "literally you'll be saying:
you healthy not?" — which is what lets a beginner produce a sentence they have
never heard.

**Nothing is ever "learned" and retired.** Each word carries a level: fresh
words come back constantly, well-drilled ones rarely, and the odds never reach
zero. Spacing counts in words met, not in days or sessions, because the course
is one continuous line you stop and resume.

## How it works

The teaching sequence is decided in code, not by the model. Before each turn
the model is handed exactly one instruction — *introduce this word*, *ask what
that piece was*, *give the literal order and ask for the sentence* — and
nothing else. It supplies the wording, the warmth and the reaction to what you
just said. It never decides the structure.

That split exists because the model holds no state between turns. Left to
re-derive its position by re-reading the conversation, it drifted every time:
ten steps recited in one breath, the same word asked four times running, a
recall chain missing a piece.

Two voices carry the lesson, routed automatically by the language each sentence
is written in: yours-language for the tutor, Vietnamese for Minh, the native
teacher who only ever says the target word.

```
tutor.py       the lesson loop and the turn planner
content.py     the roster, and the rule that a phrase waits for its words
srs.py         word levels: how often each one comes back
voice.py       Azure text-to-speech, two voices, pipelined
listen.py      microphone, silence detection, Groq transcription
content/       the course itself: items and the tutor's persona
```

## Setup

Python 3.13+.

```bash
pip install numpy sounddevice webrtcvad edge-tts
```

Create a `.env` file next to the code:

```
GROQ_API_KEY=...
AZURE_SPEECH_KEY=...
AZURE_SPEECH_REGION=northeurope
```

Groq runs both the tutor's brain and the speech recognition; Azure does the
two voices. Groq's free tier allows about 8000 tokens a minute for the model
used here, which works out to roughly two and a half turns a minute — enough
for a real lesson, tight enough that the system prompt is kept small on
purpose.

Create the Azure Speech resource at pricing tier **F0**. It allows 500,000
characters of neural speech a month, resets monthly, and never expires — and
when the allowance runs out it refuses the request rather than billing for it.
Pay-As-You-Go has no spending limit that cuts: budgets send mail, they stop
nothing. F0 is the only hard stop Azure offers.

`edge-tts` is the backup voice, and is optional. It needs no key, cannot
expire, and serves the same `vi-VN-NamMinhNeural` this course teaches with, so
a dead Azure key costs a little audio quality instead of the whole lesson. It
decodes through `ffmpeg`, which must be on PATH for the backup to work.
`voice.py` also enforces its own monthly character ceiling, below the F0
allowance, so a resource created at S0 by mistake cannot run up a bill.

## Running

```bash
python tutor.py
```

Talk when it asks. Ctrl+C ends the session and saves your progress to
`state.json`.

```bash
python tutor.py --fresh --no-intro
python tutor.py --no-intro --from=nghin
```

Three flags for working ON the tutor rather than with it. `--from=` counts
everything up to a named item as already met and starts there, so a slice a
hundred items into the course can be **heard** without playing the hundred in
front of it. It saves nothing, for the same reason `--fresh` does not: it would
mark a hundred items as taught that never were. The match ignores accents.

Two flags for working ON the tutor rather than with it. `--fresh` starts from
the first word and saves nothing, so two runs are comparable. `--no-intro`
skips the opening speech — 55 seconds of synthesis standing between you and
whatever you are trying to test. Use both while iterating.

```bash
.\session.ps1 --no-intro
```

Runs a lesson and keeps the transcript in `logs\`, so a session can be read
afterwards instead of copied out of the terminal by hand. Anything after the
script name is passed to `tutor.py`. It exists because piping Python's output
buffers it — measured, three lines a second apart all arrived together at 3.5s —
so the flags that keep the lesson live on screen are easy to get wrong by hand.

```bash
python smoke_test.py
```

Runs a whole session with the network unplugged, in about a second. Worth
running after any change: it catches the wiring breaks that otherwise only
show up several minutes into a real lesson.

```bash
python simulate_session.py 14
```

Replays a full lesson in text with a small model playing the learner, for
judging a pedagogical change without having to talk.

## Adding a language

Copy `content/vietnamese/`, replace the item files and the persona. Items are
listed in teaching order, and a construction should spell out the words it is
built from — `tôi tên là + [tên riêng]` is recognised as `tôi` + `tên` + `là`,
which is what drives both the recall chain and the ordering guarantee.

## The documents

The glossary is in English. The rest is in French — those documents are read, not run.

| file | answers |
| --- | --- |
| [`GLOSSARY.md`](GLOSSARY.md) | **the glossary** — every term defined once, grouped by whether it is standard field vocabulary, a narrowed borrowing, or coined here. Read this first. In English. |
| [`SPEC.md`](SPEC.md) | what the code does today. 59 rules, each naming where it is enforced and what to edit. |
| [`METHOD.md`](METHOD.md) | the counts from the real recordings that the rules are derived from. |
| [`STATUS.md`](STATUS.md) | where the project stands — **the three axes the work is organised on**, what holds, what is still open. |
| [`STYLE.md`](STYLE.md) | ideas not yet activated, and the measurements behind them. |
| [`changes/`](changes/) | one folder per change, written before the code; `changes/archive/JOURNAL.md` indexes what was already tried. |
| [`notes/`](notes/) | working drafts — sentences waiting to be validated, a simulated lesson. Not part of the spec. |

## Licence

MIT — see [LICENSE](LICENSE). Take it, change it, keep the notice.


---
# METHOD.md

# What we actually measured

The rules in [SPEC.md](SPEC.md) are not a memory of how Paul Noble teaches. They come
from counting moves in real recordings. This file keeps the counts, because the audio
and the transcripts were downloaded into a scratch directory that has since been
deleted — these numbers are the only surviving record, and they are the reason the
tutor is built the way it is.

Source: two Paul Noble course extracts, ~25 minutes total, Japanese and Mandarin. Two
different languages on purpose: if the same pattern appears in both, it is the method,
not the language.

## The moves

Counted across the two extracts.

| Move | Japanese | Mandarin |
|---|---|---|
| "How would you say ___ ?" | 16 | 6 |
| "What was ___ ?" (isolated recall) | 16 | 5 |
| "And again / Now again" | 9 | 6 |
| **"Repeat after me"** | **0** | **0** |

Zero. In twenty-five minutes across two languages, he never once asks the learner to
repeat after him. The learner is always *building* an answer, never reproducing a
sound. This single number is why the tutor was rebuilt: the original persona was
written around "now you try, repeat after me", which is the one move the method does
not contain.

→ SPEC.md rule 18.

## How often a word comes back

Counted over ~8 minutes of effective teaching in the Japanese extract.

| Word | Times heard |
|---|---|
| to | 60 |
| I went | 28 |
| Tokyo | 24 |
| restaurant | 17 |
| with | 16 |
| Kyoto | 13 |

Sixty times in eight minutes for one word. Nothing is taught once. Nothing is ever
finished. This is the source of the level-based recurrence in `srs.py`: the weight of
an item decays but never reaches zero, so a word met long ago still comes back.

→ SPEC.md rules 16, 17.

## The pace

| | |
|---|---|
| Gross rate | 95 words/minute |
| Silence | 59 % of the running time |
| Rate while actually speaking | 232 words/minute |

The 59 % is not dead air — it is the learner answering. He speaks fast, then gets out
of the way for longer than he spoke. A tutor that fills the silence is not being
helpful; it is taking the exercise away.

→ SPEC.md rule on the three-sentence ceiling.

## Not re-verifiable

Two findings from the same listening pass survive only as recollection, because the
working files are gone: a count of "literally ___" as a scaffolding move, and the
observation that the extracts contain no negative corrections at all ("not quite",
"that's wrong", "try again"). They are recorded here as unverified. If the extracts are
ever downloaded again, count these two properly before relying on them.


---
# STATUS.md (head)

# Where the project stands

Last updated after the session that moved the mechanical turns into code.
`README.md` explains what the project is and how to run it; this file is the
working state — what holds, what is still open, and why certain things are the
way they are.

## The course teaches NORTHERN Vietnamese

**Decided by Meo, 2026-08-17**, after being asked one question too many about the
south. It is a constraint, not a preference: it settles word choices that are
otherwise a coin toss, and it should be checked before any of them is made again.

```
nghìn   not ngàn      thousand
quả     not trái      the classifier for round things
bố      not ba / má   father
```

The content already respects it in places — `nghìn`'s own note says *"Trong Nam
nói 'ngàn', ngoài Bắc nói 'nghìn'"* — but nothing said so at the top, so it kept
being re-asked. It also decides what to make of a dictionary entry marked
*"chiefly Northern Vietnam"* (take it) or *"Southern Vietnam"* (leave it), which
comes up on almost every person-word.

## The three axes

Decided 15 August, after a day in which every session was derailed by something
other than the teaching. **This is the frame the work is organised on** — a
pending item belongs to one of these three, and saying which changes who can do
it and when.

### 1 · The mechanism — nearly done

The turn planner, the levels, the guarantees. Fifteen days of work, 60 rules,
and a smoke test that catches wiring breaks. What is left: wiring the
sentence-as-vehicle model, and two or three known defects.

**Who:** the code. No content knowledge needed.

### 2 · The content — barely started

93 of the 149 taught words appear in no sentence. One hook out of 205. 1,915
words still without a gloss. Three of the eighteen goals blocked by content that
does not exist — the numbers past ten, serial verbs, the final particles.

**Who:** Meo, or a Vietnamese speaker. This is the long pole and no amount of
code shortens it.

### 3 · The ear — never worked on

The weakest link, and the one that has no pending work. From two real sessions on
15 August:

```
"Hãy subscribe cho kênh La La School"    a YouTube outro invented from silence
"Totem Latin"                            an attempt at tôi tên là Bình
"Tot en labin."                          the same attempt, second try
```

And the languages detected for one voice in one session: English, Korean,
Vietnamese, Korean, Finnish, Korean, Spanish, Hungarian, German.

**No session failed because of the teaching.** The plan was right every time.
They failed because the tutor did not hear what was said — and the fallout lands
on axis 1: the three-word free-speech threshold, `Hồng` accepted for `không`, a
step consumed by a hallucination.

**Who:** the code, and it is short.

### The order, and why

**Axis 3 first.** It is short, and it unblocks the other two: you cannot judge a
teaching method you cannot get through, and you cannot validate content the
microphone deforms.

Then axis 1, which is a few sessions. Axis 2 runs alongside whenever there is
review time.

---

## Sorting the rest: is it content, or is it not

The question that decides who can do a thing, and therefore what order things
happen in. **The test: does fixing it require writing Vietnamese?** Counted from
the files on 2026-08-17, not from memory.

### A · Content — someone has to write Vietnamese

- **121 teachable words appear in no sentence at all** — `ăn`, `uống`, `đã`,
  `rồi`, `chưa`, `nước`, `cơm`, `thích`… The course has **22 constructions for
  2064 words**. Sentences have to be authored; nothing writes them.
- **54 candidate sentences wait in `notes/SENTENCES-TO-VALIDATE.md`**, and they
  are ready: checked on 2026-08-17, **all 54 are built entirely from words the
  course already teaches**, no new word needed. Eight seeds, each pressed with
  the course's own features as buttons — one seed yields about six sentences and
  three words. Meo has to cross out what is not said. **This is the next thing on
  this axis, and it costs reading rather than writing.**
- The arithmetic, so the target is chosen and not assumed: a seed buys ~3 words,
  so **~43 seeds cover the 149 words the course already teaches**, ~143 cover the
  500 commonest, and ~590 cover every word in the files. The last is a book, not
  a chantier.
- **52 candidate sentences** in `notes/SENTENCES-TO-VALIDATE.md` waiting to be
  accepted or thrown out.
- ~~**7 features carry no tier.**~~ **Not a gap**: `tier` ranks *discrete*
  features, and a `strand` never finishes so it holds no position in a sequence —
  the glossary's own definition. The seven without one are correct. Checked
  2026-08-17, along with the 27 discrete features: all complete, 21 anchored to
  their word.
- ~~**Two strands have no mechanism to bring them back**~~ — both now have one.
  `đếm từ 11 đến 99` was renamed and sliced by `0012`; `ghép hai từ đã biết thành
  từ mới` fires through the **hook**, by `0013`, which was built and idle all
  along — the course carried **two hooks out of 205 items**. A compound now
  recalls its halves before it arrives.
  **But it fires exactly once today.** Of 25 compounds, one has both halves
  taught. **Eight more are waiting on the frequency shelf** — `sân bay` = `sân`
  (yard) + `bay` (to fly), `xin lỗi` = `xin` (to ask) + `lỗi` (fault) — and 411
  of the 2065 words in the files have every part present. **No word needs
  adding; they need pulling off the shelf.**
- Four of the remaining five strands are the address system under four names,
  which may be one thread split four ways. Meo has not ruled on it.
- **`_needs_fill` never asks for a hook.** An item with a `kind` and a `gloss`
  counts as complete, so `fill_item_metadata.py` will never revisit the 203 items
  carrying none. Found on 2026-08-17; not opened as a change.

### B · The 1915 missing glosses are not a task — do not fill them

**Every one of the 1915 sits in a single file, `90_frequency_stock.toml`. The
eight hand-written lesson files are glossed 100%.** The stock file says what it
is in its own header:

```
# Vocabulary imported by corpus frequency -- raw material, not a lesson.
# gloss is EMPTY on purpose
```

`fill_item_metadata.py` would fill them in one command, and it would not even be
guessing — each entry already carries its dictionary `senses`, so the model only
picks one. It is cheap and it is available.

**Do it and the course breaks.** Measured: **0 of the 1915 appear in any
sentence.** Fill them and the roster becomes 2120 words that can be asked and
**28 that have a sentence to live in** — 1915 words drilled in isolation, which
is the exact opposite of the model this course is built on: a word is met
because a sentence needs it.

So the stock file is a **shopping list**, not a backlog. It is where you go to
choose the next word worth building a lesson around — which is task A. The count
at startup (`1915 item(s) awaiting a gloss`) is noise, not debt.

*This entry replaces an earlier one calling the fill "the highest-leverage item
in the whole project". That was wrong: it measured the size of the number
instead of what filling it would do.*

### C · Not content — code and prompt

**All three are closed, none of them by writing code.** Observed in real sessions
on 2026-08-17: one was the instruction being followed correctly, and the other
two were refused by the person who hears the lessons. Every one of them was found
by reading `[diag]` output rather than by a lesson going wrong — which is the
lesson worth keeping from the whole set.

- ~~**The tutor says the word it is asking for.**~~ `!! the answer was given away:
  this turn asked FOR 'tôi' and said it` — four times across two sessions.
  **Refused 2026-08-17: Meo heard those same sessions and it did not register as
  broken.** A defect only a `[diag]` line can see is not worth a change. Written
  up as `0011` in the archive, including the cause, which turned out to be one
  instruction contradicting itself rather than the persona. Reopen only if a real
  session annoys him.
- ~~**Vietnamese lands inside an English sentence**, so the voice switches
  mid-phrase~~ — `!! Vietnamese landed mid-sentence (2 voice switches)`, three
  times. **Closed 2026-08-17 without a fix: Meo listened to it and does not mind
  it.** What it sounds like was checked before deciding — `You'll hear "tôi"
  again later.` is spoken as three fragments in two voices, and
  `"Tôi tên là Anna."` is torn in half, Minh saying `Tôi tên là` and the English
  voice saying `Anna` (a name is not in the Vietnamese vocabulary, so the router
  hands it back). Judged acceptable. **Do not propose again** without a new
  observation — the person who hears the lessons has ruled on this one.
- ~~**A line spoken twice**~~ — `Minh: Tôi tên là Lan.` twice in a row. **Not a
  defect: it is the instruction.** The `answer` step tells the model *"Have Minh
  say the full sentence twice"*, so hearing it twice is the design — the learner
  gets the finished sentence in their ear before being asked to vary it. It was
  listed here as a suspected bug without reading the step that produces it.

### And one that is neither

**Noise becoming text** — the `La La School` YouTube outro invented from silence.
Code, but it stays closed until it is **reproduced**: the probe that made Whisper
invent from room noise bypassed the microphone gate entirely, so it proves only
that Whisper invents *if noise reaches it*.

### What this says about order

**C first** — short, needs nobody else, and it is the tutor handing out the
answers it is asking for, which spoils every lesson it touches. **A after, and
forever** — sentences are the only real work, and `90_frequency_stock.toml` is
the shelf to pick words off while writing them. **B is not a task at all.**

---

## What works

A full lesson runs end to end by voice. Measured on real sessions:

- the opening speech, then one teaching move per turn, no drift
- a new word gets two turns (`introduce`, then `settle`) instead of vanishing
  after one
- a construction runs its whole chain: one recall per piece, the literal
  scaffold, the answer, variations, the rule named last
- recall targets are drawn by level, so a fresh word comes back constantly and
  a drilled one rarely, without ever dropping out
- a simple word runs end to end without the model: the introduction, the second
  ask, the rapid-fire are all sentences the code writes and speaks itself, so a
  word is never revealed without the meaning in the same breath
- progress is written as the session goes, so a crash costs nothing

`python smoke_test.py` runs all of that with the network unplugged in about a
second. Run it after any change.

## The decision everything else follows from

The model holds no state between turns. Every time it was asked to remember
where it was in a cycle, it drifted — ten steps recited in one breath, the same
word asked four times running, a chain missing a piece, the lesson teaching one
item while the sequence sat on another. Each of those was patched with more
prose telling it to remember, which is a reminder aimed at something with no
memory.

So the structure lives in code and the model supplies only the words. Anything
the code can know, the code decides:

| decided in code | left to the model |
| --- | --- |
| which item comes next, and that a phrase never precedes its words | how a word is introduced, and the warmth of it |
| what this turn is for — one instruction at a time | the hook, if there is a real fact to tell |
| which word a recall asks for, and the exact sentence that asks it | the scaffold, the variations, how a rule is put |
| when an item is finished, and whether an answer counted | replying to anything the learner says that is not an answer |

The same reasoning removed the `next_item` tool: a tool call cost 