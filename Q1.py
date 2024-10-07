# Create a list to store temperature readings for 7 days
temperature_readings = []

# Input temperature readings for each day
for day in range(7):
    temp = float(input(f"Enter the temperature for day {day + 1}: "))
    temperature_readings.append(temp)

# Print the temperature readings
print("\nTemperature readings for the week:")
for day, temp in enumerate(temperature_readings, start=1):
    print(f"Day {day}: {temp}°C")
