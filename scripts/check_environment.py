#!/usr/bin/env python3
"""Check whether grounded-cv can render and verify CVs on this machine.

This is intentionally diagnostic, not an installer. It reports the commands the user still needs
rather than silently changing the environment.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def command_version(command: str, args: list[str]) -> tuple[bool, str]:
    exe = shutil.which(command)
    if not exe:
        return False, "not found"
    try:
        result = subprocess.run([exe, *args], capture_output=True, text=True, timeout=20)
    except Exception as exc:  # pragma: no cover - defensive diagnostic
        return False, f"found at {exe}, but version check failed: {exc}"
    output = (result.stdout or result.stderr).strip()
    line = (output.splitlines() or [exe])[0]
    if result.returncode != 0:
        return False, f"found at {exe}, but version check exited {result.returncode}: {line}"
    return True, line


def main() -> int:
    checks = [
        ("python", True, True, f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"),
    ]

    rendercv_ok, rendercv_msg = command_version("rendercv", ["--version"])
    pdftotext_ok, pdftotext_msg = command_version("pdftotext", ["-v"])

    checks.extend([
        ("rendercv", rendercv_ok, True, rendercv_msg),
        ("pdftotext", pdftotext_ok, False, pdftotext_msg),
    ])

    try:
        import yaml  # noqa: F401
        yaml_ok = True
        yaml_msg = "PyYAML import ok"
    except ImportError:
        yaml_ok = False
        yaml_msg = "PyYAML not installed"
    checks.append(("PyYAML", yaml_ok, True, yaml_msg))

    print("grounded-cv environment check")
    print()
    failures = 0
    for name, ok, required, message in checks:
        status = "ok" if ok else ("FAIL" if required else "WARN")
        print(f"  {status:<4} {name:<10} {message}")
        if required and not ok:
            failures += 1

    print()
    if sys.version_info < (3, 12):
        print("  WARN Python 3.12+ is recommended because RenderCV requires it.")

    if not rendercv_ok:
        print('  fix  uv tool install "rendercv[full]" --python 3.13')
    if not yaml_ok:
        print("  fix  python -m pip install -r scripts/requirements.txt")
    if not pdftotext_ok:
        print("  note install Poppler to enable ATS text-layer checks in scripts/verify.py")

    example_cv = ROOT / "examples" / "sample-profile" / "cv" / "master.yaml"
    if example_cv.is_file():
        print("  next python scripts/verify.py --cv-dir examples/sample-profile/cv --redlines examples/sample-profile/redlines.yaml")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
