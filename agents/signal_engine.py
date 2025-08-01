import yfinance as yf
import pandas as pd
from ta.trend import SMAIndicator
from ta.momentum import RSIIndicator
from ta.volume import OnBalanceVolumeIndicator
from sentiment_analyzer import analyze_sentiment
from utils import fetch_news, is_undervalued

def evaluate_signals(symbol):
    data = yf.download(symbol, period="6mo", interval="1d", progress=False)
    if data.empty or "Close" not in data or "Volume" not in data:
        return []

    close = data["Close"]
    volume = data["Volume"]

    # Compute indicators and ensure 1D arrays
    sma10_arr = SMAIndicator(close=close, window=10).sma_indicator().values.flatten()
    sma30_arr = SMAIndicator(close=close, window=30).sma_indicator().values.flatten()
    rsi = RSIIndicator(close=close, window=14).rsi()
    obv = OnBalanceVolumeIndicator(close=close, volume=volume).on_balance_volume()

    # Create series from flattened arrays
    sma10 = pd.Series(sma10_arr, index=close.index, name="sma10")
    sma30 = pd.Series(sma30_arr, index=close.index, name="sma30")

    signals = []

    # SMA crossover
    if sma10.iloc[-1] > sma30.iloc[-1]:
        signals.append({"signal": "bullish", "type": "sma_crossover"})

    # RSI between 50 and 70
    if 50 < rsi.iloc[-1] < 70:
        signals.append({"signal": "bullish", "type": "rsi_mid_trend"})

    # OBV rising
    if obv.iloc[-1] > obv.iloc[-2]:
        signals.append({"signal": "bullish", "type": "obv_up"})

    # Sentiment signal
    sentiment = analyze_sentiment(symbol)
    if sentiment == "positive":
        signals.append({"signal": "bullish", "type": "sentiment"})

    # Valuation check
    undervalued = is_undervalued(symbol)
    signals.append({
        "signal": "bullish" if undervalued else "neutral",
        "type": "valuation",
        "undervalued": undervalued
    })

    return signals
