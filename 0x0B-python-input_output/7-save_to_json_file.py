#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, mode='w', encoding='utf-8') as f:
        js_data = json.dumps(my_obj)
        data = f.write(js_data)
    return data
