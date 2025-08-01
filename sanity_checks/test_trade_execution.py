try:
    from trade_executor import place_order
    order_id = place_order("AAPL", 100.0, 1, "buy", dry_run=True)
    assert order_id.startswith("dryrun-"), "Dry run order ID incorrect"
    print("✅ trade execution passed")
except Exception as e:
    print(f"❌ trade execution test failed: {e}")
