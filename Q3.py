# Create a list to store daily stock prices for 7 days
stock_prices = []

# Input stock prices for each day
for day in range(7):
    price = float(input(f"Enter the stock price for day {day + 1}:RWF  "))
    stock_prices.append(price)

# Find the maximum and minimum stock prices
max_price = max(stock_prices)
min_price = min(stock_prices)

# Print the results
print(f"\nThe maximum stock price for the week is: RWF {max_price:.2f}")
print(f"The minimum stock price for the week is: RWF {min_price:.2f}")
