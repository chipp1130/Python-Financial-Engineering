import numpy as np
import pandas as pd
import yfinance as yf

# 02-14-2025 Morning Challenge

# Custom Probability Distribution Sampler:
# Write a function that allows the user to define a custom discrete probability
# and then randomly sample from it according to the defined probabilities:

#   1. Ask the user to input possible outcomes (e.g, "Win", "Lose", "Draw")
#   2. Ask the user to input corresponding probabilities (must sum to 1.0).
#   3️. Validate inputs (ensure probabilities sum to 1.0, handle invalid input).
#   4. Allow the user to sample from this distribution a specified number of times.
#   5. Return a dictionary showing the frequency of each outcome.

def discrete_probability_generator():

    try:
        print("Welcome! When using this calculator, please ensure that you are entering percentages as decimals (30% = 0.30). Have fun!\n")
        
        outcomes = int(input("How many total outcomes are there in your model?\n"))
        outcome_labels = []
        probabilities = []
        total_probability = 0

        for outcome in range(outcomes):
            label = input(f"Enter a name/label for Outcome {outcome+1}: ")
            probability = float(input(f"What is the probability of outcome {outcome+1}?\n"))
            outcome_labels.append(label)
            probabilities.append(probability)
            total_probability += probability

        if not np.isclose(total_probability, 1.0, atol=0.01): 
                print("\nError: Probabilities must sum to 1.0! Please check your inputs and try again.\n")
                return

        simulations = int(input("How many times do you want to run this simulation?\n"))

        simulated_results = np.random.choice(outcome_labels, size=simulations, p=probabilities)

        unique, counts = np.unique(simulated_results, return_counts = True)
        results_dict = dict(zip(unique, counts))

        print("\nSimulation Results:\n")
        for outcome, count in results_dict.items():
            print(f"{outcome}: {count} times ({(count/simulations)*100:.2f}%)\n")

    except ValueError:
        print("Please check your values and try again!")
        return
discrete_probability_generator()