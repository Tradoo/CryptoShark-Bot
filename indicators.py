import numpy as np
import pandas as pd

def calculate_sma(data, period=50):
    """Calculate the Simple Moving Average (SMA)"""
    sma = data['close'].rolling(window=period).mean()
    
    # Optionally, drop NaN values if needed for further calculations
    sma = sma.dropna()  # Drop NaN values
    
    return sma

# Exponential Moving Average (EMA)
def calculate_ema(data, period=50):
    """Calculate the Exponential Moving Average (EMA)"""
    ema = data['close'].ewm(span=period, adjust=False).mean()
    return ema

def calculate_rsi(data, period=14, smoothing=True):
    """Calculate the Relative Strength Index (RSI) with smoothing (optional)"""
    
    # Calculate the price change
    delta = data['close'].diff()
    
    # Separate gains and losses
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    
    # Calculate Relative Strength (RS)
    rs = gain / loss
    
    # Calculate RSI without smoothing (standard)
    rsi = 100 - (100 / (1 + rs))
    
    if smoothing:
        # Apply exponential smoothing to RSI for a smoother chart
        rsi = rsi.ewm(span=period, adjust=False).mean()
    
    return rsi

# Moving Average Convergence Divergence (MACD)
def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
    """Calculate the Moving Average Convergence Divergence (MACD)"""
    macd_line = calculate_ema(data, fast_period) - calculate_ema(data, slow_period)
    signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
    return {'macd_line': macd_line, 'signal_line': signal_line}

# Volume Analysis (Simple)
def calculate_volume(data):
    """Simple Volume Analysis"""
    return data['volume']

# Stochastic Oscillator
def calculate_stochastic(data, k_period=14, d_period=3):
    """Calculate the Stochastic Oscillator"""
    low_min = data['low'].rolling(window=k_period).min()
    high_max = data['high'].rolling(window=k_period).max()
    
    stoch_k = 100 * (data['close'] - low_min) / (high_max - low_min)
    stoch_d = stoch_k.rolling(window=d_period).mean()
    
    return {'stochastic_k': stoch_k, 'stochastic_d': stoch_d}

def calculate_fibonacci(data):
    """Calculate Fibonacci retracement levels based on high and low of data"""
    # Ensure the 'high' and 'low' columns are numeric
    data['high'] = pd.to_numeric(data['high'], errors='coerce')
    data['low'] = pd.to_numeric(data['low'], errors='coerce')
    
    max_price = data['high'].max()
    min_price = data['low'].min()
    diff = max_price - min_price
    
    levels = {
        'level_0': max_price,
        'level_236': max_price - 0.236 * diff,
        'level_382': max_price - 0.382 * diff,
        'level_50': max_price - 0.5 * diff,
        'level_618': max_price - 0.618 * diff,
        'level_100': min_price
    }
    
    return levels

