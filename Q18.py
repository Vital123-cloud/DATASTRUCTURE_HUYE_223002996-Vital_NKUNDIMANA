# Create a 2D list representing the seating arrangement in a theater
# 'A' represents an available seat, and 'R' represents a reserved seat
seating = [
    ['A', 'A', 'A', 'A', 'A'],  # Row 1
    ['A', 'A', 'A', 'A', 'A'],  # Row 2
    ['A', 'A', 'A', 'A', 'A'],  # Row 3
    ['A', 'A', 'A', 'A', 'A'],  # Row 4
    ['A', 'A', 'A', 'A', 'A'],  # Row 5
]

# Function to reserve a seat
def reserve_seat(row, seat):
    if seating[row][seat] == 'A':  # Check if the seat is available
        seating[row][seat] = 'R'   # Reserve the seat
        print(f"Seat {seat + 1} in row {row + 1} has been reserved.")
    else:
        print(f"Seat {seat + 1} in row {row + 1} is already reserved.")

# Display the current seating arrangement
def display_seating():
    print("\nCurrent seating arrangement:")
    for row in seating:
        print(" ".join(row))

# Initial display of seating arrangement
display_seating()

# Assigning some reserved seats
reserve_seat(0, 2)  # Reserve seat 3 in row 1
reserve_seat(2, 4)  # Reserve seat 5 in row 3
reserve_seat(4, 0)  # Reserve seat 1 in row 5
reserve_seat(1, 1)  # Reserve seat 2 in row 2

# Display the updated seating arrangement after reservations
display_seating()
