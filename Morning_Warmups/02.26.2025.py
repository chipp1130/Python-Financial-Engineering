import numpy as np
import pandas as pd
import yfinance as yf

# 02.26.2025 Morning Practice

evens = [num for num in range(1,21) if num % 2 == 0]
print(evens)

last_char = lambda x: x[-1]
print(last_char("Connor"))
print("")

random_array = np.random.randint(1, 101, size=10)

# stocks = pd.DataFrame({
#     "Stock": ["AAPL", "GOOGL", "MSFT", "TSLA"],
#     "Price": np.random.randint(100, 501, size=4)
#     })
# print(stocks)

# Challenge:

import numpy as np
import pandas as pd

portfolio = pd.DataFrame({
    "Stock": ["AAPL", "GOOGL", "TSLA"],
    "Shares": [10, 5, 8],
    "Price": np.random.randint(100, 501, size=3),
    "Daily Return": np.random.uniform(-0.05, 0.05, size=3)
})

portfolio["Value"] = portfolio["Shares"] * portfolio["Price"]
total_value = portfolio["Value"].sum()

portfolio["Weight"] = portfolio["Value"] / total_value
portfolio["Weighted Return"] = portfolio["Weight"] * portfolio["Daily Return"]

for _, row in portfolio.iterrows():
    print(f"Value of {row['Stock']}: ${row['Value']:.2f}")
    print(f"Weight of {row['Stock']}: {row['Weight'] * 100:.2f}%")
    print(f"Weighted Contribution to Return: {row['Weighted Return'] * 100:.2f}%\n")

print(f"Total Portfolio Value: ${total_value:.2f}")
print(f"Weighted Average Return: {portfolio['Weighted Return'].sum() * 100:.2f}%")