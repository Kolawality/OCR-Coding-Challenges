# Date created: Wednesday 23rd December
# Author: Michael Kolawole
# Title: Data Entry

import time
from texttable import Texttable


# prompts the user to enter member details
def register_member():
    time.sleep(1)
    print("\n You've chosen to register a new member, please enter their "
          "details below")
    name = input("\nFirst Name: ")
    last_name = input("Last Name: ")
    climbing_centre = input("Climbing centre: ")
    member = [name, last_name, climbing_centre]
    return member


# introduces the program and the menu
def main():
    # introduce the user to the program
    print()
    print("*" * 50)
    print()
    print(" \t Welcome to the Rock Climbing Program")
    print()
    print("*" * 50)

    time.sleep(1)

    print("\nPlease select from on of the following options: ")
    print(
        "\n1 - Register a new member "
        "\n2 - Search for a user's details"
    )

    choice = -1
    while choice != 1 and choice != 2:
        choice = int(input("\nPlease select 1 or 2: "))

    # depending on the number of entrants
    # the user will be prompted to entered member details a specified number
    # of times, and their details are displayed in a table
    if choice == 1:
        num_of_members = int(input("How many new members?: "))
        t = Texttable()
        for each in range(num_of_members):
            new_member = register_member()
            t.add_rows(
                [["First Name", "Last Name", "Centre Name"], new_member])
        print("\n Reviewing details...")
        time.sleep(1)
        print()
        print(t.draw())


if __name__ == "__main__":
    main()

# accept inputs
# display the output in a useful format
# ask the user to confirm the details
