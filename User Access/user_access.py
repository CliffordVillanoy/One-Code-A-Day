"""
access_control_system.py

Simulates a basic access control system based on user data using core Python constructs.
"""

users = [

    {
        "username": "test01",
        "age": 25,
        "is_verified": True
    },

    {
        "username": "test02",
        "age": 20,
        "is_verified": True
    }, 
        {
        "username": "test03",
        "age": 17,
        "is_verified": True
    }

]

print("\n===== ACCESS CONTROL CHECK =====\n")

for user in users:
    username = user["username"]
    age = user["age"]
    is_verified = user["is_verified"]

    if age >= 18 and is_verified:
        print(f"Access granted for {username}.")
    elif age < 18:
        print(f"Access denied for {username} - Reason: Underage.")
    elif not is_verified:
        print(f"Access denied for {username} - Reason: Not verified")
    elif age >= 18 and not is_verified:
        print(f"Access denied for {username} - Reason: Not verified.")
    elif age < 18 and not is_verified:
        print(f"Access denied for {username} - Reason: Underage and not verified.")
    elif age >= 18 and is_verified:
        print(f"Access granted for {username} - Reason: Verified and of age.")
    elif age < 18 and is_verified:
        print(f"Access denied for {username} - Reason: Underage but verified.")
    else:
        print(f"Access denied for {username} - Reason: Unknown.")

# Step 1: Create a dictionary to hold articles by tags
tagged_articles = {
        "python": [
        "Understanding Python Dictionaries",
        "Python List Comprehensions Explained",
        "How to Use Generators in Python"
    ],
    "web_dev": [
        "HTML & CSS Crash Course",
        "JavaScript for Beginners",
        "Responsive Design Tips"
    ],
    "data_science": [
        "Data Analysis with Pandas",
        "Machine Learning with Scikit-Learn",
        "Deep Learning with TensorFlow"
    ]
    " machine_learning": [
        "Supervised Learning",
        "Unsupervised Learning",
        "Reinforcement Learning"
    ]
    "ai": [
        "Intro to Neural Networks",
        "What is Machine Learning?",
        "Natural Language Processing Basics"
    ]
    "cloud_computing": [
        "Getting Started with AWS",
        "Azure Fundamentals",
        "Google Cloud Platform Basics"
    ]
        "cyber_security": [
        "Understanding Cyber Threats",
        "Best Practices for Online Security",
        "Introduction to Ethical Hacking"
    ]
        "game_dev": [
        "Unity for Beginners",
        "Game Design Principles",
        "Creating 2D Games with Godot"
    ]
}

print("\n===== END =====\n")