import yfinance as yf
import pandas as pd
from ta.momentum import RSIIndicator
from ta.volume import OnBalanceVolumeIndicator

from utils import fetch_news, is_undervalued

def evaluate_signals(symbol):
    data = yf.download(symbol, period="6mo", interval="1d", progress=False)
    if data.empty or len(data) < 30:
        print(f"⚠️ Not enough data for {symbol}")
        return {
            "symbol": symbol,
            "signals": [],
            "total_signals": 0,
            "undervalued": False,
            "current_price": 0.0
        }

    close = data['Close'].squeeze()
    volume = data['Volume'].squeeze()

    sma10 = close.rolling(window=10).mean()
    sma30 = close.rolling(window=30).mean()
    rsi = RSIIndicator(close=close, window=14).rsi()
    obv = OnBalanceVolumeIndicator(close=close, volume=volume).on_balance_volume()

    latest = {
        'price': close.iloc[-1],
        'sma10': sma10.iloc[-1],
        'sma30': sma30.iloc[-1],
        'rsi': rsi.iloc[-1],
        'obv': obv.iloc[-1],
    }

    signals = []

    if latest['sma10'] > latest['sma30']:
        signals.append({'type': 'trend', 'signal': 'bullish', 'value': 'SMA10 > SMA30'})
    if latest['rsi'] < 30:
        signals.append({'type': 'momentum', 'signal': 'bullish', 'value': 'RSI < 30'})
    if latest['obv'] > obv.mean():
        signals.append({'type': 'volume', 'signal': 'bullish', 'value': 'OBV > avg OBV'})

    try:
        sentiment = fetch_news(symbol)
        if sentiment == 'positive':
            signals.append({'type': 'sentiment', 'signal': 'bullish', 'value': 'Positive news'})
    except Exception as e:
        print(f"News fetch error: {e}")

    undervalued = False
    try:
        undervalued = is_undervalued(symbol)
        if undervalued:
            signals.append({'type': 'valuation', 'signal': 'bullish', 'value': 'Undervalued'})
    except Exception as e:
        print(f"Valuation check error: {e}")

    return {
        "symbol": symbol,
        "signals": signals,
        "total_signals": sum(1 for s in signals if s.get("signal") == "bullish"),
        "undervalued": undervalued,
        "current_price": latest['price']
    }
