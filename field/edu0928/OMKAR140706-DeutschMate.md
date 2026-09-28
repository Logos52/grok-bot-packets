# 🇩🇪 DeutschMate

### An LLM-powered German language companion with tool calling, persistent vocabulary, conversation practice, and AI-powered pronunciation.

DeutschMate is a personal German language companion built to make German learning more interactive.

Instead of functioning as a simple chatbot, DeutschMate can **understand the user's intent, decide when to use external tools, save vocabulary to a persistent SQLite database, retrieve previously learned words, and respond with generated German speech.**

The project was built as a practical exploration of how LLMs can move beyond generating text and interact with external tools, databases, and audio systems.

---

## ✨ Features

* 💬 Natural German conversation practice
* 🧠 Persistent vocabulary memory
* 🔧 LLM function / tool calling
* 📚 Automatic vocabulary saving
* 🔎 Retrieval of previously learned vocabulary
* 📈 Vocabulary review tracking
* ⚡ LLM-powered conversational responses
* 🔊 AI-generated German pronunciation
* 🗣️ Multimodal chat with text and audio
* 🖥️ Gradio interface
* 💾 SQLite-based local vocabulary database

---

## 🧠 How DeutschMate Works

DeutschMate uses Gemini as the language model and gives it access to Python functions that act as external tools.

The overall architecture is:

```text
                    ┌──────────────────┐
                    │      User        │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Gradio Chat UI  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Gemini      │
                    │      LLM         │
                    └────────┬─────────┘
                             │
                    Does the request
                    require a tool?
                       /          \
                     No            Yes
                     │              │
                     ▼              ▼
                Final answer    Tool call
                                    │
                                    ▼
                            ┌───────────────┐
                            │ Python Tool   │
                            └───────┬───────┘
                                    │
                                    ▼
                            ┌───────────────┐
                            │ SQLite DB     │
                            └───────┬───────┘
                                    │
                                    ▼
                              Tool result
                                    │
                                    ▼
                                Gemini
                                    │
                                    ▼
                              Final answer
                                    │
                                    ▼
                            Gemini TTS
                                    │
                                    ▼
                              Audio output
```

This allows the LLM to combine its language capabilities with deterministic Python functions and persistent application data.

---

## 🔧 LLM Tool Calling

DeutschMate currently provides Gemini with two tools.

### 1. `save_new_word`

This tool saves a German word or short phrase that the student has learned.

The tool accepts:

```text
german
english
example_sentence
```

For example:

```text
German:
Kühlschrank

English:
refrigerator

Example:
Der Kühlschrank ist leer.
```

The information is passed to the Python function:

```python
save_new_word(
    german,
    english,
    example_sentence
)
```

The function then stores the vocabulary in the SQLite database.

---

### 2. `get_known_words`

This tool retrieves the German vocabulary that the student has already saved.

It returns:

```text
German word
English translation
Number of times reviewed
```

For example:

```text
Kühlschrank = refrigerator (reviewed 1x)
```

The LLM can use this tool when the student asks what they have learned so far or when previously learned vocabulary should be reviewed.

---

## 🗄️ Vocabulary Database

DeutschMate uses **SQLite** for local persistent storage.

The database contains a `vocab` table with four fields:

| Field              | Description                                |
| ------------------ | ------------------------------------------ |
| `german`           | German word or phrase                      |
| `english`          | English translation                        |
| `example_sentence` | Example sentence using the word            |
| `times_reviewed`   | Number of times the word has been reviewed |

The database is initialized automatically when the application starts.

```sql
CREATE TABLE IF NOT EXISTS vocab (
    german TEXT PRIMARY KEY,
    english TEXT,
    example_sentence TEXT,
    times_reviewed INTEGER DEFAULT 0
)
```

The `times_reviewed` field also provides a foundation for future spaced-repetition functionality.

---

## 🔄 Agent / Tool Execution Loop

One of the main concepts explored in this project is the **tool-calling loop**.

When a user sends a message, Gemini first receives the conversation and the available tools.

If Gemini decides that it needs a tool, the application executes the requested Python function.

The flow is:

```text
User message
     ↓
Gemini
     ↓
Tool required?
     ↓
Tool call
     ↓
handle_tool_calls()
     ↓
Python function
     ↓
SQLite database
     ↓
Tool result
     ↓
Gemini
     ↓
Final response
```

The application continues this process while Gemini requests additional tool calls.

This is what allows DeutschMate to perform actions instead of simply generating text.

---

## 🧠 System Prompt

DeutschMate uses a system prompt to define the behavior of the German tutor.

The tutor is designed for an **A1-level student** and is instructed to:

* Communicate primarily in German at approximately A2 level
* Provide short English explanations for difficult language
* Correct mistakes gently
* Keep conversations short and natural
* Automatically save important vocabulary
* Retrieve saved vocabulary when appropriate
* Avoid turning the conversation into grammar drills

This allows the LLM to behave more like a conversational language companion rather than a generic chatbot.

---

## 🔊 AI Text-to-Speech

DeutschMate also includes German text-to-speech.

The project uses the Gemini native SDK for the TTS model.

The flow is:

```text
Gemini text response
        ↓
      TTS
        ↓
Generated PCM audio
        ↓
Python BytesIO buffer
        ↓
WAV container
        ↓
Gradio Audio component
        ↓
Automatic playback
```

The generated PCM audio is wrapped into a WAV container before being sent to the Gradio audio component.

