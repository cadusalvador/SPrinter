import requests
import os
from pathlib import Path
from utils.logs import log


def send_image_to_seatalk(webhook_url, image_path, message_text="Screenshot enviada pelo SPrinter"):

    if not webhook_url:
        log("❌ Webhook do SeaTalk não configurado.")
        return False
    
    if not os.path.exists(image_path):
        log(f"❌ Arquivo de imagem não encontrado: {image_path}")
        return False
    
    try:
        log("📤 Enviando imagem para o SeaTalk...")
        with open(image_path, "rb") as img_file:
            files = {"file": (Path(image_path).name, img_file, "image/png")}
            data = {"text": message_text or "Screenshot do Looker Studio"}
            response = requests.post(webhook_url, data=data, files=files)
        
        if response.status_code ==200:
            log("📨 Imagem enviada com sucesso para o grupo SeaTalk ✅")
            return True
        else:
            log(f"⚠️ Falha ao enviar imagem. Código HTTP: {response.status_code}")
            log(f"Resposta: {response.text}")
            return False
    except Exception as e:
            log(f"❌ Erro ao enviar imagem ao SeaTalk: {e}")
            return False
    
    