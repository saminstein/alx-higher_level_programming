#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """ initializes a new square

        args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ gets size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets size value """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ gets the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the current position """
        self.__position = value
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")

        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integer")

        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")

    def area(self):
        """ function returns current area of the square """
        return (self.__size) ** 2

    def my_print(self):
        """ prints the square with # character """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
        for j in range(self.__size):
            for a in range(self.__position[0]):
                print(" ", end="")
            for b in range(self.__size):
                print("#", end="")
            print()
