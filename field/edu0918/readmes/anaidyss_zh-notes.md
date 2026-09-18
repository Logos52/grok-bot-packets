# zh-notes

![zh demo](assets/demo.gif)

a cli for taking chinese lesson notes. you type a word in pinyin or paste the
hanzi, it looks it up offline in CC-CEDICT plus a russian dictionary, and it
appends one markdown line to the note you are working on:

    - <ruby>学习<rt>xuéxí</rt></ruby> — учиться; изучать; учеба #HSK1 #u03

obsidian renders that as pinyin on top of the hanzi, and the same line is what
the anki deck builder eats. the note file is the only source of truth, there is
no separate word database to keep in sync. 125 071 dictionary entries, 101 223
of them with a russian meaning, HSK 2.0 and 3.0 levels as tags.

the vault layout and the russian glosses are russian, because that is the part
that made it worth writing. everything else, including the dictionary lookups,
works in any language you put in the meaning.

## install

    ./install.sh                # cedict + hsk, about 15 s to build
    ./install.sh --with-bkrs    # plus the russian dictionary, 86 MB download
    ./install.sh --with-timer   # plus the systemd timer that commits the vault

needs: python3, curl, and for the full experience fcitx5 with the pinyin addon
(to type hanzi at all), obsidian, anki. fuzzel, fzf, mako, espeak-ng and
wl-copy are optional, `zh doctor` says which are missing and what you lose.

the script puts the python package into `~/.local/share/zh-notes`, the three
launchers into `~/.local/bin`, fish completions into `~/.config/fish`, and
downloads the dictionaries into `~/.local/share/zh-notes/dicts`. it does not
touch your compositor config, the two lines for fcitx5 and the keybinding are
in [MANUAL.md](MANUAL.md).

## use

    zh new                  # next lesson note, target for everything below
    zh 学习                 # look it up, plus where it already is in your notes
    zh -a 学习              # append it to the active lesson
    zh -q shi4              # no questions, refuses when it cannot choose
    zh -q tao -m персик     # the meaning picks the hanzi: 桃, not 套
    zh -i 了                # fzf picker when a word has five readings
    zh undo                 # take the last write back
    zh show                 # the lesson as readable text
    zh find учиться         # search your notes by meaning, pinyin or hanzi
    zh ruby 我喜欢学习中文    # annotate a whole sentence
    zh anki --open          # build the deck and hand it to anki

bind the popup capture to a key and you never leave the note:

    Mod+Z       { spawn "/home/you/.local/bin/zh-fuzzel"; }
    Mod+Shift+Z { spawn "/home/you/.local/bin/zh-fuzzel" "--ask"; }
    Mod+O       { spawn "/home/you/.local/bin/zh-open"; }

`Mod+Z` writes the dictionary meaning, `Mod+Shift+Z` asks for yours. both take
pinyin on the english layout, `shi4` style tone digits work and skip the
picker, and the prompt shows the tone cheat sheet:

```text
тоны: 1 ā · 2 á · 3 ǎ · 4 à · 5 нейтр.   shi4 = 是, de5 = 的
汉字  пиньинь> shi
какое слово? > 是  shì   быть
               十  shí   10; десять
```

## how it works

- one sqlite file, five match queries (exact hanzi, hanzi prefix, numbered
  pinyin when you typed a tone digit, toneless pinyin, pinyin prefix) plus fts5
  over hanzi, pinyin, english and russian glosses. the sort puts an exact match
  above a prefix hit, a real reading above a cross reference, HSK level 1 above
  level 5, a word's primary reading above its rare ones, and then the more
  frequent word first. each step fixes a real mistake: without the exact match
  rule `中` loses to 中介, without the cross reference rule `书` comes out as
  `abbr. for 書經`, without the primary reading rule `di` picks 的 dí over
  地 dì, and HSK levels alone cannot separate 的 from 地 because both are
  level 1, which is what the frequency counts are for
- readings are disambiguated by pinyin with tone marks, not the toneless form,
  otherwise 上 shǎng and 上 shàng both collapse to `shang`. tie breaks go to
  the order of readings in the dictionary entry, which is how 说 comes out as
  shuō and not shuì
- a typed meaning is scored against the russian and english glosses of every
  candidate and picks the hanzi itself, so `tao` + `персик` gives 桃 and
  `tao` + `peach` gives the same. when several words tie, the best ranked one
  wins and the rest show up in the notification
- the guard accepts a query only if it is hanzi or decomposes entirely into real
  pinyin syllables, taken from CEDICT and filtered by syllable shape. the search
  covers russian and english glosses, so without it `привет` writes 嗨 and
  `learn` writes 了解. CEDICT's pinyin column holds junk like `b` and `xx`, and
  with those in the set `learn` splits as `le + a + r + n` and gets through
- when several *different* words tie on rank, `-q` refuses and the popup shows a
  picker instead of guessing. different tones of one hanzi are not a tie, so
  `hao` writes 好 hǎo without asking
- a card is a line that starts with `-` and whose head is nothing but ruby
  groups, so prose and code blocks in the same file are ignored, fenced and
  indented alike. generated files carry `zh_generated: true` and are skipped,
  otherwise the index would feed its own words back into the deck
- capturing a word that is already in the note merges into it instead of
  duplicating, with ` / ` between different scripts, so an english meaning from
  class and a russian one added in the evening share a card
- anki gets `学习[xuéxí]` with `{{furigana:Hanzi}}` in the template, not raw
  `<ruby>`. anki's html filter allows ruby only in the extended set, which runs
  on paste into the editor, so raw ruby gets stripped the moment you edit the
  field. the native furigana syntax survives, and renders to the same
  `<ruby><rb>学习</rb><rt>xuéxí</rt></ruby>`
- guids are a hash of hanzi, pinyin and meaning, so reimporting updates cards
  instead of duplicating them
- meanings you type with `-m` are stored as your own and win over the
  dictionary next time. an english gloss never gets stored as yours
- `zh undo` keeps a 20 entry history, re-reads the line before touching it, and
  restores the previous text when undoing a merge

## data

- CC-CEDICT, mdbg.net, CC BY-SA 4.0
- 大БКРС, bkrs.info, free to use with the site credited, 86 MB DSL dump
- HSK 3.0 word list, [elkmovie/hsk30](https://github.com/elkmovie/hsk30), MIT,
  copyright 2021 Pleco Inc
- HSK 2.0 with russian translations,
  [LiudmilaLV/json_hsk](https://github.com/LiudmilaLV/json_hsk), no license
  stated, so it is downloaded at install time and not redistributed here
- word frequencies,
  [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords),
  OpenSubtitles counts for 50 000 zh words

no dumps and no database are in this repo, `zh db build` recreates everything.

the gif is reproducible: `assets/record.sh` records `assets/demo.sh` with
asciinema, renders it through termtosvg, rasterizes with headless chrome and
assembles the frames with ffmpeg. it runs against throwaway paths in /tmp, so
no home directory ends up in the recording.

## manual

[MANUAL.md](MANUAL.md): setup from scratch including fcitx5 on niri and the
flatpak `--user` remote gotcha, the card format, every flag, how a word gets
picked, deck building, backups, troubleshooting.
