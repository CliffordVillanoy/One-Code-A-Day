def convert_currency():
    print("Welcome to the Currency Converter!")

    while True:
        try:
            amount = float(input("Enter the amount you want to convert: "))
            if amount <= 0:
                print("Amount must be a positive number. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    print("\nAvailable currencies:")
    print("1. USD (United States Dollar)")
    print("2. EUR (Euro)")
    print("3. GBP (British Pound)")
    print("4. JPY (Japanese Yen)")
    print("5. CAD (Canadian Dollar)")
    print("6. AUD (Australian Dollar)")
    print("7. PHP (Philippine Peso)")

    exchange_rates = {
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "PHP": {"USD": 0.017, "EUR": 0.016, "GBP": 0.014, "JPY": 2.70, "CAD": 0.023, "AUD": 0.026, "PHP": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR ": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "PHP": {"USD": 0.017, "EUR": 0.016, "GBP": 0.013, "JPY": 2.7, "CAD": 0.99, "AUD": 1.05, "PHP": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "PHP": {"USD": 0.017, "EUR": 0.016, "GBP": 0.014, "JPY": 2.70, "CAD": 0.023, "AUD": 0.026, "PHP": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "PHP": {"USD": 0.017, "EUR": 0.016, "GBP": 0.014, "JPY": 2.70, "CAD": 0.023, "AUD": 0.026, "PHP": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "PHP": {"USD": 0.017, "EUR": 0.016, "GBP": 0.014, "JPY": 2.70, "CAD": 0.023, "AUD": 0.026, "PHP": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "EUR": {"USD": 1.07, "GBP": 0.85, "JPY": 168.50, "CAD": 1.47, "AUD": 1.62, "PHP": 62.80, "EUR": 1.0},
        "GBP": {"USD": 1.27, "EUR": 1.18, "JPY": 198.00, "CAD": 1.73, "AUD": 1.91, "PHP": 74.00, "GBP": 1.0},
        "JPY": {"USD": 0.0064, "EUR": 0.0059, "GBP": 0.0051, "CAD": 0.0087, "AUD": 0.0096, "PHP": 0.37, "JPY": 1.0},
        "CAD": {"USD": 0.73, "EUR": 0.68, "GBP": 0.58, "JPY": 114.00, "AUD": 1.10, "PHP": 42.80, "CAD": 1.0},
        "PHP": {"USD": 0.017, "EUR": 0.016, "GBP": 0.014, "JPY": 2.70, "CAD": 0.023, "AUD": 0.026, "PHP": 1.0},
        "USD": {"EUR": 0.93, "GBP": 0.79, "JPY": 156.80, "CAD": 1.37, "AUD": 1.51, "PHP": 58.50, "USD": 1.0},
        "AUD": {"USD": 0.66, "EUR": 0.62, "GBP": 0.52, "JPY": 103.00, "CAD": 0.91, "PHP": 38.90, "AUD": 1.0}
    }

    while True:
        from_currency_input = input("Enter the currency you want to convert from (e.g., USD, EUR, PHP): ").upper()
        if from_currency_input in exchange_rates:
            break
        else:
            print("Invalid currency. Please choose from the available options.")

    while True:
        to_currency_input = input("Enter the currency you want to convert to (e.g., USD, EUR, PHP): ").upper()
        if to_currency_input in exchange_rates:
            break
        else:
            print("Invalid currency. Please choose from the available options.")

    if from_currency_input == to_currency_input:
        converted_amount = amount
        print(f"\n{amount:.2f} {from_currency_input} is equal to {converted_amount:.2f} {to_currency_input}.")
    else:
        try:
            rate = exchange_rates[from_currency_input][to_currency_input]
            converted_amount = amount * rate
            print(f"\n{amount:.2f} {from_currency_input} is equal to {converted_amount:.2f} {to_currency_input}.")
        except KeyError:
            print(f"Conversion from {from_currency_input} to {to_currency_input} is not available.")

if __name__ == "__main__":
    convert_currency()
