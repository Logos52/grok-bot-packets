# Manga Anki：日语漫画词卡项目管理

一部漫画一个项目，保存原始输入、各卷 OCR、选词规则、校订记录和一套当前 Anki 词卡。共享程序封装在可调用的 `$manga-anki` skill 中；新增漫画无需复制旧漫画的脚本或数据。

链路：**本地漫画 → 页面清单 → 文字检测 / manga-ocr → Sudachi 分词 → 词频筛选 → 中文释义和例句校订 → JLPT 参考 → Anki / HTML 预览**。

## 第一个项目

[0001 · 今日はカノジョがいないから](projects/0001-kyou-wa-kanojo-ga-inaikara/README.md)

| 输入登记 | 当前处理范围 | 当前输出 |
|---|---|---|
| 用户提供的第一、二卷 RAR，项目内保留原件 | 第一卷 171 / 171 页；第二卷尚未处理 | 232 张词卡全部配图、188 张审核裁剪 |

- [牌组](<projects/0001-kyou-wa-kanojo-ga-inaikara/output/current/因为女朋友不在第一卷anki 词卡.apkg>)
- [词卡预览](projects/0001-kyou-wa-kanojo-ga-inaikara/output/current/preview.html)
- [项目配置](projects/0001-kyou-wa-kanojo-ga-inaikara/project.json)
- [当前统计与验证](projects/0001-kyou-wa-kanojo-ga-inaikara/output/current/report.json)

迁移完整保留 232 条笔记的字段、排列和 GUID，保留旧版牌组及首轮 9 页 / 30 卡样例。旧工作区的 `data/…`、`output/vol01-full/…` 等路径已随遗留层移入 `factory/archive/compat/`，软链仍然可用。

> 已知不一致：磁盘上的 `.apkg` 被改成了中文名，而 `project.json` 的 `anki.filename` 与构建清单仍记录 `vol01-full-vocabulary.apkg`，因此 `validate` 目前会报 `Output changed or missing`。两种修法见 [归档说明](factory/archive/README.md)。

## 日常操作

在本仓库根目录运行：

```sh
factory/.venv/bin/python factory/scripts/manga_anki.py list
factory/.venv/bin/python factory/scripts/manga_anki.py status --project 0001
factory/.venv/bin/python factory/scripts/manga_anki.py run --project 0001
factory/.venv/bin/python factory/scripts/manga_anki.py validate --project 0001
```

`run` 自动复用有效页缓存；先建立临时输出并校验，成功后才替换 `output/current`，旧输出进入 `output/history`。每次运行记录在项目的 `runs/`，失败和待审核不会覆盖现有牌组。

新漫画：

```sh
factory/.venv/bin/python factory/scripts/manga_anki.py create --title '漫画标题' --slug manga-title
# 使用上一步返回的实际编号，下例假定为 0002。
factory/.venv/bin/python factory/scripts/manga_anki.py import --project 0002 --source '/path/漫画.rar' --volume 1
factory/.venv/bin/python factory/scripts/manga_anki.py run --project 0002
```

运行返回 `needs_review` 时，助手完成 `review/draft.json` 的中文释义校订，再执行：

```sh
factory/.venv/bin/python factory/scripts/manga_anki.py apply-review --project 0002
factory/.venv/bin/python factory/scripts/manga_anki.py run --project 0002 --start export
```

修改角色名、分词规则、读音、例句或区域审核后，用 `--start analyze`。另加一卷时先 `import --volume 2`，再明确 `run --volumes 1,2`；将各卷去重合并为本漫画的一套词卡。

也可直接对 Codex 说：

> 使用 $manga-anki，将这个漫画文件建为新项目，先处理第一卷，生成中文释义词卡。

## 工厂与项目

仓库只有两类内容，边界固定：

