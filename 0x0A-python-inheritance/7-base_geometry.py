#!/usr/bin/python3

""" define BaseGeometry class """


class BaseGeometry:
    """ represent BaseGeometry class """

    def area(self):
        """ def area(self): that raises an Exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            if value is not an integer: raise a TypeError exception
            if value is less or equal to 0: raise a ValueError exception
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
