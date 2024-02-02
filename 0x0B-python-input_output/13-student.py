#!/usr/bin/python3
"""
student to disk and reload module
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            result_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result_dict[attr] = getattr(self, attr)
            return result_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the student instance
        """
        for attr in json:
            self.__dict__[attr] = json[attr]
