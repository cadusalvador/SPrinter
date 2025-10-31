import requests
from pathlib import Path


def send_image_to_seatalk(webhook_url, image_path, message_text=None):
    if not webhook_url:
        raise ValueError("SEATALK_WEBHOOK não configurado")
    
    with open(image_path, "rb") as f:
        files = {"file": (Path(image_path).name, f, "image/png")}
        data = {"text": message_text or "Screenshot do Looker Studio"}
        resp = requests.post(webhook_url, data=data, files=files, timeout=30)

    if resp.status_code >= 300:
        print("Erro ao enviar para Seatalk: ", resp.status_code, resp.text)
    else:
        print("Enviado para Seatalk com sucesso!")