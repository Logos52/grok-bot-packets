# LernSkool – Sachsen: Gymnasium Kl. 8 und Oberschule Kl. 5

Tablet-Lern-App für mehrere Kinder nach den sächsischen Lehrplänen (Inhaltspakete: Gymnasium Klasse 8, Oberschule Klasse 5): Lektionen mit Vorlesefunktion, Übungen, Tests mit Note, Arbeitsblätter, Vokabeltrainer, Fehlerheft und ein Lernplan.

**App:** https://marcelweissgerberit.github.io/FrenchSkool/

## Funktionen

- **Fächer** mit Themen nach den Lernbereichen der sächsischen Lehrpläne (Kl. 8), je Thema Lernkarten (🔊 vorlesen), Übung (10 Fragen) und Test mit Note (15 Fragen), plus Fach-Test über alle Themen
- **Lernplan**: Klassenarbeiten mit Datum und Themen eintragen, Themen „gerade im Unterricht“ markieren (📌) → Startseite schlägt unter „Heute üben“ die passenden, schwächsten Themen vor
- **Französisch** als eigene Sub-App (`#/fr`): Verben im Présent mit Aussprache, Nachsprechen und mündlicher Prüfung per Mikrofon
- Ergebnisse mit Notendurchschnitt pro Fach; Fehler gezielt nochmal üben
- Offline-fähig (PWA, „Zum Home-Bildschirm“); Fortschritt wird lokal auf dem Gerät gespeichert
- **Mehrere Kinder**: je Kind Name, Alter, Avatar, Schulform und Klasse; eigene Fortschritte und passende Inhalte (Inhaltspakete in `tools/packages.json`)
- **Vokabeltrainer** (eigene Listen EN/FR, Karteikarten, Schreiben, Hören, Karteikasten mit 5 Fächern) und **Fehlerheft** (falsche Antworten kommen nach 1, 3 und 7 Tagen wieder)
- **Datensicherung** (Export/Import als Datei), **Fehler melden** und **Offline speichern** im Elternbereich
- **Arbeitsblätter**: 6 gestaltete Arbeitsblätter pro Fach (Lückentext, Tabelle, Zuordnen, Reihenfolge, freie Aufgaben mit Musterlösung) sowie Arbeitsblätter aus der Schule per Foto/PDF mit Stift bearbeiten
- **Kindermodus** mit Eltern-Code, Lehrplan-Quellen (PDF) pro Fach, natürliche KI-Stimmen für Französisch/Englisch
- Bilder, Avatare und Icons erstellt mit OpenArt

## Inhalte ergänzen

Inhalte sind in Pakete je Bundesland/Schulform/Klasse gegliedert (`tools/packages.json`): Gymnasium 8 liegt in `js/subjects` und `js/worksheets`, Oberschule 5 in `content/sn-os-5/`. Jedes Fach ist eine Datei, die `registerSubject({...})` aufruft; Themenbilder liegen unter dem `imgBase` des Pakets.
Nach dem Hinzufügen eines Fachs:

```sh
node tools/check-content.js [dir]  # prüft alle Fächer (Antwort-Indizes, Erklärungen, Bilder, keine Emojis …)
node tools/check-worksheets.js [subjects-dir worksheets-dir]  # prüft die Arbeitsblätter
node tools/audio-texts.js          # listet fr/en-Texte für Sprachaufnahmen, baut js/audio-index.js
python3 tools/update-subjects.py   # baut js/packages.js und den Offline-Cache in sw.js
```

Veröffentlicht wird automatisch über GitHub Pages bei jedem Push auf `main`.
