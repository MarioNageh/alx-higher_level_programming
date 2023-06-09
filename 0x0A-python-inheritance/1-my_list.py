#!/usr/bin/python3
"""This Module is New Class Instance of list"""


class MyList(list):
    """This is New Class Instance of list
    with some functionality
    """
    def print_sorted(self):
        """Prints the list in sorted order Ascending sorted order"""
        print(sorted(self))

    def append(self, __object):
        if not isinstance(__object, int):
            raise TypeError("You Must Insert Integer")
        return super().append(__object)
