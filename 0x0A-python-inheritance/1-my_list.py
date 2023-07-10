#!/usr/bin/python3

""" class MyList that inherits from list """


class MyList(list):
    """ represent a MyList class """
    def print_sorted(self):
        output = sorted(self)
        print(output)
