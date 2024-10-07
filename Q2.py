# Create a list to store daily sales for 7 days
daily_sales = []

# Input daily sales for each day
for day in range(7):
    sales = float(input(f"Enter the sales for day {day + 1}: RWF "))
    daily_sales.append(sales)

# Calculate the average sales
average_sales = sum(daily_sales) / len(daily_sales)

# Print the average sales
print(f"\nThe average daily sales for the week is: {average_sales:.2f} RWF")
