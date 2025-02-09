import numpy as np
import pandas as pd

# Win Probability = .55
# Loss Probability = .45

# Payout = 1.9x Multiplier
# Loss = 0.0x Multiplier (Everything)

import numpy as np
import pandas as pd

# Function to get user bet amount
def initial_bet():
    """This function asks the user for their initial bet amount."""
    try:
        bet = float(input("How much would you like to place a bet for? $"))
        if bet <= 0:
            print("Bet amount must be greater than $0.")
            return initial_bet()
        return bet
    except ValueError:
        print("Please enter a valid amount to continue.")
        return initial_bet()

# Get bet amount from user
bet_amount = initial_bet()

# Define probabilities
win_probability = 0.55
loss_probability = 0.45

# Define payouts
win_pay = bet_amount * 1.9  # Win = 1.9x the bet
loss_pay = -bet_amount       # Loss = Lose entire bet

# Compute expected return
expected_return = (win_probability * win_pay) + (loss_probability * loss_pay)
print(f"\nYour expected return is ${expected_return:.2f}.")

# Function to compute risk metrics
def risk_analysis():
    """Analyzes the risk using variance, standard deviation, and Kelly Criterion."""
    var = win_probability * ((win_pay - expected_return) ** 2) + (loss_probability * (loss_pay - expected_return) ** 2)
    stddev = np.sqrt(var)  # Compute standard deviation correctly
    
    # Correct Kelly Criterion formula
    kelly_criterion = (win_probability - (loss_probability / 0.9))
    kelly_percent = kelly_criterion * 100

    # Print results
    print(f'\nBet Variance: ${var:.2f}')
    print(f'Standard Deviation: ${stddev:.4f}')

    if kelly_percent > 0:
        print(f'Optimal Percent to Bet: {kelly_percent:.2f}% of your bankroll.')
    else:
        print("Kelly suggests NOT placing a bet as the edge is too low.")

# Run risk analysis
risk_analysis()