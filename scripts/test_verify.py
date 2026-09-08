#!/usr/bin/env python3
"""Negative controls for verify.py.

A check that never fires is worse than no check, because it produces false confidence.
This suite plants a specific violation for each check and asserts that verify.py catches it,
then asserts the unmodified sample profile still passes.

Usage:
    python scripts/test_verify.py

Exit code 0 if every control behaves as expected, 1 otherwise.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXAMPLE = ROOT / "examples" / "sample-profile"

GREEN, RED, RESET = "\033[32m", "\033[31m", "\033[0m"
if not sys.stdout.isatty() and not os.environ.get("GITHUB_ACTIONS"):
    GREEN = RED = RESET = ""


def run_verify(workdir: Path) -> tuple[int, str]:
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "verify.py"),
         "--cv-dir", str(workdir / "cv"),
         "--redlines", str(workdir / "redlines.yaml")],
        capture_output=True, text=True, encoding="utf-8", errors="replace", env=env,
    )
    return result.returncode, (result.stdout or "") + (result.stderr or "")


def fresh_copy(tmp: Path, name: str) -> Path:
    workdir = tmp / name
    (workdir / "cv").mkdir(parents=True)
    for filename in ("master.yaml", "design.yaml"):
        shutil.copy2(EXAMPLE / "cv" / filename, workdir / "cv" / filename)
    shutil.copy2(EXAMPLE / "redlines.yaml", workdir / "redlines.yaml")
    return workdir


def patch(path: Path, old: str, new: str) -> None:
    text = path.read_text(encoding="utf-8")
    if old not in text:
        raise AssertionError(f"test fixture is stale: {old[:60]!r} not found in {path.name}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")


# Each control: (name, mutate function, regex the failure output must match)
CONTROLS = [
    (
        "literal redline",
        lambda w: patch(w / "cv" / "master.yaml",
                        "Data Platform team. Owns the batch platform behind retail analytics.",
                        "Data Platform team. Owns ORION, the batch platform behind retail analytics."),
        r"redline 'ORION' appears",
    ),
    (
        "forbidden pattern (national ID)",
        lambda w: patch(w / "cv" / "master.yaml",
                        "location: Lisbon, Portugal",
                        "location: Lisbon, Portugal 1-2345-6789"),
        r"forbidden pattern .* matched",
    ),
    (
        "team metric without its attribution qualifier",
        lambda w: patch(w / "cv" / "master.yaml",
                        "Contributed to a self-serve reporting initiative that removed roughly **900",
                        "Removed roughly **900"),
        r"team metric '900' appears without an attribution qualifier",
    ),
    (
        "contact detail lost in extraction",
        lambda w: patch(w / "cv" / "master.yaml",
                        "    - network: GitHub\n      username: example-robin-doe\n", ""),
        r"contact detail .* did not survive text extraction",
    ),
    (
        "name is not the first line of the text stream",
        # The leading whitespace matters: `show_top_note: false` also appears in a comment
        # near the top of design.yaml, and patch() replaces the first occurrence only.
        lambda w: patch(w / "cv" / "design.yaml",
                        "    show_top_note: false", "    show_top_note: true"),
        r"first line of the text stream is .*, not the candidate name",
    ),
    (
        "page limit exceeded",
        lambda w: (
            shutil.copy2(w / "cv" / "master.yaml", w / "cv" / "padded_1page.yaml"),
            patch(w / "cv" / "padded_1page.yaml",
                  "      - company: Contoso Logistics",
                  "\n".join(["          - Filler bullet added by the test suite to push this "
                             "variant past a single page."] * 16)
                  + "\n\n      - company: Contoso Logistics"),
        ),
        r"padded_1page: rendered \d+ pages, this variant must be exactly 1",
    ),
]


def main() -> int:
    if not shutil.which("rendercv"):
        print("rendercv is not on PATH - cannot run the verification test suite")
        return 1

    failures = 0
    with tempfile.TemporaryDirectory() as raw_tmp:
        tmp = Path(raw_tmp)

        print("\n=== control: the unmodified sample profile must PASS ===")
        code, output = run_verify(fresh_copy(tmp, "clean"))
        if code == 0:
            print(f"  {GREEN}ok{RESET}    clean sample passes")
        else:
            failures += 1
            print(f"  {RED}FAIL{RESET}  clean sample should pass but did not:\n{output}")

        print("\n=== negative controls: each planted violation must be CAUGHT ===")
        for index, (name, mutate, expected) in enumerate(CONTROLS):
            workdir = fresh_copy(tmp, f"neg{index}")
            mutate(workdir)
            code, output = run_verify(workdir)
            if code == 0:
                failures += 1
                print(f"  {RED}FAIL{RESET}  {name}: verify.py passed a document it should have rejected")
            elif not re.search(expected, output):
                failures += 1
                print(f"  {RED}FAIL{RESET}  {name}: failed, but not for the expected reason")
                print(f"        expected to match: {expected}")
            else:
                print(f"  {GREEN}ok{RESET}    {name}")

    print()
    if failures:
        print(f"{RED}{failures} control(s) did not behave as expected.{RESET}")
        return 1
    print(f"{GREEN}All controls behaved as expected.{RESET} Every check fires on a real violation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
