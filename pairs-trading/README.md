# Pairs Trading: Statistical Arbitrage Strategy

## 📌 Overview
This project implements a classic **Pairs Trading** (Statistical Arbitrage) strategy based on the mean-reversion of the price spread between two historically correlated assets. 

The engine calculates the dynamic hedge ratio (Rolling Beta), constructs the price spread, and generates trading signals based on the spread's Z-score.

## 🧠 Methodology
The strategy operates on the assumption that two related assets will maintain a long-term equilibrium. When their prices diverge significantly, the strategy bets on them converging back to the mean.

1. **Data Fetching**: Historical daily closing prices are downloaded via `yfinance`.
2. **Rolling Hedge Ratio (Beta)**: Instead of using a static beta over the whole period (which is prone to look-ahead bias and regime shifts), we calculate a rolling beta (e.g., 60-day window) using covariance and variance:
   \[
   \beta = \frac{\text{Cov}(Price_A, Price_B)}{\text{Var}(Price_B)}
   \]
3. **Spread Calculation**: The spread is calculated as:
   \[
   Spread = Price_A - (\beta \times Price_B)
   \]
4. **Z-Score Generation**: The spread is normalized using a rolling mean and standard deviation (e.g., 30-day window):
   \[
   Z = \frac{Spread - \mu_{rolling}}{\sigma_{rolling}}
   \]
5. **Trading Signals**:
   * **Short Spread**: If \(Z > 2\), Asset A is overvalued relative to B. Short A, Long B.
   * **Long Spread**: If \(Z < -2\), Asset A is undervalued. Long A, Short B.
   * **Exit**: Close positions when \(Z\) reverts to \(0\).

## 📂 Project Structure
```text
pairs-trading/
├── src/
│   ├── __init__.py
│   └── data_loader.py       # Fetches and cleans historical data
├── tests/
│   └── test_data_loader.py  # Pytest validation for data integrity
├── notebooks/
│   └── research.ipynb       # Research: Beta calculation, Spread & Z-score plotting
├── requirements.txt         # Dependencies
└── conftest.py              # Pytest configuration