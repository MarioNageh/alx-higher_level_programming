#!/bin/usr/python3
"""This Module is New Class Instance of list
with some functionality
"""


class MyList(list):
    """This is New Class Instance of list
    with some functionality
    """
    def print_sorted(self):
        """Prints the list in sorted order Ascending sorted order"""
        print(sorted(self))
