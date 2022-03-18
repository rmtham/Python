""" This program asks the user for their name, politely greets them,
asks them for their home currency, prints a currency table, then
provides them with a menu. The user is prompted to input an option, and
the program provides an unique polite message to the user's response
accordingly.
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
home_currency = ""


def currency_converter(quantity: float, source_curr: str, target_curr: str):
    """ Convert source currency to target currency.

    Key Arguments:
        quantity (float): the amount of the original currency
        source_curr (str): represents the source currency
        target_curr (str): represents the currency after exchange
    """
    converted_quantity = quantity \
                         * (1 / conversions[source_curr]) \
                         * conversions[target_curr]
    return converted_quantity


def currency_options(base_curr: str):
    """ Print out a table of options for converting base_curr to all
    other string currencies.

    Key Arguments:
        base_curr (str): the home currency of the user
    """
    print(f"{base_curr:9}", end="")
    for currency in conversions:
        if currency == base_curr:
            continue
        else:
            print(f"{currency:9}", end="")
    print()

    for i in range(10, 100, 10):
        print(f"{i:<9.2f}", end="")
        for currency in conversions:
            if currency == base_curr:
                continue
            else:
                converted_currency = currency_converter(i, base_curr, currency)
                print(f"{converted_currency:<9.2f}", end="")
        print()


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
    """ Print  the currency table, then print out menu. Ask user to
    select an option, catch errors, and provide a unique polite message
    for each selection until they enter 9 to indicate that they want to
    quit the menu.
    """
    currency_options(home_currency)
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


def ask_home_currency():
    """ Ask for user's home currency until user enters in a valid
    currency.
    """
    global home_currency
    invalid_currency = True
    while invalid_currency:
        home_currency = input("What is your home currency? ")
        for currency in conversions:
            if home_currency == currency:
                invalid_currency = False
            else:
                continue


def main():
    """ Greet user, ask for user currency, print table of options for
    currency conversions, print menu, and print a unique polite message
    to the user based on the user's choice until user enters the number
    9 to quit the menu.
    """
    greeting()
    ask_home_currency()
    menu()


if __name__ == "__main__":
    main()

"""
--- sample run ---
Please enter your name: Michelle
Hi Michelle, welcome to Foothill's database project.
What is your home currency? Galactic Credit Standard
What is your home currency? GBP
GBP      USD      EUR      CAD      CHF      NZD      AUD      JPY      
10.00    12.50    11.25    17.50    11.88    20.75    20.25    1349.00  
20.00    25.00    22.50    35.00    23.75    41.50    40.50    2698.00  
30.00    37.50    33.75    52.50    35.62    62.25    60.75    4047.00  
40.00    50.00    45.00    70.00    47.50    83.00    81.00    5396.00  
50.00    62.50    56.25    87.50    59.38    103.75   101.25   6745.00  
60.00    75.00    67.50    105.00   71.25    124.50   121.50   8094.00  
70.00    87.50    78.75    122.50   83.12    145.25   141.75   9443.00  
80.00    100.00   90.00    140.00   95.00    166.00   162.00   10792.00 
90.00    112.50   101.25   157.50   106.88   186.75   182.25   12141.00 
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 1
Average Rent functionality is not implemented yet
Main Menu
1 - Print Average Rent by Location and Property Type
2 - Print Minimum Rent by Location and Property Type
3 - Print Maximum Rent by Location and Property Type
4 - Print Min/Avg/Max by Location
5 - Print Min/Avg/Max by Property Type
6 - Adjust Location Filters
7 - Adjust Property Type Filters
8 - Load Data
9 - Quit
What is your choice? 9
Goodbye! Thank you for using this database
"""