# Open-source Skill Implementation Plan
> **For agentic workers:** Execute this plan task-by-task. Use isolated subagents with review checkpoints when the host supports them.

**Goal:** 发布一份通用、安全、可验证的 AI-first Vibe Coding Skill，并建立可选 GitHub 开源发版模式。

**Architecture:** `SKILL.md` 只保留路由与执行协议；详细流程、Git 策略和多 Agent 契约放入 `references/`；可复制表格放入 `templates/`；无第三方依赖的验证与打包脚本放入 `scripts/`；GitHub Actions 复用同一脚本。

**Tech Stack:** Markdown, JSON, Python 3 standard library, PowerShell, GitHub Actions.

---

1. 建立公开治理文档、双语 README、许可证与安全边界。
2. 通用化 Skill 与 references，新增 GitHub OSS release profile。
3. 添加任务基线、执行台账、决策日志与追踪矩阵模板。
4. 先记录旧 Skill 的 GitHub 场景基线，再添加新场景与断言。
5. 实现无依赖 `validate.py` 与 `package.ps1`，确保本地和 CI 同源。
6. 添加 PR/Issue 模板、Dependabot、CI、CodeQL 与 tag release workflow。
7. 运行三轮验证、敏感信息扫描、打包和独立审查。
8. 提交、推送 `main`，创建 `v1.0.0` 与 GitHub Release；记录未启用的仓库保护设置。
