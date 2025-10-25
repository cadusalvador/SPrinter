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


    

    





    