#!/usr/bin/python3
"""
A Subclass square module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square subclass
    """
    def __init__(self, size):
        """
        Instantiation with size
        """
        self.__size = size

        super().__init__(size, size)

    def area(self):
        """
        returns the area
        """
        return self.__size ** 2

    def __str__(self):
        """
        prints
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
