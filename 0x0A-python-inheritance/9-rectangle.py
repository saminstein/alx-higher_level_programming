#!/usr/bin/python3
"""
Full rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
        Instantiation with width and height:
        """
        self.__width = width
        self.__height = height

        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        area of the rectangle
        """
        res = self.__width * self.__height
        return res

    def __str__(self):
        """
        print rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
