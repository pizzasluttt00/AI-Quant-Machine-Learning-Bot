import os, json

try:
    from utils import load_config
    config = load_config()
    assert "symbols" in config, "Symbols not found in config"
    assert "capital" in config, "Capital setting missing"
    print("✅ config loading passed")
except Exception as e:
    print(f"❌ config loading failed: {e}")
