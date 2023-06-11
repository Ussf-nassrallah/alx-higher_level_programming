#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    n = len(my_list)
    output = []
    for index in range(0, n):
        if my_list[index] % 2 == 0:
            output.append(True)
        else:
            output.append(False)
    return output
