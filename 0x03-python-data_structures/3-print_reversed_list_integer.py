#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    n = len(my_list)
    my_list.reverse()
    for index in range(0, n):
        print("{:d}".format(my_list[index]))
