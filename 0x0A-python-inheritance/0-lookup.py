#!/usr/bin/python3
"""This module contains methods to look up for objects"""


def lookup(obj):
    """
    this function returns All atributes of the given object
    :param obj:
    :return: list of all attributes of the given object
    """
    return dir(obj)
