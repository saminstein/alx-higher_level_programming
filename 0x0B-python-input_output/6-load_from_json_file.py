#!/usr/bin/python3
"""
module to Create object from a JSON file
"""
import json


def load_from_json_file(filename):
    """
    function that Creates object from a JSON file

    Args:
        filename: name of file
    """
    with open(filename, mode='r') as f:
        data = json.load(f)
    return data
