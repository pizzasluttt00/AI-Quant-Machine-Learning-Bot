try:
    from utils import notify_telegram
    notify_telegram("sanity-check", "Sanity check: Telegram is working")
    print("✅ telegram alert passed (check your Telegram)")
except Exception as e:
    print(f"❌ telegram alert test failed: {e}")
