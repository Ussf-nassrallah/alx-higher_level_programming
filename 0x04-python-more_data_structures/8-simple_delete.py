#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    dictionary_keys = a_dictionary.keys()
    if key in dictionary_keys:
        del a_dictionary[key]
        return a_dictionary
    else:
        return a_dictionary
