grades = [55, 67, 80]
print(grades[0])
print (grades[1])

grades[2] = 80
grades.append(92)

print(grades)
print(grades[2:])  # Slicing to get elements from index 2 to the end 
print(grades[1:3])  # Slicing to get elements from index 1 to index 2 (exclusive)       
print(grades[:2])  # Slicing to get elements from the start to index 1 (exclusive)
print(grades[-1])  # Accessing the last element using negative indexing

print(grades[-2:])  # Slicing to get the last two elements  
print(grades[-3:-1])  # Slicing to get elements from the third last to the second last element
print(grades[-3:])  # Slicing to get the first three elements
print(grades[-1:0]) # Slicing from the last element to the first (empty result)
print(grades[-3:2])  # Slicing from the third last to index 2 (exclusive)
print(grades[-3:-2])  # Slicing to get the third last element  
print(grades[1])
print(grades[:])  # Slicing to get all elements
print(grades[1:])  # Slicing to get elements from index 1 to the end
print(grades[1:2])  # Slicing to get the element at index 1
print(grades[1:3])  # Slicing to get elements from index 1 to index 2 (exclusive)
print
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
