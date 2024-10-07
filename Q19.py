# List of products, where each sublist contains [name, price, stock]
products = [
    ["Laptop", 1200, 10],       # Name, Price, Stock
    ["Smartphone", 800, 0],
    ["Headphones", 150, 25],
    ["Monitor", 300, 5],
    ["Keyboard", 50, 0],
    ["Mouse", 30, 15]
]

# Function to filter and display products that are out of stock
def filter_out_of_stock(products):
    print("Products that are in stock:")
    for product in products:
        if product[2] > 0:  # Check if stock is greater than 0
            print(f"Name: {product[0]}, Price: RWF {product[1]}, Stock: {product[2]}")

# Display products that are in stock
filter_out_of_stock(products)
