#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.base_model import BaseModel
import os
import pep8


class test_user(unittest.TestCase):
    '''Tests user class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.user1 = User()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.user1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/user.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def docstring_class_class(self):
         self.assertIsNotNone(User.__doc__)

    def check_if_hasattr(self):
        '''Checks if the methods exists'''
        self.assertTrue(hasattr(User, "email"))
        self.assertTrue(hasattr(User, "password"))
        self.assertTrue(hasattr(User, "first_name"))
        self.assertTrue(hasattr(User, "last_name"))

    def constructor_test(self):
        '''Tests for the constructor'''
        self.assertTrue(isinstance(self.user1, BaseModel))

    def save_method_test(self):
        '''Tests save method'''
        self.user1.save()
        self.assertNotEqual(self.user1.created_at, self.user1.updated_at)

    def id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.user.id))

    def created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.user.created_at))

    def updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.user.updated_at))

    def dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.user.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.user))


if __name__ == "__main__":
    unittest.main()
