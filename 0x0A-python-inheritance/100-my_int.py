#!/usr/bin/python3
"""This Is Repel My Int == , != Is Inverted"""


class MyInt(int):
    """this is the rebel integer"""

    def __eq__(self, other):
        """return False if other is equal to this"""
        return not super().__eq__(other)

    def __ne__(self, other):
        """return True if other is not equal to this"""
        return not super().__ne__(other)
