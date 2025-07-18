"""
employee_directory.py

This script simulates a directory entry for an employee using core Python data types.

Casing used: snake_case
"""

employee_name = "John Doe"
employee_age = "25"
is_full_time = True
hourly_rate = 20.50

contact_info = {
    "email": "john.doe@example.com" ,
    "phone": "123-456-7890"
}
skills = ["Python", "Data Analysis", "Machine Learning"]

print("\n===== EMPLOYEE DIRECTORY ENTRY =====\n")

print(f"Name: {employee_name} - Type: {type(employee_name)}")
print(f"Age: {employee_age} - Type: {type(employee_age)}")
print(f"Full Time: {is_full_time} - Type: {type(is_full_time)}")
print(f"Hourly Rate: ${hourly_rate} - Type: {type(hourly_rate)}")
print(f"Email: {contact_info['email']} - Type: {type(contact_info['email'])}")
print(f"Phone: {contact_info['phone']} - Type: {type(contact_info['phone'])}")

print(f"Skills: {skills} - Type: {type(skills)}")
print(f"Skills Count: {len(skills)} - Type: {type(len(skills))}")
print(f"Contact Info: {contact_info} - Type: {type(contact_info)}")

print(f"Contact Info Keys: {list(contact_info.keys())} - Type: {type(list(contact_info.keys()))}")
print(f"Contact Info Values: {list(contact_info.values())} - Type: {type(list(contact_info.values()))}")

print("\n===== END OF ENTRY =====\n")
