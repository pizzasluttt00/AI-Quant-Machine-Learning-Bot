try:
    from signal_engine import evaluate_signals
    result = evaluate_signals("AAPL")
    assert isinstance(result, dict), "Signal result is not a dictionary"
    print("✅ signal engine passed")
except Exception as e:
    print(f"❌ signal engine test failed: {e}")
