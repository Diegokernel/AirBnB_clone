#!/usr/bin/python3
'''Unittest for user'''
import unittest
from models.user import User
from unittest.mock import create_autospec, patch
from io import StringIO
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
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
