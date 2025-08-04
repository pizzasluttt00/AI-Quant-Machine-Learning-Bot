import json, requests, os

def notify_telegram(title, message):
    with open(os.path.join("config", "api_keys.json")) as f:
        creds = json.load(f)
    token = creds["telegram_token"]
    chat_id = creds["telegram_chat_id"]

    text = f"🔔 *{title}*\n{message}"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }

    resp = requests.post(url, json=payload)
    if resp.status_code == 200:
        print("✅ Telegram alert sent")
    else:
        print(f"❌ Failed to send Telegram alert: {resp.text}")
