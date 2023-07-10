#!/usr/bin/python3
"""This File Checks if the object is Type Of Parent Class"""


def inherits_from(obj, a_class):
    """Checks if the specified instance of Class"""
    return isinstance(obj, a_class) and type(obj) != a_class
