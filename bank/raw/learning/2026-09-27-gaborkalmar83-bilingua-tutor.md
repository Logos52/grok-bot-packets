---
id: 2026-09-27-gaborkalmar83-bilingua-tutor
kind: article
title: Bilingua Tutor
source: "https://github.com/gaborkalmar83/bilingua-tutor"
author: gaborkalmar83
published: 2026-09-27
captured: 2026-09-27
via: grok-bot/Field
lane: learning
status: raw
private: false
---

# Bilingua Tutor

An Android language tutor that explains *why*, not just *what* — the native, store-ready sibling
of the LinguaMap web app (github.com/gaborkalmar83/Lucy) and a companion to Bilingua Reader.

- **Grammar map** — 331 hand-written rules for Dutch, German, Finnish, Hungarian and English, each
  with the rule, *why it exists*, colour-coded examples you can hear, pitfalls, related rules.
  Works offline, no AI needed. Can be translated once into any explanation language by the AI.
- **Sentence Lab** — write or dictate a sentence; get a verdict, the corrected version, the word
  roles colour-coded (with a translation in your 1st or 2nd explanation language underneath), and
  every rule applied ✓ or broken ✕ — tap a rule for its details, the map entry, a Lucy explanation
  or a drill.
- **Lucy** — a conversational tutor that answers in the target language with translations,
  corrects one mistake per turn in a fixed format (what you said / right version / rule / why),
  16 one-tap actions (explain, conjugate, timelines, roleplay, cloze, recap…), tappable words.
- **Words everywhere** — tap or hold any word for its meaning in both explanation languages, each
  spoken in the voice you picked for that language, the context sentence and its translation;
  save the word, the word with its sentence, or the sentence. Double-tap saves straight away.
- **Voice mode** — a spoken conversation with Lucy over the phone's own speech recognition and
  TTS; works with every provider and fully offline with on-device Gemma.
- **Reader** — share or fetch an article (direct fetch, no proxy), read it sentence by sentence
  with idiomatic translations in one or two languages and word roles.
- **Review** — built-in SM-2 spaced repetition with a daily reminder (Settings → Practice & review);
  saved words, sentences and Lucy's corrections become cards on their own. Or switch to
  **AnkiDroid**: notes go to a deck of your choice with TTS audio for both sides, like Bilingua Reader.
- **Practice & Progress** — AI drills per rule or pitfall, streaks, XP, 12-week heat-map, mastery
  per rule, model usage per provider.
- **AI providers** — Gemma 4 E2B **on-device by default** (LiteRT-LM), plus OpenAI, Anthropic,
  Google Gemini, OpenRouter, Azure AI Foundry and local OpenAI-compatible servers (Ollama, LM
  Studio). Keys are AES-GCM encrypted with an Android-Keystore key.
- **Backups** in the web app's own format — move between browser and phone both ways.
- **14 interface languages**: en, nl, de, hu, fr, es, it, pt, pl, sv, fi, ru, mk, sr.
- **Monetisation**: 14-day free trial of everything, then a one-off Play purchase
  (`bilingua_tutor_full`) unlocks the AI features; the map and reviews stay free forever.

## The on-device model

Gemma 4 E2B (`litert-community/gemma-4-E2B-it-litert-lm`, Apache-2.0, 2,588,147,712 bytes) is the
default provider. It cannot be packed into the app: Play caps the base module at 200 MB and a
single AI pack at 1.5 GB. It is therefore fetched once, on first run, through the system
`DownloadManager` (Wi-Fi only by default, resumable, survives the app closing) into the app's
external files directory — see `ai/gemma/GemmaModel.kt`. Onboarding starts the download; every AI
screen shows progress and a one-tap start until it is ready. A complete copy in
`filesDir/models/` is also accepted (that is how tests put it there with `adb shell run-as`).

`ai/gemma/GemmaEngine.kt` runs it: one engine on one thread, GPU first with a crash-safe CPU
fallback (an unfinished GPU attempt is remembered across a native crash), an 8K-token context
by default (4K–32K in Settings → Advanced; the reply budget is a quarter of it),
streaming replies, and Lucy's conversation kept alive between turns so only the new message is
prefilled. A cancelled generation is drained before the next one starts, so a new request can
never read the tail of an old one. The engine is released 4 minutes after the app goes to the
background.

