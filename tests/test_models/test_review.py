#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.review import Review
import os
import pep8


class test_user(unittest.TestCase):
    '''Tests user class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.review1 = Review()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.review1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/review.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def docstring_class_class(self):
        self.assertIsNotNone(Review.__doc__)

    def check_if_hasattr(self):
        '''Checks if the methods exists'''
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertTrue(hasattr(Review, "user_id"))

    def constructor_test(self):
        '''Tests for the constructor'''
        self.assertTrue(isinstance(self.review1, BaseModel))

    def save_method_test(self):
        '''Tests save method'''
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.review.id))

    def created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.review.created_at))

    def updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.review.updated_at))

    def dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.review.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.review))


if __name__ == "__main__":
    unittest.main()
