import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../sym")))

import json

try:
    from utils import load_config
    config = load_config()
    assert 'symbols' in config, 'Symbols not found in config'
    assert 'capital' in config, 'Capital setting missing'
    print('✅ config loading passed')
except Exception as e:
    print(f'❌ config loading failed: {e}')
