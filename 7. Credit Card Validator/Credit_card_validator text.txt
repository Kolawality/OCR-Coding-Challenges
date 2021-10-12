"""
The purpose of this program is to take in in a credit card number from a
common credit card vendor (Visa, MasterCard, American Express, Discoverer) and
validates it to make sure that it is a valid number, using the luhn algorithm
"""
import time

# Introduces the purpose of the program to the user
print("**********************************************************************")
print()
print("The purpose of this program is determine whether a card number is "
      "valid")
print()
print("**********************************************************************")
print()

time.sleep(2)

# The user is prompted to enter a card number
# Example valid card number: 4904839822485959
cc_number = input("Please enter a card number: ")

# The card number is turned into a list of integers
cc_numbers = [int(x) for x in cc_number]

# Initialise the list for the odd and even elements (numbers) in cc_numbers
even_numbers = []
odd_numbers = []

# Stepping through decrementally from the second to last number (the even
# numbered elements)
# If after being doubled the number is above 9, the sum of the two digits is
# found, i.e., 18 would be 1 + 8, the same result is achieved if nine is
# subtracted
# The result is then added to a new list (even_sum_numbers)
for x in range(len(cc_numbers) - 2, -1, -2):
    if cc_numbers[x] * 2 > 9:
        even_numbers.append(cc_numbers[x] * 2 - 9)
    else:
        even_numbers.append(cc_numbers[x] * 2)

even_numbers_sum = sum(even_numbers)

# All the odd numbered elements are added to the odd_numbers list and the
# sum is found
for x in range(1, len(cc_numbers), 2):
    odd_numbers.append(cc_numbers[x])

odd_numbers_sum = sum(odd_numbers)

# The two lists are then added together
total = odd_numbers_sum + even_numbers_sum

# If the result is divisible by 10 then the credit card number is valid
if total % 10 == 0:
    print("\nThis is a valid card number")
else:
    print("\nThis is an invalid card number")
