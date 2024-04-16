#!/usr/bin/python3
"""
function that returns an object
(Python data structure) represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Args:
        my_str: JSON string to convert

    Returns:
        returns an object (Python data structure) rep
        resented by a JSON string
    """
    data = json.loads(my_str)
    return data
