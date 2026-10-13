# Installation guide

This repository follows the open [Agent Skills specification](https://agentskills.io/specification). The Skill source is stored at `skills/hyperos4-rust-launcher-native-hook/`. Copy that directory into the discovery directory used by your Agent, or keep it in a checked-out repository directory that the Agent scans.

## ChatGPT Codex

Codex discovers repository Skills from `.agents/skills` and user Skills from `~/.agents/skills` (on Windows, `%USERPROFILE%\.agents\skills`). The repository layout in this project is convenient for distribution, but Codex does not treat the top-level `skills/` directory as the repository discovery directory by itself.

For a project-local installation, from the target repository root run:

```powershell
New-Item -ItemType Directory -Force .agents\skills | Out-Null
Copy-Item -Recurse -Force ..\hyperos-hook-agent-skills\skills\hyperos4-rust-launcher-native-hook .agents\skills\
```

For a user installation:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.agents\skills" | Out-Null
Copy-Item -Recurse -Force .\skills\hyperos4-rust-launcher-native-hook "$env:USERPROFILE\.agents\skills\"
```

In Codex CLI or the IDE extension, use `/skills` to inspect available Skills or mention `$hyperos4-rust-launcher-native-hook` explicitly. Codex may also invoke it implicitly when the request matches the description. If a newly copied Skill does not appear, restart Codex.

## Claude Code

Claude Code follows the same Skill format. Project Skills live in `.claude/skills/<name>/SKILL.md`; personal Skills live in `~/.claude/skills/<name>/SKILL.md`.

From the target repository root:

```bash
mkdir -p .claude/skills
cp -R ../hyperos-hook-agent-skills/skills/hyperos4-rust-launcher-native-hook .claude/skills/
```

For a personal installation, use `~/.claude/skills` instead of `.claude/skills`. On Windows PowerShell, use the equivalent `New-Item` and `Copy-Item` commands shown in the Codex section. Claude can load the Skill automatically when relevant; its directory name also provides the slash command name, so `/hyperos4-rust-launcher-native-hook` can be used when supported by the installed Claude Code version.

## OpenCode

OpenCode supports project Skills in `.opencode/skills/<name>/SKILL.md` and global Skills in `~/.config/opencode/skills/<name>/SKILL.md`. It also loads compatible project and global definitions from `.claude/skills` and `.agents/skills`.

The OpenCode-specific installation is:

```bash
mkdir -p .opencode/skills
cp -R ../hyperos-hook-agent-skills/skills/hyperos4-rust-launcher-native-hook .opencode/skills/
```

For a global installation:

```bash
mkdir -p ~/.config/opencode/skills
cp -R ./skills/hyperos4-rust-launcher-native-hook ~/.config/opencode/skills/
```

Using `.agents/skills` is useful when the same checkout must work with Codex, OpenCode, and other Agent Skills-compatible clients. OpenCode's project-specific directory takes precedence when the same Skill name is present in multiple locations; avoid unintentionally maintaining divergent copies.

## GitHub Copilot

GitHub Copilot supports project Skills in `.github/skills`, `.claude/skills`, or `.agents/skills`, and personal Skills in `~/.copilot/skills` or `~/.agents/skills`. For a repository-local Copilot installation:

```bash
mkdir -p .github/skills
cp -R ../hyperos-hook-agent-skills/skills/hyperos4-rust-launcher-native-hook .github/skills/
```

Alternatively copy it to `.agents/skills` when sharing one installation with Codex. Copilot CLI also provides `gh skill` commands for discovering and installing Skills; a direct copy is deterministic for this repository and preserves the exact reviewed files.

## Verify the installation

Regardless of the client, verify that the final path ends in:

```text
<discovery-root>/hyperos4-rust-launcher-native-hook/SKILL.md
```

Check that the frontmatter `name` matches the directory name, `description` is present, and the `references/` and `evals/` directories remain beside `SKILL.md`. The Skill is instruction-only: it does not install packages, modify a device, reboot a Launcher, or include proprietary APKs.

## Sources

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Codex Skills](https://developers.openai.com/codex/skills/)
- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [OpenCode Agent Skills](https://opencode.ai/docs/skills/)
- [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)
