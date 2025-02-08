import numpy as np

# Supplementary NumPy Indexing & Slicing Guide:

# How to Select Data in a 2D NumPy Array (Matrix Format)

# Format: array[row, column]

# Single Value: array[1, 2] --> Selects the element at row index 1, column index 2.
# Entire Row: array[1] --> Selects all columns in row index 1.
# Entire Column: array[:, 2] --> Selects all rows in column index 2.

# 1. Extracting a Single Value

# Example: Given this matrix:

stock_prices = np.array([
#     0    1    2    3
    [150, 152, 149, 155],   # Stock 1 (Row 0)
    [98, 101, 99, 105],     # Stock 2 (Row 1)
    [200, 198, 202, 210]    # Stock 3 (Row 2)
])

# How to Select a Specific Value? [Row, Column]
print(stock_prices[0, 2]) # Prints 149 (Stock 1, Day 3)
print(stock_prices[2, 1]) # Prints 198 (Stock 3, Day 1)
# Remember to use a comma!

# 2. Extracting a Full Row

# How to Select All Columns for a Specific Stock?
print(stock_prices[1]) # Prints [98, 101, 99, 105] Row 1 (Stock 2)
print(stock_prices[0]) # Prints [150, 152, 149, 155] Row 0 (Stock 1)

# Shortcut: array[row] = array[row, :]
print(stock_prices[1, :]) # Also all of Stock 2's prices, in different notation

# : means "select all columns."

# 3. Extracting a Full Column

# How to Select All Stocks for a Specific Day?
print(stock_prices[:, 2]) # All prices on Day 3 --> [149, 99, 202]
print(stock_prices[:, 0]) # All prices on Day 1 --> [150, 98, 200]

# : in the row means "selects all rows."

# 4. Extracting a Range (Slicing)

# How to Select Stock 1 & Stock 2 Only?
print(stock_prices[0:2, :])
# [0:2, :] selects rows 0 and 1 (excludes row 2)

# How to Select Day 2 & Day 3 Only?
print(stock_prices[:, 1:3])
# [:, 1:3] selects columns 1 and 2 (excludes column 3).

# 5. Modifying Values in a Matrix

# Increase Only Stock 3's Day 3 Price by 5%
stock_prices[2, 2] *= 1.05
print(stock_prices)

# Increase All Prices for Day 4 by 2%
stock_prices = stock_prices.astype(float)
stock_prices[:, 3] *= 1.02
print(stock_prices)

# Set Stock 1's Entire Price History to 200
stock_prices[0, :] = 200
print(stock_prices)

# Quick Overview:

# Operation:                    Syntax:                         Example:

# Select Single Value           array[row, col]                 stock_prices[1, 2] --> 99
# Select Full Row               array[row]                      stock_prices[1] --> [99, 101, 99, 105]
# Select Full Column            array[:, col]                   stock_prices[:, 2] --> [149, 99, 202]
# Slice Multiple Rows           array[start:end, :]             stock_prices[0:2, :] --> [Rows 0 & 1]
# Slice Multiple Columns        array[:, start:end]             stock_prices[:, 1:3] --> [Cols 1 and 2]
# Modify Value                  array[row, col] = new_value     stock_prices[2, 2] *= 1.05
# Modify Entire Row             array[row, :] = new_values      stock_prices[2, :] = 200
# Modify Entire Column          array[:, col] = new_values      stock_prices[:, 3] *= 1.10

