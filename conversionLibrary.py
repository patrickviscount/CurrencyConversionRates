#This file will hold all of the conversion functions. Each function needs to take an input that is the dollar amount, and then be able to either change the dollar value into canadian dollars
#or out of canadian dollars into the specified currency type.

#Demo function for the british pound
def britishPound(amount, option):
    # Define the exchange rates
    cad_to_gbp = 0.58  # 1 CAD = 0.58 GBP
    gbp_to_cad = 1.72  # 1 GBP = 1.72 CAD

    # Convert based on the option
    if option == 1:
        # Convert from CAD to GBP
        return amount * cad_to_gbp
    elif option == 2:
        # Convert from GBP to CAD
        return amount * gbp_to_cad
    else:
        return "Invalid option. Please enter 1 or 2."
