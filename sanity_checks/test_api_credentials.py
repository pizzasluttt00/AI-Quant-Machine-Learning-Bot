import os, json

try:
    creds_path = os.path.join("config", "api_keys.json")
    assert os.path.exists(creds_path), "Missing API key file"
    with open(creds_path) as f:
        creds = json.load(f)
    assert "alpaca_key" in creds and "alpaca_secret" in creds, "Alpaca credentials incomplete"
    print("✅ API credentials passed")
except Exception as e:
    print(f"❌ API credentials test failed: {e}")
