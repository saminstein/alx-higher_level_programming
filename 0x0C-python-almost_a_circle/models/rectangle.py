#!/usr/bin/python3

from models.base import Base 

class Rectangle(Base):
  def __init__(self, width, height, x=0, y=0, id=None):
    ''' constructor initializes a rectangle with dimensions, postions & id '''
    super().__init__(id)
    self.__width = width
    self.__height = height
    self.__x = x
    self.__y = y
    
  @property
  def width(self):
    ''' retrieves the value of the private attr '''
    return self.__width
    
  @width.setter
  def width(self, value):
    ''' sets the value of the private attr '''
    self.__width = value


  @property
  def height(self):
    ''' retrieves the value of the private attr '''
    return self.__height
    
  @height.setter
  def height(self, value):
    ''' sets the value of the private attr '''
    self.__height = value
   
 
  @property
  def x(self):
    ''' retrieves the value of the private attr '''
    return self.__x
  
  @x.setter
  def x(self, value):
    ''' sets the value of the private attr '''
    self.__x = value
  

  @property
  def y(self):
    ''' retrieves the value of the private attr '''
    return self.__y
    
  @y.setter
  def y(self, value):
    ''' sets the value of the private attr '''
    self.__y = value
  
  
  @property
  def id(self):
    ''' retrieves the value of the private attr '''
    return self.__id
    
  @id.setter
  def id(self, value):
    ''' sets the value of the private attr '''
    self.__id = value
    