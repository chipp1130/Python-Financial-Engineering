import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# 02.17.2025 Morning Warmup

# Lambda functions (inline anonymous functions)
# Quick one-liners where def is overkill

def square(x):
    return x ** 2

# Lambda equivalent:
square_lambda = lambda x: x ** 2

even_lambda = lambda x: x % 2 == 0

# List comprehensions (faster looping)
# instead of traditional loops, use list comprehensions for cleaner code
squared_numbers = []
for num in range(1,6):
    squared_numbers.append(num ** 2)

# List comprehension equivalent:
squared_numbers_comp = [num ** 2 for num in range(1,6)]

# Practice: Use a list comprehension to filter only even numbers from 1 to 6.
even_numbers_comp = [digit % 2 for digit in range(1,7)] # WRONG
even_numbers_comp = [digit for digit in range(1,7) if digit % 2 == 0]
print(even_numbers_comp)

# Dictionary methods (working with key-value data)
# dictionaries are essential for structuring and retrieving data efficiently

student_grades = {"Alice": 90, "Bob": 85, "Charlie": 92}

# Get a value safely (uses.get())
print(student_grades.get("Alice"))
print(student_grades.get("Bob", "N/A"))

# Iterate through dictionary keys and values
for student, grade in student_grades.items():
    print(f"{student} scored a {grade} on the test.")

# Add a new student
student_grades["David"] = 87

# Remove a student
del student_grades["Bob"]

print(student_grades)

stock_prices = {"AAPL": 110, "MSFT": 87, "META": 194, "NFLX": 231}                      # WRONG
highest_stock = 0                                                                       # WRONG
for stock, price in stock_prices.items():                                               # WRONG
    if price > 0:                                                                       # WRONG
        highest_stock = stock.upper()                                                   # WRONG
print(f"The highest stock right now is {highest_stock} with a price of ${price}.")      # WRONG

# Corrected:
highest = max(stock_prices, key=stock_prices.get)
print(highest)


# Project: Portfolio Performance Tracker
# Goal: Create a Python script that:
# Pulls stock data from Yahoo Finance
# Calculates cumulative returns & standard deviation (volatility)
# Plots performance over time for visualization

tickers = ["AAPL", "NVDA", "MSFT", "GOOGL", "NFLX", "META", "AMZN"]
weights = np.array([0.15, 0.20, 0.1, 0.1, 0.15, 0.2, 0.1])

# Download Data
data = yf.download(tickers, start="2020-01-01", end="2024-01-01")["Close"]
data.ffill(inplace=True)

# Compute Daily Returns
returns = data.pct_change().dropna()

# Correct Covariance Matrix Calculation
cov_matrix = returns.cov() * 252  

# Compute Portfolio Variance & Standard Deviation
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
portfolio_standard_deviation = np.sqrt(portfolio_variance)

print(f"Portfolio Variance: {portfolio_variance * 100:.2f}%")
print(f"Portfolio Standard Deviation: {portfolio_standard_deviation * 100:.2f}%")