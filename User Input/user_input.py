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
print("Full Name Uppercase:", first_name.upper() + " " + last_name.upper())
print("Full Name Lowercase:", first_name.lower() + " " + last_name.lower())
print("Full Name Titlecase:", first_name.title() + " " + last_name.title())
print("Full Name Capitalized:", first_name.capitalize() + " " + last_name.capitalize())
print("First Name is Alphabetic:", first_name.isalpha())
print("Last Name is Alphabetic:", last_name.isalpha())
print("First Name is Alphanumeric:", first_name.isalnum())
print("Last Name is Alphanumeric:", last_name.isalnum())
print("First Name is Lowercase:", first_name.islower())
print("Last Name is Lowercase:", last_name.islower())
print("First Name is Uppercase:", first_name.isupper())
print("Last Name is Uppercase:", last_name.isupper())
print("First Name is Titlecase:", first_name.istitle())
print("Last Name is Titlecase:", last_name.istitle())
print("First Name is Printable:", first_name.isprintable())
print("Last Name is Printable:", last_name.isprintable())
print("First Name is Space:", first_name.isspace())
print("Last Name is Space:", last_name.isspace())

# The above code takes the user's first and last name as input and prints a welcome message.
# The above code prints the data types of the variables first_name, last_name, and full name.

