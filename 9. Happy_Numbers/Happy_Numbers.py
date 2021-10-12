import time


def calc_happy_number(number):
    user_number_list = list(map(int, str(number)))
    print(user_number_list)

    x = len(user_number_list)
    i = 0

    while i < x:
        user_number_list[i] = user_number_list[i] ** 2
        i += 1

    total = sum(user_number_list)
    print(total)

    try:
        if total == 1:
            print("Happy number")
        else:
            calc_happy_number(total)
    except RecursionError:
        print("not a happy number")


for i in range(0, 100):
    time.sleep(2)
    calc_happy_number(i)
    time.sleep(2)
    print(i)
