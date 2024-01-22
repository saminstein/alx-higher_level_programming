#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
  def __init__(self, size, x=0, y=0, id=None):
    ''' class constructor[super] that calls the constructor in the parent class[rectangle] and automatically assigns sets <width> & <height> to <size> '''
    
    super().__init__(size, size, x, y, id)
    
  def __str__(self):
    return f'[Square] ({self.id}), {self.x}/{self.y} - {self.size}'
  
  @property
  def size(self):
    return self.width
    
  @size.setter
  def size(self, value):
    self.width = value
    self.height = value