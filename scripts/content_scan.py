from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

BLOCKED_PATTERNS = {
    "original_repo_name": re.compile(r"\bbim-balance\b", re.IGNORECASE),
    "reserved_email": re.compile(r"@[a-z0-9.-]*believeinme\.de", re.IGNORECASE),
    "local_reserved_path": re.compile(r"/Users/Heineken/(BiM|Downloads/BiM)"),
    "credential_marker": re.compile(r"BEGIN OPENSSH .* KEY|\bSECRET\b|\bTOKEN\b|api[_-]?key|password", re.IGNORECASE),
}

SKIP_DIRS = {".git", ".venv", "__pycache__", ".pytest_cache"}
TEXT_SUFFIXES = {".md", ".py", ".toml", ".txt", ".json", ".gitignore", ""}


def main() -> int:
    findings: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.parts):
            continue
        if path == Path(__file__).resolve():
            continue
        if path.suffix not in TEXT_SUFFIXES and path.name != "Makefile":
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in BLOCKED_PATTERNS.items():
            if pattern.search(text):
                findings.append(f"{path.relative_to(ROOT)}: {label}")

    if findings:
        print("Content scan failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Content scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
