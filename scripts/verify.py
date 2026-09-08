#!/usr/bin/env python3
"""Verify rendered CVs before they are sent.

Renders every CV YAML in the workspace, extracts each PDF's text layer the way an ATS parser
would, and fails on anything that must never reach an employer.

The point of this script is that redlines stop being something to remember and become
something the build enforces.

Usage:
    python scripts/verify.py                  # verify workspace/cv
    python scripts/verify.py --cv-dir DIR     # verify another directory
    python scripts/verify.py --redlines FILE  # use another redlines file

Exit code 0 if every check passes, 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML is required: pip install -r scripts/requirements.txt")

ROOT = Path(__file__).resolve().parent.parent

GREEN, RED, YELLOW, DIM, RESET = "\033[32m", "\033[31m", "\033[33m", "\033[2m", "\033[0m"
if not sys.stdout.isatty():
    GREEN = RED = YELLOW = DIM = RESET = ""

STANDARD_HEADINGS = ("Experience", "Education", "Skills")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []

    def ok(self, message: str) -> None:
        print(f"  {GREEN}ok{RESET}    {message}")

    def warn(self, message: str) -> None:
        self.warnings.append(message)
        print(f"  {YELLOW}WARN{RESET}  {message}")

    def fail(self, message: str) -> None:
        self.failures.append(message)
        print(f"  {RED}FAIL{RESET}  {message}")


def load_redlines(path: Path, report: Report) -> dict:
    if not path.is_file():
        report.warn(
            f"no redlines file at {path} - only generic checks will run. "
            "Copy templates/config/redlines.example.yaml to get the full set."
        )
        return {}
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def is_cv_file(path: Path) -> bool:
    """True for a RenderCV input file. Config files in the same directory are skipped."""
    try:
        with path.open(encoding="utf-8") as handle:
            return any(line.startswith("cv:") for line in handle)
    except OSError:
        return False


def render(yaml_path: Path, out_dir: Path, design: Path | None, report: Report) -> Path | None:
    """Render one CV. Returns the PDF path, or None if it could not be produced."""
    rendercv = shutil.which("rendercv")
    if not rendercv:
        report.fail("rendercv is not on PATH - install with: uv tool install \"rendercv[full]\"")
        return None

    # Clear stale PNGs so the page count is measured fresh. A PDF held open by a viewer
    # cannot be deleted on Windows; tolerate that and let rendercv overwrite it.
    if out_dir.is_dir():
        for png in out_dir.glob("*.png"):
            try:
                png.unlink()
            except OSError:
                pass

    # rendercv resolves -o relative to the input file, not the working directory.
    command = [rendercv, "render", str(yaml_path.resolve()), "-o", str(out_dir.resolve()),
               "-nomd", "-nohtml"]
    if design and design.is_file():
        command += ["-d", str(design.resolve())]

    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    pdfs = sorted(out_dir.glob("*.pdf")) if out_dir.is_dir() else []
    pdf = pdfs[0] if pdfs else None

    if result.returncode != 0:
        # A locked output file is tolerable ONLY when the existing PDF is newer than its
        # source. Otherwise the render failed for a real reason - a YAML error, say - and
        # auditing the old PDF would report a pass on content that is no longer current.
        if pdf and pdf.stat().st_mtime >= yaml_path.stat().st_mtime:
            report.warn(f"{yaml_path.name}: could not re-render (output locked); auditing the existing PDF")
            return pdf
        if pdf:
            report.fail(f"{yaml_path.name}: render failed and the existing PDF is OLDER than the source - it is stale")
        else:
            report.fail(f"{yaml_path.name}: render failed. Run rendercv directly to see the validation errors")
        detail = (result.stderr or result.stdout or "").strip().splitlines()
        for line in detail[-6:]:
            print(f"        {DIM}{line}{RESET}")
        return None

    if not pdf:
        report.fail(f"{yaml_path.name}: rendercv reported success but produced no PDF")
        return None

    report.ok(f"rendered {yaml_path.name}")
    return pdf


def extract_text(pdf: Path, report: Report) -> str | None:
    """Extract the PDF text layer exactly as an ATS parser would read it."""
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        report.warn(
            "pdftotext not found - text-layer checks skipped. Install Poppler to enable them; "
            "they are the ones that catch the expensive mistakes."
        )
        return None
    txt = pdf.with_suffix(".txt")
    subprocess.run(
        [pdftotext, "-layout", "-enc", "UTF-8", str(pdf), str(txt)],
        capture_output=True,
        check=False,
    )
    if not txt.is_file():
        report.warn(f"{pdf.name}: text extraction produced no output")
        return None
    return txt.read_text(encoding="utf-8", errors="replace")


def count_pages(pdf: Path) -> int | None:
    """Page count from the PNGs RenderCV emits, falling back to the PDF page tree."""
    pngs = list(pdf.parent.glob("*.png"))
    if pngs:
        return len(pngs)
    try:
        data = pdf.read_bytes()
    except OSError:
        return None
    matches = re.findall(rb"/Type\s*/Page[^s]", data)
    return len(matches) or None


def audit(yaml_path: Path, pdf: Path, text: str | None, redlines: dict, report: Report) -> None:
    name = yaml_path.stem

    # --- page count ---------------------------------------------------------------------
    limits = redlines.get("page_limits") or {}
    pages = count_pages(pdf)
    if pages is None:
        report.warn(f"{name}: could not determine the page count")
    else:
        limit = limits.get("default", 2)
        exact = None
        for pattern, value in limits.items():
            if pattern != "default" and re.fullmatch(pattern.replace("*", ".*"), yaml_path.name):
                exact = value
        if exact is not None and pages != exact:
            report.fail(f"{name}: rendered {pages} pages, this variant must be exactly {exact}")
        elif exact is None and pages > limit:
            report.fail(f"{name}: rendered {pages} pages, limit is {limit}")
        else:
            report.ok(f"{name}: {pages} page(s)")

    if text is None:
        return

    if len(text.strip()) < 400:
        report.fail(f"{name}: text layer is empty or implausibly short - an ATS would read nothing")
        return
    report.ok(f"{name}: text layer extracted ({len(text)} chars)")

    lines = [line for line in text.splitlines() if line.strip()]

    # --- the name must be the first line of the text stream -----------------------------
    candidate = redlines.get("candidate_name")
    if candidate and lines:
        if candidate.lower() not in lines[0].lower():
            report.fail(
                f"{name}: first line of the text stream is {lines[0].strip()!r}, not the "
                "candidate name - an ATS may mis-read the name field"
            )
        else:
            report.ok(f"{name}: name is the first line of the text stream")

    # --- contact details must survive extraction ----------------------------------------
    for contact in redlines.get("required_contact") or []:
        if contact.lower() not in text.lower():
            report.fail(f"{name}: contact detail {contact!r} did not survive text extraction")

    # --- literal redlines ---------------------------------------------------------------
    for entry in redlines.get("forbidden") or []:
        needle = entry["text"] if isinstance(entry, dict) else str(entry)
        reason = entry.get("reason", "") if isinstance(entry, dict) else ""
        if needle.lower() in text.lower():
            report.fail(f"{name}: redline {needle!r} appears in the document" + (f" - {reason}" if reason else ""))

    # --- regex redlines -----------------------------------------------------------------
    for entry in redlines.get("forbidden_patterns") or []:
        pattern = entry["pattern"] if isinstance(entry, dict) else str(entry)
        reason = entry.get("reason", "") if isinstance(entry, dict) else ""
        if re.search(pattern, text):
            report.fail(f"{name}: forbidden pattern {pattern!r} matched" + (f" - {reason}" if reason else ""))

    # --- attribution: team metrics need their qualifier ---------------------------------
    phrases = [p.lower() for p in (redlines.get("attribution_phrases") or [])]
    for metric in redlines.get("team_metrics") or []:
        for line in text.splitlines():
            if str(metric) not in line:
                continue
            if not any(phrase in line.lower() for phrase in phrases):
                report.fail(
                    f"{name}: team metric {metric!r} appears without an attribution "
                    f"qualifier: {line.strip()!r}"
                )

    # --- standard section headings ------------------------------------------------------
    for heading in STANDARD_HEADINGS:
        if not re.search(rf"(?mi)^\s*{heading}\b", text):
            report.warn(f"{name}: standard heading {heading!r} not found at a line start")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--cv-dir", type=Path, default=ROOT / "workspace" / "cv")
    parser.add_argument("--redlines", type=Path, default=ROOT / "workspace" / "redlines.yaml")
    parser.add_argument("--design", type=Path, default=None)
    args = parser.parse_args()

    report = Report()

    cv_dir: Path = args.cv_dir
    if not cv_dir.is_dir():
        print(f"No CV directory at {cv_dir}. Run: python scripts/new_workspace.py")
        return 1

    design = args.design or (cv_dir / "design.yaml")
    yamls = sorted(p for p in cv_dir.glob("*.yaml") if is_cv_file(p))
    if not yamls:
        print(f"No CV YAML files in {cv_dir} (a CV file has a top-level `cv:` key).")
        return 1

    redlines = load_redlines(args.redlines, report)

    print(f"\n{DIM}=== Rendering ==={RESET}")
    rendered: list[tuple[Path, Path]] = []
    for yaml_path in yamls:
        pdf = render(yaml_path, cv_dir / "out" / yaml_path.stem, design, report)
        if pdf:
            rendered.append((yaml_path, pdf))

    for yaml_path, pdf in rendered:
        print(f"\n{DIM}=== {yaml_path.stem} ==={RESET}")
        audit(yaml_path, pdf, extract_text(pdf, report), redlines, report)

    print(f"\n{DIM}=== Result ==={RESET}")
    if report.warnings:
        print(f"{YELLOW}{len(report.warnings)} warning(s){RESET}")
    if report.failures:
        print(f"{RED}{len(report.failures)} failure(s) - do not send these CVs{RESET}")
        return 1
    print(f"{GREEN}All checks passed.{RESET} Still walk the manual pass in the cv-verify skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
