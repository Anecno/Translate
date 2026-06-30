# translate-v2 Skill Spec v0.3.12

> Public original-preserved edition.
>
> This edition removes the historical revision stream, private local paths,
> account identifiers, raw handover evidence, and private incident trails. It
> intentionally preserves the living algorithm, relay aliases, scoring schemas,
> report contracts, Web Relay mapping, and the Antique Game Within Game /
> 《古董局中局》 workflow boundary.
>
> Current public runtime summary:
> - Default runtime channel: ordinary Web Relay unless the task explicitly asks
>   for CLI/API Relay.
> - CLI/API chain: 哈士奇 → 小D → CC → 逗比 → Codex conductor.
> - Web Relay chain: 哈基米 → 老D → 小克 → 包子 → 小G; Codex remains conductor,
>   not a hidden sixth baton.
> - 哈基米 first-baton target-language dictionary rule: when a target-language
>   NotebookLM dictionary exists, check target-language usage there first; source
>   understanding may use ordinary web search only for real source ambiguity; no
>   dictionary/search result may override source text, user constraints, project
>   context, terminology, or author intent.
> - Antique Game Within Game / 《古董局中局》 tasks require a verified
>   pre-translation context package and user audit before formal relay prompt,
>   dispatch, local translation, or final output.

---

## 0. 顶层设计（一句话）

**串行接力链 + 用户 checkpoint**：Codex-led workflow 的当前固定顺序以 `SKILL.md` 为准：CLI/API 为 **哈士奇→小D→CC→逗比→Codex conductor**；默认 Web Relay Mode 为 **哈基米→老D→小克→包子→小G**。上游旧链（Codex 曾为第 3 棒、CC 曾为末棒）只作为历史来源，不得用于新 prompt、dispatch、round archive 或最终报告。首棒 = Google/DeepL 机翻参考底稿 + 首棒审核润色为第一版译文，棒 #2+ 每棒先客观点评前一棒再给出润色版本；每**轮**（5 棒）结束 = 用户 checkpoint，每 2 轮由当前 Codex conductor 出一次发散原因分析；收敛阈值软化为「边际改进趋近 0 + 用户主观满意 + 待调研清单确认」。整文/章节级翻译，禁止段落硬拆。运行通道默认走网页版接力；只有用户明确指定 CLI 端接力 / CLI 版接力链 / 走 CLI 时才走 CLI/API/MCP 主链；通道只替换执行端，不改算法。深度调研节点（Step 4 (b)）三选一 + scholar 兜底：哈基米 Web「深度研究」/ 小G ChatGPT Web「深度研究」/ 包子 Doubao Web「深入研究」（2026-04-30 扩充）；三家以 Deep Research 身份不进普通接力链，普通 Web Relay 中的小G也不得自动开深研。

## 1. 设计原则（铁律，v0.2 同款不动）

1. **信达雅，受约束二次创作** — 以体裁成品感为目标，以语义/信息密度/
   显隐关系/修辞功能/可审计锚点为边界；可以主动重组句法与语气，但切忌
   "节外生枝"
2. **整文/章节翻译** — 段落硬拆失上下文，绝对绝对不行
3. **串行接力 + 每棒审核+润色** — 没有固定 critic/judge 角色，每个成员都有否决权和改稿权
4. **用户 checkpoint** — **接力链收敛后停**（连续 3 名满意触发），不是每棒都停；全员发言贴终端 + 落 .md 归档，等用户确认
5. **大文件嵌套** — A 章接力到用户满意，再开 B 章，依此类推（A→B→C→…→N，**可拆任意多块**），串行不并行

## 2. 五步流程（v0.3 细化版）

### Step 1 — 用户输入

1. 待译文本（必）— 主对话粘贴 或 文件路径
2. 目标语种（必）— 含古白话/文言文/江户以前日语等冷门
3. 上下文（选）
4. 体裁与风格契约（选）— 小说/对白/散文/诗词/学术/法律/技术/新闻/
   仿原文体/自定义；同时声明本次是 `constrained_recreation`、
   `controlled_literal` 还是 `strict_traceable`
5. 用户特殊要求（选）
6. **韵律/音律要求**（v0.3 新增，2026-05-27-c 扩展；韵文必填，非韵文按 `sound_contract` 判断）：
   - **节奏感**: 必保（**韵文第一优先级，必须尽最大可能保留**；中文古诗词保五言/七言断句、平仄停顿；英文/日文等保长短句节奏与音步；跨语种字数/音步不可完全对应时不得为补节奏违反 §3.1 三红线，并在 Step 5 韵律说明列明偏差）
   - **押韵**: 默认"能则押"（用户可改为"必押"或"不押"）
     · "能则押"语义: 在不漂意（不违反 §3.1 三红线 Addition/Omission/Free Rewriting）的前提下尝试押韵；一旦逼迫替换原文字面以凑韵 → 降级回不押韵版
     · "必押": 用户显式声明优先押韵 > 字面精度（罕见场景，需用户主动提）
     · "不押": 用户显式关闭
   - **非韵文可诵性**：小说对白、散文、演讲、标题、评论等可声明句长错落、
     顺口度、电影台词感、轻押韵、头韵/元音呼应、重复/顶针等目标；学术/
     法律/技术可声明保持朴素专业节奏、不追求修辞音效
   - **可唱性**（仅歌词）: 默认关；需对应原曲节拍时由用户显式开启
7. **作者参考样本**（选，2026-05-27-d 新增）— 用户有时会提供自己的
   英文或其他语种译文，作为作者级创作策略、审美手感、节奏、压缩方式、
   口语真实度或电影/小说台词感的参考。该项不是必填；不得每次要求用户
   提供英文参考，也不得因缺失参考样本而阻塞任务。
   - **双样本非主从**：源文和作者参考译文都可同时锁事实边界与审美手感，
     禁止机械理解为"中文管事实、英文管风格"或"英文参考覆盖中文源文"。
   - **路数可不同**：若中文更偏电影/小说台词、英文更偏真实现场口语，
     先记录分歧轴，再按目标语体裁选择策略；可贴近任一路线，也可为
     目标语建立第三路线，但必须保留源文锚点与作者意图。
   - **红线不让渡**：作者参考是高优先级意图证据，不授权 Addition /
     Omission / Mistranslation / Hallucination 或无锚点改变人物关系、
     知识状态、情绪强度、论证强度。
8. **首棒机翻参考底稿**（必，v0.3.10 升级；v0.3.2 起原"用户初版译文"作废）— 用户在启动前提供工业级机翻双版（或单版），作 R1 第 1 棒哈士奇审核+润色的入口底稿。
   - **默认双版**（DeepL 收录目标语种时）: **Google Translate 译版 + DeepL 译版**
   - **回退单版**（DeepL 未收录目标语种时）: 仅 Google Translate 译版（DeepL 36 种 vs Google 249 种，覆盖差异见 v0.3.7 §3.4-bis 注；古汉语 / 古典日语 / 江户以前日语 / 少数民族语种等场景必走单版）
   - **位置**: 主对话粘贴 或 文件路径 `<baseline-input-google>` + `<baseline-input-deepl>`（DeepL 缺席时仅前者）
   - **形式**: 与原文同结构（按句/按段对齐），语种 = 目标语种
   - **设计意图**:
     - (a) 双版机翻并置 = 给哈士奇暴露"两个工业基线分歧点"作为审稿入口；重合点 = 工业共识，分歧点 = 哈士奇主审决策点
     - (b) DeepL/Google 双锚点对齐 §3.4-bis 双锚点相对评级— 输入端双版机翻进接力链后，§3.4-bis 评分阶段的 DeepL/Google baseline 已经预算好
     - (c) 哈士奇审核+润色时把这两版作为"最低及格线"参照，输出第一版译文必须**不输 DeepL × 1.1**
     - (d) 替代 v0.3.2 "用户自写初版"机制 — Step 1 第 9 项档位声明已分清用户熟不熟原文，C 档不熟时用户也写不出高质量初版，工业机翻反而更稳；A 档自写场景用户原文本就是自写，"目标语种初版"职能由用户批注承担即可
   - **DeepL 调用提醒**: 喂 DeepL 翻译任何带上下文文本（小说/诗词/段落）必须传 context 字段（不计费但与翻译质量直接挂钩；project convention: DeepL context is quality-critical）；用户在 DeepL Web/Pro 网页版手抓时记得在 context 段贴入足够前情
9. **外部熵档位声明**（必，v0.3.9 新增；v0.3.10 终态重写为三档等效）— 用户对原文把握度的三档自评，**仅作 SOP 触发器使用**（区别在何时启动调研），**不分前后效力**：
   - **A 自写级**：原文是用户自写，烂熟于心 → 不需深度调研；用户批注是高优先级证据
   - **B 吃透级**：非自写但深度研读过（如《花木兰》"儿"双关 / 读过多遍的经典 / 熟悉作家的特定文本） → 不需深度调研；CC 动手前主动核对一句"这段熟到什么程度"；用户判断是高优先级证据
   - **C 不熟级**：用户不熟原文 → CC 可主动**建议**深度调研，但是否真启动由用户在 (i) 任意 Rx 轮末尾 checkpoint（含奇数轮，v0.3.11 扩面） 或 (ii) **R1 首棒派发给哈士奇之前的"启动前置调研"窗口**决定；启动后调研结论是高优先级证据。v0.3.11 扩面理由见顶部规则段——只放开"何时可以触发"，决定权恒在用户，CC 不获自启自动调研权
   - **三档效力等价铁律**：作者级 = 吃透级 = 调研级三档**同等高优先级证据**，区别仅在"信号来源"不在"权重"；CC 在收敛判断时**不应在三种输入间用权重梯度区分**
   - **缺省时**: CC 主动反问"用户这段原文是自写、吃透、还是不熟？"，不可凭印象推断
   - **镜像反射对治**（升级版）：任何高优先级证据进入接力链都需警惕 AI 收敛覆盖（不只针对调研结论）；R2/R4 发散分析报告固定含「AI 镜像反射风险对治」段——列出本轮用户/调研的关键 catalyst 是什么 + 是否被五位 AI 接力共识自然收敛覆盖；catalyst 被吞掉时 CC 主动召回
10. **运行通道声明**（必，v0.3.12 新增；v0.3.12-codex-rule-20260525 改默认值）— 默认走 Web Relay Mode：
   - **网页版接力**：默认执行通道。按 §3.12 / §4 / §5 的一一映射，把各棒次替换为对应 Web 端；优先速度、人工调度弹性、网页模型能力光谱。
   - **CLI 端接力**：仅当用户明确指定 `CLI 端接力` / `CLI 版接力链` / `走 CLI` 或同义指令时启用。走 Codex workflow 当前链 `ask_husky` / `ask_xiaod` / `ask_cc` / `ask_doubi` / Codex conductor 等 CLI/API/MCP 通道；`ask_codex` 不是常规接力棒，只能用于用户明确要求的旁路复核；优先自动化、可复现、可断点续跑。
   - **控制权铁律**：用户仍可指定通道，但未声明时不再追问，默认 `网页版接力`。CC/Codex 不得因为 CLI 更顺手、自动化更方便或历史习惯而私自切回 CLI；用户明确指定 CLI 时，也不得私自改成 Web。
   - **通道不改变算法**：无论 CLI 端还是网页版，固定棒次顺序、串行接力、N-1+N-2、§3.1 翻译原则、§3.2 14 维评分、每轮 checkpoint、收敛规则、输出 schema 全部保持同一套圣经。

### Step 2 — 格式转换

输入文件先转纯文本/Markdown：

| 格式 | 转换工具 |
|---|---|
| .pdf | 本地 `pdf` skill |
| .docx | 本地 `docx` skill |
| .html | pandoc / lynx |
| .srt / .po / .md / .txt | 直接读 |
| 全格式管道（PDF/DOCX/XLSX/MD/TXT/JSON/EPUB/SRT/ASS/PNG）| 嫁接 xunbu/docutranslate **converter 层**（仅 IO，无 HTTP，见 §10） |
| 其他稀奇格式 | 临时下载对应 skill |

### Step 3 — 串行接力链

**固定顺序（Codex-led workflow）**: **哈士奇** → 小D → CC → **逗比** → Codex conductor → 哈士奇 → …… (循环)。默认 Web Relay Mode 一一映射为 **哈基米** → 老D → 小克 → **包子** → 小G。上游 CC 侧旧顺序只作为历史背景，不得直接用于本 fork 新派发。

**首棒哈士奇协议**:

