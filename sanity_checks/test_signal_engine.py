import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../sym")))

try:
    from signal_engine import sys
sys.path.append('/home/pi/AI-trading')
from signal_engine import evaluate_signals  # or whatever is needed
    result = evaluate_signals('AAPL')
    assert isinstance(result, dict), 'Signal result is not a dictionary'
    print('✅ signal engine passed')
except Exception as e:
    print(f'❌ signal engine test failed: {e}')
