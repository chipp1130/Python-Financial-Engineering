import numpy as np

# Lesson 09: NumPy Dot Products & Portfolio Math

# Why Does This Matter in Finance?

# Used in portfolio optimization (mean-variance modeling)
# Helps calculate expected returns & risk (covariance matrices)
# Foundation for machine learning models in finance

# 1. Understanding the Dot Product

# The dot product is a fundamental operation in linear algebra & finance.

# Formula:
# A * B = (A1 x B1) + (A2 x B2) + ... + (An x Bn)

# How It's Used in Finance:
# Portfolio Expected Return: Multiply stock weights by expected returns.
# Risk Calculations: Compute variance & covariance matrices.

# Example: Computing Portfolio Return Using the Dot Product

# Expected returns of 3 assets (% returns)
expected_returns = np.array([0.08, 0.12, 0.10])

# Portfolio weights (50% in Asset 1, 30 % in Asset 2, 20% in Asset 3)
weights = np.array([0.50, 0.30, 0.20])

# Compute the expected portfolio return using dot product
portfolio_return = np.dot(weights, expected_returns)

print(f'Expected Portfolio Return: {portfolio_return:.3f}')

# Why Dot Product?
# Instead of manually computing:
# (0.50 * 0.08) + (0.30 * 0.12) + (0.20 * 0.10) = 9.60%
# NumPy does it instantly with np.dot()!

# 2. Computing Portfolio Risk (Variance & Standard Deviation)

# In finance, risk is measured by portfolio variance & standard deviation, using a covariance matrix.

# Formula for Portfolio Variance:

# First, W^T (Transpose of Weights) ensures correct dimensions for multiplication.
# Then, W^TΣ multiplies the covariance matrix by weights to compute weighted asset risk.
# Finally, the result is multiplied again by W to get total portfolio variance.

# Portfolio variance tells us how volatile the entire portfolio is.
# Portfolio standard deviation (sqrt(variance)) is the risk measure used in Sharpe ratios & VaR calculations.

# Example: Portfolio Risk Calculation:

# Covariance matrix (risk relationship between assets)
cov_matrix = np.array([
    [0.01, 0.002, 0.001],
    [0.002, 0.02, 0.003],
    [0.001, 0.003, 0.015]
])

# Compute portfolio variance
portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))

# Compute portfolio standard deviation (risk)
portfolio_stddev = np.sqrt(portfolio_variance)

print(f'Portfolio Variance: {portfolio_variance:.6f}')
print(f'Portfolio Standard Deviation: {portfolio_stddev:.6f}')

# Why Does This Matter?
# Variance tells us how volatile the portfolio is.
# Standard deviation is a risk measure used in VaR & Sharpe ratio calculations.

# Standard Deviation Standards:

# 0% - 5%:          Very Low Risk               Treasury Bonds, Money Market Funds
# 5% - 10%          Low Risk                    High-Grade Corporate Bonds, Bond ETFs
# 10% - 15%         Moderate Risk               S&P 500 Stocks, Balanced Portfolios
# 15% - 30%         High Risk                   Small-Cap Stocks, Emerging Markets
# 30%+              Extreme Risk                Crypto, Leveraged ETFs, Venture Capital

# Hands-On Coding Challenges

# Challenge 1: Compute Portfolio Return

# Given this data:
expected_returns = np.array([0.05, 0.07, 0.12, 0.09])
weights = np.array([0.4, 0.3, 0.2, 0.1])
# Compute the portfolio's expected return.

expected_return = np.dot(weights, expected_returns) * 100
print(f'Portfolio Expected Return: {expected_return:.2f}%')

# Challenge 2: Compute Portfolio Risk

# Given this covariance matrix:
cov_matrix = np.array([
    [0.010, 0.002, 0.001, 0.0005],  
    [0.002, 0.015, 0.0025, 0.0008],  
    [0.001, 0.0025, 0.020, 0.001],  
    [0.0005, 0.0008, 0.001, 0.025]
])
# Compute the portfolio's variance and standard deviation (risk).

portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
var_percentage = portfolio_variance * 100
portfolio_stddev = np.sqrt(portfolio_variance) * 100

if portfolio_stddev <= 5:
    print(f'Your portfolio contains very low risk. The Variance is {var_percentage:.2f}% and the Standard Deviation is {portfolio_stddev:.2f}%.')
elif portfolio_stddev <= 10:
    print(f'Your portfolio contains low risk. The Variance is {var_percentage:.2f}% and the Standard Deviation is {portfolio_stddev:.2f}%.')
elif portfolio_stddev <= 15:
    print(f'Your portfolio contains moderate risk. The Variance is {var_percentage:.2f}% and the Standard Deviation is {portfolio_stddev:.2f}%.')
elif portfolio_stddev <= 30:
    print(f'Your portfolio contains high risk! The Variance is {var_percentage:.2f}% and the Standard Deviation is {portfolio_stddev:.2f}%.')
else:
    print(f'Your portfolio contains extremely high risk! The Variance is {var_percentage:.2f}% and the Standard Deviation is {portfolio_stddev:.2f}%.')