import numpy as np
import pandas as pd
import yfinance as yf

# 02.18.2025 Morning Warmups

# Lambda functions
def square(x):
    return x ** 2
square_lambda = lambda x: x ** 2
print(square_lambda(5))

# Practice: Write a Lambda function that checks if a number is divisible by 3
triplet_lambda = lambda x: x % 3 == 0
print(triplet_lambda(4))

# List comprehensions
squared_numbers = []
for num in range(1,6):
    squared_numbers.append(num ** 2)

squared_numbers_comp = [num ** 2 for num in range(1,6)]
print(squared_numbers_comp)

# Practice: Use a list comprehension to create a list of even numbers from 1 to 10.
even_numbers = [num for num in range(1,11) if num % 2 == 0]
print(even_numbers)

# Dictionary Methods (Key-Value Data Structures)
stock_prices = {            # DONT FORGET COMMAS AFTER ENTRIES
    "AAPL": 175,
    "MSFT": 315,
    "NVDA": 500
}
print(stock_prices.get("AAPL"))
print(stock_prices.get("TSLA", "Not Found"))

stock_prices["TSLA"] = 230      # Adds a new entry with BRACKETS

del stock_prices["NVDA"]        # Deletes entry

for stock, price in stock_prices.items():   # Cycles through key-value pairs using .ITEMS()
    print(f"{stock}: ${price}")

# Practice: Create a dictionary where keys are stock tickers and values are their current prices. Then, add a new stock and delete one.
new_stock_prices = {
    "AMZN": 205,
    "AMD": 234,
    "META": 172
}
new_stock_prices["GOOGL"] = 263
del new_stock_prices["META"]

for new_stock, new_price in new_stock_prices.items():
    print(f"{new_stock}: ${new_price:.2f}")

# Daily project: Portfolio Beta Calculator

def get_user_input():
    stock = input("Hello! What stock would you like to compute the beta for? Please enter the ticker only: ").strip().upper()
    start_date = "2000-01-01"
    end_date = "2025-01-01"
    return stock, start_date, end_date

def beta(stock, start_date, end_date):
    data = yf.download(stock, start=start_date, end=end_date)["Close"]
    market = yf.download("^GSPC", start=start_date, end=end_date)["Close"]

    # Print data to check if Yahoo returned values
    print(f"Stock Data ({stock}):\n", data.head(), "\n")
    print(f"Market Data (^GSPC):\n", market.head(), "\n")

    # Forward-fill missing values
    data.ffill(inplace=True)
    market.ffill(inplace=True)

    stock_returns = data.pct_change().dropna()
    market_returns = market.pct_change().dropna()

    # Print returns to debug
    print(f"Stock Returns ({stock}):\n", stock_returns.head(), "\n")
    print(f"Market Returns (^GSPC):\n", market_returns.head(), "\n")

    # Check if returns are too small
    if len(stock_returns) < 2 or len(market_returns) < 2:
        print("Not enough data to compute Beta. Try another stock or increase the time range.")
        return

    # Extract correct covariance value
    covariance = np.cov(stock_returns, market_returns)[0, 1]
    market_var = market_returns.var()

    beta_value = covariance / market_var
    print(f"Beta for {stock}: {beta_value:.2f}")

stock, start_date, end_date = get_user_input()
beta(stock, start_date, end_date)
