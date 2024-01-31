#This is the main file, it will serve the user a command line user interface to allow them to interact with the software.
#In the backend, it will talk to the other python file, conversionLibrary to actually handle the currency conversion.
pip install forex-python
#If forex-python is not install so we need to install it first

from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    
    try:
        rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * rate
        return converted_amount
    except Exception as e:
        print(f"Error: {e}")
        return None

def display_menu():
    print("\n1. Convert from CAD to another currency")
    print("2. Convert from another currency to CAD")
    print("3. Exit")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("select from (1, 2, or 3): ")

        if choice == '1':
            amount = float(input("Enter the amount in CAD $: "))
            to_currency = input("Enter the currency code you want to convert: ").upper()
            converted_amount = convert_currency(amount, 'CAD', to_currency)

            if converted_amount is not None:
                print(f"{amount} CAD is equal to {converted_amount:.2f} {to_currency}")
            else:
                print("!!!ERROR!!!" 
                      "\nPlease check the currencies code and try again.")

        elif choice == '2':
            amount = float(input("Enter the amount: "))
            from_currency = input("Enter the currency code: ").upper()
            converted_amount = convert_currency(amount, from_currency, 'CAD')

            if converted_amount is not None:
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} CAD")
            else:
                print("!!!ERROR!!!"
                      "\nPlease check the currencies and try again.")

        elif choice == '3':
            print("THANK YOU"
                  "\nGoodbye!")
            break

        else:
            print("!!!Please select correct option!!!")
