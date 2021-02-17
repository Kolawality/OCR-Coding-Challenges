import sys
import time

from num2words import num2words


def num_to_words():
    print()
    print("Press '1' to convert a number")
    print("Press '0' to quit")
    print()

    choice = input("Select an option: ")

    if choice == "0":
        print("goodbye")
        time.sleep(1)
        sys.exit()
    elif choice == "1":
        user_number = input("Please enter a number: ")
        answer = num2words(user_number)
        print(answer)
        time.sleep(2)
        num_to_words()


if __name__ == "__main__":
    num_to_words()
