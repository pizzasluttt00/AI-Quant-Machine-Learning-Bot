# /home/pi/AI-trading/utils/telegram_notify.py

import json
import requests

def notify_telegram(title, message):
    with open('/home/pi/AI-trading/config/telegram_credentials.json') as f:
        creds = json.load(f)

    token = creds["bot_token"]
    chat_id = creds["chat_id"]

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": f"*{title}*\n{message}",
        "parse_mode": "Markdown"
    }

    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram notification failed: {e}")


---

