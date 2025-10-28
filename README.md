AI Code Reviewer
Overview

AI Code Reviewer is a Python automation tool that integrates with Git to perform automatic code review before each commit.
It scans only the staged changes, sends them to the OpenAI API, and returns focused feedback on potential issues and code quality.

Key Features

Analyzes only modified lines in a commit

Runs automatically via Git pre-commit hook

Uses OpenAI for context-aware code feedback

Supports multiple programming languages

Simple integration with any local Git repository

Supported Languages

.py, .js, .ts, .tsx, .java, .go, .rb, .cs

Setup

Clone the repository

git clone https://github.com/Vihar2002/AI-Code-Reviewer.git
cd AI-Code-Reviewer


Create a virtual environment

python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac


Install dependencies

pip install openai python-dotenv


Add your OpenAI API key
Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


Set up the pre-commit hook
Create .git/hooks/pre-commit:

#!/usr/bin/env bash
set -euo pipefail
PY=".venv/Scripts/python.exe"
echo "[pre-commit] running ai_code_reviewer.py"
$PY tools/ai_code_reviewer.py

Usage

After setup, every time you commit changes:

git commit -m "your commit message"


The script analyzes the new code and prints a short AI review before allowing the commit.

Example:

[ai-review] Sending code changes for AI analysis...
File: test.py
--------------------------------------------------
- Division by zero detected
- Remove print statements
- Incomplete TODO comment
--------------------------------------------------
[ai-review] Analysis complete. Commit proceeds.

Repository Structure
AI-Code-Reviewer/
├── tools/
│   └── ai_code_reviewer.py
├── .gitignore
├── .gitattributes
├── README.md
└── test.py

Future Improvements

Severity levels for feedback

JSON output for CI/CD systems

Parallel analysis for large commits
