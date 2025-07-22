
def detect_candlestick_patterns(df):
    patterns = []
    last = df.iloc[-1]
    prev = df.iloc[-2]

    body = abs(float(last["c"]) - float(last["o"]))
    candle_range = float(last["h"]) - float(last["l"])

    if body < candle_range * 0.3 and float(last["l"]) < float(prev["l"]) and float(last["h"]) < float(prev["h"]):
        patterns.append("⚠️ Можливий Hammer")

    if float(last["c"]) > float(last["o"]) and float(prev["c"]) < float(prev["o"]) and float(last["c"]) > float(prev["o"]):
        patterns.append("📈 Bullish Engulfing")

    if float(last["c"]) < float(last["o"]) and float(prev["c"]) > float(prev["o"]) and float(last["c"]) < float(prev["o"]):
        patterns.append("📉 Bearish Engulfing")

    return patterns
