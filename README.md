# GenerativeAI Projects - Setup & Usage Guide

## Project Details
- **Python Version**: 3.13.7
- **Package Manager**: uv (fast, modern alternative to pip)
- **Primary Dependency**: LangChain
- **Environment**: Windows virtual environment

---

## Project Files & Purpose

### Core Project Files

| File/Folder | Purpose | Content |
|------------|---------|---------|
| **pyproject.toml** | Project configuration & dependencies | Defines project metadata, Python version (3.13+), and all package requirements |
| **uv.lock** | Dependency lock file | Freezes exact package versions for reproducible builds across environments |
| **main.py** | Application entry point | Contains your Python code and LangChain implementations |
| **.python-version** | Python version specification | Specifies Python 3.13.7 for this project |
| **.venv/** | Virtual environment directory | Isolated Python environment with all installed packages (Windows structure with `Scripts/` folder) |
| **README.md** | Project documentation | This file - setup guide and usage instructions |

### Virtual Environment Structure (.venv)
```
.venv/
├── Scripts/           # Windows executables
│   ├── python.exe     # Python interpreter
│   ├── pip.exe        # Package installer
│   ├── activate        # Bash activation script
│   ├── activate.bat    # Command Prompt activation
│   └── Activate.ps1   # PowerShell activation script
├── Lib/               # Installed packages
│   └── site-packages/ # LangChain, dependencies, etc.
└── pyvenv.cfg         # Virtual environment configuration
```

---

## Setup Instructions

### Step 1: Fix PowerShell Execution Policy
If you encounter script execution error:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
**Why**: Windows blocks script execution by default for security. `RemoteSigned` allows local scripts.

### Step 2: Activate Virtual Environment
```powershell
.venv\Scripts\activate
```
**Indicator**: Prompt will show `(GenerativeAI Projects)` prefix.

### Step 3: Initialize Project (One-time)
```bash
uv init
```
**Creates**: `pyproject.toml`, `uv.lock`, `.python-version`

### Step 4: Add Dependencies
```bash
uv add langchain
```
**Updates**: `pyproject.toml` and `uv.lock` with LangChain + 32 dependencies.

---

## Common Development Tasks

### Run Python Code
```bash
python main.py
```

### Add New Package
```bash
uv add <package-name>
# Examples:
uv add requests
uv add pandas numpy
```

### Install All Dependencies (from lock file)
```bash
uv sync
```

### Activate/Deactivate Environment
```powershell
# Activate
.venv\Scripts\activate

# Deactivate
deactivate
```

### Check Active Environment
```bash
python --version  # Shows Python from virtual environment
```

---

## Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| Script execution blocked | Run: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `uv add` fails with "No pyproject.toml" | Run: `uv init` first |
| Prompt doesn't show `(GenerativeAI Projects)` | Ensure venv is activated and you're in correct directory |
| Import errors | Confirm virtual environment is activated before running code |

---

## Best Practices

✅ **Do**: 
- Always activate `.venv\Scripts\activate` before development
- Use `uv add` for new packages (not `pip install`)
- Commit `pyproject.toml` and `uv.lock` to version control

❌ **Don't**:
- Commit `.venv/` folder to version control
- Manually edit `pyproject.toml` dependencies (use `uv add`)
- Run Python outside the activated virtual environment

---

## Project Structure
```
E:\GenerativeAI Projects\
├── main.py              # Your Python code here
├── pyproject.toml       # Dependencies & project config
├── uv.lock             # Locked dependency versions
├── .python-version     # Python 3.13.7 specification
├── README.md           # This documentation
└── .venv/              # Virtual environment (do not edit)