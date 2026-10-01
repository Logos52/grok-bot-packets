# 汉字笔顺动画视频 · Hanzi Stroke Video

[中文](#中文说明) · [English](#english)

一个 Codex skill：输入一个汉字，输出**固定版式**的书写笔顺动画视频。

A Codex skill that turns a single Chinese character into a **fixed-layout** handwriting stroke-order animation video.

![「好」的书写笔顺动画](examples/hao-stroke-order.gif)

---

## 中文说明

### 效果

给一个字，拿到一条可以直接发布的写字动画：

- 1080×1440（3:4 竖版）、30fps、无声 H.264 MP4
- 附封面 JPG 和关键抽帧 PNG
- 暖纸底 + 米字格 + 浅色底稿，墨迹逐笔写上去盖住底稿
- 正在写的一笔朱砂高亮并同步长出来，写完转墨黑，未开始的浅灰
- 页眉自动填拼音、释义、笔画数、部首、繁体；页脚标数据出处与核对日期
- 笔顺表格数自动等于笔画数；笔画多时表格折行、米字格等比缩小
- 时序自适应：笔画少的字写得慢一些，末段留约 1 秒停留，封面取自停留段

**版式是成品的一部分，换字只换数据**，不需要每次重新设计。

### 案例：好

下面全部由本 skill 生成，只换字、不换版式。「好」共 6 笔，部首女，康熙 38 部。

| 封面 | 书写中段 |
| --- | --- |
| ![好 封面](examples/hao-cover.jpg) | ![好 书写中段](examples/hao-writing.jpg) |

中段那一帧能看清全部状态：正在写的第 3 笔用朱砂高亮、笔尖带圆点跟随，第 1、2 笔已写完转墨黑，第 4~6 笔还是浅灰，右侧「子」是浅色底稿，会被墨迹逐笔盖住。

原始视频（147 帧 / 4.9 秒 / 1080×1440）：[examples/hao-motion.mp4](examples/hao-motion.mp4)

### 安装

方式一，skills CLI：

```bash
npx --yes skills@latest add 0xhillen/hanzi-stroke-video --skill hanzi-stroke-video
```

方式二，skill-installer：

```bash
python skill-installer/scripts/install-skill-from-github.py --repo 0xhillen/hanzi-stroke-video --path hanzi-stroke-video
```

方式三，手动：把 `hanzi-stroke-video/` 整个目录复制到 `~/.codex/skills/`，最终结构为 `~/.codex/skills/hanzi-stroke-video/SKILL.md`。

装好后在下一轮对话生效。

### 环境要求

- Node.js 18+
- Python 3.9+
- 渲染机需安装中文字体（Windows 的 Microsoft YaHei、macOS 的 PingFang SC 均可），否则中文会显示成方框
- 首次运行需联网获取字形与 Unihan 数据

### 用法

```bash
python "<SKILL_DIR>/scripts/make_hanzi_video.py" --char 强 --out "<WORK_DIR>/qiang"
```

在 Codex 里直接说「把『强』做成笔顺视频」就会触发，不用手敲命令。

| 参数 | 作用 |
| --- | --- |
| `--char 强` | 要制作的汉字，单字，必填 |
| `--out DIR` | 输出目录，必填 |
| `--gloss "强大；强壮；有力"` | 中文释义，放在标题行中间；提供后读音自动移到页脚 |
| `--note "左右结构 · 弓 + 虽"` | 页脚注记（结构、部件等） |
| `--pace 2` | 书写慢放倍数，默认 1.0；只改时长不改版式 |
| `--as-of 2026-10-01` | 核对日期，默认取当天 |
| `--skip-render` | 只出工程与 `data.json`，不跑 npm |
| `--offline` | 只用缓存，不联网 |
| `--cache-dir PATH` | 指定缓存目录 |

脚本一条命令走完：复制模板工程 → 生成 `data.json` → 校验数据 → `npm ci`（首次）→ 渲染，最后打印视频与封面路径。

### 数据从哪来

全部自动取得，原始记录同时写进 `data.json` 的 `sources`：

- **字形轮廓 + 书写中线**：hanzi-writer-data（上游 Make Me a Hanzi，Arphic 派生字形，按标准笔顺排列）
- **笔画数 / 部首 / 读音 / 繁体 / 英文释义**：Unihan Database

数据按需下载并缓存到 `~/.cache/hanzi-stroke-video/`，仓库本身不包含这些数据。

### 目录结构

```
hanzi-stroke-video/
├── SKILL.md                      # 给 Codex 读的说明书
├── agents/openai.yaml            # skill 元信息
├── scripts/
│   ├── make_hanzi_video.py       # 一条命令的主入口
│   ├── build_data.py             # 取字形 + Unihan，生成 data.json
│   └── validate_data.py          # 数据自洽性校验
└── assets/project/               # Remotion 模板工程（版式在这里）
    ├── src/index.tsx
    ├── render.mjs
    └── package.json
```

### 许可与署名

本仓库的脚本与模板代码采用 MIT License，见 `LICENSE`。

生成所用数据来自第三方，**再分发或商用前请自行核对条款原文**：

- hanzi-writer-data / Make Me a Hanzi 的 `graphics.txt` 派生自 Arphic PL KaitiM GB / UKai，按 **Arphic Public License** 授权
- Unihan Database 按 **Unicode License** 授权
- Make Me a Hanzi 的 `dictionary.txt` 部分按 **LGPL-3.0-or-later** 授权

这些许可是宽松的（允许再分发、修改与商用），但要求随附许可证文本并保留版权声明。

---

## English

A Codex skill that generates a fixed-layout, publish-ready handwriting animation for a single Chinese character.

The animation above is the character 好 (hǎo, "good") rendered by this skill: 147 frames, 4.9 seconds at 1080×1440.

### What you get

- 1080×1440 (3:4 portrait), 30 fps, silent H.264 MP4
- A cover JPG plus key frames as PNG
- Warm paper background, rice-grid guides, and a faint underlay that the ink covers stroke by stroke
- The stroke currently being drawn is highlighted in vermilion; finished strokes turn black; pending strokes stay light grey
- Header auto-filled with pinyin, gloss, stroke count, radical, and traditional form; footer credits the data sources and verification date
- The stroke table always has exactly as many cells as the character has strokes; for long characters the table wraps and the grid scales down proportionally
- Timing is adaptive: characters with fewer strokes are drawn more slowly, the last segment holds for about one second, and the cover frame is taken from that hold

**The layout is part of the product.** Changing the character only changes data, never the design.

### Example: 好

Everything below was produced by this skill. Only the character changes, never the layout. 好 has 6 strokes; its radical is 女 (Kangxi radical 38).

| Cover | Mid-writing |
| --- | --- |
| ![Cover for 好](examples/hao-cover.jpg) | ![Mid-writing frame for 好](examples/hao-writing.jpg) |

The mid-writing frame shows every state at once: stroke 3 is being drawn and is highlighted in vermilion with the pen-tip dot tracking it, strokes 1 and 2 are finished and black, strokes 4 to 6 are still light grey, and the right-hand component 子 is a faint underlay waiting to be covered by ink.

Source video (147 frames, 4.9 s, 1080×1440): [examples/hao-motion.mp4](examples/hao-motion.mp4)

### Install

Option 1, skills CLI:

```bash
npx --yes skills@latest add 0xhillen/hanzi-stroke-video --skill hanzi-stroke-video
```

Option 2, skill-installer:

```bash
python skill-installer/scripts/install-skill-from-github.py --repo 0xhillen/hanzi-stroke-video --path hanzi-stroke-video
```

Option 3, manual: copy the whole `hanzi-stroke-video/` directory into `~/.codex/skills/`, so that you end up with `~/.codex/skills/hanzi-stroke-video/SKILL.md`.

The skill becomes available on your next turn.

### Requirements

- Node.js 18+
- Python 3.9+
- A CJK font on the rendering machine (Microsoft YaHei on Windows, PingFang SC on macOS). Without one, Chinese text renders as boxes.
- Network access on first run, to fetch glyph and Unihan data

### Usage

```bash
python "<SKILL_DIR>/scripts/make_hanzi_video.py" --char 强 --out "<WORK_DIR>/qiang"
```

In Codex, just ask for it in natural language, for example "make a stroke-order video for 强"; no need to type the command yourself.

| Flag | Purpose |
| --- | --- |
| `--char 强` | The character to animate. Single character, required. |
| `--out DIR` | Output directory, required. |
| `--gloss "powerful; strong"` | Gloss shown in the middle of the title row; when supplied, the reading moves to the footer |
| `--note "left-right · 弓 + 虽"` | Footer note, such as structure or components |
| `--pace 2` | Slow-motion multiplier for the writing, default 1.0; changes duration only, never the layout |
| `--as-of 2026-10-01` | Verification date, defaults to today |
| `--skip-render` | Produce the project and `data.json` only, skip npm |
| `--offline` | Use the cache only, no network |
| `--cache-dir PATH` | Custom cache directory |

One command runs the whole pipeline: copy the template project, build `data.json`, validate the data, run `npm ci` (first time only), render, then print the video and cover paths.

### Data sources

Everything is fetched automatically and the raw records are written into `sources` inside `data.json`:

- **Glyph outlines and writing medians**: hanzi-writer-data (upstream: Make Me a Hanzi; Arphic-derived glyphs ordered by standard stroke order)
- **Stroke count, radical, readings, traditional form, definition**: Unihan Database

Data is downloaded on demand and cached under `~/.cache/hanzi-stroke-video/`. This repository does not bundle it.

### Layout

```
hanzi-stroke-video/
├── SKILL.md                      # instructions for Codex
├── agents/openai.yaml            # skill metadata
├── scripts/
│   ├── make_hanzi_video.py       # single-command entry point
│   ├── build_data.py             # fetches glyph + Unihan data into data.json
│   └── validate_data.py          # data self-consistency checks
└── assets/project/               # Remotion template project (the layout lives here)
    ├── src/index.tsx
    ├── render.mjs
    └── package.json
```

### License and attribution

The scripts and template code in this repository are released under the MIT License; see `LICENSE`.

The generated output relies on third-party data. **Check the original terms before redistributing or using the videos commercially:**

- `graphics.txt` from hanzi-writer-data / Make Me a Hanzi is derived from Arphic PL KaitiM GB / UKai and licensed under the **Arphic Public License**
- The Unihan Database is licensed under the **Unicode License**
- The `dictionary.txt` portion of Make Me a Hanzi is licensed under **LGPL-3.0-or-later**

These licenses are permissive, allowing redistribution, modification, and commercial use, but they require that the license text and copyright notices be included.
