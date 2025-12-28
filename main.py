from src.data_loader import fetch_data
from src.strategy import apply_ma_crossover
from src.backtester import run_backtest
import matplotlib.pyplot as plt

# 1. Get Data
data = fetch_data("AAPL", "2020-01-01", "2023-12-31")

# 2. Apply Strategy
data_with_signals = apply_ma_crossover(data)

# 3. Run Backtest
final_df, stats = run_backtest(data_with_signals)

# 4. Print Results
print("--- Backtest Results ---")
for key, value in stats.items():
    print(f"{key}: {value}")

# 5. Simple Plot
final_df['Equity_Curve'].plot(title="Apple Strategy Growth")
plt.show()