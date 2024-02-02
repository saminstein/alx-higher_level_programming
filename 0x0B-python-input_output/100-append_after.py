#!/usr/bin/python3

"""
search and update module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a
    file, after each line containing a
    specific string

    Parameters:
      filename: the file that contains the
      original text
      search_string: the string to find before
      appending
      new_string: the new string to add to the
      file

    Return: An updated string written back
    into the file after appending
    """

    with open(filename, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if search_string in line:
                lines[i] += new_string

        f.seek(0)

        f.writelines(lines)
