#!/usr/bin/python3
"""This Module Is Python Base Class"""
import json


class Base:
    """This Class Is Python Base Class"""
    _nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' convert list of dict represent objects to json string '''
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
