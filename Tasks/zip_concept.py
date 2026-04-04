students = ["Alice", "Bob", "Charlie", "Diana"]
marks    = [92, 55, 78, 45]

# Task 1: Print each student with marks
for student, mark in zip(students, marks):
    print(f"{student} → {mark}")

# Task 2: Find passed students (marks >= 60)
passed = [s for s,m in zip(students,marks) if m >= 60]
print(passed)

# Task 3: Create student:marks dictionary
res = {s: m for s, m in zip(students, marks)}
print(res)
