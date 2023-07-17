#!/usr/bin/python3

""" define a Base class """

import json


class Base:
    """ represent a Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init a new Base """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
          returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
