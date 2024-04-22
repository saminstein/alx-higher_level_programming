#!/usr/bin/python3
"""
This is the base model for module for the project
"""

import json
import os.path


class Base:
    ''' Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' class constructor to initialize instances '''
        if id is not None:
            self.id = id
        else:
            Base.incre_objects()
            self.id = Base.__nb_objects

    @classmethod
    def incre_objects(cls):
        ''' function to track the number of instances created '''
        cls.__nb_objects += 1

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' function that converts a dictionary to a json str '''
        if list_dictionaries is None:
            return "[]"
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        Function that  writes a json str representation of <list_obj> to a file

        Parameters:
          cls: class reference
          list_objs: list that contains objects or instances
        '''
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]

        filename = cls.__name__ + '.json'
        with open(filename, mode='w', encoding='utf-8') as file:
            json_str = cls.to_json_string(list_objs)
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        '''
        function that converts a json string to a dictionary

        Parameters: a string representing a list of
        dictionaries
        '''
        if json_string is None:
            return '[]'
        else:
            data_dict = json.loads(json_string)
            return data_dict

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        '''
        function to create instances with attributes initialized based on dict

        Parameters:
          cls: class <Rectangle> or <Square>
          dictionary: dictionary contains attributes, names and values

        Returns: an instance of the class with attributes set based on dict
        '''

        if cls == Rectangle:
            dummy = cls(3, 5)
        if cls == Square:
            dummy = cls(2)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' function that returns a list of instances '''

        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, mode='r', encoding='utf-8') as file:

                data = cls.from_json_string(file.read())
                instances = [cls.create(**attr) for attr in data]

                return instances
        else:
            return []
