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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save to file"""
        data = []
        if list_objs:
            data = [x.to_dictionary() for x in list_objs]
        with open(f"{cls.__name__}.json", "w") as outfile:
            outfile.write(cls.to_json_string(data))

    @staticmethod
    def from_json_string(json_string):
        """this function converts and returns a dictionary representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' create object and update it with dictionary '''
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        else:
            return None
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ''' load json from file and convert to
        list of instances and return them'''
        json_list = []
        try:
            with open(cls.__name__+'.json', 'r', encoding="utf-8") as f:
                json_list = cls.from_json_string(f.read())
        except Exception:
            return []

        return [cls.create(**s) for s in json_list]
