# Deutsch Karten — Android app

A solo German vocabulary trainer built on the compiled `words.csv` (5,684 words, A1–C2).
Swipe to grade, progress is stored on the device, and each CEFR level has its own card colour.

## Screens

| Screen | What it does |
| --- | --- |
| **Home** | Progress ring for the current level (mastered / total), streak, per-level bars for all six levels, `Start session`, `Drill trouble`, `Browse words` |
| **Session** | The swipe deck — tap to flip, swipe to grade, undo in the top bar |
| **Summary** | Accuracy ring, cards/correct/missed/mastered, the words you missed, and a one-tap "Drill these now" |
| **Level up** | Fires when every word in a level is mastered: animated badge, stats, "up next" preview |
| **Browse** | Search all 2,000 words, filter by level / starred / trouble / mastered / due, tap for the full record |
| **Word detail** | Article, plural, IPA, conjugation, example DE+EN, your progress, Wiktionary link, audio |
| **Settings** | New cards per day, auto-play, daily reminder, export/restore backup, reset |

## Gestures

| Gesture | Action |
| --- | --- |
| Tap | Flip the card (front → back) |
| Swipe right | Got it |
| Swipe left | Missed — re-queued later in the same session |
| Swipe up | Easy — jump two Leitner boxes |
| Swipe down | Undo the previous answer |
| Long-press-free alternative | Undo icon button in the session bar |

**Swipe distance is a confidence signal:** a long, fast right swipe promotes the card a full
box, a short flick only keeps it at its current box. You get graded on how sure you looked.

## How progress works

* **Leitner boxes** 1–6 with intervals of 1, 2, 4, 8, 16, 32 days. A miss drops the card to box 1.
* **Mastered** = 3 correct answers on 3 *different* days. Mastery never regresses, which is what
  makes level completion reachable.
* **Level progression:** A1 → A2 → B1 → B2 → C1 → C2. At 80% of a level the next level starts
  mixing into the new-card queue (30% of each batch) — a soft unlock, so you feel the transition
  without hitting a wall. At 100% the level-up screen fires once per level.
* **Trouble (leech):** 4 lapses pulls a card out of rotation into `Drill trouble`; 3 correct in a
  row puts it back. You can also clear it manually from the word detail screen.
* **Streak:** consecutive days with at least one review.

## Persistence

Everything is on-device; there is no server and no account.

```
filesDir/progress.json    per-card state (box, due, counters, stars, mastery days) + review days
filesDir/reviews.jsonl    append-only review log: id, grade, timestamp, ms-to-answer
filesDir/audio/*.ogg      cached pronunciations from Wikimedia Commons
```

A JSON document plus an append-only log was chosen over Room deliberately: 2,000 cards fit in
memory, the file *is* the backup, and there is no annotation processor to keep in sync. Because
the log is append-only, the scheduler can be upgraded (Leitner → SM-2 → FSRS) later without
losing history. `peek()` never creates records, so browsing the list cannot bloat the file.

**Stable identity:** every row carries an `id` (`a1-haus`, `a1-sein-2`, …) plus a
`content_version`. Re-importing a fixed word list keeps the progress of unchanged ids and only
adds/retires the rest — that is why the id column was added to the CSV before any of this was built.

## Build

Needs JDK 17+ and an Android SDK with platform 37.2 (or edit `compileSdk`/`compileSdkMinor`).

```bash
cd app-android
export ANDROID_HOME=/path/to/Android/Sdk
./gradlew assembleDebug          # -> app/build/outputs/apk/debug/app-debug.apk
./gradlew testDebugUnitTest      # 9 logic tests (CSV, word list, conjugation, intervals)
```

Toolchain: Gradle 9.6.0, AGP 9.4.0 (built-in Kotlin — there is deliberately **no**
`org.jetbrains.kotlin.android` plugin), Kotlin Compose compiler 2.4.20, Compose BOM 2026.09.00,
`minSdk 26`, `targetSdk 36`.

Installed APK: 13.8 MB, with `assets/words.csv` (5,685 lines) embedded.

### Building in a restricted environment

If your machine has a read-only filesystem (a sandbox, a CI container), Gradle and the
Android SDK need somewhere writable to live. Point them at a directory you can write to:

