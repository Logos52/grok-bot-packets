# Japartner

Japartner is a local-first personal Japanese tutor built with Go, Wails, React, Ollama, whisper.cpp, VOICEVOX, and SQLite. It plans daily practice around a goal and deadline, tracks reusable expressions, turns real-world speaking gaps into study material, and runs targeted spoken conversations.

## Run

```sh
wails dev
```

Build a production app:

```sh
wails build
```

The built app is written to `build/bin/japartner.app`.

Run backend regressions with `go test ./...`, frontend transcript tests with `npm --prefix frontend test`, and the production frontend check with `npm --prefix frontend run build`.

## Releases

Push a version tag such as `v0.1.0` to build macOS, Windows, and Linux archives and publish a GitHub release. The macOS job signs, notarizes, and staples the app before publishing it.

Configure these GitHub Actions repository secrets for macOS releases:

- `MACOS_CERTIFICATE_BASE64`: exported Developer ID Application certificate (`.p12`) encoded as base64
- `MACOS_CERTIFICATE_PASSWORD`: password used when exporting the certificate
- `APPLE_ID`: Apple ID used for notarization
- `APPLE_TEAM_ID`: Apple developer team ID
- `APPLE_APP_SPECIFIC_PASSWORD`: app-specific password for notarization

The signing script can also be run locally with those notarization variables and an optional `MACOS_SIGNING_IDENTITY`.

## Using the App

- Set the active goal, exact deadline, focus areas, and practice frequency on **Today** (default: three days per week). Save to generate a short Ollama summary and weekly themes with scheduled lessons; a local roadmap is used if Ollama is unavailable or returns invalid content.
- Today assembles a bounded local lesson: up to 6 due reviews, 3 new expressions, 2 weak expressions, 3 conversation targets, and 2 captured gaps. A started roadmap lesson keeps its non-empty exercise list until completed, including across dates and restarts. Without a roadmap, a non-empty plan stays fixed for the local date.
- Only the current scheduled roadmap lesson can start. Start selects its local exercises and prepares a saved 5–10 minute activity brief: a concrete mission, partner role, warm-up, steps, 4–6 useful phrases, two examples to adapt, and success criteria. Ollama prepares the brief once on Start, with a local fallback; Today never needs an LLM request to open. Resume and Repeat preserve the brief across dates and restarts.
- Finish the reviews and conversation, then confirm whether you achieved the mission outcomes (with help if needed). Completing the lesson records pointers and activates the next scheduled lesson. Mission success is learner-confirmed, not an automated proficiency assessment. Completed lessons can be repeated without losing their original completion. Goal/cadence changes require finishing an in-progress lesson and preserve completed lessons.
- Review, new-learning, and weak-practice cards complete with Hard, Good, or Easy. Again means failed recall: the card remains unfinished and moves behind other cards for an in-lesson retry (its spaced-review retry is also scheduled in ten minutes). Use Reveal, the speaker button, Previous/Next, arrow keys, or touch swipes. Completed sections can be dismissed. Overall review, conversation, and vocabulary progress appears at the bottom of Today.
- Review due expressions by recalling the Japanese first, revealing the answer, then choosing Again, Hard, Good, or Easy.
- Use **Practice** for the guided activity. The tutor opens with an in-character question, follows the mission, and introduces a small complication. Try optional review expressions where they fit naturally; unrelated ones need not be used. The topic phrase kit is separate from review targets and does not silently add generated vocabulary to the library. Listen to phrases/examples using their audio buttons.
- Open **Mission & phrase kit** during Practice for support. **Help me** simplifies the task and offers an example; **Make it harder** introduces a small constraint or asks for a reason. Support actions stay in the same activity and are not recorded as learner replies. Local fallback activities rotate between opinion exchanges, role-plays, storytelling, and problem-solving. Existing started roadmaps receive a local brief safely when loaded.
- Choose **Need a hint?** only when you want to reveal a possible reply.
- End a conversation to record which target expressions you produced. Active conversation turns survive across app restarts.
- Use **Expressions** to add expressions manually, auto-fill their kana reading and meaning, and inspect their current learning status.
- Use **Capture** after a teacher lesson, meetup, or real-world conversation. Describe what you could not say, generate editable expression drafts, and approve only the useful ones.
- In **Capture**, choose a teacher PDF or vocabulary CSV. PDFs are read with built-in OCR when needed; CSV rows are imported directly. Review or remove every suggestion before adding it to the practice queue. Source files remain in their original location and are not copied into Japartner's data.
- Click `Explain` on an assistant reply to open a modal with a kana reading, translation, vocabulary, and grammar details. Useful words can be saved explicitly for later review.
- Use `How to say` mode when you want a natural Japanese phrase for an English idea.
- Use `Correction` mode when you want your Japanese sentence corrected.
- Press `Cmd+Enter` or `Ctrl+Enter` to send. Plain `Enter` stays available for Japanese IME selection and line breaks.
- Service readiness is shown as compact dots in the header. Click them for details and refresh controls.
- Model and speech configuration are kept in the collapsible **Settings** drawer.

