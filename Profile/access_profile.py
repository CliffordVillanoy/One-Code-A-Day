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



