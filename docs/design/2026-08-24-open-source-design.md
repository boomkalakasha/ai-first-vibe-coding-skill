# AI-first Vibe Coding Skill 开源设计

## 目标

把现有内部 Skill 的通用方法提炼为可公开安装、可验证、可贡献、可发布的独立项目，同时保留本地内部版本的领域能力与 GitLab/Jenkins 规则。

## 关键决策

- 公开仓库采用干净历史，不复制内部评测记录、机器路径或真实业务资料。
- 公开仓库默认使用 GitHub OSS profile：Issue/分支/PR/受保护 `main`/SemVer tag/GitHub Release。
- 内部 GitLab/Jenkins profile 仍受项目级规则控制；公开 profile 不替代客户分支、现场部署或内部制品发布。
- 许可证采用 Apache-2.0。发布者需要自行确认其拥有公开全部内容的权利。
- 公开内容以英文 README 为入口，并提供完整中文 README；Skill 正文保持中英术语兼容。
- 首个版本定位为 `v1.0.0`：工作流稳定、验证脚本可重复、兼容边界明确，但不宣称所有 Agent 宿主均已运行验证。

## 公开边界

公开：通用研发闭环、证据等级、任务分级、多 Agent 契约、GitHub 开源发版 profile、通用模板和去领域化 eval。

不公开：公司制度原文、客户分支明细、内网 URL、机器绝对路径、真实项目复盘、账号凭据、内部 Jenkins/GitLab 配置和现场交付脚本。

## 验收

1. Skill 元数据、JSON、Markdown 链接、UTF-8/BOM、敏感模式检查通过。
2. 公共 eval 能覆盖触发边界、证据声明和 GitHub OSS profile。
3. GitHub Actions 可验证并打包可下载的 Skill ZIP 与 SHA-256。
4. README、贡献、安全、支持、行为准则、变更日志和 Agent 指引齐全。
5. 首个 Git tag 和 GitHub Release 均指向已验证的公开提交。

## 非目标

- 不把 GitHub Release 当成生产部署证明。
- 不自动发布到任何 Skill marketplace。
- 不承诺未实际验证的 Claude/Cursor/Cline/Copilot 兼容性。
