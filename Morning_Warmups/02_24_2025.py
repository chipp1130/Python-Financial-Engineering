import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

def get_current_rates():
    try:
        sigma_p = float(input("Hello! What is the standard deviation (risk) of your portfolio? Please enter as a decimal.\n"))
    except ValueError:
        print("Please ensure you are entering valid numbers.")
        return  # Prevents execution if input is invalid

    # Get risk-free rate from 10-year Treasury (^TNX)
    risk_free = yf.download("^TNX", start="2025-02-24", end="2025-02-24")["Close"]
    if risk_free.empty:
        print("Error fetching risk-free rate. Using default 2.00%.")
        r_f = 0.02
    else:
        r_f = risk_free.iloc[-1] / 100  # Convert from % to decimal

    # Given market values
    e_rm = 0.10  # Market return
    sigma_m = 0.15  # Market standard deviation

    # Compute Sharpe Ratio
    sharpe_ratio = (e_rm - r_f) / sigma_m

    # Compute expected return for different levels of portfolio risk
    portfolio_risk = np.linspace(0, 0.30, 100)  # From 0% to 30%
    cml = r_f + (sharpe_ratio * portfolio_risk)

    # Plot CML
    plt.figure(figsize=(8, 5))
    plt.plot(portfolio_risk, cml, label="Capital Market Line", color='blue', linewidth=2)  
    plt.scatter(0, r_f, color='red', label="Risk-Free Asset", zorder=3)  # Risk-free rate at (0, R_f)
    
    # Labels & Title
    plt.xlabel("Portfolio Standard Deviation (σ_p)")
    plt.ylabel("Expected Return (E[R_p])")
    plt.title("Capital Market Line (CML)")
    plt.legend()
    plt.grid(True)

    # Show the plot
    plt.show()

# Run the function
get_current_rates()
