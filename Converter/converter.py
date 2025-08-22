def usd_to_php(amount):
    exchange_rate = 58.5  # Current approximate exchange rate
    return amount * exchange_rate

def main():
    print("Welcome to the Currency Converter!")
    print("1. USD to PHP")
    print("2. PHP to USD")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            usd_amount = float(input("Enter amount in USD: "))
            php_amount = usd_to_php(usd_amount)
            print(f"{usd_amount} USD is equal to {php_amount:.2f} PHP")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    else:
        print("Invalid choice.")
        return

if __name__ == "__main__":
    main()
    print("Thank you for using the Currency Converter!")