| 类型 | 触发 | 派发 prompt 内容 |
|---|---|---|
| **R1 第 1 棒哈士奇**（接力链最起头） | 跑全新翻译任务的第一棒 | (1) 原文 (2) **作者参考样本**（Step 1 第 7 项；若用户提供则附上，未提供不得追问为必填）(3) **首棒机翻参考底稿**（Step 1 第 8 项；DeepL 收录则双版 Google + DeepL，否则 Google 单版）(4) §3.1 翻译原则 + 用户特殊要求 + 当前章节 glossary（若大文件嵌套）；**不发前情提要、不发 N-2 段、不发 N-1 段** |
| **R2/R3/Rx+ 续轮哈士奇起头棒**（接 Rx-1 末棒）| 多轮接力第 2 轮及以后的哈士奇起头棒 | 按普通棒次**四段式派发**：(1) 前情提要 ≤200 字（含已锁定决议+R2 沉淀铁律）(2) **上两棒（Rx-1 倒数第 2 棒）完整译文 + 完整点评** (3) 上一棒（Rx-1 末棒；CLI/API 为 Codex conductor，Web 为小G）完整译文 (4) 上一棒完整点评 |

- 渠道: `ask_husky` / Antigravity CLI bridge（旧 Gemini 通道记录不得作为当前执行通道）
- **CLI 主链不再走旧 Web 中继**
- **v0.3.3 切开理由**：v0.3.2 "首棒哈士奇例外" 模糊指代被 R3 实战暴露——R3 哈士奇本质是续轮起头棒（接 R2 末棒；Codex-led workflow 当前末棒为 CLI/API Codex conductor 或 Web 小G），不应套 R1 用户初版协议；续轮必须按普通棒次四段式派发

| 棒次 | 成员 | 渠道 | 任务 |
|---|---|---|---|
| #1 | **哈士奇** | `ask_husky` / Antigravity CLI bridge | **首棒审核+润色 Google/DeepL 机翻参考底稿** |
| #2+ | 小D / CC / **逗比** / Codex conductor / 哈士奇 / …… | API / CLI（逗比走 ask_doubi MCP；CC 走 ask_cc；Codex conductor 在主线程收束） | 客观点评前一棒 + 给出润色版本（Codex-led workflow 以本行顺序为准） |

#### 3.12 Web Relay Mode

**定义**：网页版接力只替换"执行端/交互端"，不替换 translate-v2 算法。它不是 Deep Research，不是闭卷并行，不是额外评审团，也不是 provider fallback；2026-05-25 起它是默认同构接力通道。

**启用条件**：
- 用户未指定通道时默认启用普通 "网页版接力 / Web Relay Mode / 用网页端接力"。
- 用户指定"CLI 端接力"时，必须走 CLI/API/MCP 主链，不因网页端更快而改路。
- 只有用户明确指定 `CLI 端接力`、`CLI 版接力链`、`走 CLI` 或同义指令时，才走 CLI/API/MCP 主链。

**当前 Codex-led workflow 一一映射**：
| 接力棒 | CLI/API 端 | Web 端替换 | 备注 |
|---|---|---|---|
| #1 | 哈士奇（`ask_husky` / Antigravity CLI bridge） | 哈基米（Gemini Web） | 普通接力用 Web 聊天/模型；Deep Research 仍是 §6 调研节点，不能混作普通棒次 |
| #2 | 小D（DeepSeek API） | 老D（DeepSeek Web） | 保留节制审稿型定位 |
| #3 | CC（Claude Code CLI / `ask_cc`） | 小克（Claude Web） | 第三棒审核/润色；不是自动深研 |
| #4 | 逗比（Doubao API） | 包子（Doubao Web） | 普通网页接力与"深入研究"按钮分开 |
| #5 | Codex conductor（主线程） | 小G（ChatGPT Web） | Web 端输出第五棒普通候选；Codex conductor 仍负责归档、checkpoint、发散分析和最终报告 |

**Codex-led workflow 本地映射**：若本地 `SKILL.md` 已把正常链改成 `哈士奇 -> 小D -> CC -> 逗比 -> Codex conductor`，Web Relay Mode 对应为 **`哈基米 -> 老D -> 小克 -> 包子 -> 小G`**。小G负责第五棒普通接力输出；主控职责仍由当前 Codex conductor 负责，包括合并落档、checkpoint、发散分析、最终裁判和翻译分析报告。Codex conductor 不在 Web Relay Mode 中另起一个本地第五棒覆盖小G。

**派发要求**：
- Web 棒次使用与 CLI 棒次完全相同的 prompt 包：§3.1 顶部翻译原则 + §3.2 底部 14 维评分 schema + N-2 / N-1 四段式上下文 + 用户特殊要求 + glossary。
- Web 棒次必须输出同一 schema：对前棒的 14 维审核/问题列表、`S_norm`/严重度、规则理由、完整润色译文、收敛探针字段。
- 网页端如果因为 UI 字数、登录态、风控或输出截断导致 schema 不完整，主控应要求同一 Web 棒补齐；补不齐则在 round archive 标注"网页版通道缺口"，并在 checkpoint 交给用户决定继续、补跑或切 CLI。
- 网页端 chat URL、导出的对话文本、本地截图/抓取稿或手动复制来源路径必须写入 round archive，便于后续 baseline 评分按 v0.3.8 "chat 工作流证据"规则复核 conscious vs accidental。

**禁止**：
- 禁止把 Web Relay Mode 自动扩展成哈基米/小G/包子 Deep Research；深研仍必须由用户在 §6 调研口显式触发。
- 禁止用网页版接力为由跳棒、并行派发、缩减 14 维评分、砍掉 N-2、或把每轮一档归档改成散落聊天记录。
- 禁止在用户指定 CLI 端接力时，把某棒私自换成网页版；同理，用户指定网页版接力时，不得因 CLI 端更顺手私自切回 CLI。

**深度调研例外**（Step 4 (b) 触发，v0.3.2 强化；2026-04-30 扩充三家 + scholar 兜底；v0.3.9 拆分触发条件与结论权重）:

**触发条件**：
- (i) §3.1 标记需调研的典故/双关/古词义（沿用 v0.3.2，CC 主动**建议**入口）
- (ii) **任意 Rx 轮末尾 checkpoint 用户显式触发**
- (iii) **R1 首棒哈士奇派发前的"启动前置调研"窗口用户显式触发**：在 §Step 1 十项收集完毕、CC 准备调用 R1 首棒哈士奇之前，用户可视情况判断是否一开始就深度调研一下；用户点头 → CC 暂停首棒派发 → 走调研节点四选一中继 → 调研结果回流 → 注入 R1 首棒哈士奇 prompt 顶部"前置调研结论"段（与原文/作者参考样本如有/Google + DeepL 双版机翻底稿/§3.1 翻译原则并列）→ R1 首棒派发；不计入 round count
- (iv) ~~Step 1 第 9 项档位声明 = C 不熟级时强制前置触发~~ **作废**；v0.3.11 把"由我决定是否触发"的时机扩面到 R1 启动前 + 任意轮末尾两口，但**仍由用户确认**，C 档场景 CC 仅可主动**建议**调研

**扩面边界铁律**：
- **中间棒派发前不开调研口子**（用户校准核心边界）：R1 第 2 棒及之后的接力链中间棒派发节点**不接受**调研中断；底层逻辑——接力链 v0.3.10 N-1 + N-2 双棒上下文滑窗依赖"棒次连续"才能识别"修正还是回弹/某争议跨棒是否稳定/catalyst 是否被吞"，中间棒被调研中断会让 N-1/N-2 段出现「调研结果」这种异质内容打破"前一棒译文+点评"的纯净结构；故调研口子只开在"接力链外"两个边界——R1 启动前 + 轮末，不开在"接力链内中间"
- 扩面动作只动"何时可以触发"，不动"谁来确认"——CC 不获自启自动调研权；任何调研启动必须有用户显式指令（如"开跑前先调研一下 X 这个典故"/"R3 末尾再调一下 Y"等）
- CC 在 R1 启动前 + 轮末可主动**建议**"用户，本任务涉及 [X 典故/Y 古词义/Z 双关]，是否需要先调研？"——但这是建议不是默认，用户不点头则按原计划派发；不可把"建议"做实成"默认调研"

**调研节点四选一**，非接力链棒次，不进 round count：
- **哈基米**（Gemini Web "深度研究" 按钮）— 英文学术 / Google Scholar 路径 / 跨源综合
- **小G**（ChatGPT Web "深度研究" 按钮）— 英文学术 / OpenAI 私域 / 长报告综合
- **包子**（Doubao Web "深入研究" 按钮）— 中文长尾 / ByteDance 中文资源池
- **scholar skill** — 严格学术口径 + 真实引用（OA 检索）
- 三家 Deep Research **互补不互替**（project convention: Deep Research tools are complementary, not interchangeable）；按译文域题材选投，重要术语可二投/三投横评后再回流
- 包子（Web 网页通道）跟逗比（API 通道，doubao-seed-2-0-pro-260215）是两条独立路径，不要混用
- 三家 Deep Research 均走 Web 端，因各家 CLI 端均无 Deep Research 功能（project convention）
- 中继协议沿用 Codex workflow 人工中继规则（prompt → `<relay-prompt-scratch>`，附件 → `<relay-upload-dir>/`）
- 调研结果回流后注入下一轮哈士奇/小D 等棒的 prompt 顶部

**调研结论权重**：
- **三档等效铁律**（source decision note）：用户自写原文 = 用户吃透理解 = 三家调研结论 = **同等高优先级证据**；CC 在 R2/R4 发散分析、收敛判断时**不在三种证据间用权重梯度区分**
- **冲突处置**：当调研结论与用户判断冲突 / 调研结论彼此冲突 / 调研结论与接力链共识冲突时，CC 显式陈列各方证据让用户确认，不默认偏向任何一边
- **同源风险警惕**：调研选家时主动避免与接力链主笔同家（如调研用小G + 接力链小G 主笔会镜像反射），冲突视角应主动选用不同家调研工具（哈基米/小G/包子三选）


#### 3.0 翻译原则 vs 评分标尺职能切开

**铁律**: §3.1 与 §3.2 是 spec 内部**两套并行机制**，每棒同步使用、不互替——

| 维度 | §3.1 翻译原则 | §3.2 14 维评分 schema |
|---|---|---|
| **职能定位** | 生成时方向盘 | 事后检验标尺 |
| **prompt 位置** | 每棒 system prompt **顶部** 固化 | 每棒 system prompt **底部** 固化 |
| **内容** | 信达雅 / 三红线 / 受约束二次创作 / 体裁路由 / 场域分级 | Layer A 4 维 + Layer B 5 维 + Layer C 5 维 + GEMBA-V2 加权 |
| **用途** | 每棒**生成译文时**遵循的方法论方向 | 每棒译文**产出后**的对照尺子，输出 issue 列表 + S_norm 进 §3.4 收敛探针 |
| **量化梯度** | 无（方法论本身没有量化） | 有（critical=25 / major=5 / minor=1 / punctuation_minor=0.1） |

**职能不互替**:
- §3.1 不能用作"事后判分"——方法论本身没有量化梯度，无法转化为可对照的分数
- §3.2 不能用作"生成方向"——评分维度是事后诊断框架，不是创作方向；按 14 维"凑齐"维度产出译文会导致刻意化

**典型应用 — 哈士奇首棒选优**:
- **选优阶段** = §3.2 标尺（量化对比 Google + DeepL 双版 S_norm，选 S_norm 更小者作"润色入口"）
- **润色阶段** = §3.1 方法论（在选优胜版基础上按"信达雅 + 三红线 + 受约束二次创作 + 体裁路由"做 diff 决策）
- **自评阶段** = §3.2 标尺（对自家润色版跑 14 维评分进收敛探针）
- **点评段输出** = 双轨呈现（§3.2 客观数据 + §3.1 方法论 diff 决策点）
- 这是 §3.0 职能切开机制最干净的端到端实证，避免成员把"选优论证"和"翻译方法论论证"混为一谈

**全员适用**: 哈士奇 / 小D / Codex / 逗比 / CC 五位接力链成员**每棒同步使用** §3.1 + §3.2，二者职能边界恒定不变；下棒接力点评前一棒时同样按"§3.1 方法论 diff + §3.2 客观数据"双轨结构产出点评

#### 3.1 翻译原则（每棒 system prompt 顶部固化，v0.3 确认版）

