#!/bin/bash
echo "🔧 Setting up sanity check files in /sanity_checks..."

mkdir -p sanity_checks

PY_HEADER='import sys, os\nsys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../sym")))'

# Test 1: config loading
echo -e "$PY_HEADER\n\nimport json\n\ntry:\n    from utils import load_config\n    config = load_config()\n    assert 'symbols' in config, 'Symbols not found in config'\n    assert 'capital' in config, 'Capital setting missing'\n    print('✅ config loading passed')\nexcept Exception as e:\n    print(f'❌ config loading failed: {e}')" > sanity_checks/test_config_loading.py

# Test 2: API credentials
echo -e "$PY_HEADER\n\nimport json\n\ntry:\n    creds_path = os.path.join('../config', 'api_keys.json')\n    assert os.path.exists(creds_path), 'Missing API key file'\n    with open(creds_path) as f:\n        creds = json.load(f)\n    assert 'alpaca_key' in creds and 'alpaca_secret' in creds, 'Alpaca credentials incomplete'\n    print('✅ API credentials passed')\nexcept Exception as e:\n    print(f'❌ API credentials test failed: {e}')" > sanity_checks/test_api_credentials.py

# Test 3: signal engine
echo -e "$PY_HEADER\n\ntry:\n    from signal_engine import evaluate_signals\n    result = evaluate_signals('AAPL')\n    assert isinstance(result, dict), 'Signal result is not a dictionary'\n    print('✅ signal engine passed')\nexcept Exception as e:\n    print(f'❌ signal engine test failed: {e}')" > sanity_checks/test_signal_engine.py

# Test 4: trade executor
echo -e "$PY_HEADER\n\ntry:\n    from trade_executor import place_order\n    order_id = place_order('AAPL', 100.0, 1, 'buy', dry_run=True)\n    assert order_id.startswith('dryrun-'), 'Dry run order ID incorrect'\n    print('✅ trade execution passed')\nexcept Exception as e:\n    print(f'❌ trade execution test failed: {e}')" > sanity_checks/test_trade_execution.py

# Test 5: telegram alerts
echo -e "$PY_HEADER\n\ntry:\n    from utils import notify_telegram\n    notify_telegram('sanity-check', 'Sanity check: Telegram is working')\n    print('✅ telegram alert passed (check your Telegram)')\nexcept Exception as e:\n    print(f'❌ telegram alert test failed: {e}')" > sanity_checks/test_telegram_alerts.py

# Test 6: flask installed
echo -e "$PY_HEADER\n\nimport subprocess\n\ntry:\n    result = subprocess.run(['flask', '--version'], capture_output=True, text=True)\n    assert result.returncode == 0, 'Flask not installed'\n    print('✅ flask installed and functional')\nexcept Exception as e:\n    print(f'❌ flask launch test failed: {e}')" > sanity_checks/test_flask_launch.py

# Runner for all sanity tests
echo -e "$PY_HEADER\n\nimport os\nimport subprocess\n\nprint('🧪 Running all sanity checks...\\n')\ntests = [f for f in os.listdir('.') if f.startswith('test_') and f.endswith('.py')]\nfor test in sorted(tests):\n    print(f'▶️ {test}')\n    subprocess.run(['python3', test])\n    print()" > sanity_checks/run_sanity_checks.py

chmod +x sanity_checks/*.py

echo "✅ All sanity check scripts regenerated with path fixes!"
