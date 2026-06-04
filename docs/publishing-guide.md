# Publishing Guide

## 首发版本

当前首发版本为 `v0.1.0-alpha`。

## 发布前检查

1. 根目录存在 `README.md`。
2. 根目录存在 `CHANGELOG.md`。
3. 每个 Skill 都存在 `SKILL.md`。
4. 每个 Skill 都存在 `metadata.json`。
5. 新增 Skill 放入 `skills/`。
6. 临时输出、缓存、测试产物不进入 Git。

## 版本命名

建议使用语义化版本：

- `v0.1.0-alpha`：首发 alpha 版本
- `v0.2.0-alpha`：新增重要 Skill 或结构能力
- `v0.3.0-beta`：进入更稳定测试阶段
- `v1.0.0`：形成稳定可复用版本

## 新增 Skill 流程

1. 在 `skills/` 下新建目录。
2. 复制 `docs/skill-template.md` 的建议结构。
3. 编写 `SKILL.md`。
4. 添加 `metadata.json`。
5. 如有案例或方法论，放入 `knowledge_base/` 或 `references/`。
6. 更新根目录 `README.md` 的 Skill 列表。
7. 更新 `CHANGELOG.md`。
