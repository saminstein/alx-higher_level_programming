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
    
  def update(self, *args, **kwargs):
    ''' updates the square attributes '''
    
    attr = ['id', 'size', 'x', 'y']
    
    for i, arg in enumerate(args):
      if i < len(attr):
        setattr(self, attr[i], arg)
    
    for key, value in kwargs.items():
      if key in attr:
        setattr(self, key, value)
        
  def to_dictionary(self):
    ''' function that returns the dictionary representation of a square '''
    
    d_ict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
    return d_ict