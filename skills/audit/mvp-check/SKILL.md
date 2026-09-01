---
name: mvp-check
trigger: MVP_NEEDS_CHECK
description: 复现最小纵向切片，验证输入→核心算法→结果链真的跑通。
---

# Mvp Check

## Trigger
`MVP_NEEDS_CHECK` 或用户明确要求本局部能力。

## Scope
复现最小纵向切片，验证输入→核心算法→结果链真的跑通。

## Inputs
最小命令、代码、数据样例、模型合同

## Procedure
1. 读取输入并确认事实/合同版本。
2. 只完成本 Skill 的局部任务，不推进比赛阶段。
3. 生成结构化产物或建议，并记录关键假设与证据。
4. 按 Checks 自检；需要独立判断时调用对应 audit Skill。

## Outputs
MVP QA 回执

## Checks
检查退出码、关键约束、单位、范围、输入输出追溯；不要求完整论文图。

## Failure
实现问题返 coding，合同问题返 modeling。

## Handoff
返回 `status / outputs_written / key_findings / risks / qa_status / handoff`。Coach 决定是否采纳或继续。
