# 🌐 LinguaFlow – AI-Powered Language Learning Platform

LinguaFlow is a full-stack AI-powered language learning platform designed to provide an interactive and personalized language-learning experience. Users can create accounts, learn through structured lessons, practice questions, track their progress, earn XP, maintain learning streaks, and compete on a leaderboard.

## ✨ Features

- 🔐 User Signup & Login
- 🛡️ JWT-based Authentication
- 🌍 Multiple Language Support
- 📚 Structured Languages, Units & Lessons
- 🤖 AI-powered Question Generation using Google Gemini
- ✅ AI-based Answer Evaluation
- ⭐ XP and Level System
- 🔥 Learning Streak Tracking
- 📊 Personalized Progress Dashboard
- 🏆 XP-based Leaderboard
- 👤 User Profile & Progress
- 📱 Responsive UI
- 🔒 Protected Routes
- 🚀 RESTful APIs

## 🛠️ Tech Stack

### Frontend

- React.js
- TypeScript
- Vite
- Tailwind CSS
- React Router

### Backend

- Python
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication

### Database

- PostgreSQL
- Neon PostgreSQL

### AI

- Google Gemini API

### Tools

- Git
- GitHub
- VS Code

## 📁 Project Structure

```
LinguaFlow/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── context/
│   │   ├── hooks/
│   │   └── types/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── routers/
│   │   ├── services/
│   │   └── utils/
│   ├── requirements.txt
│   └── .env
│
└── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```
git clone https://github.com/badallsingh/Linguaflow.git
cd Linguaflow
```

### 2. Frontend Setup

```
cd frontend
npm install
npm run dev
```

The frontend will run on:

```
http://localhost:5173
```

### 3. Backend Setup

Open a new terminal:

```
cd backend

python -m venv .venv
source .venv/bin/activate
```

On Windows:

```
.venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Start the FastAPI server:

```
uvicorn app.main:app --reload
```

The backend will run on:

```
http://127.0.0.1:8000
```

API documentation:

```
http://127.0.0.1:8000/docs
```

## 🔑 Environment Variables

Create a `.env` file inside the backend directory:

```
DATABASE_URL=your_postgresql_connection_string
SECRET_KEY=your_secret_key
GEMINI_API_KEY=your_gemini_api_key
```

**Never commit your `.env` file or API keys to GitHub.**

## 🔄 Application Flow

```
User
	↓
Signup / Login
	↓
JWT Authentication
	↓
Dashboard
	↓
Select Language
	↓
Select Unit
	↓
Start Lesson
	↓
Practice Questions
	↓
AI Evaluation
	↓
XP + Progress + Streak
	↓
Leaderboard
```

## 🔌 Main API Modules

| Module | Description |
| --- | --- |
| `/auth` | Signup, Login & Authentication |
| `/languages` | Language management |
| `/units` | Unit management |
| `/lessons` | Lesson management |
| `/lesson` | Lesson completion & XP |
| `/user` | User dashboard & progress |
| `/league` | Leaderboard |
| `/ai` | AI question generation & evaluation |

## 🤖 AI Integration

LinguaFlow uses the **Google Gemini API** to generate dynamic language-learning questions and evaluate user responses.

This allows the platform to provide more flexible learning exercises instead of relying only on predefined questions.

## 📊 Learning System

Users can earn **XP** by completing lessons and exercises. Their XP contributes to their level and leaderboard position. The application also tracks learning streaks and completed lessons to provide users with continuous progress feedback.

## 🔮 Future Improvements

- Speaking and pronunciation exercises
- Voice-based AI evaluation
- More languages
- Advanced analytics
- Admin dashboard
- Personalized learning recommendations
- Achievement and badge system
- Mobile application

## 👨‍💻 Author

**Badal Singh**

B.Tech Computer Engineering
Shri Vishwakarma Skill University

## 📄 License

This project is developed for educational and portfolio purposes.
