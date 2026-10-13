"""Validate this repository's Skill metadata and local Markdown links."""

from pathlib import Path
import re
import sys

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "hyperos4-rust-launcher-native-hook"


def main() -> int:
    errors: list[str] = []
    required = [
        "LICENSE",
        "README.md",
        "README_zh.md",
        "INSTALL.md",
        "INSTALL_zh.md",
        "CONTRIBUTING.md",
        "CONTRIBUTING_zh.md",
        ".github/workflows/validate.yml",
    ]
    for path in required:
        if not (ROOT / path).is_file():
            errors.append(f"missing required file: {path}")

    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    parts = skill_text.split("---", 2)
    if len(parts) != 3:
        errors.append("SKILL.md has no valid YAML frontmatter")
    else:
        metadata = yaml.safe_load(parts[1]) or {}
        if metadata.get("name") != SKILL.name:
            errors.append("Skill name does not match directory")
        if metadata.get("license") != "Apache-2.0":
            errors.append("Skill license is not Apache-2.0")

    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for document in ROOT.rglob("*.md"):
        for target in pattern.findall(document.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            local_target = target.split("#", 1)[0]
            if local_target and not (document.parent / local_target).exists():
                errors.append(f"broken link: {document} -> {target}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository Skill metadata, required files, and local Markdown links are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
