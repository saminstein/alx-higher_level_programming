#!/usr/bin/python3
""" class Square that defines a square"""


class Square:
    """ class Square that defines a square"""

    def __init__(self, size=0):
        """ initializes a square

        args:
            value (int): size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """ sets private size

        Returns:
               private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ The size setter method update the size value of the square.

        args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ returns the area

        Returns:
               the area
        """
        return (self.__size) ** 2

    def my_print(self):
        """prints #"""

        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
            print()