Goals, expressions, gaps, sessions, attempts, and conversation turns are stored locally in `learning.sqlite` in the application's user configuration directory.

Daily plans store only selected IDs and completion alongside that existing learning state. Selection does not contact Ollama. New learning prioritizes captured/imported material, weakness uses the last three review ratings and latest evaluation among the last 20 completed conversations, and conversation/gap relevance uses simple matching against the active goal and focus areas. Missing lexical matches fall back to useful study items; this is not semantic topic classification. Without an active goal, review and learning still work, but targeted conversations are not planned.

Roadmaps add one metadata table referencing the existing goal and daily-plan snapshots. Practice dates are evenly spaced in seven-day blocks from the save date, not specific weekdays. Target dates are bounded to the next year. Weekly themes cycle for longer goals; the full curriculum is not generated upfront. Lesson pointers reuse local completion and the existing conversation evaluation, rather than requiring another model request. Skipped dates leave the current lesson available; subsequent lessons still follow their scheduled dates. New expressions saved after a lesson starts enter a later lesson, except that an empty lesson may populate when its first expressions are added.

PDF import reads selectable text first and uses built-in macOS OCR for scanned or image-only pages. Very long PDFs are capped for the first import pass, and the review dialog tells you when only the beginning was analyzed. CSV import recognizes common Japanese word, definition, reading, and example columns (with or without a header), and presents up to 100 unique entries for approval.

## Local Requirements

- Ollama running at `http://127.0.0.1:11434`
- A chat model installed in Ollama
- `ffmpeg` for microphone transcription
- `whisper.cpp` with a Japanese-capable model file
- VOICEVOX Engine for Japanese text-to-speech
- `kakasi` for deterministic kana readings that preserve katakana in sentence explanations
- macOS `say` as a fallback text-to-speech option

The app is configurable from the settings panel. Defaults are:

- Model: `hf.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf:Q4_K_M`
- TTS provider: `VOICEVOX`
- VOICEVOX URL: `http://127.0.0.1:50021`
- VOICEVOX speaker: `1`
- Ollama URL: `http://127.0.0.1:11434`

macOS may list several Japanese voices with:

```sh
say -v '?'
```

On this machine, the newer Japanese names such as `Flo (Japanese (Japan))` currently synthesize the same audio as `Kyoko` through the `say` command, so Japartner only offers `Kyoko` plus a custom voice field. Better Japanese speech will require a dedicated local TTS engine rather than macOS `say`.

## VOICEVOX Setup

Docker is the recommended first setup for VOICEVOX. It keeps the engine separate from the app and exposes the local API Japartner expects.

Start the CPU engine:

```sh
docker run --rm --name voicevox \
  -p 127.0.0.1:50021:50021 \
  voicevox/voicevox_engine:cpu-latest
```

Leave that terminal running while using Japartner. Then open the app, click `Refresh Status`, and check that TTS says VOICEVOX is reachable.

Open the local VOICEVOX docs:

```text
http://127.0.0.1:50021/docs
```

Test synthesis manually:

```sh
echo -n 'こんにちは。日本語の練習をしましょう。' > /tmp/voicevox-text.txt
curl -s -X POST '127.0.0.1:50021/audio_query?speaker=1' \
  --get --data-urlencode text@/tmp/voicevox-text.txt \
  > /tmp/voicevox-query.json
curl -s -H 'Content-Type: application/json' \
  -X POST \
  -d @/tmp/voicevox-query.json \
  '127.0.0.1:50021/synthesis?speaker=1' \
  > /tmp/voicevox.wav
afplay /tmp/voicevox.wav
```

In Japartner settings:

- TTS provider: `VOICEVOX`
- VOICEVOX URL: `http://127.0.0.1:50021`
- Click `Load VOICEVOX Voices`
- Pick a speaker/style
- Click `Save Settings`

Preview voices quickly from the terminal:

```sh
./scripts/voicevox-preview.py --text 'こんにちは。'
```

The script prints each speaker/style ID, plays the sample, then waits for a key:

- `Enter`: next voice
- `r`: replay current voice
- `b`: go back
- `q`: quit

Use the printed numeric ID for Japartner's `VOICEVOX speaker` setting. To test only a few IDs:

```sh
./scripts/voicevox-preview.py --ids 1,3,8,10 --text 'こんにちは。'
```

Apple Silicon note: use the CPU image first. The official GPU Docker image is for NVIDIA GPUs, not Apple Silicon Metal. CPU inference is usually acceptable for short study phrases.

Other local TTS candidates:

