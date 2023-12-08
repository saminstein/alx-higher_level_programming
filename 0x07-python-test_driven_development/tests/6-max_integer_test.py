#!/usr/bin/python3

"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
  """
  A class to test the max integer function
  """
  def test_max_integer(self):
    """
    test the max integer in a list when the integer in the list  is positive, negative, float or None
    """
    self.assertEqual(max_integer([1, 2, 3]), 3)
    self.assertEqual(max_integer([-1, -2, -3]), -1)
    self.assertEqual(max_integer([5, -6, -7]), 5)
    self.assertEqual(max_integer([1.2, 5.2, 3.0, 6.0]), 6.0)
    self.assertIsNone(max_integer([]), None)
    
  if __name__ == "__main__":
    unittest.main()