#!/usr/bin/python3

def no_c(my_string):
    str_len = len(my_string)
    new_string = ""
    for index in range(0, str_len):
        if my_string[index] != 'c' and my_string[index] != 'C':
            new_string += my_string[index]
    return new_string
