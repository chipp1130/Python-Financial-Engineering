import numpy as np
import pandas as pd
import yfinance as yf
import scipy.stats as si

# Lesson 12: Options Pricing & The Black-Scholes Model

# Why This Matters:
# Options pricing is a core concept in quant finance and used by traders, hedge funds, and market makers.
# The Black-Scholes Model (BSM) is the most famous model for pricing European-style options.

# Today, we'll:
# Understand the Black-Scholes Formula
# Implement it in Python
# Analyze Options Prices with Different Parameters

# 1. The Black-Scholes Formula

# The Black-Scholes equation prices a European Call or Put Option, assuming no early exercise:

# Call Option Price = The price of a call option is the probability-adjusted value of owning the stock minus the cost of paying the strike price in the future.
# Put Option Price = The price of a put option is the probability-adjusted value of receiving the strike price minus the probability-adjusted value of giving up the stock at expiration.

# 2. Implementing Black-Scholes in Python

def get_user_option_information():
    """
    Get the necessary information from the user and calculate their Call/Put prices as per the Black-Scholes model.
    """
    try:
        S = float(input("What is the current Stock Price of the options contract you are looking into? $"))
        K = float(input("What is the Strike Price of the options contract you are analyzing? $"))
        T = float(input("Please enter the number of years until the contract expires (ex. 18 months = 1.5). "))
        r = float(input("What is the current Risk-Free Interest Rate? Please enter it as a decimal. "))
        sigma = float(input("What is the volatility of the asset, measured as a decimal? "))
        return S, K, T, r, sigma
    except ValueError:
        print("Please enter valid numerical values.")
        return get_user_option_information() # Restarts function

def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Compute the Black_Scholes option price for a European Call/Put.
    
    Parameters:
    S (float): Current Stock Price
    K (float): Strike Price
    T (float): Time to Expiration (in Years)
    r (float): Risk-Free Interest Rate (decimal)
    sigma (float): Volatility of the underlying asset (decimal)
    option_type (str): "call" for Call Option, "put" for Put Option
    
    Returns:
    float: Option Price
    """

    # Calculate d1 and d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        option_price = (S * si.norm.cdf(d1)) - (K * np.exp(-r * T) * si.norm.cdf(d2))
    elif option_type == "put":
        option_price = (K * np.exp(-r * T) * si.norm.cdf(-d2)) - (S * si.norm.cdf(-d1))
    else:
        raise ValueError("Invalid Option type. Please choose 'call' or 'put'.")
    
    return option_price

S, K, T, r, sigma = get_user_option_information()
call_price = black_scholes(S, K, T, r, sigma, option_type="call")
put_price = black_scholes(S, K, T, r, sigma, option_type="put")

print(f"Call Option Premium: ${call_price:.2f}")
print(f"Put Option Premium: ${put_price:.2f}")

# 3. Understanding the Output

# If the call price is high, the market expects the stock to increase.
# If the put price is high, the market expects downside risk.

# You can change the inputs (S, K, T, r, sigma) and see how options prices shift!

# 4. Your Challenge

# Run the Black-Scholes function in your own Python script (done)
# Modify the function to accept user input for stock price, strike price, and volatility
# (Stretch Goal) Modify the function to return Greeks (Delta, Gamma, Vega, Theta, Rho)