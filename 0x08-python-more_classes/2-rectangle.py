#!/usr/bin/python3

class Rectangle:
    """
    checks parameter and initialize some values

    Args:
        width: The width of  the rectangle
        height: The height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width
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
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """
        return rectangle area
        """
        result = self.__width * self.__height
        return result

    def perimeter(self):
        """
        return rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
