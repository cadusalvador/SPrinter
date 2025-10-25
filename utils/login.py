import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import log


def login_google(driver, config):
    log("🔐 Acessando página de login...")
    driver.get("https://account.google.com")

    try:
        wait = WebDriverWait(driver, 30)
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
        email_input.send_keys(config["LOOKER_EMAIL"])
        driver.find_element(By.ID, "identifierNext").click()

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
        password_input.send_keys(config["LOOKER_PASSWORD"])
        driver.find_element(By.ID, "passwordNext").click()

        log("✅ Login enviado. Aguardando autenticação...")
        time.sleep(5)
    except Exception as e:
        log(f"❌ Erro no login: {e}")