```bash
export GRADLE_USER_HOME=$WORK/.gradle-home      # instead of ~/.gradle
export ANDROID_HOME=$WORK/android-sdk           # a writable SDK overlay
export ANDROID_USER_HOME=$WORK/.android-home    # avd + analytics
export XDG_RUNTIME_DIR=$WORK/.runtime           # used by the emulator
```

The SDK overlay is just a directory of symlinks to your real `build-tools`, plus a writable
`platforms/` so AGP can install the platform it needs (`platforms;android-37.2` for the
`compileSdk`/`compileSdkMinor` pair used here).

There is no `/dev/kvm` in such environments, so an AVD only runs under QEMU's software
emulation — workable, but slow. If you see `Failed to load native library`, or the emulator
refusing to start with a stale lock, clear `*.lock` from the AVD directory and set the four
variables above.

## Source layout

```
app/src/main/java/com/solo/deutschkarten/
  Model.kt          Word, CardState (+ JSON), Settings, CSV parser, asset loader
  Store.kt          ProgressStore (persistence), Scheduler (Leitner + mastery), Deck (queries)
  AppViewModel.kt   UI state, session queue building, grading/undo, settings, backup
  Theme.kt          Material 3 theme, per-level palettes, ProgressRing, LevelChip
  Screens.kt        Home, Session + swipe deck, Summary, Level up
  BrowseSettings.kt Browse, word detail, settings
  AudioPlayer.kt    stream-and-cache pronunciation playback (Wikimedia recordings)
  Speech.kt         on-device text-to-speech: sentences, verb forms, missing-recording fallback
  Reminder.kt       WorkManager daily notification
  MainActivity.kt   edge-to-edge entry point + navigation
app/src/test/…      CoreLogicTest
```

## Verb conjugation

Verb forms used to be unusable. The upstream export stores the whole present tense **glued
together with no separators**:

```
ichkanndukannster/sie/eskannwirkönnenihrkönntsie/SiekönnenPrät. ich konnte | Perf. ich habe gekonnt
```

That went straight onto the card back as one wrapped paragraph. **381 of the 480** conjugations in
the list were affected. It is now repaired in two places:

* **Data (`build.py`)** — `format_conjugation()` splits the glued block back into pronoun/form
  pairs, repairing the two artefacts the export also produces: reflexive verbs
  (`ichkümmern (sich)e` → `ich kümmere`) and separable verbs keep their prefix
  (`ichsehe aus` → `ich sehe aus`). The CSV field is now:
  `ich kann | du kannst | er/sie/es kann | wir können | ihr könnt | sie/Sie können | Prät. … | Perf. …`
  All 1,246 source verbs parse; `CONTENT_VERSION` is now 2.
* **UI (`Conjugation.kt`)** — `Conjugation.parse()` turns that field into person/form pairs.
  Cards show a compact **2-column × 3-row** table (plus one past-tense line); the word detail
  screen shows a full 6-row table with `Präteritum` / `Perfekt` spelled out. The grid lives in
  `ConjugationGrid()` in `Theme.kt`.

A unit test asserts that **every** conjugation in the shipped asset parses into six non-empty
person/form pairs, so a regression fails the build rather than reaching the card.

## Pronunciation — words, sentences and verb forms

Words use the **human recordings from Wikimedia Commons** (5,404 of 5,684 have one). Anything we
have no recording for — example sentences and verb forms — is spoken by the **phone's own
text-to-speech engine** (`android.speech.tts.TextToSpeech`, German `de-DE`). That choice is
deliberate: it is free, needs no API keys, no hosting and no audio files, works offline once the
voice is installed, and it covers all 5,684 sentences including C1/C2 idioms that nobody has
recorded. The source site (`wordfeather`) does the same thing in the browser with the Web Speech API.

| Where | What you can play |
| --- | --- |
| Card back | the German example sentence, and the English translation |
| Card back, verb table | tap any row to hear that form, e.g. `ich gehe` |
| Word detail | `Play word` (recording), `Slow`, ▶ next to *Present tense* speaks all six forms |
| Word detail | both sentences, and every verb row |
| Card front | if a word has **no** recording, the ▶ button falls back to TTS |

