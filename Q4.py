# Create a list to store student marks
student_marks = []

# Input marks for a number of students
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    mark = float(input(f"Enter the mark for student {i + 1}: "))
    student_marks.append(mark)
    

# Reverse the order of the marks
reversed_marks = student_marks[::-1]

# Print the reversed marks
print("\nReversed order of student marks:")
for i, mark in enumerate(reversed_marks, start=1):
    print(f"Student {i}: {mark}")
