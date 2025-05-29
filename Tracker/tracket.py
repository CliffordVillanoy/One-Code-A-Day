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
]

print("\nInventory Report")
for item in inventory:
    if item["is_active"]:
        continue

    item_name = item["item_name"]
    unit_price = item["unit_price"]
    quantity_stocks = item["quantity_stocks"]
    total_value = unit_price * quantity_stocks

    print(f"Item: {item_name}")
    print(f"Unit Price: ${unit_price:.2f}", "Type:", type(unit_price))
    print(f"Quantity in Stock: {quantity_stocks}", "Type:", type(quantity_stocks))
    print(f"  Total Stock Value: ₱{total_value:.2f}")
    print()

print("===== END OF INVENTORY REPORT =====\n")