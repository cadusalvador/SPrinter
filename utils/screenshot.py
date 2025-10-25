import os
from utils.helpers import log

def print_save(driver, path_file): 
    if driver:
        try:
            os.makedirs(os.path,dirname(path_file), exist_ok=True)
            driver.save_screenshot(path_file)
            log(f"✅ Screenshot salvo em: {path_file}")
            return True
        except Exception as e:
            log(f"❌ Erro ao tirar screenshot: {e}")
            return False

