# 📚 Study Flashcard Generator

An AI-powered web app that turns pasted study notes into interactive,
flippable flashcards — built for the AI-Powered Application Development
and Deployment Project.

## Problem Statement

Students spend a lot of time manually converting lecture notes and
textbook material into study flashcards, which is tedious and often
gets skipped entirely — leaving them to re-read dense notes instead of
actively testing themselves. This app removes that friction: paste
your notes, and AI instantly generates a set of question/answer
flashcards you can click through to review.

**Target users:** students studying for exams who want a fast way to
convert raw notes into an active-recall study tool, without manually
writing each card by hand.

**Why AI is needed:** identifying the key facts, definitions, and
concepts worth testing — and phrasing them as clear questions — is a
language-understanding task. A simple script can't tell what's
"important" in a block of notes; a large language model can read the
notes for meaning and generate pedagogically useful Q&A pairs.

## AI Tool(s) Used

- **Google Gemini API (gemini-3.8-flash)** — powers the core feature:
  reading the user's notes and generating flashcard question/answer
  pairs. The backend sends the notes to the Gemini API with a system
  instruction that tells it to return structured JSON flashcards.
- - **Claude (Anthropic)** — used throughout development to scaffold the
  Flask backend and front-end code, debug errors (including a model
  deprecation error and API authentication issues), and write the
  project documentation.

## Tech Stack

| Layer      | Technology |
|------------|------------|
| Front end  | HTML, CSS, vanilla JavaScript (served by Flask) |
| Back end   | Python, Flask |
| AI         | Google Gemini API (free tier) |
| Deployment | Render (or Railway / Vercel — see below) |

This project intentionally uses **one Flask app** that serves both the
front-end page and the `/api/generate` API route, so there is only one
service to deploy — no separate front-end/back-end hosting needed, and
no database, since nothing needs to be stored between sessions.

## How It Works (Architecture)

1. The user pastes notes into a textarea on the front end and clicks
   **Generate Flashcards**.
2. JavaScript sends the notes as JSON to the Flask backend at
   `POST /api/generate`.
3. Flask validates the input (rejects empty or overly long notes) and
   sends the notes to the Gemini API with a system instruction asking
   for structured flashcard JSON.
4. Gemini returns question/answer pairs; Flask parses and returns them
5. The front end renders each pair as a flip card — click a card to
   flip between the question and the answer.

## Project Structure

```
flashcard-app/
├── app.py                 # Flask app + /api/generate route (Claude API call)
├── templates/
│   └── index.html         # Main page
├── static/
│   ├── style.css          # Flip-card styling
│   └── script.js          # Front-end logic (fetch, render, flip)
├── requirements.txt        # Python dependencies
├── Procfile                # Start command for Render/Railway
├── .env.example             # Shows required env var (no real key)
└── .gitignore
```

## Setup & Installation (local)

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd flashcard-app
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set your Gemini API key as an environment variable (get a free one
   at [aistudio.google.com/apikey](https://aistudio.google.com/apikey) —
   no credit card required):
   ```bash
   export GEMINI_API_KEY=your_key_here     # Windows: set GEMINI_API_KEY=your_key_here
   ```
4. Run the app:
   ```bash
   python app.py
   ```
5. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

## Deployment (Render — free tier)

1. Push this project to a GitHub repository (see below).
2. Go to [render.com](https://render.com) → **New +** → **Web Service**
   → connect your GitHub repo.
3. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Add an environment variable in the Render dashboard:
   - `GEMINI_API_KEY` = your Gemini API key
5. Deploy. Render will give you a public URL like
   `https://your-app-name.onrender.com`.

> Railway and other platforms follow essentially the same steps: point
> them at this repo, set the `GEMINI_API_KEY` environment variable,
> and let them run `gunicorn app:app`.


## Deployed Application

- **Live URL:** https://flashcard-generator.onrender.com
- **GitHub Repository:** https://github.com/officialcam45-jpg/Flashcardapp

## Security Note

No API keys or secrets are committed to this repository. The
`GEMINI_API_KEY` is read from an environment variable at runtime
(see `.env.example` for the variable name) and must be set separately
in your local environment and in your hosting platform's dashboard.

## Lessons Learned / Challenges

## Lessons Learned / Challenges

- **AI model versioning:** the Gemini model originally used
  (`gemini-2.0-flash`) was deprecated mid-project, causing a 404 error.
  Had to read the API's error message carefully to identify the
  replacement model name (`gemini-3.8-flash`) and update the code.
- **API authentication:** GitHub no longer accepts account passwords
  for command-line pushes — had to generate a Personal Access Token
  instead and use it as the password when pushing code.
- **Free-tier rate limits:** the Gemini free tier caps requests per
  minute, which surfaced as a 429 error during testing. Solved by
  waiting for the cooldown period between requests.
- **Environment variables:** learned to keep API keys out of source
  code entirely by reading them from environment variables at runtime,
  set differently for local development (`export` in Terminal) versus
  production (Render's dashboard).