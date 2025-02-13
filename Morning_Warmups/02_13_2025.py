import numpy as np
import pandas as pd
import yfinance as yf

# 02-13-2025 Morning Warmup

# Bayes' Theorem Calculator

# The user will input:
#   P(A) --> Prior probability (i.e. chance of fraud, disease, etc.)
#   P(B|A) --> Likelihood (true positive rate)
#   P(B|Not A) --> False positive rate

# The program will output P(A|B), using Bayes' Theorem:
# P(A|B) = P(B|A) * P(A) + P(B¬A) * P(¬A)

def bayes_calculator():

    print("Hello, and thank you for using the Bayes' Theorem Calculator!\nPlease ensure you are entering your values as decimals prior to entry:\n")

    event = input("First question for you, what is the event that you are looking to find the true probability for?\n")

    try:
        PA = float(input(f"What is the current probability of your event, {event}, (P(A)) happening?\n"))
        
        PBA = float(input(f"Now, what is the true positive rate of your event, {event}? As in, what is the real positive case rate?\n"))
        
        PBnotA = float(input(f"What is the false positive rate of your event, {event}?\n"))

        if not (0 <= PA <= 1 and 0 <= PBA <= 1 and 0 <= PBnotA <= 1):
            
            print("\nError: All inputs must be between 0 and 1 (e.g., 0.10 for 10%).\n")
            
            return
    
    except ValueError:
        
        print("Please enter only percentages as decimal values, thank you!")

        return
    
    PnotA = (1 - PA)
    
    PB = (PBA * PA) + (PBnotA * PnotA)
    
    PAB = (PBA * PA) / PB

    print(f"Given that {event} was detected, the true probability of it actually occurring is {PAB:.2%}.\n")

bayes_calculator()