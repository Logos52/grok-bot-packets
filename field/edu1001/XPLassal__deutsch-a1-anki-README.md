# Deutsch A1 · Anki Flashcards

Официальный словарь Goethe-Zertifikat A1 (~617 лемм), упакованный в стильные Neo-Brutal-Sticker карточки для Anki.

**Источник слов:** Goethe-Zertifikat A1: Fit in Deutsch 1 — Wortliste (2. Auflage, 2024), дополненный темами BAMF Rahmencurriculum (Behörden, Arbeit, Gesundheit).
**Уровень:** A1 (полный охват Wortliste).
**Поля карточки:** `Russian`, `Hint`, `German`, `Example`, `ExampleRU`, `Plural`.
**Темы:** 24 подколоды (`A1::Person`, `A1::Wohnen`, `A1::Essen`, …).
**Частота:** теги `Top100`, `Top300`, `Top650` для фильтрации в Anki.

## 🚀 Как использовать

### Быстрый путь
1. Скачай [`deutsch_a1.apkg`](./deutsch_a1.apkg).
2. Открой файл двойным кликом — Anki сам импортирует колоду.
3. Или в Anki: **File → Import** → выбери `deutsch_a1.apkg`.

### Если хочешь править слова
1. Открой `generate_tsv.py`, найди нужную тему в `WORDS`, добавь слово.
2. Запусти `python generate_tsv.py` — обновится `deutsch_a1.tsv`.
3. Запусти `python create_apkg.py` — обновится `deutsch_a1.apkg`.
4. Импортируй свежий `.apkg` в Anki.

### Если хочешь править шаблон карточки
Шаблон живёт в трёх файлах — правь их в любом редакторе с подсветкой:
- `front.html` — лицевая сторона + JS (проверка ввода, анимации)
- `back.html` — оборотная сторона + JS (озвучка, цветные артикли, кнопки оценки)
- `style.css` — стили (Neo-Brutalism, тёмная тема, мобильная адаптация)

После правки:
1. `python sync_template.py` — заливает изменения в `model_dump.json`.
2. `python create_apkg.py` — пересобирает `.apkg`.

На Windows всё то же делает `./run.ps1`.

## 📁 Что внутри

| Файл | Назначение |
|---|---|
| `generate_tsv.py` | Словарь слов → TSV. **Источник правды.** |
| `create_apkg.py` | TSV + модель → готовый `.apkg` для Anki. |
| `model_dump.json` | Снимок шаблона из `example.apkg` (модель, CSS, JS). |
| `deutsch_a1.tsv` | Сгенерированный TSV, читается в GitHub-браузере. |
| `deutsch_a1.apkg` | Готовый пакет Anki. |

## 🛠 Зависимости

- Python 3.10+
- `pip install genanki`

## ⚖ Лицензия

Слова из Wortliste Goethe-Institut — под лицензией **CC-BY-SA 4.0**.
Код и шаблон карточек — **MIT**.
