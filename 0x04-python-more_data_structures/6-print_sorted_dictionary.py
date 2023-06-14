#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dictionary_keys = a_dictionary.keys()
    sorted_di_keys = sorted(dictionary_keys)
    for ele in sorted_di_keys:
        print("{}: {}".format(ele, a_dictionary[ele]))
