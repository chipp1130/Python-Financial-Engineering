import numpy as np
import pandas as pd
import yfinance as yf

# 02_16_2025 Morning Practice:

# List basics:
numbers = [1, 2, 3, 4, 5]                       # Creates a list
numbers.append(6)                               # Adds 6 to the end of the list "numbers"
numbers.insert(2, 99)                           # Inserts 99 at index 2 ("3")
numbers.remove(3)                               # Removes the item at index 3 ("4")
last = numbers.pop()                            # Removes last number and stores it
print(numbers, last)                            # Output: [1, 2, 99, 4, 5], 6

# List comprehensions
squares = [x ** 2 for x in range(1, 6)]         # Squares the numbers 1 through 5
evens = [x for x in range(10) if x % 2 == 0]    # Returns the even numbers from 1 to 9
print(squares, evens)

# Dictionaries
person = {"name": "Alice", "age": 25}           # Creates dictionary with name and age as keys and Alice and 25 as values
person["city"] = "New York"                     # Adds new key-value pair to the dictionary
age = person.get("age", 0)                      # Get 'age', returns 0 if missing
del person["city"]                              # Deletes key-value pair ["city": New York]
print(person, age)                              # Output: {"name": "Alice", "age": 25}, 25

# Loops
for i in range(1, 6):
    print(f"Number: {i}")                       # Output: Number: 1, 2, 3, 4, 5

# Functions
def add(a, b):
    return a + b
result = add(3, 7)
print(result)                                   # Output: 10

# Recursion
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))                             # Output: 120

# Lambda Functions
double = lambda x: x * 2
print(double(4))                                # Output: 8

# Sorting Lists
nums = [5, 2, 8, 1, 3]
nums.sort()                                     # Sorts nums in ascending order
sorted_nums = sorted(nums, reverse=True)        # Sorts nums in descending order
print(nums, sorted_nums)                        # Output: [1, 2, 3, 5, 8] [8, 5, 3, 2, 1]

# Class Basics
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."
class Dog(Animal):
    def speak(self):
        return "Woof!"
dog = Dog("Buddy")
print(dog.speak())

# Coding Exercise:
# Write a function that counts how many unique characters are in a given string.
# unique_chars("hello")  # Output: 4  (h, e, l, o → 'l' appears twice but is counted once)
# unique_chars("banana")  # Output: 3  (b, a, n)
# unique_chars("abcdef")  # Output: 6  (All letters are unique)
# unique_chars("")  # Output: 0  (Empty string)

# 📌Hints:
# ✔ Use a set (since sets only store unique elements).
# ✔ Think about how to handle an empty string.

def unique_characters(word):
    return len(set(word))

print(unique_characters("Connor"))