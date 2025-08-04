#!/bin/bash
echo "🔧 Regenerating all sanity check scripts in /sanity_checks..."

mkdir -p sanity_checks

# Test 1: config loading
cat > sanity_checks/test_config_loading.py << 'EOF'
import sys, os, json
sys.path.append(os.path.abspath("../sym/utils"))
from notify_telegram import load_config

try:
    config = load_config()
    assert "symbols" in config, "Symbols not found in config"
    assert "capital" in config, "Capital setting missing"
    print("✅ config loading passed")
except Exception as e:
    print(f"❌ config loading failed: {e}")
EOF

# Test 2: API credentials
cat > sanity_checks/test_api_credentials.py << 'EOF'
import os, json

try:
    creds_path = os.path.abspath("../sym/config/api_keys.json")
    assert os.path.exists(creds_path), "Missing API key file"
    with open(creds_path) as f:
        creds = json.load(f)
    required = ["alpaca_key", "alpaca_secret", "telegram_token", "telegram_chat_id"]
    for key in required:
        assert key in creds, f"Missing key: {key}"
    print("✅ API credentials passed")
except Exception as e:
    print(f"❌ API credentials test failed: {e}")
EOF

# Test 3: signal engine
cat > sanity_checks/test_signal_engine.py << 'EOF'
import sys, os
sys.path.append(os.path.abspath("../"))
from signal_engine import evaluate_signals

try:
    result = evaluate_signals("AAPL")
    assert isinstance(result, dict), "Signal result is not a dictionary"
    print("✅ signal engine passed")
except Exception as e:
    print(f"❌ signal engine test failed: {e}")
EOF

# Test 4: trade executor
cat > sanity_checks/test_trade_execution.py << 'EOF'
import sys, os
sys.path.append(os.path.abspath("../"))
from trade_executor import place_order

try:
    order_id = place_order("AAPL", 100.0, 1, "buy", dry_run=True)
    assert order_id.startswith("dryrun-"), "Dry run order ID incorrect"
    print("✅ trade execution passed")
except Exception as e:
    print(f"❌ trade execution test failed: {e}")
EOF

# Test 5: telegram alerts
cat > sanity_checks/test_telegram_alerts.py << 'EOF'
import sys, os, json
sys.path.append(os.path.abspath("../sym/utils"))

try:
    from notify_telegram import notify_telegram
    notify_telegram("Sanity Check", "✅ Telegram is working!")
    print("✅ telegram alert passed (check your Telegram)")
except Exception as e:
    print(f"❌ telegram alert test failed: {e}")
EOF

# Test 6: flask installed
cat > sanity_checks/test_flask_launch.py << 'EOF'
try:
    import subprocess
    result = subprocess.run(["flask", "--version"], capture_output=True, text=True)
    assert result.returncode == 0, "Flask not installed"
    print("✅ flask installed and functional")
except Exception as e:
    print(f"❌ flask launch test failed: {e}")
EOF

# Runner
cat > sanity_checks/run_sanity_checks.py << 'EOF'
import os
import subprocess

print("🧪 Running all sanity checks...\n")
tests = [f for f in os.listdir(".") if f.startswith("test_") and f.endswith(".py")]
for test in sorted(tests):
    print(f"▶️ {test}")
    subprocess.run(["python3", test])
    print()
EOF

chmod +x sanity_checks/*.py
echo "✅ All sanity check scripts regenerated!"
