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

print(f"Name: {product_name} | Type: {type(product_name)}")
print(f"Price: {product_price} | Type: {type(product_price)}")
print(f"Quantity: {stock_quantity} | Type: {type(stock_quantity)}")
print(f"Available: {is_available} | Type: {type(is_available)}")
print(f"Details: {product_details} | Type: {type(product_details)}")
print(f"Tags: {product_tags} | Type: {type(product_tags)}")

print("\n===== END OF PRODUCT INFORMATION =====\n")


