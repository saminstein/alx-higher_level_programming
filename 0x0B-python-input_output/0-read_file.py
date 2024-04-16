#!/usr/bin/python3
"""
read file
"""


def read_file(filename=""):
    """
    function that reads from a file
    """

    with open(filename, 'r', encoding="UTF8") as f:
        line = f.read()
        print(line, end='')
