# Lesson 3: Nesting Functions & Advanced f-Strings

# Goal: Learn how to nest functions inside each other, understand scope, and master f-string formatting for dynamic financial calculations.

# 1. Introductory Reading: Nested Functions and F-Strings

# What is a Nested Function?
# A nested function is a function inside another function.
# It is used for modularity, encapsulation, and code organization.

def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()  # Calling inner function inside the outer function.


outer_function()

# Output:
# This is the outer function.
# This is the inner function.

# Why use nested functions?
# They keep related logic together.
# The inner function can only be called within the outer function.
# They are useful in financial calculations to break down complex formulas.

# Understanding Function Scope (Local vs. Global Variables)
# Global Variable: Defined outside a function, accessible everywhere.
# Local Variable: Defined inside a function, and is accessible only in that function.

investment = 5000  # Global variable


def calculate_growth():
    rate = 0.05  # Local variable
    return investment * (1 + rate)  # Uses the global variable


print(calculate_growth())  # Works because "investment" is global
# print(rate()) # Fails because "rate" is local to the function

# Key Rule: A function cannot access local variables from another function.

# f-Strings: Advanced Formatting
# f-Strings allow clean formatting of financial data.

# Formatting Numbers:
amount = 1234.5678
print(f"Formatted Amount: ${amount:.2f}")  # Rounds "amount" to 2 decimals

# Adding Commas for Readability:
total_value = 2500000
print(f"Your account currently has ${
      total_value:,} present.")  # Output: $2,500,000

# Aligning Text for Reports:
print(f"{'Stock:':<10} {'Price:':>10}")
print(f"{'AAPL':<10} {150.25:>10.2f}")

# 2. Experiential Coding & Lessons

# Exercise 1: Create a Nested Function for Invested Growth
# Define a function investment_growth (initial, years, rate).
# Inside it, define calculate_future_value() that only works inside the main function.
# Use it to return future investment value.


def investment_growth(initial, years, rate):    # Defines parameters
    def calculate_future_growth():              # Creates inner function
        return initial * ((1 + rate) ** years)  # Uses parameters

    return calculate_future_growth()            # Calling inner function


print(f"Your investment is now worth ${investment_growth(100, 1, 0.05):,.2f}.\n")

# Exercise 2: Format Output with f-Strings
# Print results with 2 decimal places and comma separators.
# Print a financial report with text alignment.

results = 104110.3234
print(f"{results:,.2f}\n")

print(f"{'Stock:':<10} {'Price:':>10}")
print(f"{'CVS':<10} {130.24:>10.2f}")
print(f"{'XLM':<10} {214.74:>10.2f}\n")

# Exercise 3+: Create a Nested Function for Compounded Growth
# Write a function compound_growth(principal, rate, years).
# Inside it, create a nested function calculate_future_value() that:
# Uses the formula: FV = P * (1 + r)^t
# Returns the future value.
# Call the inner function inside the outer function.
# Return the final investment value rounded to two decimal places.

principal = 10000
growth_rate = 0.07
time_in_years = 30

def function_compound_growth(principal, growth_rate, time_in_years):
    def compound_growth_calculator():
        return principal * ((1 + growth_rate) ** time_in_years)
    
    return round(compound_growth_calculator(), 2)

print(f"Your initial investment of ${principal:,.2f} will be equal to ${function_compound_growth(10000, .07, 30):,} after {time_in_years} years.")