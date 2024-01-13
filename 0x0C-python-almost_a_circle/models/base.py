#!/usr/bin/python3

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