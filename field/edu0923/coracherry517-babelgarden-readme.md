# Babelgarden 巴别园

**English** | [简体中文](README.zh-CN.md)

An open-source community for learning languages: listening, speaking, reading, writing, regional expressions, and public learning diaries that anyone can comment on and correct. There are no friends lists, follows or private messages by design.

## Features (roadmap)

- **Listening** – graded audio, adjustable speed, dictation
- **Speaking** – recording, shadowing, pronunciation feedback (Whisper)
- **Reading** – CEFR-graded texts, spaced repetition (FSRS)
- **Writing** – grammar checks (LanguageTool), exam-criteria feedback
- **Regional expressions** – idioms and slang tagged by region and register
- **Learning diaries** – public posts with comments and corrections
- **Exam goals** – IELTS, TOEFL, TOPIK, JLPT, DELF/DALF, DELE, HSK

UI languages: 简体中文, English, 日本語, 한국어, Français, Español.

## Quick start

Requirements: Node.js 20+ and pnpm.

```bash
pnpm install
cp .env.example .env.local   # fill in your Supabase values
pnpm dev
```

Open https://babelgarden.vercel.app.

## Database

Create a free project at [supabase.com](https://supabase.com), open **SQL Editor**, and run `supabase/migrations/0001_init.sql`.

## Tech stack

Next.js · TypeScript · Tailwind CSS · next-intl · Supabase (PostgreSQL)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Translations, learning content and regional expressions are all welcome.

## License

Code: [MIT](LICENSE). Learning content: [CC BY-SA 4.0](CONTENT_LICENSE.md).
