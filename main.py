# main.py
from utils.driver import start_driver_window
from utils.login import login_google
from utils.screenshot import print_save
from utils.helpers import log, wait_for_looker, load_env
import os

# --- Função Principal ---
def executar_ciclo_produtividade():
    config = load_env()
    # driver = None

    try:
        driver = start_driver_window(config, first_url=config["LOOKER_URL_VISAO_GERAL"])
        # login_google(driver, config)
        wait_for_looker(driver, config["LOOKER_URL_VISAO_GERAL"])
        success = print_save(driver, config["PRINT_PATH"])
        if success:
            log("✅ Ciclo concluído com sucesso.")
    finally:
        if driver:
            driver.quit()
            log("🧹 Driver encerrado.")

# --- Execução principal ---
if __name__ == "__main__":
    executar_ciclo_produtividade()