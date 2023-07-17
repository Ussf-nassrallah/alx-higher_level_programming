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
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        output = json.dumps(list_dictionaries)
        return output

    @classmethod
    def save_to_file(cls, list_objs):
        """
          writes the JSON string representation of list_objs to a file:
        """
        f_name = "{}.json".format(cls.__name__)
        with open(f_name, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
          returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "[]":
            return []
        output = json.loads(json_string)
        return output

    @classmethod
    def create(cls, **dictionary):
        """
          returns an instance with all attributes already set:
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                r = cls(1, 1)
            else:
                r = cls(1)
            r.update(**dictionary)
            return r
