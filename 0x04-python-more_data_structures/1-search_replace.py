#!/usr/bin/python3

def search_replace(my_list, search, replace):
    n = len(my_list)
    new_list = my_list.copy()
    for index in range(0, n):
        if new_list[index] == search:
            new_list[index] = replace
    return new_list
