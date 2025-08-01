import random

def analyze_sentiment(symbol):
    """
    Dummy sentiment analyzer.
    Replace this with real NLP/news/sentiment feed later.
    """
    sentiments = ['bullish', 'bearish', 'neutral']
    score = random.uniform(-1, 1)
    label = 'bullish' if score > 0.3 else 'bearish' if score < -0.3 else 'neutral'
    return {
        'symbol': symbol,
        'sentiment': label,
        'score': round(score, 2)
    }
