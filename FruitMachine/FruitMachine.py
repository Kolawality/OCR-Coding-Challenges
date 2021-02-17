import time
from tkinter import *
import random

# Create the main window, referred to as window
window = Tk()
window.title("The Ultimate Fruit Machine")
window.configure(background="White")

# Turn each image into a object
cherry_photo = PhotoImage(file="cherry.png")
bell_photo = PhotoImage(file="bell.png")
lemon_photo = PhotoImage(file="lemon.png")
orange_photo = PhotoImage(file="orange.png")
skull_photo = PhotoImage(file="skull.png")
star_photo = PhotoImage(file="star.png")

# Put images into a list which can be used to create a random choice
images = [cherry_photo,
          bell_photo,
          lemon_photo,
          orange_photo,
          skull_photo,
          star_photo]

# Randomly generate an image for the label and store in variable
symbol1 = Label(window, width=35, height=30, bg="white")
symbol2 = Label(window, width=35, height=30, bg="white")
symbol3 = Label(window, width=35, height=30, bg="white")

# Place the symbols generated into the middle of the window
symbol1.grid(row=2, column=3, sticky=E)
symbol2.grid(row=2, column=4, sticky=E)
symbol3.grid(row=2, column=5, sticky=E)


# Function allow the user to close the program
def leave():
    sys.exit()


# Runs when the roll button is selected
def roll():
    """
    Firstly a random image is selected from the images array and assigned to
    one of three variables.

    Each of the random images appear on the screen i.e., symbol 1,2 and 3

    The random images that have been selected are then placed in a list and
    returned so that they can be used in the get total function
    """
    global symbol1
    global symbol2
    global symbol3

    random_image1 = random.choice(images)
    random_image2 = random.choice(images)
    random_image3 = random.choice(images)

    # Randomly generate an image for the label and store in variable
    symbol1 = Label(window, image=random_image1, bg="white")
    symbol2 = Label(window, image=random_image2, bg="white")
    symbol3 = Label(window, image=random_image3, bg="white")

    # Place the symbols generated into the middle of the window
    symbol1.grid(row=2, column=3, sticky=E)
    symbol2.grid(row=2, column=4, sticky=E)
    symbol3.grid(row=2, column=5, sticky=E)

    random_images = [random_image1, random_image2, random_image3]

    get_total(random_images)


# Before the new symbols appear the current symbols are cleared from the screen
def clear():
    symbol1.destroy()
    symbol2.destroy()
    symbol3.destroy()


# def check():
#     z = int(str(eval(total_window.get())))
#     x = format(Decimal.from_float(z), '.2')
#     if x < 0:
#         total_window.delete(0, END)
#         total_window.insert(0, "You Lose")

# Adding 50p and then subtract 20p for the roll
def adding_point_five():
    total_window.insert(END, "+0.50 - 0.20")
    # total_window.insert(END, "-.2")
    result = str(eval(total_window.get()))
    total_window.delete(0, END)
    total_window.insert(0, result[0:4])


# Adding £1 and then subtract 20p for the roll
def adding_one():
    total_window.insert(END, "+1.00 - 0.20 ")
    # total_window.insert(END, "-.2")
    result = str(eval(total_window.get()))
    total_window.delete(0, END)
    total_window.insert(0, result[0:4])


# Adding £5 and then subtract 20p for the roll
def adding_five():
    total_window.insert(END, "+5.00 - 0.20")
    result = str(eval(total_window.get()))
    total_window.delete(0, END)
    total_window.insert(0, result[0:4])


# Subtracting 20p for the roll
def subtract_point_two():
    total_window.insert(END, "-0.20")
    result = str(eval(total_window.get()))
    total_window.delete(0, END)
    total_window.insert(0, result[0:4])


# Subtracting £1 for the roll
def subtract_one():
    total_window.insert(END, "-1")
    result = str(eval(total_window.get()))
    total_window.delete(0, END)
    total_window.insert(0, result[0:4])


