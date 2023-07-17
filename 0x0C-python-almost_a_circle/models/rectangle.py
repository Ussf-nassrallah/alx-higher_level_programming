#!/usr/bin/python3
""" Define a Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Represent a Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init a new rectangle """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ return the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ return the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ return the x value of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ return the y value of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return the area of the Rectangle."""
        result = self.width * self.height
        return result

    def display(self):
        """ display method """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for y in range(self.y):
            print("")
        for col in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for row in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """ update method """
        if args and len(args) != 0:
            index = 0
            for argument in args:
                if index == 0:
                    if argument is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = argument
                elif index == 1:
                    self.width = argument
                elif index == 2:
                    self.height = argument
                elif index == 3:
                    self.x = argument
                elif index == 4:
                    self.y = argument
                index += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ return the dict of the Rectangle."""
        dic = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return dic

    def __str__(self):
       """ __str__ method """
        _id = self.id
        _w = self.width
        _h = self.height
        _x = self.x
        _y = self.y
        s = "[Rectangle] ({}) {}/{} - {}/{}"
        return s.format(_id, _x, _y, _w, _h)
