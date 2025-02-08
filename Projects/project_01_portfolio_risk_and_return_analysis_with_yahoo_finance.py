import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Project 01: Portfolio Risk and Return Analysis Using Yahoo Finance

# What You'll Learn:

# Pull real stock data from Yahoo Finance
# Calculate historical returns, expected returns, and portfolio variance
# Assess risk & volatility using the covariance matrix

# Step 1: Install & Import Required Libraries

# First, make sure you have yfinance and numpys installed.abs

# Step 2: Define Your Portfolio (Stock Selection & Weights)

# Let's assume we create a simple portfolio of 4 stocks:
# AAPL      (Apple)
# MSFT      (Microsoft)
# GOOGL     (Google)
# TSLA      (Tesla)

# Define stock tickers
stocks = ["AAPL", "MSFT", "GOOGL", "TSLA"]

# Define portfolio weights (must sum to 1.00)
weights = np.array([0.4, 0.3, 0.2, 0.1])

# Step 3: Download Stock Price Data from Yahoo Finance

# We'll get the past 1 year of adjusted closing prices for these stocks

# Download historical stock prices (Last 1 year)
data = yf.download(stocks, start="2023-01-01", end="2024-01-01")["Close"]

# This gives us a DataFrame with stock prices for each day.
# The ["Adj Close"] price is used for accurate return calculations.

# Step 4: Calculate Daily & Annualized Returns

# We need to calculate the daily percentage changes (returns) for each stock.

# Calculate daily returns
returns = data.pct_change().dropna()

# Calculate expected annualized returns (mean daily return * 252 trading days)
expected_returns = returns.mean() * 252

# Why 252? There are about 252 trading days per year, so we annualize daily returns.

# Step 5: Compute Portfolio Expected Return

# Now, we use np.dot() to calculate the expected return of the entire portfolio.

# Compute portfolio expected return
portfolio_return = np.dot(weights, expected_returns)

print(f'Expected Annualized Portfolio Return: {portfolio_return:.2f}')

# Step 6: Compute Portfolio Risk (Variance & Standard Deviation)

# We need to calculate the covariance matrix & apply the Variance formula.

# Compute covariance matrix (annualized)
cov_matrix = returns.cov() * 252

# Compute portfolio variance
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))

# Compute portfolio risk (stddev)
portfolio_stddev = np.sqrt(portfolio_variance)

print(f'Portfolio Variance: {portfolio_variance:.2%}')
print(f'Portfolio Standard Deviation (Risk): {portfolio_stddev:.2%}')

# Step 7: Plot Portfolio Performance

# Let's visualize the stock price trends over time.
plt.figure(figsize=(12,6))
data.plot()
plt.title("Stock Price Performance Over Time:")
plt.xlabel("Date:")
plt.ylabel("Stock Price: ($USD)")
plt.legend(stocks)
plt.show()

# This gives us a time-series plot of stock performance.

if portfolio_stddev <= 0.05:
    risk_level = "Very Low Risk (Bonds, Money Market)"
elif portfolio_stddev <= 0.10:
    risk_level = "Low Risk (Large-Cap Stocks, Blue-Chip)"
elif portfolio_stddev <= 0.20:
    risk_level = "Moderate Risk (Balanced Portfolios, S&P 500)"
elif portfolio_stddev <= 0.30:
    risk_level = "High Risk (Small-Caps, Emerging Markets)"
else:
    risk_level = "Very High Risk (Crypto, Venture Capital)"

print(f'Portfolio Risk Classification: {risk_level}')