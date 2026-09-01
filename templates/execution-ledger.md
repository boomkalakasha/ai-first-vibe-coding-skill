# AI-first 主执行台账

- 目标：
- 当前 Plan 版本/哈希：
- Controller：
- Implementer 能力层：
- Reviewer 能力层：
- 开始时间：
- 当前 Wave：
- 操作模式：
- allowedWrites：
- allowedRestart：
- allowedDatabaseWrites：
- allowedExternalSideEffects：
- 放行标准：P0 = __；P1 = __

## 并发容量快照

| Wave/时间 | 活跃主任务 | 当前树 Agent(含主)/子 Agent/容量 | 预留槽位 | 跨窗口子 Agent 可见性 | 独立 READY 包 | 审核积压/资源压力 | 目标 active 子 Agent/本次新增 | 调整原因 |
|---|---:|---|---:|---|---:|---|---|---|
| 1 / | | 1 / 0 / | 1 | UNKNOWN | | | 1 / 1 | 初始保守派发 |

## 进度摘要

| 状态 | 数量 | 说明 |
|---|---:|---|
| UNTRIAGED | 0 | 尚未完成依赖和边界分析 |
| PENDING | 0 | 范围已登记，等待依赖或审批 |
| READY | 0 | 输入、依赖、写集和 Case 已冻结 |
| RUNNING | 0 | Agent 正在执行 |
| SPEC_REVIEW | 0 | 等待需求/边界审查 |
| QUALITY_REVIEW | 0 | 等待质量审查 |
| VERIFIED | 0 | 当前 commit/运行版本已有证据 |
| DONE | 0 | 已满足本工作包 Gate |
| BLOCKED | 0 | 缺少权限、环境或外部条件 |
| HOLD | 0 | 发现 P0/P1 或范围漂移 |
| STOP | 0 | 已达到停止条件，未完成 |

- 未关闭 P0：
- 未关闭 P1：
- 当前总状态：PASS / PARTIAL_PASS / HOLD / BLOCKED / STOP
- 下一审批 Gate：

## 状态与证据交叉规则

| 维度 | 值 | 用途 |
|---|---|---|
| 工作流状态 | PENDING / READY / RUNNING / SPEC_REVIEW / QUALITY_REVIEW / VERIFIED / DONE / BLOCKED / HOLD / STOP | 表示工作包推进位置 |
| 证据等级 | RUNTIME_PASS / STATIC_PASS_PENDING_RUNTIME / OLD_RUNTIME / PARTIAL_PASS / BLOCKED / NOT_RUN / FAIL | 表示结论被什么事实证明 |
| 交互来源 | UI_OBSERVED / HTTP_OBSERVED / SOURCE_INFERRED / DOCUMENTED_ONLY / NOT_EVALUATED | 表示页面/交互观察来源 |

VERIFIED 只表示已取得本工作包要求的证据；只有 requiredEvidenceLevel 已满足且 Gate 通过才进入 DONE。需要运行证据的工作包不能用 STATIC_PASS_PENDING_RUNTIME 完成。

## 工作包

| ID | 需求/Case | 优先级 | 仓库/分支/baseline | 依赖 | Agent/角色 | 允许写集 | 禁止动作 | requiredEvidenceLevel | 验收证据 | 状态 | P0/P1 | 最后验证 commit/运行版本/时间 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | UNTRIAGED | | |

## Agent 交付登记

| Agent | 工作包 | 状态 | 修改文件 | 命令/exit code/测试数 | 关注项 | 主 Agent 复核 |
|---|---|---|---|---|---|---|
| | | | | | | |

## Context Re-anchor

| Wave | baseline/plan/decision log 已重读 | Git/运行事实已刷新 | 范围漂移 | 新决策 | 处理 |
|---|---|---|---|---|---|
| | | | | | |

## P0/P1 收敛

| Issue | 等级 | 证据 | 影响 Case | 修复工作包 | 复核结果 | 状态 |
|---|---|---|---|---|---|---|
| | | | | | | |

## 外部审批

| 动作 | 目标 | 版本/哈希 | 备份 | 回滚 | 授权证据 | 执行人 | 状态 |
|---|---|---|---|---|---|---|---|
| Git/MR | | | | | | | |
| CI/CD | | | | | | | |
| 部署/切流 | | | | | | | |
| 数据库 | | | | | | | |
| 删除/清理 | | | | | | | |

## 最终验收

- [ ] 全部需求/Case 可追踪到实现与证据
- [ ] 当前 commit、制品、镜像和运行版本一致
- [ ] 浏览器/API/日志/数据证据达到任务要求
- [ ] 所有旧失败 Case 已回归
- [ ] P0/P1 满足本任务放行标准
- [ ] 外部动作和回滚均有事实记录
- [ ] BLOCKED/HOLD/STOP 未被计入完成度
