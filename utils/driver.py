import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import log

def start_driver_window(config, first_url="http://www.google.com"):
    try:
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--window-size=1920,1080")

        user_profile = config["CHROME_USER_PROFILE"]
        options.add_argument(f"--user-data-dir={os.path.dirname(user_profile)}")
        options.add_argument(f"--profile-directory={os.path.basename(user_profile)}")

        options.binary_location = config["BINARY_LOCATION"]

        service = Service(ChromeDriverManager().install())

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(first_url)

        log(f"✅ Driver iniciado e navegando para: {first_url}")
        return driver
    except Exception as e:
        log(f"❌ Erro ao iniciar o driver: {e}")
        return None