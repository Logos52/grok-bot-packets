# Hànyǔ Lab

An audio-led Mandarin course for everyday conversation. The site is static; there is no application build step.

Run locally:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`. Progress is saved in the browser and can be backed up from the course sidebar. Audio is generated locally and served from the same server.

## Learn through lesson albums

Each lesson opens as an album of tracks: a real conversation, useful phrases, a mini-story, the same story from another point of view, a grammar spotlight, mixed practice, and a hands-free listen-again queue. Tracks unlock in order. A reference page at `#/hello/notes` collects the transcript, phrase details, grammar, pronunciation, culture, stories, practice picker, and printable cheat sheet.

The first album is **你好，邻居！ Hello, neighbour!**. Phrase review lives at `#/phrases`, and spaced review lives at `#/review`. Learners choose a Chinese name and reuse it throughout the dialogue and story questions.

## Project structure

- `js/core.js` and `app.js`: lesson order, saved state, route registration, navigation, and settings.
- `js/components/audio.js`: shared audio player and local clip fallback.
- `js/components/narrator.js`: full-screen track player and hands-free narration queue.
- `js/components/drills.js`: reusable listening, speaking, writing, reading, matching, and sentence drills.
- `js/components/vocab.js`: phrase shelf and three-direction spaced repetition.
- `js/lessons/hello-album.js` and `hello-notes.js`: first lesson album and notes routes.
- `narration/hello.json`: source for lesson lines, Chinese audio inventory, phrases, tracks, stories, drills, and notes. `narration/hello.js` is generated from it.
- `docs/method.md` and `docs/roadmap/data.js`: teaching method and course plan.
- `js/components/motion.js` and `styles/motion.css`: orchestrator-owned animation and interaction APIs. Call `HanyuLab.Motion`; do not edit either file.

Read [docs/adding-a-lesson.md](docs/adding-a-lesson.md) and [narration/STYLE.md](narration/STYLE.md) before creating lesson content. Check JSON with `uv run tools/voice.py lint narration/<id>.json`, then build Edge audio with `uv run tools/voice.py build narration/<id>.json --engine edge`. MiniMax audio is rendered later by the orchestrator. Generated audio stays under ignored `audio/` and is never deployed.

--- docs/method.md ---
# The Hànyǔ Lab method

Hànyǔ Lab follows AJ Hoge's Effortless English system, adapted to Mandarin. Every lesson follows it; when a design question comes up, the method decides.

## The rules, and what they mean here

1. **Learn phrases, not single words.** The unit of study is a phrase you can say: 认识你很高兴, 你叫什么名字, 我也是. Cards, drills and review use phrases; a single word appears only inside a phrase.
2. **Ears first.** You hear everything before you see it. A new text plays with no transcript; characters and pinyin come after several listens.
3. **Deep learning.** A lesson is not "done" when you finish it once. You listen to its tracks on several separate days (target: 7). The app tracks listening days per lesson and recommends moving on after 5 days or when the mini-story answers are instant.
4. **Mini-stories are the core.** A short, silly, vivid story told in Chinese, with a stream of very easy questions. You answer out loud, fast, then hear the model answer. Most of each lesson's time is here.
5. **Point-of-view stories.** The same story retold from another angle (he → I → you; later now → yesterday → tomorrow, 了, 过, 会, 要). Grammar is absorbed by hearing the same meaning in different forms.
6. **Real, spoken Chinese.** Texts sound like people talk: particles (啊, 呢, 吧), short replies, reactions. No textbook Chinese.
7. **Energy.** Exaggeration, surprise, jokes, big reactions from the tutor and the characters. Emotion makes phrases stick.

## Our tweaks

- **Grammar Spotlight.** Effortless English teaches grammar only through POV stories. We add one short, explicit grammar track per lesson, placed *after* the stories, explaining the pattern the learner has already heard many times, with examples taken from the stories. Never rules first.
- **Vocabulary practice.** A practice track after the stories: spaced-repetition phrase cards and quick drills (listen and choose, match, build the sentence, speak it, write key characters).
- **Pronunciation clinic.** Mandarin needs tone work. Tones are coached inside the vocabulary track (contours, minimal pairs, sandhi), briefly, never as a separate theory lecture.
- **Pictures for meaning.** Mini-stories show a simple animated picture per story beat, so meaning is clear without translation. English glosses are available on tap, off by default after Unit 1.
- **Speaking is checked, never required.** Answers are said out loud; speech recognition scores them when available. The learner can always continue.

## A lesson ("lesson set") has these tracks

| # | Track | What happens | Length |
|---|---|---|---|
| 1 | **Main text** | A short real-life dialogue. Listen at slow, then learner speed, then natural. Then the transcript appears with karaoke highlighting. Two or three gist questions. | 3 min |
| 2 | **Phrases** | The tutor (English) explains each phrase from the main text with examples, and you repeat after the Mandarin voice (shadowing). Pronunciation clinic lives here. | 4 min |
| 3 | **Mini-story** | Ask and answer. The storyteller tells a silly story in Chinese, with pictures; the questioner asks 30 to 60 fast questions; you answer out loud within a few seconds; the model answer follows. | 6 to 8 min |
| 4 | **Point of view** | The same story retold, shorter, from another angle, followed by a few questions. | 2 to 3 min |
| 5 | **Grammar spotlight** | One pattern the stories used, explained in English with story examples, then a short practice. | 3 min |
| 6 | **Practice** | Phrase cards and drills. Feeds the daily review. | 4 min |
| 7 | **Listen again** | Hands-free audio of tracks 1, 3 and 4 back to back, for daily listening (walking, commuting). | 10 min |

Every lesson also has a **Lesson notes** page: the detailed written reference (full transcripts, phrases in depth, grammar notes, pronunciation, culture, new words, a practice picker and a printable cheat sheet). Tracks are for learning by ear; the notes are for looking things up.

The lesson page shows the tracks like an album, the listening-days tracker (●●●○○○○), and a "Listen again today" button. Tracks unlock in order the first time; afterwards any track can be replayed.

## Voices

- Tutor (English): Kokoro `af_heart` today; energetic, warm, brief.
- Mandarin: MiniMax by default, Edge as the alternative; three speed tiers (slow, learner, natural). See `docs/agent-notes.md`.
- Recurring cast: 王明 (the neighbour, over-excited), 李月 (the calm colleague), the storyteller, and the questioner who asks the mini-story questions and gives model answers.

## Writing rules for stories

- Every sentence uses known words plus at most one new word, and new words are shown in the picture.
- Questions come in the Effortless English order after each new fact: a yes question (对), a no question (不, correction), an either-or question, a what/who question, and the fact again.
- Something absurd happens in every story. The absurd detail is what gets asked about most.
- Model answers are short and natural first (对！/ 不是！), then the full sentence.
