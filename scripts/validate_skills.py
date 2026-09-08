#!/usr/bin/env python3
"""Validate every SKILL.md in skills/ against the Agent Skills specification.

Spec: https://agentskills.io/specification

Checks the rules that actually break skill loading:
  - SKILL.md exists and has YAML frontmatter delimited by ---
  - `name` and `description` are present
  - `name` matches its parent folder exactly
  - `name` is lowercase letters, digits and hyphens, does not start or end with a hyphen,
    and is at most 64 characters
  - `description` is at most 1024 characters and says both what the skill does and when to
    use it
  - no angle brackets anywhere in the frontmatter, which can inject into a system prompt

Exit code 0 if every skill is valid, 1 otherwise.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
# "when to use" signals - a description that never says when is a description that
# never activates at the right moment.
WHEN_SIGNALS = ("use when", "use this when", "use it when", "use before", "use after")

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Minimal frontmatter parse: top-level `key: value`, values may be folded."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None
    fields: dict[str, str] = {}
    key = None
    for line in match.group(1).splitlines():
        if re.match(r"^[A-Za-z0-9_-]+:", line):
            key, _, value = line.partition(":")
            key = key.strip()
            fields[key] = value.strip()
        elif key and line.strip():
            fields[key] = (fields[key] + " " + line.strip()).strip()
    return fields


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.is_file():
        return [f"{skill_dir.name}: no SKILL.md"]

    text = skill_md.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    if fields is None:
        return [f"{skill_dir.name}: no YAML frontmatter delimited by ---"]

    name = fields.get("name")
    description = fields.get("description")

    if not name:
        errors.append(f"{skill_dir.name}: frontmatter is missing `name`")
    else:
        if name != skill_dir.name:
            errors.append(f"{skill_dir.name}: `name` is '{name}' but must match the folder name")
        if not NAME_RE.match(name):
            errors.append(f"{skill_dir.name}: `name` must be lowercase letters, digits and hyphens")
        if len(name) > 64:
            errors.append(f"{skill_dir.name}: `name` is {len(name)} characters, limit is 64")

    if not description:
        errors.append(f"{skill_dir.name}: frontmatter is missing `description`")
    else:
        if len(description) > 1024:
            errors.append(
                f"{skill_dir.name}: `description` is {len(description)} characters, limit is 1024"
            )
        if not any(signal in description.lower() for signal in WHEN_SIGNALS):
            errors.append(
                f"{skill_dir.name}: `description` should say when to use the skill, "
                "not only what it does"
            )

    if "<" in str(fields) or ">" in str(fields):
        errors.append(f"{skill_dir.name}: frontmatter contains angle brackets; remove them")

    return errors


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"no skills directory at {SKILLS_DIR}")
        return 1

    skills = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skills:
        print("no skills found")
        return 1

    all_errors: list[str] = []
    for skill in skills:
        errors = validate(skill)
        if errors:
            all_errors.extend(errors)
            for error in errors:
                print(f"  FAIL  {error}")
        else:
            desc_len = len(parse_frontmatter((skill / "SKILL.md").read_text(encoding="utf-8"))["description"])
            print(f"  ok    {skill.name}  (description {desc_len}/1024 chars)")

    print()
    if all_errors:
        print(f"{len(all_errors)} problem(s) across {len(skills)} skill(s).")
        return 1
    print(f"All {len(skills)} skills conform to the Agent Skills specification.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
