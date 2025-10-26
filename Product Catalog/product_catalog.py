"""
product_catalog.py

This script simulates a simple product entry using Python's core data types.
Naming style used: snake_case (PEP8 standard)
"""

product_name = "Wireless Mouse"
product_price = 49.99
stock_quantity = 150
is_available = True

product_details = {
    "sku": "WM12345",
    "manufacturer": "TechGadgets Inc.",
}
product_tags = ["electronics", "accessories", "wireless"]  

print("\n===== PRODUCT INFORMATION =====\n")

print(f"Product Name: {product_name}")
print(f"Price: ${product_price:.2f}")
print(f"Stock Quantity: {stock_quantity}")
print(f"Available: {'Yes' if is_available else 'No'}")
print(f"SKU: {product_details['sku']}")
print(f"Manufacturer: {product_details['manufacturer']}")   
print(f"Tags: {', '.join(product_tags)}")
print("\n===== PRODUCT CATEGORIES =====\n")
product_categories = ["Computers", "Peripherals", "Input Devices"]
for category in product_categories:
    print(f"- {category}")
    print("-" * 20)
    print(f"Category: {category}")
    print(f"Type: {type(category)}")
    print(f"Length: {len(category)}")
    print(f"Uppercase: {category.upper()}")
    print(f"Lowercase: {category.lower()}")
    print(f"Is Alphanumeric: {category.isalnum()}")
    print(f"Is Alphabetic: {category.isalpha()}")
    print(f"Is Digit: {category.isdigit()}")
    print(f"Is Title: {category.istitle()}")
    print(f"Is Printable: {category.isprintable()}")
    print(f"Is Space: {category.isspace()}")
    print("-" * 20)
    print("\n===== END OF PRODUCT CATEGORIES =====\n")    
    print("Character Analysis:")
    print("-" * 20)

    [print(f"Character '{char}': Type: {type(char)}, Ordinal: {ord(char)}") for char in category]
    print("\n===== END OF PRODUCT CATEGORIES =====\n")
print("\n===== PRODUCT REVIEWS =====\n")
print("\n===== PRODUCT DETAILS =====\n")



print("\n===== END OF PRODUCT INFORMATION =====\n")


