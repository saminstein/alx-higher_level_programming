#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    function that writes to a text file

    Args:
        filename: filename
        text: text to write
    """
    with open(filename, mode='w', encoding='utf-8') as wf:
        return wf.write(text)
