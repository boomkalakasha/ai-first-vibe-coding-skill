# 多窗口动态并发 RED/GREEN/REFACTOR 证据

- 日期：2026-08-26
- 证据等级：`HOST_OBSERVED`
- 场景：应用内有 4 个 active 主任务；当前任务树只有主 Agent，容量 4（含主 Agent）；有 8 个独立低成本实现包；其他窗口子 Agent 数不可见。
- 限制：只运行了 1 个低成本模型评测 Agent，没有创建嵌套 Agent 或执行外部副作用。

## RED：未加载新规则

评测 Agent 一次启动 3 个子 Agent，依据只是当前树名义空余 3 个槽；同时承认无法知道其他窗口的子 Agent 数。这证明原 Skill 没有把“局部空槽”和“全局可用容量”区分开。

## GREEN：第一版规则

评测 Agent 将初始数量降为 1，并把跨窗口负载标记为 `UNKNOWN`；但它把当前运行 Agent 写成 0，遗漏已占槽的主 Agent，并允许后续扩到 3 个子 Agent，暴露了计数和预留槽位歧义。

## REFACTOR：最终规则

最终复测得到一致容量快照：

```text
activeRootTasks=4
localRunningAgentsIncludingController=1
localRunningChildren=0
treeCapacity=4
reserveSlots=1
crossWindowChildrenVisibility=UNKNOWN
localFreeAfterReserve=2
targetActiveChildren=1
spawnNow=1
```

最终决策为：当前全局负载未知时初始只开 1 个；即使后续负载明确，本任务树也默认最多 2 个 active 子 Agent，额外保留 1 个槽位；严格全机上限必须依赖平台全局调度器或原子租约信号量。

## 证据边界

本记录只证明当前主机、当前评测模型和当前压力场景的行为改善。
不证明所有平台都能列出活跃主任务，也不代表全局调度器或共享信号量已经实现。
