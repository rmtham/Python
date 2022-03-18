""" This program provides the results of a unit test for the method
_cross_table_statistics. Then, it asks the user for their name,
politely greets them, asks them for their home currency, asks them
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
    copyright = "No copyright has been set."

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

    class EmptyDatasetError(Exception):
        pass

    class NoMatchingItems(Exception):
        pass

    def _cross_table_statistics(self, descriptor_one: str,
                                descriptor_two: str):
        """ Return the minimum, average, and maximum rent of the
        borough and property type, if there are valid entries with a
        match.
        """
        if self._data is None:
            raise DataSet.EmptyDatasetError

        rent_list = [descriptor[2] for descriptor in self._data
                     if descriptor_one == descriptor[0] and
                     descriptor_two == descriptor[1]]

        if not rent_list:
            raise DataSet.NoMatchingItems

        min_rent = float(min(rent_list))
        max_rent = float(max(rent_list))
        avg_rent = float(sum(rent_list) / len(rent_list))

        return min_rent, avg_rent, max_rent,

    def load_default_data(self):
        """ Load the default data. """
        self._data = [("Staten Island", "Private room", 70),
                      ("Brooklyn", "Private room", 50),
                      ("Bronx", "Private room", 40),
                      ("Brooklyn", "Entire home / apt", 150),
                      ("Manhattan", "Private room", 125),
                      ("Manhattan", "Entire home / apt", 196),
                      ("Brooklyn", "Private room", 110),
                      ("Manhattan", "Entire home / apt", 170),
                      ("Manhattan", "Entire home / apt", 165),
                      ("Manhattan", "Entire home / apt", 150),
                      ("Manhattan", "Entire home / apt", 100),
                      ("Brooklyn", "Private room", 65),
                      ("Queens", "Entire home / apt", 350),
                      ("Manhattan", "Private room", 98),
                      ("Brooklyn", "Entire home / apt", 200),
                      ("Brooklyn", "Entire home / apt", 150),
                      ("Brooklyn", "Private room", 99),
                      ("Brooklyn", "Private room", 120)]


def unit_test():
    """ Test _cross_table_statistics in the class DataSet. """
    print("Testing _cross_table_statistics")
    my_set = DataSet()
    # call my_set._cross_table_statistics (no data) -> EmptyDatasetError
    try:
        my_set._cross_table_statistics("Staten Island", "Private room")
        print("Method Raises EmptyDataSet Error: Fail")
    except DataSet.EmptyDatasetError:
        print("Method Raises EmptyDataSet Error: Pass")
    except:
        print("Method Raises EmptyDataSet Error: Fail")

    my_set.load_default_data()

    # Invalid Property Type -> NoMatchingItems
    try:
        my_set._cross_table_statistics("Staten Island", "Luxury Suite")
        print("Invalid Property Type Raises NoMatchingItems Error: Fail")
    except DataSet.NoMatchingItems:
        print("Invalid Property Type Raises NoMatchingItems Error: Pass")
    except:
        print("Invalid Property Type Raises NoMatchingItems Error: Fail")
    # Invalid Borough -> NoMatchingItems
    try:
        my_set._cross_table_statistics("Hogwarts", "Private room")
        print("Invalid Borough Type Raises NoMatchingItems Error: Fail")
    except DataSet.NoMatchingItems:
        print("Invalid Borough Type Raises NoMatchingItems Error: Pass")
    except:
        print("Invalid Borough Type Raises NoMatchingItems Error: Fail")
    # No matching rows -> NoMatchingItems
    try:
        my_set._cross_table_statistics("Staten Island", "Entire home / apt")
        print("No Matching Rows Raises NoMatchingItems Error: Fail")
    except DataSet.NoMatchingItems:
        print("No Matching Rows Raises NoMatchingItems Error: Pass")
    except:
        print("No Matching Rows Raises NoMatchingItems Error: Fail")
    # One matching row -> correct tuple
    if my_set._cross_table_statistics("Staten Island", "Private room") \
            == (70.0, 70.0, 70.0):
        print("One Matching Row Returns Correct Tuple: Pass")
    else:
        print("One Matching Row Returns Correct Tuple: Fail")
    # Multiple matching rows -> correct tuple
    if my_set._cross_table_statistics("Brooklyn", "Private room") \
            == (50.0, 88.8, 120.0):
        print("Multiple Matching Rows Returns Correct Tuple: Pass")
    else:
        print("Multiple Matching Rows Returns Correct Tuple: Fail")
    # Invalid Property and Borough Type -> NoMatchingItems
    try:
        my_set._cross_table_statistics(12345, ["list", "of", "strings"])
        print("Invalid Property and Borough Type Raises NoMatchingItems"
              " Error: Fail")
    except DataSet.NoMatchingItems:
        print("Invalid Property and Borough Type Raises NoMatchingItems"
              " Error: Pass")
    except:
        print("Invalid Property and Borough Type Raises NoMatchingItems"
              " Error: Fail")


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
Testing _cross_table_statistics
Method Raises EmptyDataSet Error: Pass
Invalid Property Type Raises NoMatchingItems Error: Pass
Invalid Borough Type Raises NoMatchingItems Error: Pass
No Matching Rows Raises NoMatchingItems Error: Pass
One Matching Row Returns Correct Tuple: Pass
Multiple Matching Rows Returns Correct Tuple: Pass
Invalid Property and Borough Type Raises NoMatchingItems Error: Pass

Please enter your name: 
"""