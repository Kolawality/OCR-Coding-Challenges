# Date: Monday 8th July 2020
# Author: Michael Kolawole
# Title: Speed Tracker Extension 1.py

'''

Pseudocode planning:

Set format for plates (LLNN LLL)
For 1 to 10:
    Generate random license plates

For each in car_database:
    add comma and random number(20,60)

distance = 1

For each in car_database:
    if last 2 characters > 30:
        add '-fine'
        add first 8 characters to fine_list

for each in fine_list:
    OUTPUT these cars will be fined

'''

import random
import string
from datetime import datetime


# function to generate a random character for specified length (y)
def random_char(y):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(y))


# randomly generates two letters, two numbers (adds a space) and then three
# letters to simulate a license plate number
def license_plate_gen():
    p1 = random_char(2)
    p2 = str(random.randint(10, 99))
    p3 = random_char(3)
    return ''.join(p1 + p2 + ' ' + p3)


# Calculates the speed of a car depending on the user inputs
def speed_check():
    # distance is set to 1 as the distance between cameras is fixed
    distance = 1

    # find out the current date, year, month and day to pre-populate the start
    # and end times
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    # ask the user for the time it passes the first and then the second camera
    start_hour = int(input("start hour: "))
    start_minute = int(input("start minute: "))
    finish_hour = int(input("end hour: "))
    finish_minute = int(input("end minute: "))

    # convert the start and end times into datetime objects
    start_time = datetime(year, month, day, start_hour, start_minute)
    finish_time = datetime(year, month, day, finish_hour, finish_minute)

    # find the difference between the two times
    difference = finish_time - start_time

    # the difference is converted into seconds and then to hours
    time_elapsed = difference.total_seconds() / 60 ** 2

    # speed equals distance divided by time, converted to float to allow for
    # decimal numbers
    return str(int(distance / time_elapsed))


# Adds the license plate and speed to the car_database file
with open('car_database', 'a') as the_file:
    x = license_plate_gen()
    the_file.write(''.join(('\n{}'.format(x)) + ' at ' + speed_check()))

# Reads each line of the file and reads them to a list
cars = []
with open('car_database', 'r') as the_file:
    for line in the_file:
        line = line.rstrip()
        cars.append(line)

# For each element in the list check whether the speed is above a threshold
# level and should be fined
for each in range(len(cars)):
    x = int(cars[each][-2:])
    if x > 30:
        with open('car_fine_database', 'a') as the_file:
            the_file.write((cars[each][:8]) + " was travelling at {}mph "
                                              "and will be fined\n".format(x))
