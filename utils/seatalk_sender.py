import requests
import httpx
import base64
import os
from pathlib import Path
from utils.logs import log


def send_image_to_seatalk(webhook_url, image_path, message_text="📊 Relatório Looker Studio atualizado!"):
    
    try:
        log("📤 Enviando imagem para o SeaTalk...")
        json_payload: dict
        with open(image_path, "rb") as img_file:
            img_bytes: bytes = img_file.read()
            img_base64: str = base64.b64encode(img_bytes).decode("latin-1")

            json_payload = {
                 "tag": "image",
                 "image-base64": {
                      "content": img_base64
                 }
            }

            response = httpx.post(webhook_url, json=json_payload)
            log(f"Status code: {response.status_code}")
            log(f"Resposta SeaTalk: {response.text}")
        
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
    
