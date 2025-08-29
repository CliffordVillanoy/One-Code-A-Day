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
    print()
    print("===== END OF ITEM REPORT =====\n")

print("===== END OF INVENTORY REPORT =====\n")