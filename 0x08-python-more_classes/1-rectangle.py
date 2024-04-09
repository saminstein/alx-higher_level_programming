#!/usr/bin/python3

"""
  defines a rectangle based on the empty class
"""


class Rectangle:
    """
    An empty rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        checks parameter and initialize some values
        Args:

            width: The width of  the rectangle
            height: The height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ 
        returns the width of the rctangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """
        height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
