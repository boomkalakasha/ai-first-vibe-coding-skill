# Skill 沉淀、迭代与反馈闭环

研发任务不仅产出代码，也会暴露可复用的规则、失败模式、决策和工具边界。
AI 应主动识别这些候选，但不能把一次性的项目事实、私人偏好或未授权的组织规则
直接写进公共 Skill。

## 归属层级

| 层级 | 适合沉淀的内容 | 所有者 | 默认动作 |
| --- | --- | --- | --- |
| `LOCAL_ONLY` | 一次性推理、临时 workaround、工具流水、机器事实、个人草稿 | 当前任务/宿主 | 保留在任务记录，不升级 |
| `USER_PREFERENCE` | 用户稳定的协作偏好、表达规则、授权边界 | 用户偏好文档 | 记录到用户级偏好，必要时在交付摘要说明 |
| `PROJECT_GUIDANCE` | 项目命令、模块边界、数据/权限契约、项目特有验收规则 | 项目仓库 | 更新最近作用域的项目 guide 或等效事实源 |
| `ORG_POLICY` | 跨项目共享的分支、交付、安全、模型或治理规则 | 私有组织策略 | 提案或更新组织策略；需要相应授权 |
| `PUBLIC_SKILL` | 跨项目可复用、脱敏、与具体客户/机器无关的方法 | 公共 Skill | 形成候选，补 eval 后再更新公共 Skill |

## 触发时机

在 L1+ 任务启动回看本次上下文及可用的最近同类记录；每个自然收口、用户纠正、重复失败
和交接主动扫描。LITE/L0也处理实际纠正和失败信号。这是工作职责，不用“按需”省略：

- 同一规则是否在不同模块、项目或会话中重复出现；
- 用户是否明确确认了一个应长期保留的偏好或边界；
- 当前项目 guide、组织策略或公共 Skill 是否已经与事实漂移；
- 本轮新增的失败 Case、验证方法或工具降级是否值得复用。

即使没有候选，也要在收尾写明 `skillUpdateSummary: none` 及扫描范围/原因，区分已检查与未检查。
复用现有任务记录维护轻量 `skillUpdateCandidates`；同模式在两次独立任务出现、用户确认
长期偏好或可复现缺口造成返工时及时提出收益和落点，不另建台账系统。

## 闭环步骤

1. **发现**：只从实际事实、用户明确反馈、可复现 Case 或重复模式提出候选，不把猜测当规则。
2. **分层**：为候选标注归属层级、敏感性、证据来源、复用范围、置信度和当前状态：`OBSERVED_CANDIDATE`、`REPEATED_CANDIDATE`、`PROMOTE_PENDING_AUTH`、`PROMOTED`、`DEFERRED` 或 `REJECTED`。
3. **汇总**：复用任务记录的 `skillUpdateCandidates` 记录候选规则、证据/Case、所有者/落点、状态、验证和复核条件；收口的 `skillUpdateSummary` 引用它并概括结果，不重复抄全表。详细字段按影响补齐。
4. **提案或更新**：项目事实写入项目所有者；跨项目规则写入私有组织策略；用户偏好写入用户锚点；公共 Skill 只吸收可复用且脱敏的判断框架。没有授权时只形成提案，不直接改组织或公共规则。
5. **验证**：更新对应文档后，补一条可区分的 eval/回归 Case，检查引用、敏感信息、范围和现有行为；不能用“文件已写入”证明规则已生效。
6. **回馈**：最终汇总列出已提升、待授权、暂缓和明确不沉淀的候选，并说明下一轮如何继续观察。下一次任务启动时读取上次摘要，避免重复提出同一候选。

## `skillUpdateSummary` 最小格式

```text
skillUpdateSummary:
  candidates:
    - rule: <可复用规则>
      trigger: <问题、反馈或重复 Case>
      evidence: <文件、Case、运行或用户确认>
      owner: USER_PREFERENCE | PROJECT_GUIDANCE | ORG_POLICY | PUBLIC_SKILL | LOCAL_ONLY
      destination: <建议文件或策略入口>
      status: OBSERVED_CANDIDATE | REPEATED_CANDIDATE | PROMOTE_PENDING_AUTH | PROMOTED | DEFERRED | REJECTED
      change: <拟新增、修改或保持不变的内容>
      validation: <eval、测试或核验方法>
      next_review: <时间或触发条件>
  none_reason: <没有候选时填写>
```

公共 Skill、公司级策略和项目级 guide 不能互相复制成长期分叉；每层只保留自己
拥有的事实和规则，并从入口链接其他层级。
