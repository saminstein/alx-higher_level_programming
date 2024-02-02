#!/usr/bin/python3
from os import path
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

emp_list = []
num_arg = len(argv)

if path.exists('add_item.json'):
    obj_json = load_from_json_file('add_item.json')
else:
    obj_json = emp_list

for i in range(1, num_arg):
    obj_json.append(argv[i])

save_to_json_file(obj_json, 'add_item.json')
