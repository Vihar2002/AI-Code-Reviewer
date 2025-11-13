# AI-Code-Reviewer

## Overview  
AI-Code-Reviewer is a Python-based tool that integrates into Git as a pre-commit hook to automatically review staged changes and provide feedback using the OpenAI API. It helps catch logic issues, anti-patterns, risky constructs and missing edge-cases *before* code is committed to the repository.

## Features  
- Runs as a `.git/hooks/pre-commit` script and scans only staged file diffs.  
- Uses the OpenAI API (via Python) to analyze code changes and return review feedback.  
- Filters out irrelevant file paths to minimise noise.  
- Supports Windows (PowerShell) and Unix-style shells.  
- Handles Unicode decoding, binary files and safe Git repository handling (`safe.directory`) reliably.  
- Outputs results directly in the terminal before the commit completes.  
- Includes complete documentation, examples and recommended best practices.

## Use Case  
1. Developer stages changes in Git (`git add`).  
2. The pre-commit hook triggers AI-Code-Reviewer.  
3. The tool extracts staged diffs and sends them to the OpenAI model for analysis.  
4. The AI returns human-style review comments highlighting issues and potential improvements.  
5. The commit proceeds after the developer resolves the flagged items or chooses to override.

## Getting Started  

### Prerequisites  
- Python 3.8+  
- Git  
- An OpenAI API key stored in `.env` or environment variable `OPENAI_API_KEY`  
- Git hook permissions enabled  
- Clone or download this repository  

### Installation  
```bash
git clone https://github.com/Vihar2002/AI-Code-Reviewer.git
cd AI-Code-Reviewer

# Install dependencies
pip install -r requirements.txt

# Copy or symlink the pre-commit hook
cp .git_hooks/pre-commit .git/hooks/pre-commit

# Make it executable (Unix)
chmod +x .git/hooks/pre-commit
