math_grade_str = input("Enter your Math grade: ")
english_grade_str = input("Enter your English grade: ")
science_grade_str = input("Enter your Science grade: ")

math_grade = int(math_grade_str)
english_grade = int(english_grade_str)
science_grade = int(science_grade_str)

print(f"Math grade: {math_grade}")
print(f"English grade: {english_grade}")
print(f"Science grade: {science_grade}")

def get_letter_grade(score):
    if score >= 75:
        return "A"
    elif score > 50:
        return "B"
    else:
        return "C"

print("\n===== GRADE CONVERSION RESULTS =====\n")
print("Subject Grades:")
print(f"Math: {math_grade} -> {get_letter_grade(math_grade)}")
print(f"English: {english_grade} -> {get_letter_grade(english_grade)}")
print(f"Science: {science_grade} -> {get_letter_grade(science_grade)}")
print(f"Math: {get_letter_grade(math_grade)}")
print(f"English: {get_letter_grade(english_grade)}")
print(f"Science: {get_letter_grade(science_grade)}")
print(f"Average: {get_letter_grade((math_grade + english_grade + science_grade) // 3)}")
print(f"Final Decision: {get_letter_grade((math_grade + english_grade + science_grade) // 3)}")
print("\n===== GRADE CONVERSION RESULTS =====\n")
print(f"Thank you for using the grade conversion program!")