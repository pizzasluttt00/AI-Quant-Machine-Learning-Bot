import random

def fetch_news(symbol):
    # Fake headlines for now
    return [
        f"{symbol} surges on bullish momentum",
        f"{symbol} posts strong earnings",
        f"{symbol} sees institutional buying"
    ]

def is_undervalued(symbol):
    # Dummy valuation logic
    return random.choice([True, False])
