import numpy as np
import pandas as pd
import yfinance as yf

# Project 02: Portfolio Risk and Return Calculator

def get_user_inputs():
    """Ask user for stock tickers, timeframe and weight allocations for each asset."""
    # Ask for tickers:
    tickers = [ticker.strip() for ticker in input("Enter stock tickers (comma-separated): ").upper().split(",")]
    # Ask for date range:
    start_date = input("Please enter the start date (YYYY-MM-DD): ")
    end_date = input("Please enter end date (YYYY-MM-DD): ")
    # Ask for portfolio weights:
    weights = []
    for ticker in tickers:
        weight = float((input(f'Enter portfolio weight for {ticker.strip()} as a decimal. (30% = 0.3, etc.) ')))
        weights.append(weight)
    if sum(weights) != 1.0:
        print("\n Error: Portfolio weights MUST sum to 1. Please check your weightings and try again.\n")
        return get_user_inputs() # Restarts input process if weights are incorrect
    return tickers, start_date, end_date, np.array(weights)

def calculate_portfolio_metrics(tickers, start_date, end_date, weights):
    """Download stock data amd compute expected risk & return metrics."""
    data = yf.download(tickers, start=start_date, end=end_date)["Close"]
    data.ffill(inplace=True) # Fills in missing data with last known price
    returns = data.pct_change(fill_method=None).dropna() # Computes daily returns, .dropna removes NaN values
    expected_returns = returns.mean() * 252
    cov_matrix = returns.cov() * 252 # Computes covariance matrix
    expected_portfolio_return = np.dot(weights, expected_returns)
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_stddev = np.sqrt(portfolio_variance)
    print('\nPortfolio Metrics: \n')
    print(f'Expected Annualized Return: {expected_portfolio_return:.6f}')
    print(f'Portfolio Variance: {portfolio_variance:.6f}')
    print(f'Portfolio Standard Deviation (Risk): {portfolio_stddev:.6f}')
    risk_free_rate = 0.02
    sharpe_ratio = (expected_portfolio_return - risk_free_rate) / portfolio_stddev
    print(f'Portfolio Sharpe Ratio (2% Rf): {sharpe_ratio:.2f}')

# Run the Portfolio Calculator
tickers, start_date, end_date, weights = get_user_inputs()
calculate_portfolio_metrics(tickers, start_date, end_date, weights)