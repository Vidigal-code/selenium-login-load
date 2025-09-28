import os
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException,
    NoSuchElementException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from source.config.driverconfig import create_driver

load_dotenv()

LOGIN_USERNAME = os.getenv("LOGIN_USERNAME", "tomsmith")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "SuperSecretPassword!")
OUTPUT_DIR = os.getenv("OUTPUT_DIR", "./results")
OUTPUT_DIR_SCREENSHOT = os.getenv("OUTPUT_DIR_SCREENSHOT", "./results/screenshot")
OUTPUT_DIR_HTML = os.getenv("OUTPUT_DIR_HTML", "./results/html")
TARGET_URL = os.getenv("TARGET_URL", "https://the-internet.herokuapp.com/login")
SAVE_SCREENSHOTS = os.getenv("SAVE_SCREENSHOTS", "true").lower() == "true"
SAVE_HTML_ON_FAILURE = os.getenv("SAVE_HTML_ON_FAILURE", "true").lower() == "true"
TARGET_URL_TO_CHECK = os.getenv("TARGET_URL_TO_CHECK", "/secure")
ELEMENT_WAIT_TIMEOUT = int(os.getenv("ELEMENT_WAIT_TIMEOUT", 10))

for path in [OUTPUT_DIR, OUTPUT_DIR_SCREENSHOT, OUTPUT_DIR_HTML]:
    os.makedirs(path, exist_ok=True)

def save_file(content, path):
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path
    except Exception as e:
        print(f"Falha ao salvar HTML: {e}")
        return ""

def save_screenshot(driver, path):
    try:
        driver.save_screenshot(path)
        return path
    except Exception as e:
        print(f"Falha ao salvar screenshot: {e}")
        return ""

def perform_login(index, seq_id):
    result = {
        "id": seq_id,
        "index": index,
        "status": "Failed",
        "url": "",
        "error": "",
        "time_seconds": 0,
        "screenshot": "",
        "html": ""
    }
    start_time = time.time()
    driver = None

    id_folder_screen = os.path.join(OUTPUT_DIR_SCREENSHOT, f"ID-{seq_id}")
    id_folder_html = os.path.join(OUTPUT_DIR_HTML, f"ID-{seq_id}")
    os.makedirs(id_folder_screen, exist_ok=True)
    os.makedirs(id_folder_html, exist_ok=True)
    screenshot_path = os.path.join(id_folder_screen, f"{seq_id}.png")
    html_path = os.path.join(id_folder_html, f"{seq_id}.html")

    try:
        driver = create_driver()
        driver.get(TARGET_URL)
        wait = WebDriverWait(driver, ELEMENT_WAIT_TIMEOUT)

        try:
            username_elem = wait.until(EC.presence_of_element_located((By.ID, "username")))
            password_elem = wait.until(EC.presence_of_element_located((By.ID, "password")))
            submit_elem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            username_elem.clear()
            username_elem.send_keys(LOGIN_USERNAME)
            password_elem.clear()
            password_elem.send_keys(LOGIN_PASSWORD)
            submit_elem.click()
        except TimeoutException:
            result["error"] = "Timeout ao buscar elementos de login."
            return result
        except NoSuchElementException:
            result["error"] = "Elemento de login não encontrado."
            return result

        time.sleep(1)
        result["url"] = driver.current_url

        if SAVE_SCREENSHOTS:
            result["screenshot"] = save_screenshot(driver, screenshot_path)
        if SAVE_HTML_ON_FAILURE or result["status"] != "SUCCESS":
            result["html"] = save_file(driver.page_source, html_path)

        if TARGET_URL_TO_CHECK in driver.current_url:
            try:
                success_msg = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
                ).text
                if "You logged into a secure area!" in success_msg:
                    result["status"] = "SUCCESS"
                else:
                    result["error"] = "Redirecionado, mas mensagem de sucesso não encontrada."
            except TimeoutException:
                result["error"] = "Redirecionamento, mas mensagem de sucesso não encontrada (timeout)."
            except NoSuchElementException:
                result["error"] = "Redirecionamento, mas mensagem de sucesso não encontrada."
        else:
            result["error"] = "Redirecionamento ou elemento de sucesso não encontrado."

    except TimeoutException:
        result["error"] = "Timeout geral do WebDriver."
    except NoSuchElementException:
        result["error"] = "Elemento não encontrado na página."
    except WebDriverException as e:
        result["error"] = f"WebDriverException: {e}"
    except Exception as e:
        result["error"] = f"Erro inesperado: {e}"
    finally:
        result["time_seconds"] = round(time.time() - start_time, 2)
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"Falha ao finalizar driver: {e}")
    return result