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
1. Clone the Repository
git clone https://github.com/Vihar2002/AI-Code-Reviewer.git
cd AI-Code-Reviewer

2. Create a Virtual Environment
python -m venv .venv


Activate it:

Windows

.\.venv\Scripts\activate


Linux / macOS

source .venv/bin/activate

3. Install Dependencies
pip install openai python-dotenv

4. Add Your OpenAI API Key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

5. Set Up the Pre-Commit Hook

Create .git/hooks/pre-commit and add:

#!/usr/bin/env bash
set -euo pipefail
PY=".venv/Scripts/python.exe"
echo "[pre-commit] running ai_code_reviewer.py"
$PY tools/ai_code_reviewer.py


Make it executable:

git update-index --chmod=+x .git/hooks/pre-commit

Usage

After setup, every time you commit changes:

git commit -m "your commit message"


The script analyzes the modified code and prints an AI-generated review before allowing the commit.

Example Output
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

Add severity levels for feedback

Enable JSON output for CI/CD pipelines

Support concurrent analysis for large commits

This version is ready to copy directly into your GitHub repository as README.md. It will render perfectly with proper headings, indentation, and code blocks.
