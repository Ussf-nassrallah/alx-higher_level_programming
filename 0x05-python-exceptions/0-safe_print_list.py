#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for index in range(0, x):
        try:
            print("{}".format(my_list[index]), end="")
            count = count + 1
        except IndexError:
            break
    print()
    return count
