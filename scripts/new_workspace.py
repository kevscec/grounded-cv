#!/usr/bin/env python3
"""Scaffold workspace/ from the templates.

Creates the directories a session needs and copies in the core knowledge-base files, the
shared CV design block, and a starter redlines file. Never overwrites anything that already
exists.

Usage:
    python scripts/new_workspace.py                 # core knowledge base (5 files)
    python scripts/new_workspace.py --tier recommended
    python scripts/new_workspace.py --tier all
    python scripts/new_workspace.py --from-example  # start from the sample profile
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / "templates"
WORKSPACE = ROOT / "workspace"

CORE = [
    "00_START_HERE.md",
    "01_IDENTITY_AND_FACTS.md",
    "08_IMPACT_LEDGER.md",
    "10_CLAIMS_REGISTER.md",
    "11_GAPS.md",
]
RECOMMENDED = CORE + [
    "02_POSITIONING.md",
    "03_CAPABILITY_MAP.md",
    "05_PROJECTS.md",
    "13_BULLET_LIBRARY.md",
]


def copy(src: Path, dst: Path, created: list[str], skipped: list[str]) -> None:
    if dst.exists():
        skipped.append(str(dst.relative_to(ROOT)))
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    created.append(str(dst.relative_to(ROOT)))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--tier", choices=["core", "recommended", "all"], default="core")
    parser.add_argument("--from-example", action="store_true",
                        help="seed the knowledge base from examples/sample-profile instead of blank templates")
    args = parser.parse_args()

    created: list[str] = []
    skipped: list[str] = []

    for sub in ("knowledge-base", "cv", "applications"):
        (WORKSPACE / sub).mkdir(parents=True, exist_ok=True)

    kb_src = ROOT / "examples" / "sample-profile" / "knowledge-base" if args.from_example else TEMPLATES / "knowledge-base"
    if not kb_src.is_dir():
        print(f"Source directory not found: {kb_src}")
        return 1

    if args.from_example:
        wanted = sorted(p.name for p in kb_src.glob("*.md") if p.name != "README.md")
    elif args.tier == "core":
        wanted = CORE
    elif args.tier == "recommended":
        wanted = RECOMMENDED
    else:
        wanted = sorted(p.name for p in kb_src.glob("*.md") if p.name != "README.md")

    for filename in wanted:
        src = kb_src / filename
        if src.is_file():
            copy(src, WORKSPACE / "knowledge-base" / filename, created, skipped)

    copy(TEMPLATES / "cv-build" / "design.yaml", WORKSPACE / "cv" / "design.yaml", created, skipped)
    copy(TEMPLATES / "cv-build" / "CONTENT_MAP.md", WORKSPACE / "cv" / "CONTENT_MAP.md", created, skipped)
    copy(TEMPLATES / "config" / "redlines.example.yaml", WORKSPACE / "redlines.yaml", created, skipped)

    for path in created:
        print(f"  created  {path}")
    for path in skipped:
        print(f"  kept     {path}  (already existed)")

    print()
    if args.from_example:
        print("Workspace seeded from the sample profile. That profile is fictional - replace")
        print("its content with your own before generating anything you intend to send.")
    else:
        print(f"Workspace ready ({args.tier} tier). Next:")
        print("  1. Edit workspace/redlines.yaml - your name, contacts, and anything that")
        print("     must never appear in a document.")
        print("  2. Ask your agent to read AGENTS.md and start the knowledge-base interview.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
