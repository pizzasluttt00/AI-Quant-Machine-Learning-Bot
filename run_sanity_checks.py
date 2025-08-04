	# FILE: sanity_checks/run_sanity_checks.py

import subprocess
import os

TESTS = [
    "test_config_loading.py",
    "test_api_credentials.py",
    "test_signal_engine.py",
    "test_trade_execution.py",
    "test_telegram_alerts.py",
    "test_flask_launch.py"
]

def run_all():
    base = os.path.dirname(__file__)
    print("\n🧪 Running all sanity checks...\n")
    
    for test in TESTS:
        print(f"▶️  {test}")
        try:
            subprocess.run(["python3", os.path.join(base, test)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌  {test} failed with error code {e.returncode}\n")

if __name__ == "__main__":
    run_all()
