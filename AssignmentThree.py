""" This program asks the user for their name, then it politely greets
them and provides them with a menu. The user is prompted to input an
option, and the program provides an unique polite message to the user's
response accordingly.
"""


def main():
    """ Greet user, print menu, ask user for option, and print an unique
    polite message to the user accordingly.
    """

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
        errors, and provide a unique polite message for each selection.
        """
        show_menu = True
        while show_menu:
            print_menu()
            try:
                response = int(input("What is your choice? "))
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
            except ValueError:
                print("Please enter in a number only")

    def greeting():
        """ Obtain the user's name. """
        my_name = input("Please enter your name: ")
        print("Hi ", my_name, ", welcome to Foothill's database project.",
              sep='')

    greeting()
    menu()


if __name__ == "__main__":
    main()

"""
--- sample run ---
Please enter your name: Michelle
Hi Michelle, welcome to Foothill's database project.
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
What is your choice? 2
Minimum Rent functionality is not implemented yet
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
What is your choice? one
Please enter in a number only
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
What is your choice? 100
Please enter a number between 1 and 9
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
