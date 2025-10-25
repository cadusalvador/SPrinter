from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from utils.helpers import log

def start_driver_window(first_url="http://www.google.com", chromedriver_path=None):
    try:
        service = ChromeService(chromedriver_path)
        options = webdriver.ChromeOptions()

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--remote-debugging-port=9222")
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

        options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        driver = webdriver.Chrome(service=service, options=options)
        driver.get(first_url)

        log(f"✅ Driver iniciado e navegando para: {first_url}")
        return driver
    except Exception as e:
        log(f"❌ Erro ao iniciar o driver: {e}")
        return None