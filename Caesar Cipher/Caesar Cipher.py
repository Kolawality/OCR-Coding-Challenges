import time


def menu():
    print("Choose from one of the following options")

    time.sleep(1)

    print("1 - encrypt a message")
    print("2 - decrypt a message")

    choice = input("Your selection: ")

    if choice == "1":
        encrypt()
    elif choice == "2":
        decrypt()
    else:
        print("That option is not valid, please re-enter your option")
        menu()


def encrypt():
    cipher_text = []

    plaintext = input("Enter the message you want to encrypt: ")
    shift = int(input("Enter the number of shifts: "))

    for each in plaintext:
        cipher_letter = chr(ord(each) + shift)
        cipher_text.append(cipher_letter)

    cipher_text = ''.join(cipher_text)

    print()
    print("The encrypted message is: {}".format(cipher_text))
    print()

    time.sleep(1)

    menu()


def decrypt():
    plaintext = []

    cipher_text = input("Enter the message you want to decrypt: ")
    shift = int(input("Enter the number of shifts: "))

    for each in cipher_text:
        plain_letter = chr(ord(each) - shift)
        plaintext.append(plain_letter)

    plaintext = ''.join(plaintext)

    print()
    print("The decrypted message is: {}".format(plaintext))
    print()

    time.sleep(1)

    menu()


print()
print("Welcome to the Caesar Cipher program")
print("Where you can encrypt and decrypt messages")
print()

time.sleep(1)
menu()
