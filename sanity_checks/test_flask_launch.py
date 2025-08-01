try:
    import subprocess
    result = subprocess.run(["flask", "--version"], capture_output=True, text=True)
    assert result.returncode == 0, "Flask not installed"
    print("✅ flask installed and functional")
except Exception as e:
    print(f"❌ flask launch test failed: {e}")
