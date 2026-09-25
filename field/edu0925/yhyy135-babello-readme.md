<p align="center">
  <img src="brand/babello-icon.png" alt="Babello" width="128" height="128">
</p>

<h1 align="center">Babello</h1>

<p align="center">
  完全运行在浏览器里的语言学习平台，一次一种练习：听力、写作，阅读在路上。
</p>

<p align="center">
  简体中文 | <a href="README.en.md">English</a>
</p>

导入一集播客，用你自己的 LLM Key 转录，然后像看歌词一样学习：当前行随播放滚动并逐词高亮，母语译文贴在每行下方，日语自带假名注音和词性着色。没有服务器、没有账号，所有数据都留在你的浏览器里。

## 功能

- **听力**：粘贴播客 RSS，选一集，转录成歌词式字幕，随播放滚动、逐词高亮。
- **边听边译**：只翻译你正在听的那一段，译文显示在每行下方，听了几分钟就只翻译几分钟。
- **日语注音**：假名注音（furigana）与词性着色由本地分词器完成，不需要任何 Key。
- **写作**：写一句目标语言，返回它读起来是什么意思、哪里不对、母语者会怎么说。
- **自带模型**：OpenAI、Gemini、Groq、SiliconFlow、DeepSeek、OpenRouter，以及任何 OpenAI 兼容服务。
- **数据不出浏览器**：Key、书架、转录稿和音频都存在 IndexedDB，多人可共用一个部署、各付各的账单。
- **8 种界面语言**：简体中文、繁體中文、English、日本語、한국어、Español、Français、Deutsch。
- **可装到主屏幕**：PWA，已导入的内容离线也能打开。

## 部署

Babello 由两个互相独立的部分组成，都跑在 Cloudflare 上，免费额度足够个人使用：

| 部分     | 是什么                                                                                                                                                        | 目录       |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **页面** | 纯静态站点，不含任何配置                                                                                                                                      | 仓库根目录 |
| **代理** | 一个不到两百行的 Worker，只转发字节、不存任何东西。浏览器自己做不到这三件事：跟随播客主机的重定向、访问不带 CORS 头的主机、把大文件的一个字节区间交给转录服务 | `worker/`  |

### 一键部署（无需安装 wrangler）

需要一个 Cloudflare 账号和一个 GitHub 或 GitLab 账号。按钮会把仓库复制到你的账号下，并在 Cloudflare 上配好自动构建，之后每次推送都会自动重新部署。

**1. 部署代理**

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/yhyy135/babello/tree/main/worker)

部署时会让你填 `PROXY_KEY`：这是你发给使用者的共享密钥，自己编一个足够长的随机串即可（例如 `openssl rand -hex 16`）。**不要留空**，留空等于任何人都能用你的代理。

部署完成后记下代理地址，形如 `https://babello-proxy.<你的子域>.workers.dev`。

**2. 部署页面**

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/yhyy135/babello)

页面不需要填任何东西。完成后得到 `https://babello.<你的子域>.workers.dev`。

**3. 连起来**

打开页面，进入 **设置**，填入代理地址和 `PROXY_KEY`，再填模型，见[配置](#配置)。

### 命令行部署

```bash
git clone https://github.com/yhyy135/babello.git
cd babello
npm ci                              # 需要 Node 22.18 或更新版本
npx wrangler login

# 页面
npm run build
npx wrangler deploy

# 代理
cd worker
npx wrangler secret put PROXY_KEY   # 不要写进 wrangler.toml，那个文件会被提交
npx wrangler deploy
```

### 其他静态托管

页面可以放在任何静态主机上：`npm run build` 生成 `dist/web`。唯一的要求是主机**不能**对 `/kuromoji/dict/*` 加 `Content-Encoding: gzip`。那些文件本身就是 gzip 内容，由日语分词器自己解压，被服务器先解一次就会让分词器卡住且没有任何报错。Cloudflare 不会这么做。

## 配置

打开 **设置**，有三处要填。

| 项目         | 端点                              | 用途                         |
| ------------ | --------------------------------- | ---------------------------- |
| **文本模型** | `{base URL}/chat/completions`     | 翻译、询问 AI、写作批改      |
| **转录模型** | `{base URL}/audio/transcriptions` | 语音转文字，必须能返回时间戳 |
| **代理**     | 上面部署的地址 + `PROXY_KEY`      | 下载播客、切分音频           |

设置页里选择服务商会自动填好 base URL。转录已验证过 Groq（`whisper-large-v3-turbo`）；OpenAI、SiliconFlow、Gemini 按其文档实现，尚未用真实节目跑过。**测试连接** 会用真实请求检查两个模型槽，填错在这里就能发现，不用等到导入到一半。

两个模型都是可选的：只填代理也能导入，得到音频和播放器；之后补上转录模型，点 **重试转录** 即可，已经下载的音频不会重复下载。

**母语**决定译文的语言，界面语言也跟着它走。目标语言可以留空自动检测，所以同一个书架里可以同时放日语、西语和英语节目。

## 使用

- **导入**：把播客 RSS 粘贴到书架页的输入框，选一集。导入在页面里运行，需要保持标签页打开；中断后点 **继续** 从断点接着做，不会重新花钱转录。没有想听的节目时，页面底部会按你的目标语言推荐（来自 Apple 播客目录）。
- **写作**：只需要文本模型，不需要代理和音频。回答误读了你的意思时，补一句你想表达的，它会从两者的差距出发重新批改。
- **导出备份**：浏览器在磁盘吃紧时会清理存储，导出文件是转录稿唯一可靠的副本。书架页的 **导出** 会写出一个 JSON，包含转录稿、书架、播放位置和已有的译文；不含音频（可重新下载）和 API Key。导入只会添加，不会覆盖。换设备时，设置页的 **导出设置** 可以把 Key 和模型一并带走。

<details>
<summary>从 Duolistening（2.x）升级</summary>

3.0.0 改名后，浏览器里存放书架的数据库也换了名字，所以旧书架会显示为空（数据没有被删除）。请在**升级前**：

1. 旧版：书架页 **导出**；需要带走 Key 的话，再在设置页 **导出设置**。
2. 升级。
3. **导入** 该文件，并粘贴设置字符串。

2.x 写出的备份文件和设置字符串仍然可以读取。

</details>

## 开发

```bash
npm ci
npm run dev:web     # http://localhost:5173
npm test            # node:test，无测试框架
npm run typecheck
npm run build       # → dist/web
```

转录服务商访问不到 `localhost`，所以导入真实节目需要一个已部署的页面。

[CLAUDE.md](CLAUDE.md) 是代码地图，[CONTEXT.md](CONTEXT.md) 定义了用到的术语，[docs/adr/](docs/adr/) 记录了架构为什么是现在这个样子。

## 已知限制

- 书架属于单个浏览器：手机和电脑是两个书架，只能靠导出文件互通。
- 询问 AI 每次只问一个固定问题，没有对话历史；写作不保存历史，刷新即清空。
- 推荐列表由浏览器直连 Apple，每天一次，Apple 会知道你在学哪种语言；封面图同样来自 Apple 的 CDN，离线时显示为占位。
- iOS 上「添加到主屏幕」能避免存储被 Safari 清理，但独立 Web App 在最小化或锁屏时有丢音频的历史，请先在自己的手机上试一下。
