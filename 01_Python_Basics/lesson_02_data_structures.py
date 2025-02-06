# Lesson 02: Data Structures in Python

# Introductory Reading: Lists, Tuples, and Dictionaries

# Lists (Ordered, Mutable Sequences)
# Lists are ordered collections that allow duplicates and can be modified.
# Defined using square brackets [].

stocks = ["AAPL", "TSLA", "MSFT", "AMZN"]
print(stocks[0])
# Lists are indexed (first item is stocks[0])

# Modifying Lists

stocks.append("NVDA")  # Adds NVDA to stocks
stocks.remove("TSLA")  # removes TSLA from the list
# Modifies the item in the list indexed at 1 (MSFT after line 14's alteration)
stocks[1] = "GOOGL"
print(stocks)

# Tuples (Ordered, Immutable Sequences)
# Tuples are like lists, but they are immutable in that they cannot be altered after creation.
# Defined using parentheses ().

stock_prices = ("AAPL", "KO", "BX")
print(stock_prices[0])

# Tuples are used when data should not be modified, such as historical prices.

# Dictionaries (Key-Value Pairs)
# Dictionaries are used to store mapped relationships (i.e. stock tickers ➡️ number of shares).
# Defined using curly brackets {}.

portfolio_prices = {
    "AAPL": 130.18,
    "KO": 18.72,
    "BX": 235.47
}
# If stock isn't found, returns error message.
print(portfolio_prices.get("KO", "Stock not found"))

# Dictionaries are faster than lists for lookup operations.

# Modifying a Dictionary:
portfolio_prices["GOOGL"] = 143.29  # Adds new entry to the dictionary.
portfolio_prices["KO"] = 19.35  # Updates the price of "KO".
del portfolio_prices["BX"]  # Deletes "BX" from the dictionary.

# Experiential Coding & Lessons:

# Exercise 1: Creating & Modifying Lists

# Task:

# Create a list of five stock tickers.
# Print the first and last stock.
# Add a new stock, remove one, and modify another.

tickers = ["NFLX", "XLP", "XLK", "XLM", "SPY"]
print(tickers[0])
print(tickers[-1])

tickers.append("VOO")
tickers.remove("XLP")
print(tickers)


# Exercise 2: Using Tuples for Immutable Data

# Task:

# Create a tuple storing stock prices (ticker, price).
# Print the price of the second stock.
# Try modifying a value (expect an error).

stock_tuple = ("AAPL", 112.50, "BX", 235.13, "CVS", 73.96)
print(stock_tuple[3])
# stock_tuple["BX"] = "AMZN"

# Exercise 3: Using Dictionaries for a Portfolio

# Task:

# Create a dictionary mapping tickers to share counts.
# Print the total shares of a specific stock.
# Add a new stock and remove one.
# Use a loop to print all holdings.

stock_portfolio = {
    "AAPL": 1000,
    "AMZN": 350,
    "BX": 40,
    "CVS": 300
}
print(stock_portfolio.get("AAPL", "Stock not found"))
del stock_portfolio["AMZN"]
stock_portfolio["XRP"] = 341.93
for tickers, shares in stock_portfolio.items():
    print(f"You own {shares} shares of {tickers}.")

# You must use .items() to access both keys (tickers) and values (shares).

# Recap & Reflection:

# What did you find easy?
# Today, I found the syntax and indenting more natural as I get used to Python.

# Where did you struggle?
# I am getting used to all the nested functions like string(input("")) vs. the .extensions like in stock_portfolio.items().
# I also need to get better at being meticulous with the punctuation like commas and underscores.

# What do you want to reinforce tomorrow?
# I want to further build on my ability to nest functions within each other, as well as becoming even more comfortable with f-strings and the syntax.
