book = {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "pages": 464,
    "is_available": True
}

print("\n===== BOOK DETAILS =====\n")
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")
print(f"Pages: {book['pages']}")
print(f"Available: {book['is_available']}")


book["genre"] = "Software Engineering"

book["is_available"] = False

del book["pages"]

print("\n===== UPDATED BOOK DETAILS =====\n")

for key, value in book.items():
    print(f"{key.capitalize()}: {value}")
    