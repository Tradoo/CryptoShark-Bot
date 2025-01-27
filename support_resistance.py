import pandas as pd
import numpy as np

# Function to calculate support levels
def calculate_support(data, window=5):
    """Calculate Support levels (local minima)"""
    support_levels = []
    for i in range(window, len(data) - window):
        if data['low'][i] == min(data['low'][i - window:i + window]):
            support_levels.append(data['low'][i])
        else:
            support_levels.append(np.nan)
    
    return pd.Series(support_levels, index=data.index[window:len(data) - window])

# Function to calculate resistance levels
def calculate_resistance(data, window=5):
    """Calculate Resistance levels (local maxima)"""
    resistance_levels = []
    for i in range(window, len(data) - window):
        if data['high'][i] == max(data['high'][i - window:i + window]):
            resistance_levels.append(data['high'][i])
        else:
            resistance_levels.append(np.nan)
    
    return pd.Series(resistance_levels, index=data.index[window:len(data) - window])

# Function to calculate support and resistance levels together
def calculate_support_resistance(data, window=5):
    """Calculate both Support and Resistance levels"""
    support = calculate_support(data, window)
    resistance = calculate_resistance(data, window)
    
    # Handle cases where there may be NaN values in support or resistance
    support = support.dropna().iloc[-1] if not support.dropna().empty else None
    resistance = resistance.dropna().iloc[-1] if not resistance.dropna().empty else None
    
    # Return the latest support and resistance values
    return support, resistance


