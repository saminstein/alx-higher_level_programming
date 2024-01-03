#!/usr/bin/python3

class Rectangle:
  def __init__(self, width=0, height=0):
    self.__width = width
    self.__height = height
    
  @property
  def width(self):
    return self.__width
    
  @width.setter
  def width(self, value):
    self.__width = value
    if type(value) is not int:
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
      
  @property
  def height(self):
    return self.__height
      
  @height.setter
  def height(self, value):
    self.__height = value
    if type(value) is not int:
      raise TypeError("width must be an integer")
    if value < 0:
      raise ValueError("width must be >= 0")
        
  def area(self):
    result = self.__width * self.__height
    return result
      
  def perimeter(self):
    if self.__width == 0 or self.__height == 0:
      return 0
    else:
      return 2 * (self.__width + self.__height)
  