#!/usr/bin/python3
'''Unittest for base_model'''
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from console import HBNBCommand
from unittest.mock import patch
from io import StringIo
import os
import pep8


class test_base_model(unittest.TestCase):
    '''Tests BaseModel class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.consol = HBNBCommand()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.consol
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['consol.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_docstring_test(self):
        '''Checks for docs'''
        for doc_fun in dir(HBNCommand):
            self.assertIsNotNone(doc_fun.__doc__)

    def test_docstring_class_class(self):
        self.assertIsNotNone(HBNCommand.__doc__)

    def test_check_if_hasattr(self):
        """Checks if the methods exists"""
        self.assertTrue(hasattr(HBNCommand, "emptyline"))
        self.assertTrue(hasattr(HBNCommand, "default"))
        self.assertTrue(hasattr(HBNCommand, "do_quit"))
        self.assertTrue(hasattr(HBNCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNCommand, "do_create"))
        self.assertTrue(hasattr(HBNCommand, "do_show"))
        self.assertTrue(hasattr(HBNCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNCommand, "do_all"))
        self.assertTrue(hasattr(HBNCommand, "do_update"))

    def test_isinstance(self):
        self.assertIsInstance(self.consol, HBNCommand)

    def test_create(self):
        self.assertFalse(cli.onecmd("create"))

if __name__ == "__main__":
    unittest.main()
