# Simultaneous Login Automation - Python + Selenium Grid

Automate multiple configurable simultaneous logins to the test application:  
[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

---

## Example 

<img src="./example/example.png" alt="" width="800"/> 

---

## Example Docker

<img src="./example/example-docker.png" alt="" width="800"/> 

---

## Example Selenium Grid

<img src="./example/example-selenium-grid.png" alt="" width="800"/> 

---

## Example Interface Gui

<img src="./example/example-interface-gui.png" alt="" width="800"/> 

---


## 📚 Documentation

- [README_PT.md](./README_PT.md) — Portuguese documentation.

---


## Table of Contents

- [Project Objective](#project-objective)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Configuration](#configuration)
- [Execution](#execution)
- [Generated Results](#generated-results)
- [Scalability & Production](#scalability--production)
- [Monitoring & Auditing](#monitoring--auditing)
- [ChromeDriver: Windows, Mac, Linux](#chromedriver-windows-mac-linux)
- [FAQ](#faq)

---

## Project Objective

Automate multiple simultaneous logins to [the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login) using Python 3.13+, Selenium 4+, with a user-configurable quantity.  
The total execution time is calculated and displayed, along with the status of each login (success or failure).  
Success validation, artifact exportation, and production-ready setup using Selenium Grid and Docker.

---

## Features

- User input: configure the number of simultaneous logins via CLI or graphical interface.
- Parallel execution: multiple independent WebDrivers (threads and Selenium Grid).
- Configurable sequencing (`SEQUENCE=INCREASING|DECREASING|RANDOM`)
- Artifacts organized by ID: screenshots and HTML saved in folders per login.
- Automated login: user `tomsmith`, password `SuperSecretPassword!`.
- Total time calculation: logs and displays after execution.
- Success validation: checks redirect to success page.
- Results export: JSON, CSV, TXT, screenshots, and HTML artifacts (for both success and failure).
- Docker + Selenium Grid production-ready.
- Monitoring via artifacts and logs.
- **Centralized messages**: `message_errors.py` and `message_system.py` files facilitate customization, translation, and auditing.

---

## Folder Structure

```
selenium-login-load/
├─ source/
│  ├─ main.py                        # Main entry point (CLI/GUI)
│  ├─ interface/
│  │    ├─ gui.py                    # Graphical interface (optional)
│  ├─ system/
│  │    ├─ login_worker.py           # Individual login worker
│  │    ├─ run_logins.py             # Logins orchestrator
│  ├─ config/
│  │    ├─ driverconfig.py           # WebDriver configuration
│  ├─ messages/
│  │    ├─ message_errors.py         # Centralized error messages
│  │    ├─ message_system.py         # Centralized system/success messages
├─ results/
│  ├─ results.json
│  ├─ results.csv
│  ├─ report_summary.txt
│  ├─ screenshot/
│  │    ├─ ID-uuid/
│  │    │    └─ uuid.png
│  ├─ html/
│  │    ├─ ID-uuid/
│  │    │    └─ uuid.html
├─ .env
├─ .dockerignore
├─ .gitignore
├─ generate_compose_cli.py
├─ generate_compose_grid.py
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ entrypoint.sh
├─ README_PT.md
├─ README_PROD_PT.md
├─ README_PROD.md
└─ README.md
```

---

## Configuration

### `.env` (example)

```dotenv
# Configurable limits for simultaneous logins!
MIN_LOGINS=1      # Minimum allowed simultaneous logins.
MAX_LOGINS=1000   # Maximum allowed simultaneous logins.

# SEQUENCE defines the type of sequence for login IDs (INCREASING, DECREASING, RANDOM)
SEQUENCE=RANDOM     # INCREASING, DECREASING, RANDOM

# Number of simultaneous logins (total attempts)
CONCURRENT_LOGINS=50

# Maximum number of concurrent threads/processes
MAX_CONCURRENT=10

# Run browser in headless mode? Use 'true' for production.
HEADLESS=true

# Maximum page load timeout (seconds)
PAGE_LOAD_TIMEOUT=30

# Maximum wait for elements on page (seconds)
ELEMENT_WAIT_TIMEOUT=10

# Login user
LOGIN_USERNAME=tomsmith

# Login password
LOGIN_PASSWORD=SuperSecretPassword!

# Main output folder for results
OUTPUT_DIR=./results

# Folder for login screenshots
OUTPUT_DIR_SCREENSHOT=./results/screenshot

# Folder for saving HTML per login
OUTPUT_DIR_HTML=./results/html

# Save screenshots of login results (true/false)
SAVE_SCREENSHOTS=true

# Save page HTML after failed login (true/false)
SAVE_HTML_ON_FAILURE=true

# Export results to JSON (true/false)
EXPORT_JSON=true

# Export results to CSV (true/false)
EXPORT_CSV=true

# Selenium execution mode ('local' for local machine, 'grid' for Selenium Grid)
SELENIUM_MODE=local

# Selenium Hub URL (used only in grid mode)
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub

# Login page URL (target application)
TARGET_URL=https://the-internet.herokuapp.com/login

# URL fragment indicating login success (used for redirect validation)
TARGET_URL_TO_CHECK=/secure

# Enable/disable Selenium Grid (true/false)
USE_GRID=false

# Number of Chrome nodes in Grid (used in docker-compose)
GRID_NODES=3

# Local ChromeDriver path (required for Windows local execution)
# Docker Config or windows C:\WebDriver\bin\chromedriver.exe
CHROMEDRIVER_PATH=/usr/bin/chromedriver
```

---

### `.env` (execute grid docker)

```dotenv
# Minimum allowed simultaneous logins.
MIN_LOGINS=1

# Maximum allowed simultaneous logins.
MAX_LOGINS=1000

# Sequence type for login IDs: INCREASING, DECREASING or RANDOM.
SEQUENCE=RANDOM

# Number of simultaneous logins (total attempts).
CONCURRENT_LOGINS=50

# Maximum number of concurrent threads/processes.
MAX_CONCURRENT=10

# Run browser in headless mode (no GUI). Use 'true' for production.
HEADLESS=true

# Maximum page load timeout (seconds).
PAGE_LOAD_TIMEOUT=30

# Maximum wait for elements on page (seconds).
ELEMENT_WAIT_TIMEOUT=10

# Login user.
LOGIN_USERNAME=tomsmith

# Login password.
LOGIN_PASSWORD=SuperSecretPassword!

# Main output folder for results.
OUTPUT_DIR=./results

# Folder for login screenshots.
OUTPUT_DIR_SCREENSHOT=./results/screenshot

# Folder for saving HTML per login.
OUTPUT_DIR_HTML=./results/html

# Save screenshots of login results (true/false).
SAVE_SCREENSHOTS=true

# Save page HTML after failed login (true/false).
SAVE_HTML_ON_FAILURE=true

# Export results to JSON (true/false).
EXPORT_JSON=true

# Export results to CSV (true/false).
EXPORT_CSV=true

# Selenium execution mode ('local' for local machine, 'grid' for Selenium Grid).
SELENIUM_MODE=grid

# Selenium Hub URL (used only in grid mode).
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub

# Login page URL (target application).
TARGET_URL=https://the-internet.herokuapp.com/login

# URL fragment indicating login success (used for redirect validation).
TARGET_URL_TO_CHECK=/secure

# Enable/disable Selenium Grid (true/false).
USE_GRID=true

# Number of Chrome nodes in Grid (used in docker-compose).
GRID_NODES=1

# Local ChromeDriver path (required for Windows local execution).
# Docker Config or windows C:\WebDriver\bin\chromedriver.exe
CHROMEDRIVER_PATH=
```

---


## Execution

### Local

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install ChromeDriver matching your Chrome version:
   - [Google Chrome for Testing: Downloads](https://googlechromelabs.github.io/chrome-for-testing)
   - Windows: 
     - 64-bit: [Win64 chromedriver](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/win64/chromedriver-win64.zip)
     - 32-bit: [Win32 chromedriver](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/win32/chromedriver-win32.zip)
   - Mac:
     - [chromedriver-mac-arm64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/mac-arm64/chromedriver-mac-arm64.zip)
     - [chromedriver-mac-x64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/mac-x64/chromedriver-mac-x64.zip)
   - Linux:
     - [chromedriver-linux64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/linux64/chromedriver-linux64.zip)
   - More info: [ChromeDriver Docs](https://developer.chrome.com/docs/chromedriver/downloads?hl=en)
3. Run logins:
   ```bash
   python -m source.main -n 10
   ```
   - Change the number as desired.
   - Use `SEQUENCE=INCREASING`, `SEQUENCE=DECREASING`, or `SEQUENCE=RANDOM` in `.env` to change the order/IDs.

# Docker + Selenium Grid (Production)

## 1. Build Containers

```bash
docker compose build
```

## 2. Start the Complete Environment

```bash
docker compose up
```
- The app automatically detects Grid or Local mode from your `.env`:
  - If `SELENIUM_MODE=grid`, it uses Selenium Grid.
  - If `SELENIUM_MODE=local`, it runs locally.
- Logs will display **time spent** and **status** for each login attempt.

## 3. Generate and Launch with the Python Grid Script

```bash
python generate_compose_grid.py
```
- This script:
  - Automatically generates a `docker-compose.yml` with the number of nodes set in `.env` (`GRID_NODES`)
  - Deletes any previous `docker-compose.yml`
  - Runs: `docker compose up --build`

## 4. Generate and Launch with the Python CLI Script

```bash
python generate_compose_cli.py
```
- This script:
  - Automatically generates a `docker-compose.yml`
  - Deletes any previous `docker-compose.yml`
  - Runs: `docker compose up --build`

---

### Graphical Interface

```bash
python -m source.main --gui
```
- Enter the desired quantity and click **Run**.

---

## Generated Results

- `results/results.json` → Details for each login (ID, time, status, error, screenshot, HTML)
- `results/results.csv` → CSV export
- `results/report_summary.txt` → Summary with total time and status per login
- `results/screenshot/ID-uuid/uuid.png` → Screenshot (success and failure)
- `results/html/ID-uuid/uuid.html` → HTML (success and failure)

---

## Scalability & Production

- Configurable parallelism via `MAX_CONCURRENT` and `CONCURRENT_LOGINS`
- Distributed Grid for hundreds of simultaneous logins
- Ready for cloud/on-premises deployment
- Easily adaptable for other authentication scenarios

---

## Monitoring & Auditing

- Container and CLI logs display total time and status for each login
- Success and error artifacts saved for investigation
- Reports exported in professional formats
- **Error and system messages centralized** in:
  - `source/message_errors.py`: module-specific errors.
  - `source/message_system.py`: success, status, and system feedback messages.
- Facilitates translation, auditing, and maintenance.

---

## ChromeDriver: Windows, Mac, Linux

- Always download ChromeDriver matching your Chrome version!
- [Google Chrome for Testing: Downloads](https://googlechromelabs.github.io/chrome-for-testing)
- For local execution (Windows, Mac, Linux), set `CHROMEDRIVER_PATH` in `.env`.
- For Docker/Grid, ChromeDriver setup is automatic.

---

## FAQ

**Do I need ChromeDriver locally?**  
- Only for local execution. Not needed for Grid/Docker.

**How do I adjust for more or fewer logins?**  
- Edit `CONCURRENT_LOGINS` in `.env` or use the `-n` argument.

**Which artifacts are used for auditing?**  
- JSON, CSV, TXT, PNG, and HTML are generated in the `results/` folder.

**How do I scale to hundreds of logins?**  
- Adjust `MAX_CONCURRENT` and `CONCURRENT_LOGINS` in `.env` and increase Chrome nodes in `docker-compose.yml`.

**How do I set the sequence for IDs and display order?**  
- Use `SEQUENCE=INCREASING`, `SEQUENCE=DECREASING`, or `SEQUENCE=RANDOM` in `.env`.

**PySimpleGUI not working?**  
- Follow installation instructions in the README to install from the private repository.

---

## Contact

For questions, suggestions, or bugs, open an [issue](https://github.com/Vidigal-code/).

---

## Extra Notes

- Code meets 100% of challenge requirements, production-ready.
- Artifacts generated for both success and failure for auditing.
- Maintained up to date for Python 3.13.7, Selenium 4+, Docker, and Grid.