# Calculates and determines how much the user's score should change
def get_total(random_images):
    """
    Firstly a for loop is used to calculate how many of (each) symbol has
    appeared. If  If the Fruit Machine “rolls” two of the same symbol, the
    user wins 50p. The player wins £1 for three of the same
    and £5 for 3 Bells. The player loses £1 if two skulls are rolled and
    all of his/her money if three skulls are rolled.
    """
    skull_counter = 0
    for x in random_images:
        if x == skull_photo:
            skull_counter += 1
    if skull_counter == 3:
        message.delete(0, END)
        message.insert(0, " Two cherries! + 50p ")
        time.sleep(3)
    else:
        cherry_counter = 0
        for x in random_images:
            if x == cherry_photo:
                cherry_counter += 1
        if cherry_counter == 2:
            adding_point_five()
            message.delete(0, END)
            message.insert(0, " Two cherries! + 50p ")
        elif cherry_counter == 3:
            adding_one()
            message.delete(0, END)
            message.insert(0, " Three cherries! + £1 ")

        bell_counter = 0
        for x in random_images:
            if x == bell_photo:
                bell_counter += 1
        if bell_counter == 2:
            adding_point_five()
            message.delete(0, END)
            message.insert(0, " Two bells! + 50p ")
        elif bell_counter == 3:
            adding_five()
            message.delete(0, END)
            message.insert(0, " Three bells! + £5 ")

        lemon_counter = 0
        for x in random_images:
            if x == lemon_photo:
                lemon_counter += 1
        if lemon_counter == 2:
            adding_point_five()
            message.delete(0, END)
            message.insert(0, " Two lemons! + 50p ")
        elif lemon_counter == 3:
            adding_one()
            message.delete(0, END)
            message.insert(0, " Three lemons! + 50p ")

        orange_counter = 0
        for x in random_images:
            if x == orange_photo:
                orange_counter += 1
        if orange_counter == 2:
            adding_point_five()
            message.delete(0, END)
            message.insert(0, " Two oranges! + 50p ")
        elif orange_counter == 3:
            adding_one()
            message.delete(0, END)
            message.insert(0, " Three oranges! + £1 ")

        star_counter = 0
        for x in random_images:
            if x == star_photo:
                star_counter += 1
        if star_counter == 2:
            adding_point_five()
            message.delete(0, END)
            message.insert(0, " Two stars! + 50p ")
        elif star_counter == 3:
            adding_one()
            message.delete(0, END)
            message.insert(0, " Three stars! + £1 ")

        skull_counter = 0
        for x in random_images:
            if x == skull_photo:
                skull_counter += 1
        if skull_counter == 2:
            subtract_one()
            message.delete(0, END)
            message.insert(0, " Oh no two skulls! -£1 ")

        if lemon_counter < 2 and orange_counter < 2 and bell_counter < 2 and \
                star_counter < 2 and cherry_counter < 2:
            message.delete(0, END)


# Quit button in the top right
Button(window, borderwidth=3, relief="ridge", text="Quit", command=leave,
       bg="white", fg="black", font="none 12 bold").grid(row=0, column=8,
                                                         stick=E)

# Creating the 'roll' button on the screen
roll_button = Button(window, width=20, relief="ridge", text="ROLL",
                     command=lambda: [clear(), roll()],
                     bg="white",
                     fg="black",
                     font="none 12 bold")
roll_button.grid(row=0, column=3, columnspan=3)

# Adding the running total
total_window = Entry(window, width=5, relief="groove",
                     bg="white", fg="black", font="none 12 bold")
total_window.grid(row=1, column=2, sticky=E)
total_window.insert(END, "1")

pound_sign = Label(window, width=1, text="£", bg="white", fg="black",
                   font="none 12 bold")
pound_sign.grid(row=1, column=1, sticky=E)

# Creating the 'roll' button on the screen
message = Entry(window, width=30, text="Welcome", bg="white", fg="black",
                font="none 12 bold")
message.grid(row=3, column=3, columnspan=3)

window.mainloop()
