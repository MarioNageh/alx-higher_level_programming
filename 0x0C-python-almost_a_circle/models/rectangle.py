#!/usr/bin/python3
"""this is Rectangle Classes"""
from .base import Base


class Rectangle(Base):
    """this is Rectangle Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """this is Rectangle Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """this is Rectangle Width Setter"""
        self.__width = value

    @property
    def height(self):
        """this is Rectangle Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this is Rectangle Height Setter"""
        self.__height = value

    @property
    def x(self):
        """this is Rectangle X"""
        return self.__x

    @x.setter
    def x(self, value):
        """this is Rectangle X Setter"""
        self.__x = value

    @property
    def y(self):
        """this is Rectangle Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """this is Rectangle Y Setter"""
        self.__y = value
