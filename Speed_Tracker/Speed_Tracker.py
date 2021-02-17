# Date: Sunday 7th July 2020
# Author: Michael Kolawole
# Title: Speed_Tracker.py

'''

Pseudocode answer:

distance = 1
start_time = USER_INPUT
finish_time = USER_INPUT
time = finish_time - start_time
speed = distance/time
OUTPUT speed

'''

# import module to help us manipulate dates
from datetime import datetime

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
time_elapsed = difference.total_seconds()/60**2

# speed equals distance divided by time, converted to float to allow for
# decimal numbers
speed = float(distance/time_elapsed)

# display the speed of the vehicle
print("The vehicle was travelling at {} mph".format(speed))
