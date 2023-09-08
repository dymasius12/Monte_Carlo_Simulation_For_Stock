# Monte Carlo Stock Price Prediction

This script uses the Monte Carlo method to simulate possible future stock prices based on historical stock data fetched from Yahoo Finance. Learn from this youtube channel: https://www.youtube.com/watch?v=6-dhdMDiYWQ

## Features:

1. Fetches historical stock data using the `yfinance` library.
2. Calculates daily returns and uses them to determine the mean and standard deviation.
3. Simulates future stock prices based on the historical data.
4. Plots the simulated stock price paths along with their average path.

## Dependencies:

- numpy
- matplotlib
- yfinance

To install the required libraries, run:
```
pip install numpy matplotlib yfinance
```

## Usage:

Execute the script. You will be prompted to enter the stock ticker (e.g., AAPL for Apple Inc.). After entering the ticker, the script fetches the historical data, runs the Monte Carlo simulation, and then plots the results. The individual simulated paths are displayed in light gray, while the average path is shown in blue.

```python
python Monte_Carlo_Simulation.py
```

## Functions:

- `fetch_stock_data(ticker, period="1y")`: Fetches historical stock data for the given ticker and period.
- `monte_carlo_simulation(ticker, num_simulations=1000, num_days=252)`: Runs the Monte Carlo simulation to predict future stock prices.
- `plot_simulation(ticker, simulations)`: Plots the simulated stock price paths and their average.
