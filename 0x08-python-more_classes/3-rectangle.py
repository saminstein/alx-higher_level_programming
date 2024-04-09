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
        returns rectangle area
        """
        result = self.__width * self.__height
        return result

    def perimeter(self):
        """
        returns rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def draw_rectangle(self):
        """
        returns the rectangle with the character #
        """
        empty_str = ""
        width = self.__width
        height = self.__height

        if width == 0 or height == 0:
            return empty_str

        for rows in range(height):
            for cols in range(width):
                empty_str += "#"

            if rows != height - 1:
                empty_str += "\n"

            return empty_str

    def __str__(self):
        """
        returns a string representation
        """
        return self.draw_rectangle()
