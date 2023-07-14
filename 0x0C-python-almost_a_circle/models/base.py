#!/usr/bin/python3

""" define a Base class """


class Base:
    """ represent a Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects
