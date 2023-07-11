#!/usr/bin/python3

""" append_write - function that appends at the end of a text file """


def append_write(filename="", text=""):
    """ returns the number of characters added """
    num_of_chars = 0
    with open(filename, 'a', encoding='utf-8') as file:
        num_of_chars = file.write(text)
    return num_of_chars
