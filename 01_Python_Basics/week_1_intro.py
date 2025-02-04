# Week 1, Lesson 1: Python Basics
print("Hello World!\n")

# Exercise 1: Print Statements and Variables

# Task:

# Print "Hello, Financial Engineering!" to the screen.
# Create a variable called investment and assign it a value of 1000 (representing $1,000).
# Print "Initial Investment: $" followed by the investment value.

investment = 3000
print(f"Initial investment amount: ${investment:.2f} USD.\n")

# Exercise 2: Data Types and Simple Calculations

# Task:

# Create three variables representing the number of shares you own for three stocks (e.g., Apple, Tesla, Amazon).
# Assign stock prices for each company.
# Calculate the total portfolio value and print it.

# number of shares owned
shares_nvda = 1000
shares_msft = 230
shares_nok = 400

# stock prices (hypothetical)
price_nvda = 118.75
price_msft = 412.25
price_nok = 4.50

total_portfolio_value = shares_nvda * price_nvda + \
    shares_msft * price_msft + shares_nok * price_nok

print(f"Total portfolio value: ${total_portfolio_value:.2f} USD.")


# Exercise 3: Using Input

# Task:

# Ask the user how much money they want to invest.
# Convert the input into an integer or float.
# Print a confirmation message.

while True:  # this function will keep asking for input until a valid number is entered
    try:  # this will try to convert the input into a float
        investing_capital = float(
            input("How much money would you like to invest?\n"))
        if investing_capital <= 0:
            print("Your investment must be positive. Please try again.\n")
            continue
        break  # this exits the loop if the input is valid (positive number)
    except ValueError:  # this will catch any errors if the input is not a number
        print("Invalid input. Please enter a numerical input.\n")
confirmation = f"You have chosen to invest ${investing_capital:.2f} USD.\n"
print(confirmation)

# Exercise 4: String Manipulation

# Task:

# Create a variable stock_ticker and assign it a stock symbol (e.g., "AAPL").
# Convert the ticker symbol to lowercase.
# Print "Stock selected: aapl" (in lowercase).

# Exercise 5: Lists & Dictionaries

# Task:

# Create a list of three stock symbols.
# Create a dictionary that maps each symbol to the number of shares owned.
# Print the holdings using a loop.

# Exercise 6: Simple Conditional Logic

# Task:

# Ask the user for the price of AAPL stock.
# If the price is above $180, print "AAPL is expensive!".
# Otherwise, print "AAPL is at a reasonable price.".

# Exercise 7: Investment Growth Calculation

# Task:

# Assume an initial investment and a growth rate (e.g., 5%).
# Calculate the investment value after 1 year.
# Print the result.
