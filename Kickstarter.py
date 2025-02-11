import numpy as np
import pandas as pd
import yfinance as yf


# 02-11-2025:
def returns_finder():
    ticker = input("What stock do you want to find returns for? Please enter the ticker for your stock (Apple = AAPL)\n")
    start_date = input("Please enter the start date for the analysis in the following format: YYYY-MM-DD\n")
    end_date = input("Please enter the end date for the analysis in the following format: YYYY-MM-DD\n")
    return ticker, start_date, end_date
def returns_analyzer(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)["Close"]
    returns = data.pct_change().dropna()
    annualized_returns = returns.mean() * 252
    print(f"The average return of ${ticker.upper()} from {start_date} to {end_date} is {annualized_returns.iloc[0] * 100:.2f}%.")

ticker, start_date, end_date = returns_finder()
returns_analyzer(ticker, start_date, end_date)