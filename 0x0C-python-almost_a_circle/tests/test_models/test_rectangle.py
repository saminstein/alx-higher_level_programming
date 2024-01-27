#!/usr/bin/python3

"""
Test module for verifying the functionality of the Rectangle class
"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' class to test the Rectangle class '''

    def test_pep8_rect(self):
        ''' function to check PEP8 '''

        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, 'PEP8 style issues found')

    def test_rectangle_subclass(self):
        ''' tests if Rectangle class inherits
        from Base Class '''
        
        self.assertIsTrue(issubclass(Rectangle, Base))

    def test_rectangle_param(self):
        ''' tests parameters for rectangle class '''

        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        
        with self.assertEqual(TypeError):
            r4 = Rectangle()