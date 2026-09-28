# Deutsch Üben (no README — fetched index.html + js/lessons.js + js/data/lessons-data.js)
Desc: Learn German by speaking and reading — placement test, lessons, AI tutor, factory-tour phrasebook
Created: 2026-09-26
URL: https://github.com/cointugboat8211/deutsch-ueben

## Nav (from index.html)
Dashboard · Lessons · Conversation · Reading · AI Tutor. PWA (manifest + service worker).

## Lessons mechanism (from lessons.js)
- Placement-aware path: A1→u3, A2→u4 else u1; recommend next incomplete lesson.
- Daily Review from due vocab (up to 16).
- Speech: speakGerman + speechRecognition listenOnce + matchesExpected.
- Units with lesson list, streak + XP pills.

## lessons-data.js head
// Course content. Exercises are generated from `items` (words/phrases) and
// `sentences` (full sentences, used for word-tile and speaking exercises), so
// authoring a lesson only needs correct German + English.
//
// lesson.qa (optional): German-only "which answer fits?" pairs { q, a, wrong: [..] }
// item.pic (optional): an emoji, used for German-only picture exercises (added by PICS below)
//
// lesson.digits (optional) adds generated "hear a number/price, type the digits" drills:
//   { kind: "number", lo, hi, count }  or  { kind: "price", count }

const w = (de, en, note) => ({ de, en, ...(note ? { note } : {}) });

export const lessonUnits = [
  {
    id: "u1",
    title: "Erste Schritte",
    titleEn: "First steps",
    emoji: "👋",
    lessons: [
      {
        id: "u1l1",
        title: "Greetings",
        items: [
          w("Hallo", "Hello", "HAH-loh"),
          w("Guten Morgen", "Good morning", "GOO-ten MOR-gen"),
          w("Guten Tag", "Good day / Hello", "GOO-ten tahk"),
          w("Guten Abend", "Good evening", "GOO-ten AH-bent"),
          w("Tschüss", "Bye", "chewss"),
          w("Auf Wiedersehen", "Goodbye (formal)", "owf VEE-der-zay-en"),
        ],
        sentences: [
          w("Hallo, wie geht's?", "Hello, how are you?"),
          w("Mir geht es gut.", "I'm doing well."),
          w("Guten Morgen, Anna!", "Good morning, Anna!"),
        ],
      },
      {
        id: "u1l2",
        title: "Polite words",
        items: [
          w("Bitte", "Please / You're welcome", "BIT-teh"),
          w("Danke", "Thank you", "DAHN-keh"),
          w("Vielen Dank", "Thank you very much"),
          w("Entschuldigung", "Excuse me / Sorry", "ent-SHOOL-dee-gung"),
          w("Ja", "Yes"),
          w("Nein", "No"),
        ],
        sentences: [
          w("Ja, bitte.", "Yes, please."),
          w("Nein, danke.", "No, thank you."),
          w("Vielen Dank, tschüss!", "Thank you very much, bye!"),
        ],
      },
      {
        id: "u1l3",
        title: "Introducing yourself",
        items: [
          w("Ich heiße", "My name is (I am called)"),
          w("Wie heißt du?", "What's your name?"),
          w("Ich komme aus", "I come from"),
          w("Woher kommst du?", "Where are you from?"),
          w("Freut mich", "Nice to meet you"),
          w("Ich bin", "I am"),
        ],
        sentences: [
          w("Ich heiße Anna.", "My name is Anna."),
          w("Ich komme aus Amerika.", "I come from America."),
        
