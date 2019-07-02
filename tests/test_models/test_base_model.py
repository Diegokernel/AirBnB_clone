#!/usr/bin/python3
'''Unittest for base_model'''
import unittest
from models.base_model import BaseModel
import os
import pep8


class test_base_model(unittest.TestCase):
    '''Tests BaseModel class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.base1 = BaseModel()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.base1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = style.check_files(['models/base_model.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_test(self):
        '''Checks for docs'''
        for doc_fun in dir(BaseModel):
            self.assertIsNotNone(doc_fun.__doc__)

    def test_docstring_class_class(self):
        self.assertIsNotNone(BaseModel.__doc__)

    
    def test_dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.basemodel.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.basemodel))


if __name__ == "__main__":
    unittest.main()
