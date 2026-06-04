# Contributing

感谢关注 `Real Estate AI Skills Pack`。

本项目的目标是长期沉淀面向中国房地产市场的 AI Skill。为了保持项目高内聚、低耦合、可扩展、易维护，新增或更新 Skill 时请遵循以下约定。

## 基本原则

1. 一个 Skill 只解决一个明确业务问题。
2. Skill 之间可以互相参考，但不要强依赖。
3. 方法论、案例库、脚本分开存放。
4. 不把版本号写进目录名。
5. 新增案例优先进入知识库，不直接堆进 `SKILL.md`。
6. 平台专属工具调用应写成可替换表达。
7. 重要更新需要记录到 `CHANGELOG.md`。

## 新增 Skill

新增 Skill 放入 `skills/{skill-slug}/`。

推荐结构：

```text
skills/{skill-slug}/
  SKILL.md
  metadata.json
  references/
  knowledge_base/
  scripts/
  examples/
```

其中 `SKILL.md` 和 `metadata.json` 为必需文件，其余目录按需创建。

新增前建议先参考：

- `docs/skill-template.md`
- `docs/publishing-guide.md`

## 更新已有 Skill

更新已有 Skill 时，优先判断修改属于哪一层：

- 工作流程或触发条件：修改 `SKILL.md`
- 方法论或参考资料：修改 `references/`
- 项目案例或知识库：修改 `knowledge_base/`
- 自动化辅助：修改 `scripts/`
- 版本、状态、分类：修改 `metadata.json`

不要把所有内容都堆进 `SKILL.md`。`SKILL.md` 应保持为 Skill 的入口说明和执行规则。

## metadata.json

每个 Skill 都应包含 `metadata.json`。

推荐字段：

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

## 命名规范

- Skill 目录使用英文小写和连字符，例如 `real-estate-storyline`
- 中文资料文件可以保留中文名，便于专业团队阅读
- 版本号放入 `metadata.json`，不放入目录名

## 提交说明

提交信息建议简洁明确，例如：

```text
Add customer research skill
Update storyline knowledge base
Refine strategy report generator
```

## 内容边界

本项目鼓励沉淀专业方法论、案例分析、工作流和可复用模板。

请避免提交：

- 未核实的市场数据
- 涉及客户隐私或企业内部敏感信息的资料
- 无来源的政策、价格、成交数据
- 与房地产 AI Skill 无关的通用内容

## 授权边界

本项目采用双许可证：

- 代码与脚本使用 MIT License
- 文档、Skill 定义、方法论、参考资料、知识库和案例内容使用 CC BY-NC 4.0

提交内容即表示你同意该内容按上述许可证进入项目，除非在提交中另有明确说明并获得维护者接受。
