#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.review import Review
from datetime import datetime
import os
import pep8


class test_review(unittest.TestCase):
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

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/review.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_class_class(self):
        self.assertIsNotNone(Review.__doc__)

    def test_check_if_hasattr(self):
        '''Checks if the methods exists'''
        self.assertTrue(hasattr(Review, "place_id"))
        self.assertTrue(hasattr(Review, "text"))
        self.assertTrue(hasattr(Review, "user_id"))

    def test_save_method_test(self):
        '''Tests save method'''
        self.review1.save()
        self.assertNotEqual(self.review1.created_at, self.review1.updated_at)

    def test_id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.review1.id))

    def test_created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.review1.created_at))

    def test_updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.review1.updated_at))

    def test_dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.review1.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.review1))


if __name__ == "__main__":
    unittest.main()
