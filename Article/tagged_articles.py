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

# Step 1: Create a dictionary to hold articles by tags
# Step 4: Add a new article to a tag
new_article = input("Enter a new article title to add under the selected tag: ").strip()

if selected_tag in tagged_articles:
    tagged_articles[selected_tag].append(new_article)
    print(f"Added '{new_article}' under #{selected_tag.upper()}.")
else:
    print(f"Tag #{selected_tag} does not exist. Article not added.")
# Step 5: Print updated articles under the selected tag

print(f"\nUpdated articles under #{selected_tag.upper()}:")
if selected_tag in tagged_articles:
    for article in tagged_articles[selected_tag]:
        print(f"  - {article}") 
else:
    print("No articles found for that tag.")
                        
print ("End of Article")