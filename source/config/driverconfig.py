import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
from source.messages.message_errors import ERROR_MESSAGES_DRIVERCONFIG
from source.messages.message_system import MESSAGE_SYSTEM_DRIVERCONFIG

load_dotenv()

HEADLESS = os.getenv("HEADLESS", "true") == "true"
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", 30))
SELENIUM_MODE = os.getenv("SELENIUM_MODE", "local")
SELENIUM_REMOTE_URL = os.getenv("SELENIUM_REMOTE_URL", "http://selenium-hub:4444/wd/hub")
CHROMEDRIVER_PATH = os.getenv("CHROMEDRIVER_PATH", None)

def create_driver():
    print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_config_start"])
    options = Options()
    if HEADLESS:
        options.add_argument("--headless=new")
        print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_headless_mode"])
    else:
        print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_non_headless_mode"])
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    print(MESSAGE_SYSTEM_DRIVERCONFIG["selenium_mode_info"].format(selenium_mode=SELENIUM_MODE))
    driver = None
    try:
        if SELENIUM_MODE == "grid":
            print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_init_remote"])
            print(ERROR_MESSAGES_DRIVERCONFIG["grid_connect_attempt"].format(selenium_remote_url=SELENIUM_REMOTE_URL))
            driver = webdriver.Remote(command_executor=SELENIUM_REMOTE_URL, options=options)
            print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_started_ok"])
        elif SELENIUM_MODE == "local":
            print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_init_local"])
            if CHROMEDRIVER_PATH:
                if not os.path.exists(CHROMEDRIVER_PATH):
                    raise FileNotFoundError(ERROR_MESSAGES_DRIVERCONFIG["invalid_chromedriver_path"])
                service = Service(CHROMEDRIVER_PATH)
                driver = webdriver.Chrome(service=service, options=options)
            else:
                driver = webdriver.Chrome(options=options)
            print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_started_ok"])
        else:
            raise ValueError(ERROR_MESSAGES_DRIVERCONFIG["unsupported_selenium_mode"].format(mode=SELENIUM_MODE))
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
        print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_timeout_set"].format(timeout=PAGE_LOAD_TIMEOUT))
        print(MESSAGE_SYSTEM_DRIVERCONFIG["driver_config_complete"])
        return driver
    except Exception as e:
        print(ERROR_MESSAGES_DRIVERCONFIG["webdriver_start_failed"])
        print(f"{type(e).__name__}: {e}")
        raise