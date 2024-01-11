#!/usr/bin/python3
"""
Student to json with filter module
"""
#Student = __import__('11-student').Student

class Student:
  """
  initialize a public student instance
  """
  def __init__(self, first_name, last_name, age):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    
  def to_json(self, attrs=None):
    """
    method that retrieves a dict rep of a student instance
    
    Parameters:
      attr(list): a list of attribute names to retrieve. if attribute containd thr default 'None', retrieve all attributes
    
    Returns:
      dict: a dictionary containing attributes of a Student instance 
    """
    
    if attrs is not None:
      result_dict = {}
      for attr in attrs:
        if hasattr(self, attr):
          result_dict[attr] = getattr(self, attr)
      return result_dict
    else:
      return self.__dict__
  
  """
  def reload_from_json(self, json):

    for attr in json:
      self.__dict__[attr] = json[attr]
  """