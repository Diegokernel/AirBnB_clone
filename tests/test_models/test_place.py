#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.place import Place
from datetime import datetime
import os
import pep8


class test_place(unittest.TestCase):
    '''Tests user class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.place1 = Place()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.place1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/place.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_class_class(self):
        self.assertIsNotNone(Place.__doc__)

    def test_check_if_hasattr(self):
        '''Checks if the methods exists'''
        self.assertTrue(hasattr(Place, "city_id"))
        self.assertTrue(hasattr(Place, "user_id"))
        self.assertTrue(hasattr(Place, "name"))
        self.assertTrue(hasattr(Place, "description"))
        self.assertTrue(hasattr(Place, "number_rooms"))
        self.assertTrue(hasattr(Place, "number_bathrooms"))
        self.assertTrue(hasattr(Place, "max_guest"))
        self.assertTrue(hasattr(Place, "price_by_night"))
        self.assertTrue(hasattr(Place, "latitude"))
        self.assertTrue(hasattr(Place, "longitude"))
        self.assertTrue(hasattr(Place, "amenity_ids"))

    def test_save_method_test(self):
        '''Tests save method'''
        self.place1.save()
        self.assertNotEqual(self.place1.created_at, self.place1.updated_at)

    def test_id_fun_test(self):
        """ test id functionality """
        self.assertEqual(str, type(self.place1.id))

    def test_created_at_fun_test(self):
        """ test created_at functionality"""
        self.assertEqual(datetime, type(self.place1.created_at))

    def test_updated_at_fun_test(self):
        """ test updated_at functionality"""
        self.assertEqual(datetime, type(self.place1.updated_at))

    def test_dictionary_test(self):
        '''Tests to_dict method'''
        test_dict = self.place1.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.place1))


if __name__ == "__main__":
    unittest.main()
