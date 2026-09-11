# LingoEcho — AI Conversational Tutor & Pronunciation Coach

> **Academic Project Origin**  
> The concept for **LingoEcho** was conceived and developed as part of a university project assignment. It addresses a very real and widespread educational challenge: the difficulty, hesitation, and anxiety that language learners face when trying to practice spoken conversation with real people, alongside the need for a practical, bite-sized tool that fits into busy daily routines to maintain and sharpen language fluency.

---

## 💡 The Problem & Purpose

Learning a new language is often hindered by two major obstacles:

1. **Speaking Anxiety & Fear of Judgment:** Many students study grammar rules and vocabulary for years, yet freeze when speaking to native speakers or classmates. The fear of making mistakes, having an accent, or pausing awkwardly prevents them from ever speaking freely.
2. **Fast-Paced Daily Routines:** Traditional language courses or weekly tutoring sessions demand rigid scheduling and substantial time commitments. Busy professionals and university students struggle to find hours in their week, leading to skill stagnation and lost fluency.

**LingoEcho** bridges this gap. It provides a judgment-free, patient, and immersive conversation partner powered by artificial intelligence. Learners can practice speaking at any time, in 3-minute increments between tasks or during dedicated study blocks, receiving instant feedback on pronunciation, grammar, and natural phrasing.

---

## ✨ Key Features

### 🎙️ 1. Voice-First Conversational Roleplay
- Speak directly into the microphone with live speech-to-text transcription.
- Real-time audio wave meter for responsive visual feedback.
- Tailored scenarios (Ordering food in Paris, job interviews in Berlin, travel check-ins in Tokyo, casual chats in New York, and more).
- Bite-sized conversational turns that encourage active student speaking time.

### 🔬 2. Phonetics & Pronunciation Lab
- In-depth word-by-word pronunciation analysis powered by Google Gemini.
- Highlights words that are **Perfect**, **Good**, **Needs Work**, or **Missed**.
- Phonetic transcriptions (**IPA**), syllable breakdown with stressed syllable capitalization, and mouth/tongue articulation tips.
- Specialized advice targeting common interference patterns (such as Portuguese-speaker tendencies to add vowels after final consonants or nasalize sounds).
- Custom sentence tester: type any sentence in any supported language to evaluate pronunciation.

### 🌐 3. Multi-Language Support (Top 10+ World Languages)
Seamlessly switch between languages and regional accents:
- 🇺🇸 **English** (American, British, Australian)
- 🇪🇸 **Spanish** (Spain, Mexico, Argentina)
- 🇫🇷 **French** (France, Canada)
- 🇩🇪 **German** (Germany, Austria, Switzerland)
- 🇮🇹 **Italian** (Italy)
- 🇯🇵 **Japanese** (Standard Tokyo)
- 🇨🇳 **Mandarin Chinese** (Standard Simplified)
- 🇰🇷 **Korean** (Standard Seoul)
- 🇷🇺 **Russian** (Standard Moscow)
- 🇸🇦 **Arabic** (Modern Standard)
- 🇧🇷 **Portuguese** (Brazil, Portugal)

### ✍️ 4. Real-time Grammar Feedback & "False Friends" Alerts
- Automatically spots grammatical inaccuracies, syntax slips, and false cognates.
- Explains corrections warmly in Portuguese (or the chosen native language) so you understand *why* it changed.
- Offers a **"Natural Alternative"** showcasing how native speakers colloquially or professionally express the same thought.

### 💡 5. "How Do I Say...?" Nuance & Idiom Assistant
- Instant translation and nuance lookup for idioms, slang, and expressions.
- Shows both **casual/street** and **formal/workplace** variations.
- Includes contextual dialogue examples and audio pronunciation.
- One-click insertion directly into your active conversation.

### 📓 6. Saved Words & Review Notebook
- Bookmark tricky words encountered during roleplay or phonetics lab.
- Review syllable stress, IPA guides, and phonetic tips anytime.
- Practice pronouncing them with the microphone to reinforce muscle memory.

---

## 🛠️ Technology Stack

- **Frontend:**
  - [React 18](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/)
  - [Vite](https://vitejs.dev/) for fast module bundling
  - [Tailwind CSS](https://tailwindcss.com/) for modern, responsive UI design
  - [Lucide React](https://lucide.dev/) for crisp, accessible iconography
  - **Web Speech API:** Browser-native `SpeechRecognition` and `SpeechSynthesis`
- **Backend:**
  - [Express](https://expressjs.com/) on [Node.js](https://nodejs.org/)
  - TypeScript executed seamlessly with `tsx` and bundled with `esbuild`
  - [@google/genai](https://www.npmjs.com/package/@google/genai) SDK for high-performance AI responses and pronunciation diagnostics
  - Structured JSON schema enforcement with Gemini models

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18 or higher recommended)
- A modern web browser with microphone access (Google Chrome, Edge, or Safari recommended for full Web Speech API compatibility)
- A **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/lingoecho.git
   cd lingoecho
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Configure Environment Variables:**
   Create a `.env` file in the project root:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Start the Development Server:**
   ```bash
   npm run dev
   ```

5. **Open the Application:**
   Open your browser and navigate to `http://localhost:3000`.

---

## 📱 How to Use

1. **Choose Your Target Language & CEFR Level:** Use the language selector in the top bar (e.g., English, French, Spanish, Japanese) and pick your proficiency level (A1 to C1).
2. **Select a Conversation Scenario:** Pick a real-life scenario from the dropdown (e.g., ordering coffee, casual networking, job interview).
3. **Speak or Type:** Click the microphone button and talk naturally. The AI will respond with text and spoken audio.
4. **Learn from Feedback:** Click on any message to inspect grammar corrections, read pronunciation warnings, or practice specific words.
5. **Visit the Pronunciation Lab:** Access the **Pronunciation Lab** tab to complete phonetic exercises or test your own custom phrases.
6. **Save Tricky Words:** Hit the bookmark icon on any difficult word to review it later in the **Review** tab.

---

## 🎓 Academic Acknowledgments & Vision

This project was built with the conviction that education should be accessible, humane, and stress-free. By simulating authentic language interactions in a supportive environment, LingoEcho empowers learners around the world to conquer communication barriers and maintain their language skills amidst demanding everyday schedules.
