#!/usr/bin/python3

""" read_file - function that reads a text file (UTF8) """


def read_file(filename=""):
    """ read_file function """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
