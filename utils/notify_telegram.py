import json, os, requests

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '../config/api_keys.json')

def notify_telegram(title, message):
    try:
        with open(CONFIG_PATH) as f:
            creds = json.load(f)
        token = creds["telegram_token"]
        chat_id = creds["telegram_chat_id"]
        text = f"📢 *{title}*\n{message}"
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        res = requests.post(url, data=data)
        if not res.ok:
            print("Telegram error:", res.text)
        else:
            print("✅ Telegram message sent")
    except Exception as e:
        print(f"❌ Telegram notify failed: {e}")
