import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Lesson 10: Introduction to Pandas for Financial Data

# Why Pandas?

# Essential for handling large financial datasets (stocks, bonds, crypto, etc).
# Used in quant finance, backtesting, risk modeling, and trading algorithms.
# Works seamlessly with NumPy to enable powerful data analysis.

# 1. Creating & Manipulating Pandas DataFrames

# Step 1: Import Pandas & Create a Sample DataFrame

# Sample stock data
data = {
    "Date": ["2024-02-01", "2024-02-02", "2024-02-03"],
    "AAPL": [180, 182, 185],
    "MSFT": [370, 374, 380],
    "TSLA": [180, 178, 182]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert "Date" column to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Set "Date" as the index (important for time-series data)
df.set_index("Date", inplace=True)

print(df)

print("\n")

# Key Takeaways:
# Pandas uses DataFrames (like Excel tables, but in Python).
# Setting Date as the index is crucial for time-series analysis.

# 2. Loading Real Stock Data Using Yahoo! Finance

# Step 2. Download Financial Data Using Pandas & yFinance

# Define tickers & download last 3 months of data
tickers = ["AAPL", "MSFT", "TSLA"]
data = yf.download(tickers, start="2023-11-01", end="2024-02-01")["Close"]

# Print the first few rows
print(data.head())
print("\n")

# Key Takeaways:
# yf.download() grabs real market data and loads it into a Pandas DataFrame.
# ["Close"] ensures we use adjusted closing prices (accounts for dividends and splits).

# 3. Basic DataFrame Operations (Filtering, Slicing, Statistics)

# Step 3. Inspect and Clean Financial Data

# View the first 5 rows
# print(data.head())

# Check for missing values
print(data.isnull().sum())

# Fill missing values with the previous day's price
data.ffill(inplace=True)  # Correct way to forward-fill

print("\n")

# Key Takeaways:
# head() shows the first few rows
# isnull().sum() checks for missing data (common in stock datasets)
# fillna(method="ffill") carries forward previous values (fixing missing data).

# 4. Calculating Returns & Rolling Averages

# Step 4. Compute Daily Returns & Moving Averages

# Calculate daily percentage change (returns)
returns = data.pct_change()

# Calculate 7-day moving average
rolling_average = data.rolling(window=7).mean()

# Display results
print(returns.head())
print(rolling_average.head())

# Key Takeaways:
# pct.change() computes daily returns for each stock.
# .rolling(window=7).mean calculates a 7-day moving average (smooths out price fluctuations).

# 5. Visualizing Stock Trends Using Matplotlib

# Step 5. Plot Stock Prices Over Time

# Plot stock prices
data.plot(figsize=(12,6))
plt.title("Stock Price Trends")
plt.xlabel("Date:")
plt.ylabel("Price: (in $USD)")
plt.legend(tickers)
plt.show()

# Key Takeaways:
# Pandas integrates directly with MatPlotLib for fast financial visualizations.
# Time-series plots are critical for analyzing market trends.

# Hands-On Challenges (Your Turn!)

# Challenge 1: Extract and Analyze Specific Stock Data

# Load 6 months of AAPL & MSFT stock data from Yahoo Finance.
# Compute & print:
#   Mean price for each stock.
#   Standard deviation (volatility) for each stock.
#   Rolling 14-day moving average.