```
【底线】信达雅；翻译是受约束的二次创作。译文必须在目标语里成为符合
目标体裁的成品文本，同时保留原文语义、信息密度、显隐关系、修辞功能、
音律/可诵性（当体裁需要时）、人物/论证关系和可审计源文锚点。

【创作边界】
- "直译为主"不得理解为词序搬运、逐词贴合、句法尸检或机器腔修补；
  它的正确含义是：优先保留可恢复的意义、信息密度、显隐程度、修辞
  结构、语用功能和可审计对应。
- 在不触犯 Addition / Omission / Mistranslation / Hallucination 的前提下，
  允许按目标语体裁进行句法重组、语气再造、节奏设计、信息顺序调整、
  习语替换和表达再创作。译文可以不表面贴源，但必须能说明每个创作
  动作服务于原文功能而非新增内容。
- 目标语成品感是忠实的一部分：小说译文要像小说，散文译文要像散文，
  学术译文要像论文，法律/技术译文要像可执行的专业文本。只覆盖字典
  意义但不像目标体裁成品，也是不忠实。
- 音律美是成品感的一部分，不限于诗歌。句长错落、停顿位置、重音落点、
  尾音、重复、轻微押韵、头韵/元音呼应、顶针/回环，都可以是翻译取舍
  的正当理由；但声音结构必须服务源文功能，不能为顺口而漂意。

【上下文证据边界】
- 用户提供的额外背景、剧透、人设说明、前文报告、深度调研结论，是为了消歧、校准语域、稳定术语、避免误读；它们不是待译原文的一部分。
- 用户提供的作者参考译文（如用户自己的英文版）也是作者级证据，但不是
  每次任务必备项。若提供，它与源文共同约束事实边界和创作手感；不得
  机械分工为"源文锁事实、参考译文锁风格"，也不得让参考译文覆盖源文。
  若两者审美路线不同，先说明分歧轴，再按目标语体裁重建。
- 禁止把背景信息中的动机、阴谋、因果解释、人物尚未知情的事实、研究结论、上下文推理，显性加进译文；除非原文本句已经明说或强烈暗示到必须显化，否则一律只作为选词依据。
- 译文必须保留原文的信息密度与显隐程度。原文是低密度小说对白、靠上下文托住潜台词时，目标语不得翻成解释型台词。
- 目标语为避免歧义或语法不通所需的最低限度补足可以接受；一旦目标读者能凭译文 + 上下文恢复原意，继续添加解释即按 Addition 处理，即使添加内容在剧情上为真。
- 每棒点评必须区分「用上下文校准措辞」与「把上下文内容写进译文」。若译文因背景信息而信息密度膨胀，应作为 Addition / Style 风险进入 issue list。

【场域分级】
- 小说 / 文学对白：推荐按目标语文学与表演标准再创作，保人物声音、
  场面气口、潜台词、关系压力、信息密度与可读性，不抠原句字面顺序。
  允许省略目标语中可由上下文承载的主语/称谓，或在后文补回，只要不
  造成 Omission；同时控制句子长短、停顿和尾音，让台词能顺口读出。
  禁止为了"解释清楚"把潜台词、背景或人物未知信息写明。
- 散文 / 随笔 / 文学非虚构：推荐在意象、句群呼吸、节奏、审美密度和
  叙述视角上做目标语重构。可重排句法与停顿以形成目标语散文美；不得
  改变思想推进、情感温度、意象关系或修辞重心。
- 学术论文 / 评论：推荐概念精确优先，保术语一致、定义边界、论证关系、
  hedge 强弱、引用/转述立场和段落逻辑。可追求清晰、平衡、可读的句群
  节奏，但禁止文学化、美文化、夸大结论或把推测翻成断言。
- 法律 / 技术 / 合同 / 标准：推荐受控直译与结构对齐，保定义、条件、
  范围、否定、枚举、单位、参数和可追溯性。创作自由最低，宁可硬一点
  也不能漂亮到改变执行含义。
- 成语 / 俗语 / 谚语 / 歇后语：推荐意译，保意不保字面
- 口语化场景：推荐适当意译，保口吻不抠字眼；同时必须保留目标语
  真实口语的气口、碎片、停顿、省略、短促度和现场关系压力，不得
  翻成完整书面句、商务邮件、成熟敬语套、会议发言或"联合国演讲口语"。
  · **判定标准**：原文含明显非正式口语标记（网络流行语、方言俚语、随意省略主语/助词）时触发；此外，只要是对白、现场发言、聊天、谈判、角色外语、code-switch、非母语角色说目标语、或原文故意含破碎目标语，也必须触发口语预检。中规中矩的陈述句即使内容生活化，也不自动授权无锚点自由改写；但在已确认的口语场景中，"语法完整"不得压倒"现场可处理性 / 人物声音 / 目标语口语自然度"。
  · **角色化非标准语保护**：若破碎英语/日语/其他目标语是作者定稿、角色外语能力、族群/奇幻/行业语域、或现场策略的一部分，只允许做最小必要修复。保留可懂的单词块、非标准语法、短句、旧派/族群词汇；禁止为了母语化而改成客服腔、HR 腔、商务函、说明文或完整礼貌套。
  · **电影台词 / 文学对白例外**：口语不等于越破碎越好。若用户明确追求电影台词美、戏剧性、文学对白、或章节既有英文风格基本语法完整，应保留相对完整的句法，用短句、节奏、停顿、词感、语气转折来做口语化；禁止为了反商务腔而过度打碎、降智或制造假 casual。
  · **口语优先级**：能否被目标语听者即时处理 > 书面语法完整；人物声音成立 > 礼貌完整；短促低密度 > 解释清楚一切。但当完整句更符合电影台词美、角色能力、风格一致性或用户定稿时，完整句不扣分。只有当碎片造成非预期歧义、误解、语义丢失或角色错位时，才作为 fluency/semantic issue 修复。
- 中规中矩的陈述句：不得无依据整段改写；但仍按体裁成品标准翻译，
  允许目标语必要的句法重组、搭配替换和语气调整。表面贴源但不成文
  不算高质量。
- 修辞性造词 / 隐喻性构词：允许（鼓励）按目标语构词法做对等映射
  示例：中文"玉质疏松" → 日文「玉粗鬆症」
  （类比日语原有"骨粗鬆症"自创对等术语，保留原文的修辞构词逻辑；
   原文"玉质疏松"本身也是借"骨质疏松"造的比喻新词，
   译文按目标语规则造对等新词 = 修辞结构对等翻译，非脑补、非自由发挥）
- 韵文体裁（古诗词 / 歌词 / 戏曲唱段 / Rap / 韵律散文）：
  三优先级（v0.3 确认，由 Step 1 第 6 项触发）：
    第一优先级 = **节奏感对应**（断句 / 停顿 / 字数 / 音步）—— 必保
    第二优先级 = **字面精度**（守 §3.1 三红线，不漂）
    第三优先级 = **押韵**（默认"能则押"——发现漂意立即降级回不押）
  默认取向：**宁失韵不漂意**；节奏感为第一优先级，必须尽最大可能保留——无法完全对应时不得为补节奏违反三红线，偏差点统一在 Step 5 韵律说明列明
  押韵冲突原则：节奏感 / 字面精度 / 押韵 三者打架时，按上述优先级牺牲低位
- 非韵文音律：小说、对白、散文、演讲、标题、评论等也要检查可诵性。
  可通过句长交替、短句落点、重复、顶针、内韵、轻押韵、头韵、元音/
  辅音呼应来增强目标语成品感；若这些结构自然出现，应优先保留或重建。
  但不得为了音律牺牲术语、事实、论证强度、人物关系或法律/技术精度。

【绝对红线】
- Addition: 禁添加原文不存在的解释/补充/修饰/情感色彩
- Omission: 禁省略原文任何信息
- Free Rewriting: 禁无依据加戏、整段脱离源文功能重写、改动人物关系/
  知识状态/情感强度/论证强度；不禁止有源文锚点、服务体裁成品感的
  句法重组与表达再创作

【结构性约束】
译文须保留与原文可分析的功能/语义/修辞对应；句法对应可以是转换后
的对应，不要求词序或从句结构一一贴合——
以满足 Translation.txt "句法构词分析" 段的输出要求（spec §2 Step 5）。
通篇无锚点自由改写会让对应消失，违反 spec 输出 schema 强制；有锚点、
可解释、服务目标体裁的转换不算违规。
```

#### 3.2 评分 schema

**v0.3.5 确认版**：从 v0.3 的 6 维 MAATS/MQM 平铺 schema 升级为 14 维三层 nested schema（语言 / 文学 / 文化）。底层逻辑见顶部 v0.3.4 → v0.3.5 规则段，关键依据是包子+小G+哈基米三家深研 + Codex/小D/逗比/小K 四家闭卷评审收敛建议。

##### Layer A · 语言层（4 维 · MQM 错误骨干 · 必填）

| # | 维度 ID | 评估对象 | severity 典型例（critical / major / minor / punctuation_minor）|
|---|---|---|---|
| 1 | `semantic_fidelity` | 语义忠实（v0.3 Accuracy 收紧）：Addition / Omission / Mistranslation / Hallucination 四红线 | critical：核心意象错（"沧海月明"译成 dark sea）/ major：典故误指 / minor：限定词漏 / — |
| 2 | `completeness` | 完整性：未译片段、跳行、丢句子| critical：整句漏 / major：从句漏 / minor：修饰语漏 / — |
| 3 | `fluency_mechanics` | 译入语流畅 + 语法 + 拼写 + 标点 + 排版；同时检查目标语是否像该体裁的成品文本、是否顺口可读。口语场景另查即时可处理性、碎句/省略是否自然、是否把现场话翻成书面/演讲/商务腔，也查是否过度碎片化破坏电影台词美 | major：句子读不通；或表面直译导致目标语像练习题/译注/句法尸检；或句长机械齐平、读不出口；或口语场景虽语法完整但像客服/HR/会议稿、人物不可能这样说；或为反正式而碎得假/降智 / minor：搭配不地道、口语气口偏硬、轻微过碎、节奏别扭、或体裁手感偏硬 / — / punct：标点错（全/半角混）|
| 4 | `terminology_entities` | 术语一致 + 专名拆层译（Title+Name 两层不无脑拼音化）| major：望帝译错失杜鹃双关、Hanwudi 纯拼音化 / minor：术语前后不一致 / — |

##### Layer B · 文学层（5 维 · 文学专属 · 韵文必填、散文选填）

| # | 维度 ID | 评估对象 | severity 典型例 |
|---|---|---|---|
| 5 | `voice_register` | 作者声音 + 文白语体落差 + 人物语体（吸收逗比文白独立诉求作子项）；按体裁检查小说/散文/论文/法律技术的声音是否成立。口语场景必须检查角色年龄/身份/关系/非母语能力/现场压力是否进入句尾、断句、完整度或破碎度 | critical：李商隐沉郁译成欢快 / major：文白错位；小说不像小说、论文不像论文、散文失去句群气息；或把低密度对白翻成联合国演讲、商务函、成熟敬语套；或把本应有电影台词美的对白打碎成假口语 / minor：tone 偏移 / — |
| 6 | `imagery_rhetoric` | 意象 + 列锦 / 对仗 / 互文 / **Liu Bai over-translation 子检测**（吸收哈基米 gap + Codex over-explicitation detector）| critical：核心意象丢 / major：列锦谓词化破坏意象并置 / minor：意象顺序调换 / — |
| 7 | `rhythm_prosody` | 韵律节奏（slant rhyme / metrical / 节奏对应 / 句长错落 / 停顿 / 重音 / 尾音 / 轻押韵 / 内韵 / 顶针 / 重复 / **列锦体裁的英诗合法性**子检测）。非诗歌也可触发可诵性检查 | major：列锦体裁强加 perfect rhyme；或小说/散文/台词译成死板等长句、失去顺口度；或为押韵/顶针漂意 / minor：押韵密度偏离、句长单调、音节落点不顺 / — |
| 8 | `prosody_compensation` | **平仄补偿映射**。注意字段名是 compensation 而非 preservation——英语非声调语言无 syllabo-tonic 等价物，评估"是否用 alliteration / assonance / metrical pacing 补偿了源诗的 Pingze 张力" | major：源诗 Pingze 紧密但译文声学完全平淡 / minor：部分补偿但密度低 / — |
| 9 | `form_coherence` | 篇章视角 / 行段结构 / 形式美 / 视觉空间排布 | major：篇章 POV 跳乱 / minor：行间布局微差 / — |

##### Layer C · 文化层（5 维 · 文化负载 · 古典/文学必填）

| # | 维度 ID | 评估对象 | severity 典型例 |
|---|---|---|---|
| 10 | `cultural_transfer` | 文化负载词 + 归化/异化策略一致性（道/气/阴阳 等）| critical：核心文化负载词错译 / major：归化过度 / minor：minor cultural drift / — |
| 11 | `allusion_intertext` | **典故 + 嵌套连环双关层级追踪**。**连环双关需标注「谐音层 + 典故层 + 同源词层」三级损失度**，不可合并为单一扣分 | critical：连环双关全丢（如望/亡谐音 + 望帝姓杜→杜鹃同源 完全损失）/ major：失一层 / minor：注释代偿 / — |
| 12 | `paratext_apparatus` | 注释 / 前言 / 页注 / 副文本。评估副文本是否到位、是否破坏正文气韵；正文 explicitation 与副文本 explication 应分离 | major：典故无注且正文无法自洽 / minor：注释冗长破坏阅读 / — |
| 13 | `strategy_coherence` | 策略一致性（Venuti 异化/归化是否前后一致；归化/异化飘移视为错误）；检查本次体裁路由是否一贯：文学是否敢于受约束再创作，论文/法律技术是否收紧创作自由。口语场景检查是否一边保留专名/异化，一边把人话润成说明文或商务套 | major：前段异化后段归化；文学段落机械直译导致不成文；论文/法律段落被文学化改弱精度；或口语/角色外语策略未先判定就强行母语化 / minor：单点 drift / — |
| 14 | `reader_reachability` | **TREQA 阅读理解外部评估**。译文是否使目标读者能完成针对原文的核心理解任务，并能把文本作为目标体裁阅读/朗读；口语场景还要测试读者是否能读出人物关系、现场气口、调侃/尊重/压力等语用功能 | critical：5 题中 ≥3 题答错 / major：≥2 题答错，或只能懂字面却读错体裁功能/场面功能/人物声音，或台词/散文读不出应有节奏 / minor：1 题答错 / — |

