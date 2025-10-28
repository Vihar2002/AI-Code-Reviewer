#!/usr/bin/env python3
"""
Step 2 – Diff-aware pre-commit reviewer.
Scans only staged diffs, reports modified lines containing potential issues.
(Still no AI yet — just diff parsing logic.)
"""

import subprocess
import sys
from pathlib import Path

ALLOWED_EXTS = {".py", ".js", ".ts", ".tsx", ".java", ".go", ".rb", ".cs"}

# Ignore our own tooling folder during development
IGNORE_PATH_PREFIXES = {Path("tools")}
IGNORE_FILES = {Path("tools") / "ai_code_reviewer.py"}


def run(cmd):
    """Run shell command and return stdout (UTF-8 safe for Windows)."""
    try:
        return subprocess.check_output(cmd, text=True, encoding="utf-8", errors="ignore")
    except subprocess.CalledProcessError:
        return ""


def get_staged_diffs():
    """Return staged diff (unified format)."""
    return run(["git", "diff", "--cached", "--unified=0", "--diff-filter=ACM"])


def parse_diffs(diff_text):
    """
    Parse git diff output → list of (file_path, line_number, line_text)
    for each added/modified line.
    """
    results = []
    current_file = None
    for line in diff_text.splitlines():
        if line.startswith("+++ b/"):
            current_file = Path(line[6:].strip())
        elif line.startswith("@@") and current_file:
            try:
                header = line.split(" ")[2]  # +13,2
                start_line = int(header.split(",")[0][1:])
                line_no = start_line
            except Exception:
                continue
        elif line.startswith("+") and not line.startswith("+++"):
            results.append((current_file, line_no, line[1:].rstrip()))
            line_no += 1
    return results


def main():
    diff_text = get_staged_diffs()
    if not diff_text.strip():
        print("[ai-review] No staged diffs found.")
        return 0

    added_lines = parse_diffs(diff_text)
    issues = []

    for path, lineno, text in added_lines:
        # skip files in our tools folder and the reviewer itself to avoid self-blocking
        if any(path == p or (p in path.parents) for p in IGNORE_FILES) or (path.parts and path.parts[0] == "tools"):
            continue

        if path.suffix not in ALLOWED_EXTS:
            continue
        if "TODO" in text or "FIXME" in text:
            issues.append(f"{path}:{lineno}: contains TODO/FIXME")
        if len(text) > 120:
            issues.append(f"{path}:{lineno}: line exceeds 120 chars")
        if "print(" in text and path.suffix == ".py":
            issues.append(f"{path}:{lineno}: avoid print statements in production code")

    if issues:
        print("❌ Commit blocked by ai-review (diff scan):")
        for msg in issues:
            print("  -", msg)
        print("\nFix or bypass with `git commit --no-verify` (not recommended).")
        return 1

    print("✅ ai-review: no issues found in staged changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
