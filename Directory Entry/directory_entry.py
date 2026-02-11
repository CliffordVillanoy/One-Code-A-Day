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
print(f"Skills List Pop: {skills.pop()} - Type: {type(skills.pop())}")
print(f"Skills List After Pop: {skills} - Type: {type(skills)}")
print(f"Skills List Insert 'SQL' at Index 3: {skills.insert(3, 'SQL')} - Type: {type(skills.insert(3, 'SQL'))}")
print(f"Skills List After Insert: {skills} - Type: {type(skills)}")
print(f"Skills List Remove 'Python': {skills.remove('Python')} - Type: {type(skills.remove('Python'))}")
print(f"Skills List After Remove: {skills} - Type: {type(skills)}")
print(f"Skills List Clear: {skills.clear()} - Type: {type(skills.clear())}")
print(f"Skills List After Clear: {skills} - Type: {type(skills)}")
print(f"Contact Info Type: {type(contact_info)}")
print(f"Contact Info Items: {list(contact_info.items())} - Type: {type(list(contact_info.items()))}")
print(f"Contact Info Get Email: {contact_info.get('email')} - Type: {type(contact_info.get('email'))}")
print(f"Contact Info Get Phone: {contact_info.get('phone')} - Type: {type(contact_info.get('phone'))}")
print(f"Contact Info Get Address: {contact_info.get('address', 'N/A')} - Type: {type(contact_info.get('address', 'N/A'))}")
print(f"Is Full Time Type: {type(is_full_time)}")
print(f"Is Full Time Value: {is_full_time} - Type: {type(is_full_time)}")
print(f"Is Full Time Not: {not is_full_time} - Type: {type(not is_full_time)}")
print(f"Is Full Time And True: {is_full_time and True} - Type: {type(is_full_time and True)}")
print(f"Is Full Time Or False: {is_full_time or False} - Type: {type(is_full_time or False)}")
print(f"Is Full Time Equals True: {is_full_time == True} - Type: {type(is_full_time == True)}")
print(f"Is Full Time Not Equals False: {is_full_time != False} - Type: {type(is_full_time != False)}")
print(f"Hourly Rate Type: {type(hourly_rate)}")
print(f"Hourly Rate Value: {hourly_rate} - Type: {type(hourly_rate)}")
print(f"Hourly Rate Plus 5: {hourly_rate + 5} - Type: {type(hourly_rate + 5)}")
print(f"Hourly Rate Minus 10: {hourly_rate - 10} - Type: {type(hourly_rate - 10)}")
print(f"Hourly Rate Times 2: {hourly_rate * 2} - Type: {type(hourly_rate * 2)}")
print(f"Hourly Rate Divided By 3: {hourly_rate / 3} - Type: {type(hourly_rate / 3)}")
print(f"Hourly Rate Exponentiated To 4: {hourly_rate ** 4} - Type: {type(hourly_rate ** 4)}")
print(f"Hourly Rate Modulo 7: {hourly_rate % 7} - Type: {type(hourly_rate % 7)}")
print(f"Hourly Rate Floor Division By 3: {hourly_rate // 3} - Type: {type(hourly_rate // 3)}")
print(f"Employee Name Type: {type(employee_name)}")
print(f"Employee Name Value: {employee_name} - Type: {type(employee_name)}")
print(f"Employee Name Uppercase: {employee_name.upper()} - Type: {type(employee_name.upper())}")
print(f"Employee Name Lowercase: {employee_name.lower()} - Type: {type(employee_name.lower())}")
print(f"Employee Name Capitalize: {employee_name.capitalize()} - Type: {type(employee_name.capitalize())}")
print(f"Employee Name Title: {employee_name.title()} - Type: {type(employee_name.title())}")
print(f"Employee Name Split: {employee_name.split()} - Type: {type(employee_name.split())}")
print(f"Employee Name Replace 'John' with 'Jane': {employee_name.replace('John', 'Jane')} - Type: {type(employee_name.replace('John', 'Jane'))}")
print(f"Employee Name Startswith 'John': {employee_name.startswith('John')} - Type: {type(employee_name.startswith('John'))}")
print(f"Employee Name Endswith 'Doe': {employee_name.endswith('Doe')} - Type: {type(employee_name.endswith('Doe'))}")
print(f"Employee Name Find 'Doe': {employee_name.find('Doe')} - Type: {type(employee_name.find('Doe'))}")
print(f"Employee Name Index 'Doe': {employee_name.index('Doe')} - Type: {type(employee_name.index('Doe'))}")
print(f"Employee Name Count 'o': {employee_name.count('o')} - Type: {type(employee_name.count('o'))}")
print(f"Employee Name Centered: {employee_name.center(20)} - Type: {type(employee_name.center(20))}")
print(f"Employee Name Justified Left: {employee_name.ljust(20)} - Type: {type(employee_name.ljust(20))}")
print(f"Employee Name Justified Right: {employee_name.rjust(20)} - Type: {type(employee_name.rjust(20))}")
print(f"Employee Name Zfill: {employee_name.zfill(20)} - Type: {type(employee_name.zfill(20))}")
print(f"Employee Name Encode: {employee_name.encode()} - Type: {type(employee_name.encode())}")


print("\n===== END OF ENTRY =====\n")
