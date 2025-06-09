first_book = {
    "title": "Clean Code",
    "author": "Robert C. Martin",
    "pages": 464,
    "is_available": True
}

second_book = {
    "title": "Refactoring",
    "author": "Martin Fowler",
    "pages": 448,
    "is_available": True
}

third_book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "pages": 464,
    "is_available": True
}

print("\n===== BOOK DETAILS =====\n")
print(f"Title: {first_book['title']}")
print(f"Author: {first_book['author']}")
print(f"Pages: {first_book['pages']}")
print(f"Available: {first_book['is_available']}")

print("\n===== BOOK DETAILS =====\n")
print(f"Title: {second_book['title']}")
print(f"Author: {second_book['author']}")
print(f"Pages: {second_book['pages']}")
print(f"Available: {second_book['is_available']}")

print("\n===== BOOK DETAILS =====\n")
print(f"Title: {third_book['title']}")
print(f"Author: {third_book['author']}")
print(f"Pages: {third_book['pages']}")
print(f"Available: {third_book['is_available']}")

third_book["genre"] = "Software Engineering"

third_book["is_available"] = False

del third_book["pages"]

print("\n===== UPDATED BOOK DETAILS =====\n")

for key, value in third_book.items():
    print(f"{key.capitalize()}: {value}")

print("\n===== End of Program =====\n")