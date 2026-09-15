# 🇲🇦 Tilmidh Agent: Moroccan Primary Education & AI Companion

[![Apache 2.0 License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Vue 3](https://img.shields.io/badge/Vue-3.3%2B-emerald.svg)](https://vuejs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-4.0-cyan.svg)](https://tailwindcss.com/)

**Tilmidh Agent** is an open-source, interactive educational PWA and AI-powered companion tailored for Moroccan primary school students (**1re à 6e Année Primaire / 1AP–6AP**), parents, and educators. It aligns with official Ministry of National Education guidelines to make learning engaging, accessible, and transparent.

---

## 🌟 Key Benefits

### 🎒 For Students
- **Interactive Quizzes & Matching**: Practice Arabic, French, Mathematics, Islamic Education, Science, and Social Studies through gamified quizzes with instant audio-visual feedback.
- **Regional Explorer**: Discover all 12 regions of Morocco, capital cities, regional plates, local specialties, and iconic monuments.
- **Memory & Matching Challenges**: Fun cognitive exercises to reinforce memory and vocabulary across multiple languages.
- **Multilingual Support**: Seamless switching between **Arabic (العربية)**, **French (Français)**, and **English**.

### 👨‍👩‍👧‍👦 For Parents
- **Weekly Sommaires & Curricula**: Clear, week-by-week summaries of what children are learning in school.
- **Ministry Holidays & Exam Alerts**: Stay up-to-date with official school holiday schedules, continuous assessment dates, and regional exam periods.
- **Zero-Auth & Offline Friendly**: Fast loading, private local storage of student progress, stars, and badges without requiring complex account creation or cloud data collection.

---

## 🛠️ System Architecture

- **Frontend**: Vue 3 (Composition API), TypeScript, Tailwind CSS, Lucide Icons, and Canvas confetti.
- **Backend / API**: Node.js & Express server handling AI proxy requests and tool calling.
- **AI Integration**: Google Gemini API integration for dynamic curriculum assistance, quiz generation, and educational support.
- **Architecture Diagram**: View [`architecture_diagram.jpg`](architecture_diagram.jpg) in the root directory for a complete system layout.

---

## 🚀 Getting Started for Developers

To run Tilmidh Agent locally for development or contribution:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/tilmidh-agent.git
   cd tilmidh-agent
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Configure environment variables**:
   Copy `.env.example` to `.env` and add your server configuration:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the development server**:
   ```bash
   npm run dev
   ```
   Open `http://localhost:3000` in your browser.

---

## 🤝 How to Contribute

We welcome contributions from educators, developers, designers, and language experts! Whether you want to add new quiz questions, translate content, improve UI responsiveness, or enhance the AI agent tools:

1. **Fork the repository**.
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`.
3. **Commit your changes**: `git commit -m 'Add some amazing feature'`.
4. **Push to the branch**: `git push origin feature/amazing-feature`.
5. **Open a Pull Request**.

Please ensure your code passes TypeScript checks (`npm run lint`) and builds successfully (`npm run build`).

---

## 📜 License

This project is open-source software licensed under the **[Apache License 2.0](LICENSE)**.
