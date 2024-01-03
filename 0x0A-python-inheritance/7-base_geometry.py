#!/usr/bin/python3

"""
An integer validator module
"""

class BaseGeometry:
  """
  A super class for geometrical shapes or objects.
  """
  
  def area(self):
    """
    This function just raises an exception when called
    """
    
    raise Exception("area() is not implemented")
  
  def integer_validator(self, name, value):
    """
    Validates an integer value
    
    Args:
      name (str): The name of the value
      value (int): The value
      
    Raises:
      TypeError: if 'value' is not an integer
      ValueError: if 'value' is less or equal to zero
    """
    
    self.name = name
    self.value = value
    
    if not isinstance(value, int):
      raise TypeError(f"{name} must be an integer")
    if value <= 0:
      raise ValueError(f"{name} must be greater than 0")