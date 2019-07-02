#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.city import City
import os
import pep8


class test_user(unittest.TestCase):
    '''Tests user class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.city1 = City()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.city1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def docstring_class_class(self):
         self.assertIsNotNone(City.__doc__)

    def check_if_hasattr(self):
        '''Checks if the methods exists'''
	self.assertTrue(hasattr(City, "created_at"))
        self.assertTrue(hasattr(City, "updated_at"))
        self.assertTrue(hasattr(City, "id"))
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def constructor_test(self):
        '''Tests for the constructor'''
        self.assertTrue(isinstance(self.city1, BaseModel))

    def save_method_test(self):
        '''Tests save method'''
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.city.id))

    def created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.city.created_at))

    def updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.city.updated_at))

    def dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.city.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.city))


if __name__ == "__main__":
    unittest.main()
