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
DRIVER_MOCK = os.getenv("DRIVER_MOCK", "false").lower() == "true"

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
    # If DRIVER_MOCK is enabled, return a lightweight mock driver for tests
    if DRIVER_MOCK:
        print("Using mock WebDriver (DRIVER_MOCK=true)")

        class FakeElement:
            def __init__(self, text=""):
                self._text = text

            def clear(self):
                return None

            def send_keys(self, *args, **kwargs):
                return None

            def click(self):
                return None

            @property
            def text(self):
                return self._text

        class MockDriver:
            def __init__(self):
                self.current_url = "https://the-internet.herokuapp.com/login"
                self.page_source = "<html><body>login page</body></html>"

            def get(self, url):
                # simulate redirect to secure after a short delay
                self.current_url = url
                return None

            def save_screenshot(self, path):
                # create an empty file to simulate saving
                try:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write("")
                except Exception:
                    pass
                return True

            def quit(self):
                return None

            def find_element(self, by, value):
                # Return FakeElement for username/password/button
                return FakeElement()

            def find_elements(self, by, value):
                return [FakeElement()]

            def set_page_load_timeout(self, timeout):
                return None

        return MockDriver()
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