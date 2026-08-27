# 分层模型多 Agent 闭环

本参考仅用于跨仓库、长周期、可拆分且有明显模型成本差异的 L3 任务。普通 L0/L1 和紧耦合单模块任务保持串行。

## 1. 目标

用高判断力控制面保持方向、边界和验收一致，用高吞吐执行面完成边界清楚的盘点、实现和回归；所有状态回写到唯一台账，防止长上下文、任务切换和多 Agent 完成声明造成进度漂移。

模型名称不是流程的一部分。当前平台可用的旗舰、均衡、经济模型可以变化，按实际能力选择：

| 角色 | 适合的能力层 | 不可下放职责 |
|---|---|---|
| Controller / Planner | 当前可用的高判断力模型 | 目标、应用地图、Spec、依赖图、优先级、授权边界 |
| Implementer | 满足任务难度的最低成本模型 | 只能在给定写集、Case 和停止条件内实现 |
| Evidence Runner | 高吞吐模型 | 构建、测试、浏览器、日志、数据库只读证据采集 |
| Spec Reviewer | 高判断力模型或隔离的新上下文 | 逐条核对需求、非目标、写入路径和业务语义 |
| Quality Reviewer | 独立上下文 | 正确性、安全、性能、可维护性和回归风险 |
| Release Auditor | Controller 或同等级独立模型 | P0/P1 收敛、运行版本、制品、迁移、回滚和放行 |

高 reasoning 档位不能把经济模型自动变成旗舰模型。边界清楚的任务优先经济模型；跨域设计、数据迁移、兼容语义和放行判断优先高判断力模型。

## 2. 唯一控制面

复杂任务只维护一份主执行台账。各仓库 README、Agent 回复和聊天进度都不是总状态源。

复制 [执行台账模板](../templates/execution-ledger.md)，至少记录：

    workPackageId, requirementId, priority, repository, branch, baseline,
    dependencies, assignedRole, agentId, allowedWrites, forbiddenActions,
    acceptanceCases, evidence, status, openP0, openP1, approvalGate,
    rollback, lastVerifiedCommit, lastVerifiedRuntime, lastVerifiedAt

状态只能由 Controller 根据证据推进：

    UNTRIAGED → PENDING → READY → RUNNING → SPEC_REVIEW → QUALITY_REVIEW
    → VERIFIED → DONE
                 ↘ BLOCKED / HOLD / STOP

- 子 Agent 返回 DONE 只表示已交付候选产物，不等于主台账 DONE。
- PENDING 表示范围已登记但依赖或审批尚未满足；不是 BLOCKED，也不计入完成。
- VERIFIED 要求当前 commit、构建/测试输出和所需运行证据一致。
- BLOCKED、HOLD、NOT_RUN 不计入完成度。
- 总百分比只作导航；放行由 Gate 和未关闭 P0/P1 决定。
- 工作流状态与证据等级是两个维度。VERIFIED 只有达到工作包声明的 requiredEvidenceLevel 才有效；要求 RUNTIME_PASS 的任务不能用 STATIC_PASS_PENDING_RUNTIME 进入 DONE。

## 3. 分解和并发

先画依赖 DAG，再并发。工作包满足以下条件才允许并行写入：

1. 写集不重叠；
2. 不依赖同一未稳定契约；
3. 不修改同一数据库状态或运行实例；
4. 能独立测试和回滚；
5. 主 Agent 能在本轮完成整合验证。

适合并发：

- 不同仓库的只读盘点；
- 已冻结契约下的独立模块；
- 构建、静态检查和只读证据采集；
- 独立的 Spec、质量和运行复核。

必须串行：

- 共享 API/Schema/路由契约尚未冻结；
- 同一文件或同一脏工作树；
- 数据迁移、调度器切换、Nginx 切流；
- 实现后的 Spec Review 和 Quality Review；
- 需要上一任务实际输出才能开始的工作。

### 3.1 跨窗口并发容量预算

并发数量是反馈控制结果，不是固定编制。每次派发前和每个 Wave 结束时记录一次容量快照。

| 信号 | 能证明什么 | 边界 |
|---|---|---|
| 平台全局调度器/配额 | 全局硬授权和剩余槽位 | 可用时优先作为事实源 |
| 应用内活跃主任务列表 | 其他对话窗口是否在工作 | 除非平台明确暴露，否则看不到其子 Agent 数 |
| 当前任务树 Agent 列表和容量 | 本任务局部占用/空槽 | 不能证明全机仍有容量 |
| 独立 `READY` 工作包 | 有价值的并行度 | PENDING 或有依赖的包不能派发 |
| 审核积压、失败/超时、CPU/内存/IO 压力 | Controller 是否还能吸收新结果 | 压力信号只会降低并发 |

快照至少记录：`activeRootTasks`、`localRunningAgentsIncludingController`、`localRunningChildren`、`treeCapacity`、`reserveSlots`、`crossWindowChildrenVisibility`、`readyIndependentWork`、`reviewBacklog`、`resourcePressure`、`targetActiveChildren`、`spawnNow`、时间和调整原因。主 Agent 运行时 `localRunningAgentsIncludingController` 至少为 1；`targetActiveChildren` 表示目标 active 子 Agent 总数，`spawnNow` 只表示本次新增数。

任务树容量已知时，只要平台允许就额外保留 1 个本地槽位给 Reviewer/紧急任务：

`localFreeAfterReserve = max(0, treeCapacity - localRunningAgentsIncludingController - reserveSlots)`

`spawnNow` 不得超过 `localFreeAfterReserve`；`targetActiveChildren` 不得超过 `localRunningChildren + localFreeAfterReserve`。

平台没有全局配额事实时采用保守策略：

