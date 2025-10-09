Quick run instructions

This project automates concurrent logins to https://the-internet.herokuapp.com/login using Selenium.

Requirements
- Python 3.8+
- Selenium
- ChromeDriver (if running local mode) or a Selenium Grid endpoint
- Recommended: create a .env file to set configuration (see README.md)

Run (CLI)
- From repository root:
  python -m source.main -n 5

Run with GUI
- From repository root:
  python -m source.main --gui

Notes
- The GUI includes an input to set the number of concurrent logins.
- Results (JSON/CSV) are saved to the folder configured by OUTPUT_DIR (default ./results).
- If you don't have ChromeDriver installed, run in an environment with Selenium Grid or set appropriate env vars.

Limitations
- This repository expects a working Selenium environment. The included code generates tokens for successful logins and prints per-login status and total execution time.
