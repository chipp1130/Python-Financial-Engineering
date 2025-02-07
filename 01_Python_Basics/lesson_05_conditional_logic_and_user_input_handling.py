# Lesson 05: Conditional Logic & User Input Handling

# 1. Concept Breakdown:
# if, elif, and else Statements

# Conditional statements allow a program to make decisions.
x = 10

if x > 5:
    print("x is greater than 5.")
elif x == 5:
    print("x is equal to 5.")
else:
    print("x is less than 5.")

# Python checks each condition in order and stops when one is True.

# Quick Example: Trading Decision
price = 105

if price > 100:
    print("Sell the stock!")
elif price < 90:
    print("Buy the stock!")
else:
    print("Hold the stock.")

# What happens if price = 95?
# "Hold the stock." is returned.

# Boolean Logic (and, or, not)
# You can combine multiple conditions using "and", "or", and "not".

# "and" Operator: Both Conditions Must Be True
x = 10
y = 20

if x > 5 and y > 15:
    print("Both conditions are true!") # Only prints if both conditions are met

# "or" Operator: At Least One Condition is True
temp = 50

if temp < 20 or temp > 90:
    print("Extreme weather!") # Prints if temp < 20 or temp > 90 (only one must be True)

# "not" Operator: Reverses a Condition
is_raining = False

if not is_raining:
    print("Touch grass.") # Since is_raining = False, not False = True, so it prints "Touch grass."

# Handling User Input (input() % try-except)
# Python's input() lets users enter data, but input is always stored as a string.

# Example: Convert Input to an Integer
age = int(input("Please enter your age: ")) # Converts input to an integer

if age >= 18:
    print("You are allowed to register to vote!")
else:
    print("You must be 18 or older in order to register to vote.")

# Entering anything except a number results in a ValueError, so patching that looks like the following:

# Preventing Crashes with try-except
# We can catch input errors using try-except:

try:
    age = int(input("Please enter your age: "))
    print(f"You are {age} years old!")
except ValueError:
    print("Invalid entry! Please enter a number.") # This prevents crashing if they enter a non-number

# Real-World Example: Trading Bot User Input
try:
    price = float(input("Enter Stock Price: ")) # Converts input to float
    if price > 100:
        print("Sell the Stock!")
    elif price < 90:
        print("Buy the Stock!")
    else:
        print("Hold the Stock.")
except ValueError:
    print("Invalid entry. Please enter a valid number.") # This handles incorrect input without crashing

# 2. Hands-On Coding Challenges