The current implementation uses:

```text
24 kHz
16-bit
Mono
```

audio.

The generated speech is automatically played through the Gradio interface.

---

## 💬 Multimodal Conversation Flow

The final interface combines:

**Text → LLM → Tools → Database → Text → TTS → Audio**

For example:

```text
User:
"Teach me a useful German word."

        ↓

Gemini

        ↓

save_new_word()

        ↓

SQLite

        ↓

Gemini generates response

        ↓

Gemini TTS

        ↓

🔊 German pronunciation
```

This makes the application more than a text-only chatbot.

---

## 📚 Example Interaction

### User

> Hallo! Ich bin neu in Deutsch.

### DeutschMate

> Hallo! Willkommen! Keine Sorge, wir machen es einfach. Wie geht es dir?

The tutor can introduce useful vocabulary during the conversation.

For example:

> **Kühlschrank** = refrigerator
> *Der Kühlschrank ist leer.*

The word can then be saved automatically through the `save_new_word` tool.

Later, the student can ask:

> What German words have I learned?

DeutschMate can call:

```text
get_known_words
```

and retrieve the vocabulary stored in SQLite.

---

## 🛠️ What I Learned

Building DeutschMate helped me understand what happens **behind an LLM-powered application**, rather than simply calling an API and displaying its response.

### LLM Application Concepts

* Function / tool calling
* Structured tool definitions
* JSON tool arguments
* Tool execution
* Agent execution loops
* Conversation state
* Message history
* Streaming and conversational responses

### Backend / Application Concepts

* Connecting an LLM to Python functions
* Persistent local storage with SQLite
* Database CRUD operations
* Passing tool results back to an LLM
* Environment variable management
* Building an interactive Gradio application

### Audio / Multimodal Concepts

* Gemini text-to-speech
* Generating PCM audio
* Converting raw PCM into WAV
* In-memory binary buffers using `BytesIO`
* Connecting generated audio to a Gradio interface

Most importantly, the project helped me understand the difference between **using an LLM** and **building an application around an LLM**.

---

## ⚙️ Tech Stack

| Technology            | Purpose                       |
| --------------------- | ----------------------------- |
| Gemini                | Language model                |
| Gemini TTS            | German speech generation      |
| OpenAI-compatible API | LLM interaction layer         |
| Google GenAI SDK      | Native Gemini TTS integration |
| Python                | Application logic             |
| Gradio                | User interface                |
| SQLite                | Persistent vocabulary storage |
| python-dotenv         | Environment configuration     |

---

## 📁 Project Structure

```text
DeutschMate/
│
├── german_companion.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── .env          # Local only - not committed
├── vocab.db      # Local database - not committed
└── .venv/        # Local environment - not committed
```

The main implementation is currently contained in:

```text
german_companion.ipynb
```

The notebook walks through the project from initialization and database setup to tool calling, agent execution, TTS, and the Gradio interface.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/DeutschMate.git
cd DeutschMate
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your Gemini API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The `.env` file is intentionally excluded from Git through `.gitignore`.

### 5. Run the notebook

Open:

```text
german_companion.ipynb
```

in Jupyter Notebook, JupyterLab, or VS Code.

Run the cells sequentially to initialize the database, configure Gemini, load the tools, start the agent loop, and launch the Gradio interface.

---

## 🎥 Demo

A demonstration of DeutschMate shows:

1. 🇩🇪 German conversation
2. 📚 Learning new vocabulary
3. 🔧 Automatic tool calling
4. 💾 Saving vocabulary
5. 🔎 Retrieving known vocabulary
6. 🔊 AI-generated German pronunciation

---

## 🗺️ Roadmap

### Completed

* [x] Gemini LLM integration
* [x] German conversational tutor
* [x] System prompt
* [x] Conversation history
* [x] Function / tool calling
* [x] `save_new_word` tool
* [x] `get_known_words` tool
* [x] SQLite vocabulary database
* [x] Vocabulary review tracking
* [x] Gemini text-to-speech
* [x] Gradio chat interface
* [x] Automatic audio playback

### Future Improvements

* [ ] Spaced repetition using `times_reviewed`
* [ ] Dedicated daily quiz mode
* [ ] Difficulty progression from A1 → A2 → B1
* [ ] Pronunciation feedback
* [ ] German listening exercises
* [ ] Speaking practice
* [ ] Learning progress dashboard
* [ ] More advanced vocabulary analytics
* [ ] Lightweight local TTS option

---

## 🔐 Security

API keys and local user data are intentionally excluded from the repository.

The following files should never be committed:

```text
.env
vocab.db
.venv/
```

The repository includes `.env.example` so that other developers know which environment variable is required without exposing the actual API key.

---

## 🚧 Future Ideas

The existing `times_reviewed` field provides a foundation for implementing spaced repetition.

For example, future versions could prioritize words that have been reviewed less frequently and gradually increase their usage as the student becomes more comfortable with them.

Other possible extensions include:

* Personalized vocabulary recommendations
* Daily German conversations
* Adaptive CEFR difficulty
* Pronunciation scoring
* Listening comprehension
* Voice-based conversations
* Learning analytics

---

## 👨‍💻 Author

**Omkar Dabholkar**

Built as a practical exploration of **LLM application engineering, tool calling, persistent memory, and AI-assisted language learning.**

---

⭐ If you find DeutschMate interesting, feel free to explore the implementation and suggest improvements.

