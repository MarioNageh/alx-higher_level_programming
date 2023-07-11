#!/usr/bin/python3
"""this function to read python files"""


def append_write(filename="", text=""):
    """this function to append_write"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
