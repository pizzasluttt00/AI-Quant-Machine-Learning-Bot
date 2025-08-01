import json
import os
import requests
from datetime import datetime
import pytz

CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.json')
ORDER_STATE_PATH = os.path.join(os.path.dirname(__file__), 'order_state.json')

def load_config():
    with open(CONFIG_PATH, 'r') as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)

def load_order_state():
    if not os.path.exists(ORDER_STATE_PATH):
        return {}
    with open(ORDER_STATE_PATH, 'r') as f:
        return json.load(f)

def save_order_state(state):
    with open(ORDER_STATE_PATH, 'w') as f:
        json.dump(state, f, indent=2)

def notify_telegram(message):
    config = load_config()
    if not config.get("enable_telegram_alerts"):
        return
    token = config["telegram_bot_token"]
    user_id = config["telegram_user_id"]
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    try:
        requests.post(url, data={"chat_id": user_id, "text": message})
    except Exception as e:
        print(f"Telegram error: {e}")

def fetch_news(symbol):
    """Mock function - Replace with actual news sentiment API."""
    return {
        "symbol": symbol,
        "sentiment": "neutral",
        "headline": "No news source configured"
    }

def is_undervalued(symbol, price_data):
    """Basic undervaluation logic using moving averages."""
    try:
        recent = price_data['close'][-5:]
        avg_recent = sum(recent) / len(recent)
        long_term = price_data['close'][-30:]
        avg_long = sum(long_term) / len(long_term)
        return avg_recent < avg_long
    except Exception:
        return False
