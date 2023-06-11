#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        n = len(my_list)
        my_list.sort()
        return my_list[n - 1]
