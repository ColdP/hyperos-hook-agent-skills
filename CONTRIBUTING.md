# Contributing

Contributions to `hyperos-hook-agent-skills` are welcome. This repository collects reusable Agent Skills for evidence-based HyperOS analysis and native Hook development. Keep contributions focused, reproducible, and safe to publish.

## Before opening a change

1. Read the target Skill's `SKILL.md` and the [Agent Skills specification](https://agentskills.io/specification).
2. Check the existing Git status and preserve unrelated work.
3. Do not add proprietary APKs, decompiled source, private keys, device logs containing personal data, or credentials.
4. For technical findings, record the artifact identity and use the repository evidence labels: `DEVICE_VERIFIED`, `STATICALLY_VERIFIED`, `INFERRED`, or `UNKNOWN`.

## Skill changes

- Keep each `SKILL.md` focused on one capability and keep detailed procedures in `references/`.
- Use lowercase letters, numbers, and hyphens for Skill directory names; the frontmatter `name` must match the directory name.
- Make the `description` say what the Skill does and when it should trigger.
- Use relative links from `SKILL.md` to references and keep linked files in the same Skill directory.
- Never present an offset, ABI, symbol, object layout, or test result from one Launcher version as universal.
- Separate compilation, library loading, and functional behavior in every validation report.

## Documentation and language

Update the matching English and Chinese documentation when changing user-facing repository guidance. Keep commands copyable and state platform-specific paths explicitly. If a public source supports a workflow claim, link it in the relevant guide.

## Validation

Run these checks before submitting a pull request:

```bash
python <path-to-quick_validate.py> skills/hyperos4-rust-launcher-native-hook
python scripts/validate_repo.py
git diff --check
```

Also verify all local Markdown links and inspect the final diff for accidental binary files or secrets. The GitHub Actions workflow runs the same checks on pushes and pull requests.

## Pull requests

Describe the user problem, the changed Skill or documentation, evidence status, validation commands, and any remaining unknowns. Keep the pull request small enough to review. Do not commit generated artifacts unless the repository explicitly requires them.

## License

By submitting a contribution, you agree that it is provided under the [Apache License 2.0](LICENSE), subject to the license's terms. Contributions must be your own work or clearly identified work that you are authorized to redistribute.
