# Simultaneous Login Automation - Python + Selenium Grid

Automate multiple configurable simultaneous logins to the test application:  
[https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

---

## Key Features

- Configurable input: set the number of logins via CLI, `.env`, or graphical interface.
- Efficient parallel execution: threads, Selenium Grid, and control via `.env`.
- ID sequencing and ordering configurable (`SEQUENCE=INCREASING|DECREASING|RANDOM`).
- Artifacts organized by ID: screenshots and HTML saved in dedicated folders per login.
- Results export: JSON, CSV, TXT, screenshots, and HTML (for both success and failure).
- Docker and Docker Compose ready for local or production use.
- Ready for auditing, monitoring, and cross-platform replication (Windows, Mac, Linux).
- **Centralized error and system messages** in:
  - `source/message_errors.py`: module-specific errors.
  - `source/message_system.py`: success, status, and system feedback messages.
- Facilitates translation, auditing, and maintenance.

---

## Project Structure

```
selenium-login-load/
├─ source/
│  ├─ main.py
│  ├─ run_logins.py
│  ├─ login_worker.py
│  ├─ driverconfig.py
│  ├─ gui.py
│  ├─ message_errors.py
│  ├─ message_system.py
├─ results/
│  ├─ results.json
│  ├─ results.csv
│  ├─ report_summary.txt
│  ├─ screenshot/
│  │    ├─ ID-uuid/
│  │        └─ uuid.png
│  ├─ html/
│  │    ├─ ID-uuid/
│  │        └─ uuid.html
├─ .env
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ entrypoint.sh
└─ README_PROD.md
```

---

## Configuration (`.env`)

Example:

```dotenv
# Configurable limits for simultaneous logins!
MIN_LOGINS=1      # Minimum allowed simultaneous logins.
MAX_LOGINS=1000   # Maximum allowed simultaneous logins.

# SEQUENCE defines the login ID sequence type (INCREASING, DECREASING, RANDOM)
SEQUENCE=RANDOM     # INCREASING, DECREASING, RANDOM

# Number of simultaneous logins (total attempts)
CONCURRENT_LOGINS=50

# Maximum number of concurrent threads/processes
MAX_CONCURRENT=10

# Run browser in headless mode. Use 'true' for production.
HEADLESS=true

# Maximum page load time (seconds)
PAGE_LOAD_TIMEOUT=30

# Maximum time to wait for elements on the page (seconds)
ELEMENT_WAIT_TIMEOUT=10

# Login user
LOGIN_USERNAME=tomsmith

# Login password
LOGIN_PASSWORD=SuperSecretPassword!

# Main folder for saving results
OUTPUT_DIR=./results

# Folder for screenshots of each login
OUTPUT_DIR_SCREENSHOT=./results/screenshot

# Folder for saving HTML of each login
OUTPUT_DIR_HTML=./results/html

# Save login screenshots (true/false)
SAVE_SCREENSHOTS=true

# Save HTML of the page after login failure (true/false)
SAVE_HTML_ON_FAILURE=true

# Export results in JSON (true/false)
EXPORT_JSON=true

# Export results in CSV (true/false)
EXPORT_CSV=true

# Selenium execution mode ('local' for local machine, 'grid' for Selenium Grid)
SELENIUM_MODE=local

# Selenium Hub URL (used only in grid mode)
SELENIUM_REMOTE_URL=http://selenium-hub:4444/wd/hub

# Login page URL (target application)
TARGET_URL=https://the-internet.herokuapp.com/login

# URL fragment that indicates login success (used for redirect validation)
TARGET_URL_TO_CHECK=/secure

# Enable/disable Selenium Grid (true/false)
USE_GRID=false

# Number of Chrome nodes in the Grid (used in docker-compose)
GRID_NODES=3

# Local ChromeDriver path (required for Windows local execution)
# Docker Config or windows C:\WebDriver\bin\chromedriver.exe
CHROMEDRIVER_PATH=/usr/bin/chromedriver
```

- For Docker/Grid: `SELENIUM_MODE=grid`, `USE_GRID=true`
- For local: `SELENIUM_MODE=local`, `USE_GRID=false`, and set `CHROMEDRIVER_PATH`

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

## How to Run

### 1. Local (Windows, Mac, Linux)

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Download ChromeDriver matching your Chrome version:
   - [Google Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing)
   - Windows:
     - 64 bit: [chromedriver-win64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/win64/chromedriver-win64.zip)
     - 32 bit: [chromedriver-win32.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/win32/chromedriver-win32.zip)
   - Mac:
     - [chromedriver-mac-arm64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/mac-arm64/chromedriver-mac-arm64.zip)
     - [chromedriver-mac-x64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/mac-x64/chromedriver-mac-x64.zip)
   - Linux:
     - [chromedriver-linux64.zip](https://storage.googleapis.com/chrome-for-testing-public/140.0.7339.207/linux64/chromedriver-linux64.zip)
   - More info: [ChromeDriver Docs](https://developer.chrome.com/docs/chromedriver/downloads?hl=en)
3. Set the path in `.env`:
   ```dotenv
   CHROMEDRIVER_PATH=C:\WebDriver\bin\chromedriver.exe
   ```
4. Run:
   ```bash
   python -m source.main -n 10
   ```
   - Adjust the number of logins as desired.
   - Set `SEQUENCE` to control ID order and display.

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

- `results/results.json` → details of each login
- `results/results.csv` → CSV export
- `results/report_summary.txt` → summary with total time and status of each login
- `results/screenshot/ID-uuid/uuid.png` → Screenshot (success and failure)
- `results/html/ID-uuid/uuid.html` → HTML (success and failure)

---

## Sequencing and Ordering

- **SEQUENCE=RANDOM**: random IDs, order of arrival.
- **SEQUENCE=INCREASING**: IDs from 1 to N, ascending order.
- **SEQUENCE=DECREASING**: IDs from N to 1, descending order.
- Display and artifact order follow the selected type.

---

## Scalability & Production

- Configurable parallelism via `MAX_CONCURRENT` and `CONCURRENT_LOGINS`
- Distributed Grid for hundreds of simultaneous logins
- Ready for replication on any OS

---

## Monitoring & Auditing

- Container and CLI logs display time/status for each login
- Error and success artifacts saved per ID
- Reports exported in professional formats
- Easy auditability and traceability by ID
- **Centralized error and system messages** in:
  - `source/message_errors.py`: module-specific errors.
  - `source/message_system.py`: success, status, and system feedback messages.
- Facilitates translation, auditing, and maintenance.

---

## ChromeDriver: Windows, Mac, Linux

- Always download ChromeDriver **with the same version as your Chrome**.
- Official links: [Google Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing)
- Set `CHROMEDRIVER_PATH` in `.env` for local execution.
- For Grid/Docker, ChromeDriver setup is automatic.

---

## FAQ

**How do I run with more or fewer logins?**  
- Edit `CONCURRENT_LOGINS` in `.env` or use the `-n` argument.

**How do I scale to hundreds of logins?**  
- Adjust `MAX_CONCURRENT` and `CONCURRENT_LOGINS` in `.env` and increase Chrome nodes in `docker-compose.yml`.

**How do I configure the sequence of IDs and display order?**  
- Use `SEQUENCE=INCREASING`, `SEQUENCE=DECREASING`, `SEQUENCE=RANDOM` in `.env`.

**Are artifacts organized?**  
- Yes, each login has its own folder by ID for screenshot and HTML.

**PySimpleGUI not working?**  
- Follow installation instructions in the README to install from the private repository.

---

## Notes

- Code fully meets the challenge requirements, production and audit-ready.
- Artifacts and logs guarantee traceability and reliability.
- Replicable on any computer, Windows, Mac, Linux, locally or Grid with Docker.

---

## WHAT THE CODE NEEDS TO DO (CHALLENGE)

### System Functionality

1. **Input for Number of Simultaneous Logins:**  
   ○ User sets the number of simultaneous logins via input field.
2. **Execution of Multiple Simultaneous Logins:**  
   ○ Selenium automates logins, each uses its own isolated WebDriver instance.
   ○ Login: tomsmith | Password: SuperSecretPassword!
3. **Execution Time Calculation:**  
   ○ Total time for all simultaneous logins displayed at the end.
4. **Success Validation:**  
   ○ Checks redirect to the success page and records status for each login.
5. **Display of Time and Status:**  
   ○ Shows total time, status (success/failure), and unique token for each login.

### Implementation Steps

1. User Interface
   - Input field for the number of simultaneous logins.
   - Run button.
2. Simultaneous Logins Execution
   - Selenium, independent WebDrivers, Grid for production.
3. Time Calculation and Display
   - Total time, report, and artifacts.
4. Success Validation
   - Redirect validated and exported.
5. User Feedback
   - Real-time status, audit artifacts, clear reports.

### Evaluation Points

- Correct Login Process: real login and redirect validation.
- Efficient Parallel Execution: multiple simultaneous logins, Grid and local.
- Accurate Time Calculation: total and individual time displayed.
- User Feedback: status, artifacts, clear logs and reports.
- Deploy & Monitoring: Docker, Grid, artifacts, and replication in any environment.

## PySimpleGUI & Docker

If using the graphical interface (`--gui`) on Linux/Docker, you may need extra dependencies for PySimpleGUI to work:

```bash
apt-get update && apt-get install -y python3-tk
```

For Docker, add in Dockerfile:

```dockerfile
RUN apt-get update && apt-get install -y python3-tk
```

If using headless mode, the GUI will not work. Prefer CLI (`python -m source.main -n 20`) or Grid/Docker execution.

---

## Troubleshooting

- **"element not found" or timeout error:**  
  Could be network or machine slowness. The system now waits up to 10 seconds (configurable via `ELEMENT_WAIT_TIMEOUT` in `.env`) for each element to appear.
- **PySimpleGUI does not open on VM/Docker:**  
  Install `python3-tk` as above. Or use CLI.
- **Chrome/Chromedriver incompatibility:**  
  Download the correct version from [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing) and set the path in `.env`.