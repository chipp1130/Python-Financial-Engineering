import numpy as np
import pandas as pd
import yfinance as yf

# 02.19.2025

# Lambda functions
square = lambda x: x ** 2
print(square(2))    # Output: 4

# practice: Write a lambda function to check if a number is divisible by 5.
div_five = lambda x: x % 5 == 0
print(div_five(5))

# List comprehensions
squared_numbers = [num ** 2 for num in range(1,6)]
print(squared_numbers)                              # Output: [1, 4, 9, 16, 25]

# Practice: Write a list comprehension that extracts odd numbers from 1 to 10
odd_numbers = [num for num in range(1, 11) if num % 2 == 1]
print(odd_numbers)

# Dictionary Methods:
stock_prices = {
    "AAPL": 175,
    "MSFT": 315,
    "NVDA": 500
}
print(stock_prices.get("AAPL"))
print(stock_prices.get("TSLA", "Not Found"))

# Practice: Write a dictionary where keys are stock tickers and the values are current prices. Then add a new stock, delete one stock, print all items
tickers = {
    "TSLA": 110,
    "AMZN": 236,
    "AMD": 94,
    "T": 31
}
tickers["KO"] = 62
del tickers["T"]
for ticker, price in tickers.items():
    print(f"Company ({ticker}): ${price}")

# Morning Challenge:
# Goal: Build a simple stock performance tracker that:
# Asks the user to input stock tickers
# Fetches historical stock prices from Yahoo Finance
# Calculates the cumulative return over a user-defined period
# Prints out which stock performed best

def get_user_input():
    tickers = [ticker.upper() for ticker in input("Please input the tickers you want to track, separated by commas.\n").strip().split(",")]
    start_date = input("Please enter the start date in format YYYY-MM-DD:\n")
    end_date = input("Please enter the end date in format YYYY-MM-DD:\n")
    return tickers, start_date, end_date

def performance_tracker(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)["Close"]
    data.ffill(inplace=True)
    cumulative_returns = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    best_stock = cumulative_returns.idxmax()
    best_return = cumulative_returns.max()
    print("\nCumulative Returns (%):")
    print(cumulative_returns)
    print(f"\nBest performing stock: {best_stock} with {best_return:.2f}% return!")

tickers, start_date, end_date = get_user_input()
performance_tracker(tickers, start_date, end_date)