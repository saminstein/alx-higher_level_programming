#!/usr/bin/python3

"""
This module contains function for to add two number, it could be int or float
"""

"""
def convert_int(num):
  
  function that converts a float to int
  
  Parameters:
    num: float number to convert
    
  Returns:
    int: The integer 
  
    if type(num) == float:
      num = int(num)
    return num
"""

def add_integer(a, b=98):
  """
  function that adds two integers
  
  Parameters:
    a: first number
    b: second number
  
  Returns:
  int: addition of a and b
  
  Raises:
    TypeError: a must be an integer or b must be an integer
  """
  if not isinstance(a, int) and not isinstance(a, float):
    raise TypeError("a must be an integer")
  if not isinstance(b, int) and not isinstance(b, float):
    raise TypeError("b must be an integer")
  a = int(a)
  b = int(b)
  return (a + b)
    