##### 严重度公式（GEMBA-V2 加权，吸收 Codex + 小D 共识）

```
WEIGHTS = { "critical": 25.0, "major": 5.0, "minor": 1.0, "punctuation_minor": 0.1 }

S_raw  = 25 × c + 5 × m + 1 × n + 0.1 × p
S_norm = S_raw × 1000 / char_count    # 中→英用 source char_count；多语种可改 word_count
quality_score = max(0, 100 − S_norm)

# 派生字段（向后兼容 v0.3.4 / MQM 经典）
mqm_legacy_penalty = (10 × c + 5 × m + 1 × n + 1 × p) × 1000 / char_count
```

##### 输出 JSON schema（每棒 system prompt 底部固化）

```json
{
  "schema_version": "0.3.5",
  "scores": {
    "language": {
      "semantic_fidelity":      {"rating": 0-100, "errors": [...], "method": "llm_judge", "confidence": 0-1, "evidence": [...]},
      "completeness":           {"rating": 0-100, "errors": [...], "method": "llm_judge", ...},
      "fluency_mechanics":      {"rating": 0-100, "errors": [...], "method": "rule|llm_judge", ...},
      "terminology_entities":   {"rating": 0-100, "errors": [...], "method": "rule|llm_judge", ...}
    },
    "literary": {
      "voice_register":         {"rating": 0-100, "errors": [...], "method": "llm_judge", ...},
      "imagery_rhetoric":       {"rating": 0-100, "errors": [...], "method": "llm_judge|hybrid", ...},
      "rhythm_prosody":         {"rating": 0-100, "errors": [...], "method": "rule|hybrid", ...},
      "prosody_compensation":   {"rating": 0-100, "errors": [...], "method": "hybrid", ...},
      "form_coherence":         {"rating": 0-100, "errors": [...], "method": "rule|llm_judge", ...}
    },
    "cultural": {
      "cultural_transfer":      {"rating": 0-100, "errors": [...], "method": "llm_judge", ...},
      "allusion_intertext":     {"rating": 0-100, "errors": [...], "method": "llm_judge", "puns_layers": ["谐音","典故","同源词"]},
      "paratext_apparatus":     {"rating": 0-100, "errors": [...], "method": "human|llm_judge", ...},
      "strategy_coherence":     {"rating": 0-100, "errors": [...], "method": "llm_judge", ...},
      "reader_reachability":    {"method": "external_task", "questions": [...], "accuracy": 0-1, "confidence": 0-1}
    }
  },
  "aggregate": {
    "penalty_per_1000": <S_norm>,
    "quality_score":    <0-100>,
    "pass":             <bool>,
    "blocking_issues":  [{"span":"...","severity":"critical","category":"semantic_fidelity"}],
    "weight_profile":   "literary|technical|legal|mixed"   // §3.8
  }
}
```

**error 子结构**（每条错误）：

```json
{
  "span": "<译文片段>",
  "source_span": "<原文对应片段>",
  "category": "semantic_fidelity|...|reader_reachability",
  "severity": "critical|major|minor|punctuation_minor",
  "penalty": 25|5|1|0.1,
  "rationale": "<一句话解释>"
}
```

**method 字段取值**：`rule` / `embedding` / `llm_judge` / `hybrid` / `human` / `external_task`（吸收 Codex 设计）。

不强制每棒输出冗长审计报告，每维 errors 数组可空（无错时）但 `rating` 与 `method` 必填。

#### 3.3 点评模板（每棒 system prompt 点评段开头，借鉴 MAD 四要素，v0.3 确认版）

```
请按以下四要素客观评价前一棒译文（不挂角色，不分 Devil/Angel/Judge）：

1. 位置: 指出具体词 / 句 / 段位置
2. 理由: 说明问题原因（对照 §3.1 翻译原则 + §3.2 三层 14 维 schema）
3. 证据: 引用原文相关片段作证
4. 替代: 给出更优替代译文（不是空批评）
```

#### 3.4 收敛探针字段

**v0.3.5 改造**：v0.3 / v0.3.3 的 `satisfaction: satisfied | minor_issues | unsatisfied` 三档软标签被推翻，原因是该 schema 无法区分"严重文学损伤"与"轻微机械错误"——一个 critical 错和一个 minor 错被同等对待，导致 critical 错被掩盖（小D 评审 R2 风险分析）。新方案：每棒输出 **§3.2 错误列表 + 加权聚合分数 + 三档判定**，CC 不再正则解析单行 satisfaction 字段，改解析 `aggregate.pass` 布尔值。

**每棒回复最后一段强制输出**：

```
penalty_per_1000: <S_norm 数值>
quality_score: <0-100>
pass: <true|false>
critical_count: <c>
remarks: <一句话本棒自评>
```

**三档判定**（吸收小D 阈值 + Codex profile 设计）：

| 等级 | 条件 | CC 处理 |
|---|---|---|
| **Pass** | `S_norm ≤ 8` 且 `c=0` | 棒可接受，连击计数器 +1（硬阈值场景） |
| **Major-defect** | `8 < S_norm ≤ 20` 或 `1 ≤ c ≤ 2` | 需规则，触发重评，连击重置 0 |
| **Critical-defect** | `S_norm > 20` 或 `c ≥ 3` | 致命，连击重置 0；critical 标记注入下一棒 prompt 顶部作为本轮重点修复目标，接力链继续往下推；用户在轮末 checkpoint 决定是否提前触发深度调研或人工介入 |

阈值数值（8 / 20）由小D 评审给出 [推断]，需 R4-R6 实战校准。

**weight_profile** 字段（详见 §3.8）：每棒按当前任务的 brief 选 `literary` / `technical` / `legal` / `mixed` 预置权重表，14 维 rating 在归一化时按权重加权。

**向后兼容**：保留 `mqm_legacy_penalty` 派生字段，按 critical=10/major=5/minor=1 公式回算，便于跨版本对比。

#### 3.4-bis DeepL/Google 双锚点相对评级

**底层逻辑**：v0.3.5 14 维 + GEMBA-V2 加权三版实测（DeepL 机翻 / 哈基米 R1#1 / R3 终态用户满意版）暴露 **S_norm 单一标量在文学翻译里区分度归零**——三版 S_norm 分别 203 / 238 / 207，DeepL 反超 R3 终态。本节在 §3.4 绝对阈值之上叠加"行业最强翻译器作为及格线锚点"的相对评级，落地用户 KPI："不输 DeepL"是 skill MVP 底线。

**3.4-bis.1 DeepL 主锚点**

| 等级 | 条件 | 含义 |
|---|---|---|
| Excellent | `S_norm < DeepL_baseline × 0.6` | 比 DeepL 强 40%+，文学翻译罕见 |
| Good | `DeepL_baseline × 0.6 ≤ S_norm < × 0.9` | 比 DeepL 强 10-40% |
| **On par**（及格线）| `× 0.9 ≤ S_norm ≤ × 1.1` | ±10% 内 = 持平 DeepL |
| Below baseline | `S_norm > DeepL_baseline × 1.1` | 比 DeepL 差 >10%，需重做 |

**3.4-bis.2 Google 兜底锚点**（DeepL 不支持目标语种时）

| 等级 | 条件 | 含义 |
|---|---|---|
| Excellent | `S_norm < Google_baseline × 0.6` | 同 DeepL 优秀线 |
| Good | `Google_baseline × 0.6 ≤ S_norm < × 0.9` | — |
| **On par**（及格线）| `× 0.9 ≤ S_norm ≤ × 0.95` | **系数收紧 5%**：Google < DeepL（专家偏好 1.3×），"不输 Google × 0.95" ≈ "接近 DeepL 真实水平" |
| Below baseline | `S_norm > Google_baseline × 0.95` | — |

⚠️ **0.95 系数为 [推断] 数值**，需用户未来跑同一篇双 baseline（DeepL + Google）实测后校准。如实测发现 Google 平均比 DeepL 多 X 分（每千字符），则系数应调整为 `1 - X/Google_baseline`。

**3.4-bis.3 锚点选择决策树**

```
1. 目标语种 ∈ DeepL 36 种支持列表？
   → 是：抓 DeepL baseline，套 §3.4-bis.1
   → 否：跳 2

2. 目标语种 ∈ Google 249 种支持列表？
   → 是：抓 Google baseline，套 §3.4-bis.2
   → 否：跳 3

3. 双锚点均不可用：
   → 退化为 §3.4 GEMBA-V2 绝对阈值（不再有相对评级）
```

DeepL 支持列表（2026.05 实情）：DE/EN/JA/ZH/FR/ES/IT/PT/RU/NL/PL/SV/DA/FI/NO/CS/HU/RO/TR/AR/ID/UK/KO/HE/TH/VI 等 36 种 + 文档翻译加 Arabic/Traditional Chinese。

Google 支持列表：249 种含小语种（蒙/藏/Quechua/Sanskrit 等）。

**3.4-bis.4 baseline 抓取协议**

- **手抓模式**：用户网页版手抓 DeepL/Google 译文 → 落档 → CC 评 14 维算 S_norm
- **DeepL Free vs Pro**：翻译模型完全相同（同一 neural engine）；网页 Free **单次粘贴** UI 上限约 1500 字符（**v0.3.10 终态澄清**：这是 DeepL Web UI 的单次粘贴上限，**非 skill 硬约束**——长文走"用户自定义分段（按章节/Part/段落）"分多次粘贴抓取后用户自拼回整文 baseline）
- **长文分段一致性铁律**：同一篇全程同一种分段策略（不可一段按句号分一段按段落分），保证 §3.4-bis baseline S_norm 计算口径一致；sample 4《木兰诗》3 Part 已实证用户手分章节模式可行，分段策略由用户决定不由 skill 卡死
- **不接 API 理由**：DeepL 改 2026 产品矩阵后无永久免费档（"免费试用"仅一次性 100 万字），Free 档烧光后只能切付费 Developer $26/月；网页版手抓零成本零额度焦虑
- **v0.3.10 工作流闭环**：v0.3.10 §Step 1 第 8 项「首棒机翻参考底稿」要求用户启动翻译时即提供 Google + DeepL 双版（或 Google 单版） — **本节 baseline 抓取直接复用** Step 1 输入端的同份双版机翻档，无需事后再抓一次。R1 启动时 baseline 自动到位 + 评分阶段 S_norm 计算与 R1 首棒哈士奇审稿底稿同源 → 保证"评估锚点"与"接力起点"是同一对工业基线。落档路径 = Step 1 上传位置（`<baseline-input-{google,deepl}>`）→ CC 拷贝镜像入下方 baselines 目录归档
- **落档路径**：
  ```
  <translate-v2-workdir>/baselines/
  ├── deepl/<YYYYMMDD>-<topic>.md
  ├── google/<YYYYMMDD>-<topic>.md（DeepL 缺位语种走单版）
  └── _matrix.md（跨样本对照矩阵汇总）
  ```

**3.4-bis.5 系数校准建议**

未来用户每抓一组同篇双 baseline（DeepL + Google）时，CC 自动算：
```
ratio = Google_S_norm / DeepL_S_norm     # 实测样本平均
new_google_coef = round(1 / ratio × 0.95, 2)   # 0.95 = DeepL On par 上限倍率
```
样本量 ≥ 5 时更新 §3.4-bis.2 的系数（替换 [推断] 标记）。

**3.4-bis.6 实测档案锚点**

- `<relay-raw-dir>/20260501-193700-cc-v035-schema-mvp-test.md`：R3 终态单版 14 维评分
- `<relay-raw-dir>/20260501-195300-cc-v035-schema-mvp-3way-test.md`：DeepL + 哈基米 R1#1 + R3 终态三版对照（暴露 S_norm 区分度归零问题）
- `<translate-v2-workdir>/baselines/deepl/20260501-jinse.md`：锦瑟 DeepL baseline

#### 3.5 收敛条件

**v0.3.2 确认**：文学翻译（古诗词/小说/戏曲）不再要求"任何错都挑不出"零错收敛。

