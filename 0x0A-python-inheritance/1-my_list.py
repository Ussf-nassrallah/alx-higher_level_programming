#!/usr/bin/python3

""" class MyList that inherits from list """


class MyList(list):
    """ represent a MyList class """
    def print_sorted(self):
        if not all(isinstance(ele, int) for ele in self):
            raise TypeError("all the elements of the list must be of type int")
        output = sorted(self)
        print(output)
