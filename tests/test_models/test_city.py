#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.city import City
from datetime import datetime
import os
import pep8


class test_city(unittest.TestCase):
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

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/city.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_class_class(self):
        self.assertIsNotNone(City.__doc__)

    def test_check_if_hasattr(self):
        '''Checks if the methods exists'''
        self.assertTrue(hasattr(City, "state_id"))
        self.assertTrue(hasattr(City, "name"))

    def test_save_method_test(self):
        '''Tests save method'''
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.city1.id))

    def test_created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.city1.created_at))

    def test_updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.city1.updated_at))

    def test_dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.city1.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.city1))


if __name__ == "__main__":
    unittest.main()
