#!/usr/bin/python3
"""This Module Is Python Base Class"""


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
