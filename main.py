import time
import pandas as pd
from data_fetcher import fetch_historical_data
from indicators import calculate_sma, calculate_rsi, calculate_macd, calculate_stochastic, calculate_fibonacci
from candlestick_patterns import detect_doji, detect_engulfing, detect_hammer, detect_hanging_man, detect_morning_star, detect_inverted_hammer, detect_shooting_star
from chart_patterns import detect_head_and_shoulders, detect_triangle, detect_double_top, detect_double_bottom
from support_resistance import calculate_support_resistance
from risk_reward import calculate_risk_reward

# Configuration
symbols = [
    'BTC_USDT', 'ETH_USDT', 'BNB_USDT', 'XRP_USDT', "SOL_USDT", "DOGE_USDT", "PEPE_USDT", "SUI_USDT", "LINK_USDT", "SHIB_USDT", "SEI_USDT", "TRX_USDT"
]

# Loop through each symbol (coin) in the list
while True:
    for symbol in symbols:
        print(f"\n\u25B6 Monitoring {symbol}...")

        # Fetch historical data (e.g., last 100 minutes of data)
        historical_data = fetch_historical_data(symbol, interval='1m', limit=1000)

        print()
        if historical_data is not None:
            print(f"Fetching Historical Data...")

            # Convert the 'close' column to numeric to avoid issues with diff()
            historical_data['close'] = pd.to_numeric(historical_data['close'], errors='coerce')

            # Calculate indicators
            sma = calculate_sma(historical_data, period=14)
            rsi = calculate_rsi(historical_data)
            macd, signal_line = calculate_macd(historical_data)
            stochastic = calculate_stochastic(historical_data)
            fibonacci_levels = calculate_fibonacci(historical_data)

            # Detect candlestick patterns
            doji = detect_doji(historical_data)
            engulfing = detect_engulfing(historical_data)
            hammer = detect_hammer(historical_data)
            hanging_man = detect_hanging_man(historical_data)
            morning_star = detect_morning_star(historical_data)
            inverted_hammer = detect_inverted_hammer(historical_data)
            shooting_star = detect_shooting_star(historical_data)

            # Detect chart patterns
            head_and_shoulders = detect_head_and_shoulders(historical_data)
            triangle = detect_triangle(historical_data)
            double_top = detect_double_top(historical_data)
            double_bottom = detect_double_bottom(historical_data)

            # Calculate support and resistance
            support, resistance = calculate_support_resistance(historical_data)

            # Check if a signal is confirmed by at least three conditions
            signal_confirmations = 0
            signal_reasons = []
            signal_message = None  # Will indicate whether the price is going up or down

            # SMA Confirmation
            if len(sma) > 0:
                if historical_data['close'].iloc[-1] > sma.iloc[-1]:
                    signal_confirmations += 1
                    signal_reasons.append("Price above SMA")
                    signal_message = "Price likely to go up from here."
                elif historical_data['close'].iloc[-1] < sma.iloc[-1]:
                    signal_confirmations += 1
                    signal_reasons.append("Price below SMA")
                    signal_message = "Price likely to go down from here."

            # RSI Confirmation
            if len(rsi) > 0:
                last_rsi_value = rsi.iloc[-1]
                if last_rsi_value < 30:
                    signal_confirmations += 1
                    signal_reasons.append("RSI oversold")
                    signal_message = "Price likely to go up from here."
                elif last_rsi_value > 70:
                    signal_confirmations += 1
                    signal_reasons.append("RSI overbought")
                    signal_message = "Price likely to go down from here."

            # MACD Confirmation
            if len(macd) > 0 and macd[-1] > signal_line[-1] and macd[-2] < signal_line[-2]:
                signal_confirmations += 1
                signal_reasons.append("Bullish MACD crossover")
                signal_message = "Price likely to go up from here."
            elif len(macd) > 0 and macd[-1] < signal_line[-1] and macd[-2] > signal_line[-2]:
                signal_confirmations += 1
                signal_reasons.append("Bearish MACD crossover")
                signal_message = "Price likely to go down from here."

            # Candlestick Patterns
            if engulfing or hammer or morning_star:
                signal_confirmations += 1
                signal_reasons.append("Bullish candlestick pattern")
                signal_message = "Price likely to go up from here."
            elif shooting_star or hanging_man:
                signal_confirmations += 1
                signal_reasons.append("Bearish candlestick pattern")
                signal_message = "Price likely to go down from here."

            # Support/Resistance Breakout
            if support is not None and resistance is not None:
                try:
                    support = float(support)
                    resistance = float(resistance)
                    if historical_data['close'].iloc[-1] > resistance:
                        signal_confirmations += 1
                        signal_reasons.append("Breakout above resistance")
                        signal_message = "Price likely to go up from here."
                    elif historical_data['close'].iloc[-1] < support:
                        signal_confirmations += 1
                        signal_reasons.append("Breakdown below support")
                        signal_message = "Price likely to go down from here."
                except ValueError:
                    print(f"Invalid support or resistance value for {symbol}. Skipping breakout check.")

            # Print Signal Summary
            print(f"\n\u2501\u2501\u2501\u2501 SIGNAL SUMMARY FOR {symbol} \u2501\u2501\u2501\u2501")
            for reason in signal_reasons:
                print(f"- {reason}")

            # Check if a signal is confirmed
            if signal_confirmations >= 3:
                print(f"\u2714 {signal_message} \u2714")

                if "up" in signal_message:
                    # Calculate Entry Price, Stop Loss, and Take Profit
                    entry_price = historical_data['close'].iloc[-1]
                    stop_loss = entry_price * 0.98  # Example: 2% below entry
                    take_profit = entry_price * 1.05  # Example: 5% above entry

                    print(f"Entry Price: {entry_price}")
                    print(f"Stop Loss: {stop_loss}")
                    print(f"Take Profit: {take_profit}")

                    # Calculate Risk/Reward
                    risk_reward_ratio = calculate_risk_reward(entry_price, stop_loss, take_profit)
                    if risk_reward_ratio is not None:
                        print(f"Risk/Reward Ratio: {risk_reward_ratio:.2f}")
                    else:
                        print(f"Risk/Reward ratio calculation failed for {symbol}.")

                    print(f"\u23F3 Pausing for 80 seconds due to signal confirmation... \u23F3")
                    time.sleep(80)
                

            else:
                print(f"\u274C Signal not confirmed for {symbol}, no action taken. \u274C")

        else:
            print(f"Failed to fetch data for {symbol}. Skipping...")

        time.sleep(5)  # Wait 5 seconds before checking the next coin

    print("\n\u23F3 Cycle complete. Waiting for 60 seconds before the next cycle. \u23F3\n")
    time.sleep(60)
