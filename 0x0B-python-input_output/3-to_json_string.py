#!/usr/bin/python3
"""
This module returns JSON representation of an object(str)
"""
import json


def to_json_string(my_obj):
    """
    function initializes and defines a JSON
    object
    """
    new_string = json.dumps(my_obj)
    return new_string
