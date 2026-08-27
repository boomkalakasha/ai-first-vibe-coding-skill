# AI-first 任务交接

## 一句话结论

- 完成度/是否可继续使用：
- P0 是否放行：
- 当前定位：REAL / HYBRID / DEMO / PLANNED：

## 操作模式与授权

- 操作模式：READ_ONLY_REVIEW / PLAN_ONLY / IMPLEMENT_AND_VERIFY / FULL_ITERATIVE_DELIVERY / SKILL_REVIEW：
- 允许编辑：
- 允许运行/重载：
- 允许数据库写入：
- 允许外部业务副作用：
- 明确禁止：

## 任务基线

- 任务等级：L0 / L1 / L2 / L3：
- 当前轮次：第几轮 / 总轮数：
- 用户目标和黄金业务链：
- 非目标和禁止动作：
- 运行环境/URL/端口：
- 热部署状态和是否重启过：
- 数据任务/时间范围/任务 ID：
- 当前分支和脏文件边界：

## 需求与正式产物

- 应用地图及系统核心业务/边界：
- 详细业务 Spec：
- 用户故事与测试 Case：
- 需求业务角度审查：
- 本轮模块实施计划：
- 本轮回测与评估：
- 本轮优化方案：
- 决策日志：
- 需求追踪表：
- 正式业务写入路径清单：
- 同一动作的唯一策略源：

## 已完成

- 文档：
- 后端/接口/数据：
- 前端/页面/交互：
- 测试/脚本/配置：
- 业务规则和动作闸门：
- 写入路径审计结论：
- 未执行的高风险副作用 Case：

## 验证证据

| 范围 | 证据 | 等级 | 备注 |
|---|---|---|---|
| 静态 | 编码、BOM、语法、diff、敏感信息 | RUNTIME_PASS / STATIC_PASS_PENDING_RUNTIME / FAIL | |
| 运行 | URL、接口、日志、进程、热部署 | RUNTIME_PASS / OLD_RUNTIME / PARTIAL_PASS / BLOCKED / NOT_RUN | |
| 数据 | 来源、任务、数据库、时间窗口、关联、统计 | RUNTIME_PASS / BLOCKED / NOT_RUN | |
| 用户/交互 | 页面路径、空态、错误、重试、重复提交、跨页 | UI_OBSERVED / HTTP_OBSERVED / SOURCE_INFERRED / DOCUMENTED_ONLY / NOT_EVALUATED | |
| 业务价值 | 时间成本、误判风险、证据质量、动作闭环 | 已验证 / 部分验证 / 未验证 | |

## REAL / HYBRID / DEMO / PLANNED

- REAL：
- HYBRID：
- DEMO：
- PLANNED：

## 未完成和风险

- P0：
- P1：
- P2：
- 旧运行态/未重启：
- 浏览器/数据库/日志等不可用边界：
- 代理未落盘、超时或降级项：
- 回滚方式：

## 本轮复盘

- 用户/业务：
- 数据/内容：
- 技术/性能：
- 视觉/交互：
- 运营/治理：
- 相对上一轮的改善：
- 新增决策：

## 下一轮

- P0：目标、Case、责任人、证据：
- P1：
- P2：
- 下一轮开始前需要重新确认的环境/数据/权限：
