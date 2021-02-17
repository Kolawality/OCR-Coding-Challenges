# Date created: Wednesday 23rd December
# Author: Michael Kolawole
# Title: Data Entry

import time
from texttable import Texttable


def register_member():
    time.sleep(1)
    print("\n You've chosen to register a new member, please enter their "
          "details below")
    name = input("\nFirst Name: ")
    last_name = input("Last Name: ")
    climbing_centre = input("Climbing centre: ")
    member = [name, last_name, climbing_centre]
    return member


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

    if choice == 1:
        new_member = register_member()
        print("\n Reviewing details...")
        time.sleep(1)
        print()
        t = Texttable()
        t.add_rows([["First Name", "Last Name", "Centre Name"], new_member])
        print(t.draw())


if __name__ == "__main__":
    main()

# accept inputs
# display the output in a useful format
# ask the user to confirm the details
