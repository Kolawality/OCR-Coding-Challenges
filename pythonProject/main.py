# Date created: Monday 8th February 2021
# Title: Simple Life Calculator
# Author: Michael Kolawole

import time


# VAT calculator
def calculate_vat():
    price = float(input("How much did you pay? "))
    vat = round(.2 * price, 2)
    final_price = price + vat
    return price, vat, final_price


# displays the line items in a useful format
def display(price, vat, final_price):
    print("You paid", price)
    print("The VAT you paid came to £{:.2f}".format(vat))
    print("Your final payment after VAT is £{:.2f}".format(final_price))


# displays the times tables from 1 to 10 for a given number
def times_tables():
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, 'x', i, '=', num * i)


# calculates the amount of tax the user has to pay given the income
def tax_calculator():
    income = float(input("Enter the annual income: "))

    tax = 0.0
    if income <= 85528:
        tax = income * 0.18 - 556.02
        if tax < 0:
            tax = 0
    else:
        tax = (income - 85528) * .32 + 14839.02
    tax = round(tax, 0)
    print("The tax is: £{:.2f}". format(tax))


# Main menu showing the user options, continues display until '0' selected
def main():
    choice = ""
    while choice != 0:
        print("\nWelcome to the life calculator")
        print("Please select from the following options:"
              "\n1 - VAT"
              "\n2 - Tax"
              "\n3 - Times Tables"
              "\n0 - Quit")
        choice = int(input("Enter option here: "))

        if choice == 1:
            time.sleep(1)
            line_items = calculate_vat()
            print(line_items)
            display(*line_items)

        elif choice == 2:
            time.sleep(1)
            tax_calculator()

        elif choice == 3:
            time.sleep(1)
            times_tables()


if __name__ == '__main__':
    main()

