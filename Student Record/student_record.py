"""
student_record.py

This script models a student record including grades and status,
demonstrating Python data types, nested structures, and conditional logic.

Naming convention: snake_case
"""

students = {
    "2023-001": {
        "name": "Cliff Mendoza",
        "year": "1st Year",
        "grades": {
            "Math": 89,
            "English": 91,
            "Python": 95
        }
    },
    "2023-002": {
        "name": "Andrea Cruz",
        "year": "2nd Year",
        "grades": {
            "Math": 87,
            "English": 85,
            "Python": 92
        }
    },
    "2023-003": {
        "name": "Leo Tan",
        "year": "3rd Year",
        "grades": {
            "Math": 90,
            "English": 88,
            "Python": 93
        }
    }
}
# Step 2: Print all student records
print("\n===== STUDENT RECORDS =====\n")

for student_id, details in students.items():
    print(f"ID: {student_id}")
    print(f"Name: {details['name']}")
    print(f"Year: {details['year']}")
    print("Grades:")
    for subject, grade in details["grades"].items():
        print(f"  {subject}: {grade}")
    print("-" * 35)
    print (f"Average Grade: {sum(details['grades'].values()) / len(details['grades']):.2f}")
    print("-" * 35)
    if sum(details["grades"].values()) / len(details["grades"]) >= 90:
        print("Status: Passed")
    else:
        print("Status: Failed")
    
    print(f"Type of Grades: {type(details['grades'])}")
    print(f"Type of Grades Dictionary: {type(details['grades'])}")
    print("-" * 35)
    print(f"Type of Student ID: {type(student_id)}")
    print(f"Type of Details: {type(details)}") 
    print("-" * 35)
    print(f"Type of Average Grade: {type(sum(details['grades'].values()) / len(details['grades']))}")
    print("-" * 35)
    print(f"Type of Average Grade: {type(sum(details['grades'].values()) / len(details['grades']))}")
    print("-" * 35)
    print(f"Type of Status: {type('Passed' if sum(details['grades'].values()) / len(details['grades']) >= 90 else 'Failed')}")
    print("-" * 35)
    print(f"Type of Grades Dictionary: {type(details['grades'])}")
    print("-" * 35) 

print("\n===== END OF STUDENT RECORDS =====\n")

print ("===END OF RECORD===")