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

    def to_json_string(list_dictionaries):
        """
          returns the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        else:
            return json.dumps(list_dictionaries)