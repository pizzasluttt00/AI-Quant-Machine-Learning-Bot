import os
import shutil

REPO_ROOT = "/home/pi/AI-trading"
SANITY_DIR = os.path.join(REPO_ROOT, "sanity_checks")
UTILS_DIR = os.path.join(REPO_ROOT, "utils")

def fix_signal_engine():
    path = os.path.join(SANITY_DIR, "test_signal_engine.py")
    with open(path, "r") as f:
        lines = f.readlines()

    fixed_lines = ["import sys\n", f"sys.path.append('{REPO_ROOT}')\n"]
    for line in lines:
        if not line.strip().startswith("sys.path.append"):
            fixed_lines.append(line)

    with open(path, "w") as f:
        f.writelines(fixed_lines)
    print("✅ Fixed: test_signal_engine.py")

def fix_notify_telegram():
    init_path = os.path.join(UTILS_DIR, "__init__.py")
    notify_path = os.path.join(UTILS_DIR, "notify_telegram.py")
    if os.path.exists(notify_path):
        with open(init_path, "w") as f:
            f.write("from .notify_telegram import notify_telegram\n")
        print("✅ Fixed: notify_telegram import in utils/__init__.py")
    else:
        print("❌ Missing: utils/notify_telegram.py")

def check_load_config():
    found = False
    for root, dirs, files in os.walk(UTILS_DIR):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file)) as f:
                    if "def load_config" in f.read():
                        found = True
    if not found:
        print("❌ Missing: `load_config` function — please add or re-import.")
    else:
        print("✅ Found: load_config defined somewhere in utils/")

def fix_all():
    print("🔧 Running sanity auto-fixes...\n")
    fix_signal_engine()
    fix_notify_telegram()
    check_load_config()
    print("\n🧪 Now re-run your sanity checks!")

if __name__ == "__main__":
    fix_all()
