import numpy as np
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Lesson 13: Monte Carlo Methods for Options Pricing

# Why Monte Carlo?
# Black-Scholes is great for simple options, but real markets have complexities like:
# Volatility Smiles, Stochastic Interest Rates, Path-Dependent Options, etc.

# Monte Carlo methods let us simulate thousands / millions of possible price paths
# and compute an average expected payoff under the risk-neutral measure.

# 1. Monte Carlo Basics

# Monte Carlo simulations use random sampling to estimate expected values.

# How does it work in finance?
#   1. Simulate thousands of potential future stock prices using a mathematical model.
#   2. Compute the option payoff for each scenario.
#   3. Average the payoffs and discount them back to present value.

# Risk Neutral Expected Value Formula:
# 1️. Generate random stock price paths using the Geometric Brownian Motion model.
# 2️. Calculate the option's payoff for each simulated price path:
#   Call Option: max⁡(​S subT − K,0) → If the stock price is above 𝐾, the option has value. Otherwise, it's worthless.
#   Put Option: max(K − S SubT, 0) → If the stock price is below 𝐾, the option has value. Otherwise, it's worthless.
# 3️. Average all payoffs from the simulations.
# 4️. Discount the expected payoff back to present value using e ^ (-Rf * T)
# This method allows us to estimate the fair price of an option by modeling thousands of possible outcomes and finding the average expected return.

# 2. Simulating Stock Prices

# To simulate stock prices, we use the Geometric Brownian Motion (GBM) model, which assumes:
#   1. Define initial stock price S sub 0, risk-free rate Rf, volatility 𝜎, and time horizon 𝑇.
#   2. Generate random normal shocks (simulating market uncertainty).
#   3. Compute the drift and random shock components.
#   4. Calculate the future stock price 𝑆 sub T using the GBM formula.
#   5️. Repeat many times (e.g., 10,000 simulations) to estimate a range of possible stock prices.

# 3. Monte Carlo Option Pricing in Python

# Now, let's price a European Call Option using Monte Carlo simulation:

def monte_carlo_call_price(S0, K, T, r, sigma, num_simulations=1000000):
    """
    Monte Carlo simulation for European call option pricing.
    
    Parameters:
    S0 (float): Initial Stock Price
    K (float): Strike Price
    T (float): Time to Expiration (years)
    r (float): Risk-Free Interest Rate (decimal)
    sigma (float): Volatility of the asset (decimals)
    num_simulations (int): Number of Monte Carlo Simulations

    Returns:
    float: Estimated Call Option Price
    """

    # Generate random numbers from standard normal distribution
    W_T = np.random.standard_normal(num_simulations)

    # Simulate end stock prices using Geometric Brownian Motion (GBM)
    S_T = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * W_T)

    # Compute payoffs (only positive payoffs contribute)
    payoffs = np.maximum(S_T - K, 0)

    # Compute present value of expected payoff
    option_price = np.exp(-r * T) * np.mean(payoffs)

    return option_price, S_T

# Example:
S0 = 100        # Current stock price
K = 110         # Strike price
T = 1           # 1 year until expiration
r = 0.05        # 5% risk-free rate
sigma = 0.20    # 20% volatility

call_price, simulated_prices = monte_carlo_call_price(S0, K, T, r, sigma)
print(f"Monte Carlo Estimated Call Price: ${call_price:.2f}")

plt.figure(figsize=(12,6))
plt.hist(simulated_prices, bins=50, edgecolor="black", alpha=0.75)
plt.xlabel("Simulated Stock Price at Expiration")
plt.ylabel("Frequency")
plt.title(f"Monte Carlo Simulation of {len(simulated_prices)} Stock Price Paths")
plt.axvline(K, color="red", linestyle="dashed", label=f"Strike Price (${K})")
plt.legend()
plt.show()

# Key Takeaways:
#   1. Monte Carlo simulations estimate expected payoffs by simulating thousands of price paths
#   2. The GBM model is commonly used to model stock prices.
#   3. We discount future expected payoffs using the risk-free rate to get the present value.