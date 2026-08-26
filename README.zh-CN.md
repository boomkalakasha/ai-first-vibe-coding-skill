# AI-first Vibe Coding Skill

![BOOMKALAKASHA 水印](assets/brand/watermark-dark.svg)

[English](README.md) · [快速开始](docs/quick-start.zh-CN.md) · [品牌](docs/brand.md) · [变更日志](CHANGELOG.md) · [贡献指南](CONTRIBUTING.md) · [支持](SUPPORT.md) · [安全策略](SECURITY.md)

一个面向真实软件交付的 AI 研发工作流 Skill：保留 vibe coding 的速度，同时补上事实链、边界、追踪、验证、复盘和发布门禁。

已公开的首个版本是 `v1.0.0`；这个 v1.1.0 功能分支是本地候选，只有 PR、CI、不可变 tag 与 GitHub Release 门禁被实际观察后才可称为公开发布。

## 60 秒路径

请使用[安装、升级、回滚与卸载指南](docs/quick-start.zh-CN.md)。打包命令只能生成本地物料与校验和；除非在对应宿主中观察到行为，宿主发现或运行态仍是 `DOCUMENTED_ONLY`。

## 核心亮点

- 按风险从单文件修复平滑扩展到跨仓库、跨运行态交付，小任务不堆文档，大任务不省验收。
- 明确区分源码、构建、测试、运行、业务、发布、部署与切流证据。
- 保护脏工作区；建分支、提交、推送、PR、标签、发布、部署、写库、重启和清理分别管理。
- 用“需求 → 契约 → Case → 实现 → 证据 → 放行状态”避免上下文漂移。
- 支持 Controller / Implementer / Reviewer 多 Agent 协作，但不把子 Agent 的完成声明直接当作验收。
- 支持可选的 GitHub 开源迭代发版模式，同时兼容项目自行定义的 GitLab/Jenkins/客户分支规则。
- 不绑定特定模型或 IDE；没有运行证据就主动降级结论。

## 安装

### Codex

```powershell
git clone https://github.com/boomkalakasha/ai-first-vibe-coding-skill.git "$env:USERPROFILE\.codex\skills\ai-first-vibe-coding"
```

重载 Codex 会话后，可显式使用 `$ai-first-vibe-coding`，也可通过匹配的研发任务描述触发。

对于打包候选，执行 `pwsh -NoProfile -File scripts/package.ps1 -Version 1.1.0`，检查 `dist/manifest.json` 和 `dist/SHA256SUMS.txt`，再遵循宿主的安装文档。生成归档不等于 Codex 或其他宿主已经安装它。

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
pwsh -NoProfile -File scripts/package.ps1 -Version 1.1.0
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

需要完整公开仓库就绪流程时，可在宿主实际提供时转交给可选的 `icarus-open-source-governance` companion。本 Skill 不声称该 companion 已安装，也不声称 GitHub 设置已经验证。

## 可选品牌示例

可选的 BOOMKALAKASHA 水印和头像副本只是本地文档资产。可选的 BOOMKALAKASHA 使用不代表项目归属、支持承诺，也不授权修改个人 GitHub profile；详见[品牌说明](docs/brand.md)。

## 状态与限制

自动化检查只验证结构和确定性断言，不能证明所有 Agent 宿主都会完全一致地执行指令。当前兼容性证据见[兼容性矩阵](compatibility.md)，公开 eval 的边界见 [evals](evals/README.md)。

## 开源边界

本仓库只包含通用化方法与示例，不应提交公司制度原文、内网地址、客户标识、凭据、真实业务数据或专有复盘材料。贡献者必须确认有权按 Apache-2.0 提交对应内容。

## 许可证

Apache License 2.0。贡献者需确认拥有相应内容的公开授权，且提交不包含公司、客户或个人敏感信息。