**新软阈值**（默认）:
1. **边际改进趋近 0**: 连续 N 棒改动量小（措辞微调、无 Accuracy/critical 类新增问题）
2. **用户主观满意**: 在 Step 4 checkpoint 时用户表示"可以了"
3. **待调研清单确认**: 已知争议点（典故/双关/古词义）走过 Step 4 (b) 调研一轮，结论已注入接力链

**硬阈值**（仅技术文档/法律文本/格式化合同等"标准答案"型走原 v0.3.1 滑动窗口；v0.3.5 升级到 GEMBA-V2 加权 + 三档判定）:

| 棒次状态（§3.4 三档判定）| 计数器动作 |
|---|---|
| 当前棒 **Pass**（`S_norm ≤ 8` ∧ `c=0`）| 连击计数器 +1 |
| 当前棒 **Major-defect**（`8 < S_norm ≤ 20` 或 `1 ≤ c ≤ 2`）| 连击计数器重置为 **0** |
| 当前棒 **Critical-defect**（`S_norm > 20` 或 `c ≥ 3`）| 连击计数器重置为 0 + **critical 标记注入下一棒 prompt 顶部作为"本轮重点修复目标"** + 接力链继续往下推；用户在轮末 checkpoint 决定是否提前触发深度调研 |
| 连击计数器连续达到 **3** | 触发 Step 4 用户 checkpoint |

**v0.3.5 改造**：v0.3.3 "minor_issues 一律 unsatisfied" 粗暴版被推翻。粗暴版的两大风险（小D 评审）：(R1) 1 个 minor_issue 整轮 decapitated，掩盖该棒实际高质量；(R2) critical 错与 minor 错同等惩罚，致命错传递到下一棒。新加权版用 GEMBA-V2 公式区分严重度，同时保留"必触发发散分析"的设计意图——`S_norm ≤ 8` 容差仅放过 8 个 minor 或 1 major + 3 minor 等组合，不会让明显有错的版本轻易过关；critical 仍是硬限不可绕过。

**关键语义**: 滑动窗口判定，**非绝对值累加**；前序棒次曾 unsatisfied 后被修复，下一棒符合计票条件即重新计数。

**Why 软化**（2026-04-29 锦瑟 R1+R2 实测）:
- 锦瑟 10 棒按硬阈值判定，计数器始终 0/3 全链未收敛
- 5 大反复争议点（L1 无端 / L4 望帝译名+春心 / L5 鲛人珠泪 / L7 可待 / L8 惘然）属 4 类根本困境（汉英语义颗粒度差 / 典故压缩 vs 句法展开 / ambiguity 是诗意 / 学界两派分歧）
- 实测出现"循环退化"（小K R2 复发 R1 已被挑过的 spring heart→grief Mistranslation + far astray Addition）
- 硬阈值会陷入无限循环；文学翻译边际改进归零比"零错"更合理

#### 3.6 轮次上限（v0.3 守 v0.2 铁律 4，"无上限"）

- **没有硬终止**——守 §1 铁律 4 "轮数无上限"
- **满 8 轮提示用户介入**: CC 在第 8 轮末尾向用户报告"已跑 N 棒未收敛，是否：(a) 继续跑 / (b) 介入打回某棒 / (c) 强制收尾出当前最佳版本"
- **用户可选择继续跑**——不是硬超时

#### 3.7 API / 成员调用层容灾（Codex workflow rule 2026-05-27）

- **同路一次重试**: 单棒 API/CLI/成员调用失败后，Codex 调度层只做一次明确重试，且必须保持同成员、同工具、同模型、同 thinking/effort、同 prompt（传输层格式可等价重发）。上游 SDK/CLI 内部 retry 不算这一次。
- **禁止静默 provider fallback**: 不得把 DeepSeek 挂了自动切 Moonshot、不得把 CC 掉线自动换 Codex、不得因失败降模型/降 thinking/改通道。二败后停止该棒自动推进，向用户报告失败证据并让用户决定 fallback。
- **铁律**: 渠道容灾不能改成员顺序、不能跳棒、不能把污染/截断/未 raw 落档输出当 N-1/N-2。

#### 3.8 文体动态权重

**底层逻辑**：14 维 schema 平权计分对所有体裁一刀切是错的。包子原始报告给出"文学：信30/达30/雅40 vs 科技：信50/达40/雅10"差异化权重；小D 评审基于 12 维给出文学场景 22/32/46 容差范围分布；本节按 14 维重分配，并通过 `brief` 字段动态切换 profile。

**先路由再评分**：译前必须建立 `genre + purpose + creative_contract + sound_contract`。
`creative_contract` 写明本体裁允许的再创作幅度：文学/小说/散文可在红线内
主动重组句法、节奏和语气，以目标语成品感为质量目标；学术论文收紧为概念、
论证和术语精度；法律/技术文本进一步收紧为可追溯、可执行、结构稳定。
`sound_contract` 写明是否追求可诵性、句长错落、电影台词感、散文节奏、
轻押韵、头韵/元音呼应、顶针/重复，或明确保持朴素专业、不追求音效。
若用户提供作者参考译文，还必须建立 `author_reference_contract`：记录参考
是否存在、它与源文共同锁定了什么、在哪些审美/口语/节奏轴上分歧、目标语
最终采用哪条策略路线。若没有作者参考译文，写 `not_provided`，不得追问为
必填项。
没有体裁/音律路由时，不得默认把所有文本压成表面直译，也不得默认自由发挥。

**weight_profile 预置表**（每个 profile 定义 14 维各自权重 ω_i ∈ [0, 1]，归一化 Σω_i = 1）：

| 维度 ID | literary（文学/古诗词）| technical（科技/法律）| legal（合同/合规）| mixed（默认）|
|---|---:|---:|---:|---:|
| **Layer A 语言层** | **22%** | **70%** | **65%** | **40%** |
| semantic_fidelity | 8 | 25 | 25 | 12 |
| completeness | 6 | 20 | 20 | 10 |
| fluency_mechanics | 5 | 15 | 12 | 10 |
| terminology_entities | 3 | 10 | 8 | 8 |
| **Layer B 文学层** | **32%** | **15%** | **5%** | **25%** |
| voice_register | 8 | 5 | 2 | 6 |
| imagery_rhetoric | 8 | 3 | 1 | 6 |
| rhythm_prosody | 6 | 2 | 0 | 4 |
| prosody_compensation | 5 | 2 | 0 | 3 |
| form_coherence | 5 | 3 | 2 | 6 |
| **Layer C 文化层** | **46%** | **15%** | **30%** | **35%** |
| cultural_transfer | 10 | 5 | 5 | 10 |
| allusion_intertext | 12 | 2 | 1 | 6 |
| paratext_apparatus | 6 | 4 | 8 | 5 |
| strategy_coherence | 8 | 2 | 6 | 6 |
| reader_reachability | 10 | 2 | 10 | 8 |

（数值 [推断] 基于小D 文学权重表 + R3 锦瑟实战经验，需 R4-R6 校准）

**brief 字段触发**（吸收 Codex 设计）：

```json
"brief": {
  "genre": "<诗词|小说|散文|科技文献|法律合同|新闻|...>",
  "audience": "<...>",
  "purpose": "<...>",
  "creative_contract": "<constrained_recreation|controlled_literal|strict_traceable|...>",
  "sound_contract": "<plain|read_aloud_smooth|cinematic_dialogue|prose_cadence|rhyme_alliteration|...>",
  "author_reference_contract": "<not_provided|dual_author_evidence_same_route|dual_author_evidence_divergent_routes>",
  "author_reference_divergence_axis": "<none|cinematic_vs_raw_speech|literary_vs_documentary|complete_vs_fragmentary|cadenced_vs_plain|compressed_vs_expanded|...>",
  "strategy": "<documentary|instrumental|domesticating|foreignizing|mixed>",
  "weight_profile": "<literary|technical|legal|mixed>",  // 默认按 genre 自动选
  "requires_poetry_metrics": <bool>,                      // 文学层 #7/#8 是否必填
  "requires_paratext": <bool>                             // 文化层 #12 是否必填
}
```

CC 在 Step 1 预处理时根据 `genre` 自动选 profile（诗词/古诗→literary；科技文献→technical；合同→legal；其他→mixed），用户可在 Step 1 第 5 项「特殊要求」显式 override。

#### 3.9 final 10 次盲评 + 2σ 离群剔除 + RRWA 聚合

**底层逻辑**：5 棒接力是顺序依赖 trajectory（i 棒看到 i-1 棒输出，错误会被继承/放大/修复），**不是 i.i.d. 独立采样**，因此不能直接套 GEMBA-V2 的 10 次评估 + 2σ + RRWA。改造为 **CC 收敛后对 final candidate 跑 10 次独立 LLM judge + 2σ 离群剔除 + Reciprocal-Rank Weighted Average 聚合**。

**实施要点**（吸收 Codex 评审）：

1. **棒内不跑 N 次自评**——成本 + self-preference 风险；只跑一次轻量 schema check（JSON 合法性、术语表 drift、明显遗漏）
2. **棒输出保留 `stage_eval`**，只作 debug signal 不进 RRWA
3. **CC 收敛后**对 final candidate 跑 10 次独立 GEMBA-style judge（不同 seed / 温度），每次返回 §3.2 的 14 维 errors + S_norm
4. **2σ 离群剔除**：剔除 |s_i - s̄| > 2σ̂ 的运行
5. **RRWA**：按排名倒数加权聚合，进 `aggregate.penalty_per_1000`
6. **高风险维度 focused rejudge**（吸收 Codex）：`allusion_intertext` / `voice_register` / `prosody_compensation` 三维各 3 次而非 10 次，避免维度全 10 次成本爆炸

**伪代码**：

```python
def final_gemba_aggregate(source, candidate, runs=10, profile="literary"):
    penalties = []
    annotations = []
    for seed in range(runs):
        report = gemba_judge(source, candidate, seed=seed,
                             weights="25/5/1/0.1", profile=profile)
        penalties.append(report["penalty_per_1000"])
        annotations.append(report["errors"])
    kept = sigma_filter(penalties, k=2.0)            # 2σ 离群剔除
    return {
        "penalty_per_1000": rrwa(kept),               # RRWA 聚合
        "raw_runs": penalties,
        "kept_runs": kept,
        "merged_errors": merge_error_spans(annotations)
    }
```

**成本估算**（小D 评审）：3000 字源文 × 10 次 ≈ 20K token × 10 = 200K token；按 DeepSeek API 计价 ≈ ¥1.5 / 轮，可接受。

#### 3.10 Best-Worst Scaling 全对全比较

**底层逻辑**：哈基米报告实测 Likert 5 点量表在文学翻译评估中导致 ~60% 误判率（学生评估者将 60% 人翻译标为机翻），原因是 Likert 中间值模糊 + 锚定效应。**Best-Worst Scaling (BWS)** 通过强制评估者在多选项中选"最好"和"最差"提升信号区分度。

**实施方式**（路径 B 全对全，吸收小D 推荐）：

- 接力链每轮产生 5 个候选版本：CLI/API 为 V1 哈士奇 / V2 小D / V3 CC / V4 逗比 / V5 Codex conductor；默认 Web Relay 为 V1 哈基米 / V2 老D / V3 小克 / V4 包子 / V5 小G。
- 最终回合 CC 执行 **C(5,2) = 10 对两两比较**：每对问"这两个版本，哪个质量更好？"
- 收集 10 次二选一结果，按胜场数排序：Q_j = win_j / Σ win_k × 100
- 平局计 0.5；胜场数 ∈ [0, 4]

**双轨制**（与 §3.9 RRWA 互补）：
- §3.9 RRWA 给绝对分（penalty_per_1000）
- §3.10 BWS 给相对排序 + 一致性审计

**为什么不用路径 A 增量 BWS**（仅相邻棒次比较）：会有传递性错误（V1 vs V2 / V2 vs V3 但 V1 vs V3 从未直接比较），全局排序可能不一致。

**成本**：10 次比较 × 200 token ≈ 2K token，相对 §3.9 可忽略。

#### 3.11 TREQA 阅读理解外部评估

**底层逻辑**：哈基米 gap analysis 指出 TREQA（Translation Evaluation via Question-Answering）是后 GEMBA 时代最核心的 extrinsic 评估范式——**不直接评译文质量，而是测试译文能否让目标读者完成针对原文的核心理解任务**。如果译文 flatten 了某个 nuance / 抹掉某个隐含 metaphor，answering model 读译文就答不出来；这是文学翻译"质量是否真到位"最硬的实证。

**实施 schema**（吸收 Codex 评审）：

