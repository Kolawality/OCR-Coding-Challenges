import sys
import time


# The main part of the program displaying the options to the user
def main():
    """
    The user's options are shown on multiple lines, the sections are broken
    up by time.sleep commands to make it easier to read. To make a selection
    the user needs to press the appropriate number to begin a conversion or
    press '0' to quit.
    """
    print("**************************************************************")
    print("The purpose of this program is to convert between units")
    print()
    print("You can convert between temperature, currency and volume")
    print()
    print("**************************************************************")
    time.sleep(2)

    print("1 - Convert from celsius to fahrenheit")
    print("2 - Convert from fahrenheit to celsius")
    print("3 - Convert from pounds to dollars")
    print("4 - Convert from dollars to pounds")
    print("5 - Convert from cubic centimetres to litres")
    print("6 - Convert from litres to cubic centimetres")
    print()
    print("0 - Exit the program\n")

    choice = input("Please select the conversion you want to perform: ")

    if choice == "1":
        celsius_to_fahrenheit()
    elif choice == "2":
        fahrenheit_to_celsius()
    elif choice == "3":
        pounds_to_dollars()
    elif choice == "4":
        dollars_to_pounds()
    elif choice == "5":
        cm3_to_l()  # centimetres cubed to litres
    elif choice == "6":
        l_to_cm3()  # # litres cubed to centimetres cubed
    elif choice == "0":
        sys.exit()
    else:
        print("You've entered an incorrect value, please try again")
        main()


# Converts celsius to fahrenheit (rounded to two decimal places)
def celsius_to_fahrenheit():
    celsius = int(input("Please enter the amount of celsius you want to "
                        "convert: "))
    fahrenheit = float((celsius * (9 / 5)) + 32)
    print("{} is equal {} fahrenheit".format(celsius, round(fahrenheit, 2)))
    time.sleep(1)
    main()


# Converts fahrenheit to celsius (rounded to two decimal places)
def fahrenheit_to_celsius():
    fahrenheit = int(input("Please enter the amount of fahrenheit you want "
                           "to convert: "))
    celsius = float((fahrenheit - 32) * (5 / 9))
    print("{} is equal {} celsius".format(fahrenheit, round(celsius, 2)))
    time.sleep(1)
    main()


# Converts pounds to dollars used the exchange rate of 1.23
def pounds_to_dollars():
    pounds = int(input("Please enter the amount of pounds you wish to "
                       "convert: "))
    dollars = float(pounds * 1.23)
    print("{} pounds is equal to {} dollars".format(pounds, round(dollars, 2)))
    time.sleep(1)
    main()


# Converts dollars to pounds using the exchange rate of 0.81
def dollars_to_pounds():
    dollars = int(input("Please enter the amount of dollars you wish to "
                        "convert: "))
    pounds = float(dollars * 0.81)
    print("{} dollars is equal to {} pounds".format(dollars, round(pounds,
                                                                   2)))
    time.sleep(1)
    main()


# Converts cubic centimetres to litres (the result is rounded to two decimal
# places)
def cm3_to_l():
    cm3 = int(input("Please enter the amount of cubic centimetres you wish "
                    "to convert: "))
    litres = cm3 * 0.001
    print("{} cubic centimetres is equal to {} litres".format(cm3,
                                                              round(litres,
                                                                    2)))


# Converts litres to cubic centimetres (the result is rounded to two decimal
# places)
def l_to_cm3():
    litres = float(input("Please enter the amount of litres you wish "
                         "to convert: "))
    cm3 = litres * 1000
    print("{} litres is equal to {} cm3".format(cm3, round(cm3, 2)))


main()  # Runs the program
