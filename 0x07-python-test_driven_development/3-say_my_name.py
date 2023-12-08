#!/usr/bin/python3

"""
This module contains a function that prints my name
"""

def say_my_name(first_name, last_name=""):
  """
  prints the names
  
  Parameter:
    first_name: The first name (str)
    last_name: The last name (str)
  
  Raises:
    TypeError: first_name must be a string or last_name must be a string
  """
  
  if not isinstance(first_name, str):
    raise TypeError("first_name must be a string")
  if not isinstance(last_name, str):
    raise TypeError("last_name must be a string")
    
  print("My name is", first_name, last_name)