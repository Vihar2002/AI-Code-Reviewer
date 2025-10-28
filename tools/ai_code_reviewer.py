#!/usr/bin/env python3
"""
Minimal pre-commit sanity check.
Blocks commit if staged files contain "TODO" or any line > 120 chars.
This proves the hook pipeline works before we add AI.
"""
import subprocess
import sys
from pathlib import Path

ALLOWED_EXTS = {".py", ".js", ".ts", ".tsx", ".java", ".go", ".rb", ".cs"}

def run(cmd):
    return subprocess.check_output(cmd, text=True).strip()

def staged_files():
    out = run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"])
    files = [Path(p) for p in out.splitlines() if p.strip()]
    return [p for p in files if p.suffix in ALLOWED_EXTS and p.exists()]

def scan(path: Path):
    problems = []
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f, start=1):
            if "TODO" in line:
                problems.append(f"{path}:{i}: contains 'TODO'")
            if len(line.rstrip("\n")) > 120:
                problems.append(f"{path}:{i}: line > 120 chars")
    return problems

def main():
    files = staged_files()
    if not files:
        print("[ai-review] No staged source files. Skipping.")
        return 0
    all_issues = []
    for p in files:
        all_issues.extend(scan(p))
    if all_issues:
        print("❌ Commit blocked by ai-review (bootstrap checks):")
        for msg in all_issues:
            print("  -", msg)
        print("\nFix or bypass with `git commit -m \"msg\" --no-verify` (not recommended).")
        return 1
    print("✅ ai-review: no issues found (bootstrap stage).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
