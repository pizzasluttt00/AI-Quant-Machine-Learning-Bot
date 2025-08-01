import sys
import os
import time
import json
import requests
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from signal_engine import evaluate_signals
from trade_executor import place_order, cancel_stale_orders
from db_manager import log_signal_data
from utils.trade_logger import load_order_state, save_order_state, log_trade
from utils import load_config, notify_telegram

config = load_config()
SYMBOLS = config["symbols"]
THRESHOLDS = config["auto_trade_thresholds"]
CAPITAL = config["capital"]

def calculate_position_size(price):
    if price <= 0:
        return 0
    return round(CAPITAL / price)

def run():
    print("🚀 QuantBot scanning...")
    order_state = load_order_state()

    for symbol in SYMBOLS:
        try:
            signals = evaluate_signals(symbol)

            if signals.get("total_signals", 0) < THRESHOLDS["min_signals"]:
                print(f"❌   Not enough signals for {symbol}")
                continue

            price = signals["current_price"]
            size = calculate_position_size(price)
            action = "buy"  # currently only long-only

            if size < 1:
                print(f"⚠️  Position size too small for {symbol}")
                continue

            last_trade = order_state.get(symbol, {})
            last_time = last_trade.get("timestamp", 0)
            cooldown_passed = time.time() - last_time > THRESHOLDS["cooldown_seconds"]

            if not cooldown_passed:
                print(f"⏳  Cooldown active for {symbol}")
                continue

            order_id = place_order(symbol, price, size, action)
            if order_id:
                log_trade(symbol, action, price, size)
                notify_telegram(f"📈 Trade Placed: {symbol} @ ${price} x {size}")
                order_state[symbol] = {"timestamp": time.time()}
                save_order_state(order_state)
        except Exception as e:
            print(f"⚠️  Error processing {symbol}: {e}")

    try:
        cancel_stale_orders()
    except Exception as e:
        print(f"⚠️  Error cancelling stale orders: {e}")

    print("✅  Scan complete.")

if __name__ == "__main__":
    run()
