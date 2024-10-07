# Define the number of students and subjects
num_students = 3
num_subjects = 4

# Sample 2D array where rows represent students and columns represent marks in different subjects
marks = [
    [75, 85, 90, 95],  # Student 1 marks
    [88, 92, 80, 76],  # Student 2 marks
    [60, 65, 70, 72]   # Student 3 marks
]

# Initialize a list to store the total marks of each student
total_marks = []

# Loop through each student (each row)
for i in range(num_students):
    # Calculate the sum of marks for the current student
    total = sum(marks[i])
    # Append the total marks of the current student to the total_marks list
    total_marks.append(total)

# Print total marks of each student
for i in range(num_students):
    print(f"Total marks of student {i+1}: {total_marks[i]}")
