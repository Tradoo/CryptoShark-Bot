import pandas as pd

# Doji Candlestick Pattern
def detect_doji(data):
    """Detect Doji Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['high'] = pd.to_numeric(data['high'], errors='coerce')
    data['low'] = pd.to_numeric(data['low'], errors='coerce')
    
    doji = (abs(data['open'] - data['close']) / (data['high'] - data['low'])) > 0.1
    return 'doji' if doji.any() else 'no_doji'

# Bullish Engulfing Candlestick Pattern
def detect_engulfing(data):
    """Detect Bullish and Bearish Engulfing Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    
    bullish_engulfing = (data['close'] > data['open']) & (data['open'].shift(1) > data['close'].shift(1))
    bearish_engulfing = (data['close'] < data['open']) & (data['open'].shift(1) < data['close'].shift(1))
    
    if bullish_engulfing.any():
        return 'bullish'
    elif bearish_engulfing.any():
        return 'bearish'
    else:
        return 'no_engulfing'

# Hammer Candlestick Pattern
def detect_hammer(data):
    """Detect Hammer Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['high'] = pd.to_numeric(data['high'], errors='coerce')
    data['low'] = pd.to_numeric(data['low'], errors='coerce')
    
    hammer = (data['high'] - data['low']) > 3 * (data['open'] - data['close'])  # Long shadow
    hammer &= (data['close'] - data['low']) < 0.33 * (data['high'] - data['low'])  # Small body
    hammer &= (data['open'] - data['low']) < 0.33 * (data['high'] - data['low'])  # Small body
    return 'hammer' if hammer.any() else 'no_hammer'

# Hanging Man Candlestick Pattern
def detect_hanging_man(data):
    """Detect Hanging Man Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['high'] = pd.to_numeric(data['high'], errors='coerce')
    data['low'] = pd.to_numeric(data['low'], errors='coerce')
    
    hanging_man = (data['high'] - data['low']) > 3 * (data['open'] - data['close'])  # Long shadow
    hanging_man &= (data['close'] - data['low']) < 0.33 * (data['high'] - data['low'])  # Small body
    hanging_man &= (data['open'] - data['low']) < 0.33 * (data['high'] - data['low'])  # Small body
    return 'hanging_man' if hanging_man.any() else 'no_hanging_man'

# Morning Star Candlestick Pattern
def detect_morning_star(data):
    """Detect Morning Star Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    
    morning_star = ((data['close'].shift(2) < data['open'].shift(2))) & \
                   ((data['close'].shift(1) > data['open'].shift(1))) & \
                   ((data['close'] > data['open']))
    return 'morning_star' if morning_star.any() else 'no_morning_star'

# Inverted Hammer Candlestick Pattern
def detect_inverted_hammer(data):
    """Detect Inverted Hammer Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['high'] = pd.to_numeric(data['high'], errors='coerce')
    data['low'] = pd.to_numeric(data['low'], errors='coerce')
    
    inverted_hammer = (data['high'] - data['low']) > 3 * (data['open'] - data['close'])  # Long shadow
    inverted_hammer &= (data['high'] - data['close']) < 0.33 * (data['high'] - data['low'])  # Small body
    inverted_hammer &= (data['high'] - data['open']) < 0.33 * (data['high'] - data['low'])  # Small body
    return 'inverted_hammer' if inverted_hammer.any() else 'no_inverted_hammer'

# Shooting Star Candlestick Pattern
def detect_shooting_star(data):
    """Detect Shooting Star Candlestick Pattern"""
    # Ensure the columns are numeric
    data['open'] = pd.to_numeric(data['open'], errors='coerce')
    data['close'] = pd.to_numeric(data['close'], errors='coerce')
    data['high'] = pd.to_numeric(data['high'], errors='coerce')
    data['low'] = pd.to_numeric(data['low'], errors='coerce')
    
    shooting_star = (data['high'] - data['low']) > 3 * (data['open'] - data['close'])  # Long shadow
    shooting_star &= (data['open'] - data['low']) < 0.33 * (data['high'] - data['low'])  # Small body
    shooting_star &= (data['close'] - data['low']) < 0.33 * (data['high'] - data['low'])  # Small body
    return 'shooting_star' if shooting_star.any() else 'no_shooting_star'
