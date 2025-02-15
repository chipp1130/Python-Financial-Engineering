import numpy as np
import pandas as pd
import yfinance as yf

# 02_15_2025: Covariance Matrix & Portfolio Risk Analysis

# Challenge Overview:
# ✅ Download stock data (manually input returns or use yfinance)
# ✅ Compute the covariance matrix for multiple assets
# ✅ Calculate portfolio variance & standard deviation using matrix operations

def user_inputs():
    tickers = [ticker.strip() for ticker in input("What stocks do you want to analyze? Please separate with commas.\n").upper().split(",")]
    start_date = input("Please enter the first date for the analysis in YYYY-MM-DD.\n")
    end_date = input("Please enter the last date for the analysis in YYYY-MM-DD.\n")
    weights = []
    try:
        for ticker in tickers:
            weight = float(input(f"What is the weight of {ticker} in your portfolio? Please enter percentages as decimals.\n"))
            weights.append(weight)
    except ValueError:
        print("Please enter valid decimal entries in order to get accurate results.")
        return
    if not np.isclose(sum(weights), 1.00, atol=1e-4):
        print("Please make sure your weights add up to 1.00!")
        return
    return tickers, start_date, end_date, pd.array(weights)

def risk_analysis(tickers, start_date, end_date, weights):
    data = yf.download(tickers, start=start_date, end=end_date)["Close"]
    if data.empty:
        print("Error: No data retrieved. Check tickers and date range.")
        return
    data.ffill(inplace=True)
    returns = data.pct_change().dropna()
    cov_matrix = returns.cov() * 252
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_stddev = np.sqrt(portfolio_variance)

    print(f'Portfolio Variance: {portfolio_variance:.2%}')
    print(f'Portfolio Standard Deviation (Risk): {portfolio_stddev:.2%}')

tickers, start_date, end_date, weights = user_inputs()
risk_analysis(tickers, start_date, end_date, weights)