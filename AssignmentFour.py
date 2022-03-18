""" This program prints the unit test results for the function
currency_converter. Then, it asks the user for their name, politely
greets them, and provides them with a menu. The user is prompted to
input an option, and the program provides an unique polite message to
the user's response accordingly.
"""
conversions = {
        "USD": 1,
        "EUR": .9,
        "CAD": 1.4,
        "GBP": .8,
        "CHF": .95,
        "NZD": 1.66,
        "AUD": 1.62,
        "JPY": 107.92
    }


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """ Convert source currency to target currency

    Args:
        quantity (float): the amount of in the original currency
        source_curr (str): represents the source currency
        target_curr (str): represents the currency after exchange
    """
    if source_curr not in conversions or target_curr not in conversions:
        raise KeyError
    else:
        converted_quantity = quantity \
                             * (1 / conversions[source_curr]) \
                             * conversions[target_curr]

    return converted_quantity


def unit_test():
    """ Check the following results from currency_converter:
    invalid source currency, invalid target currency, conversion from
    USD to GBP, conversion from CAD to USD, and conversion from EUR to
    CAD.
    """
    # invalid source currency -> KeyError
    try:
        currency_converter(100, "Galactic Credit Standard", "USD")
        print("FAIL: invalid source currency did not raise a KeyError")
    except KeyError:
        print("PASS: invalid source currency raised Key Error")
    except:
        print("FAIL: invalid source currency raised some other error")
    # invalid target currency -> KeyError
    try:
        currency_converter(100, "EUR", "Republic credits")
        print("FAIL: invalid target currency did not raise a KeyError")
    except KeyError:
        print("PASS: invalid target currency raised Key Error")
    except:
        print("FAIL: invalid target currency raised some other error")
    # conversion from USD (quantity = 5) to GBP -> 4.00
    if currency_converter(5, "USD", "GBP") == 4.00:
        print("PASS: Conversion from USD to GBP")
    else:
        print("FAIL: Conversion from USD to GBP")
    # conversion from CAD (quantity = 8.40) to USD --> 6.00
    if currency_converter(8.40, "CAD", "USD") == 6.00:
        print("PASS: Conversion from CAD to USD")
    else:
        print("FAIL: Conversion from CAD to USD")
    # conversion from EUR (quantity = 1.26) to CAD --> 1.96
    if currency_converter(1.26, "EUR", "CAD") == 1.96:
        print("PASS: Conversion from EUR to CAD")
    else:
        print("FAIL: Conversion from EUR to CAD")


def print_menu():
    """ Print out the nine choices and the numbers associated with
    them.
    """
    print("Main Menu")
    print("1 - Print Average Rent by Location and Property Type")
    print("2 - Print Minimum Rent by Location and Property Type")
    print("3 - Print Maximum Rent by Location and Property Type")
    print("4 - Print Min/Avg/Max by Location")
    print("5 - Print Min/Avg/Max by Property Type")
    print("6 - Adjust Location Filters")
    print("7 - Adjust Property Type Filters")
    print("8 - Load Data")
    print("9 - Quit")


def menu():
    """ Print out the options, ask user to input an option, catch
    errors, and provide a unique polite message for each selection
    until they enter 9 to indicate that they want to quit the menu.
    """
    show_menu = True
    while show_menu:
        print_menu()
        try:
            response = int(input("What is your choice? "))
        except ValueError:
            print("Please enter in a number only")
            continue
        if response == 1:
            print("Average Rent functionality is not implemented yet")
        elif response == 2:
            print("Minimum Rent functionality is not implemented yet")
        elif response == 3:
            print("Maximum Rent functionality is not implemented yet")
        elif response == 4:
            print("Min/Avg/Max by Location functionality is not "
                  "implemented yet")
        elif response == 5:
            print("Min/Avg/Max by Property Type functionality is not "
                  "implemented yet")
        elif response == 6:
            print("Location Filters functionality is not implemented "
                  "yet")
        elif response == 7:
            print("Property Type Filters functionality is not "
                  "implemented yet")
        elif response == 8:
            print("Load Data functionality is not implemented yet")
        elif response == 9:
            print("Goodbye! Thank you for using this database")
            break
        else:
            print("Please enter a number between 1 and 9")


def greeting():
    """ Obtain the user's name. """
    my_name = input("Please enter your name: ")
    print("Hi ", my_name, ", welcome to Foothill's database project.",
          sep='')


def main():
    """ Print unit test results, greet user, print menu, and print a
    unique polite message to the user based on the user's choice until
    user enters the number 9 to quit the menu.
    """
    unit_test()
    greeting()
    menu()


if __name__ == "__main__":
    main()

"""
--- sample run ---
PASS: invalid source currency raised Key Error
PASS: invalid target currency raised Key Error
PASS: Conversion from USD to GBP
PASS: Conversion from CAD to USD
PASS: Conversion from EUR to CAD
Please enter your name: 
"""
