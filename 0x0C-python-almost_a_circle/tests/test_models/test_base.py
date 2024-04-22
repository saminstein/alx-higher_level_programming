#!/usr/bin/python3
"""
Test module for verifying the functionality of the Base class
"""

import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    ''' class to test the base class '''

    def test_pep8_base(self):
        ''' function to check PEP8 '''

        style = pep8.StyleGuide(quit=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0, 'PEP 8 style issues found')

    def setUp(self):
        ''' imports module, Instantiates class '''
        Base._Base__nb_objects = 0

    def test_base_instance(self):
        ''' tests a Base Class Instance '''

        base_instance = Base()
        self.assertIsInstance(base_instance, Base)
        self.assertTrue(isinstance(base_instance, Base))

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
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_id_string(self):
        ''' test for string Base Class id '''

        base_instance = Base('Holberton')
        self.assertEqual(base_instance.id, 'Holberton')
        base_instance = Base('School')
        self.assertEqual(base_instance.id, 'School')

    def test_to_json_string(self):
        ''' test for when data is not None in json_string method '''

        r1 = Rectangle(19, 10, 7, 3, 1)
        r1_dict = r1.to_dictionary()
        json_str = Base.to_json_string([r1_dict])
        self.assertIsInstance(json_str, str)

    def test_empty_to_json_string(self):
        ''' test for when data is empty or None in the json_string method '''

        empty_dict = []
        json_str = Base.to_json_string(empty_dict)
        self.assertEqual(json_str, '[]')

        no_data = None
        json_str = Base.to_json_string(no_data)
        self.assertEqual(json_str, '[]')

    def test_save_to_file(self):
        ''' test to check if calling 'dict' raises error '''

        with self.assertRaises(AttributeError) as err:
            Base.save_to_file([None])

        self.assertEqual(
             "'NoneType' object has no attribute 'to_dictionary'",
             str(err.exception))

    def test_from_json_string(self):
        ''' test for from_json_string method '''
        list_input = [{'id': 89, 'width': 10, 'height': 4}]

        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(list, type(list_output))

    def test_load_from_file(self):
        ''' tests the load_from_file method '''

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]

        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()

        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_input = [s1, s2]

        Square.save_to_file(list_input)
        list_output = Square.load_from_file()

        self.assertNotEqual(id(list_input[0]), id(list_output[0]))
        self.assertEqual(str(list_input[0]), str(list_output[0]))
        self.assertNotEqual(id(list_input[1]), id(list_output[1]))
        self.assertEqual(str(list_input[1]), str(list_output[1]))

    def test_create(self):
        '''
        test to check if the create instance has the correct attribute
        '''

        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)

        self.assertEqual(str(r1), str(r2))
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
