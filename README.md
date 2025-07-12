# Crypto Price Tracker CLI

A production-grade, testable Python CLI tool that fetches real-time cryptocurrency prices in INR and USD using a modular, professional structure with mock data fallback.

---

## Features

- Clean CLI interface using `click`
- Retry logic (or mock fallback)
- Output to terminal or file
- Logging with error handling
- Tested with `unittest` and `CliRunner`
- Beginner-friendly + production-ready

---

##  How to Run

```bash
# Activate your virtual environment
.\.venv\Scripts\activate

# Run CLI
python cli_entry.py --crypto bitcoin

#Or interactively:
python cli_entry.py

#To output to a file:
python cli_entry.py --crypto bitcoin --output file --file bitcoin.json

#Run testspython -m unittest discover tests
python -m unittest discover tests
```
---

## Built With

- Python 3.10+
- lick
- requests
- unittest
- rich

