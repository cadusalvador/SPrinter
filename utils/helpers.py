import os
import time
from utils.logs import log
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def load_env():
    load_dotenv()

    config = {
        "LOOKER_URL": os.getenv("LOOKER_URL"),
        "LOOKER_URL_VISAO_GERAL": os.getenv("LOOKER_URL_VISAO_GERAL"),
        "APP_ID": os.getenv("APP_ID"),
        "APP_SECRET": os.getenv("APP_SECRET"),
        "LINK_APP_TOKEN": os.getenv("LINK_APP_TOKEN"),
        "SEATALK_WEBHOOK": os.getenv("SEATALK_WEBHOOK"),
        "CHROME_DRIVER_PATH": os.getenv("CHROME_DRIVER_PATH"),
        "PRINT_PATH": os.getenv("PRINT_PATH"),
        "BINARY_LOCATION": os.getenv("BINARY_LOCATION"),
        "PAGE_LOAD_TIMEOUT": os.getenv("PAGE_LOAD_TIMEOUT"),
        "HEADLESS": os.getenv("HEADLESS")
   
    }
    
    missing = [k for k, v in config.items() if not v]
    if missing:
        raise ValueError(f"❌ Variáveis de ambiente ausentes: {', '.join(missing)}")
    
    return config

def wait_for_looker(driver, url, timeout=30):
    try:
        log("🌐 Acessando dashboard Looker...")
        driver.get(url)
        WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(10)
        log("✅ Dashboard carregado.")
    except Exception as e:
        log(f"⚠️ Erro ao aguardar carregamento: {e}")
