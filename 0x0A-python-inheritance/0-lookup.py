#!/usr/bin/python3
def lookup(obj):
    """
    this function returns All atributes of the given object
    :param obj:
    :return: list of all attributes of the given object
    """
    return dir(obj)
