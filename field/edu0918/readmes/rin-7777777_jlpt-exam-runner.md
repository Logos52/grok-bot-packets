# JLPT 模拟考试 App（考试运行器）

> 一款**纯前端、无后端、无听力**的日语 JLPT 模拟考试运行器。
> 把任意大模型生成的 JSON 试卷导入 App，即可按真实考试时长倒计时答题、自动评分，并查看**中文详尽解析**。
> Capacitor 8 + 原生 HTML/CSS/JS，可打包成 Android APK，所有数据只存在本机。

**简体中文** | [English](README.en.md) | [日本語](README.ja.md)

---

## 这是什么

App 本身**不出题、不内置 AI**，只做一件事：把一份符合约定格式的 JSON 试卷，变成一次完整的模拟考试体验。

```
AI 生成 JSON 试卷  →  导入 App  →  选模式（模拟考试 / 练习）  →  答题  →  交卷  →  按 JLPT 规则判合格 + 逐题中文解析
```

三个设计原则：

| 原则 | 说明 |
| --- | --- |
| **考试运行器，不是题库** | 题库由你在任意大模型里生成（App 内置提示词模板），备考范围、题量、难度完全自定义 |
| **一切由 meta 驱动** | 级别、时长、各部分满分、总分、合格线、各部分最低分全部写在试卷 JSON 里，App 不硬编码；缺省才回落到 N3 参考值 |
| **离线可用** | 试卷、答题进度、历史成绩全部存 `localStorage`，不联网、不上传、不需要账号 |

## 功能

| 模块 | 实现 |
| --- | --- |
| 导入试卷 | 文件选择器（`.json`）+ 粘贴 JSON；导入时**校验并自动修正**，逐条列出问题（尾逗号、全角标点、答案写成选项原文/数字、缺 `points` 等都能自动处理） |
| 级别 | N5 / N4 / N3 / N2 / N1，由 `meta.level` 指定，缺省 **N3** |
| 模拟考试 | 按 `meta.durationMinutes` 倒计时（剩 10 分钟变黄、5 分钟变红闪烁），**时间到自动交卷**，也可手动交卷；交卷前看不到任何答案 |
| 练习模式 | 不限时、只记用时；**每题作答后可随时查看该题参考答案与中文解析**，可勾选「作答后自动展开」 |
| 评分 | 分部得分按答对比例换算到该分部满分；总分 = 各分部之和；**合格 = 总分 ≥ passScore 且每个分部 ≥ 该分部 minScore**；同时给出正确率、答对/答错/未作答、各部分达标情况 |
| 成绩与解析 | 逐题回顾：题干、你的选择、正确答案、中文详解；支持「全部 / 错题 / 答对 / 标记 / 未作答」筛选；可一键复制纯文本成绩单 |
| 题型 | 第一版只做单选题；**排序题（★）转成「选择正确顺序」四选一** |
| 读解 | 文章写在 `passages`，题目用 `passageId` 关联；答题时可折叠/展开原文 |
| 无听力 | Schema 与提示词都明确排除听力部分 |
| 断点续答 | 中途退出/被杀进程后可「继续答题」，模拟考试剩余时间继续走 |
| 答题卡 | 抽屉式题号网格，按分部排列，显示已答/标记状态，可跳题 |
| 手机适配 | 移动端优先布局、安全区适配、≥44px 触控区、深/浅双主题、安卓返回键防误退 |

## 快速开始

### 方式一：直接装 APK（推荐）

