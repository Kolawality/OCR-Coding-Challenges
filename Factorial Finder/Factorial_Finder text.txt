# Date: Sunday 7th July 2020
# Author: Michael Kolawole
# Title: Factorial_Finder.py

'''

Pseudocode answer

n = USER_INPUT
y = n-1
total = n
IF n == 0:
    OUTPUT 1
ELSE:
    WHILE y NOT 0:
        total = total * y
        y = y - 1

OUTPUT total

'''

# Share the purpose of the program
print()
print("The Factorial of a positive integer, n, is defined as the product "
      "\nof the sequence n, n-1, n-2, ...1 and the factorial of zero, 0, is "
      "\ndefined as being 1. Solve this using both loops and recursion.")
print()

# Prompt the user to find a number to find the factorial for
n = int(input("Please enter a number: "))

# Take away one from 'n' find the first multiplier
y = n - 1

# To keep track of the calculation, i.e., ((n*n-1)*(n-2))...*1)
total = n

# If the user enters 0, the answer is always 1
if n == 0:
    print("0! is equal to 1")
else:
    # While multiplier doesn't equal 0 it will multiply the multiplicand
    # until the multiplier reaches 1
    while y != 0:
        total = total * y
        y = y - 1

# Displays the answer
print("{} factorial is equal to {}".format(n, total))