Settings → **Pronunciation**: `Slow speech (0.7×)` and `Speak the sentence on reveal` (off by
default, so a reveal never ambushes you with sound). Speech always interrupts the recording player
and vice versa, so the two never overlap.

### When speech isn't available

`isLanguageAvailable(de-DE)` is **not** a reliable signal — it can report a language as present while
the voice *data* is still missing (it downloads separately, ~30 MB). On this emulator it reported
German as available and then every utterance failed with `GoogleTTSServiceImpl: Synthesis failure
with error status code: -4` / `ECONNREFUSED` against the voice-download server.

So the app trusts an `UtteranceProgressListener` instead: the first real synthesis error flips a flag
that raises a toast ("German voice unavailable — see Settings") and turns on a warning card in
Settings with an **Open speech settings** button. Verified on the emulator — screenshots
`24-tts-error-toast-dark` and `25-tts-settings-warning-dark`.

**Verified on a real device** (Pixel 7, Android 17): the engine synthesises successfully —

```
currentLocale = de-DE
Synthesis request for locale deu-DEU and name de-DE-language
TTS dispatch: de-de-x-dea-seanet-embedded
```

The `-embedded` suffix matters: that phone ships the German neural voice in the firmware, so German
sentence playback needs **no download and no network**. On the emulator (no voice data, no route to
the voice server) the same tap fails with `Synthesis failure … -4` / `ECONNREFUSED`, which is exactly
the case the toast and Settings warning cover. Screenshots: `30-phone-home`, `31-phone-tts-controls`.

## Placement — where do you start?

On first launch the app asks for your current knowledge instead of assuming A1. The picker shows
**real sample words from each level** (three each), because self-rating against `A1/A2/B1` labels
alone is guesswork — seeing `der Hund, gehen, gut` next to `die Abhandlung, die Souveränität` is what
makes the choice meaningful.

Not sure? **Take a 12-card check**: two words per level, you say *I know it* / *Not yet*, and it
suggests the highest level where you recognised at least half. The check is deliberately **not**
recorded as reviews — it must not touch your schedule. The result screen shows the per-level
breakdown (`2 of 2 recognised`) so the suggestion is explainable, not magic.

### What placement does

* Levels **below** your placement are marked **"known"** on the home screen and stay open, so you can
  still browse or drill them — but you are not forced through them. Placing at B1 no longer means
  first mastering 1,245 A1/A2 words.
* Your **study level** becomes the first unfinished level at or above your placement, and the new-card
  queue draws from it. Levels above stay gated by progression (80% soft unlock), as before.
* **Home level rows are tappable** — "tap to study that level" — but only for unlocked levels. A lock
  glyph marks the rest.

### Settings → Your level

| Control | Effect |
| --- | --- |
| `Placed at A1` + **Change** | re-runs the placement picker (or the quick check) at any time |
| **Unlock all levels** | opens every level immediately, ignoring progression gating |

Both are persisted (`placementLevel`, `unlockAll`, `focusLevel`, `onboarded`) and applied to the deck
on launch, so the choice survives restarts. Verified on the phone: toggling *Unlock all levels*
persists `unlockAll=true`, and with placement set to B1 the home screen showed A1/A2 as **known**,
B1 active, and B2/C1/C2 still locked.

## Card design

The back of the card used to be a wall of centred text with the verb table dominating it. It is now
laid out as a page with a deliberate hierarchy:

1. **the meaning** — large, semibold, left-aligned (the answer should be the first thing you read)
2. **one grammar line** — article and plural for nouns, part of speech otherwise
3. **the example**, grouped in its own tinted container with a speaker on the German *and* the
   English line
4. **verb forms** under a `VERB FORMS ▶ / tap a form to hear it` header, with a play-all button

Left alignment replaced centred text because a centred block has no edge for the eye to follow once
it wraps past one line; only the *front* of the card stays centred, since a single large word is a
flash, not a paragraph.

