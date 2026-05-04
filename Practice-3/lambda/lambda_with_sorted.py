# lambda_with_sorted.py

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 92},
    {"name": "Charlie", "grade": 78}
]

# Sort students by grade
sorted_students = sorted(students, key=lambda student: student["grade"])

print("Sorted by grade:")
for student in sorted_students:
    print(student)
