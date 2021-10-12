# Python program to display calendar of
# given month of the year

# import module
import calendar
import datetime
from datetime import date


def format_date(a_date):
    d = datetime.date(a_date).strftime("%A, %B %e, %Y")
    return d


yy = 2020
mm = 7

# display the calendar
print(calendar.month(yy, mm))

event_list = {
    "event_1": ["2020-07-07", "2020-07-09"],
    "event_2": ["2020-06-04", "2020-07-06"]
}

# startOfEvent_1 = event_list.get("event_1")[0]
# endOfEvent_1 = event_list.get("event_1")[1]
#
# startOfEvent_2 = event_list.get("event_2")[0]
# endOfEvent_2 = event_list.get("event_2")[1]

# print(x)
#
# for each in event_list:
#     print(event_list.get(each)[0])

event = []

new_date_entry = input("Enter a start date in YYYY-MM-DD format: ")
year, month, day = map(int, new_date_entry.split('-'))
start_of_event = datetime.date(year, month, day)
event.append(start_of_event)

new_date_entry = input("Enter an end date in YYYY-MM-DD format: ")
year, month, day = map(int, new_date_entry.split('-'))
end_of_event = datetime.date(year, month, day)
event.append(end_of_event)

for each in event_list:

    start_date_entry = event_list.get(each)[0]
    year, month, day = map(int, start_date_entry.split('-'))
    start = datetime.date(year, month, day)

    end_date_entry = event_list.get(each)[1]
    year, month, day = map(int, end_date_entry.split('-'))
    end = datetime.date(year, month, day)

    if start <= start_of_event <= end:
        print("event overlaps ")

    elif start <= start_of_event and end_of_event <= end:
        print("event overlaps")

    elif start_of_event <= start and start_of_event <= end_of_event:
        print("event overlaps")

    elif start <= start_of_event and end <= end_of_event:
        print("event overlaps")

    elif start_of_event <= end <= end_of_event:
        print("event overlaps")

    else:
        print("this event doesn't overlap")