| 角色 | 职责 | 模型 |
|---|---|---|
| **Question Generator** | 基于源文本生成 5 题，**只看 source / gold reference 不看 candidate**（避免污染） | 独立 evaluator agent，建议哈基米 Web 或外部 LLM；**不能由首棒生成**（首棒会把自己理解偏差注入题集） |
| **Answering Model** | 仅看 candidate 译文回答 5 题 | 独立 LLM（避免与 Question Generator 同模型导致循环） |
| **Grader** | 比较 gold answer vs predicted answer | 三段式：exact match → semantic similarity → LLM-as-judge |

**5 题能力槽**（固定配比，吸收 Codex 设计）：

| 能力槽 | 测试什么 |
|---|---|
| `literal_fact` | 译文是否保留了原文的具体事实（人物名、时间、地点、动作）|
| `long_dependency` | 译文是否保留了跨句长程依赖（前文铺垫与后文呼应）|
| `implicit_causality` | 译文是否保留了隐含因果关系（连接词被原文省略时）|
| `character_relation` | 译文是否保留了人物/角色之间的关系（从属、对立、亲疏）|
| `metaphor_allusion` | 译文是否保留了核心隐喻 / 典故 / 双关层级 |

**JSON 输出**（嵌入 §3.2 `cultural.reader_reachability`）：

```json
{
  "dimension_id": "reader_reachability",
  "method": "external_task",
  "questions": [
    {
      "question": "...",
      "target_capability": "metaphor_allusion",
      "gold_answer": "...",
      "predicted_answer": "...",
      "score": 0-1,
      "judge_rationale": "..."
    },
    ... // 共 5 题
  ],
  "accuracy": <0-1>,        // 5 题平均分
  "confidence": <0-1>
}
```

**Grader 三段式打分**（吸收 Codex）：

```python
def grade_answer(gold, predicted, capability):
    if capability == "literal_fact" and normalize(gold) == normalize(predicted):
        return 1.0                                    # exact match
    sim = semantic_similarity(gold, predicted)        # embedding 廉价预筛
    if sim >= 0.88: return 1.0
    if sim <= 0.55: return 0.0
    return llm_judge_score({                           # 边界样本交 judge
        "gold_answer": gold,
        "predicted_answer": predicted,
        "rubric": "Score 0..1 for semantic equivalence. Ignore style."
    })
```

**触发场景**：长文本 / 文学翻译最终验收**建议必填**；技术文档 / 短文本可选；Step 1 brief 字段 `requires_reader_reachability` 控制。长文本可分 chunk，每 chunk 5 题（不是全文只 5 题）。

**成本估算**：5 题生成 + 5 题回答 + 5 题打分 ≈ 5K token，小成本。

### Step 4 — 用户 checkpoint

**触发条件**（叠加不替代）:
1. **每轮 5 棒结束**（Codex-led workflow CLI/API: 哈士奇→小D→CC→逗比→Codex conductor；默认 Web: 哈基米→老D→小克→包子→小G）— v0.3.2 新增，**轮，不是棒**
2. **收敛触发**（边际改进趋近 0 + 用户主观满意 + 待调研清单确认；硬阈值场景仍走滑动窗口"连续 3 名满意"）
3. **满 8 轮未收敛主动建议**（沿用 §3.6）

Codex conductor 在每轮第 5 棒完成并 raw/round archive 合格后**必须主动停下来**等用户 checkpoint，不再凭"是否收敛"判断；中间棒次（轮内）静默串接。

**每 2 轮发散分析**:
- 每跑完 2 轮（10 棒），Codex conductor 必须出一次「发散原因分析」：
  - (i) 5 大反复争议点候选轨迹横向对比
  - (ii) 归类到 4 类根本困境（如：源/目标语义颗粒度差 / 典故压缩 vs 句法展开 / ambiguity 是诗意 / 学界两派分歧）
  - (iii) 标注哪些可调研、哪些是不可调和、哪些需用户确认
- **R2/R4/R6/...** 偶数轮末尾出分析；**R1/R3/R5/...** 奇数轮仅 checkpoint 不出分析
- 设计意图: 2 轮恰好覆盖一个完整双循环（当前 fork 固定五棒 × 2），帮用户做 R+1 / 调研 / 收尾决策；3 轮跨度太大漏新争议，4 轮太久

**v2 落档（每轮一档，v0.3.6 改造）**:
- 派发回流走 v2 落档铁律（project convention: dispatch archives are not live-inlined in chat）：**不 inline 直播**，仅报告路径+字节+一句话核心判断
- 每棒派发回流时不另造竞争性 round archive；Web 成员 raw capture 仍必须即时落 `<relay-raw-dir>/`。待**每轮 5 棒结束**（当前 fork 固定五棒一周完毕）由 Codex conductor 合订**一档**落 `<relay-raw-dir>/YYYYMMDD-HHMMSS-translate-r{N}-{topic}.md`
- 轮档内容（按棒次顺序拼接）：
  ```
  # Round {N} — {topic}（{开始时间} → {结束时间}）

  ## 棒1 哈士奇 / 哈基米（{时间}）
  ### 点评（接 R{N-1} 末棒，R1 首棒例外）
  ...
  ### 译文
  ...
  ### 收敛探针
  penalty_per_1000: ... / quality_score: ... / pass: ... / critical_count: ... / remarks: ...

  ## 棒2 小D / 老D（{时间}）
  ...

  ## 棒3 CC / 小克（{时间}）
  ...

  ## 棒4 逗比 / 包子（{时间}）
  ...

  ## 棒5 Codex conductor / 小G（{时间}）
  ...

  ## 本轮 checkpoint 决策（用户三选一回流后 Codex conductor 补）
  ...
  ```
- **关 tab 备案闭环**：v2 命名 schema 字典序即时序，关 tab timeline 拼接协议（the public timeline-merge rule）从 relay raw captures + session timeline merge sort 自动覆盖；CC 中场讨论/决策/散原因分析 from JSONL 自动穿插到轮档之间
- **禁直落桌面**：`<translation-output-dir>/Translation.txt` 仅终版译文裸文本，轮档去 `<relay-raw-dir>/` 不留桌面根目录

**用户三选一**:
- (a) 提修改意见 → 进下一次接力
- (b) 让深度调研某个词 → 调用 **哈基米 / 小G / 包子 三家 Deep Research（Web）** 或 **scholar skill**，按题材选投；结果回流后再接力（接力链外角色，不计入 round count；详见 §6 深度调研例外段）
- (c) 表示满意 → skill 收尾出最终产出

**最终产出硬闸（2026-05-22 用户补强）**:
- Step 5 只能在以下两种状态之一发生：
  1. **连续三棒严格收敛 + checkpoint 用户表示满意**：译文文本已按 §3.5/本地硬规则达到连续三棒严格同文收敛，且用户在 checkpoint 明确表示满意、接受最终译文或要求收尾。
  2. **轮末未收敛 + 用户综合选定最满意译文**：某轮结束后仍未收敛，但用户在候选之间综合比较后，明确选择其中一版作为最满意译文，并要求以它生成最终产出。
- 仅有 `strict_consecutive_identical_count = 3`、成员建议 final、主控认为可收敛、或 round archive / handover 写出，都**不**构成 Step 5 许可。未满足上述两种状态时，主控必须停在 checkpoint，禁止写 `Translation*.txt` / `Translation-report*.md` 作为正式最终产物。

### Step 5 — 最终产出

**v0.3.3 确认（source decision）**："这些应该都是报告的内容，我要求最终的产出物是翻译 + 报告，其中翻译只留翻译就行，其他那些都是报告的内容"。Translation.txt 仅装译文裸正文，所有分析（句法/亮点/韵律）全归 Translation-report.md。

**进入条件复核**：执行本 Step 前必须先确认已满足上一节「最终产出硬闸」两种状态之一；否则只能输出 checkpoint / handover / round archive，不能生成正式最终产物。

**三类产物文件清单**:

```
<translation-output-dir>/Translation.txt                                       ← 终版译文裸文本（仅按行译文，无任何标题/分析/署名）
<translate-v2-workdir>/output/.translation-archive/   ← 历史版本（每轮终态译文存档）
<translate-v2-workdir>/output/Translation-report.md   ← 最终报告（接力轨迹+全文统计+句法构词分析+翻译亮点+音律/可诵性说明+调研待办+合规自查）
<relay-raw-dir>/YYYYMMDD-HHMMSS-translate-r{N}-{topic}.md  ← 接力轮档
<translate-v2-workdir>/relay-runs/<round>-发散原因分析.md ← R2/R4/R6 偶数轮中场发散分析报告（含句法构词分析三件套；非派发产物，专项归档保留）
```

#### 产物 1：Translation.txt

**强制 schema**：仅按行译文正文，**禁带任何**：
- ❌ 标题（如 `# 翻译结果`）
- ❌ 原文对照
- ❌ 诗题/作者署名
- ❌ 生成时间/版本号
- ❌ 任何注释/说明/分析

**示例**（《锦瑟》中→英 R3 终态）：
```
The brocaded zither: fifty strings, no cause.
Each string, each bridge, recalls the flowering years.
Zhuang Zhou at dawn was lost in a butterfly dream;
The banished Emperor Wang entrusted his spring heart to the cuckoo.
Pearls are tears in moonlight on the vast sea;
At Lantian, sun-warmed jade gives rise to mist.
Need this feeling wait to become a memory?
Only, even then, I was already bewildered.
```

设计意图：**职责分离**——译文是直接给读者用（粘贴/打印/朗诵），分析是给用户复盘用，两者读者+用途+格式都不同；混在一起破坏译文文本纯净性。

#### 产物 2：Translation-report.md

**强制 schema**（七段，第 4 段为 v0.3.3 新增强制）:

```markdown
## 完整用户输入与译前上下文

### 用户原始输入（完整）
### 译前上下文包摘要（若为《古董局中局》且使用小D，必须含小D译前上下文包摘要版）
### 输入边界（上下文不是待译正文；不得增写解释性设定）

## Segment 全文（接力轨迹）

### 原文 / 作者参考样本（如有）/ 首棒机翻参考底稿（仅 R1 触发）/ 运行通道 / 接力轨迹（按棒次表）/ 收敛点 / Final / Rationale

## 句法构词分析

> **颗粒度硬门槛（current rule）**：本段不得只写三件套标题或摘要。短文本也必须逐句、逐短语拆开；助词、敬语、时态/体貌、连接形、名词化、指示词、机构/人物称谓、信息密度转换点必须逐项说明。最低强度不得低于 `20260514-215234-tanaka-jp-Translation-report.md` §八。

### 逐句总览
| # | 译句 | 按目标语结构近似直译 | 对应原文 | 一句话判断 |

### 逐短语 / 助词 / 敬语拆解
| 句号 | 译文片段 | 构词/语法 | 字面意思 | 对应原文 | 功能说明 | 信息密度判断 |

### 依存句法树（按行 JSON）
{ "L1": { "root": "...", "modifiers": ["..."], "source_alignment": ["..."] }, "L2": {...}, ... }

### 关键实词形态分析
| 行 | 词形 | lemma/构词 | 形态 | 原文锚点 | 采用理由 | 风险 |

### 翻译策略标记
| 策略 | 应用行/片段 | 直译或转换 | 是否增密 | 红线核查 | 说明 |

### 直译与转换总核查
- Addition / Omission / Free Rewriting / 信息密度四项逐条核查。
- 明确哪些是目标语必要转换，哪些不是背景扩写。
- 明确本次体裁契约下哪些句法/语气/节奏再创作属于有锚点转换，而不是
  无依据自由改写；不得把"表面不直译"本身当作错误。

## 翻译亮点（3-5 条）

## 音律 / 可诵性说明（按 sound_contract 触发；朴素专业文本可写 N/A）

### 句长设计 / 停顿与重音 / 押韵或头韵策略 / 顶针或重复结构 / 牺牲点清单
（押韵评级约束：默认"能则押"下信息影响只能为 none/low；medium/high 仅允许在用户显式"必押"且告知风险时出现）

## 全文统计

### Severity 分布 / Accuracy 红线触发统计 / 高频错误维度 Top 3 / 术语争议清单（glossary 漂移检测）

## 调研待办（移交后续 Rx+ 或独立调研使用）

## 圣经合规自查（spec §6 自查清单）
```

#### 产物 3：中场发散分析报告（R2/R4/R6/... 偶数轮末尾，v0.3.3 强制句法构词分析段）

**强制 schema**:

