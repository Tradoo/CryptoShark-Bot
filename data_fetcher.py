import requests
import pandas as pd

# MEXC API Base URL
base_url = "https://api.mexc.com"

def fetch_historical_data(symbol, interval='1m', limit=100):
    """Fetch historical data from the MEXC API"""
    endpoint = f"/api/v3/klines"
    params = {
        'symbol': symbol.replace("_", ""),
        'interval': interval,
        'limit': limit
    }
    try:
        response = requests.get(base_url + endpoint, params=params)
        if response.status_code == 200:
            data = response.json()
            # Check the structure of the data
            print(data[:1])  # Output first item to inspect the structure
            
            # Ensure the data is in the correct format
            # Adjust column names based on the returned data structure
            df = pd.DataFrame(data, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume', 
                'close_time', 'quote_asset_volume'
            ])
            
            # Convert 'timestamp' to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            
            # Return the data
            return df
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return None
