#!/usr/bin/python3
"""this function to convert python object to string"""
import json


def to_json_string(my_obj):
    """this function to convert python object to json string"""
    return json.dumps(my_obj)
