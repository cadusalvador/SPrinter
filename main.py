# main.py
import time
from utils.driver import create_chrome_driver
from utils.screenshot import take_fullpage_screenshot
from utils.seatalk_sender import send_image_to_seatalk
from utils.helpers import log, load_env

# --- Função Principal ---
def executar_ciclo_produtividade():
    config = load_env()
    driver = None
    try:
        driver = create_chrome_driver(config, headless=True)
        print("Abrindo relatório público: ", config["LOOKER_URL_VISAO_GERAL"])
        driver.get(config["LOOKER_URL_VISAO_GERAL"])
        time.sleep(5)

        screenshot_path = take_fullpage_screenshot(driver, config["PRINT_PATH"])
        print("Screenshor salvo em: ", screenshot_path)

        send_image_to_seatalk(config["SEATALK_WEBHOOK"], screenshot_path, "Relatório Looker Studio")
        log("✅ Ciclo concluído com sucesso.")
    finally:
        if driver:
            driver.quit()
            log("🧹 Driver encerrado.")

# --- Execução principal ---
if __name__ == "__main__":
    executar_ciclo_produtividade()