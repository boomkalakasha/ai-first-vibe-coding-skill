# 跨工具适配

本文件主要做命令映射，并补充跨工具交接和能力缺失时的结论降级；不能改变 `SKILL.md` 的边界、证据和复盘要求。

| 能力 | Codex | Claude Code | Cursor / Windsurf | Cline / Roo | Copilot / Gemini CLI / Qoder |
|---|---|---|---|---|---|
| 规则 | 读取 `AGENTS.md`、skill | 读取 `CLAUDE.md`、skill | 读取 `.cursor/rules` 或项目规则 | 读取 workspace rules | 读取项目 instructions / prompt rules |
| 搜索 | `rg` / `rg --files` | `rg` / built-in search | IDE search + terminal `rg` | workspace search + terminal | IDE/CLI search |
| 编辑 | patch 工具，保持编码 | edit/apply patch | IDE edit，保留 diff | workspace edit | IDE edit / patch |
| 运行态 | browser/Playwright + shell | browser/terminal | preview + terminal | browser + terminal | browser/terminal |
| 数据事实 | PostgreSQL/项目脚本 | DB client/脚本 | DB client/脚本 | DB client/脚本 | DB client/脚本 |
| 并行分工 | sub-agents（若可用） | sub-agents / tasks | worktrees/agent mode | sub-tasks | agent mode / 手动分工 |
| 交付 | Markdown + 文件链接 | Markdown + diff | PR/Markdown | task summary | PR/Markdown |

## 不同工具下的降级

- 没有子 Agent：主 Agent 依次完成研究、实现、验证，不假装并行。
- 没有浏览器：用接口、日志、DOM/静态分析和人工验证步骤替代，并明确未做视觉验证。
- 没有数据库连接：只做 SQL/脚本审计和接口验证，不给出伪造数据结论。
- 没有热部署：检查编译产物后提示人工重启，不把重启偷偷当成验证步骤。

## 完整业务研发流程的适配要求

当任务被判定为 L2（业务系统）或 L3（多轮迭代）时，任何工具都应继续使用同一套阶段和产物名称，不得因为工具界面不同而把业务分析压缩成一句“已完成”：

`应用地图与业务边界 → 详细 Spec → 用户故事与功能测试 Case → 业务角度审查 → 模块计划 → 分模块实现 → 正式业务写入路径审计 → 运行回测 → 交互/价值评估 → 优化方案 → 再迭代`

各工具至少要能承接以下信息：

| 流程产物 | 最低交接内容 | 不得丢失的判断 |
|---|---|---|
| 应用地图与边界 | 角色、对象、主链路、状态、系统边界、非目标 | 哪些能力属于当前系统，哪些必须留在人工/外部系统 |
| 详细 Spec | 字段来源、状态变迁、前置条件、异常/空态、权限、统计口径 | 业务规则是否可执行、可验证、可追溯 |
| 用户故事与 Case | 正常、空、失败、重试、重复提交、权限、上下文冲突 | 用户是否能完成任务，以及失败后能否继续 |
| 业务审查与模块计划 | P0/P1/P2、依赖、写集、回滚点、代理契约 | 先做哪条黄金链，哪些问题不能被技术实现掩盖 |
| 写入路径审计 | 页面、API、任务、回调、脚本、写入字段、策略源、人工确认 | 同一动作是否存在旁路或互相矛盾的规则 |
| 回测与评估 | 运行状态、浏览器/数据库/日志证据、交互摩擦、业务价值 | 是真的跑通、旧进程残留，还是仅静态通过 |
| 优化与下一轮 | 证据对应的改动、保留项、预期收益、复测 Case | 优化是否来自失败证据，而不是范围漂移 |

如果某个工具不具备浏览器、数据库、日志或多代理能力，应明确标记 `BLOCKED` / `NOT_RUN`，并切换到静态验证或人工补测；禁止把“无法观察”写成“已通过”。

## 工具切换时的最小协议

交接前后都应使用 `templates/handoff.md`，并在交接内容中写明：

1. 当前处于哪一阶段、哪一轮；
2. 已完成的正式产物及其路径；
3. 每条黄金链的证据等级和最新复测时间；
4. 当前实现属于 REAL、HYBRID、DEMO 还是 PLANNED；
5. 未完成项、阻塞原因、下一步只允许修改的模块/写集；
6. 下一轮必须复测的用户故事和 Case；
7. 正式状态写入路径是否已全量审计，同一动作的策略源在哪里。

这样可以让 Codex、Claude Code、Cursor 或人工开发在不同入口间切换时，继续沿用同一套业务判断，而不是重新凭印象理解项目。
