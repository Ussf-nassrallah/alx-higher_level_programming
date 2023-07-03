#!/usr/bin/python3

""" define a rectangle """


class Rectangle:
    """ represen a Rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        # Private instance attribute
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            p = 0
        else:
            p = (2 * self.width) + (2 * self.height)
        return p

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""

        w = self.width
        h = self.height
        s = ""

        for y in range(0, h):
            for x in range(0, w):
                s += '#'
            if y != h - 1:
                s += '\n'
        return s

    def __repr__(self):
        s = "Rectangle({}, {})".format(str(self.width), str(self.height))
        return s
