import os

# Folders to create
folders = ["src", "tests", "logs"]

# Files to create 
files = [
    "src/__init__.py",
    "src/main.py",
    "src/api.py",
    "src/cli.py",
    "src/utils.py",
    "src/errors.py",
    "src/logger.py",
    "run.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

# Create folders
for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"✅ Created folder: {folder}")
    else:
        print(f"⚠️ Folder already exists: {folder}")

# Create files
for file in files:
    if not os.path.exists(file):
        with open(file, "w", encoding="utf-8") as f:
            pass  # Creates an empty file
        print(f"✅ Created file: {file}")
    else:
        print(f"⚠️ File already exists: {file}")