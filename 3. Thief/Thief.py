# Date: Wednesday 10th July 2020
# Author: Michael Kolawole
# Title: Thief.py

'''

Pseudocode initial planning

OUTPUT Welcome to the program

four_numbers = []

first_digit = USER_INPUT append to four_numbers
second_digit = USER_INPUT append to four_numbers
third_digit = USER_INPUT append to four_numbers
fourth_digit = USER_INPUT append to four_numbers

combinations = list(permutations(fournumbers))

for combination in range(combinations):
    print("possible combination: " combination)

'''
import time
from itertools import permutations


# Convert a list of integers into a single integer
def convert(list):
    # Converting the integer list to string list and joining the list using
    # join()
    result = int("".join(map(str, list)))
    return result


# Introduces the purpose of this program
print()
print("A A thief has managed to find out the four digits for an online PIN "
      "\ncode, but doesn’t know the correct sequence needed to hack into the "
      "\naccount."
      "\n"
      "\nDesign and write a program that displays all the possible "
      "combinations"
      "\nfor any four numerical digits entered by the user. The program "
      "\nshould avoid displaying the same combination more than once.")

# Pauses the program for one second
time.sleep(1)

# Initialises a list to store the entries of the 'thief'
four_numbers = []

# Ask the user for four digits and read them to the four_numbers list
print()
four_numbers.append(int(input("What is the first number: ")))
four_numbers.append(int(input("What is the second number: ")))
four_numbers.append(int(input("What is the third number: ")))
four_numbers.append(int(input("What is the fourth number: ")))
print()

# store all the permutations (combinations without any duplicates) using the
# permutations method
combinations = list(permutations(four_numbers))

# print each combination (permutation) on a separate line
for combination in combinations:
    print("Possible combination: {}".format(combination))
