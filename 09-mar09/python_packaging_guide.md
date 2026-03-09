# 🐍 Python Packaging for Beginners

> Learn how to create your own Python package, install it locally, and share it via GitHub — step by step.

---

## 📦 What is a Python Package?

A **package** is just a folder of Python files that you can import and reuse anywhere. Instead of copy-pasting code between projects, you install your package once and use it everywhere.

---

## 🗂️ Step 1 — Set Up Your Project Structure

Create the following folder and file structure on your computer:

```
cli_utils/
├── cli_utils/
│   ├── __init__.py
│   └── separators.py
├── pyproject.toml
└── README.md
```

### Create the folders

```bash
mkdir cli_utils
cd cli_utils
mkdir cli_utils
```

---

## ✍️ Step 2 — Write Your Package Code

### `cli_utils/__init__.py`

This file tells Python that this folder is a package. It can be empty, or you can use it to expose functions.

```python
# cli_utils/__init__.py
from .separators import print_separator
```

### `cli_utils/separators.py`

This is where your actual code lives. Start with one simple function:

```python
# cli_utils/separators.py

def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)
```

**What this function does:**
- Takes **no arguments**
- Prints exactly `30` asterisk (`*`) characters
- Returns **nothing** (`None`)

---

## ⚙️ Step 3 — Create `pyproject.toml`

This file tells Python how to build and install your package. Create it in the **root** `cli_utils/` folder (not inside the inner one):

```toml
# pyproject.toml

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "cli_utils"
version = "0.1.0"
description = "A small utility package for CLI separator functions"
readme = "README.md"
requires-python = ">=3.8"
```

---

## 📝 Step 4 — Add a README

Create a `README.md` in the root folder:

```markdown
# cli_utils

A beginner-friendly Python package with CLI utility functions.

## Usage

```python
from cli_utils import print_separator

print_separator()
# Output: ******************************
```
```

---

## 💻 Step 5 — Install the Package Locally

Now let's install your package so you can use it anywhere on your machine.

Open a terminal, navigate to the **root** project folder (the one containing `pyproject.toml`), and run:

```bash
pip install -e .
```

### What does `-e` mean?

The `-e` flag stands for **editable** (also called "development mode"). It means:
- Your package is installed, but Python reads directly from your source files
- Any change you make to your `.py` files is instantly reflected — no reinstalling needed!

### ✅ Verify it works

Open a Python shell or create a test file:

```python
# test_it.py
from cli_utils import print_separator

print_separator()
```

Run it:

```bash
python test_it.py
```

**Expected output:**
```
******************************
```

---

## 🐙 Step 6 — Push Your Package to GitHub

### 6a. Create a `.gitignore` file

Add this to avoid committing unnecessary files:

```
__pycache__/
*.egg-info/
dist/
build/
.venv/
```

### 6b. Initialize and push your repo

```bash
git init
git add .
git commit -m "Initial commit: cli_utils package"
```

Then go to [github.com](https://github.com), create a **new repository** called `cli_utils`, and follow the instructions to push:

```bash
git remote add origin https://github.com/YOUR_USERNAME/cli_utils.git
git branch -M main
git push -u origin main
```

---

## 🌐 Step 7 — Install Your Package from GitHub

Once your code is on GitHub, **anyone** (including you, on a new machine) can install it with:

```bash
pip install git+https://github.com/YOUR_USERNAME/cli_utils.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

### Install a specific branch or tag

```bash
# Install from a specific branch
pip install git+https://github.com/YOUR_USERNAME/cli_utils.git@main

# Install from a specific tag (e.g., v0.1.0)
pip install git+https://github.com/YOUR_USERNAME/cli_utils.git@v0.1.0
```

---

## 🧪 Quick Recap

| Step | What you did |
|------|-------------|
| 1 | Created the folder structure |
| 2 | Wrote `print_separator()` in `separators.py` |
| 3 | Configured `pyproject.toml` |
| 4 | Added a `README.md` |
| 5 | Installed locally with `pip install -e .` |
| 6 | Pushed to GitHub |
| 7 | Installed from GitHub with `pip install git+...` |

---

## 🏆 Challenges

Now that your package works, level it up! Add more functions to `separators.py`.

---

### 🟢 Challenge 1 — Custom Character Separator

**Goal:** Create a function that lets the user choose which character to repeat.

**Function signature:**
```python
def print_char_separator(char):
    ...
```

**Expected usage:**
```python
print_char_separator("-")   # ------------------------------
print_char_separator("=")   # ==============================
print_char_separator("~")   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
```

> 💡 **Hint:** Your existing function uses `"*" * 30`. Can you replace the hardcoded `"*"` with the `char` argument?

> 🔍 **Tip:** What happens if someone passes `"abc"` as the character? You could use `char[0]` to always grab only the first character!

---

### 🟡 Challenge 2 — Custom Length Separator

**Goal:** Let the user control both the character **and** the length.

**Function signature:**
```python
def print_custom_separator(char, length):
    ...
```

**Expected usage:**
```python
print_custom_separator("*", 30)   # ******************************
print_custom_separator("-", 10)   # ----------
print_custom_separator("#", 50)   # ##################################################
```

> 💡 **Hint:** You now have two arguments. Combine them: `char * length`.

> 🔍 **Tip:** What if `length` is negative or zero? Try adding a guard:
> ```python
> if length <= 0:
>     print("")
>     return
> ```

---

### 🟠 Challenge 3 — Labeled Separator

**Goal:** Print a separator with a label centered inside it.

**Function signature:**
```python
def print_labeled_separator(label, char="*", width=30):
    ...
```

**Expected usage:**
```python
print_labeled_separator("START")
# ************START*************

print_labeled_separator("DONE", char="-", width=40)
# ------------------DONE------------------
```

> 💡 **Hint:** Python strings have a built-in method for this — look up `str.center(width, fillchar)`.
> ```python
> "hello".center(20, "-")   # '-------hello--------'
> ```

> 🔍 **Tip:** Notice `char="*"` and `width=30` have **default values**. This means calling `print_labeled_separator("START")` still works without providing those arguments!

---

### 🔴 Challenge 4 — Boxed Text

**Goal:** Print a message surrounded by a full border box.

**Function signature:**
```python
def print_box(message, char="*"):
    ...
```

**Expected usage:**
```python
print_box("Hello, World!")
```

**Expected output:**
```
***************
* Hello, World! *
***************
```

> 💡 **Hint:** You'll need to:
> 1. Calculate the width based on the message length
> 2. Print a top border
> 3. Print the message with `char` on each side
> 4. Print a bottom border

> 🔍 **Tip:** The width should be `len(message) + 4` to account for the spaces and border characters on each side.

---

### ⭐ Bonus Challenge — Export All Functions

Once you've added your new functions, make sure they're accessible by updating `__init__.py`:

```python
# cli_utils/__init__.py
from .separators import (
    print_separator,
    print_char_separator,
    print_custom_separator,
    print_labeled_separator,
    print_box,
)
```

Then bump your version in `pyproject.toml`:
```toml
version = "0.2.0"
```

And reinstall (if not using `-e` mode):
```bash
pip install -e .
```

---

## 🎉 You Did It!

You've built, installed, and published a real Python package. Every professional Python library — `requests`, `numpy`, `flask` — started exactly like this.

**Keep building. Keep sharing. 🚀**
