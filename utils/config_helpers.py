import json
import requests

def load_config(path="config.json"):
    with open(path, "r") as f:
        return json.load(f)

def notify_telegram(token, user_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": user_id, "text": message}
    try:
        response = requests.post(url, json=payload)
        return response.ok
    except Exception as e:
        print(f"[Telegram Error] {e}")
        return False
