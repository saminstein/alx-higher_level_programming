#!/usr/bin/python3

"""
empty class rectangle that defines a rectangle
"""


class Rectangle:
    """ class rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
        return the area of a rectangle
        """
        result = self.__width * self.__height
        return result

    def perimeter(self):
        """
        return the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def draw_rectangle(self):
        """
        prints #
        """
        empty_str = ""
        width = self.__width
        height = self.__height

        if width == 0 or height == 0:
            return empty_str

        for rows in range(height):
            for cols in range(width):
                empty_str += str(self.print_symbol)

            if rows != height - 1:
                empty_str += "\n"

        return empty_str

    def __str__(self):
        """
        return a string representation of an instance
        """
        return self.draw_rectangle()

    def __repr__(self):
        """
        return a string with the representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints the message when an instance of the rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
