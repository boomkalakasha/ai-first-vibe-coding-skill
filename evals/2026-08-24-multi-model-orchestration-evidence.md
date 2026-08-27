# 分层模型闭环行为评测证据

- 日期：2026-08-24 Asia/Shanghai
- 模式：SKILL_REVIEW
- 被测场景：跨 10+ 仓库、20 个工作包、昂贵高能力 Controller + 低成本高吞吐 Implementer、统一进度、防上下文漂移、最终 P0/P1=0。
- 执行能力层：高吞吐执行模型，reasoning=max，新上下文，只读。

## RED：更新前版本

旧 Skill 能主动分多 Agent、做证据分级和 P0 Gate，但执行 Agent 明确报告以下内容需要自行推断：

- 高/低成本模型的能力路由；
- 唯一机器可读台账和依赖 DAG；
- 上下文压缩、状态锁和并发上限；
- 无进展停止条件和重试上限；
- 用户要求 P1=0 时的严格放行标准。

结论：BASELINE_GAP_CONFIRMED。

## GREEN：更新后版本

同一场景使用新上下文重复执行。Agent 能逐项引用：

- SKILL.md 0.6 的 Controller/Implementer/Reviewer 分工；
- references/multi-model-orchestration.md 的能力路由、唯一台账、并发写入条件、Context Re-anchor、三层复核和外部 Gate；
- templates/execution-ledger.md 的 PENDING→READY→RUNNING→SPEC_REVIEW→QUALITY_REVIEW→VERIFIED→DONE；
- P0/P1=0、旧失败 Case 回归、BLOCKED/HOLD/STOP 不算完成；
- task baseline 中预先定义 Wave、重试和无进展停止条件。

evals.json 第 9 项的 9 条 expectations 均在回答中得到明确覆盖：MANUAL_PASS 9/9。

## 静态验证

    uv run --with pyyaml python <skill-creator>/scripts/quick_validate.py <skill-root>

结果：Skill is valid。

- evals.json：标准 JSON，可解析，9 项，字段使用 expectations。
- trigger-evals.json：标准 JSON，可解析，23 项。
- 触发 precision/recall：本轮 NOT_RUN；显式调用和行为 GREEN 不能代替自动触发评测。
