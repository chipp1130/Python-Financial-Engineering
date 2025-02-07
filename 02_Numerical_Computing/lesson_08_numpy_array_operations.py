# Lesson 08: NumPy Array Operations (Indexing, Slicing, Reshaping)

# 1. Understanding NumPy Indexing & Slicing

# In finance, we often deal with time series data, where we need to extract specific dates, stocks, or time periods.
# NumPy makes this easy with indexing and slicing.

# Creating a NumPy Array of Stock Prices

import numpy as np

prices = np.array([100, 102, 98, 105, 110, 107, 115]) # Stock prices over time
print(prices)

# Indexing works like Python lists:
print(prices[0]) # First stock price (100)
print(prices[-1]) # Last stock price (115)

# Slicing to get stock prices from Day 2 to Day 5
print(prices[1:5]) # [102, 98, 105, 110]

# Get every other day's price (Step Size of 2)
print(prices[::2]) # [100, 98, 110, 115]

# 2. Modifying NumPy Arrays (Updating Stock Prices)

# We can easily modify individual elements or entire sections of arrays easily.

# Updating a single stock price
prices[3] = 108 # Changing 105 to 108
print(prices)

# Bulk update (Changing the last two days' prices)
prices[-2:] = [109, 112]
print(prices) # Last two values updated

# 3. Reshaping and Multi-Dimensional Arrays:

# In finance, we often work with multiple stocks across multiple time periods, which requires reshaping data.

# Reshape a 1D array into a 2d matrix (i.e. 3 stocks over 3 days)
stock_prices = np.array([
    100, 102, 105,
    98, 101, 103,
    97, 99, 104
])

stock_prices = stock_prices.reshape(3, 3) # 3 rows (stocks) by 3 columns (days)
print(stock_prices)

# Accessing specific rows & columns
print(stock_prices[0]) # Prices of Stock 1 over 3 days
print(stock_prices[:, 1]) # Prints prices of all stocks on Day 2

# Hands-On Coding Challenges:

# Challenge 1: Extracting and Modifying Data

# Given this stock price array:
prices = np.array([150, 152, 148, 155, 160, 158, 165])
# Extract all of the prices for the last 3 days
# Increase all prices by 3% and print the updated array

print(prices[-3:])
increased_prices = prices * 1.03
print(increased_prices)

# Challenge 2: Working with Multi-Stock Data

# Given this 2D array of 3 stocks over 4 days,
stock_prices = np.array([
    [150, 152, 149, 155],   # Stock 1
    [98, 101, 99, 105],     # Stock 2
    [200, 198, 202, 210]    # Stock 3
])
# Extract Stock 2's prices
# Extract all stock prices on Day 3

print(stock_prices[1])
print(stock_prices[:, 2])