import os

SANITY_DIR = "/home/pi/AI-trading/sanity_checks"
REPO_ROOT = "/home/pi/AI-trading"
IMPORT_FIXES = {
    "from utils_local": "from utils"
}

def fix_file(filepath):
    changed = False
    with open(filepath, "r") as f:
        lines = f.readlines()

    new_lines = []
    has_sys_import = False
    inserted_path = False

    for line in lines:
        for old, new in IMPORT_FIXES.items():
            if old in line:
                line = line.replace(old, new)
                changed = True

        if line.strip().startswith("import sys"):
            has_sys_import = True

        if "sys.path.append" in line:
            inserted_path = True

        new_lines.append(line)

    if not has_sys_import:
        new_lines.insert(0, "import sys\n")
        changed = True

    if not inserted_path:
        new_lines.insert(1, f"sys.path.append('{REPO_ROOT}')\n")
        changed = True

    if changed:
        with open(filepath, "w") as f:
            f.writelines(new_lines)
        print(f"✅ Fixed: {os.path.basename(filepath)}")
    else:
        print(f"✅ Already OK: {os.path.basename(filepath)}")

def main():
    print("🔧 Fixing sanity check scripts...")
    for fname in os.listdir(SANITY_DIR):
        if fname.startswith("test_") and fname.endswith(".py"):
            fix_file(os.path.join(SANITY_DIR, fname))
    print("✅ All done.")

if __name__ == "__main__":
    main()
