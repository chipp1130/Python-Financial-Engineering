# Lesson 04: Loops & Iterations
# Loops allow us to repeat actions efficiently instead of writing the same code multiple times.
# In financial modeling, loops help process large datasets, simulate market scenarios, and automate calculations.

# 1. Introductory Reading: Understanding Loops

# Why Do We Need Loops?

# Imagine you need to calculate daily stock returns for an entire year. You could manually type:

# return_day_1 = (price_day_1 - price_day_0) / price_day_0  
# return_day_2 = (price_day_2 - price_day_1) / price_day_1  
# return_day_3 = (price_day_3 - price_day_2) / price_day_2  

# ... this would take forever!  

# Instead, with a loop, you automate this process:

# for i in range(1, len(prices)):
#     daily_return = (prices[i] - prices[i - 1]) / prices[i- 1]
#     print(f'Day {i}: {daily_return:.2%}')

# 1. For Loops -- Iterate over sequences

# Syntax:
# for variable in iterable:
#   do something

# Used for lists, tuples, dictionaries, ranges, and even strings.

# Example: Iterating Over Stock Prices:
prices = [100, 102, 105, 101]
for price in prices:
    print(f'Stock Price: {price}')

# 2. While Loops -- Repeat until a condition is false

# Syntax:
# while condition:
#   do something

# Best for when we don't know the exact number of iterations in advance.

# Example: Simulating Market Drop Until Recovery:
price = 80 
while price > 90:  
    price -= 2  # price drops  
    print(f"Price dropped to: {price}")  
print("Market recovered!")

# 3. Loop Control Statements
# Statement:         Function:
# break              Stops the loop immediately
# continue           Skips to the next iteration

# Example: Stop When a Stop-Loss is Hit:
prices = [100, 98, 95, 92, 89, 94]
for price in prices:
    if price < 90:
        print("Stop-Loss triggered! Exiting position.\n")
        break # exits loop
    print(f'The price is currently {price}.')

# 2. Experiential Coding & Exercises:

# Challenge 1: Calculate Moving Averages
# A moving average smooths out stock prices over a period.
# Write a loop to compute a 3-day moving average from this list:

prices = [100, 102, 104, 98, 95, 97, 106]

# Hint: The moving average at index "i" is (prices[i] + prices[i - 1] + prices[i - 2]) / 3

for i in range(2, len(prices)):  # Start from index 2 to access [i-2]
    three_day = (prices[i] + prices[i - 1] + prices[i - 2]) / 3
    print(f"3-day moving average at day {i + 1}: {three_day:.2f}\n")  # Print inside loop

# Challenge 2: Find the First Stock Price Above $105
# Loop through prices and print the first price above $105 and then stop.
# Hint: Use break

for price in prices:
    if price > 105:
        print(f'The price is ${price}.\n')
        break
    

# Challenge 3: Simulate a Trading Bot
# Start with $1000.
# Buy stock when the price drops below 95.
# Sell stock when it goes above 103.
# Stop if the portfolio balance drops below $500.

# portfolio = 1000
# stock_price = [102, 92, 94, 96, 99, 105, 109]

# for price in stock_price:
#     if price > 95:                                              # This would buy if the price is above $95
#         portfolio - int(stock_price)                            # This doesn't update the portfolio
#         break                                                   # This will exit the loop after the first price
#     elif price < 103:                                           # This would buy if the price is below $103
#         portfolio + int(stock_price)                            # This doesn't update the portfolio
#         break
#     print(f"Your portfolio is currently worth ${portfolio}.")

# Corrected version: 

portfolio = 1000
stock_price = [102, 92, 94, 96, 99, 105, 109]

for price in stock_price:
    if price < 95:  # Buy when price drops below 95
        portfolio -= price
        print(f"Bought stock at ${price}. Current Portfolio Value: ${portfolio}\n")
    elif price > 103:  # Sell when price goes above 103
        portfolio += price
        print(f"Sold stock at ${price}. Current Portfolio Value: ${portfolio}\n")
    # Stop trading if portfolio balance drops below $500
    if portfolio < 500:
        print("Portfolio dropped below $500. Trading stopped.")
        break