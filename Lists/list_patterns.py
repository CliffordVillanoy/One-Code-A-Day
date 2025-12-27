grades = [55, 67, 80]
print(grades[0])
print (grades[1])

grades[2] = 80
grades.append(92)

print(grades)
print(len(grades))
print(type(grades))
# Step 1: Create a dictionary to store student records
students = {
    "2023-001": {
        "name": "John Doe",
        "year": "1st Year",
        "grades": {
            "Math": 85,
            "English": 90,
            "Python": 88
            
        }   
    },

    "2023-002": {
        "name": "Jane Smith",
        "year": "2nd Year",
        "grades": {
            "Math": 78,
            "English": 82,
            "Python": 80
        }
    },
    "2023-003": {
        "name": "Alice Johnson",
        "year": "3rd Year",
        "grades": {
            "Math": 92,
            "English": 95,
            "Python": 94
        }
    },
    "2023-004": {
        "name": "Bob Brown",
        "year": "4th Year",
        "grades": {
            "Math": 88,
            "English": 84,
            "Python": 90
        }
    },
    "2023-005": {
        "name": "Bob Brown",
        "year": "4th Year",
        "grades": {
            "Math": 88,
            "English": 84,
            "Python": 90
        }
    }
    
    , "2023-006": {
 "name": "Bob Brown",
        "year": "4th Year",
        "grades": {
            "Math": 88,
            "English": 84,
            "Python": 90 
        }   
    },
    "2023-007": {
        "name": "Bob Brown",
        "year": "4th Year",
        "grades": {
            "Math": 88,
            "English": 84,
            "Python": 90
        }
    },
    "2023-008": {
        "name": "Bob Brown",
        "year": "4th Year",
        "grades": {
            "Math": 88,
            "English": 84,
            "Python": 90
        }
    }
}
# Step 2: Print all student records
for student_id, student_info in students.items():
    print(f"ID: {student_id}")
    print(f"Name: {student_info['name']}")
    print(f"Year: {student_info['year']}")
    print("===")
    print("Grades:")
    for subject, grade in student_info['grades'].items():
        print(f"  {subject}: {grade}")
        print("===")
    print()


    
print("\n===== STUDENT RECORDS =====\n")
print("===END OF RECORD===")
print("\n===== END OF STUDENT RECORDS =====\n")
