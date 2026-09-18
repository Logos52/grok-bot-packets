# 欧路词典生词本同步到 Anki

读取本机欧路词典的数据库，把生词本增量同步到 Anki。提供图形界面程序 `EudicAnkiSync.exe`（源码 `eudic_anki_gui.py`）与命令行脚本 `eudic_anki_sync.py`。卡片背面按欧路中的顺序和展开设置，原样展示所选第三方词库（MDX/MDD）的释义，并把词库用到的样式、脚本、字体、图片和音频一并上传到 Anki 媒体库。

## 下载

在 [Releases](https://github.com/ydd0729/eudic-anki-sync/releases/latest) 下载 `EudicAnkiSync.exe`，无需安装，双击运行。

## 准备

1. 安装 [uv](https://docs.astral.sh/uv/)，在项目目录运行 `uv sync`。
2. Anki 已启动并安装 AnkiConnect 插件。
3. 本机安装欧路词典，并已把生词本同步到本机。脚本默认读取 `%APPDATA%\Francochinois\eudic`。

## 图形界面

直接运行 `dist\EudicAnkiSync.exe`，或在项目目录运行 `uv run eudic_anki_gui.py`。

- 欧路生词本与 Anki 牌组从现有列表中选择，“新建牌组”可创建新牌组（子牌组用 `::` 分隔）。
- 词库按欧路中的顺序列出，默认勾选欧路中已启用的第三方词库，并标注缺少资源包的词库。
- “试运行”只预览改动，“开始同步”写入 Anki；开启“反向同步”后，删除欧路生词本中的词之前会弹窗确认。
- 右上角显示 Anki 连接状态，启动 Anki 或切换配置文件后点击“刷新”。
- 连不上 Anki 时，界面顶部会说明原因（Anki 未运行、未安装 AnkiConnect、插件已停用、插件尚未生效）并给出处理步骤；未安装时可一键复制插件代码 2055492159 或打开插件页面。
- 界面尺寸与字号跟随系统的显示缩放。
- 界面跟随系统的浅色与深色模式，上次的选择保存在 `%LOCALAPPDATA%\EudicAnkiSync\gui-settings.json`。

## 命令行

```powershell
# 用默认生词本、默认牌组和欧路中启用的全部第三方词库同步
uv run eudic_anki_sync.py

# 指定生词本、牌组与词库，并把在 Anki 中删除的词从欧路生词本删除（需先退出欧路）
uv run eudic_anki_sync.py --book 我的生词本 --deck "English::Eudic" --dict 牛津 --dict 汉英 --reverse

# 先看将要做什么
uv run eudic_anki_sync.py --dry-run

# 查看可选的词库与生词本
uv run eudic_anki_sync.py --list-dicts
uv run eudic_anki_sync.py --list-books
```

| 参数 | 说明 |
| --- | --- |
| `-b, --book` | 生词本名称或 ID，默认使用欧路默认生词本（ID 0） |
| `-d, --deck` | Anki 牌组，默认 `English::Basics::欧路词典生词本` |
| `-D, --dict` | 包含的第三方词库，可重复，匹配词库文件名片段或 ID；默认使用欧路中启用的全部第三方词库 |
| `-r, --reverse` | 反向同步，把同步过、之后在 Anki 中删除的词从欧路生词本删除 |
| `-y, --yes` | 反向删除时跳过确认 |
| `-n, --dry-run` | 只显示计划，不写入 Anki 或欧路 |
| `--eudic-dir` | 欧路数据目录 |

## 同步规则

- **读取**：欧路运行时也可以读取。脚本复制 `study.db` 与 WAL 文件，在副本中合并后只读查询，不会影响欧路。
- **增量**：每条笔记保存内容摘要，只有新词或内容变化（星级、词库释义、渲染版本）时才写入；媒体文件按摘要跳过已上传的文件。
- **Anki 中删除的词**：状态文件 `%LOCALAPPDATA%\EudicAnkiSync\state.json` 记录已同步的笔记，图形界面与命令行共用；早期放在项目目录的 `.eudic-anki-state.json` 会在首次运行时自动迁移。未开启 `--reverse` 时这些词会被跳过，不会重新加回；开启后从欧路生词本删除。
- **反向删除的写入方式**：必须先退出欧路。脚本先把 `study.db` 及其 WAL 备份到 `%APPDATA%\Francochinois\eudic\eudic-anki-backups\<时间>`（保留最近 10 份），再按欧路自身的方式删除（移除生词本归属，不再属于任何生词本时软删除并标记待上传），下次打开欧路同步时推送到云端。
- **欧路中删除的词**：Anki 中的笔记保持不变。
- **展示**：沿用欧路查词页面的结构，每个词库一个带标题栏的区块，展开状态取欧路的词库“默认展开”设置或“自动展开前 N 个词库”。卡片模板加载欧路安装目录中的 `main.css` 与各词库资源包根目录下的 CSS、JS，这些样式限定在卡片内的容器与各自词库区块中；词库字体缺字时回退到与欧路一致的系统无衬线字体。词条中无法在 Anki 打开的查词链接会被拦截，页内跳转与发音链接可用。
- **样式放在模板而非字段**：Anki 编辑器保存字段时会删除 `<head>`，因此词条自带的样式链接在渲染时去掉，改由模板统一加载。更新样式文件后若 Anki 仍显示旧样式，重启 Anki 以清除网页缓存。
- **笔记类型**：`Eudic Sync`，字段为 Word、Explanation、Stars、Dictionaries、SyncHash。本地数据库不含欧路的简明释义，Explanation 由用户自行填写，同步不会覆盖。

## 限制

- 反向删除直接修改欧路的私有数据库格式，欧路升级后格式可能变化；出现问题时用备份目录中的文件覆盖回 `study.db`。
- `study.db` 未通过 SQLite 完整性检查时不执行反向删除，以免在损坏的 B 树上写入扩大损坏；正向同步不受影响，读取时会绕开损坏的索引。
- 词库缺少的资源（例如词库本身不含的发音文件或 CSS）会在同步结果中列出，卡片中保留原引用。
- `.spx` 音频需要 PATH 中有 `ffmpeg` 才能转换为 mp3。

## 开发与打包

```powershell
# 运行测试
uv run --group dev pytest

# 打包为单文件程序 dist\EudicAnkiSync.exe
uv run --group dev build_exe.py

# 重新生成程序图标 assets\app.png 与 assets\app.ico
uv run --group dev assets/make_icon.py
```

打包后可用 `dist\EudicAnkiSync.exe --smoke-test <输出文件>` 检查程序能否读取欧路与 Anki 数据，结果以 JSON 写入输出文件。

## 发布

推送 `v` 开头的 tag 时，GitHub Actions 在 Windows 上运行测试、打包并验证产物能否启动，然后创建 release 并附上 `EudicAnkiSync.exe`。

```powershell
git tag v0.1.0
git push origin v0.1.0
```

平时推送 `main` 分支或提交 PR 只运行测试。
