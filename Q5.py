# Create a list to store random numbers
random_numbers = []

# Input the number of random numbers to be entered
num_count = int(input("Enter the number of random numbers: "))

# Input random numbers
for i in range(num_count):
    number = int(input(f"Enter number {i + 1}: "))
    random_numbers.append(number)

# Initialize counters for even and odd numbers
even_count = 0
odd_count = 0

# Count even and odd numbers
for number in random_numbers:
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print the results
print(f"\nNumber of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")
