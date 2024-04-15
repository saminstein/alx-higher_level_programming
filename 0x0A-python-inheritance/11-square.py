#!/usr/bin/python3
"""
subclass of a square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """
        return the area
        """
        return self.__size ** 2

    def __str__(self):
        """
        prints
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
