#!/usr/bin/python3
"""this function to read python files"""


def read_file(filename=""):
    """this function to read python files"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read())