**Touch targets.** The verb rows were the reported problem: they were ~20 dp tall, gave no feedback,
and looked like plain text. They are now full-width, **44 dp** rows (measured at 116 px on a Pixel 7,
density 2.625) with a bounded ripple; the speaker buttons went from 30 dp to **44 dp**, and icon
buttons remain 48 dp. The accessibility tree confirms the sizes.

**Tapping a control no longer flips the card.** This was a genuine bug: the card treats a tap as
"reveal/hide", and buttons *inside* the card (sentence speakers, verb rows, star, word audio) were
running their action **and** flipping the card back over the audio. The gesture loop now records
whether the child consumed the down event (`startedOnChild`) and, if a button handled the tap, leaves
the card revealed. A real drag still grades, wherever it started. Verified on device by hash: the
screenshot after tapping a sentence speaker and after tapping a verb row is byte-identical to the
revealed card, while tapping empty card space still flips it back.

## Dark mode

The app follows the system theme (`isSystemInDarkTheme()`), and the same level palettes are used in
both — one accent hue per level, with a dark variant of the card tint and accent:

| Level | Light accent | Dark accent | Card tint (dark) |
| --- | --- | --- | --- |
| A1 | emerald `#0F766E` | `#5EEAD4` | `#0F2B29` |
| A2 | indigo `#4338CA` | `#A5B4FC` | `#1A1B3A` |
| B1 | amber `#B45309` | `#FCD34D` | `#321F0C` |
| B2 | violet `#6D28D9` | `#C4B5FD` | `#241640` |
| C1 | rose `#BE123C` | `#FDA4AF` | `#3A101C` |
| C2 | sky `#0369A1` | `#7DD3FC` | `#0B2A3C` |

The first version was **not** dark-mode compatible, and the bug is worth naming because it is easy
to reproduce: screens were plain `Column`s with `.background(...)` and no `Surface` anywhere above
them. `MaterialTheme` does not provide `LocalContentColor`, so every `Text`/`Icon` without an
explicit colour fell back to the default **black**. That is invisible only by accident in light
mode — in dark mode the title, the level names and the "Words" heading rendered black on near-black.

Fixes:

* The whole app is wrapped in a root `Surface(color = background, contentColor = onBackground)`,
  so unstyled text and icons inherit a themed colour everywhere.
* Hardcoded colours became theme-aware helpers: `starTint()`, `easyTint()`, `onEasyTint()`.
* The swipe-overlay badges now use `onPrimary` / `onError` / `onEasyTint()` instead of
  `Color.White`, which was unreadable on the light accents used in dark mode.
* Cards use a hairline border in dark mode (`cardOutline()`) instead of a shadow, which is
  invisible on a dark background; the progress-ring track is `onSurface` at 12% alpha so it reads
  on both the light and dark card tints.
* `values-night/themes.xml` sets the dark window background so launch does not flash white.

## Verified on an emulator

The debug APK was installed and driven on a Pixel 7 AVD (API 34, 1080×2400) **in both light and
dark mode** (`cmd uimode night yes|no`). Screenshots in `screenshots/`, suffixed `-light` / `-dark`:

