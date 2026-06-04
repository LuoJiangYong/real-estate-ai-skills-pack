# Skill Template

新增 Skill 时，建议复制此结构。只保留必要目录，不需要的目录可以不建。

```text
skills/{skill-slug}/
  SKILL.md
  metadata.json
  references/
  knowledge_base/
  scripts/
  examples/
```

## metadata.json

```json
{
  "name": "Skill Display Name",
  "slug": "skill-slug",
  "version": "0.1.0-alpha",
  "category": "category-name",
  "status": "draft",
  "description": "一句话说明这个 Skill 解决什么问题。",
  "language": "zh-CN",
  "author": "老罗",
  "updated_at": "YYYY-MM-DD"
}
```

## SKILL.md 建议结构

```markdown
---
name: skill-slug
description: 说明触发条件和核心能力。
---

# Skill 名称

## 角色定位

说明 AI 在该 Skill 中扮演什么专业角色。

## 适用场景

- 场景 1
- 场景 2
- 场景 3

## 用户需要提供什么

- 必填信息
- 建议信息
- 可选资料

## 工作流程

1. 信息采集
2. 方法论或知识库检索
3. 分析判断
4. 输出成果
5. 自检与追问

## 输出格式

定义默认输出结构。

## 参考资料

列出需要读取的 `references/` 或 `knowledge_base/` 文件。

## 限制

说明数据核实、专业边界和不适用场景。
```

## 维护原则

- 一个 Skill 只解决一个明确业务问题。
- 方法论、案例库、脚本分开存放。
- 版本号写入 `metadata.json`，不要写进目录名。
- 新增案例优先进入知识库，不直接堆进 `SKILL.md`。
- 平台专属工具调用写成可替换表达。
