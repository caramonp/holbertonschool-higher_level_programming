#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for numbers in range(0, x):
            print("{}".format(my_list[numbers]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
