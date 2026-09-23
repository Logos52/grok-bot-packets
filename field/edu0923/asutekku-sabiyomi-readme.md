# Sabiyomi

[![CI](https://github.com/asutekku/sabiyomi/actions/workflows/ci.yml/badge.svg)](https://github.com/asutekku/sabiyomi/actions/workflows/ci.yml)
[![crates.io](https://img.shields.io/crates/v/sabiyomi.svg)](https://crates.io/crates/sabiyomi)
[![docs.rs](https://img.shields.io/docsrs/sabiyomi)](https://docs.rs/sabiyomi)
[![MSRV](https://img.shields.io/badge/rust-1.88%2B-orange.svg)](https://blog.rust-lang.org/2025/06/26/Rust-1.88.0/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*sabi* (錆, rust) + *yomi* (読み, reading): Japanese readings, in Rust.

Japanese text → hiragana, katakana or romaji. Plain text in, plain text out.

```console
$ echo '今日は東京で日本語を勉強します' | sabiyomi --to romaji
kyōwatōkyōdenihongoobenkyōshimasu

$ echo '今日は東京で日本語を勉強します' | sabiyomi --to romaji --mode spaced
kyō wa tōkyō de nihongo o benkyō shi masu

$ echo '今日は東京で日本語を勉強します' | sabiyomi --mode annotated
今日(きょう)は東京(とうきょう)で日本語(にほんご)を勉強(べんきょう)します
```

Readings come from [lindera](https://github.com/lindera/lindera) with the IPADIC
dictionary embedded in the binary, so there's nothing to download or configure.

## Install

```sh
cargo install sabiyomi   # CLI
cargo add sabiyomi       # library
```

## CLI

```
sabiyomi [--to hiragana|katakana|romaji]      default: hiragana
         [--mode normal|spaced|annotated]     default: normal
         [--system hepburn|kunrei|nippon|passport]         default: hepburn (romaji only)
         [--long-vowels macron|circumflex|spelled|omitted] default: depends on system
         [--delimiters <start><end>]          default: "()" (annotated only)
```

Input is read from stdin and converted line by line.

## Library

```rust
use sabiyomi::{Mode, Options, Sabiyomi, Target};

let s = Sabiyomi::new()?; // loads the dictionary; create once, reuse
let opts = Options { to: Target::Romaji, mode: Mode::Annotated, ..Options::default() };
assert_eq!(s.convert("東京", &opts)?, "東京(tōkyō)");
```

- `sabiyomi::kana` has the dictionary-free helpers: `is_kanji`, `is_kana`, `to_hiragana`,
  `to_katakana`, `to_romaji`, …
- `Sabiyomi::tokenize` exposes the morphemes. `convert_tokens` accepts tokens from any
  other analyzer.

## Romanization

|          | 地図  | お茶を | 新聞    | 本屋   | スーパー |
| -------- | ----- | ------ | ------- | ------ | -------- |
| hepburn  | chizu | ochao  | shimbun | hon'ya | sūpā     |
| kunrei   | tizu  | otyao  | sinbun  | hon'ya | sûpâ     |
| nippon   | tizu  | otyawo | sinbun  | hon'ya | sûpâ     |
| passport | chizu | ochao  | shimbun | honya  | supa     |

### Long vowels

Every system has a usual long-vowel style. `--long-vowels` (`Options::long_vowels`)
overrides it, which is useful when the output has to be plain ASCII:

|            | 食べましょう | 東京    | スーパー |                         |
| ---------- | ------------ | ------- | -------- | ----------------------- |
| macron     | tabemashō    | tōkyō   | sūpā     | hepburn default         |
| circumflex | tabemashô    | tôkyô   | sûpâ     | kunrei, nippon default  |
| spelled    | tabemashou   | toukyou | suupaa   | ASCII, follows the kana |
| omitted    | tabemasho    | tokyo   | supa     | passport default        |

Particles are romanized as pronounced (は → wa, へ → e). Katakana words keep their written
spelling (ヴァイオリン → vaiorin), and Latin text passes through untouched.

## Performance

Measured on an Apple M3 (4 performance + 4 efficiency cores, 16 GB) under macOS 27, with
Rust 1.98 and a `--release` build. The input is *吾輩は猫である* (Natsume Sōseki) from Aozora
Bunko with ruby markup stripped: 2,341 lines, 321k characters, 958 KB. Each number is the
best of 15 runs, taken across three separate benchmark sessions. The machine was also running
other work (load average about 6), so treat these figures as conservative.

**Library, whole novel, one `convert` call per line**

|                                                   | time     | throughput | chars          |
| ------------------------------------------------- | -------- | ---------- | -------------- |
| tokenize only (lindera)                           | 95.7 ms  | 10.0 MB/s  | 3.35 M chars/s |
| hiragana                                          | 118.5 ms | 8.1 MB/s   | 2.71 M chars/s |
| katakana                                          | 116.4 ms | 8.2 MB/s   | 2.76 M chars/s |
| romaji (hepburn)                                  | 139.3 ms | 6.9 MB/s   | 2.31 M chars/s |
| romaji, spelled long vowels                       | 139.1 ms | 6.9 MB/s   | 2.31 M chars/s |
| hiragana, spaced                                  | 118.6 ms | 8.1 MB/s   | 2.71 M chars/s |
| romaji, spaced                                    | 139.2 ms | 6.9 MB/s   | 2.31 M chars/s |
| hiragana, annotated                               | 131.7 ms | 7.3 MB/s   | 2.44 M chars/s |
| romaji, annotated                                 | 141.4 ms | 6.8 MB/s   | 2.27 M chars/s |
| `kana::to_romaji` on the novel's katakana reading | 12.7 ms  | 93.8 MB/s  | 31.3 M chars/s |
| `kana::to_katakana`                               | 0.8 ms   | 1256 MB/s  | 421 M chars/s  |

Morphological analysis takes 70–80% of the time. Everything sabiyomi adds on top costs
20–45 ms for the whole novel.

**Input size.** The same text was cut into pieces of N characters and each piece converted to
romaji separately.

| piece size                | time     | throughput |
| ------------------------- | -------- | ---------- |
| 16 chars                  | 164.0 ms | 5.8 MB/s   |
| 128 chars                 | 140.4 ms | 6.8 MB/s   |
| 1,024 chars               | 132.1 ms | 7.2 MB/s   |
| 8,192 chars               | 130.3 ms | 7.3 MB/s   |
| 65,536 chars              | 135.7 ms | 7.0 MB/s   |
| whole novel as one string | 132.4 ms | 7.2 MB/s   |

Cost grows linearly with input length. Only very short strings pay a noticeable overhead per
call: a 16-character sentence takes **6.3 µs**.

**Threads.** `Sabiyomi` is `Sync`, so one instance can be shared by any number of threads.

| threads | time     | throughput | speed-up |
| ------- | -------- | ---------- | -------- |
| 1       | 137.2 ms | 7.0 MB/s   | 1.00×    |
| 2       | 84.9 ms  | 11.3 MB/s  | 1.62×    |
| 4       | 40.7 ms  | 23.6 MB/s  | 3.37×    |
| 8       | 31.4 ms  | 30.5 MB/s  | 4.37×    |

Speed-up flattens past 4 threads because the other 4 are efficiency cores.

**CLI and resources**

|                                       |                                                                        |
| ------------------------------------- | ---------------------------------------------------------------------- |
| startup + one line                    | 2.6 ms (median 3.0 ms over 50 runs)                                    |
| `Sabiyomi::new()`                     | ≈1 ms; the dictionary is embedded, so it is paged in instead of parsed |
| 9.6 MB (the novel ×10) → hiragana     | 1.35 s                                                                 |
| 9.6 MB → romaji / annotated / spelled | 1.52–1.54 s                                                            |
| peak memory, one line                 | 2.8 MB                                                                 |
| peak memory, 9.6 MB input             | 49 MB (most of the dictionary paged in; output is streamed)            |
| binary size                           | 49 MB, almost all of it IPADIC                                         |

Reproduce:

```sh
curl -sLO https://www.aozora.gr.jp/cards/000148/files/789_ruby_5639.zip && unzip -o 789_ruby_5639.zip
iconv -f SHIFT_JISX0213 -t UTF-8 wagahaiwa_nekodearu.txt \
  | sed -e 's/《[^》]*》//g' -e 's/｜//g' -e 's/［＃[^］]*］//g' | tr -d '\r' \
  | awk 'NR>17' | sed -e '/^底本：/,$d' -e '1,/^-----/d' > neko.txt   # strip header/footer
cargo run --release --example bench -- neko.txt 15
```

## Inspiration

Inspired by [kuroshiro](https://github.com/hexenq/kuroshiro). The romanization tables
started from its data (MIT, see [`src/romaji/LICENSE-kuroshiro`](src/romaji/LICENSE-kuroshiro)).

## License

[MIT](LICENSE)
