My Chinese Tutor — local setup

Requirements:
- Node 18+ (to get fetch and modern JS)
- npm or yarn

1. Install
   npm install

2. Create .env
   cp .env.example .env
   Edit .env and set OPENAI_API_KEY to your key (or other provider). Do NOT commit .env.

3. Run (frontend dev server + server)
   npm run dev

   - Vite frontend runs on http://localhost:5173
   - Backend proxy runs on http://localhost:5178 (configurable via PORT)

Notes:
- The frontend calls endpoints under /api/ai/*; in dev the concurrently command starts both Vite and the Express server.
- The server proxies to OpenAI's chat/completions endpoint by default (see server/index.js). You can adapt it to any provider by changing callOpenAI.
- All local user data (preferences, vocabulary, sessions, stats) are stored in LocalStorage.

Extending:
- Add grammar pages under src/data/grammar.ts and src/pages/GrammarPage.tsx
- Improve TTS voices selection by enumerating speechSynthesis.getVoices()
- Replace server implementation with serverless function if you prefer
- Add authentication and cloud sync if desired (keep local-first)

Security:
- Never store API keys in the client.
- Use environment variables and server-side requests to call the provider.

Testing tips:
- Try the Practice tab, type "Hello" or a short Mandarin phrase and see the assistant reply.
- Toggle microphone (note: the Web Speech API is browser-dependent).