- Style-Bert-VITS2: higher ceiling for expressive Japanese voices, but heavier to install and operate.
- Piper: fast local TTS, but Japanese voice availability and quality are less compelling for this use case.

Sources:

- VOICEVOX Engine: https://github.com/VOICEVOX/voicevox_engine
- Style-Bert-VITS2: https://github.com/litagin02/Style-Bert-VITS2
- Piper: https://github.com/rhasspy/piper

## Model Selection

Use the built-in "Benchmark Installed Models" button before choosing the default model. It checks only models already installed in Ollama and compares fixed Japanese tutor prompts for latency and structured JSON compliance.

Recommended candidates to test:

- `hf.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf:Q4_K_M`
- `swallow-jp:8b`
- `Gemma-2-Llama-Swallow-9b-it-v0.1`
- `Qwen3-Swallow-8B-RL-v0.2`
- `qwen3.5:9b`
- `llama3.1:latest`

Model names must match the names registered in your local Ollama instance.

To create a shorter local alias for the downloaded Swallow model:

```sh
ollama cp hf.co/mmnga/Llama-3.1-Swallow-8B-Instruct-v0.5-gguf:Q4_K_M swallow-jp:8b
```

Then set the app model to `swallow-jp:8b`.

## Speech Setup

Japartner uses `kakasi` to clean up kana readings in the Explain modal while preserving katakana. This avoids showing model-generated romaji as if it were furigana.

Japartner records audio in the UI, converts it to 16 kHz mono WAV with `ffmpeg`, then sends it to `whisper.cpp` through the configured `whisper-cli` executable.

Install build tools, `ffmpeg`, and `kakasi`:

```sh
brew install cmake ffmpeg git kakasi
```

Clone and build `whisper.cpp`:

```sh
mkdir -p ~/Dev/vendor
cd ~/Dev/vendor
git clone https://github.com/ggml-org/whisper.cpp.git
cd whisper.cpp
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j --config Release
```

Download a multilingual Whisper model. Do not use `.en` models for Japanese:

```sh
sh ./models/download-ggml-model.sh small
```

`small` is the recommended first choice for Japanese: better than `base`, still fast on Apple Silicon. Use `medium` if transcription quality matters more than latency:

```sh
sh ./models/download-ggml-model.sh medium
```

Test the CLI:

```sh
./build/bin/whisper-cli -m models/ggml-small.bin -f samples/jfk.wav
```

For a Japanese audio file:

```sh
ffmpeg -i input.m4a -ar 16000 -ac 1 -c:a pcm_s16le japanese.wav
./build/bin/whisper-cli -m models/ggml-small.bin -f japanese.wav -l ja -nt
```

Configure Japartner settings:

- Whisper executable: `/Users/<you>/Dev/vendor/whisper.cpp/build/bin/whisper-cli`
- Whisper model: `/Users/<you>/Dev/vendor/whisper.cpp/models/ggml-small.bin`

Replace `<you>` with your macOS username, or use the exact path from:

```sh
pwd
```

### Apple Silicon Notes

`whisper.cpp` is a good fit for Apple Silicon. The project supports ARM NEON, Accelerate, Metal, and optional Core ML acceleration. The normal CMake build above should use the available Apple acceleration paths on macOS.

If CMake cannot find Apple developer tools, install them:

```sh
xcode-select --install
```

Optional Core ML acceleration can speed up the encoder on Apple Neural Engine, but it adds Python/Core ML setup and model generation. Skip it for the first version unless transcription is too slow. The default Metal/CPU path is simpler and usually good enough for short practice sentences.

Useful paths after the recommended install:

```text
Whisper executable:
~/Dev/vendor/whisper.cpp/build/bin/whisper-cli

Small model:
~/Dev/vendor/whisper.cpp/models/ggml-small.bin

Medium model:
~/Dev/vendor/whisper.cpp/models/ggml-medium.bin
```

Source: `whisper.cpp` upstream README: https://github.com/ggml-org/whisper.cpp

### Speech Troubleshooting

If the app shows `ggml_metal_*`, `system_info`, or `read_audio_data` lines, those are `whisper.cpp` diagnostic logs, not the transcript. Current Japartner builds ask `whisper-cli` to write a `.txt` transcript and ignore those logs.

If transcription returns `no speech detected`:

- Record a clear spoken sentence, not silence or background audio.
- Hold the microphone close enough for the Mac input level to move.
- Try `ggml-medium.bin` if `small` misses short or quiet Japanese phrases.
- Test outside the app with:

```sh
ffmpeg -i input.m4a -ar 16000 -ac 1 -c:a pcm_s16le japanese.wav
~/Dev/vendor/whisper.cpp/build/bin/whisper-cli \
  -m ~/Dev/vendor/whisper.cpp/models/ggml-small.bin \
  -f japanese.wav \
  -l ja \
  -nt \
  -otxt \
  -of transcript
cat transcript.txt
```
