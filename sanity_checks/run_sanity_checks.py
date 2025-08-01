import os
import subprocess

print("🧪 Running all sanity checks...\n")
tests = [f for f in os.listdir(".") if f.startswith("test_") and f.endswith(".py")]
for test in sorted(tests):
    print(f"▶️ {test}")
    subprocess.run(["python3", test])
    print()
