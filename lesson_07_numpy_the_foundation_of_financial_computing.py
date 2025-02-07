import numpy as np

# Lesson 07: NumPy -- The Foundation of Financial Computing

# Numerical Python- NumPy- is the core library for numerical computing in Python.

# Financial Engineers use it because:

# It is MUCH faster than Python Lists for math-heavy calculations.
# It supports vectorized operations, making code cleaner and more efficient.
# It handles large datasets, which is essential for portfolio optimization, risk modeling, and Monte-Carlo simulations.

# 1. Creating NumPy Arrays:

# Before we get into financial applications, let's first understand NumPy arrays:

# Importing NumPy:
# import numpy as np

# Creating a Simple NumPy Array
prices = np.array([100, 102, 98, 105]) # Stock prices
print(prices)
print(type(prices)) # class 'numpy.ndarray

# Why NumPy Arrays?
# They are faster than Python Lists
# They support mathematical operations directly

# Comparing NumPy Arrays vs. Python Lists:

prices_list = [100, 102, 98, 105]
prices_array = np.array([100, 102, 98, 105])

# Multiplying a Python List by 2 (unexpected result)
print(prices_list * 2) # [100, 102, 98, 105, 100, 102, 98, 105]

# Multiplying a NumPy array by 2 (correct result)
print(prices_array * 2) # [200 204 196 210]

# Takeaway: NumPy automatically applies math operations to all elements (vectorization), unlike lists!

# 2. Basic NumPy Operations:

# Once we have an array, we can perform fast calculations like:

# Element-wise arithmetic:
returns = prices_array / 100 # Normalizing stock prices
print(returns)

# Mean, Max, Min (Basic Statistics):
print("Mean Price: ", np.mean(prices_array))
print("Mean Price: ", np.max(prices_array))
print("Mean Price: ", np.min(prices_array))

# Generating Arrays Automatically:

# Creates an array from 0 to 9
arr = np.arange(10) # Index starts at 0 like usual
print(arr)

# Creates an array of 5 zeros
zeros = np.zeros(5)
print(zeros)

# Creates an array of 5 ones
ones = np.ones(5)
print(ones)

# These are useful when generating synthetic financial data.

# 3. Hands-On Coding Challenges:

# Let's test your understanding!

# Challenge 1: Create and Modify NumPy Arrays
# 1. Create a NumPy array of stock prices: [150, 152, 148, 155, 160]
# 2. Multiply all prices by 1.02 to simulate a 2% increase
# 3. Print the updated prices

stock_prices = [150, 152, 148, 155, 160]
stock_prices_array = np.array([150, 152, 148, 155, 160]) # Step 1 Completed

increased_array = stock_prices_array * 1.02 # Step 2 Completed
print(increased_array) # Step 3 Completed

# Challenge 2: Compute Basic Statistics
# Given this stock price array:
prices = np.array([110, 115, 120, 125, 130])
# Compute and print:
# 1. The mean stock price
# 2. The highest stock price
# 3. The lowest stock price

mean_price = np.mean(prices)
min_price = np.min(prices)
max_price = np.max(prices)

print(f"Average Stock Price: ${mean_price:.2f}")
print(f"Lowest Stock Price: ${min_price:.2f}")
print(f"Highest Stock Price: ${max_price:.2f}")