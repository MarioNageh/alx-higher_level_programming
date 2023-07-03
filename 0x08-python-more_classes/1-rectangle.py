#!/usr/bin/python3
"""This Is Rectangle Module"""


class Rectangle:
    """
    this is Rectangle class
    Args:
        width (int): the width of rectagle
        height (int): the height of rectagle
    """
    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0

    @staticmethod
    def check_valid_dimention(property, value):
        """
        this function to check validty of dimention
        Args:
            property (str): string of property name
            value (int): value of dimention
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{property} must be an integer")
        if value <= 0:
            raise ValueError(f"{property} must be >= 0")

    @property
    def width(self):
        """__width getter.
        Returns:
            __width (int): horizontal dimension of rectangle
        """
        return self.__width

    @property
    def height(self):
        """__height getter.
        Returns:
            __height (int): vertical dimension of rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle
        Attributes:
            __width (int): horizontal dimension of rectangle
        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        self.check_valid_dimention("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.
        """
        self.check_valid_dimention("height", value)
        self.__height = value
