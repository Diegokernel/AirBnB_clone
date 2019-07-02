#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.amenity import Amenity
from datetime import datetime
import os
import pep8


class test_user(unittest.TestCase):
    '''Tests user class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.amenity1 = Amenity()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.amenity1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/amenity.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_class_class(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_check_if_hasattr(self):
        '''Checks if the methods exists'''
        self.assertTrue(hasattr(Amenity, "name"))

    def test_constructor(self):
        '''Tests for the constructor'''
        self.assertTrue(isinstance(self.amenity1, BaseModel))

    def test_save_method(self):
        '''Tests save method'''
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_id_fun(self):
        """ test id functionality """
        self.assertEqual(str, type(self.amenity1.id))

    def test_created_at_fun(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.amenity1.created_at))

    def test_updated_at_fun(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.amenity1.updated_at))

    def test_dictionary(self):
        '''Tests to_dict method'''
        test_dict = self.amenity1.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.amenity1))


if __name__ == "__main__":
    unittest.main()
