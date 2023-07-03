#!/usr/bin/python3

""" define a rectangle """


class Rectangle:
    """ represen a Rectangle """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

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
        sy = str(self.print_symbol)
        s = ""

        for y in range(0, h):
            for x in range(0, w):
                s += sy
            if y != h - 1:
                s += '\n'
        return s

    def __repr__(self):
        s = "Rectangle({}, {})".format(str(self.width), str(self.height))
        return s

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
