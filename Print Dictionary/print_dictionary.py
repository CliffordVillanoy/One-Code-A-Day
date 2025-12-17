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
    print("-" * 20)
    print(f"Type of {key}: {type(value)}")
    print("-" * 20)
    print(f"Length of {key}: {len(str(value))}")
    print("-" * 20)
print("\n===== End of Book Details =====\n")

print("\n===== UPDATED BOOK DETAILS =====\n")
for key, value in third_book.items():
    print(f"{key.capitalize()}: {value}")
    print("-" * 20)
    print(f"Type of {key}: {type(value)}")
    print("-" * 20)
    print(f"Length of {key}: {len(str(value))}")
    print("-" * 20)
    print(f"Is '{key}' a string? {isinstance(value, str)}")
    print("-" * 20)
    print(f"Is '{key}' an integer? {isinstance(value, int)}")
    print("-" * 20)
    print(f"Is '{key}' a float? {isinstance(value, float)}")
    print("-" * 20)
    print(f"Is '{key}' a boolean? {isinstance(value, bool)}")
    print("-" * 20)
    print(f"Is '{key}' a list? {isinstance(value, list)}")
    print("-" * 20)
    print(f"Is '{key}' a dictionary? {isinstance(value, dict)}")
    print("-" * 20)
    print(f"Is '{key}' a tuple? {isinstance(value, tuple)}")
    print("-" * 20)
    print(f"Is '{key}' a set? {isinstance(value, set)}")
    print("-" * 20)
    print(f"Is '{key}' a range? {isinstance(value, range)}")
    print("-" * 20)
    print(f"Is '{key}' NoneType? {value is None}")
    print("-" * 20)   
    print(f"Is '{key}' a complex number? {isinstance(value, complex)}")
    print("-" * 20)
    print(f"Is '{key}' a frozenset? {isinstance(value, frozenset)}")
    print("-" * 20)
    print(f"Is '{key}' a bytes? {isinstance(value, bytes)}")
    print("-" * 20)
    print(f"Is '{key}' a bytearray? {isinstance(value, bytearray)}")
    print("-" * 20)
    print(f"Is '{key}' a memoryview? {isinstance(value, memoryview)}")
    print("-" * 20)
    print(f"Is '{key}' a callable? {callable(value)}")
    print("-" * 20)
    print(f"Is '{key}' an object? {isinstance(value, object)}")
    print("-" * 20)
    print(f"Is '{key}' iterable? {hasattr(value, '__iter__')}")
    print("-" * 20)
    print(f"Is '{key}' hashable? {hasattr(value, '__hash__')}")
    print("-" * 20)
print("===== End of Book Details =====\n")

print("\n===== End of Program =====\n")