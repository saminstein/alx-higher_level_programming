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
    if list_dictionaries is None:
      return "[]"
    else:
      json_str = json.dumps(list_dictionaries)
      return json_str