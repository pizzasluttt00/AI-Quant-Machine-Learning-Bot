import os
from datetime import datetime, timedelta
from alpaca_trade_api import REST
from utils import notify_telegram

# --- 🔐 HARDCODED ALPACA API CREDENTIALS ---
API_KEY = "YOUR_ALPACA_API_KEY"
API_SECRET = "YOUR_ALPACA_API_SECRET"
BASE_URL = "https://paper-api.alpaca.markets"  # Use live URL if applicable
IS_LIVE = False  # Set to True only if trading real money
DRY_RUN = not IS_LIVE

# --- Initialize Alpaca API client ---
api = REST(API_KEY, API_SECRET, BASE_URL)

def place_order(symbol, price, qty, action):
    """
    Places a limit order through Alpaca. In dry-run mode, it simulates the trade.
    """
    if DRY_RUN:
        order_id = f"dryrun-{symbol}-{datetime.utcnow().timestamp()}"
        print(f"🧪 [Dry Run] {action.upper()} {qty} {symbol} @ ${price:.2f} → ID: {order_id}")
        return order_id

    try:
        order = api.submit_order(
            symbol=symbol,
            qty=qty,
            side=action,
            type='limit',
            time_in_force='gtc',
            limit_price=price
        )
        print(f"✅ Order placed: {order.id} | {action.upper()} {qty} {symbol} @ ${price:.2f}")
        return order.id
    except Exception as e:
        print(f"❌ Order failed for {symbol}: {e}")
        notify_telegram(f"❌ Failed to place {action.upper()} order for {symbol}: {e}")
        return None

def cancel_stale_orders():
    """
    Cancels open Alpaca orders that were submitted over 10 minutes ago.
    """
    try:
        cutoff = datetime.utcnow() - timedelta(minutes=10)
        open_orders = api.list_orders(status='open', limit=50)

        for order in open_orders:
            created = order.submitted_at.replace(tzinfo=None)
            if created < cutoff:
                try:
                    api.cancel_order(order.id)
                    print(f"🗑️  Cancelled stale order: {order.symbol} (ID: {order.id})")
                except Exception as cancel_error:
                    print(f"⚠️  Failed to cancel order {order.id}: {cancel_error}")
    except Exception as e:
        print(f"⚠️  Stale order cancellation error: {e}")
        notify_telegram(f"⚠️ Error cancelling stale orders: {e}")
