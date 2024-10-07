# 2D list where each sublist contains expenses for 6 months for each category
expenses = [
    [1200, 1300, 1250, 1350, 1280, 1400],  # Rent
    [300, 350, 400, 380, 370, 390],        # Food
    [150, 160, 170, 180, 175, 165],        # Utilities
    [100, 120, 90, 110, 130, 105]          # Transportation
]

# List of categories for reference
categories = ["Rent", "Food", "Utilities", "Transportation"]

# Calculate and display the average monthly expense per category
for i in range(len(expenses)):
    # Calculate the average by summing up expenses and dividing by the number of months (6 months)
    avg_expense = sum(expenses[i]) / len(expenses[i])
    print(f"Average monthly expense for {categories[i]}: RWF {avg_expense:.2f}")
