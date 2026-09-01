# 项目与模块 AI 引导覆盖度 / Project and module AI guidance coverage

在 L2/L3 基线阶段，除了读取已有规则，还要作出一次可记录的引导覆盖度决策：

> **Read the closest guidance, verify it against facts, then decide whether a
> project or module needs its own AI guide.**

这是一项项目所有的决定。公共 Skill 只给判断框架；端口、命令、服务账户、数据、
客户分支、部署环境和项目专有工作方式必须留在对应项目仓库或私有组织策略中。

## 决策状态

每个受影响仓库记录一个状态，而不是默认创建更多 Markdown：

| 状态 | 含义 | 下一步 |
| --- | --- | --- |
| `PRESENT_VALIDATED` | 已有项目或模块引导，且命令、边界和引用与当前事实一致 | 记录核验来源与时间 |
| `NEEDS_UPDATE` | 引导存在，但已与源码、配置或运行事实漂移 | 先区分 `DOC_STALE` / `IMPLEMENTATION_DRIFT`，再在项目内修正责任方 |
| `CREATE_PROJECT_GUIDE` | 根仓库缺少会影响协作、安全或交付的本地规则 | 在根目录建立或补充项目级 `AGENTS.md` / 等效入口 |
| `CREATE_MODULE_GUIDE` | 某个子模块确有根文档无法清楚表达的独特边界 | 在该模块最近作用域创建最小补充指南，并从根指南链接 |
| `NOT_NEEDED` | 根指南和现有文档已经足以解释该模块 | 记录理由，避免复制粘贴的“空指南” |

## 何时需要项目级引导

Project-level guidance is warranted when a contributor or agent cannot safely
infer one of the following from ordinary source and README content:

- the supported build, test, local-run, migration or release commands;
- repository-specific branch, review, artifact, rollback or ownership rules;
- credentials, privacy, data-write, security, production or external-side-effect boundaries;
- cross-module contracts, source-of-truth ownership, generated-code rules, or required evidence gates.

最小项目级引导应说明范围、主要命令、不可触碰边界、关键链接和事实来源；不要复制通用
Skill 的全部流程，也不要把内部事实回灌到公开包。

## 何时需要模块级引导

Module-level guidance is warranted only when the module differs materially from
the root in at least one of these areas:

1. 独立的构建、启动、测试、代码生成或迁移命令；
2. 独立拥有的外部 API、持久化/数据迁移、权限、密钥、隐私或合规边界；
3. 独立的发布生命周期、代码所有者、兼容性承诺或回滚方式；
4. 容易被错误跨越的依赖方向、领域不变量或生成物边界。

如果只是普通包划分、复用根命令、没有特权动作且根文档已给出依赖方向，则选择
`NOT_NEEDED`。不要为每个目录生成 duplicate module guides；这会制造漂移而不是帮助
Agent 决策。

模块指南必须短、可验证，并包含：模块拥有的内容/不拥有的内容、输入输出契约、特有命令
或前置条件、禁止动作、测试位置和回指到根指南。它不能覆盖根项目的安全或交付策略。

## 验证与维护

在每次 L2/L3 启动和影响结构、命令、权限、发布或模块边界的变更后，更新任务基线中的
覆盖度决策。对新增或更新的 guide，验证引用路径、命令、版本和示例；如果没有运行态
证据，按 `STATIC_PASS_PENDING_RUNTIME` 或 `NOT_RUN` 记录，不把文档存在当作运行保证。
