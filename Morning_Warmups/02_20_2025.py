import numpy as np
import pandas as pd
import yfinance as yf

# 02.20.2025 Rudiments

# 1. Lists:
num_list = [1, 2, 3, 4, 5]
num_list.append(6)
num_list.remove(1)      # Output: 2, 3, 4, 5, 6
print(num_list[0])
print(num_list[-1])
print(num_list[0:2])    # Prints first 3 elements
print(num_list[::-1])   # Reverses list
for num in num_list:
    print(num)
num_comp = [num for num in num_list if num % 2 == 0]    # List comp that prints only even digits
print(num_comp)

sorted_nums = sorted(num_list)
print(sorted_nums)
print(sorted_nums[0])   # Prints minimum
print(sorted_nums[-1])   # Prints maximum

# 2. Tuples:
my_tuple = (1, 2, 3)       # TUPLES USE PARENTHESES
print(tuple[0:-1])      # Prints all elements in tuple
listuple = list(my_tuple)   # Converts tuple into list
listuple.append(4)
my_tuple = tuple(listuple)
print(my_tuple)

# 3. Lambda Functions:
squared = lambda x: x ** 2
print(squared(3))       # Outcome: 9
even = lambda x: x % 2 == 0
print(even(3))          # Outcome: False
absval = lambda x: 0 - x * (-1)**x
print(absval(3))
posnegval = lambda x: print("Positive") if x > 0 else print("Negative")
posnegval(2)

# 4. List Comprehensions:
num_square = [num ** 2 for num in range(1,11)]
print(num_square)
odd_nums = [num for num in range(0,21) if num % 2 == 1]
print(odd_nums)
tfalsefodd = {num: num % 2 == 0 for num in range(0,11)}
print(tfalsefodd)
titles = ["ConnorPython", "ChatGPT", "OpenAI", "Cat"]
longtitle = [title for title in titles if len(title) > 5]
print(longtitle)
sevenmultiples = [num * 7 for num in range(1,11)]
print(sevenmultiples)
square_dictionary = {
    num: num ** 2 for num in range(1,11)
}
print(square_dictionary)

# 5. Dictionary Methods:
stockprices = {
    "AAPL": 130,
    "BX": 309,
    "CVS": 63
}
print(stockprices.get("CVS", "Not Applicable"))
stockprices["DAL"] = 34
del stockprices["DAL"]
for keys, values in stockprices.items():
    print(f"{keys} cost ${values}")
highest_stock = max(stockprices, key=stockprices.get())

# Daily Challenge:
# Objective:
# You're going to simulate a simple stock portfolio by:
# Allowing the user to "buy" and "sell" stocks
# Tracking their holdings and cash balance
# Displaying the final portfolio value

def get_user_input():
    tickers = [ticker.upper for ticker in input("What stocks would you like to analyze (comma-separated)?\n").strip().split()]
    latest_prices = yf.download(tickers)
    print(latest_prices)