import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../sym")))

import subprocess

try:
    result = subprocess.run(['flask', '--version'], capture_output=True, text=True)
    assert result.returncode == 0, 'Flask not installed'
    print('✅ flask installed and functional')
except Exception as e:
    print(f'❌ flask launch test failed: {e}')
