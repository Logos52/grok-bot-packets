# Hanzi Sort

宣纸、水墨、竹简与红印章风格的 HTML5 汉字排序游戏。React + TypeScript + Vite + CSS，纯前端，无账号、后端、数据库或广告 SDK。

## 启动

在项目目录 `D:\new_game` 打开终端：

```powershell
npm install
npm run dev
```

打开终端显示的本地网址，默认 http://localhost:5173。开发服务绑定 `0.0.0.0`，同一局域网的手机可用电脑的局域网 IP 与相同端口访问（取决于系统防火墙配置）。

生产构建与本地预览：

```powershell
npm run build
npm run preview
```

`dist/` 是完整静态站点，可部署至静态托管或嵌入游戏平台；使用相对资源路径，支持子目录。开发环境使用 Node.js 24.13.0 / npm 11.12.1；Node 版本要求见 [Vite 官方文档](https://vite.dev/guide/)。请通过 HTTP 服务运行，不要直接双击源码 HTML。

## 已实现

- 20 个固定、独立验证可解的关卡；难度分段为 3 / 4 / 5 / 6 / 7 种汉字，各关初始有两个空槽。
- 全部十个汉字、指定拼音与英文含义；界面为英文。
- 顶部连续同字自动整组移动，容量四片，目标空间不足时部分移动。
- 抬起、280ms 实际飞行、非法移动晃动、完成槽回弹与印章、短暂学习提示。
- Undo 最多保留 100 步；Restart；高亮合法移动的 Hint。
- 胜利弹窗、Next Level；第 20 关完成后可 Play Again。
- localStorage 保存关卡、最高解锁关卡、棋盘、步数、撤销历史、首次进入状态及声音/震动设置。
- Web Audio 合成五种音效，首次用户操作后初始化；可关闭声音和震动。
- 原生模态对话框、键盘操作、焦点回归与减少动态效果偏好支持。
- CSS 竹纹与宣纸纹理、原创 SVG 山景与图标，没有远程图片、字体或音频请求。

## 核心规则

`Board` 是二维汉字数组，**每个槽从数组首项到底部、末项到顶部**。例如 `['山', '水', '水']` 表示顶部连续两片水。

`getMove(board, from, to)` 校验来源、目标、顶字和容量，并计算 `min(顶部连续同字数量, 目标剩余容量)`。`applyMove` 返回新棋盘，不修改输入。`isWon` 要求每个非空槽同时满足「恰好四片」和「全部同字」。空棋盘不算胜利。

`useGame` 管理选中状态、历史、关卡和存档；`GameBoard` 只负责显示与动画。飞行期间锁定交互，完成后提交一次原子移动，避免动画和棋盘状态不同步。

Hint 是当前合法操作提示，优先合并已有同字组；它不保证是最优解，也不保证当前任意局面仍有解。没有合法操作时提示 Undo / Restart。

## 关卡可解性

首版采用需求中允许的「已验证固定关卡」。开发脚本使用固定种子构造候选局面，经过带对称剪枝的 DFS 求解，再将棋盘与完整解题路径一起保存到 `levelData.json`。**未经求解验证的随机棋盘不会写入文件。** 每次测试都会按实际最大整组移动规则回放全部 20 条解题路径并检查胜利。运行时没有求解开销。

需要替换关卡时运行：

```powershell
npm run levels:generate
npm test
```

这会覆盖关卡数据；发布后如改变关卡内容，应同时更新存档版本/键，避免旧棋盘与新关卡配置不一致。

## 文件清单

| 文件 / 目录 | 用途 |
| --- | --- |
| `package.json`、`package-lock.json` | 依赖与运行/构建/验证命令 |
| `index.html`、`vite.config.ts`、`tsconfig.json` | 入口、相对资源路径、严格 TS 配置 |
| `public/favicon.svg` | 原创汉字印章图标 |
| `src/main.tsx`、`src/App.tsx` | React 入口与界面组合 |
| `src/game/types.ts`、`characters.ts` | 类型、容量、汉字词典 |
| `src/game/gameLogic.ts` | 独立纯函数排序规则与提示 |
| `src/game/levels.ts`、`levelData.json` | 20 关数据与解法证书 |
| `src/game/levelGenerator.ts`、`scripts/generate-levels.ts` | 仅开发阶段使用的关卡生成与验证 |
| `src/hooks/useGame.ts` | 游戏状态、历史、交互锁与进度 |
| `src/components/HomeScreen.tsx`、`GameHeader.tsx` | 首页与关卡信息 |
| `src/components/GameBoard.tsx`、`BambooTube.tsx`、`BambooTile.tsx` | 响应式棋盘、竹简与飞行动画 |
| `src/components/Modal.tsx`、`CompleteModal.tsx`、`SettingsModal.tsx` | 原生对话框、胜利、设置 |
| `src/components/Icon.tsx`、`Landscape.tsx` | SVG 图标与山景 |
| `src/services/storage.ts` | 存档校验与异常降级 |
| `src/services/audio.ts` | 合成音效与可选震动 |
| `src/services/ads.ts` | `onGameReady`、`showInterstitialAd`、`showRewardedAd` 占位接口 |
| `src/styles/index.css` | 完整视觉样式、手机适配与动画 |
| `tests/game.test.ts` | 规则、20 关解法、数据与存档测试 |
| `tests/game.spec.ts`、`playwright.config.ts` | Chromium 实际操作与视口验证 |
| `artifacts/*.png` | 自动测试截取并检查的界面截图 |
| `docs/superpowers/` | 设计与实施记录 |

## 验证

```powershell
npm test
npx playwright install chromium
npm run test:e2e
npm run build
```

- 28 项核心测试：包括 20 关逐步合法解法回放、容量限制、连续组、不可变性、胜利条件、词典覆盖与损坏存档恢复。
- 11 项 Chromium 浏览器测试：真实点击通关前 3 关和第 20 关；撤销、重开、Hint、非法移动、移动动画及交互锁、设置、刷新存档、广告占位节奏与存储禁用降级；另有移动浏览器触摸模拟。
- 检查 375×667、390×844、430×932、1280×900 下所有槽数布局，无横向溢出；保存首页、游戏、胜利及第 20 关截图。
- 前 3 关通关过程中没有捕获到页面异常或控制台 error。

测试使用 Windows 上的 Chromium 和触摸模拟，没有宣称测试过实体手机或 Safari。小屏较高关卡保留三列可读竹简，允许页面纵向滚动。中文优先使用设备楷体，再回退至中文衬线和系统字体；无中文字体的极简系统需安装 CJK 字体。

## 广告与存档边界

三个广告接口当前只执行 `console.log`，没有真实广告或网络 SDK。首次完成第 3、6、9、12、15、18 关调用插屏占位；刷新已完成关卡不会重复触发。Rewarded 接口保留，未加入额外空槽或奖励玩法。

进度仅存于当前浏览器、当前站点。清除站点数据或换设备不会保留进度；存储不可用时仍可玩，并显示无法持久保存的提示。声音和震动依赖浏览器支持，失败时不阻碍游戏。
