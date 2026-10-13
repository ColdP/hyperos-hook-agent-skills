# 贡献指南

欢迎为 `hyperos-hook-agent-skills` 贡献内容。本项目收集基于证据的 HyperOS 分析和 Native Hook 开发 Agent Skill。贡献应当保持范围清晰、结果可复现，并适合公开发布。

## 提交修改前

1. 阅读目标 Skill 的 `SKILL.md` 和 [Agent Skills 开放规范](https://agentskills.io/specification)。
2. 检查当前 Git 状态，保留与本次修改无关的工作。
3. 不要加入专有 APK、反编译源码、私钥、包含个人信息的设备日志或凭据。
4. 技术结论必须记录目标文件身份，并使用统一证据标签：`DEVICE_VERIFIED`、`STATICALLY_VERIFIED`、`INFERRED` 或 `UNKNOWN`。

## Skill 修改要求

- 每个 `SKILL.md` 只负责一个清晰能力，详细流程放入 `references/`。
- Skill 目录名只能使用小写字母、数字和连字符；frontmatter 中的 `name` 必须与目录名一致。
- `description` 必须说明 Skill 能做什么，以及应当在什么任务中触发。
- `SKILL.md` 使用相对路径链接参考文件，链接文件放在同一个 Skill 目录中。
- 不要把某个桌面版本的偏移、ABI、符号、对象布局或测试结果推广成通用结论。
- 所有验证报告都要区分编译成功、库已加载和功能已经生效。

## 文档与语言

修改面向用户的仓库说明时，同时更新对应的英文和中文文档。命令应当可以直接复制执行，并明确平台相关路径。公开资料支持某项工作流时，应在对应指南中提供链接。

## 验证

提交 Pull Request 前运行：

```bash
python <quick_validate.py 的路径> skills/hyperos4-rust-launcher-native-hook
python scripts/validate_repo.py
git diff --check
```

同时检查所有本地 Markdown 链接，并审查最终 diff，确认没有误加入二进制文件或秘密信息。GitHub Actions 会在 Push 和 Pull Request 时自动执行相同检查。

## Pull Request

请说明用户问题、修改了哪个 Skill 或文档、证据状态、验证命令、验证结果和仍然未知的事项。保持 Pull Request 范围足够小，便于审查。除非仓库明确要求，不要提交生成产物。

## 许可证

提交贡献即表示你同意该贡献按照 [Apache License 2.0](LICENSE) 提供，并遵守许可证条款。贡献内容必须是你的原创工作，或是你有权重新发布且已明确标注来源的内容。
