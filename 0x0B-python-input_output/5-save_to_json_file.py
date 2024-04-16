#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    converts an object to JSON and sav in a text file

    Args:
        my_obj: object to save to a file
        filename: The name of the file where the JSON
        will be stored
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        js_data = json.dumps(my_obj)
        data = f.write(js_data)
    return data
