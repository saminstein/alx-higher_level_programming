#!/usr/bin/python3
import json

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
    
  def to_json_string(list_dictionaries):
    ''' function that converts a dictionary to a json str '''
    if list_dictionaries is None:
      return "[]"
    else:
      json_str = json.dumps(list_dictionaries)
      return json_str
  
  @classmethod
  def save_to_file(cls, list_objs):
    ''' Function that  writes a json str representation of <list_obj> to a file
    
    Parameters:
      cls: class reference
      list_objs: list that contains objects or instances
    '''
    if list_objs is None:
      list_objs = []
    else:
      list_objs = [obj.to_dictionary() for obj in list_objs]
      
    filename = cls.__name__ + '.json'
    with open(filename, mode= 'w', encoding= 'utf-8') as file:
      json_str = cls.to_json_string(list_objs)
      file.write(json_str)