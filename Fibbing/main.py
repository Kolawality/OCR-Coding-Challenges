
# a list containing the sequence
sequence = [1, 1]

# index of next item in the sequence
current = 2
length = 0

# ensure that the input is at least three
while length < 3:
    try:
        length = int(input(
            "How many numbers would you like in the sequence?"
            "\nIt must be at least three: "))
    except:
        print("That's not a number.")
        length = 0

# while the sequence is shorter than chosen length,,,
while len(sequence) < length:
    # add the total of the last two numbers in the list
    # to the end of the list
    sequence.append(sequence[current - 2] + sequence[current - 1])
    # move on to the next item
    current += 1

# print the results
print("The sequence is", sequence)
sequence.reverse()
print("Reversed it would be", sequence)
print("The sum of the numbers in the sequence is", sum(sequence))
