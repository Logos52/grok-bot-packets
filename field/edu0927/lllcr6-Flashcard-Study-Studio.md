# Flashcard Study Studio

Flashcard Study Studio turns a photo, scan, or PDF of class notes into a study deck. The app sends the uploaded document through an LLM API call, extracts key terms and concise descriptions, lets you edit the results in the browser, and saves the deck locally in SQLite for later review.

The LLM layer uses an OpenAI-style API key and base URL configuration, so you can point it at TritonAI or another OpenAI-compatible provider.

## Project Description

- Upload an image or PDF of notes, handouts, or slides.
- Run an LLM API call to generate flashcard terms and descriptions.
- Edit the generated entries and adjust the suggested deck title before saving.
- Review saved decks in the browser.
- Keep extraction results and saved decks on the local machine in a SQLite database.

## Setup

1. Create and activate a virtual environment.
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables.
   Copy `.env.example` to `.env`.

## Environment Variables

The app uses OpenAI-style environment variables for the LLM call. If you are using TritonAI, keep the Triton defaults. If you are using xAI, set `XAI_API_KEY` and either `XAI_MODEL=xai/grok-4-1-fast-reasoning` or another LiteLLM-style `xai/...` model name. If you are using another OpenAI-compatible provider, update the base URL and model to match that provider.

Example configuration:

```env
# OpenAI-compatible provider example
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_MODEL=gpt-4.1-mini

# xAI-compatible provider example
XAI_API_KEY=your_xai_api_key_here
XAI_BASE_URL=https://api.x.ai/v1
XAI_MODEL=xai/grok-4-1-fast-reasoning

# TritonAI-compatible defaults
TRITON_API_KEY=your_triton_api_key_here
TRITON_BASE_URL=https://tritonai-api.ucsd.edu/v1
TRITON_MODEL=api-llama-4-scout
```

## How To Run

Start the app with either command:

```bash
uvicorn app:app --reload
```

or

```bash
python app.py
```

Then open the app in your browser:

- `http://127.0.0.1:8000`

How to use the app:

1. Upload an image or PDF of your document.
2. Optionally choose a flashcard preference.
3. Click `Extract flashcards`.
4. Review and edit the extracted entries and deck title.
5. Click `Save deck` to store the deck locally.
6. Use the Review tab to study saved decks.

## Review Workflow

- Select one or more saved decks in the Review tab.
- Start a review session to mix the selected decks into one queue.
- View the term first and try to recall its meaning before looking at the answer.
- Reveal the answer when you are ready to check yourself.
- Choose a familiarity level after revealing the answer. `Know` means you recalled it well, `Unsure` means you recognized it but were not fully confident, and `Don't know` means you could not recall it yet.
- Cards return to the queue based on that score, and a card completes after you select `Know` three times in a row.

## Demo Video

[Watch on YouTube](https://youtu.be/fI-fTzASavg)

## AI Transcripts

Transcript files are stored in the [`transcripts/`](transcripts/) folder.

## Code Structure

- Frontend: vanilla HTML/CSS/JavaScript in `static/`. `static/index.html` defines the layout, `static/app.js` boots the app, `static/modules/upload.js` handles file selection and the `POST /api/extract` upload request, `static/modules/decks.js` manages saved decks, `static/modules/review.js` powers review sessions, and `static/modules/utils.js` holds shared helpers.
- Backend: FastAPI in `app.py` plus the `flashcard/` package. `app.py` serves the UI and exposes API routes such as `POST /api/extract`, `POST /api/decks`, and `PUT /api/decks/{deck_id}`; `flashcard/extraction.py` sends the uploaded file through the LLM API call and parses the response; `flashcard/storage.py` reads and writes records in SQLite; `flashcard/models.py` defines the shared request and response models.
- Data framework: Pydantic models with local SQLite storage. `flashcard/models.py` defines `FlashcardEntry`, `ExtractionRecord`, `DeckCreate`, and `DeckRecord`, while `flashcard/storage.py` persists those objects under `data/flashcards.db` so extracted decks and sessions stay local.
