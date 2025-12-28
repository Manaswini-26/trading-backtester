import pandas as pd
import numpy as np

def apply_ma_crossover(df, short_window=20, long_window=50):
    """Generates buy/sell signals based on moving average crossovers."""
    # Pandas: Calculate moving averages
    df['SMA_Fast'] = df['Close'].rolling(window=short_window).mean()
    df['SMA_Slow'] = df['Close'].rolling(window=long_window).mean()
    
    # NumPy: Vectorized signal generation (Clean and Fast)
    # Signal = 1 (Buy) when Fast > Slow, else 0
    df['Signal'] = np.where(df['SMA_Fast'] > df['SMA_Slow'], 1, 0)
    
    # Identify the actual trade points (where signal changes)
    # 1.0 = Buy, -1.0 = Sell
    df['Position'] = df['Signal'].diff()
    
    return df