1. 其他窗口子 Agent 不可见时标记 `UNKNOWN`，不能当作 0。
2. 把主 Agent/Controller 计入本地占用；容量允许时再额外保留至少 1 个槽位给 Reviewer/紧急任务，不把本任务树所有空槽都塞给 Implementer。
3. 初始只开 1 个。上一 Wave 无失败、超时、冲突和审核积压，资源正常、应用内活跃任务没有增加且仍有独立 `READY` 包时，下一 Wave 最多增加 1 个。
4. 其他窗口活跃且全局子 Agent 负载未知时，最多保留 1 个或串行；出现新活跃任务、`needs_attention`、重复失败、审核积压、契约不稳定、写集重叠、资源压力或用户转向时立即缩容。
5. 只在 Wave 边界和 spawn 前重算；不为占满槽位而制造任务，也不做高频轮询。

如果必须严格限制整台机器的总子 Agent 数，只能使用平台级全局调度器；平台没有该能力时，可实现带 owner、容量、原子 acquire/release、heartbeat、TTL 和孤儿租约回收的共享信号量。没有锁的 JSON/文本计数器不能作为可靠的全局并发控制。

同一实现任务使用“实现 → Spec Review → 修复 → Quality Review → 修复 → 主 Agent 验证”的顺序。多个实现 Agent 不得同时修改共享文件。

## 4. 子 Agent 上下文包

不要把完整长对话作为默认上下文。Dispatcher 为每个 Agent 提供最小但充分的上下文包：

    目标和工作包 ID
    已确认 FACT 与证据路径
    相关 Spec / Case / 决策编号
    仓库、分支、baseline commit、脏文件
    依赖和当前运行版本
    允许读取、允许修改、禁止修改
    必须产出和验收命令
    外部审批边界
    停止条件和超时交付格式
    需要加载的 Skill / 插件

子 Agent 返回：

    DONE / DONE_WITH_CONCERNS / NEEDS_CONTEXT / BLOCKED
    实际修改文件
    实际运行命令、exit code、测试数量
    commit / 运行版本 / URL
    未完成项和新风险
    是否发现范围或文档漂移

## 5. 注意力漂移检查

每个 Wave 开始和结束时做 Context Re-anchor：

1. 重读 task baseline、最新 plan、decision log、执行台账和受影响 Spec/Case；
2. 重新读取真实 Git HEAD、脏文件、运行版本和外部状态；
3. 比较本轮拟执行项与原目标、非目标、授权写集；
4. 把新事实写回 decision log 和台账，不只留在聊天消息；
5. 若计划与现场冲突，先修计划，再继续实现；
6. 使用新上下文 Reviewer，避免实现者的确认偏误。

以下是漂移信号：

- 为了提高完成度而重定义 Case；
- 用新的功能替代原本失败的主路径；
- 子 Agent 修改未授权文件或相邻仓库；
- 当前运行实例不是刚验证的 commit；
- 只报告“改了什么”，没有失败证据和命令；
- P0/P1 数量下降但问题没有对应验证证据。

发现漂移时把工作包退回 HOLD，恢复到最后一个已验证 baseline，不通过破坏性 reset 覆盖用户改动。

## 6. P0/P1 收敛循环

每个 Wave 结束执行：

    聚合实现和证据
    → 独立 Spec/质量/运行审查
    → 更新 P0/P1/P2
    → 只把已证实 P0/P1 拆成下一轮工作包
    → 实现和回归旧失败 Case
    → 重新审查

退出规则：

- 用户明确要求“无 P0/P1”时，未关闭 P0/P1 必须为 0 才能放行；
- 其他 L3 任务至少 P0=0；P1 只有用户接受、具备降级/回滚且不影响核心链路时才可受控保留；
- BLOCKED 不能换名为“已知限制”后放行；
- 轮数、token 或时间耗尽都不等于完成。

在 task baseline 中预先定义本地重试和外部副作用重试上限。相同根因连续重试仍无新证据、任务需要新权限、或依赖外部状态时停止自动重试并 HOLD/BLOCKED，不要让经济模型无限循环消耗。

## 7. 外部副作用

分层模型调度不扩大授权。Git push/MR、Jenkins 写入、部署/切流、数据库写入、删除和重启分别检查：

- 当前请求是否明确授权；
- 目标、版本、备份和回滚是否已验证；
- 是否由唯一 Agent 执行；
- 是否有幂等或重复执行保护；
- 执行后是否立即采集当前运行证据。

未授权时，Implementer 可以准备未提交源码变更、脚本、dry-run、发布包和人工步骤；建分支、commit、push、MR 仍分别遵循 task baseline 的 Git 授权。

## 8. 完成与主 Agent 验收

主 Agent 最终重新执行而不是转述子 Agent 的关键验证：

- plan/Spec/Case 逐条追踪；
- 受影响仓库的完整测试和构建；
- 浏览器、console、network、接口、日志和数据事实；
- 制品 SHA、镜像 digest、运行 commit 和配置；
- 数据迁移前后校验、调度唯一性和回滚演练；
- P0/P1 清单与所有旧失败 Case。

只有唯一台账达到目标 Gate 才能宣称完成。子 Agent、CI 或页面任一单点成功都不能代替 Controller 验收。

## 9. 平台降级

- 没有多 Agent：同一主 Agent 用新的检查清单分阶段执行，角色隔离改为上下文重锚和独立复核轮次。
- 没有多模型：使用同一模型的不同 Agent/会话承担 Controller、Implementer、Reviewer，仍保持写集和证据隔离。
- 没有浏览器/数据库/运行环境：相关项保持 NOT_RUN/BLOCKED，不能降低完成门槛。