Measured on the x86_64 emulator (CPU only, 2.5 GB RAM — far slower than a phone GPU): engine
init 23 s cold / 3 s with the weight cache; Lucy reply ~45 s; Sentence Lab ~85 s; word gloss ~20-45 s.

Lessons baked into the prompts (`ai/Prompts.kt`, `compact` variants):
- LiteRT-LM 0.17.1's constrained JSON decoding made Gemma run to the output cap at 1.5 tok/s and
  still emit invalid JSON — it is **off by default** (Settings → AI provider → Strict answer format).
- The full rule catalogue is most of the Lab prompt, and prompt reading is the slow part, so on the
  phone the model names rules freely and `Tutor.matchRule` links them to the map afterwards.
- A per-language checklist of the most error-prone rules (`Prompts.checklist`) is what made the
  2B model catch e.g. Dutch verb-second errors.
- `extractJson` repairs the bracket mistakes small models make (`repairJson`, `salvagePairs`),
  and `Tutor.sanitize` drops contradictory Lab output. Every failure seen is a unit test.

## Build

Same toolchain as Bilingua Reader (not on PATH):

```bash
export JAVA_HOME="C:/Program Files/Microsoft/jdk-17.0.20.101-hotspot"
/c/dev/tools/gradle-9.6.0/bin/gradle :app:assembleDebug          # debug APKs (com.bilingua.tutor.debug)
/c/dev/tools/gradle-9.6.0/bin/gradle :app:testDebugUnitTest      # JVM tests (JSON repair, SM-2, licence, corrections)
/c/dev/tools/gradle-9.6.0/bin/gradle :app:bundleRelease :app:assembleRelease   # AAB + universal APK
```

AGP 9.4.1 with built-in Kotlin 2.4.20, Compose BOM 2026.06.01, Room 2.8.5 (KSP), LiteRT-LM 0.17.1,
Play Billing 8.3.0, OkHttp 4.12, jsoup 1.21.2. compileSdk/targetSdk 36, minSdk 26. LiteRT-LM ships
arm64-v8a and x86_64 only.

Machine-local files (gitignored, never commit): `local.properties` (sdk.dir, `play.license.key`),
`keystore.properties` + `tutor-upload.jks` (the upload key — **back it up**).

The grammar maps are generated from the web app's data:

```bash
node tools/export-grammar.mjs ../claude/code/lucy.nl/src/data   # → app/src/main/assets/grammar/*.json
```

## Test on the emulator

- Install `app/build/outputs/apk/debug/app-x86_64-debug.apk`, finish onboarding.
- Put the model in place without downloading (debug builds only):
  `adb shell run-as com.bilingua.tutor.debug sh -c 'mkdir -p files/models && cp /data/local/tmp/g.litertlm files/models/gemma-4-E2B-it.litertlm'`
- Engine timing is logged: `adb logcat | grep GemmaEngine`; unparseable model replies: `grep Llm`.
- Licence states in debug builds: `adb shell setprop debug.bilingua.tutor.license trial|expired|licensed`.
- **Always smoke-test the release APK** before shipping (R8 differs from debug).

## Before the first Play release

1. Create the app in Play Console (developer "Kalmarium"), package `com.bilingua.tutor`.
2. Monetise → Products → one-time product `bilingua_tutor_full`; copy this app's licensing public
   key into `local.properties` as `play.license.key=…` and rebuild (without it every purchase is
   refused on purpose — see `billing/PlaySignature.kt`).
3. Upload `app-release.aab` to internal testing; enrol Play App Signing with `tutor-upload.jks`.
4. Store listing, privacy policy and Data safety answers: see `store/`.
5. Support address: kalmariumservices@gmail.com (`SUPPORT_EMAIL`).

## Layout

```
ai/            Llm router, CloudClient (OpenAI-compatible + Anthropic SSE), Prompts, Tutor services
ai/gemma/      GemmaModel (download), GemmaEngine (LiteRT-LM)
data/          Settings (DataStore JSON), SecretStore (Keystore vault), Room DB, languages & roles
grammar/       grammar-map model and repository (+ cached translations)
learn/         SM-2, vocab, mistakes, streaks, rule mastery
backup/        web-compatible export/import
billing/       trial + one-off purchase, paywall
speech/        TTS and speech recognition
home map lucy lab reader review practice progress settings onboarding   — screens
ui/            theme, components, word sheet, Lucy markdown renderer, dictation
```
