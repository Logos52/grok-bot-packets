# Voca AI

A Kotlin/Jetpack Compose Android vocabulary-learning voice-agent prototype. It includes phone/OTP onboarding, region, language and level selection, a gamified home screen, and a spoken lesson loop.

## Run

Open `android/` in Android Studio (JDK 17, Android SDK 35) and run on a device/emulator. Use any phone number and OTP `123456` in demo mode. Microphone permission is requested during lessons.

Start the API with `cd backend; gradle run`. It serves `http://localhost:8080`.

## Integrations

- Android TextToSpeech and SpeechRecognizer power the local voice experience.
- Replace demo OTP with Supabase Phone Auth; keep `SUPABASE_URL` and `SUPABASE_ANON_KEY` as secrets.
- The API evaluates a transcript locally and is ready for Groq feedback via `GROQ_API_KEY`. The selected Hugging Face ASR model is `openai/whisper-small`, whose multilingual checkpoint supports the eight-language onboarding path; configure access with `HF_TOKEN`.
- Deploy the backend to Vercel (the requested “Versal” host); Android is shipped separately as an APK/Play Store app.
