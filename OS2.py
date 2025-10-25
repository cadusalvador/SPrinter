import base64
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
# --- 1. Configurações e Constantes --- #

LOOKER_URL = "https://lookerstudio.google.com/reporting/3d4cd909-8899-4b8e-bd9c-e829e8ddb248/page/p_7ioxh6sxod?pli=1"
LOOKER_URL_VISAO_GERAL = "https://lookerstudio.google.com/u/0/reporting/1a16d8bc-5440-465e-b125-fba67df6d50a/page/page_12345"
EMAIL = os.getenv("GOOGLE_EMAIL")
SENHA = os.getenv("GOOGLE_SENHA")
PRINT_PATH = "prints/print_temp.png"

# WEBHOOK_URL_SEATALK = "INSERIR"
# TOKEN = "INSERIR"
# HEADERS = {
#     "Authorization": f"Bearer {TOKEN}",
#     "content_type": "application/json"
# }

def log(message):
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def start_driver_window(first_url="http://www.google.com"):
    try:
        service = ChromeService(ChromeDriverManager().install())
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
    
def login_google(driver):
    log("🔐 Acessando página de login...")
    driver.get("https://account.google.com")

    wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "identifierId")))


    email_input = driver.find_element(By.XPATH,)
    email_input.send_keys(EMAIL)
    driver.find_element(By.ID, "identifierNext").click()

    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys(SENHA)
    driver.find_element(By.ID, "passwordNext").click()

    log("✅ Login enviado. Aguardando autenticação...")
    time.sleep(5)
    
def wait_for_looker(driver, timeout=30):
    try:
        log("🌐 Acessando dashboard Looker...")
        driver.get(LOOKER_URL)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(10)
        log("✅ Dashboard carregado.")
    except Exception as e:
        log(f"⚠️ Erro ao aguardar carregamento: {e}")


# --- 2. Captura de Tela --
def print_save(driver, path_file): 
    if driver:
        try:
            driver.save_screenshot(path_file)
            log(f"✅ Screenshot salvo em: {path_file}")
            return True
        except Exception as e:
            log(f"❌ Erro ao tirar screenshot: {e}")
            return False

# --- Função Principal ---
def executar_ciclo_produtividade():
    driver = None
    try:
        driver = start_driver_window(LOOKER_URL_VISAO_GERAL)
        login_google(driver)
        wait_for_looker(driver)
        success = print_save(driver, PRINT_PATH)
        if success:
            log("✅ Ciclo concluído com sucesso.")
    finally:
        if driver:
            driver.quit()
            log("🧹 Driver encerrado.")

# --- Execução principal ---
if __name__ == "__main__":
    executar_ciclo_produtividade()

    