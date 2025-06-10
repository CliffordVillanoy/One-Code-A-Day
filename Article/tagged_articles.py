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
    "ai": [
        "Intro to Neural Networks",
        "What is Machine Learning?",
        "Natural Language Processing Basics"
    ]
}

# Step 2: Print all articles under each tag
print("\n===== TAGGED ARTICLES =====\n")
for tag, articles in tagged_articles.items():
    print(f"#{tag.upper()}")
    for article in articles:
        print(f"  - {article}")
    print()

# Step 3: Simulate a filter
selected_tag = input("Enter a tag to filter articles (e.g., python, web_dev, ai): ").strip()

print(f"\nArticles under #{selected_tag.upper()}:")
if selected_tag in tagged_articles:
    for article in tagged_articles[selected_tag]:
        print(f"  - {article}")
else:
    print("No articles found for that tag.")