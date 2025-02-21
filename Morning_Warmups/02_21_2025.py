import numpy as np
import pandas as pd
import yfinance as yf

# 02.21.25

# Lists.
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.pop(0)      # Indexes
print(my_list[::-1])
evens = [num for num in my_list if num % 2 == 0]
print(evens)
maximum = max(my_list)
print(maximum)
minimum = min(my_list)
print(minimum)

# Lambda Functions.
cubes = lambda x: x ** 3
print(cubes(-2))     # Output: -8

# List Comprehension
odds = [num for num in range(1,11) if num % 2 == 1]
print(odds)

# NumPy Basics
my_array = np.array([1, 2])
print(my_array * 2)
second_array = np.array([9, 8])
dot = np.dot(my_array, second_array)
print(dot)
mean = np.mean(my_list)
print(mean)
standard = np.std(my_list)
print(standard)

# Challenge: Portfolio Risk Calculation with NumPy
# Task: Implement a function to compute portfolio variance using a covariance matrix and asset weights in NumPy.

weights = np.array([0.4, 0.6])  # Portfolio weights for two assets
cov_matrix = np.array([[0.0225, 0.018],[0.018, 0.04]])

p_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
p_stddev = np.sqrt(p_variance)
print(f"Portfolio Variance: {p_variance * 100:.3f}%")
print(f"Portfolio Standard Deviation: {p_stddev * 100:.3f}%")