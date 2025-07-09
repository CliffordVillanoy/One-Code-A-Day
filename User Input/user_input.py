first_name  = input("Enter your first name: ")
last_name   = input("Enter your last name: ")
print (f"Welcome {first_name} {last_name}!")
# The above code takes the user's first and last name as input and prints a welcome message.
# The input() function is used to take input from the user.
# The f-string is used to format the string and insert the values of first_name and last_name into the string.

print("Data Types:")
print("First Name:", type(first_name)) 
print("Last Name:", type(last_name))
print("Full Name:", type(first_name + " " + last_name))
print("First Name:", first_name)
print("Last Name:", last_name)
print("Full Name:", first_name + " " + last_name)
print("First Name Length:", len(first_name))
print("Last Name Length:", len(last_name))
print("Full Name Length:", len(first_name + last_name))
# The above code prints the data types of the variables first_name, last_name, and full name.

