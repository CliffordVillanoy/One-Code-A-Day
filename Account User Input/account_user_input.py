"""
bank_account_simulator.py

This script simulates basic bank account transactions using Python variables, types, and control structures.

Naming Convention: snake_case (PEP8)
"""

from datetime import time


account_holder =  {
    "name": "John Doe",
    "account_number": "123456789",
    "balance": 1000.0, #Float
    "is_active": True #Boolean
}

transactions = [2000.00, -300.00, 210.00, -70.00]  # List to store transaction history

print("\n===== BANK ACCOUNT TRANSACTION LOG =====\n")

for txn in transactions:
    if not account_holder["is_active"]:
        print(f"Account {account_holder['account_number']} is inactive. Cannot process transactions.")
        break

    txn_type = "Deposit" if txn > 0 else "Withdrawal"
    projected_balance = account_holder["balance"] + txn

    if projected_balance < 0:
        print (f"{txn_type} of {abs(txn):.2f} failed. Insufficient funds for this transaction.")

    else:
        account_holder["balance"] = projected_balance
        print(f"{txn_type} of {abs(txn):.2f} successful.")
        print(f"New balance: {account_holder['balance']:.2f}")
        print(f"Transaction Type: {txn_type}")
        print(f"Account Holder: {account_holder['name']}")
        print(f"Account Number: {account_holder['account_number']}")
        print(f"Transaction ID: {id(txn)}")
        print(f"Transaction Time: {time(12, 0, 0)}")
        print("-" * 40)
        print(f"Transaction Details: {txn} - Type: {type(txn)}")
        print(f"Projected Balance: {projected_balance:.2f} - Type: {type(projected_balance)}")
        print(f"Account Holder Name: {account_holder['name']} - Type: {type(account_holder['name'])}")
        print(f"Account Number: {account_holder['account_number']} - Type: {type (account_holder['account_number'])}")
        print(f"Account Balance: {account_holder['balance']:.2f} - Type: {type(account_holder['balance'])}")
        print(f"Is Account Active: {account_holder['is_active']} - Type: {type(account_holder['is_active'])}")
        print(f"Transaction History: {transactions} - Type: {type(transactions)}")
        print(f"Transaction Type: {txn_type} - Type: {type(txn_type)}")
        print(f"Transaction Details: {txn} - Type: {type(txn)}")
        print(f"Projected Balance: {projected_balance:.2f} - Type: {type(projected_balance)}")
        print(f"Account Holder Name: {account_holder['name']} - Type: {type(account_holder['name'])}")
        print(f"Account Number: {account_holder['account_number']} - Type: {type(account_holder['account_number'])}")
        print(f"Account Balance: {account_holder['balance']:.2f} - Type: {type(account_holder['balance'])}")
        print(f"Is Account Active: {account_holder['is_active']} - Type: {type(account_holder['is_active'])}")
        print(f"Transaction History: {transactions} - Type: {type(transactions)}")
        print(f"Transaction Type: {txn_type} - Type: {type(txn_type)}")
        print(f"Transaction Time: {time(12, 0, 0)} - Type: {type(time(12, 0, 0))}")
        print(f"Transaction ID: {id(txn)} - Type: {type(id(txn))}")
        print(f"Account Holder Info: {account_holder} - Type: {type(account_holder)}")
        print(f"Account Holder Keys: {list(account_holder.keys())} - Type: {type(list(account_holder.keys()))}")
        print(f"Account Holder Values: {list(account_holder.values())} - Type: {type(list(account_holder.values()))}")
        print(f"Account Holder Items: {list(account_holder.items())} - Type: {type(list(account_holder.items()))}")
        print(f"Account Holder Length: {len(account_holder)} - Type: {type(len(account_holder))}")
        print(f"Account Holder Type: {type(account_holder)} - Type: {type(type(account_holder))}")
        print(f"Account Holder Hash: {hash(id(account_holder))} - Type: {type(hash(id(account_holder)))}")
        print(f"Account Holder ID: {id(account_holder)} - Type: {type(id(account_holder))}")
        print(f"Account Holder Str: {str(account_holder)} - Type: {type(str(account_holder))}")
        print(f"Account Holder Repr: {repr(account_holder)} - Type: {type(repr(account_holder))}")
        print(f"Account Holder Dir: {dir(account_holder)} - Type: {type(dir(account_holder))}")
        print(f"Fallback Transaction Value: {txn or 0} - Type: {type(txn or 0)}")
        print(f"Absolute Transaction Value: {abs(txn)} - Type: {type(abs(txn))}")
        print(f"Rounded Transaction Value: {round(txn, 2)} - Type: {type(round(txn, 2))}")
        
        print("-" * 40) 
        print(f"Transaction Summary for {account_holder['name']}:")
        print(f"  Account Number: {account_holder['account_number']}")
        print(f"  Final Balance: {account_holder['balance']:.2f}")


print("===== END OF TRANSACTION LOG =====")
print(f"Final Balance for {account_holder['name']}: {account_holder['balance']:.2f}\n")