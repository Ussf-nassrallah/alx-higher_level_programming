#!/usr/bin/python3

class Square:
    """ represent a square """
    def __init__(self, size=0):
        """ create a new square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            print("size must be >= 0")
        else:
            self.__size = size
