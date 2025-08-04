import json
import os
from datetime import datetime

REQUIRED_KEYS = {
    "alpaca_key": "6V8UyYr3cXTnPYY0lGJLxvd3sDa0J6sAXAU2xXEC",
    "alpaca_secret": "PKQ0YK19VVLXIOH9HY6V",
    "telegram_token": "6748112285:AAFu5upBqggUtXPA9n_5KSh_XZuBU47-8rk",
    "telegram_chat_id": "1979554243",
    "reddit_client_id": "8Q4ieFqquHazulJP1TSXrQ",
    "reddit_client_secret": "ZzY_NNEw0F2GKny0_FJo9p9Uf8O36g",
    "reddit_username": "Bulky_Basket_9224",
    "reddit_password": "JELLYbabies3"
}

CONFIG_PATH = "config/api_keys.json"

def load_current_keys():
    if not os.path.exists(CONFIG_PATH):
        return {}

    with open(CONFIG_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"❌ Invalid JSON format: {e}")
            return {}

def backup_file():
    if os.path.exists(CONFIG_PATH):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup_path = f"{CONFIG_PATH}.bak.{timestamp}"
        os.system(f"cp {CONFIG_PATH} {backup_path}")
        print(f"📦 Backup created at: {backup_path}")

def update_keys():
    current_keys = load_current_keys()
    updated = False

    for key, value in REQUIRED_KEYS.items():
        if current_keys.get(key) != value:
            print(f"🔄 Updating key: {key}")
            current_keys[key] = value
            updated = True

    if updated:
        backup_file()
        with open(CONFIG_PATH, "w") as f:
            json.dump(current_keys, f, indent=2)
        print("✅ api_keys.json updated successfully.")
    else:
        print("✅ All keys are already up to date.")

if __name__ == "__main__":
    update_keys()
