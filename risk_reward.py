import pandas as pd

# Function to calculate the Risk/Reward ratio
def calculate_risk_reward(entry, stop_loss, take_profit):
    """Calculate the Risk/Reward ratio based on entry, stop-loss, and take-profit levels"""
    if entry <= 0 or stop_loss <= 0 or take_profit <= 0:
        return None  # Invalid input
    
    risk = entry - stop_loss  # Amount at risk (stop-loss distance)
    reward = take_profit - entry  # Potential reward (take-profit distance)
    
    # Risk/Reward ratio calculation
    if risk == 0:
        return None  # Avoid division by zero
    else:
        risk_reward_ratio = reward / risk
        return risk_reward_ratio

# Function to calculate risk/reward ratio for a series of trades (for all symbols)
def calculate_multiple_risk_reward(trades_data):
    """Calculate the Risk/Reward ratios for multiple trades"""
    risk_reward_ratios = []
    
    for trade in trades_data:
        entry = trade['entry']
        stop_loss = trade['stop_loss']
        take_profit = trade['take_profit']
        
        risk_reward_ratio = calculate_risk_reward(entry, stop_loss, take_profit)
        risk_reward_ratios.append(risk_reward_ratio)
    
    return pd.Series(risk_reward_ratios, name='risk_reward')

