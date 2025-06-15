employees = [
    {
        "name": "John Doe",
        "position": "Software Engineer",
        "department": "Engineering",
        "email": "test@sample.com"
    },
    {
        "name": "Jane Smith",
        "position": "Product Manager",                      
        "department": "Product",
        "email": "jane.smith@sample.com"
    }
]

print("\n===== EMPLOYEE DIRECTORY =====\n")

for emp in employees:
    print(f"Name: {emp['name']}")
    print(f"Position: {emp['position']}")
    print(f"Department: {emp['department']}")
    print(f"Email: {emp['email']}")
    print("\n")
    




