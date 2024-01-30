#!/usr/bin/python3

"""
Test module for verifying the functionality of the Square class
"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    ''' class to test the Square class '''

    def test_pep8_sqr(self):
        ''' function to check PEP8 '''

        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0, 'PEP8 style issues found')

    def test_cl_constructor_int(self):
        ''' test class constructor parameters with integer values '''

        s2 = Square(4, 1, 2, 5)
        self.assertEqual(s2.size, 4)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 2)
        self.assertEqual(s2.id, 5)

    def test_default_attr(self):
        ''' test with only square value provided '''

        s2 = Square(8)
        self.assertEqual(s2.size, 8)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)
        self.assertIsNotNone(s2.id)

    def test_size_property(self):
        s2 = Square(5)
        s2.size = 8
        self.assertEqual(s2.size, 8)

    def test_type_params(self):
        '''
        tests with different types of
        parameters for the square class:
        'size, 'x', 'y'
        '''

        with self.assertRaises(TypeError):
            s1 = Square(5.1)

        with self.assertRaises(TypeError):
            s1 = Square('')

        with self.assertRaises(TypeError):
            s1 = Square(None)

        with self.assertRaises(ValueError):
            s1 = Square(-2)

        with self.assertRaises(TypeError):
            s1 = Square(6, 1.2)

        with self.assertRaises(TypeError):
            s1 = Square(9, '')

        with self.assertRaises(TypeError):
            s1 = Square(2, None)

        with self.assertRaises(ValueError):
            s1 = Square(8, -1)

        with self.assertRaises(TypeError):
            s1 = Square(7, 3, 2.5)

        with self.assertRaises(TypeError):
            s1 = Square(8, 6, '')

        with self.assertRaises(TypeError):
            s1 = Square(8, 9, None)

        with self.assertRaises(ValueError):
            s1 = Square(5, 12, -7)

    def test_update_all_attr(self):
        ''' test to update all attr of the Square Class '''

        s3 = Square(10, 20, 30, 40)
        s3.update(40, 30, 20, 10)
        self.assertEqual(s3.id, 40)
        self.assertEqual(s3.size, 30)
        self.assertEqual(s3.x, 20)
        self.assertEqual(s3.y, 10)

    def test_update_empty_attr(self):
        ''' tests update with no attribute '''
        s3 = Square(8, 4, 6, 2)
        s3.update()
        self.assertEqual(s3.id, 2)
        self.assertEqual(s3.size, 8)
        self.assertEqual(s3.x, 4)
        self.assertEqual(s3.y, 6)

    def test_update_empty_kwargs(self):
        ''' tests update with empty kwargs '''

        s3 = Square(9, 12)
        s3.update()
        self.assertEqual(s3.id, 37)
        self.assertEqual(s3.size, 9)
        self.assertEqual(s3.x, 12)
        self.assertEqual(s3.y, 0)

    def test_to_dictionary(self):
        ''' test using only default value '''

        s4 = Square(10, 2, 1)
        s4_dictionary = s4.to_dictionary()
        expected = "{'id': 22, 'size': 10, 'x': 2, 'y': 1}"
        self.assertEqual(str(s4_dictionary), expected)

    def test_to_dictionary_values(self):
        ''' test with specified values '''

        s4 = Square(9, 1)
        s4_dictionary = s4.to_dictionary()
        expected = "{'id': 24, 'size': 9, 'x': 1, 'y': 0}"
        self.assertEqual(str(s4_dictionary), expected)

    def test_to_dictionary_type(self):
        ''' test type of returned object '''

        s4 = Square(1, 1)
        s4_dictionary = s4.to_dictionary()
        self.assertIsInstance(s4_dictionary, dict)
