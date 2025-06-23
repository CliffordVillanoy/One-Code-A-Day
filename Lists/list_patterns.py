grades = [55, 67, 80]
print(grades[0])
print (grades[1])

grades[2] = 80
grades.append(92)

print(grades)
print(grades[2:])  # Slicing to get elements from index 2 to the end 
print(grades[1:3])  # Slicing to get elements from index 1 to index 2 (exclusive)       
print(grades[:2])  # Slicing to get elements from the start to index 1 (exclusive)
print(grades[-1])  # Accessing the last element using negative indexing

print(grades[-2:])  # Slicing to get the last two elements  
print(grades[-3:-1])  # Slicing to get elements from the third last to the second last element
print(grades[-3:])  # Slicing to get the first three elements          