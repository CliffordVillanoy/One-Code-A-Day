def usd_to_php(amount):
    exchange_rate = 58.5  # Current approximate exchange rate
    return amount * exchange_rate

def main():
    print("Welcome to the Currency Converter!")
    print("1. USD to PHP")
    print("2. PHP to USD")
    print("3. Exit")
    print("Please select a conversion option:")
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            usd_amount = float(input("Enter amount in USD: "))
            php_amount = usd_to_php(usd_amount)
            print(f"{usd_amount} USD is equal to {php_amount:.2f} PHP")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            print("Exiting the converter.")
    else:
        print("Invalid choice.")
        print("Exiting the converter.") 
        print("Please try again.")
        return

if __name__ == "__main__":
    main()
    print("Thank you for using the Currency Converter!")
# The above code defines a simple currency converter that converts USD to PHP.
# It prompts the user to enter an amount in USD and displays the equivalent amount in PHP.
# The program handles invalid inputs gracefully and exits if the user enters an invalid choice or non-numeric value.
# The program also thanks the user for using the converter upon exit.