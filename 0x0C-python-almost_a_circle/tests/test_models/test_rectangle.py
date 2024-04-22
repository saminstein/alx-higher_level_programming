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

        self.assertTrue(issubclass(Rectangle, Base))

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

        with self.assertRaises(TypeError):
            r4 = Rectangle()

    def test_type_params(self):
        '''
        tests with different types of
        parameters for the rectangle class:
        'width, 'height', 'x', 'y'
        '''

        with self.assertRaises(TypeError):
            r1 = Rectangle(5.1, 3, 7, 8)

        with self.assertRaises(TypeError):
            r1 = Rectangle('', 3, 7, 8)

        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 3, 7, 8)

        with self.assertRaises(ValueError):
            r1 = Rectangle(-41567, 3, 7, 8)

        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 4.2, 7, 8)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, '', 8, 9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, None, 8, 9)

        with self.assertRaises(ValueError):
            r1 = Rectangle(7, -21113, 8, 9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, 6.3, 9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, '', 9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, None, 9)

        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 8, -11678, 9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, 9, 8.9)

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, 9, '')

        with self.assertRaises(TypeError):
            r1 = Rectangle(7, 8, 9, None)

        with self.assertRaises(ValueError):
            r1 = Rectangle(7, 8, 9, -8)

    def test_area(self):
        ''' tests for width and height '''

        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.area(), 20)

    def test_str_(self):
        ''' test the str method '''

        r1 = Rectangle(3, 2, 1, 1, 4)
        self.assertEqual(str(r1), '[Rectangle] (4) 1/1 - 3/2')

    def test_invalid_arg(self):
        ''' tests invalid args '''
        with self.assertRaises(TypeError):
            r1 = Rectangle(3, 2, 1, 1, 4, 10)

    def test_to_dictionary_values(self):
        ''' test with specified values '''

        r4 = Rectangle(1, 1)
        r4_dictionary = r4.to_dictionary()
        expected = "{'id': 3, 'width': 1, 'height': 1, 'x': 0, 'y': 0}"
        self.assertEqual(str(r4_dictionary), expected)

if __main__ == '__main__':
    unittest.main()