```markdown
## R<x> 接力链速览（5 棒成员/渠道/sat/sev/关键贡献表）

## 5 大反复争议点候选轨迹横向对比

| 争议点 | R1 | R2 | ... | R<x> | 学界分歧 | 收敛方向 |

## 4 类根本困境归类

| 困境类型 | 涉及争议点 | 是否可调研 / 不可调和 / 需用户确认 |

## 候选轨迹收敛 vs 发散判定

## 句法构词分析

> **颗粒度硬门槛（current rule）**：发散分析、收敛 checkpoint 轮档、最终报告使用同一最低强度。若 RxB1 提前收敛，只分析触发收敛的候选，但仍要完整写逐句总览、逐短语拆解、依存骨架、关键实词形态、策略标记、直译/转换总核查六项。

### 逐句总览表
### 逐短语 / 助词 / 敬语拆解表
### 依存句法树（按行 JSON）
### 关键实词形态分析表
### 翻译策略标记表
### 直译与转换总核查
- 必须区分"受约束二次创作"与"无锚点自由改写"：前者可作为亮点或
  必要转换，后者按 Free Rewriting / Addition / Omission 处理。

## 用户 checkpoint 三选一建议
- (a) 提修改意见 → R<x+1> 接力
- (b) 让深度调研某词 → 哈基米/小G/包子 三家 Web Deep Research 或 scholar skill
- (c) 表示满意 → skill 收尾出最终产出
```

**v0.3.3 强制理由（source decision）**："少了句法构词分析。你以后中场的发散分析报告也要加句法构词分析"。底层逻辑：句法构词分析是评判译文质量的客观锚点（vs 主观意会），少了它发散分析报告就只剩争议点列举和困境归类，**评判译文是否合理无落脚点**；中场发散分析报告同样需要这层锚点，5 大争议点 + 4 类根本困境讨论才有句法依据。

**翻译报告**（v0.3 借鉴 openlrc QA report schema，仅 schema 不拷音频流程；v0.3.2 棒次表头改）:
```markdown
## Segment #N
**原文**: ...
**作者参考样本**: <Step 1 第 7 项；未提供则 not_provided>
**首棒机翻参考底稿**: <Step 1 第 8 项 Google/DeepL 底稿>
**运行通道**: <CLI 端接力 / 网页版接力；如中途用户显式改道，列运行通道变更记录>
**接力轨迹**:
- 哈士奇 (棒1): <审核+润色版译文>
- 小D (棒2): <点评 JSON + 润色版>
- CC / 小克 (棒3): <点评 JSON + 润色版>
- 逗比 / 包子 (棒4): <点评 JSON + 润色版>
- Codex conductor / 小G (棒5): <点评 JSON + 润色版 / 主控综合>
- ...
**收敛点**: 棒N→N+2 三连满意（硬阈值场景） / 边际改进趋近 0 + 用户主观满意（软阈值场景）
**Final**: <最终译文>
**Rationale**: <为什么这样定>

## 全文统计（v0.3 新增）
- severity 分布: critical X / high Y / medium Z / low W
- Accuracy 红线触发统计: Addition A / Omission O / Mistranslation M / Hallucination H
- 高频错误维度 Top 3
- 术语争议清单（glossary 漂移检测）
```

## 3. 大文件嵌套（v0.2 同款，glossary 注入策略守圣经）

**触发条件**: 转换后纯文本超过单棒 token 安全阈值（建议 > 8k token 或 > 15 页）。

**拆分原则**:
- 边界走 **H1/H2 章节**，禁止字数硬切（避免拦腰斩段落）
- 拆出 chunk A / B / C / ……

**嵌套流程**:
```
Step 2 转换+拆分 → A 串行接力 → 用户对 A 打回/满意循环 → A 满意
                  → B 串行接力 → 用户对 B 打回/满意循环 → B 满意
                  → ……
                  → 全部章节满意 → Step 5 拼回出终版
```

**跨章节一致性**:
- 复用旧版 §10 **Consistency Guard** 模块
- A 章满意后，提取术语/人名/地名映射表
- **强制注入 B 章每棒 prompt 顶部**（v0.3 守圣经，驳"仅注首棒"规则；防漂移机制走 CC 派发时按段落相关性筛选 + 长度控制，不靠少注入）

**断点续跑**（v0.3 借鉴 llm-subtrans MIT）:
- 每章节开始前写 checkpoint 行: `file/chapter/segment/current_baton/index/version_hash`
- 崩溃恢复时从最后 checkpoint 行继续
- 状态字典走 SQLite/JSON 持久化（沿用 v0.2 §6 第 4 项）

## 4. 白板转发协议

**严禁**: 把所有历史一股脑发给下一棒成员。

**每棒派发 prompt 严格四段**:
1. **前情提要**（≤ 200 字）— CC 压缩本轮之前的接力情况
2. **上两棒（N-2）完整译文 + 完整点评**
3. **上一棒（N-1）完整译文**
4. **上一棒（N-1）完整点评**（R1 第 1 棒哈士奇跳过此段）

**运行通道适用范围**：
- CLI 端接力与网页版接力使用同一四段式派发协议；网页版只改变"发送到哪个 Web 端"，不改变 prompt 内容与上下文窗口。
- Web Relay Mode 下，主控可以把每棒 prompt 写入 `<relay-prompt-scratch>` 或 round archive 的对应段，供用户/浏览器中继；回流结果必须粘回主控并纳入同一轮档。
- 若 Web UI 需要拆分长 prompt，拆分边界只能在"前情提要 / N-2 / N-1 / 评分 schema"等结构边界处；译文正文不得截断丢失。

**v0.3.10 上下文窗口扩展底层逻辑**:
- 单棒上下文（N-1）易导致"漂"——每棒对前一棒的过度反应（修正过度 / 风格回弹 / 决议遗忘 / catalyst 信号衰减）
- 双棒上下文（N-2 + N-1）让当前棒能识别(a) 上一棒是修正还是回弹 (b) 跨棒争议点是否已稳定 (c) 主审 catalyst 是否被中间棒吞掉
- N=3（含当前棒）边际收益最大；N=4 prompt 长度膨胀显著但收益递减

**token 节流**: 若 N-2 + N-1 累计 > 5000 字符，prompt 顶部加压缩元数据头部"上两棒接力上下文（N-2 是 [成员 A 译文+点评]，N-1 是 [成员 B 译文+点评]）"，CC 视情况对 N-2 点评做 ≤300 字摘要（**译文不摘要保全文**）。

**跳过场景一览**:
| 棒次 | N-2 段 | N-1 段 | 说明 |
|---|---|---|---|
| R1 第 1 棒哈士奇 | 跳过 | 跳过 | 首棒例外，无前序棒；只给原文 + 双版（或单版）机翻 + §3.1 原则 + §3.2 标尺 |
| R1 第 2 棒（小D）| **给（哈士奇选优胜版机翻 + 哈士奇对该版的 14 维点评）** | 给（哈士奇润色版 + 哈士奇润色 diff 三层点评） | v0.3.10 终态：N-2 段不再跳过；落选版机翻进前情提要段 |
| R1 第 3+ 棒 | 给 | 给 | 标准四段式 |
| Rx 续轮哈士奇起头棒 | 给（Rx-1 倒数第 2 棒）| 给（Rx-1 末棒；CLI/API 为 Codex conductor，Web 为小G）| 续轮按普通棒次四段式 |
| Rx 续轮第 2 棒 | 给（Rx 第 1 棒 = Rx-1 末棒候选）| 给（Rx 第 1 棒 = 哈士奇）| 标准四段式 |

**首棒哈士奇例外**:
- 严格指 **R1 第 1 棒哈士奇**（接力链最起头，全新翻译任务的首跑棒）
- 不发前情提要、不发 N-2 段、不发 N-1 段（无前一棒）
- 直接给：(1) 原文 (2) **作者参考样本**（Step 1 第 7 项；若用户提供则附上，未提供写 not_provided 且不追问）(3) **首棒机翻参考底稿**（Step 1 第 8 项；DeepL 收录目标语种 → Google + DeepL 双版；DeepL 未收录 → Google 单版）(4) **§3.1 翻译原则**（生成时方向盘，每棒 prompt 顶部固化）+ **§3.2 14 维评分 schema**（事后检验标尺，每棒 prompt 底部固化）+ 用户特殊要求 + 当前章节 glossary（若大文件嵌套）
- **哈士奇五步动作流**：
  1. **双版评分（用 §3.2 14 维标尺）**：对 Google 版跑 14 维评分得 `S_norm_google + issue 列表`；对 DeepL 版跑同样评分得 `S_norm_deepl + issue 列表`（DeepL 缺位则跳过比较直接选 Google，五步退化为四步）
  2. **选优**：S_norm 更小者 = 选优胜版作"润色入口"
  3. **润色（用 §3.1 翻译原则方法论）**：在选优胜版基础上，按"信达雅 + 受约束二次创作 + 体裁路由 + 三红线 + 场域分级"做 diff 决策，产出哈士奇润色版译文
  4. **润色版自评（用 §3.2 14 维标尺）**：对自家润色版再跑一次 14 维评分 → 进 §3.4 收敛探针
  5. **点评段输出三层**：(a) 双版 14 维评分对照（§3.2 标尺产出的客观数据）(b) 选优理由（哪几个维度差异最大）(c) 润色 diff 决策点（按 §3.1 方法论说明哪些信达雅取舍）
- **职能切开铁律**（与 §3.0 联动）：哈士奇选优用 §3.2 评分标尺（量化对比），润色用 §3.1 翻译原则（方法论方向），二者每棒同步使用、不互替——这是 §3.0 翻译原则 vs 评分标尺职能切开机制最干净的端到端实证；不允许无锚点整段重写式意译，三红线照守；KPI 底线: 输出译文 §3.4-bis 评估 ≤ DeepL × 1.1
- **下棒衔接**（修复 v0.3.10 中段定稿"R1 第 2 棒 N-2 跳过"歧义）：选优胜版机翻 = R1 第 2 棒小D 的 N-2 段（含完整译文 + 哈士奇对该版的 §3.2 14 维点评）；R1 第 2 棒 N-2 段**不再跳过**；落选版机翻 = R1 第 2 棒前情提要段（≤200 字 by CC 压缩——含落选版关键差异点 + 落选版到选优版的工作流轨迹），按"其他棒次历史发言"协议处理，不弃

**末棒 / conductor 例外**:
- 在 Codex-led workflow 中，CLI/API 末棒与 conductor 是 **Codex conductor**；Web Relay Mode 的第五普通接力棒是 **小G**，但 Codex conductor 仍负责全局观察、归档、checkpoint、发散分析、最终裁判和报告。
- **不受 N=3 滑窗限制** — Codex conductor 的输入范围是本轮 R 内 5 棒全员译文 + 全员点评 + 跨轮已锁定决议 + 主审 catalyst 全部记录。
- 角色定位：全局观察 + 漂检测者。N-2 漂模式（修正过度 / 风格回弹 / 决议遗忘 / catalyst 衰减）当本轮跨多棒发生时，由 Codex conductor 在末棒/轮末主动捕获并写入"发散原因分析"段（R2/R4/R6 偶数轮）。
- 四段式滑窗仍适用于普通中间棒；Codex conductor 做轮末综合、报告和最终裁判时必须纵览全员，不得只看前两棒。
- Codex conductor 输出仍走 §Step 5 三类产物 schema（Translation.txt 裸译文 / Translation-report.md 最终报告 / R2/R4/R6 中场发散原因分析）。

**Rx+ 续轮哈士奇起头棒**:
- R2/R3/Rx+ 续轮的哈士奇起头棒**不套首棒例外**
- 按普通棒次四段式派发：(1) 前情提要 ≤200 字（含 R2 沉淀铁律 + 已锁定决议 + 前序轮关键变更）(2) **上两棒（Rx-1 倒数第 2 棒 = CLI/API 第 4 棒逗比；Web 第 4 棒包子）完整译文 + 完整点评** (3) 上一棒（Rx-1 末棒；CLI/API 为 Codex conductor，Web 为小G）完整译文 (4) 上一棒完整点评
- 首棒机翻参考底稿是 **R1 首跑专用**，续轮不重新出机翻（Rx-1 末棒候选已是更厚底稿）

**PUA 运行策略**（2026-05-14 用户确认）:

- translate-v2 不做全局 PUA 开关管理。
- Codex 自身 PUA 默认状态由 Codex 侧运行配置决定。
- 其他成员沿用各自默认状态；translate-v2 不统一改写。
- 若未来某个具体成员在具体文本上因 PUA 旁白造成输出质量或通道问题，只按该成员/该通道做局部处置。

## 5. 成员配置

