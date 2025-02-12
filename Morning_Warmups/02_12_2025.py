import numpy as np
import pandas as pd
import yfinance as yf

# 02-12-2025 Coding Exercises:

# Betting Strategy Calculator:

# Build a program that:
#   Asks the user for probabilities & payoffs of a bet
#   Calculates the expected value (EV)
#   Tells the user if the bet is profitable

def bet_outline():
    
    print("Hello! Welcome to the Expected Value Calculator. Please enter the parameters of your game here:")

    try:
        outcomes = int(input("In your game, how many different outcomes can you achieve? (ex. win/loss/tie mean three possible results)\n"))
        
        total_probability = 0
        
        expected_value = 0
        
        for i in range(outcomes):
            
            payout = float(input(f"Enter the payout amount for outcome {i + 1}. (Negative amount for losses)\n$"))
            
            probability = float(input(f"Enter the probability of this outcome in decimal format please.\n"))    
            
            total_probability += probability
            expected_value += probability * payout
        
        if not np.isclose(total_probability, 1.0, atol=0.01):
            
            print("\nError: Probabilities must sum to 1.0! Please check your inputs.\n")
            
            return
        
        print(f"\nExpected Value (EV) of this game: ${expected_value:.2f}\n")
        
        if expected_value > 0:
            print("This is a profitable bet in the long run!")
        
        if expected_value < 0:
            print("This is an unprofitable bet in the long run.")
        
        else:
            print("This is a breakeven bet.")
    
    except ValueError:
        print("Please ensure you are checking your inputs before entering.")

bet_outline()