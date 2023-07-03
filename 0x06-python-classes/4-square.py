#!/usr/bin/python3

""" define a Square """


class Square:
    """ represent a square """
    def __init__(self, size=0):
        """ create a new square """
        self.__size = size

    def area(self):
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        """ __size: private instance attribute """
        self.__size = value