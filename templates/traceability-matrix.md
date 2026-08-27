# AI-first 需求追踪矩阵

| 需求 ID | 业务问题/目标 | 对象 | 动作 | Spec 条款 | 用户故事 | 测试 Case | 实现文件/API | 数据/任务事实 | 回测证据 | 当前状态 | 下一步 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| REQ-001 | | | | | | | | | | PASS / PARTIAL_PASS / PENDING / BLOCKED / NOT_RUN / FAIL | |

## 追踪规则

- 每个 P0 必须能追踪到至少一个负向 Case 和一个运行或明确阻塞证据。
- 只有文档定义而没有源码或运行证据时，不能标记为 REAL 或 PASS。
- 源码已修改但运行实例未加载时，使用 `STATIC_PASS_PENDING_RUNTIME` 或 `OLD_RUNTIME`。
- 交互证据同时记录 `UI_OBSERVED`、`HTTP_OBSERVED`、`SOURCE_INFERRED`、`DOCUMENTED_ONLY` 或 `NOT_EVALUATED`。
- 下一轮只继承仍未闭合、已有事实支持的项，不能借追踪矩阵扩大范围。