| 成员 | 渠道 | 入选 | 备注 |
|---|---|---|---|
| **哈士奇** | **`ask_husky` / Antigravity CLI bridge** | ✅ 首棒 | v0.3.2 替代哈基米首棒位置；CLI 端接力通过当前 Codex workflow 的哈士奇桥接通道执行 |
| 小D | DeepSeek API（默认）/ cc-deepseek 借壳 tab（重任务） | ✅ 第 2 棒 | |
| CC | Claude Code CLI / `ask_cc` | ✅ 第 3 棒 | Codex-led workflow 第 3 棒；若 `ask_cc` 不可用，作为基础设施 blocker 报告，不得静默替换 |
| **逗比** | **`ask_doubi` MCP**（doubao-seed-2-0-pro-260215） | ✅ **第 4 棒** | v0.3.4 转正：(1) MCP 直调零中继零粘贴吻合 SKILL 代码化前提；(2) project capacity evidence 已通过 23kB 输入+7k 输出深度评审压力测试，引用 9/10 真实；(3) 中文长尾资源池；早期"信任度未建"风险已退场 |
| Codex conductor | Codex 主线程 | ✅ 第 5 棒 / 主控 | CLI 模式下承担第 5 棒审稿与轮末综合；Web Relay Mode 下不替代小G普通第五棒，但仍负责主控、落档、checkpoint、发散分析和最终报告 |
| 小K | cc-kimi 借壳 tab（私聊场景）/ ask_xiaok 纯 API（快任务）| ⏸ **接力链已退场** | 退场理由：(a) 借壳 tab 需用户切 tab 拷文件，阻塞 SKILL 自动化；(b) 锦瑟 R1+R2 三红线复发（grief Mistranslation / banished king Addition / lost and far astray Addition）历史包袱重；(c) R3 借壳 tab 虽未复发但样本仅 1，逗比已通过更扎实压力测试。**借壳 tab 私聊场景仍保留**（用户主动派遣 cc-kimi 写代码/讨论场景），不退出团队 |
| **哈基米** | **Gemini Web 普通聊天 / "深度研究"** | ⚠️/✅ | CLI 主链中仅 §6 Step 4 (b) 深度调研角色；默认 Web Relay Mode 中作为第 1 棒普通接力。Deep Research 只在用户显式触发 §6 调研时使用 |
| **小G** | **ChatGPT Web "深度研究"**（CLI 主链外，2026-04-30 新增）/ ChatGPT Web 普通聊天（Web Relay Mode） | ⚠️/✅ | CLI 主链中仅 §6 Step 4 (b) 深度调研角色；若用户指定 Web Relay Mode，则按 §3.12 作为 Codex-led workflow 的第 5 棒普通接力输出者。普通接力不自动开深研；合并落档、发散分析、最终报告仍由 Codex conductor 负责 |
| **包子** | **Doubao Web 普通聊天 / "深入研究"** | ⚠️/✅ | CLI 主链中仅 §6 Step 4 (b) 深度调研角色；默认 Web Relay Mode 中作为第 4 棒普通接力。与逗比 API 通道是两条独立路径，调研用 Web 深研 / 接力用 Web 普通聊天 / API 接力三者不混用 |

**v0.3.12 运行通道映射补充**：
- CLI 端接力：使用上表 ✅ 成员的 CLI/API/MCP 渠道。
- 网页版接力：Codex-led workflow 按本地 `SKILL.md` 拓扑映射为 **哈基米 / 老D / 小克 / 包子 / 小G**，其中小G承担 Web 链第五普通接力棒，Codex conductor 只保留主控、落档、分析与报告职责。上游 CC 侧旧映射不得用于新任务。
- 同一任务内不得混跑，除非用户显式说"这一棒临时用网页/CLI 替换"；临时替换必须写入 round archive 的"运行通道变更记录"。
- "深度研究/深入研究"按钮仍只属于 §6 调研节点；普通 Web Relay Mode 用常规聊天接力，不自动开深研。

**敏感词降级**（沿用旧版 §9 + v0.3.1 收紧 + v0.3.2 主链替换）:
- 启动时强制询问"是否含敏感话题"
- 勾 yes → **启动前重配置链路**（不是运行中跳棒）：剔除国内 AI（小D/逗比，v0.3.4 改：原"小D/小K"，因 v0.3.4 第 4 棒已切逗比，逗比同样属国内 AI 政审风险），Codex-led workflow 默认降级为 **哈士奇→CC→Codex conductor→哈士奇→……（3 人循环）**；若走 Web Relay，则按敏感话题规则跳过国内 Web 端并在 checkpoint 让用户确认替代链。
- 运行中某成员被屏 → 先尝试同成员学术转述模式 / 渠道容灾（§3.7）；仍失败则触发 §3.7 例外，**走用户 checkpoint 决定是否临时剔除该成员**（不擅自跳棒，守 §1 铁律 3）

## 6. 复用旧版的 13 项严谨性特性

1. §2 优先级层级: 安全政策 > 用户特殊要求 > 上下文一致性 > 风格模板
2. §3 输出 schema 强制（空字段触发自动重试）
3. §10.1 Chunker → 升级为 Chapter Splitter（H1/H2 边界）
4. §10.2 Checkpoint（SQLite/JSON 持久化，崩溃可恢复）
5. §10.3 Domain Router（自动检测 + 启动时 1 秒确认）
6. §10.4 **Consistency Guard**（跨章节，glossary 强制注入 B 章每棒 prompt 顶部）
7. §10.5 Diff 渲染（每次接力 vs 上一棒高亮差异）
8. §11 冷门语种"年代-方言"坐标系
9. §12 编码标准化（变体假名 / 训读返点）
10. §13 七域 glossary（按 Domain 自动注入；v0.3.1 注：本项即 §10.1 引用的"§6 列表第 10 项 / 旧版 §13"，对账消歧）
11. §14 自检清单（完整性/准确性/流畅度）
12. §6 哈基米深度调研回流（Step 4 (b) 触发）
13. §8 争议词调研（每棒可提名，回流到下一次接力 prompt 顶部）

## 7. 与 v0.2 的差异

| 维度 | v0.2 | v0.3 |
|---|---|---|
| 翻译原则段 | 4 行抽象（"信达雅+直译为主+禁脑补禁省略"）| 4 段细化（底线 + 场域分级 + 三红线 + 结构性约束）+ 玉粗鬆症修辞构词例 |
| 审核尺度 | "MQM 6 维做自查工具，不强制每条都列"（模糊）| MAATS/MQM 6 维 JSON schema 落地（Style 改定义"直译永不算错"）|
| 点评模板 | 无固定模板 | MAD 四要素（位置/理由/证据/替代） |
| 收敛字段 | 议题 #2 ⚠️ 未决 | satisfaction + severity + remarks 探针 + 滑动窗口计票 |
| 轮次上限 | 无 | 无（守铁律），满 8 轮 CC 提示用户介入但可继续 |
| API 容灾 | 无 | retry/429 + provider fallback（仅渠道容灾） |
| GitHub 借鉴 | §6 13 项特性提及但无嫁接表 | §10 完整嫁接矩阵（5 项嫁接 + License 弃用清单） |
| 玉粗鬆症例 | 无 | §3.1 收录作"修辞构词对等映射"示范 |
| 韵文体裁 | 无（古诗词/歌词/Rap 等无专门规约）| Step 1 第 6 项「韵律要求」+ §3.1 韵文档三优先级（节奏感>字面精度>押韵）+ Step 5 Translation.txt「韵律说明」段（仅韵文触发）|

## 8. 路线图（v0.2 同款，工时不进 spec 正文）

| Phase | 范围 | 验收 |
|---|---|---|
| Phase 0 | spec v0.3 用户审稿 | ✅ 已确认（2026-04-28） |
| Phase 1 | 串行接力链 + 用户 checkpoint，纯文本输入 | 短文 1 篇端到端 |
| Phase 2 | Step 2 格式转换接入 pdf/docx skill + xunbu converter | .pdf / .docx 各 1 篇 |
| Phase 3 | 大文件嵌套 + Consistency Guard + llm-subtrans 断点续跑 | 30 页文档章节嵌套 |
| Phase 4 | 翻译报告（含 openlrc schema 增强）+ 深度调研回流 | 用户拿 .md trace |
| Phase 5 | 性能优化（缓存 / 并发评估 / 状态恢复） | 长文档可接受时间 |

工时估算落到独立文件 `implementation-notes.md`，不进 spec 正文（避免把估时当承诺）。

## 9. 议题进展（2026-04-28 R-真1 审查后确认，v0.3.2 部分已被新规约覆盖）

> ⚠️ v0.3.2 注：第 1、4 项的"哈基米首棒"已被 v0.3.2 接力链全替换覆盖，下表保留作历史，**实际生效以 §0/§3/§5 v0.3.2 改动为准**。

1. **哈基米 Web 中继自动化**：✅ 确认（v0.3）→ ⚠️ 已被当前 Codex-led workflow 覆盖——CLI 首棒走 `ask_husky` / Antigravity CLI bridge；默认 Web Relay 首棒走哈基米普通聊天；Deep Research 仍只属于 §6 调研节点
2. **"连续 3 名满意"判断**：✅ 确认（v0.3 §3.4-3.6）→ ⚠️ v0.3.2 软化——文学翻译走"边际改进趋近 0 + 用户主观满意 + 待调研清单确认"软阈值；技术文档走原硬阈值
3. **Step 4 (b) 深度调研回流位置**：✅ 确认——用户自行判断打回/收尾
4. **Codex/CC 同质化**：✅ 确认（v0.3）→ ⚠️ 已被当前 Codex-led workflow 覆盖——当前 CLI/API 链为哈士奇→小D→CC→逗比→Codex conductor，默认 Web 链为哈基米→老D→小克→包子→小G

## 10. GitHub 借鉴方案（v0.3 新增，R-真1 审查后定稿）

### 10.1 嫁接矩阵（5 项 P0/P1/P2）

| 项目 | License | 借鉴模块 | 嫁接节点 | 优先级 |
|---|---|---|---|---|
| **MAATS** | 当前 GitHub API 未识别 LICENSE（2026-06-30 复核） | MQM 风格 prompt / schema 设计参考；不拷代码，license 未确认前不作为可嫁接代码来源 | Step 3 §3.2 每棒 system prompt 底部 | **P0 design reference** |
| **xunbu/docutranslate** | MPL-2.0 | **仅 converter 层**（纯文件 IO 管道，无 HTTP，不引用 translator/workflow/exporter）| Step 2 全格式管道 + §6 列表第 10 项（旧版 §13）七域 glossary 双链路 | **P0** |
| **machinewrapped/llm-subtrans** | MIT | ① 断点续跑状态字典 ② retry/429 处理 ③ provider 插件架构 | §3 大文件嵌套断点 + Step 3 §3.7 API 调用层容灾 | **P1** |
| **Skytliang/Multi-Agents-Debate** | GPL-3.0（2026-06-30 复核） | 仅概念参考四要素点评模板（位置/理由/证据/替代），**不拷代码/文本**，弃 Devil/Angel/Judge 角色 | Step 3 §3.3 每棒 system prompt 点评段开头 | **P1 concept only** |
| **zh-plus/openlrc** | MIT | QA report 数据 schema（severity 分布 / Accuracy 红线统计 / 术语争议清单）| Step 5 Translation-report.md 增强（仅 schema 不拷音频流程）| **P2** |
| `nicepkg/gpt-runner` | MIT | — | **作对照不嫁接**（用户确认，Playwright MCP 路线放弃）| — |

### 10.2 License 弃用清单（红线）

| 项目 | License | 处理 |
|---|---|---|
| omegat-plugin-openai-translate | **GPLv2** | 仅看 API surface，不可拷代码 |
| Koharu | **GPL-3.0** | 仅看 CJK 视觉排版思路，不可拷代码 |
| BabelDOC | **AGPL-3.0** | 仅参考 PDF 布局保真思路，不可拷代码 |
| PDFMathTranslate | **AGPL-3.0** | 仅参考 PDF 多 provider 思路，不可拷代码 |

### 10.3 待考清单（License 未见，谨慎引用）

| 项目 | 状态 | 处理 |
|---|---|---|
| HiMATE | 未见 LICENSE ⚠️ | 暂仅参考 MQM Tier-1/Tier-2 思路，不拷代码 |
| M-MAD | 未见 LICENSE ⚠️ | 暂仅参考 Stage1 维度切分思路，不拷代码 |
| **DITING** | MIT (仅 README) ⚠️ + R3 实测虚假宣传 | **确定弃用**（三槽硬编码 + 虚假"6 维共享内存池"） |

### 10.4 嫁接边界声明（防越界）

- **MPL-2.0 派生边界**: xunbu/docutranslate converter 层文件保留原 license 声明，不混入其他层代码
  · **Phase 2 前置硬闸门**：未生成 xunbu converter 文件清单、修改文件清单、原始 license/header 保留策略前，**不得拷入代码**
- **MIT 嫁接**: llm-subtrans/openlrc 拷代码或 prompt 时保留原 LICENSE 文件 + 头部署名/版权声明；MAATS license 未确认前仅作设计参考
- **GPL-3.0 concept only**: Skytliang/Multi-Agents-Debate 只保留"位置 / 理由 / 证据 / 替代"这类抽象点评结构，不拷代码、prompt 原文或角色模板
- **API surface only (GPL/AGPL)**: 仅参考接口形态、不拷代码、不混入项目

---

> **下一节点**: Phase 1 implementation（短文端到端串行接力跑通），awaiting project kickoff.
