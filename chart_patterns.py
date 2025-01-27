import pandas as pd
import numpy as np

# Head and Shoulders Pattern
def detect_head_and_shoulders(data):
    """Detect Head and Shoulders pattern"""
    # We need at least 3 peaks for a valid Head and Shoulders pattern
    if len(data) < 3:
        return 'no_head_and_shoulders'

    left_shoulder = data['high'].iloc[0]
    head = data['high'].iloc[1]
    right_shoulder = data['high'].iloc[2]

    if left_shoulder < head > right_shoulder:  # Head is higher than shoulders
        return 'head_and_shoulders'
    return 'no_head_and_shoulders'

# Triangle Pattern (Symmetrical, Ascending, Descending)
def detect_triangle(data):
    """Detect Triangle chart pattern (Symmetrical, Ascending, Descending)"""
    if len(data) < 5:
        return 'no_triangle'

    highs = data['high'].iloc[-5:].reset_index(drop=True)  # Reset index
    lows = data['low'].iloc[-5:].reset_index(drop=True)  # Reset index

    # Ascending Triangle: Higher lows and flat tops
    if all(lows[i] < lows[i+1] for i in range(len(lows)-1)) and all(highs[0] == highs[i] for i in range(1, len(highs))):
        return 'ascending_triangle'

    # Descending Triangle: Lower highs and flat bottoms
    if all(highs[i] > highs[i+1] for i in range(len(highs)-1)) and all(lows[0] == lows[i] for i in range(1, len(lows))):
        return 'descending_triangle'

    # Symmetrical Triangle: Both higher lows and lower highs
    if all(lows[i] < lows[i+1] for i in range(len(lows)-1)) and all(highs[i] > highs[i+1] for i in range(len(highs)-1)):
        return 'symmetrical_triangle'

    return 'no_triangle'

# Double Top Pattern
def detect_double_top(data):
    """Detect Double Top chart pattern"""
    if len(data) < 5:
        return 'no_double_top'

    # Check for two peaks at the top with a retracement in between
    peaks = data['high'].rolling(window=3).apply(lambda x: x[1] > x[0] and x[1] > x[2], raw=True)
    peaks = peaks.dropna().astype(int)

    # A valid Double Top pattern requires two peaks followed by a significant drop
    if peaks.sum() == 2:
        peak_indices = peaks.index[peaks == 1]
        if len(peak_indices) == 2 and (data['high'][peak_indices[1]] < data['high'][peak_indices[0]]):
            return 'double_top'

    return 'no_double_top'

# Double Bottom Pattern
def detect_double_bottom(data):
    """Detect Double Bottom chart pattern"""
    if len(data) < 5:
        return 'no_double_bottom'

    # Check for two troughs at the bottom with a retracement in between
    troughs = data['low'].rolling(window=3).apply(lambda x: x[1] < x[0] and x[1] < x[2], raw=True)
    troughs = troughs.dropna().astype(int)

    # A valid Double Bottom pattern requires two troughs followed by a significant rise
    if troughs.sum() == 2:
        trough_indices = troughs.index[troughs == 1]
        if len(trough_indices) == 2 and (data['low'][trough_indices[1]] > data['low'][trough_indices[0]]):
            return 'double_bottom'

    return 'no_double_bottom'
