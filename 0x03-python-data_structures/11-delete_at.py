#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    n = len(my_list)
    if idx < 0 or idx >= n:
        return my_list
    else:
        del my_list[idx]
        return my_list
