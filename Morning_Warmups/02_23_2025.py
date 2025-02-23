import pandas as pd
import numpy as np
import yfinance as yf

# Lambda Functions:
square = lambda x: x ** 2
print(square(4))

even = lambda x: x % 2 == 0
print(even(3))

absolute = lambda x: abs(x)
print(absolute(-21))

polarity = lambda x: print("Positive") if x > 0 else print("Negative")
polarity(-4)

three_div = lambda x: x % 3 == 0
print(three_div(15))

even_range = filter(lambda x: x % 2 ==0, range(1,11))
print(list(even_range))

# NumPy

zeroes_array = np.array([0] * 10)
ones_array = np.array([1] * 10)
print(zeroes_array)
print(ones_array)

twos = ones_array * 2
print(np.dot(twos, ones_array))

print(np.mean(ones_array))

# Daily Challenge: Portfolio Variance Calculation

cov_matrix = np.array([
    [0.04, 0.02, 0.01], 
    [0.02, 0.05, 0.03], 
    [0.01, 0.03, 0.06]
])

weights = np.array([0.4, 0.3, 0.3])
expected_returns = np.array([0.12, 0.15, 0.18])
risk_free_rate = 0.02

portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
portfolio_stdeviation = np.sqrt(portfolio_variance)
expected_return = np.dot(weights, expected_returns)
sharpe_ratio = (expected_return - risk_free_rate)/portfolio_stdeviation

print(f"Portfolio Variance: {portfolio_variance * 100:.3f}%")
print(f"Portfolio Standard Deviation: {portfolio_stdeviation * 100:.3f}%")
print(f"Portfolio Sharpe Ratio: {sharpe_ratio:.4f}")