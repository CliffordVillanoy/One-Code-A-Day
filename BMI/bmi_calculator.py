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


