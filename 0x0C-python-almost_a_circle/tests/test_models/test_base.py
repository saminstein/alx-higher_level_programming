#!/usr/bin/python3

"""
module that test different scenerios for the Base class
"""

import unittest
import pep8
import os
from ..models.base import Base
from ..models.rectangle import Rectangle
from ..models.square import Square

class TestBase(unittest.TestCase):
  ''' class to test the base class '''
  
  def test_pep8_base(self):
    ''' function to check PEP8 '''
    
    style = pep8.StyleGuide(quit=True)
    result = style.check_files(['models/base.py'])
    self.assertEqual(result.total_errors, 0, 'PEP 8 style issues found')
    
  def test_id_with_positive(self):
    ''' tests for positive Base Class id '''
    
    base_instance = Base(51)
    self.assertEqual(base_instance.id, 51)
    base_instance = Base(19)
    self.assertEqual(base_instance.id, 19)
    
  def test_id_with_neg(self):
    ''' tests for negative Base Class id '''
    
    base_instance = Base(-21)
    self.assertEqual(base_instance.id, -21)
    base_instance = Base(-68)
    self.assertEqual(base_instance.id, -68)
    
  def test_id_none(self):
    ''' tests for none Base Class id '''
    
    base_instance = Base()
    self.assertEqual(base_instance.id, 5)
    base_instance = Base(None)
    self.assertEqual(base_instance.id, 7)
    
  def test_id_string(self):
    ''' test for string Base Class id '''
    
    base_instance = Base('Holberton')
    self.assertEqual(base_instance.id, 'Holberton')
    base_instance = Base('School')
    self.assertEqual(base_instance.id, 'School')










if __name__ == '__main__':
  unittest.main()