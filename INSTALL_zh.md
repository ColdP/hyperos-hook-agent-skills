# 安装指南

本仓库遵循公开的 [Agent Skills 规范](https://agentskills.io/specification)。Skill 源码位于 `skills/hyperos4-rust-launcher-native-hook/`。请把这个目录复制到对应 Agent 的发现目录，或将本仓库放在 Agent 会扫描的项目目录中。

## ChatGPT Codex

Codex 会从项目的 `.agents/skills` 和用户目录的 `~/.agents/skills` 中发现 Skill。Windows 用户目录对应 `%USERPROFILE%\.agents\skills`。本仓库根目录的 `skills/` 适合发布和复制，但不会自动作为 Codex 的项目 Skill 发现目录。

在目标项目根目录安装：

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse -Force ..\hyperos-hook-agent-skills\skills\hyperos4-rust-launcher-native-hook .agents\skills\
```

也可以安装到当前用户：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\hyperos4-rust-launcher-native-hook "$env:USERPROFILE\.agents\skills\"
```

在 Codex CLI 或 IDE 扩展中使用 `/skills` 检查 Skill，或显式输入 `$hyperos4-rust-launcher-native-hook`。匹配任务时 Codex 也可能自动调用。新复制的 Skill 没有出现时，重启 Codex。

## Claude Code

Claude Code 的项目 Skill 路径是 `.claude/skills/<name>/SKILL.md`，个人 Skill 路径是 `~/.claude/skills/<name>/SKILL.md`：

```bash
mkdir -p .claude/skills
cp -R ../hyperos-hook-agent-skills/skills/hyperos4-rust-launcher-native-hook .claude/skills/
```

Skill 可以在相关任务中自动加载；其目录名也可作为斜杠命令名称，在支持该功能的版本中使用 `/hyperos4-rust-launcher-native-hook`。

## OpenCode

OpenCode 的项目 Skill 路径是 `.opencode/skills/<name>/SKILL.md`，全局路径是 `~/.config/opencode/skills/<name>/SKILL.md`：

```bash
mkdir -p .opencode/skills
cp -R ../hyperos-hook-agent-skills/skills/hyperos4-rust-launcher-native-hook .opencode/skills/
```

也可以把 Skill 放到 `.agents/skills` 或 `.claude/skills`，供多个兼容 Agent 共用。OpenCode 加载 Skill 时使用 `skill({ name: "hyperos4-rust-launcher-native-hook" })`。

## GitHub Copilot

GitHub Copilot 支持项目目录 `.github/skills`、`.claude/skills` 和 `.agents/skills`，个人目录包括 `~/.copilot/skills` 和 `~/.agents/skills`。在项目中安装：

```bash
mkdir -p .github/skills
cp -R ../hyperos-hook-agent-skills/skills/hyperos4-rust-launcher-native-hook .github/skills/
```

Copilot CLI 也提供 `gh skill` 用于发现和安装 Skill；直接复制可以固定使用本仓库中已经审查过的文件。

## 检查安装结果

最终路径应当类似：

```text
<发现目录>/hyperos4-rust-launcher-native-hook/SKILL.md
```

请确认 `SKILL.md` 的 frontmatter 中 `name` 与目录名一致，并且 `references/` 和 `evals/` 目录仍然位于 `SKILL.md` 旁边。本 Skill 只提供分析指导，不会安装软件包、修改设备、重启桌面，也不包含专有 APK。

## 官方资料

- [Agent Skills 规范](https://agentskills.io/specification)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills/)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [OpenCode Agent Skills](https://opencode.ai/docs/skills/)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
