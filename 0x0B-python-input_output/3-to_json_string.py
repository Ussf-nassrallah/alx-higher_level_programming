#!/usr/bin/python3

""" function that returns the JSON repre of an object (string) """
import json


def to_json_string(my_obj):
    return json.dumps(my_obj)
