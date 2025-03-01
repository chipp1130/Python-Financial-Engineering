

# 03.01.2025

portfolio = {}     # Start with empty dictionary to start
total_value = 0
while True:
    ticker = input("Please enter the ticker of the stock (or type 'exit' to finish):\n").upper()
    if ticker == 'EXIT':
        break
    
    try:
        shares = int(input(f"Enter shares for {ticker}:\n"))
        price = float(input(f"Enter share price for {ticker}:\n"))

        portfolio[ticker] = {'shares': shares, 'price': price}
        print(f"Added {shares} shares of {ticker} at ${price:.2f} each.\n")

    except ValueError:
        print("Invalid input, please check your entries.\n")

print("Your Stock Portfolio:\n")
for ticker, info in portfolio.items():
    print(f"{ticker}: {info['shares']} shares at ${info['price']} each.")
    value = info['price'] * info['shares']
    total_value += value
print(f"Total Portfolio Value: ${total_value:.2f}")