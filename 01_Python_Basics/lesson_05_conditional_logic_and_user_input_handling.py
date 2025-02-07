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

# Challenge 1: Temperature Checker
# Write a program that asks for a temperature and prints:
# "It's freezing!" if below 0.
# "It's warm outside." if between 1 and 25.
# "It's hot!" if above 25.

try:
    temperature = int(input("What is the current temperature outside (In degrees Celsius)? "))
    if temperature <= 0:
        print("It's freezing outside!")
    elif 1 <= temperature <= 25:
        print("It's warm outside.")
    else:
        print("It's hot outside!")
except ValueError:
    print("Please enter a valid temperature in degrees Celsius.")

# Challenge 2: FizzBuzz Game
# If the number is divisible by both 3 and 5, print "FizzBuzz!"
# If only divisible by 3, print "Fizz!"
# If only divisible by 5, print "Buzz!"
# Otherwise, print "Not a FizzBuzz number."

try:
    number = int(input("Please enter an integer!\n"))
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz! Your number, {number}, is divisible by both 3 and 5!")
    elif number % 3 == 0:
        print(f"Fizz! Your number, {number}, is divisible by 3!")
    elif number % 5 == 0:
        print(f"Buzz! Your number, {number}, is divisible by 5!")
    else:
        print(f"Your number, {number}, is not a FizzBuzz number. Try again!")
except ValueError:
    print("Please enter a valid integer to play FizzBuzz!")

# Challenge 3: User Age Input (Handle Errors!)
# If the input is not a number, print "Invalid input!"
# If the number is less than 18, print "You cannot vote yet."
# Otherwise, print "You can vote!"

try:
    user_age = int(input("Please enter your age!\n"))
    if user_age <= 18:
        print(f"Sorry! {user_age} year olds are not permitted to vote in your location.")
    else:
        print(f"{user_age} year olds are permitted to vote in your jurisdiction!")
except ValueError:
    print("Please enter a valid age to check voter eligibility!")

