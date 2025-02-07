# Lesson 06: Error Handling & Debugging
# Common Python Errors (Syntax Error, TypeError, ValueError)
# Using try-except for Robust Programs

# 1. Understanding Common Python Errors:
# Syntax Errors (SyntaxError)
# This happens when Python doesn't understand your code structure.

# print("Hello" # This is missing the closing parenthesis

# Type Errors (TypeError)
# These occur when an operation is used on an incorrect data type.

age = "25"
# print(age + 5) # You cannot add a string and integer together.

# Fix:
print(int(age) + 5) # Successfully converts the string to an integer

# Value Errors (ValueError)
# These happen when a function receives an invalid value.

# num = int("hello") # Can't convert a string into an integer

# Fix:
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid input.")

# 2. Using try-except to Prevent Crashes
# Instead of letting a program crash, try-except lets us handle errors gracefully.

# Example: Handling ZeroDivisionError

try:
    x = 10 / 0 # Division by 0 is not allowed
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

# Challenge: Fix This Code
# try:
#    num = int(input("Enter a number: "))
#    print("Your number doubled is:", num * 2)
# except:
#    print("Something went wrong!")

try:
    num = int(input("Enter a number: "))
    print("Your number doubled is:", num * 2)
except ValueError:
   print("Invalid entry! Please enter a valid number.")

# 3. Debugging Techniques
# Debugging with Print Statements

# Example: Debugging a Loop
nums = [1, 2, 3, 4, 5]
total = 0

for num in nums:
    print(f"Before adding: {total}") # Debugging print
    total += num
    print(f"After adding: {total}\n") # Debugging print

# Seeing the value before and after the change helps find errors.

# Debugging with breakpoints (VS Code, PyCharm)
# If you're using an IDE, you can pause execution at breakpoints to inspect variables.

# Hands-On Debugging Challenges

# 1. Fix the error in this code:
# x = "10"
# y = 5
# print(x + y)

x = 10
y = 5
print(x + y) # You can't add a string and an integer

# 2. Fix the logic bug here:
# numbers = [1, 2, 3, 4, 5]
# even_numbers = []

# for num in numbers:
#   if num % 2 == 0:
#       num = num * 2
# print(even_numbers) # Expects doubled even numbers, but it's empty!

numbers = [1, 2, 3, 4, 5]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num * 2)
print(even_numbers)