# Title: Number Table
# Author: Michael Kolawole
# Date: Tuesday 12th October 2021

# User enters a number
number = int(input("Enter a number: "))

# user enters a symbol
operator = input("Enter one of the operators: +, -, * or /: ")

# print the operator, followed by the line, and 0 to n numbers (ideally added to a list)
print(f"{operator} | ", end='')

top = []

for each in range(number + 1):
    if each == 0:
        break
    print(each, end='')
    top.append(each)
    
left = []

for each in range(number + 1):
    print(each)
    left.append(each)