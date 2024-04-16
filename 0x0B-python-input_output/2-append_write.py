#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """
    function that intializes a file that appends a te
    xt, If the file doesn’t exist, it should be creat
    ed
    """
    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
