import requests
from utils.helpers import load_env
from utils.logs import log

def import_token():
    config = load_env()

    app_id = config["APP_ID"]
    app_secret = config["APP_SECRET"]

    resp = requests.post(
        config["LINK_APP_TOKEN"],
        json={
            "app_id": app_id,
            "app_secret": app_secret
        }
    )
    resp.raise_for_status()
    token = resp.json()["app_access_token"]

    print("Status Code: ", resp.status_code)
    print("Response text: ", resp.text)
    log("✅ Token do SeaTalk obtido com sucesso")
    
    return token
