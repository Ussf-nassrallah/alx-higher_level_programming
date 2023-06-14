#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = set(my_list)
    output = 0
    for num in new_list:
        output += num
    return output
