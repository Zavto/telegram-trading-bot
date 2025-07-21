import random

def get_market_signal():
    signals = ["🔴 Шорт за RSI + EMA", "🟢 Лонг підтверджено по патерну", "🟡 Чекати – невизначеність"]
    return random.choice(signals)

def get_current_price():
    import random
    return round(114000 + random.uniform(-500, 500), 2)