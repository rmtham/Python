""" This  program asks the user for their name, and it responds
with a friendly greeting with the user's name.
"""


def main():
    """ Obtain the user's name. """
    my_name = input("Please enter your name: ")
    print("Hi ", my_name, ", welcome to Foothill's database project.", sep='')

    def print_menu():
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
        print_menu()


if __name__ == "__main__":
    main()

"""
--- sample run #1 (My name) ---
Please enter your name: Michelle
Hi Michelle, welcome to Foothill's database project.

--- sample run #2 (No input) ---
Please enter your name: 
Hi , welcome to Foothill's database project.

--- sample run #3 (Non alpha input) ---
Please enter your name: *~*~*~*~
Hi *~*~*~*~, welcome to Foothill's database project.
"""
