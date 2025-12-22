first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
print(f"Welcome {first_name} {last_name}!")
print(f"You are {age} years old.")

math_grade_str = input("Enter your Math grade: ")
english_grade_str = input("Enter your English grade: ")
science_grade_str = input("Enter your Science grade: ")
history_grade_str = input("Enter your History grade: ")
computer_grade_str = input("Enter your Computer Science grade: ")

# Convert grades to integers immediately after input
math_grade = int(math_grade_str)
english_grade = int(english_grade_str)
science_grade = int(science_grade_str)
history_grade = int(history_grade_str)
computer_grade = int(computer_grade_str)

# Print grades
print(f"Math grade: {math_grade}")
print(f"English grade: {english_grade}")
print(f"Science grade: {science_grade}")
print(f"History grade: {history_grade}")
print(f"Computer Science grade: {computer_grade_str}") # Computer Science grade is not used in calculations

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
#History grade
if history_grade <= 50: # Now comparing integers
    print("You need to improve your History grade.")
elif history_grade >= 75:
    print("You are doing great in History!")
else:
    print("You are doing well in History!")

if computer_grade <= 50: # Now comparing integers
    print("You need to improve your Computer Science grade.")
elif computer_grade >= 75:
    print("You are doing great in Computer Science!")
else:
    print("You are doing well in Computer Science!") 
print("Thank you for using the grade input system!")
            
# Calculate average of the four subjects
import statistics
grades = [math_grade, english_grade, science_grade, history_grade, computer_grade]

average = statistics.mean(grades)
print(f"Your average grade is: {average}")
if average <= 50:
    print("You need to improve your grades.")
elif average > 50 and average < 75:
    print("You are doing well, but there is room for improvement.")
elif average >= 75:
    print("You are doing great!")
# The above code takes the user's first and last name, age, and grades in Math, English, and Science as input.
# It then prints a welcome message and the grades entered by the user.