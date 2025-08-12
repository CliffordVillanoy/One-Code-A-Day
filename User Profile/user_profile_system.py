"""
user_profile_system.py

This script simulates the creation of a user profile using Python's core data types and naming conventions.

Casing: snake_case (Python's PEP8 recommendation for variable and function names)
"""
user_name = "John Doe" # String
user_age = 30 # Integer
user_rating = 4.7   # Float
is_verified = True  # Boolean

user_hobbies = ["reading", "coding", "playing video games"] # List
user_contact = {
    "email": "john.mckinley@examplepetstore.com",
    "phone": "123-456-7890"
} # Dictionary

print("\n===== USER PROFILE =====\n")

print(f"Name: {type(user_name)}")
print(f"Age: {type(user_age)}")
print(f"Rating: {type(user_rating)}")
print(f"Is Verified: {type(is_verified)}")
print(f"Hobbies: {type(user_hobbies)}")
print(f"Email Address: {type(user_contact['email'])}")
print(f"Phone Number: {type(user_contact['phone'])}")
print(f"Full Name: {user_name}")
print(f"Age: {user_age}")
print(f"Rating: {user_rating}")
print(f"Is Verified: {is_verified}")
print(f"Hobbies: {', '.join(user_hobbies)}")
print(f"Contact Email: {user_contact['email']}")
print(f"Contact Phone: {user_contact['phone']}")

print("\n===== END OF USER PROFILE =====\n")
# The script creates a user profile with various attributes and prints them in a formatted manner.
# The script uses Python's core data types: string, integer, float, boolean, list, and dictionary.
# The script also demonstrates the use of f-strings for formatted output.
