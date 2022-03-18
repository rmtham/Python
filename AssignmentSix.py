""" This program provides the results of a unit test for the header and
copyright properties of the program. Then, it asks the user for their
name, politely greets them, asks them for their home currency, asks them
to enter a header for the menu, prints a currency table, then provides
them with a menu with the copyright and header at the top. The user is
prompted to input an option, and the program provides an unique polite
message to the user's response accordingly.
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

class DataSet:

    copyright = "No copright has been set."

    def __init__(self, header=""):
        try:
            self.header = header
        except ValueError:
            self.header = ""
        self._data = None

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, header: str):
        if type(header) == str and len(header) <= 30:
            self._header = header
        else:
            self._header = ""
            raise ValueError


def unit_test():
    """ Check the header and copyright properties by testing the result
    of an object created with no header argument, a valid argument, and
    an invalid header argument; in addition, test the result when a
    user provides an invalid or valid header.
    """
    # object created with default parameter -> empty string
    test_dataset_one = DataSet()
    if test_dataset_one.header == "":
        print("Testing constructor with default parameter: Pass")
    else:
        print("Testing constructor with default parameter: Fail")
    # object created with valid header argument -> header set
    header = "Welcome to the airBNB Database"
    test_dataset_two = DataSet(header)
    if test_dataset_two.header == header:
        print("Testing constructor with valid header argument: Pass")
    else:
        print("Testing constructor with valid header argument: Fail")
    # object created with invalid header argument -> empty string
    header = 123456789
    test_dataset_three = DataSet(header)
    if test_dataset_one.header == "":
        print("Testing constructor with invalid header argument: Pass")
    else:
        print("Testing constructor with invalid header argument: Fail")
    # setter with valid assignment -> header is changed
    valid_header = "Welcome to the airBNB Database"
    test_dataset_one.header = valid_header
    if test_dataset_one.header == valid_header:
        print("Testing setter with valid assignment: Pass")
    else:
        print("Testing setter with valid assignment: Fail")
    # setter with invalid assignment -> header is not changed
    invalid_header = "Really lonnnnnnggggggggggggggggggggggggggg header"
    try:
        test_dataset_one.header = invalid_header
        print("Testing setter with invalid assignment: Fail")
    except ValueError:
        if test_dataset_one.header == "":
            print("Testing setter with invalid assignment: Pass")
        else:
            print("Testing setter with invalid assignment: Fail")
    except:
        print("Testing setter with invalid assignment: Fail")
    # access class attribute using class name -> copyright attribute
    print("Setting DataSet.copyright = 'copyright Michelle Tham'")
    DataSet.copyright = 'copyright Michelle Tham'
    print("Checking that I can access this using DataSet.copyright")
    try:
        DataSet.copyright
        print("Pass")
    except:
        print("Fail")
    # access class attribute using object name -> copyright attribute
    print("Checking that I can access this after I have created a\n"
          "test object using test.copyright")
    test = DataSet()
    try:
        test.copyright
        print("Pass")
    except:
        print("Fail")


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


def menu(dataset: DataSet):
    """ Print  the currency table, then print out menu with the
    copyright and header on the top. Ask user to select an option,
    catch errors, and provide a unique polite message for each selection
    until they enter 9 to indicate that they want to quit the menu.
    """
    print(f"Options for converting from {home_currency}")
    currency_options(home_currency)
    print(DataSet.copyright)
    show_menu = True
    while show_menu:
        print(dataset.header)
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
    my_name = input("\nPlease enter your name: ")
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
    """ Print out results of unit test, greet user, ask user for their
    home currency, ask user to enter header for the menu, print table of
    options for currency conversions, print menu with header and
    copyright at the top, and print a unique polite message to the user
    based on the user's choice until user enters the number 9 to quit
    the menu.
    """
    unit_test()
    greeting()
    ask_home_currency()
    DataSet.copyright = "\nCopyright Michelle Tham"
    air_bnb = DataSet()
    while True:
        header = input("Please enter a header for the menu: ")
        try:
            air_bnb.header = header
            break
        except ValueError:
            continue
    menu(air_bnb)


if __name__ == "__main__":
    main()

"""
--- sample run #1 ---
Testing constructor with default parameter: Pass
Testing constructor with valid header argument: Pass
Testing constructor with invalid header argument: Pass
Testing setter with valid assignment: Pass
Testing setter with invalid assignment: Pass
Setting DataSet.copyright = 'copyright Michelle Tham'
Checking that I can access this using DataSet.copyright
Pass
Checking that I can access this after I have created a
test object using test.copyright
Pass

Please enter your name: Michelle
Hi Michelle, welcome to Foothill's database project.
What is your home currency? GBP
Please enter a header for the menu: Welcome to the airBNB Database
Options for converting from GBP
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

Copyright Michelle Tham
Welcome to the airBNB Database
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
What is your choice? 

--- sample run #2 ---
Testing constructor with default parameter: Pass
Testing constructor with valid header argument: Pass
Testing constructor with invalid header argument: Pass
Testing setter with valid assignment: Pass
Testing setter with invalid assignment: Pass
Setting DataSet.copyright = 'copyright Michelle Tham'
Checking that I can access this using DataSet.copyright
Pass
Checking that I can access this after I have created a
test object using test.copyright
Pass

Please enter your name: Michelle
Hi Michelle, welcome to Foothill's database project.
What is your home currency? GBP
Please enter a header for the menu: Welcome to the airBNB Database
Options for converting from GBP
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

Copyright Michelle Tham
Welcome to the airBNB Database
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
Welcome to the airBNB Database
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
What is your choice? 5
Min/Avg/Max by Property Type functionality is not implemented yet
Welcome to the airBNB Database
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