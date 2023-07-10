#!/usr/bin/python3

""" checks if an object is exactly an instance of the specified class """


def is_same_class(obj, a_class):
    """ is_same_class function """
    output = type(obj) is a_class
    return output
