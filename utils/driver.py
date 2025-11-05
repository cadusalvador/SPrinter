from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utils.helpers import log

def create_chrome_driver(config, headless=True, window_size="1920,1440"):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument(f"--window-size={window_size}")
    else:
        chrome_options.add_argument("--start-maximized")


    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-infobars")

    page_load_timeout = int(config.get("PAGE_LOAD_TIMEOUT", 30))

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_page_load_timeout(page_load_timeout)
    log(f'✅ Driver iniciado e navegando para: {config["LOOKER_URL_VISAO_GERAL"]}')
    return driver

