# Week 2: Data Structures in Python

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
