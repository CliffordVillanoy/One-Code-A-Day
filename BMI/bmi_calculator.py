print ("Enter age: ")
age = int(input())

print ("Enter weight: ")
weight = float(input())

print ("Enter height: ")
height = float(input())

print ("Enter weight units (kg or lbs): ")
weight_units = str(input())

print ("Enter height units (m or cm): ")
height_units = str(input())

print ("Enter Imperial or Metric: ")
system_measure = str(input())

if system_measure =="Imperial":
    if weight_units == "lbs":
        weight = weight * 0.4536
    if height_units == "cm":
        height = height *0.01
elif system_measure == "Metric":
    if weight_units == "kg":
        weight = weight * 2.2046
    if height_units == "m":
        height = height * 100
print ("Your weight is: ", weight, "kg")
print ("Your height is: ", height, "cm")
bmi = weight / (height * height)
print ("Your BMI is: ", bmi)
print ("Your BMI category is: ", end='')
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <24.9:
    print("Normal weight")
elif 25 <= bmi <29.9:
    print("Overweight")
elif bmi >= 30:
    print ("Obese")
    
elif system_measure not in ["Imperial", "Metric"]:
    print("Invalid measurement system")
elif weight_units not in ["kg", "lbs"]:
    print("Invalid weight units")
elif height_units not in ["m", "cm"]:
    print("Invalid height units")
    
else:
    print("Enter valid age, weight, height, and measurement system.")

print("End of BMI Calculator")
print("BMI Calculator")
print("This program calculates the Body Mass Index (BMI) based on user input for age, weight")
print("height, and the measurement system (Imperial or Metric).")
print("It then categorizes the BMI into Underweight, Normal weight, Overweight, or Obese.")

