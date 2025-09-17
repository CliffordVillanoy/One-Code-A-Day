first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
print(f"Welcome {first_name} {last_name}!")
print(f"You are {age} years old.")

math_grade_str = input("Enter your Math grade: ")
english_grade_str = input("Enter your English grade: ")
science_grade_str = input("Enter your Science grade: ")
history_grade_str = input("Enter your History grade: ")

# Convert grades to integers immediately after input
math_grade = int(math_grade_str)
english_grade = int(english_grade_str)
science_grade = int(science_grade_str)
history_grade = int(history_grade_str)

# Print grades
print(f"Math grade: {math_grade}")
print(f"English grade: {english_grade}")
print(f"Science grade: {science_grade}")
print(f"History grade: {history_grade}")

#Math grade
if math_grade <= 50: # Now comparing integers
    print("You need to improve your Math grade.")
elif math_grade >= 75:
    print("You are doing great in Math!")
else:
    print("You are doing well in Math!")
#English grade
if english_grade <= 50: # Now comparing integers
    print("You need to improve your English grade.")
elif english_grade >= 75:
    print("You are doing great in English!")
else:
    print("You are doing well in English!")
#Science grade
if science_grade <= 50: # Now comparing integers
    print("You need to improve your Science grade.")
elif science_grade >= 75:
    print("You are doing great in Science!")
else:
    print("You are doing well in Science!")

average = (math_grade + english_grade + science_grade + history_grade) / 4 # No need for int() here anymore
print(f"Your average grade is: {average}")
if average <= 50:
    print("You need to improve your grades.")
elif average > 50 and average < 75:
    print("You are doing well, but there is room for improvement.")
elif average >= 75:
    print("You are doing great!")
# The above code takes the user's first and last name, age, and grades in Math, English, and Science as input.
# It then prints a welcome message and the grades entered by the user.