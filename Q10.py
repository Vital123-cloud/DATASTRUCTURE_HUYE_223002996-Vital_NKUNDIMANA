# Define the number of cities and days in a week
num_cities = 4
num_days = 7

# 3D array where each sub-array represents a city, and inside it are daily temperature readings
temperatures = [
    [ [30, 32, 31, 29, 30, 31, 33] ],  # City 1 temperatures for 7 days
    [ [25, 26, 27, 25, 24, 26, 28] ],  # City 2 temperatures for 7 days
    [ [35, 36, 34, 33, 35, 34, 36] ],  # City 3 temperatures for 7 days
    [ [20, 22, 21, 23, 21, 20, 24] ]   # City 4 temperatures for 7 days
]

# List to store the average temperature of each city
average_temperatures = []

# Loop through each city
for city in range(num_cities):
    # Calculate the average temperature for the current city
    total_temperature = sum(temperatures[city][0])
    average_temperature = total_temperature / num_days
    
    # Append the average temperature to the list
    average_temperatures.append(average_temperature)

# Display the average temperature for each city
for city in range(num_cities):
    print(f"Average temperature for City {city + 1}: {average_temperatures[city]:.2f}°C")
