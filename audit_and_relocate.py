import os
import shutil

ROOT = os.path.abspath(os.path.dirname(__file__))
DEST = os.path.join(ROOT, 'unorganized')

# Create unorganized folder if missing
os.makedirs(DEST, exist_ok=True)

# Expected structure
EXPECTED = {
    'run.py',
    'config.json',
    'signal_engine.py',
    'trade_executor.py',
    'utils.py',
    'db_manager.py',
    'audit_and_relocate.py',
    'agents',
    'logs',
    'backups',
    'templates',
    '__pycache__'
}

# Nested expected content
EXPECTED_AGENTS = {'quant_agent.py'}
EXPECTED_TEMPLATES = {'index.html'}

moved = []

def move_file(full_path, reason):
    filename = os.path.basename(full_path)
    new_path = os.path.join(DEST, filename)
    shutil.move(full_path, new_path)
    moved.append((full_path, new_path, reason))

def scan_and_move():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for fname in filenames:
            full_path = os.path.join(dirpath, fname)
            rel_path = os.path.relpath(full_path, ROOT)

            # Top-level file
            if dirpath == ROOT:
                if fname not in EXPECTED:
                    move_file(full_path, "Unexpected top-level file")
            elif 'agents' in dirpath:
                if fname not in EXPECTED_AGENTS:
                    move_file(full_path, "Unexpected file in agents/")
            elif 'templates' in dirpath:
                if fname not in EXPECTED_TEMPLATES:
                    move_file(full_path, "Unexpected file in templates/")
            elif '__pycache__' in dirpath:
                continue  # Ignore pycache
            else:
                if not rel_path.startswith(('logs/', 'backups/', 'unorganized/')):
                    move_file(full_path, "File outside known paths")

scan_and_move()

if moved:
    print(f"🧹 Moved {len(moved)} files to: {DEST}")
    for old, new, why in moved:
        print(f"  - {old} → {new}  ({why})")
else:
    print("✅ All files in correct structure.")
