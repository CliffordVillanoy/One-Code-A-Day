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
print("Tags:", ", ".join(product_tags)) 



print("\n===== END OF PRODUCT INFORMATION =====\n")


