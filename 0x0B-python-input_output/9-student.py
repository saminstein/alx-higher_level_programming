#!/usr/bin/python3

"""
 A class Student module
"""


class Student:
    """
    class that creates student instances
    """

    def __init__(self, first_name, last_name, age):
        """ initializes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary description
        """
        return self.__dict__
