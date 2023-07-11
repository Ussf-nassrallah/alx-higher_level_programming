#!/usr/bin/python3

""" write_file - function that writes a str to a text file """


def write_file(filename="", text=""):
    """ returns the number of characters written """
    num_of_chars = 0
    with open(filename, 'w', encoding='utf-8') as file:
        num_of_chars = file.write(text)
    return num_of_chars
