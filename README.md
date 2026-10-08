# my-skills

自用的 AI Agent 技能集合（Claude Code 及兼容 `SKILL.md` 约定的 Agent 均可使用）。

每个技能是**一个自包含目录**，内含 `SKILL.md`（`name` / `description` frontmatter 定义标识与触发条件）以及它需要的模板、规范、脚本。

## 技能列表

| 技能 | 作用 |
| --- | --- |
| [`prd-from-draft`](prd-from-draft/) | 需求描述 / 图片 / 已有原型 → 可点击 HTML 草图原型 → 需求 PRD → 飞书文档，三个阶段各有一道用户确认门禁 |

## 用法

把需要的技能目录整个复制到你的技能目录即可：

```bash
# Claude Code（用户级）
cp -r prd-from-draft ~/.claude/skills/

# 或项目级
cp -r prd-from-draft <你的项目>/.claude/skills/
```

技能里的路径一律写成 `<工作区>/…` 相对形式，复制后无需改动。

## 目录约定

新增技能时，在仓库根目录平级建一个同名目录：

```
my-skills/
├── README.md              # 本文件，新增技能后在这里补一行
├── prd-from-draft/
│   ├── SKILL.md           # 必需：流程与触发条件
│   ├── DESIGN.md          # 规范源（可选，视技能而定）
│   ├── *.html / *.md      # 模板与骨架
│   └── *.py / *.js        # 校验或转换脚本
└── <下一个技能>/
```

约定：

- **`SKILL.md` 是入口**，保持精简（建议 500 行以内）；长规范拆到独立文件，由 `SKILL.md` 引用
- **目录自包含**，不依赖仓库里其他技能的文件
- **不写死本机绝对路径**，用 `<工作区>/…` 或相对路径
- 有规范文档的同时，尽量配一个**一致性校验脚本**——文档与骨架漂移时靠脚本发现，不靠人眼

## 许可

[MIT](LICENSE) © 2026 vxkt4s6wpm-jpg
