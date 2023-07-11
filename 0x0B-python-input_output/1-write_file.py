#!/usr/bin/python3
"""this function to write to the filedescriptor"""


def write_file(filename='', text=''):
    """write a text of the file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