```text
factory/                       工厂：可复用程序、环境与归档，不含任何一部漫画的数据
  skills/manga-anki/           skill 的唯一维护源
    SKILL.md                   触发条件与操作原则
    scripts/                   项目管理、导入、OCR、分析、审核、导出、环境准备
    references/                操作流程和项目数据格式
    assets/                    通用选词默认值、依赖锁、模型清单、JLPT 参考与许可证
  scripts/manga_anki.py        统一 CLI 入口
  tests/                       工厂回归测试（合成数据，不碰真实漫画）
  docs/                        技术预研与来源调研
  .venv/ .ocr-venv/ .models/   跨漫画共享的本地运行环境
  .cache/                      pip 缓存（仅 bootstrap --install 时产生）
  archive/                     首批遗留脚本、旧布局兼容软链，冻结不再维护
projects/                      项目：一部漫画的全部数据与产物
  index.json                   项目目录和当前项目
  <id>/                        input / review / work / output / runs / reports
  <id>/tests/                  该漫画自己的产物回归测试

.agents/skills/manga-anki -> ../../factory/skills/manga-anki   技能发现入口，指向工厂
.manga-anki-workspace.json     工作区标记 + runtime 路径（工厂位置的唯一真相）
```

工厂的位置只由 `.manga-anki-workspace.json` 的 `runtime` 决定：`core_python`、`ocr_python`、`models`。skill 脚本不假设自己叫 `factory/`，把环境搬到别处只需改这个文件。项目按 `projects/index.json` 登记，路径落在项目内。

skill 通过 `.agents/skills/manga-anki` 被发现——这是 DSH 的项目级技能根（`<项目根>/.agents/skills`），里面的 `manga-anki` 是指向工厂的软链，所以技能的唯一维护源仍在 `factory/`，没有副本。换机器时保持这个软链（或把 `DSH_BUNDLED_SKILL_DIR` 指向 `factory/skills`）即可。

具体命令见 [skill 工作流](factory/skills/manga-anki/references/workflow.md)，配置和审核格式见 [项目数据约定](factory/skills/manga-anki/references/project-schema.md)。首批遗留脚本已移入 `factory/archive/`，保留可追溯、不参与新项目，说明见 [归档说明](factory/archive/README.md)。

新机器先用 Python 3.12 运行 skill 入口的 `init`，再 `bootstrap --install --models`。当前机器环境与全部模型哈希已验证；普通运行离线。依赖锁来自 macOS arm64，其他平台可能需适配。

## 质量边界

自动检测、OCR、分词、排序和打包已脚本化；中文释义与语境审核由助手完成，未接入通用自动翻译后端。OCR 没有逐字全量对图校订，词频仍可能受识别和切分错误影响。例句文本与图片分别按审核记录导出，缺少已审核例句时保留词条卡。

JLPT 是**非官方参考**：词形和读音同时精确匹配，保留未收录及冲突状态，不能把通用词频视为考试等级。详见 [JLPT 预研](factory/docs/jlpt-difficulty-research.md)。参考数据与版本来源见 [ATTRIBUTION](factory/skills/manga-anki/assets/jlpt-reference/ATTRIBUTION.md)。

## 验证

工厂测试与项目测试分开跑，互不依赖：

```sh
factory/.venv/bin/python -m unittest discover -s factory/tests -v
factory/.venv/bin/python -m unittest discover -s projects/0001-kyou-wa-kanojo-ga-inaikara/tests -v
```

共 21 项：工厂 14 项（跨项目身份隔离、多卷合并、归档路径检查、输入变更、过期审核、失败保留旧输出、重复导出、JLPT 同形异读），项目 0001 有 7 项（整卷页面覆盖、样例身份保持、已知切分错误不入卡、JLPT 标签证据、配图来源、必配图约束、重复导出稳定）。工厂测试用合成项目，项目测试读该漫画自己的输入、审核与产物。

构建检查 Anki SQLite、卡片/字段数量、GUID、媒体及所有选定页面覆盖；`validate` 还校验输出与其构建依据的哈希。

尚未在 Anki 客户端实际导入验证。
