# 🤖 AI-Code-Reviewer

An AI-powered Python tool that integrates into Git as a pre-commit hook to automatically review staged code changes using the OpenAI API — catching issues *before* they are committed.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-API-412991?style=for-the-badge&logo=openai&logoColor=white)
![Git](https://img.shields.io/badge/Git-Hooks-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 📌 Overview

AI-Code-Reviewer is a Python-based tool that integrates into Git as a pre-commit hook to automatically review staged changes and provide feedback using the OpenAI API. It helps catch logic issues, anti-patterns, risky constructs and missing edge-cases *before* code is committed to the repository.

---

## ✨ Features

- Runs as a `.git/hooks/pre-commit` script and scans only staged file diffs
- Uses the OpenAI API to analyze code changes and return review feedback
- Filters out irrelevant file paths to minimise noise
- Supports Windows (PowerShell) and Unix-style shells
- Handles Unicode decoding, binary files and safe Git repository handling reliably
- Outputs results directly in the terminal before the commit completes

---

## 🔄 How It Works

1. Developer stages changes in Git (`git add`)
2. The pre-commit hook triggers AI-Code-Reviewer automatically
3. The tool extracts staged diffs and sends them to the OpenAI model
4. The AI returns human-style review comments highlighting issues and improvements
5. The commit proceeds after the developer reviews the flagged items

---

## 🗂️ Repository Structure
```
ai-code-reviewer/
├── tools/
│   └── ai_code_reviewer.py   # Main Python script
├── .git/hooks/
│   └── pre-commit            # Git pre-commit hook
├── .env                      # Stores OpenAI API key (not committed)
├── .gitignore
├── .gitattributes
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- OpenAI API key

### Installation
```bash
# Clone the repository
git clone https://github.com/Vihar2002/AI-Code-Reviewer.git
cd AI-Code-Reviewer

# Install dependencies
pip install -r requirements.txt

# Copy the pre-commit hook
cp .git_hooks/pre-commit .git/hooks/pre-commit

# Make it executable (Unix/Mac)
chmod +x .git/hooks/pre-commit
```

### Windows (PowerShell)
```powershell
# Allow script execution
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

# Fix safe directory if needed
git config --global --add safe.directory your/repo/path

# Set hook permissions
git update-index --chmod=+x .git/hooks/pre-commit
```

---

## ⚙️ Configuration

Create a `.env` file in the root directory:
```
OPENAI_API_KEY=your_key_here
```

---

## 💻 Example Output
```
AI Code Review — file.py
--------------------------------------------------
⚠️  Division by zero detected on line 12.
⚠️  Unhandled exception in function process_data().
📝  TODO comment found on line 34 — consider resolving before commit.
--------------------------------------------------
Review complete. Proceed with commit? (y/n):
```

---

## 🔮 Future Improvements

- Support for multiple AI models (GPT-4, Claude, etc.)
- Severity levels for review comments (critical, warning, info)
- HTML/Markdown report export
- CI/CD pipeline integration

---

## 👤 Author

**Vihar Yeole**
[LinkedIn](https://www.linkedin.com/in/viharyeole/) • [GitHub](https://github.com/Vihar2002)
