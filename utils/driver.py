from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from utils.helpers import log

def create_chrome_driver(config, headless=True):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--window-size=1920,1440")
    else:
        chrome_options.add_argument("--start-maximized")
        
        
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    chrome_driver_path = config["CHROME_DRIVER_PATH"]
    page_load_timeout = int(config.get("PAGE_LOAD_TIMEOUT", 30))

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_page_load_timeout(page_load_timeout)
    log("✅ Driver iniciado e navegando para: ", config["LOOKER_URL_VISAO_GERAL"])
    return driver