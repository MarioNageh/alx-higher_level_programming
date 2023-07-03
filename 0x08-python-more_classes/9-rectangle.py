#!/usr/bin/python3
"""This Is Rectangle Module"""


class Rectangle:
    """
    this is Rectangle class with private instance width
    height

    Args:
        width (int): the width of rectagle
        height (int): the height of rectagle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances -= 1

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
        if value < 0:
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

    def area(self):
        """
        Returns: the area of Rectanglue
        """
        return self.width * self.height

    def check_if_zero_dimention(self):
        """
        Returns: False if any of dimention = 0
            else True
        """
        return self.width == 0 or self.height == 0

    def perimeter(self):
        """
        Returns: the perimeter of Rectanglue
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """
        Returns: string representation of Rectangle
        """
        if self.check_if_zero_dimention():
            return ""
        rec = (f"{self.print_symbol}" * self.width + '\n') * \
            (self.height - 1) + (self.width * f"{self.print_symbol}")
        return rec

    def __repr__(self):
        """
        return rectangle arguments
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """print delete message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        this method for compare two Rectangle ares
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

        @classmethod
    def square(cls, size=0):
        """square
        Args:
            size: width == height == size
        Return:
            Rectangle new object
        """
        return Rectangle(size, size)
