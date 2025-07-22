import requests
import pandas as pd
import pandas_ta as ta
from ta_utils import detect_candlestick_patterns

def get_klines(symbol="BTCUSDT", interval="1h", limit=100):
    url = f"https://api.mexc.com/api/v3/klines?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data, columns=["time", "o", "h", "l", "c", "v", "_", "_", "_", "_", "_", "_"])
    df["c"] = pd.to_numeric(df["c"])
    return df

def get_market_signal():
    df = get_klines()
    df["rsi"] = ta.rsi(df["c"], length=14)
    df["ema"] = ta.ema(df["c"], length=20)
    patterns = detect_candlestick_patterns(df)

    latest = df.iloc[-1]
    signal = []
    if latest["rsi"] < 30:
        signal.append("🔵 RSI в зоні перепроданості")
    elif latest["rsi"] > 70:
        signal.append("🔴 RSI в зоні перекупленості")

    if latest["c"] > latest["ema"]:
        signal.append("🟢 Ціна вище EMA (аптренд)")
    else:
        signal.append("🔻 Ціна нижче EMA (даунтренд)")

    signal.extend(patterns)
    return "\n".join(signal)  # <- ось так правильно

def get_current_price():
    df = get_klines(limit=2)
    return round(df.iloc[-1]["c"], 2)
