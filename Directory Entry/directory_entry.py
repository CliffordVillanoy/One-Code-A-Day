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

print (f"Skills List: {skills} - Type: {type(skills)}")
print(f"Skills List Length: {len(skills)} - Type: {type(len(skills))}")
print(f"Skills List First Element: {skills[0]} - Type: {type(skills[0])}")
print(f"Skills List Last Element: {skills[-1]} - Type: {type(skills[-1])}")
print(f"Skills List Sliced: {skills[1:3]} - Type: {type(skills[1:3])}")
print(f"Skills List Reversed: {skills[::-1]} - Type: {type(skills[::-1])}")
print(f"Skills List Sorted: {sorted(skills)} - Type: {type(sorted(skills))}")
print(f"Skills List Reversed Sorted: {sorted(skills, reverse=True)} - Type: {type(sorted(skills, reverse=True))}")
print(f"Skills List Count of 'Python': {skills.count('Python')} - Type: {type(skills.count('Python'))}")
print(f"Skills List Index of 'Data Analysis': {skills.index('Data Analysis')} - Type: {type(skills.index('Data Analysis'))}")
print(f"Skills List Append 'SQL': {skills.append('SQL')} - Type: {type(skills.append('SQL'))}")
print(f"Skills List After Append: {skills} - Type: {type(skills)}")
print("\n===== END OF ENTRY =====\n")
