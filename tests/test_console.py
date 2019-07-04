#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.user import User
from unittest.mock import create_autospec, patch
from io import StringIO
from models import storage
from console import HBNBCommand
from datetime import datetime
import os

class test_console(unittest.TestCase):
    '''Tests user class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.console1 = HBNBCommand()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.console1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_quit(self):
        with patch("sys.stdout", new=StringIO()) as filer:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as filer:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help(self):
        with patch("sys.stdout", new=StringIO()) as filer:
            self.assertFalse(HBNBCommand().onecmd("help"))

    def test_empty_line(self):
        with patch('sys.stdout', new=StringIO()) as filer:
            self.console1.onecmd("\n")
            self.assertEqual('', filer.getvalue())

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_show_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            testID = output.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as output:
            obj = storage.all()["BaseModel.{}".format(testID)]
            command = "BaseModel.show({})".format(testID)
            self.assertNotEqual(obj.__str__(), output.getvalue().strip())
            self.assertFalse(HBNBCommand().onecmd(command))

if __name__ == "__main__":
    unittest.main()
