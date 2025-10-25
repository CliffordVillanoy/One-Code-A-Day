"""
inventory_tracker.py

This script simulates an inventory tracker using Python's core data types and proper naming conventions.

Naming Convention: snake_case
"""

inventory = [
    {
        "item_name": "Widget A",
        "unit_price": 19.99,
        "quantity_stocks": 100,
        "is_active": True,
    },
    
    {
        "item_name": "Widget B",
        "unit_price": 29.99,
        "quantity_stocks": 200,
        "is_active": False,
    },

    {
        "item_name": "Widget C",
        "unit_price": 15.49,
        "quantity_stocks": 150,
        "is_active": True,
    },
    {
        "item_name": "Widget D",
        "unit_price": 25.00,
        "quantity_stocks": 0,
        "is_active": False,
    },

    {
        "item_name": "Widget E",
        "unit_price": 39.99,
        "quantity_stocks": 50,
        "is_active": True,
    }
]

print("\nInventory Report")
for item in inventory:
    if item["is_active"]:
        continue

    item_name = item["item_name"]
    unit_price = item["unit_price"]
    quantity_stocks = item["quantity_stocks"]
    total_value = unit_price * quantity_stocks

    print(f"Length of Item Name: {len(item_name)}")
    print(f"Length of Unit Price: {len(str(unit_price))}")
    print(f"Length of Quantity Stocks: {len(str(quantity_stocks))}")
    print(f"Length of Total Value: {len(str(total_value))}")
    print("-" * 30)
    print(f"Is Active: {item['is_active']}")
    print(f"Type of Is Active: {type(item['is_active'])}")
    print("-" * 30)
    print(f"Item Name: {item_name}")
    print(f"Unit Price: ${unit_price:.2f}")
    print(f"Quantity Stocks: {quantity_stocks}")
    print(f"Total Value: ${total_value:.2f}")
    print("-" * 30)
    print(f"Item Name Uppercase: {item_name.upper()}")
    print(f"Item Name Lowercase: {item_name.lower()}")
    print(f"Item Name Titlecase: {item_name.title()}")
    print(f"Is Item Name Alphanumeric: {item_name.isalnum()}")
    print(f"Is Item Name Alphabetic: {item_name.isalpha()}")
    print(f"Is Item Name Digit: {item_name.isdigit()}")
    print(f"Is Item Name Title: {item_name.istitle()}")
    print(f"Is Item Name Printable: {item_name.isprintable()}")
    print(f"Is Item Name Space: {item_name.isspace()}")
    print("-" * 30)
    print(f"Item Report Generated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 30)
    print(f"Total Characters in Item Report: {len(item_name) + len(str(unit_price)) + len(str(quantity_stocks)) + len(str(total_value))}")
    print("-" * 30)
    print("===== END OF ITEM REPORT =====\n")

print("===== END OF INVENTORY REPORT =====\n")