"""
student_record.py

This script models a student record including grades and status,
demonstrating Python data types, nested structures, and conditional logic.

Naming convention: snake_case
"""

full_name = "John Doe"
student_id = "123456"
age = 20
is_enrolled = True

grades = {
    "math": 89,
    "science": 92,
    "history": 85,
    "english": 88
}

average_grade = sum(grades.values()) / len(grades)
status = "Pass" if average_grade >= 75 else "Fail"

print("\n===== STUDENT RECORD =====\n")

print(f"Full Name: {full_name}) — Type: {type(full_name)}")
print(f"Student ID: {student_id} — Type: {type(student_id)}")
print(f"Age: {age} — Type: {type(age)}")
print(f"Enrolled: {is_enrolled} — Type: {type(is_enrolled)}")

print(f"\nGrades: {grades} — Type: {type(grades)}")
print(f"Average Grade: {average_grade:.2f} — Type: {type(average_grade)}")
print(f"Status: {status} — Type: {type(status)}")
print(f"Grades (Detailed):")
for subject, grade in grades.items():
    print(f"  {subject}: {grade} — Type: {type(grade)}")    
print("\n===== END OF STUDENT RECORD =====\n")

    