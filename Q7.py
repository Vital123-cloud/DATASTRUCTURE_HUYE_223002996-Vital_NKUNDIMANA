# Define the number of products and days
num_products = int(input("Enter the number of products: "))
num_days = 7  # Weekly sales

# Create a 2D array to store weekly sales
weekly_sales = [[0 for _ in range(num_days)] for _ in range(num_products)]

# Input sales data for each product
for i in range(num_products):
    print(f"\nEnter sales for Product {i + 1}:")
    for j in range(num_days):
        sales = float(input(f"  Day {j + 1}: "))
        weekly_sales[i][j] = sales

# Display the sales data
print("\nWeekly Sales Data:")
print("Product \\ Day", end="\t")
for day in range(1, num_days + 1):
    print(f"Day {day}", end="\t")
print()

for i in range(num_products):
    print(f"Product {i + 1}", end="\t")
    for j in range(num_days):
        print(f"{weekly_sales[i][j]:.2f}", end="\t")
    print()  # New line after each product
