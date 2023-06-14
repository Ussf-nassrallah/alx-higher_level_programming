#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    new_dictionary_keys = list(new_dictionary.keys())
    for ele in new_dictionary_keys:
        new_dictionary[ele] = new_dictionary[ele] * 2
    return new_dictionary
