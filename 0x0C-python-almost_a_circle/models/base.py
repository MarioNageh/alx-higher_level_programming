#!/usr/bin/python3
"""This Module Is Python Base Class"""


class Base:
    """This Class Is Python Base Class"""
    _nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor"""
        self.id = id
        self._nb_objects += 1