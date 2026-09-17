**English** · [简体中文](README.zh-CN.md)

# bannysway

> I build small tools, and I try to publish the parts that were hard to get right.

Most repositories here are earlier practice work. One project is finished enough to be worth your time.

## 🧰 [grab-series-vocab](https://github.com/bannysway/grab-series-vocab)

An **agent skill** and a command-line tool in one folder. Point it at a directory of subtitle files and it builds a searchable vocabulary library — headword, gloss, IPA, difficulty — that exports to Anki, Markdown or a single-file web page.

It exists because of one measurement. I built a vocabulary deck one episode at a time, and when I finally merged all 33,270 cards, **35.9% of them turned out to be duplicates**: `pick up` had been collected independently 39 times, `check out` 35 times, `take off` 33. Duplicates are not only wasted effort — three copies of a word means three times the review load, and the interval scheduler is then optimising against the wrong data.

The fix was not a better prompt. It was a different data structure: **build the corpus first, and treat every export as a view of it.**

## 📚 The corpora — one show, one repository

| | Corpus | Scope | Headwords | Register |
|---|---|---:|---:|---|
| 🚔 | **[tv-vocab-nypd-blue](https://github.com/bannysway/tv-vocab-nypd-blue)** | complete · 259 ep | 9,938 | Police, legal and courtroom English — a register you will not meet in a textbook. |
| ☕ | **[tv-vocab-friends](https://github.com/bannysway/tv-vocab-friends)** | S01–S05 · 121 ep | 4,754 | Everyday spoken English of the 1990s: phrasal verbs, idioms, how people actually talk. |
| 🎹 | **[tv-vocab-your-lie-in-april](https://github.com/bannysway/tv-vocab-your-lie-in-april)** | S01 · 22 ep | 1,175 | The English subtitles of an anime — short, emotional, and a natural bridge for Japanese-speaking learners. |

Together: **402 episodes**, 22,477 collected cards, **14,413 distinct headwords**.

Each corpus is standalone. Download it, import the Anki file, start studying — the tool is not required. The per-show figures add up to 15,867 headwords, but the true unique count is 14,413: 1,314 words appear in more than one show. Nobody chose those twice by hand. That is exactly the duplication the tool exists to prevent, which is why the library tracks headwords globally rather than per episode.

## How to study with them

1. **Pull** the corpus for a show you already watch, in season and episode order.
2. **Drill in context.** Every entry records the season and episode it came from, so you know *where* you met the word, not only what it means.
3. **Watch with the subtitles off.** After every four or five episodes of drilling, watch those same episodes without subtitles. This is the step that does the work.
4. **Return to the corpus.** Anything that slipped, pull into your own hard-words deck.

Spaced repetition is good at making you *remember*. The episode is what tells you *when to use it*.

## Install the skill

```bash
npx skills add bannysway/grab-series-vocab --skill grab-series-vocab
```

It is a plain `SKILL.md` folder, so it works anywhere the Agent Skills standard is implemented — Claude Code, Codex CLI, WorkBuddy, Cursor, Gemini CLI. Per-agent paths are in the [install guide](https://github.com/bannysway/grab-series-vocab/blob/main/docs/INSTALL.md).

## No subtitle text, anywhere

No repository here contains a subtitle file, a transcript, or a dialogue translation. Every published entry is a headword, a gloss and an IPA transcription — nothing else. That is enforced by a script rather than by good intentions: the release audit fails the build if it ever finds otherwise.

## What is coming

- **Friends seasons 6–10.** The corpus currently stops at season 5.
- **10,926 entries whose headword was lost** — the gloss and the IPA survived, the English word did not. They ship with the NYPD Blue corpus as a separate repair queue rather than being guessed at. Recovering them is the most useful thing anyone could contribute.
- **Glosses in more languages.** Today every gloss is Simplified Chinese.
- **Difficulty labels.** `level` is unset, so level filtering does not do anything yet.

## Elsewhere

**Browse without installing anything.** Every corpus also ships as a single-file web page — the whole word list, with a search box, no server and no build step:

- 🚔 [NYPD Blue vocabulary](https://bannysway.github.io/tv-vocab-nypd-blue/)
- ☕ [Friends vocabulary](https://bannysway.github.io/tv-vocab-friends/)
- 🎹 [Your Lie in April vocabulary](https://bannysway.github.io/tv-vocab-your-lie-in-april/)

The remaining repositories are earlier practice projects, and [bannysway.github.io](https://bannysway.github.io/) is where the blog lives.

If any of this is useful, a ⭐ on [grab-series-vocab](https://github.com/bannysway/grab-series-vocab) helps other people find it.
