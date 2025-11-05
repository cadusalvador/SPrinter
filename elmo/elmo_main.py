from utils.driver import create_chrome_driver
from utils.helpers import load_env
from utils.logs import log
from utils.seatalk_sender import send_image_to_seatalk
import os
import time

def executar_elmo():
    config = load_env()
    driver = create_chrome_driver(config, headless=True, window_size="2560,1440")

    try:
        url = config["ELMO_LOOKER_URL_FECHAMENTO"]
        log(f"🤖 Elmo iniciando captura do dashboard alternativo: {url}")

        driver.get(url)
        time.sleep(10)

        screenshot_path = os.path.join(config["ELMO_PRINT_PATH"])
        driver.save_screenshot(screenshot_path)
        log(f"📸 Elmo salvou print em {screenshot_path}")

        webhook = config["ELMO_SEATALK_WEBHOOK_URL"]
        if webhook:
            log("📤 Enviando print do Elmo para o SeaTalk...")
            send_image_to_seatalk(
                webhook_url=webhook,
                image_path=screenshot_path,
                message_text="🤖 Elmo diz: 📊 Segue reporte operacional:"
            )
            log("✅ Print enviado ao SeaTalk!")

        else:
            log("⚠️ Nenhum webhook configurado para envio ao SeaTalk.")
    except Exception as e:
        log(f"❌ Erro ao executar Elmo: {e}")

    finally:
        driver.quit()
        log("🧹 Elmo finalizou execução.")
