#!/usr/bin/python3

""" Define a square Class """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Represent a Square class """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if args and len(args) != 0:
            index = 0
            for argument in args:
                if index == 0:
                    if argument is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = argument
                elif index == 1:
                    self.size = argument
                elif index == 2:
                    self.x = argument
                elif index == 3:
                    self.y = argument
                index += 1
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def __str__(self):
        _id = self.id
        _x = self.x
        _y = self.y
        _w = self.width
        s = "[Square] ({}) {}/{} - {}"
        return s.format(_id, _x, _y, _w)

    def to_dictionary(self):
        dic = {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
        return dic
