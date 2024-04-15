#!/usr/bin/python3

"""
module checks class and subclass
"""

def is_kind_of_class(obj, a_class):
    """
    returns True if the object is an instance of, or
    if the object is an instance of a class that inhe
    rited from, the specified class ; otherwise False
    """
    what_class = isinstance(obj, a_class)
    return what_class
