#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

ALLOWED_EXTS = {".py", ".js", ".ts", ".tsx", ".java", ".go", ".rb", ".cs"}
IGNORE_PATH_PREFIXES = {Path("tools")}
IGNORE_FILES = {Path("tools") / "ai_code_reviewer.py"}


def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True, encoding="utf-8", errors="ignore")
    except subprocess.CalledProcessError:
        return ""


def get_staged_diffs():
    return run(["git", "diff", "--cached", "--unified=0", "--diff-filter=ACM"])


def parse_diffs(diff_text):
    results = []
    current_file = None
    for line in diff_text.splitlines():
        if line.startswith("+++ b/"):
            current_file = Path(line[6:].strip())
        elif line.startswith("@@") and current_file:
            try:
                header = line.split(" ")[2]
                start_line = int(header.split(",")[0][1:])
                line_no = start_line
            except Exception:
                continue
        elif line.startswith("+") and not line.startswith("+++"):
            results.append((current_file, line_no, line[1:].rstrip()))
            line_no += 1
    return results


def call_ai_reviewer(file_path, code_chunk):
    prompt = f"""
You are a senior software engineer reviewing a commit diff.
Identify code issues, risks, or bad practices.
Provide 3–5 short and clear bullet points.

File: {file_path}
Diff:
{code_chunk}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert code reviewer."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[AI ERROR: {e}]"


def main():
    diff_text = get_staged_diffs()
    if not diff_text.strip():
        print("[ai-review] No staged diffs found.")
        return 0

    added_lines = parse_diffs(diff_text)
    review_batches = {}

    for path, lineno, text in added_lines:
        if any(path == p or (p in path.parents) for p in IGNORE_FILES) or (path.parts and path.parts[0] == "tools"):
            continue
        if path.suffix not in ALLOWED_EXTS:
            continue
        review_batches.setdefault(path, []).append(f"{lineno}: {text}")

    if not review_batches:
        print("[ai-review] No eligible code changes for review.")
        return 0

    print("[ai-review] Sending code changes for AI analysis...")

    for file_path, lines in review_batches.items():
        snippet = "\n".join(lines[:30])
        feedback = call_ai_reviewer(file_path, snippet)
        print(f"\nFile: {file_path}")
        print("-" * 50)
        print(feedback)
        print("-" * 50)

    print("\n[ai-review] Analysis complete. Commit proceeds.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
