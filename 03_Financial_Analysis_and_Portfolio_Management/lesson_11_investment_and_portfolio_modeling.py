import pandas as pd
import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Lesson 11: Investment & Portfolio Modeling -- Portfolio Risk & Return Metrics

# Step 1: Setup and Data Import

# Import necessary libraries
# Download stock data from Yahoo! Finance
# Calculate both arithmetic & log returns

# define tickers & time range
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]
start_date = "2023-01-01"
end_date = "2024-01-01"

# Download historical stock prices
data = yf.download(tickers, start=start_date, end=end_date)["Close"]

# Calculate arithmetic returns
simple_returns = data.pct_change().dropna()

# Calculate log returns
log_returns = np.log(data / data.shift(1)).dropna()

# Print first five rows
print("Simple Returns:\n",simple_returns.head())
print("Log Returns:\n",log_returns.head())

# Step 2: Compute Portfolio Data

# Portfolios are weighted, meaning each asset contributes based on its allocation.
# Formula: Portfolio Return = (Weight 1 * Asset 1 Return) + (Weight 2 * Asset 2 Return) + ... + (Weight n * Asset n Return)

# Ask user for portfolio weights

weights = []  # Empty list to store weights
for ticker in tickers:
    try:
        weight = float(input(f"What is the weight of {ticker} in your portfolio? (Enter as a decimal, e.g., 0.30 for 30%)\n").strip())
        weights.append(weight)  # Append weight to list
    except ValueError:
        print("Invalid input! Please enter numbers as decimals (e.g., 0.30).")

# Convert to NumPy array
weights = np.array(weights)

# Ensure weights sum to 1.00
if not np.isclose(weights.sum(), 1.0):
    print("\nError: Portfolio weights MUST sum to 1.00! Please restart and enter valid weights.\n")
else:
    print("\nPortfolio weights accepted:", weights)

# Compute portfolio returns
portfolio_simple_return = np.dot(simple_returns, weights)
portfolio_log_return = np.dot(log_returns, weights)

# Step 3: Annualized Portfolio Return

# Since stock markets trade ~252 times a year, we annualize daily returns
annualized_simple_return = portfolio_simple_return.mean() * 252
annualized_log_return = portfolio_log_return.mean() * 252

print(f"\nAnnualized Portfolio Simple Return: {annualized_simple_return:.2%}")
print(f"Annualized Portfolio Log Return: {annualized_log_return:.2%}")

# Step 4: Visualizing Portfolio Growth

# Let's plot how the portfolio performs over time.
# We assume $10,000 was invested initially.

# Portfolio cumulative growth
initial_value = 10000
cumulative_simple = (1 + portfolio_simple_return).cumprod() * initial_value
cumulative_log = np.exp(portfolio_log_return.cumsum()) * initial_value

# Plot
plt.figure(figsize=(12,6))
plt.plot(cumulative_simple, label = "Portfolio (Simple Returns)")
plt.plot(cumulative_log, label="Portfolio (Log Returns)", linestyle="dashed")
plt.xlabel("Date")
plt.ylabel("Portfolio Value ($USD)")
plt.title("Portfolio Growth Over Time")
plt.legend()
plt.show()