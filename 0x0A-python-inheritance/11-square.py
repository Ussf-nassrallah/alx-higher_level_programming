#!/usr/bin/python3

""" define a Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represent a Square class """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