| Shot | Confirms |
| --- | --- |
| `01-home-*` | Home: progress ring, streak, per-level bars, lock state |
| `02-card-front-*` | Session deck — German headword + IPA, `1 / 10`, level chip |
| `03-card-back-*` | Tap-to-flip — English gloss, POS, example DE + EN |
| `04-after-right-swipe-*` | Right swipe grades and advances the deck |
| `05-after-left-swipe-*` | Left swipe grades and advances the deck |
| `06-summary-*` | Summary: accuracy ring, cards/correct/missed, "Drill these 1 now" |
| `07-browse-*`, `07b-browse-search-*` | Browse with filters, and search ("haus" → 5 matches) |
| `08-settings-*` | Settings: new cards/day, auto-play, reminder, backup, about |
| `09-levelup-dark` | Level-up after the 655th A1 word; "Up next A2 · Elementary" (indigo) |
| `12-verb-card-back-dark` | Verb card back: `sein` as a 2-column table + `Präteritum` / `Perfekt` |
| `13-verb-detail-dark` | Word detail: `gehen` as a full 6-row present-tense table |
| `14-home-c1-dark` | All six levels with their own colours; A1–B2 complete, C1 active, C2 locked |
| `15/16-c1-card-*-dark` | A C1 card (`Tugend`) in the rose palette, with plural + translated example |
| `17-browse-levels-dark` | Browse filters for A1–C2; "5684 of 5684" |
| `19-c1-detail-dark` | C1 word detail: IPA, plural, audio, example, progress |
| `20-tts-controls-dark` | Speech controls: ▶ on *Present tense*, tappable verb rows, `Play word` / `Slow`, speaker on both sentences |
| `23-tts-card-back-dark` | Card back with speakers on the German and English sentences |
| `24-tts-error-toast-dark` | Missing-voice failure surfaced as a toast instead of silence |
| `25-tts-settings-warning-dark` | Settings warning + *Open speech settings*, and the corrected about text |
| `45-phone-card-back-redesign` | Redesigned card back on the phone: hierarchy, grouped example, 44 dp verb rows |
| `70-onboarding-placement`, `71-onboarding-first-launch` | First-run placement picker with real sample words per level |
| `73-settings-your-level` | Settings → *Your level*: "Placed at" + Change, and Unlock all levels |
| `74-settings-unlock-all-on` | Unlock-all switched on |
| `10-home-level-complete-dark`, `11-after-levelup-dark` | 654→655/655, soft-unlock note, level-up dismissed |

Behaviour confirmed on device: install + launch with no `AndroidRuntime` crashes in either theme;
grading writes `files/progress.json` (`box: 1`, `due: today+1`, `correctDays: [today]`) and appends
to `reviews.jsonl`; a card correct on three distinct days is marked `masteredDay` and the level-up
screen fires once (`celebrated: ["A1"]`); the mistake drill re-queues the missed word as a 1-card
session; `peek()` keeps `progress.json` free of records for words that were only browsed.

Re-run it yourself:

```bash
./verify-on-emulator.sh          # needs a booted device and a built debug APK; captures both themes
```

### A bug this caught

The first version put `Modifier.clickable` next to `detectDragGestures` on the card. On device the
tap detector swallowed the gesture, so **no swipe ever graded** — the deck looked frozen. It is now
a single `awaitEachGesture` loop that decides tap-vs-drag itself. It also no longer captures the
composition-time `x`/`y`, which were frozen at 0 inside the never-restarting `pointerInput` block.

### Emulator notes for this sandbox

There is no `/dev/kvm` here, so the AVD runs under QEMU TCG (software emulation) — functional but
slow, and it needs a few things redirected onto a writable filesystem (`/` is read-only):
`HOME`, `ANDROID_USER_HOME`, `ANDROID_AVD_HOME` and `XDG_RUNTIME_DIR` all point inside the
workspace, and stale `*.lock` files in the AVD directory must be cleared before a restart.

## Not built yet

* FSRS scheduling (the review log already stores everything it needs).
* Card-type variants: article drill (der/die/das), plural drill, EN→DE production, cloze.
* Listening-comprehension cards — now nearly free, since sentences are speakable.
* Word-by-word glosses for example sentences — feasibility measured, see below.

## Word-by-word glosses (next, feasibility done)

`gloss_coverage.py` answers the question every-word glosses depend on: how many sentence tokens can we
define from data we already hold? Measured over all 5,684 example sentences (48,271 tokens):

| | before | after adding a closed-class table |
| --- | --- | --- |
| tokens resolvable | 87.1% | **96.6%** |
| sentences with **every** word covered | 31.8% | **77.4%** |
| proper nouns (no gloss needed) | — | 2.9% |
| genuinely unknown words | — | **0.5%** |

The first pass failed mostly on grammar, not vocabulary: `die`, `das`, `den`, `im`, `zum` are not in
the 5,684-word list at all (`der` is — the source treats the articles as one entry). A ~200-entry
function-word table plus morphology for zu-infinitives (`vorzubereiten`), comparatives (`größere`),
imperatives (`komm`) and feminine forms (`Lehrerin`) took token coverage to 96.6%. What remains is
0.5% unknown vocabulary, concentrated in C1/C2, which a Wiktionary fallback can cover.
* Stats history screen (currently just the streak and per-level bars).
* Widget / Wear tile.
