#!/usr/bin/python3
"""
module function that reads from a text file
"""


def read_file(filename=""):
    """
    function that reads from a file
    """

    with open(filename, 'r', encoding="UTF8") as f:
        read_line = f.read()
        print(read_line, end='')
