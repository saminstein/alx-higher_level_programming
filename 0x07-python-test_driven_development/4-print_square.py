#!/usr/bin/python3

"""
module defines a square that prints a square with the # character
"""

def print_square(size):
    """
    size of the square to print with the # character
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    for rows in range(size):
        for cols in range(size):
            print("#", end="")
        print("")
