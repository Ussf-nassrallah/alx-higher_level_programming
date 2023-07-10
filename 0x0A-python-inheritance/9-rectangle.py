#!/usr/bin/python3

""" define a rectangle class """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ represent a rectangle class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        className = str(self.__class__.__name__)
        w = self.__width
        h = self.__height
        return "[{}] {}/{}".format(className, w, h)
