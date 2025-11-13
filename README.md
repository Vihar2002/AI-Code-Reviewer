# AI-Code-Reviewer

## Overview  
AI-Code-Reviewer is a Python-based tool that integrates into Git as a pre-commit hook to automatically review staged changes and provide feedback using the OpenAI API. It helps catch logic issues, anti-patterns, risky constructs and missing edge-cases *before* code is committed to the repository.

## Features  
- Runs as a `.git/hooks/pre-commit` script and scans only staged file diffs.  
- Uses the OpenAI API (via Python) to analyze code changes and return review feedback.  
- Filters out irrelevant file paths (configured for your project structure) to minimise noise.  
- Supports Windows (PowerShell) and Unix-style shells.  
- Handles Unicode, binary files and safe Git repository handling (`safe.directory`) reliably.  
- Outputs results in the terminal, giving developers instant insights.  
- Full documentation included in `README.md`, with setup instructions, examples and good practise guidelines.

## Use Case  
1. Developer stages changes in Git (`git add`).  
2. The pre-commit hook triggers AI-Code-Reviewer.  
3. The tool sends the diff to OpenAI, analyses it, and returns human-style feedback.  
4. If issues are flagged, the commit is blocked (or a warning shown) and the developer reviews and resolves before proceeding.  
5. Commit proceeds once all checks pass.

## Getting Started  
### Prerequisites  
- Python 3.8+  
- Git  
- An OpenAI API key (set in environment variable `OPENAI_API_KEY`)  
- Clone or download this repository  
- Make the pre-commit hook executable (`chmod +x .git/hooks/pre-commit`) or link it into your Git hooks directory  

### Installation  
```bash
git clone https://github.com/Vihar2002/AI-Code-Reviewer.git  
cd AI-Code-Reviewer  
# Copy or symlink the pre-commit script into .git/hooks/  
cp tools/pre_commit_hook.sh .git/hooks/pre-commit  
chmod +x .git/hooks/pre-commit  
