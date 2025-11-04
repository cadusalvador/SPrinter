import httpx
import base64
from utils.logs import log


def send_image_to_seatalk(webhook_url, image_path, message_text="📊 Visão Geral"):
    
    try:
        log("📤 Enviando imagem para o SeaTalk...")
        json_payload_txt: dict
        json_payload_img: dict

        log("📤 Enviando mensagem de texto para o SeaTalk...")
        json_payload_txt = {
            "tag": "text",
            "text": {
                "format": 1,
                "content": message_text
            }
        }
        text_response = httpx.post(webhook_url, json=json_payload_txt)
        log(f"📝 Texto enviado | Status: {text_response.status_code} | Resposta: {text_response.text}")

        with open(image_path, "rb") as img_file:
            img_bytes: bytes = img_file.read()
            img_base64: str = base64.b64encode(img_bytes).decode("latin-1")

            json_payload_img = {     
                "tag": "image",
                "image_base64": {
                    "content": img_base64
                }
            }

            response = httpx.post(webhook_url, json=json_payload_img)
            log(f"Status code: {response.status_code}")
            log(f"Resposta SeaTalk: {response.text}")
        
            if response.status_code == 200:
                log("📨 Imagem enviada com sucesso para o grupo SeaTalk ✅")
                return True
            else:
                log(f"⚠️ Falha ao enviar imagem. Código HTTP: {response.status_code}")
                log(f"Resposta: {response.text}")
                return False
    except Exception as e:
            log(f"❌ Erro ao enviar imagem ao SeaTalk: {e}")
            return False
    
