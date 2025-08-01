#FILE: sanity_checks/run_sanity_checks.py

import subprocess import os

TESTS = [ "test_config_loading.py", "test_api_credentials.py", "test_signal_engine.py", "test_trade_execution.py", "test_telegram_alerts.py", "test_flask_launch.py" ]

def run_all(): base = os.path.dirname(file) print("\n🧪 Running Sanity Checks...\n") for test in TESTS: path = os.path.join(base, test) print(f"Running: {test}") result = subprocess.run(["python3", path], capture_output=True, text=True) if result.returncode == 0: print(f"✅  {test} PASSED\n") else: print(f"❌  {test} FAILED:\n{result.stderr}\n")

if name == "main": run_all()


