user = {
    "name": "Cliff",
    "role": "Junior SQA",
    "is_active": True,
    "interests": ["testing", "AI", "Automation"]
}

print(user["name" ])
print(user["interests"][1])

del user["is_active"]
print(user)
print(user.get("role", "Role not found"))
print(user.get("is_active", "Is Active not found"))
print(user.get("interests", "Interests not found"))
print(user.get("location", "Location not found"))
print(user.get("name", "Name not found"))
print(user.get("interests", ["No interests found"])[0])
print(user.get("interests", ["No interests found"])[1])
print(user.get("interests", ["No interests found"])[2])
print(user.get("interests", ["No interests found"])[3])
print(user.keys())
print(user.values())
print(user.items())
print(user.copy())
print(user.clear())
print(user) 
print(len(user))


