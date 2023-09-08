import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def fetch_stock_data(ticker, period="1y"):
    """Fetch historical stock data using yfinance."""
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data

def monte_carlo_simulation(ticker, num_simulations=1000, num_days=252):
    """Run a Monte Carlo simulation for future stock prices."""
    
    # Fetch historical data
    data = fetch_stock_data(ticker)
    
    # Calculate daily returns
    returns = data['Close'].pct_change().dropna()
    
    # Calculate mean and standard deviation of daily returns
    mu = returns.mean()
    sigma = returns.std()
    
    # Initialize array for simulations
    simulations = np.zeros((num_days, num_simulations))
    
    # Set first row of simulations to the last closing price
    simulations[0] = data['Close'].iloc[-1]
    
    # Simulate future stock prices
    for simulation in range(num_simulations):
        for day in range(1, num_days):
            simulations[day, simulation] = (simulations[day - 1, simulation]
                                            * (1 + np.random.normal(mu, sigma)))
    
    return simulations

def plot_simulation(ticker, simulations):
    """Plot the Monte Carlo simulation results."""
    # Compute the average path
    average_path = np.mean(simulations, axis=1)
    
    plt.figure(figsize=(10,5))
    for i in range(simulations.shape[1]):
        plt.plot(simulations[:, i], color='gray', alpha=0.1)
        
    # Plot the average path in blue
    plt.plot(average_path, color='blue', label='Average Path')
    
    plt.title(f"{ticker} Monte Carlo Simulation of Stock Prices")
    plt.xlabel("Days")
    plt.ylabel("Simulated Stock Price")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    ticker = input("Enter the stock ticker (e.g., AAPL): ").upper()
    simulations = monte_carlo_simulation(ticker)
    plot_simulation(ticker, simulations)

