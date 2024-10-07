# List of students, where each sublist contains [name, age, grade]
students = [
    ["Alice", 20, 88],
    ["Bob", 22, 75],
    ["Charlie", 21, 95],
    ["Diana", 19, 80],
    ["Eve", 23, 90]
]

# Print the original list of students
print("Original list of students:")
for student in students:
    print(student)

# Sort the list by grade (3rd element in each sublist, index 2)
students.sort(key=lambda x: x[2])

# Print the sorted list of students
print("\nSorted list of students by grade:")
for student in students:
    print(student)
