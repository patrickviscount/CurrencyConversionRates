#This is the main file, it will serve the user a command line user interface to allow them to interact with the software.
#In the backend, it will talk to the other python file, conversionLibrary to actually handle the currency conversion.

import conversionLibrary
#How to use the functions in the library
#result = conversionLibrary.britishPound(100, 1) 


def main():
    options = ["American Dollar", "Mexican Peso", "British Pound"]
    print(f"Welcome, what currency do you want to select: {options}!")
    #command line Ui menu here, 1. American dollar, 2. peso, etc
    print(f"Would you like to convert into Canadian dollars or not?")
    #command line Ui menu here, 1. into, 2. out of



if __name__ == "__main__":
    main()