仓库根目录已附带构建好的安装包：**`JLPT模拟考试-debug.apk`**（4.0 MB，Android 7.0+）。
也可以直接到 **[Releases](https://github.com/rin-7777777/jlpt-exam-runner/releases/latest)** 下载最新版（`jlpt-mock-exam-v1.0.0-debug.apk`，发布说明里附有 SHA-256 校验值）。
下载后传到手机点开安装即可（需允许「安装未知来源应用」）；手机连 USB 时也可以：

```bash
adb install -r JLPT模拟考试-debug.apk
```

### 方式二：电脑上先跑网页版

```bash
npm install
npm run dev          # http://localhost:5173
```

打开后点「导入试卷 → 载入示例试卷 → 保存并选择模式」，30 秒就能体验完整流程；也可以用手机浏览器访问同一 Wi-Fi 下的地址。

### 方式三：自己打包 APK

```bash
npm install
npx cap add android        # 首次：生成原生工程（本仓库未提交 android/，见下方说明）
npm run android:sync       # 把 www/ 同步进原生工程
cd android && ./gradlew assembleDebug
# 产物：android/app/build/outputs/apk/debug/app-debug.apk
```

需要 **JDK 21 + Android SDK（platform 36 / build-tools 36.0.0）**。
完整步骤、Release 签名、常见报错处理见 **[docs/BUILD_APK.md](docs/BUILD_APK.md)**。

> ⚠️ 如果项目路径包含中文（非 ASCII），AGP 会拒绝构建，需要在 `android/gradle.properties` 里加一行：
> `android.overridePathCheck=true`（官方开关）。

## 怎么用

1. **生成试卷**：打开 App →「提示词模板」→ 选级别/题量/额外要求 → 点「复制」；
2. **喂给 AI**：粘贴给任意大模型（DeepSeek / GPT / Claude / Gemini / 通义千问 / Kimi…），得到一份纯 JSON；
3. **导入**：App →「导入试卷」→ 选文件或粘贴 JSON →「校验并预览」，有问题会告诉你哪里错、怎么改；
4. **开考**：选「模拟考试」或「练习模式」，开始答题；
5. **看成绩**：交卷后看到合格判定、各部分达标情况、正确率，以及逐题中文解析。

完整提示词见 **[docs/PROMPT_TEMPLATE.md](docs/PROMPT_TEMPLATE.md)**（App 内同名页面内容完全一致）。

## 试卷 JSON 格式（速览）

```json
{
  "meta": {
    "title": "JLPT N3 模拟考试 第 1 回",
    "level": "N3",
    "durationMinutes": 110,
    "totalScore": 120,
    "passScore": 63,
    "sections": [
      { "id": "language_knowledge", "name": "文字・词汇・文法", "score": 60, "minScore": 19 },
      { "id": "reading", "name": "读解", "score": 60, "minScore": 19 }
    ]
  },
  "passages": [{ "id": "p1", "title": "コンビニの朝", "text": "读解文章正文……" }],
  "questions": [
    {
      "id": "q1",
      "sectionId": "language_knowledge",
      "type": "single_choice",
      "passageId": null,
      "stem": "＿＿の言葉の読み方として最もよいものを選びなさい。\n彼はいつも【丁寧】に説明してくれる。",
      "options": [
        { "key": "A", "text": "ていねい" },
        { "key": "B", "text": "ていねん" },
        { "key": "C", "text": "ちょうねい" },
        { "key": "D", "text": "でいねい" }
      ],
      "answerKey": "A",
      "explanation": "正确答案：A ていねい。\n「丁寧」意为礼貌、细心……（中文详尽解析）",
      "points": 1
    }
  ]
}
```

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `meta.title` / `meta.level` | 是 | 标题 / 级别（N5–N1） |
| `meta.durationMinutes` | 是 | 模拟考试时长（分钟），如 N3 = 110 |
| `meta.totalScore` / `meta.passScore` | 是 | 总分 / 总分合格线 |
| `meta.sections[].id` / `.name` | 是 | 分部 id / 中文名（不含听力） |
| `meta.sections[].score` | 是 | 该分部**满分**（JLPT 固定值，与题数无关） |
| `meta.sections[].minScore` | 是 | 该分部**最低合格分**，低于它总分再高也判不合格 |
| `passages[].id` / `.text` | 读解必填 | 文章 id / 正文 |
| `questions[].sectionId` | 是 | 必须等于某个 `meta.sections[].id` |
| `questions[].stem` / `.options` / `.answerKey` | 是 | 题干 / 2–6 个选项 / 正确答案（必须是某个 option 的 key） |
| `questions[].explanation` | 是 | 中文详尽解析 |
| `questions[].passageId` | 读解必填 | 关联 `passages[].id`，其他题填 `null` |
| `questions[].points` | 否 | 该题权重，默认 1 |

字段全表、容错规则、常见报错修复见 **[docs/SCHEMA.md](docs/SCHEMA.md)**；机器可读版本见 [`samples/paper.schema.json`](samples/paper.schema.json)（JSON Schema draft 2020-12）；可直接导入的示例卷见 [`samples/n3-sample.json`](samples/n3-sample.json)。

## 评分规则（与 JLPT 官方口径一致）

```
分部原始分 raw    = 该部分答对题目的 points 之和
分部理论满分 maxRaw = 该部分全部题目的 points 之和
分部换算得分       = round(raw ÷ maxRaw × sections[].score)   ← 各分部满分固定、题数可变，所以要按比例换算
总分              = 各分部换算得分之和
合格              = 总分 ≥ passScore  且  每个分部得分 ≥ 该分部 minScore
正确率            = 答对题数 ÷ 总题数（未作答按答错计）
```

⚠️ 最容易被忽略的一条：**总分够了、但某个分部低于它的 `minScore`，依然判不合格**。
App 会在成绩页把原因写清楚，例如「读解得分 15 分，低于该部分最低分 19 分（差 4 分），按 JLPT 规则判为不合格」。

## 项目结构

```
jlpt-exam-runner/
├── www/                      ← 唯一需要维护的前端源码（纯原生，无框架无打包器）
│   ├── index.html            6 个页面：首页 / 导入 / 提示词 / 模式 / 考试 / 成绩
│   ├── css/style.css         移动端优先，深色 + 浅色双主题
│   └── js/
│       ├── util.js           DOM / 时间 / 剪贴板 / 节流等工具
│       ├── schema.js         试卷 JSON 校验 + 规范化（宽容导入、明确报错）
│       ├── score.js          评分与合格判定（分部换算 + minScore 规则）
│       ├── store.js          localStorage：试卷库 / 进度 / 成绩 / 设置
│       ├── prompt.js         给 AI 的提示词模板（完整版 + 精简版）
│       ├── demo-paper.js     内置示例试卷（N3，11 题，含读解）
│       └── app.js            应用主逻辑（路由、考试运行器、结果页）
├── docs/
│   ├── SCHEMA.md             试卷 JSON 详解（字段表、评分公式、容错规则、排错）
│   ├── PROMPT_TEMPLATE.md    可直接复制的 AI 提示词（由 prompt.js 自动生成）
│   └── BUILD_APK.md          打包 APK 完整说明（环境、命令、签名、排查）
├── samples/
│   ├── n3-sample.json        示例试卷（可直接导入）
│   └── paper.schema.json     正式 JSON Schema
├── tools/
│   ├── serve.js              零依赖静态服务器（浏览器预览）
│   ├── selftest.js           核心逻辑单元测试（87 项）
│   ├── domtest.js            jsdom 端到端流程测试（107 项）
│   ├── export-sample.js      导出 samples/n3-sample.json
│   └── gen-prompt-doc.js     导出 docs/PROMPT_TEMPLATE.md
├── capacitor.config.json     appId=com.jlptmock.exam / appName=JLPT模拟考试 / webDir=www
└── package.json
```

> `android/` 目录由 `npx cap add android` 生成，属于可再生的原生工程，**没有提交到本仓库**（`.gitignore` 已忽略）。
> 克隆后执行 `npm install && npx cap add android && npm run android:sync` 即可得到同样的工程。

## 技术栈

- **Capacitor 8**（`@capacitor/cli` / `core` / `android`）
- **原生 HTML / CSS / JavaScript**：无框架、无打包器、零运行时依赖，`www/` 直接就是能跑的网页
- **localStorage** 本地存储；**不依赖任何 Capacitor 插件**（复制用 Clipboard API + `execCommand` 降级，导入用 `<input type="file">` + 粘贴）
- 生成的原生工程：`minSdk 24`（Android 7.0）、`compileSdk 36`、`targetSdk 36`、AGP 8.13.0、Gradle 8.14.3

## 测试与验证

```bash
npm test            # 单元测试 + 端到端 UI 测试
npm run test:unit   # schema.js / score.js / store.js / prompt.js（87 项）
npm run test:dom    # jsdom 跑完整流程：导入→答题→看解析→交卷→成绩→重答（107 项）
npm run sample      # 重新生成 samples/n3-sample.json
npm run docs        # 重新生成 docs/PROMPT_TEMPLATE.md
```

当前状态（全部实测通过）：

| 项目 | 结果 |
| --- | --- |
| 单元测试 | ✅ 87 项通过 |
| jsdom 端到端流程测试 | ✅ 107 项通过 |
| 真机尺寸真实浏览器渲染 | ✅ Chromium 手机视口跑完全流程，0 个控制台错误 |
| 布局 / 可访问性审计 | ✅ 360×800 与 320×568、深浅主题、6 个页面：无横向溢出、无 <32px 触控区、无 <12px 字号、文字对比度全部 ≥ 4.5:1 |
| Android 打包 | ✅ `./gradlew assembleDebug` 构建成功，APK 内嵌前端资源与 `www/` 源码 md5 完全一致 |

覆盖的关键用例：级别默认值兜底、答案别名识别（数字 / 选项原文 / 带标点）、分部换算四舍五入、**「总分达标但分部未达标」判定**、未作答计错、非法 JSON 的中文提示、进度保存与恢复、答题卡、解析筛选、主题持久化。

## 界面与可访问性

- **移动端优先**：`#app` 固定全屏、内容区独立滚动；顶/底栏适配 `env(safe-area-inset-*)` 安全区；320px 窄屏下底栏按钮不折行、不遮挡正文。
- **深/浅双主题**：颜色全部走 CSS 变量。`--primary / --ok / --bad / --warn` 用于描边、进度条等大面积色块；`--primary-text / --ok-text / --bad-text / --warn-text` 专供小字号文字与徽章，保证对比度达标。
- **无障碍**：所有正文 ≥ 12px，触控目标 ≥ 32px（主要按钮 44px+），文字与背景对比度 ≥ 4.5:1（WCAG AA）。

## 常见问题

**Q：AI 输出的 JSON 里带了 ```json 代码块 / 前后有说明文字？**
App 会自动剥离代码块围栏并忽略多余文字。但如果 JSON 内部混入了中文全角标点、尾逗号或注释，仍会解析失败——重新让 AI「只输出 JSON、使用英文半角标点、不要注释」即可，导入页会直接告诉你问题出在哪。

**Q：一次生成题量太大，模型输出被截断？**
分批生成：先出「文字・词汇・文法」，再出「读解」，然后把两次的 `questions` 数组合并、`passages` 合并（注意 `id` 不要重复）。

**Q：判合格的口径想和真题完全一致？**
在提示词里明确写出 `totalScore`、`passScore` 和每个 `sections[].minScore`，App 会严格按「总分达标 **且** 每个分部达标」判定。

**Q：排序题（★）怎么办？**
第一版只支持单选题，提示词已要求 AI 把排序题改写成「选择正确顺序」四选一（题干给 ①②③④，选项是四种语序）。

**Q：中途接电话 / App 被系统杀掉，答案会丢吗？**
不会。答题进度实时存在本机，首页会出现「继续答题」入口；模拟考试的剩余时间也会继续计算。

**Q：能装到 iPhone 上吗？**
当前只打包了 Android。代码是纯前端网页，`npx cap add ios` 后同样可以出 iOS 版（需要 macOS + Xcode）。

## 已知限制

- 只支持单选题（排序题需让 AI 转成四选一）；
- 不含听力题（Schema、提示词、内置示例都明确排除）；
- 试卷与成绩存在浏览器 `localStorage` 里，清除 App 数据会一并清空（建议 IMPORTANT 试卷同时保留 JSON 原文件）；
- 安卓 WebView 无法阻止系统自动锁屏，长时间答题建议调大系统「自动锁屏」时间（进度会自动保存，不怕锁屏）。

## 后续可扩展

- 题型：多选、填空、拖拽排序、连线，以及真正的听力播放（接入 Capacitor 音频插件 + 音频文件随试卷打包）；
- 学习闭环：错题本、按知识点统计、历史成绩趋势图、艾宾浩斯复习提醒；
- 试卷管理：批量导入、按级别/标签分类、从 URL 直接导入、导出当前试卷；
- 体验：防息屏（keep-awake 插件）、分享成绩单（share 插件）、字体大小调节、答题音效；
- 平台：iOS 打包、PWA 离线安装；
- **理论上稍稍修改便可适配其他类型的试卷，后续计划优化。**（例如 JLPT 之外的日语考试、英语单词测验、教资/法考类客观题、公司内部认证考试等——只需按自己的分值口径生成对应的 `meta` 与题目 JSON，App 的答题、评分、解析流程可以原样复用。）

## 许可

[MIT](https://opensource.org/licenses/MIT)

## 致谢

试卷由使用者自行用大模型生成；本项目只提供格式规范、提示词模板与考试运行器，不附带任何受版权保护的真题。
