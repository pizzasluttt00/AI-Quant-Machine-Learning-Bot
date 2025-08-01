import json
import os
from datetime import datetime

STATE_FILE = "order_state.json"

def log_trade(symbol, order_type, price=0.0, qty=0):
    with open("trade_log.txt", "a") as f:
        f.write(f"{datetime.utcnow()} | {symbol} | {order_type.upper()} | Price: {price} | Qty: {qty}\n")

def load_order_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_order_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)
