# Algorithmic Trading Backtester

A high-performance trading strategy backtester built with **Python**, **Pandas**, and **NumPy**. This project demonstrates vectorized data processing and financial performance analysis.

## 🚀 Overview
This tool automates the process of testing "Moving Average Crossover" strategies. Instead of using slow loops, it leverages **NumPy vectorization** to process years of market data in milliseconds.

## 🛠️ Tech Stack
- **Pandas**: Used for time-series manipulation, rolling window calculations, and data alignment.
- **NumPy**: Used for high-speed signal generation and calculating financial metrics (Sharpe Ratio, Volatility).
- **Matplotlib**: Used for visualizing equity curves and trade entry/exit points.
- **YFinance**: Integration with Yahoo Finance API for real-time historical data.

## 📊 Logic & Performance
The system implements a Dual Moving Average strategy:
* **Buy Signal:** When the Short-term SMA crosses above the Long-term SMA.
* **Sell Signal:** When the Short-term SMA crosses below the Long-term SMA.



## 📁 Project Structure
```text
├── data/               # Local cache for downloaded market data
├── src/
│   ├── data_loader.py  # API handling & cleaning
│   ├── strategy.py     # Signal logic (Pandas/NumPy)
│   └── backtester.py   # Performance math engine
├── main.py             # Main entry point
└── requirements.txt    # Project dependencies