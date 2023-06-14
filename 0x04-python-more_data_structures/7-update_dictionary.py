#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    dictionary_keys = a_dictionary.keys()
    if key in dictionary_keys:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
