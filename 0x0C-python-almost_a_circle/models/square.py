#!/usr/bin/python3
"""this is square Classification"""
from .rectangle import Rectangle

class Square(Rectangle):
    """this is square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """this is square class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is Square String Representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y}"\
            f" - {self.width}"
