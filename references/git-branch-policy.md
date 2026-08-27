# 前后端 Git 分支与交付规范

来源：`前后端分支管理规范.docx`（2025-10-15）。当仓库另有更严格的 `AGENTS.md` 或用户明确的临时授权时，以更严格或更具体的要求为准，并记录差异。本文件默认对应 `internal-gitlab`；公开 GitHub 仓库可显式启用 [GitHub 开源迭代发版模式](github-open-source-release-profile.md)，但不得借此覆盖内部客户分支和 Jenkins/现场交付规范。

## Delivery profile 选择

| Profile | 启用条件 | 合作/发版事实源 |
|---|---|---|
| `internal-gitlab` | 现有内部 remote、仓库规则或用户明确指定 | GitLab Issue/MR、Jenkins、内部 tag、客户交付记录 |
| `github-open-source` | 仓库 `AGENTS.md`、公开 GitHub remote 或用户明确要求开源发版 | GitHub Issue/PR、required checks、SemVer tag、GitHub Release |

只根据 remote 猜测但会产生 push/tag/release 等外部副作用时，必须先停在副作用前确认。两种 profile 可以在 upstream/downstream 架构中并存，但同一个 tag、部署目标或制品发布只能有一个明确执行者。

## 分支

| 类型 | 命名 | 用途与来源 |
|---|---|---|
| 稳定分支 | `main` | 可发布产品代码；受保护，禁止直接推送，只能经 MR 合并。 |
| 功能分支 | `feat-#<Issue编号>-<简短_描述>` | 从最新 `main` 创建；同一语义用 `_`，不同语义用 `-`。协作时可追加人员缩写。 |
| 缺陷分支 | `bug_fix-#<Issue编号>-<简短_描述>` | 从最新 `main` 创建；关联修复 Issue。 |
| 项目分支 | `proj_main-<项目标识>` | 从 `main` 指定 tag 创建，用于客户现场定制；只在确定需要时从 main 引入新功能。 |

除 MVP 外，每项开发工作都关联 GitLab Issue。功能联调、优化和后续缺陷修复继续在对应功能/修复分支进行。合并后两周由系统清理功能/修复分支。

## 合并门槛

1. 从最新 `main` 建分支，记录 main 基线、Issue、分支和脏文件。
2. 代码、测试和所需文档在功能/修复分支完成。
3. 发起到 `main` 的 Merge Request，标题为 `[{类型}] {简要描述}`；描述包含功能/修复、Issue、测试/单测覆盖和影响范围。
4. 至少一名核心开发审核，全部自动化测试通过，无冲突并可正常构建后才合并。
5. SDK 项目必须同步更新单元测试；新增代码行覆盖率不低于 80%，关键模块不低于 90%，并覆盖正常和异常场景。

Commit 要清晰说明内容与原因并关联 Issue。标签由 Jenkins 流水线管理，标签描述说明功能、核心修改、数据库/API/配置变化、限制和依赖。

## Commit message 格式

- 主题行一律为：`<type>(<scope>): <实际变更摘要>`。
- `type` 根据真正完成的工作选择：新增能力用 `feat`，修复问题用 `fix`，结构调整用 `refactor`，工程或构建维护用 `chore`，文档更新用 `docs`。示例不是固定模板，不得无视实际变更机械复用。
- `scope` 标识实际影响范围；摘要表达可验证的变更结果，避免“更新”“修改”等空泛词。
- 单一简单变更可只写主题行。复杂提交的主题行后空一行后用 - 列出关键变化、兼容性处理与测试证据。
- 需要关联 Issue 时，只引用真实的 Issue，按项目约定写入提交正文或 MR；不编造 Issue 编号。

格式示意：`fix(<scope>): <实际修复摘要>`、`feat(<scope>): <实际新增能力摘要>`；每次提交内容均按当次实际工作填写。

## AI/自动化操作守则

- 先读取远端 `main`、当前分支、脏文件和仓库规则；不要用 reset/checkout 覆盖用户修改。
- 建分支、commit、push、创建 MR、合并 main 和标签分别检查用户授权。未授权 commit/push 时只保留工作树变更、验证证据和建议 message；任何情况下都不因实现请求直接写入 main。
- 用户要求先汇总确认时，停在 feature 分支和完整证据；不创建 MR、不合并、不打发布 tag。
- 用户临时指定 `feat/<name>` 等与标准不同的隔离分支时，遵从该明确指令、保留工作区，并在交付/MR 前写明偏离原因；不虚构 Issue 编号。
- 提交前按本参考的 Commit message 格式审阅主题、正文和 Issue 关联；主题与正文必须反映实际改动和验证，不复制示例文本。
- 项目分支发现通用问题时，创建产品 Issue，在 main 修复后通过 cherry-pick 或合并同步回项目分支。
- GitHub 开源 profile 中，公开 PR/Release 与内部 `proj_main-*`、Jenkins 部署分别维护；不能把 GitHub Release 写成客户现场已部署，也不能把内部部署记录当成公开 Release。
