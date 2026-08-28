# AI-first Vibe Coding Skill

![BOOMKALAKASHA 水印](assets/brand/watermark-auto.svg)

[English](README.md) · [快速开始](docs/quick-start.zh-CN.md) · [AI 操作指南](docs/ai-operation-guide.zh-CN.md) · [品牌](docs/brand.md) · [变更日志](CHANGELOG.md) · [贡献指南](CONTRIBUTING.md) · [支持](SUPPORT.md) · [安全策略](SECURITY.md)

> **让 AI 自主分工，把交付交给证据验收。**
>
> **Let AI divide the work; let evidence earn the release.**

在明确授权边界内，这个 Skill 会让 Codex 或其他编码 Agent 自主拆解目标、按需分工、完成实现与独立复核，再通过多轮迭代让证据决定是否交付。它适合服务重构、跨仓协作、长周期交付和多轮验收复盘，而不只是生成代码。

<!-- icarus-release-fact: dynamic -->
公开 GitHub Releases 状态与下载物料请查看
[最新 GitHub Release](https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases/latest)
和[完整发布记录](https://github.com/boomkalakasha/ai-first-vibe-coding-skill/releases)。
可复现安装应使用不可变标签物料；仅创建标签不能证明 Release 门禁已经通过。

## 一眼看懂：它能帮你做什么

| 你想完成的事 | 这个 Skill 怎么帮你 | 最后拿到什么 |
| --- | --- | --- |
| 把模糊目标变成可执行计划 | 先梳理结果、边界、契约、Case 和决策点，再进入编码 | 任务基线、Spec 和可追踪验收 Case |
| 把长任务交给多个 Agent | 为每个 Agent 划定写集、角色和停止条件，并按实时容量信号调整并发 | 一份统一执行台账，而不是散落的“已完成”消息 |
| 判断改动是否真的可以放行 | 分开源码、构建、运行、业务、发布和切流证据 | 带 `P0/P1` 门禁、明确未知项的放行结论 |
| 在 GitHub、GitLab 或 Jenkins 上安全交付 | 按仓库选择交付 profile，把提交、评审、标签和部署证据分开 | 可审查、可回滚、证据边界清晰的分支/MR/PR 路径 |

它尤其适合服务重构、跨仓改动、面向生产的数据链路，以及“测试通过”仍不足以回答是否可用的长周期任务。

## 60 秒路径

1. 让 Agent 宿主读取本仓库的 `SKILL.md`，或按[安装、升级、回滚与卸载指南](docs/quick-start.zh-CN.md)安装；[AI 操作指南](docs/ai-operation-guide.zh-CN.md)给出最小安全工作闭环。
2. 第一个任务先要求建立基线、用户路径、验收 Case 和最小安全写集。
3. 长周期或多 Agent 任务复制[执行台账](templates/execution-ledger.md)和[任务基线](templates/task-baseline.md)，每个 Wave 收口都重新核对容量。
4. 按下面的本地校验命令回收证据。除非在对应宿主中真实观察到行为，宿主发现或运行态仍是 `DOCUMENTED_ONLY`。

如果只是单行翻译、简单问答或纯信息查询，不必套用完整流程。

## 你会得到什么

**示意结果——以下仅展示交付格式，不代表你的仓库已经获得运行或发布证据：**

| 台账字段 | 示例结果 |
| --- | --- |
| 目标 | 拆分一个服务，同时保持既有 API 行为 |
| 工作包 | 契约、实现、独立复核、运行检查 |
| 证据 | 42 个测试通过；运行实例身份仍为 `NOT_RUN` |
| 门禁 | `P0：0 个未关闭`；`P1：0 个未关闭`；候选状态为 `STATIC_PASS_PENDING_RUNTIME` |

真正的产物不只是代码，而是一条可复核的决策链：改了什么、观察到了什么、
还有什么未知，以及为什么当前可以或不可以放行。

## 核心亮点

- 按风险从单文件修复平滑扩展到跨仓库、跨运行态交付，小任务不堆文档，大任务不省验收。
- 明确区分源码、构建、测试、运行、业务、发布、部署与切流证据。
- 保护脏工作区；建分支、提交、推送、PR、标签、发布、部署、写库、重启和清理分别管理。
- 用“需求 → 契约 → Case → 实现 → 证据 → 放行状态”避免上下文漂移。
- 支持 Controller / Implementer / Reviewer 多 Agent 协作，但不把子 Agent 的完成声明直接当作验收。
- 支持可选的 GitHub 开源迭代发版模式，同时兼容项目自行定义的 GitLab/Jenkins/客户分支规则。
- 不绑定特定模型或 IDE；没有运行证据就主动降级结论。

## 配套项目

- [Icarus AI Spring Scaffold](https://github.com/boomkalakasha/icarus-ai-spring-scaffold)：先生成可审查的 Java 17 多模块服务骨架，再交给 Agent 协作实现。
- [Icarus 开源治理](https://github.com/boomkalakasha/icarus-open-source-governance-skill)：准备开源时扫描来源与隐私风险，整理双语文档和发布证据。

## 安装

### Codex

```powershell
git clone --depth 1 https://github.com/boomkalakasha/ai-first-vibe-coding-skill.git "$env:USERPROFILE\.codex\skills\ai-first-vibe-coding"
```

这是最短的可用安装路径。重载 Codex 会话后，可显式使用
`$ai-first-vibe-coding`，也可通过匹配的研发任务描述触发。其他宿主请让
其读取 `SKILL.md`，并以 [AI 操作指南](docs/ai-operation-guide.zh-CN.md)
作为不绑定具体厂商的基础工作约定。

对于打包候选，执行 `pwsh -NoProfile -File scripts/package.ps1 -Version 1.2.2`，检查 `dist/manifest.json` 和 `dist/SHA256SUMS.txt`，再遵循宿主的安装文档。生成归档不等于 Codex 或其他宿主已经安装它。

### 其他 Agent

让宿主读取仓库根目录的 `SKILL.md`。不同宿主对目录、frontmatter 和工具映射的支持不同，请先参考[兼容性矩阵](compatibility.md)并自行运行验证，不要把“可读取 Markdown”误写成“全部能力已验证”。

## 适用示例

- “重构这个服务，保留既有行为，并证明受影响的数据链路仍然可用。”
- “复盘这个功能分支能否 1:1 替换当前服务，源码、运行态和切流分别给证据。”
- “多 Agent 分模块实现，再由独立 Reviewer 和主 Agent 验收，直到 P0/P1 清零。”
- “把内部脚手架安全适配后开源到 GitHub，不要泄露 GitLab/Jenkins/客户信息。”

## 本地验证

```powershell
python scripts/validate.py
python scripts/run_evals.py
pwsh -NoProfile -File scripts/package.ps1 -Version 1.2.2
```

验证器检查 Skill frontmatter、JSON、相对 Markdown 链接、BOM、已知内部信息模式和必要文件。它不能代替人工版权审查、完整历史 secret 扫描或真实运行态验收。

打包器只暂存一次源树，再生成 `.zip`、`.skill`、`manifest.json` 和 `SHA256SUMS.txt`。manifest 会标记源树为 `clean` 或 `dirty`；只有干净的确切 tag 包才能进入发版审查。

## 仓库结构

```text
SKILL.md                    核心路由与执行协议
references/                 详细工作流和交付 profile
templates/                  可复制的基线、台账与追踪模板
evals/                      行为与触发场景
scripts/validate.py         无第三方依赖的结构校验
scripts/package.ps1         带 SHA-256 的可重复执行打包
.github/                    公开协作、CI、安全与发版自动化
```

## Git 发版模式

- `project-defined`：以项目最近作用域内的规则为准。
- `github-open-source`：受保护 `main`、PR、SemVer tag、GitHub Release、校验和、可选来源证明和 fork 安全 CI。
- `internal-gitlab`：使用组织提供的 MR/Jenkins/客户分支规范。

GitHub Release 代表公开源码/物料发布，不等于生产部署，也不等于客户现场验收。

需要完整公开仓库就绪流程时，可在宿主实际提供时转交给可选的 `icarus-open-source-governance` companion。这里的名称只是路由提示，不代表宿主已安装；GitHub Release 也不等于仓库设置或生产部署已经核验。

## 可选品牌示例

可选的 BOOMKALAKASHA 水印和头像副本只是本地文档资产。可选的 BOOMKALAKASHA 使用不代表项目归属、支持承诺，也不授权修改个人 GitHub profile；详见[品牌说明](docs/brand.md)。

## 状态与限制

自动化检查只验证结构和确定性断言，不能证明所有 Agent 宿主都会完全一致地执行指令。当前兼容性证据见[兼容性矩阵](compatibility.md)，公开 eval 的边界见 [evals](evals/README.md)。

## 开源边界

本仓库只包含通用化方法与示例，不应提交公司制度原文、内网地址、客户标识、凭据、真实业务数据或专有复盘材料。贡献者必须确认有权按 Apache-2.0 提交对应内容。

## 许可证

Apache License 2.0。贡献者需确认拥有相应内容的公开授权，且提交不包含公司、客户或个人敏感信息。
